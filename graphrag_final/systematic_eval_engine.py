import os
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
# 1. Core configuration and upgrade parameters (ssc enabled)
# ==========================================
NEO4J_URI = os.getenv("NEO4J_URI", "")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")

ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "")
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

STRICT_CONFIDENCE_FILTER = True
RAG_CONFIDENCE_THRESHOLD = 85
MAX_WORKERS = 8  

# ==========================================
# 2. Intelligent core modules (thread-safe version)
# ==========================================
thread_local = threading.local()

def get_neo4j_session():
    if not hasattr(thread_local, "driver"):
        thread_local.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return thread_local.driver.session()

def extract_keywords_from_question(question):
    prompt = f"Extract the core higher-education examination-point keywords of the question.\nQuestion: {question}\n[Instruction]: Output only 1-2 keywords, comma-separated."
    headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    try:
        res = requests.post(ZHIPU_URL, headers=headers, json=data, timeout=10)
        return [k.strip() for k in res.json()['choices'][0]['message']['content'].split(',')]
    except: return []

def filter_noise_nodes(question, raw_nodes):
    if not STRICT_CONFIDENCE_FILTER or not raw_nodes: return raw_nodes
    prompt = f"""As an academic arbiter, judge whether each knowledge-graph node below has a [direct and strong causal relevance to solving] the question.
Only nodes whose confidence reaches {RAG_CONFIDENCE_THRESHOLD} or above may be retained. If a node is only weakly related through generic vocabulary (for example plain words such as 'liability', 'right' or 'cognition'), judge it to be noise.
Question: {question}
Candidate nodes: {raw_nodes}
[Instruction]: Return only the retained strongly causal node texts; if all of them are irrelevant noise, reply 'NONE'."""
    
    headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    try:
        res = requests.post(ZHIPU_URL, headers=headers, json=data, timeout=15)
        filtered = res.json()['choices'][0]['message']['content'].strip()
        return [] if filtered == "NONE" else [filtered]
    except: return raw_nodes

def get_graph_context(question):
    try:
        keywords = extract_keywords_from_question(question)
        if not keywords: return "NONE"
        
        raw_data_str = []
        with get_neo4j_session() as session:
            for kw in keywords:
                if len(kw) < 2: continue 
                query = """MATCH (c:Concept) WHERE c.name CONTAINS $kw OR c.detail CONTAINS $kw
                           OPTIONAL MATCH (c)-[r:DEPENDS_ON]-(m:Concept)
                           RETURN c.name as name, c.type as type, c.detail as detail, collect(r.type + ': ' + m.name) as rels LIMIT 2"""
                res = session.run(query, kw=kw)
                for r in res:
                    info = f"🚨Trap [{r['name']}]: {r['detail']}"
                    valid_rels = [rel for rel in set(r['rels']) if rel and not rel.endswith(': ')]
                    if valid_rels: info += f" -> (related blind spots: {', '.join(valid_rels)})"
                    raw_data_str.append(info)
        
        if not raw_data_str: return "NONE"
        final_nodes = filter_noise_nodes(question, list(set(raw_data_str)))
        return "\n".join(final_nodes) if final_nodes else "NONE"
    except Exception: 
        return "NONE"

def ask_model(question, use_graph=True, max_retries=5):
    context = get_graph_context(question) if use_graph else "NONE"
    prompt = f"""You are a rigorous academic expert. Please solve the following multiple-choice question.
[Reference knowledge] (for trap-avoidance reference only; ignore it decisively if irrelevant):
{context}
[Question]:
{question}
[Instruction]: Think step by step, and in your final output [output only one letter: A, B, C or D]; no other explanation is needed."""
    
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
# 3. Atomic function for multithreaded processing of a single row
# ==========================================
def process_single_row(row, idx):
    truth = str(row['Answer']).strip()
    
    context = get_graph_context(row['Question'])
    is_triggered = context != "NONE"
    
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
# 4. Main evaluation logic
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
        print("❌ No test-set files found in the current directory!")
        return

    all_reports = []
    for filepath in csv_files:
        clean_name = filepath.replace(".csv", "").replace("_test", "").replace("theoremqa_", "").replace("mmlu_", "").replace("benchmark_", "")
        sub = clean_name.replace("_", " ").title()
        
        print(f"\n🚀 [High-concurrency turbo mode] Starting systematic evaluation ───> [{sub}] (concurrency: {MAX_WORKERS})")
        
        try:
            # 🤖 Apply the ultimate bulletproof data reader in step, so evaluation cannot crash
            df_raw = pd.read_csv(filepath)
            df_raw.columns = [str(c).strip() for c in df_raw.columns]

            q_col_name = None
            for col in df_raw.columns:
                if str(col).lower() in ['question', 'content', 'text', 'prompt']:
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
                print(f"  ⚠️ Skipping {filepath}: no valid question found.")
                continue
            
            # Handle the Answer column
            ans_col_name = None
            for col in df_raw.columns:
                if str(col).lower() in ['answer', 'target', 'label']:
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
                
                print(f"\n📊 [{sub}] systematic causal metrics dashboard:")
                print(f" - 🔎 Graph prerequisite trigger rate: {trigger_rate:.1f}% ({stats['graph_triggered']}/{stats['total']})")
                print(f" - 📉 Knowledge-noise ingestion rate (points lost through over-caution): {noise_rate:.1f}%")
                print(f" - 📈 Precise trap-defence rate (points recovered by logic): {rescue_rate:.1f}%\n")
            else:
                print(f"\n📊 [{sub}] systematic causal metrics dashboard:")
                print(f" - 🔎 Graph knowledge not strongly triggered (0/{stats['total']})\n")
                
            report = pd.DataFrame(results)[['Base', 'Ours']].mean()
            report.name = sub
            all_reports.append(report)
            
        except Exception as e:
            print(f"❌ Evaluation error for {sub}: {e}")
    
    if all_reports:
        final_report = pd.DataFrame(all_reports)
        final_report['Improvement'] = final_report['Ours'] - final_report['Base']
        final_report = final_report.sort_values(by='Improvement', ascending=False)
        
        print("\n🎉 [Full 12-subject turbo final data leaderboard]")
        print(final_report.to_markdown())
        final_report.to_csv("final_systematic_report.csv", encoding="utf-8-sig")

if __name__ == "__main__":
    run_eval()
