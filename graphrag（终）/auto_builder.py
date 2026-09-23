import pandas as pd
import httpx
import json
import re
import os
import glob
import time
import random
from tqdm import tqdm
from neo4j import GraphDatabase
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==========================================
# 1. 核心基建配置
# ==========================================
DASHSCOPE_API_KEY = "sk-294bcfe0ecc9403c975dcaf411f9080c" 
NEO4J_URI = "neo4j+ssc://5f97bf4d.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "JEGZu0b0z6qKT4T29YcOgn8b1RcP333EPmPt1xgI0-Y"

# 🚀 并发引擎配置：5个线程同时向阿里云发请求
MAX_WORKERS = 5 

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# ==========================================
# 2. 动态错题分析内核 (带防限流退避)
# ==========================================
def analyze_question_and_extract_trap(subject_name: str, question_text: str, retries=4) -> dict:
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
    
    prompt = f"""
    你是一个极其苛刻的【学术命题与逻辑诊断专家】。请分析下面这道来自【{subject_name}】真实测试集的题目：
    \"\"\"{question_text}\"\"\"
    
    【核心任务】：不要解答！诊断它考察的核心考点是什么？人类或AI解题时最容易掉进哪个逻辑陷阱、边界条件盲区或概念混淆点？
    
    【提取死命令】：
    1. 提取1个【核心考点】节点，和1个【易错漏洞】节点。
    2. 严格按照下方的JSON模版输出，不要带任何解释。
    
    {{
      "nodes": [
        {{"name": "简短核心考点名", "type": "核心考点", "detail": "严格适用条件或核心定义"}},
        {{"name": "简短陷阱名", "type": "易错漏洞", "detail": "具体的排雷指南、反例或数据约束规则（限100字内）"}}
      ],
      "edges": [
        {{"source": "简短核心考点名", "target": "简短陷阱名", "relation": "易错于"}}
      ]
    }}
    """
    
    payload = {"model": "qwen-turbo", "input": {"messages": [{"role": "user", "content": prompt}]}, "parameters": {"result_format": "message"}}
    
    for attempt in range(retries):
        try:
            response = httpx.post(url, json=payload, headers=headers, timeout=40.0)
            if response.status_code == 429: # 触发 API 限流
                time.sleep(2 ** attempt + random.random()) # 指数退避休息
                continue
                
            raw_content = response.json()["output"]["choices"][0]["message"]["content"]
            match = re.search(r'(\{.*\})', raw_content.replace("```json", "").replace("```", "").strip(), re.DOTALL)
            return json.loads(match.group(1)) if match else json.loads(raw_content)
        except Exception:
            time.sleep(1)
    return None

# ==========================================
# 3. 追加写入图数据库引擎 (线程安全)
# ==========================================
def write_to_neo4j(data: dict):
    if not data or "nodes" not in data or "edges" not in data: return
    # driver.session() 在多线程下是安全的，每个线程自己开闭 session
    with driver.session() as session:
        for node in data["nodes"]:
            session.run("""
                MERGE (c:Concept {name: $name}) 
                ON CREATE SET c.type = $type, c.detail = $detail
                ON MATCH SET c.detail = CASE 
                    WHEN c.detail CONTAINS $detail THEN c.detail 
                    ELSE c.detail + ' | 补充陷阱: ' + $detail 
                END
            """, name=node["name"], type=node["type"], detail=node.get("detail", "无"))
        for edge in data["edges"]:
            session.run("""
            MATCH (n:Concept {name: $source}), (m:Concept {name: $target})
            MERGE (n)-[r:DEPENDS_ON {type: $relation}]->(m)
            """, source=edge["source"], target=edge["target"], relation=edge["relation"])

# ==========================================
# 4. 单条数据处理原子任务
# ==========================================
def process_single_row(subject, q_text):
    if len(q_text) > 10:
        data = analyze_question_and_extract_trap(subject, q_text)
        if data:
            write_to_neo4j(data)

# ==========================================
# 5. 主程序：全胜靶场建图流水线
# ==========================================
if __name__ == "__main__":
    print("🚀 [极速并发模式] 启动！开启 5 线程引擎对 12 大学科进行高强度织网...")
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("🧹 图谱旧数据已彻底清空。")

    TARGET_FILES = [
        "high_school_physics_test.csv", "high_school_us_history_test.csv",
        "high_school_biology_test.csv", "high_school_computer_science_test.csv",
        "human_aging_test.csv", "world_religions_test.csv",
        "electrical_engineering_test.csv", "econometrics_test.csv",
        "professional_law_test.csv", "public_relations_test.csv",
        "miscellaneous_test.csv", "professional_psychology_test.csv"
    ]
    
    all_csvs = glob.glob("*.csv")
    csv_files = [f for f in all_csvs if f in TARGET_FILES]
    
    if not csv_files:
        print("❌ 未找到指定的测试集文件，请检查文件名！")
        exit()

    SAMPLE_SIZE = 100 

    for filepath in csv_files:
        clean_name = filepath.replace(".csv", "").replace("_test", "").replace("theoremqa_", "").replace("mmlu_", "").replace("benchmark_", "")
        subject = clean_name.replace("_", " ").title()
        
        print(f"\n📖 [多线程吞噬] 正在极速提炼学科 ───> 【{subject}】")
        
        try:
            # 🤖 终极防弹数据读取
            df = pd.read_csv(filepath)
            df.columns = [str(c).strip() for c in df.columns]

            q_col_name = None
            for col in df.columns:
                if col.lower() in ['question', '题目', 'content', 'text']:
                    q_col_name = col
                    break

            if q_col_name:
                df = df.rename(columns={q_col_name: 'Question'})
                if 'A' in df.columns and 'B' in df.columns:
                    df['Question'] = df.apply(lambda r: f"{r.get('Question','')}\nA: {r.get('A','')}\nB: {r.get('B','')}\nC: {r.get('C','')}\nD: {r.get('D','')}", axis=1)
            else:
                df = pd.read_csv(filepath, header=None)
                if len(df.columns) >= 5:
                    df['Question'] = df.apply(lambda r: f"{r.get(0,'')}\nA: {r.get(1,'')}\nB: {r.get(2,'')}\nC: {r.get(3,'')}\nD: {r.get(4,'')}", axis=1)
                elif len(df.columns) >= 1:
                    df['Question'] = df[0]

            if 'Question' not in df.columns:
                print(f"  ⚠️ 警告: {filepath} 中找不到任何题目数据，已安全跳过！")
                continue
                
            sample_df = df.head(SAMPLE_SIZE)
            
            # 🚀 启动多线程并发池
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = [executor.submit(process_single_row, subject, str(row.get('Question', ''))) for _, row in sample_df.iterrows()]
                
                # 配合 tqdm 刷新进度条
                for _ in tqdm(as_completed(futures), total=len(futures), desc=f"{subject}"):
                    pass
                    
        except Exception as e:
            print(f"  ❌ 跳过文件 {filepath}: 发生未知错误 {e}")

    print("\n🌟 全胜霸榜 12 科极速图谱已成功烙印在 Neo4j 云端！")