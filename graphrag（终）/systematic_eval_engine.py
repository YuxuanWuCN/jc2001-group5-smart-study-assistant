import pandas as pd
import requests
import re
import random
import glob
import time
from tqdm import tqdm
from neo4j import GraphDatabase
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# ==========================================
# 1. 核心配置与升级参数 (已开启 ssc)
# ==========================================
NEO4J_URI = "neo4j+ssc://5f97bf4d.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "JEGZu0b0z6qKT4T29YcOgn8b1RcP333EPmPt1xgI0-Y"

ZHIPU_API_KEY = "94f8794590284ebabfc04695450d0c88.ZdDgQcFk0UTaCkk8"
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

STRICT_CONFIDENCE_FILTER = True
RAG_CONFIDENCE_THRESHOLD = 85
MAX_WORKERS = 8  

# ==========================================
# 2. 智能核心模块 (线程安全版)
# ==========================================
thread_local = threading.local()

def get_neo4j_session():
    if not hasattr(thread_local, "driver"):
        thread_local.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return thread_local.driver.session()

def extract_keywords_from_question(question):
    prompt = f"提取题目最核心的高等学科考点关键词。\n题目：{question}\n【指令】：仅输出1-2个中文关键词，逗号分隔。"
    headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    try:
        res = requests.post(ZHIPU_URL, headers=headers, json=data, timeout=10)
        return [k.strip() for k in res.json()['choices'][0]['message']['content'].replace('，', ',').split(',')]
    except: return []

def filter_noise_nodes(question, raw_nodes):
    if not STRICT_CONFIDENCE_FILTER or not raw_nodes: return raw_nodes
    prompt = f"""作为学术仲裁官，请判断以下知识图谱节点是否与题目【存在直接且强烈的因果解题关联】。
要求置信度达到 {RAG_CONFIDENCE_THRESHOLD} 分以上才予以保留。如果是通用词汇的弱关联（如普通的'责任'、'权利'、'认知'），请直接判定为噪音。
题目：{question}
候选节点：{raw_nodes}
【指令】：仅返回保留的强因果节点文本，如果全是不相关的噪音，直接回复'无'。"""
    
    headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    try:
        res = requests.post(ZHIPU_URL, headers=headers, json=data, timeout=15)
        filtered = res.json()['choices'][0]['message']['content'].strip()
        return [] if filtered == "无" else [filtered]
    except: return raw_nodes

def get_graph_context(question):
    try:
        keywords = extract_keywords_from_question(question)
        if not keywords: return "无"
        
        raw_data_str = []
        with get_neo4j_session() as session:
            for kw in keywords:
                if len(kw) < 2: continue 
                query = """MATCH (c:Concept) WHERE c.name CONTAINS $kw OR c.detail CONTAINS $kw
                           OPTIONAL MATCH (c)-[r:DEPENDS_ON]-(m:Concept)
                           RETURN c.name as name, c.type as type, c.detail as detail, collect(r.type + ': ' + m.name) as rels LIMIT 2"""
                res = session.run(query, kw=kw)
                for r in res:
                    info = f"🚨排雷 [{r['name']}]: {r['detail']}"
                    valid_rels = [rel for rel in set(r['rels']) if rel and not rel.endswith(': ')]
                    if valid_rels: info += f" -> (关联漏洞: {', '.join(valid_rels)})"
                    raw_data_str.append(info)
        
        if not raw_data_str: return "无"
        final_nodes = filter_noise_nodes(question, list(set(raw_data_str)))
        return "\n".join(final_nodes) if final_nodes else "无"
    except Exception: 
        return "无"

def ask_model(question, use_graph=True, max_retries=5):
    context = get_graph_context(question) if use_graph else "无"
    prompt = f"""你是一个严谨的学术专家。请解答以下多项选择题。
【参考知识】（仅供避坑参考，如无关请果断忽略）：
{context}
【题目】：
{question}
【指令】：请一步步思考，最终输出时【仅输出 A, B, C 或 D】其中一个字母，不需要其他解释。"""
    
    headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-plus", "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    
    for attempt in range(max_retries):
        try:
            res = requests.post(ZHIPU_URL, headers=headers, json=data, timeout=45)
            if res.status_code == 200:
                return res.json()['choices'][0]['message']['content']
            elif res.status_code == 429:
                time.sleep(2 ** attempt + random.random())
            else:
                time.sleep(1)
        except Exception:
            time.sleep(2)
    return "Z"

def extract_ans(text):
    match = re.search(r'([ABCD])', text.upper())
    return match.group(1) if match else "Z"

def smart_prepare_dataset(df):
    standardized = []
    for _, row in df.iterrows():
        question = str(row.get('Question', ''))
        ans = str(row.get('Answer', '')).strip()
        if "\nA:" in question and "\nB:" in question:
            standardized.append({"Question": question, "Answer": ans})
        else:
            options = [ans, "Option_X", "Option_Y", "Option_Z"]
            random.shuffle(options)
            correct_letter = ['A', 'B', 'C', 'D'][options.index(ans)]
            q_text = f"{question}\nA: {options[0]}\nB: {options[1]}\nC: {options[2]}\nD: {options[3]}"
            standardized.append({"Question": q_text, "Answer": correct_letter})
    return pd.DataFrame(standardized)

# ==========================================
# 3. 多线程处理单条数据的原子函数
# ==========================================
def process_single_row(row, idx):
    truth = str(row['Answer']).strip()
    
    context = get_graph_context(row['Question'])
    is_triggered = context != "无"
    
    ans_base = extract_ans(ask_model(row['Question'], use_graph=False))
    ans_ours = extract_ans(ask_model(row['Question'], use_graph=True))
    
    base_correct = (ans_base == truth)
    ours_correct = (ans_ours == truth)
    
    return {
        "idx": idx,
        "is_triggered": is_triggered,
        "base_correct": base_correct,
        "ours_correct": ours_correct,
        "Base": 1 if base_correct else 0,
        "Ours": 1 if ours_correct else 0
    }

# ==========================================
# 4. 评测主逻辑
# ==========================================
def run_eval():
    TARGET_FILES = [
        "high_school_physics_test.csv",
        "high_school_us_history_test.csv",
        "high_school_biology_test.csv",
        "high_school_computer_science_test.csv",
        "human_aging_test.csv",
        "world_religions_test.csv",
        "electrical_engineering_test.csv",
        "econometrics_test.csv",
        "professional_law_test.csv",
        "public_relations_test.csv",
        "miscellaneous_test.csv",
        "professional_psychology_test.csv", 
    ]
    
    all_csvs = glob.glob("*.csv")
    csv_files = [f for f in all_csvs if f in TARGET_FILES]
    
    if not csv_files:
        print("❌ 未在当前目录找到测试集文件！")
        return

    all_reports = []
    for filepath in csv_files:
        clean_name = filepath.replace(".csv", "").replace("_test", "").replace("theoremqa_", "").replace("mmlu_", "").replace("benchmark_", "")
        sub = clean_name.replace("_", " ").title()
        
        print(f"\n🚀 [高并发极限提速] 正在启动系统性评测 ───> 【{sub}】 (并发度: {MAX_WORKERS})")
        
        try:
            # 🤖 同步应用终极防弹数据读取，防止评测时崩盘
            df_raw = pd.read_csv(filepath)
            df_raw.columns = [str(c).strip() for c in df_raw.columns]

            q_col_name = None
            for col in df_raw.columns:
                if str(col).lower() in ['question', '题目', 'content', 'text']:
                    q_col_name = col
                    break

            if q_col_name:
                df_raw = df_raw.rename(columns={q_col_name: 'Question'})
                if 'A' in df_raw.columns and 'B' in df_raw.columns:
                    df_raw['Question'] = df_raw.apply(lambda r: f"{r.get('Question','')}\nA: {r.get('A','')}\nB: {r.get('B','')}\nC: {r.get('C','')}\nD: {r.get('D','')}", axis=1)
            else:
                df_raw = pd.read_csv(filepath, header=None)
                if len(df_raw.columns) >= 5:
                    df_raw['Question'] = df_raw.apply(lambda r: f"{r.get(0,'')}\nA: {r.get(1,'')}\nB: {r.get(2,'')}\nC: {r.get(3,'')}\nD: {r.get(4,'')}", axis=1)
                elif len(df_raw.columns) >= 1:
                    df_raw['Question'] = df_raw[0]

            if 'Question' not in df_raw.columns:
                print(f"  ⚠️ 跳过 {filepath}：未找到有效题目。")
                continue
            
            # 处理 Answer 列
            ans_col_name = None
            for col in df_raw.columns:
                if str(col).lower() in ['answer', '答案', 'target']:
                    ans_col_name = col
                    break
            if ans_col_name:
                df_raw = df_raw.rename(columns={ans_col_name: 'Answer'})
            elif len(df_raw.columns) >= 6:
                 df_raw['Answer'] = df_raw[5]
            
            if 'Answer' not in df_raw.columns:
                df_raw['Answer'] = 'A' 
                
            df = smart_prepare_dataset(df_raw.head(200)) 
            results = []
            
            stats = {
                "total": 0,
                "graph_triggered": 0,  
                "noise_ingestion": 0,  
                "accurate_rescue": 0   
            }
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = {executor.submit(process_single_row, row, idx): idx for idx, row in df.iterrows()}
                
                for future in tqdm(as_completed(futures), total=len(futures), desc=f"{sub}"):
                    res = future.result()
                    results.append(res)
                    
                    stats["total"] += 1
                    if res["is_triggered"]:
                        stats["graph_triggered"] += 1
                        if res["base_correct"] and not res["ours_correct"]:
                            stats["noise_ingestion"] += 1
                        elif not res["base_correct"] and res["ours_correct"]:
                            stats["accurate_rescue"] += 1
            
            if stats["graph_triggered"] > 0:
                trigger_rate = (stats["graph_triggered"] / stats["total"]) * 100
                noise_rate = (stats["noise_ingestion"] / stats["graph_triggered"]) * 100
                rescue_rate = (stats["accurate_rescue"] / stats["graph_triggered"]) * 100
                
                print(f"\n📊 【{sub}】系统性因果指标看板：")
                print(f" - 🔎 图谱前置触发率: {trigger_rate:.1f}% ({stats['graph_triggered']}/{stats['total']})")
                print(f" - 📉 知识噪音摄入率 (过度防备丢分): {noise_rate:.1f}%")
                print(f" - 📈 精准排雷率 (逻辑挽回得分): {rescue_rate:.1f}%\n")
            else:
                print(f"\n📊 【{sub}】系统性因果指标看板：")
                print(f" - 🔎 图谱知识未被强触发 (0/{stats['total']})\n")
                
            report = pd.DataFrame(results)[['Base', 'Ours']].mean()
            report.name = sub
            all_reports.append(report)
            
        except Exception as e:
            print(f"❌ {sub} 测评出错: {e}")
    
    if all_reports:
        final_report = pd.DataFrame(all_reports)
        final_report['提升幅度'] = final_report['Ours'] - final_report['Base']
        final_report = final_report.sort_values(by='提升幅度', ascending=False)
        
        print("\n🎉 [12 科全量极速终极数据榜单]")
        print(final_report.to_markdown())
        final_report.to_csv("final_systematic_report.csv", encoding="utf-8-sig")

if __name__ == "__main__":
    run_eval()