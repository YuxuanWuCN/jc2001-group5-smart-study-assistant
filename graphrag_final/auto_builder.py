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
# 1. Core infrastructure configuration
# ==========================================
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "") 
NEO4J_URI = os.getenv("NEO4J_URI", "")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")

# 🚀 Concurrency engine configuration: 5 threads send requests to Alibaba Cloud simultaneously
MAX_WORKERS = 5 

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# ==========================================
# 2. Dynamic wrong-answer analysis kernel (with rate-limit backoff)
# ==========================================
def analyze_question_and_extract_trap(subject_name: str, question_text: str, retries=4) -> dict:
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
    
    prompt = f"""
    You are an exceptionally exacting [academic item-writing and logic-diagnosis expert]. Please analyse the following question from the real [{subject_name}] test set:
    \"\"\"{question_text}\"\"\"
    
    [Core task]: Do NOT solve it! Diagnose what core concept it tests. Which logical trap, boundary-condition blind spot or conceptual confusion point do humans or AI most easily fall into when answering it?
    
    [Iron extraction commands]:
    1. Extract 1 [Core concept] node and 1 [Common-error blind spot] node.
    2. Output strictly according to the JSON template below, with no extra explanation.
    
    {{
      "nodes": [
        {{"name": "short core-concept name", "type": "Core concept", "detail": "strict applicability conditions or core definition"}},
        {{"name": "short trap name", "type": "Common-error blind spot", "detail": "concrete trap-defence guidance, counter-example or data constraint rule (max 100 words)"}}
      ],
      "edges": [
        {{"source": "short core-concept name", "target": "short trap name", "relation": "Common error at"}}
      ]
    }}
    """
    
    payload = {"model": "qwen-turbo", "input": {"messages": [{"role": "user", "content": prompt}]}, "parameters": {"result_format": "message"}}
    
    for attempt in range(retries):
        try:
            response = httpx.post(url, json=payload, headers=headers, timeout=40.0)
            if response.status_code == 429: # API rate limit triggered
                time.sleep(2 ** attempt + random.random()) # exponential backoff rest
                continue
                
            raw_content = response.json()["output"]["choices"][0]["message"]["content"]
            match = re.search(r'(\{.*\})', raw_content.replace("```json", "").replace("```", "").strip(), re.DOTALL)
            return json.loads(match.group(1)) if match else json.loads(raw_content)
        except Exception:
            time.sleep(1)
    return None

# ==========================================
# 3. Append-only graph-database write engine (thread-safe)
# ==========================================
def write_to_neo4j(data: dict):
    if not data or "nodes" not in data or "edges" not in data: return
    # driver.session() is safe under multithreading; each thread opens and closes its own session
    with driver.session() as session:
        for node in data["nodes"]:
            session.run("""
                MERGE (c:Concept {name: $name}) 
                ON CREATE SET c.type = $type, c.detail = $detail
                ON MATCH SET c.detail = CASE 
                    WHEN c.detail CONTAINS $detail THEN c.detail 
                    ELSE c.detail + ' | Additional trap: ' + $detail 
                END
            """, name=node["name"], type=node["type"], detail=node.get("detail", "none"))
        for edge in data["edges"]:
            session.run("""
            MATCH (n:Concept {name: $source}), (m:Concept {name: $target})
            MERGE (n)-[r:DEPENDS_ON {type: $relation}]->(m)
            """, source=edge["source"], target=edge["target"], relation=edge["relation"])

# ==========================================
# 4. Atomic task for processing a single row
# ==========================================
def process_single_row(subject, q_text):
    if len(q_text) > 10:
        data = analyze_question_and_extract_trap(subject, q_text)
        if data:
            write_to_neo4j(data)

# ==========================================
# 5. Main program: all-subject target-range graph-building pipeline
# ==========================================
if __name__ == "__main__":
    print("🚀 [Turbo concurrency mode] Started! 5-thread engine now weaving the graph for 12 subjects at full intensity...")
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("🧹 Old graph data fully cleared.")

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
        print("❌ The specified test-set files were not found; please check the filenames!")
        exit()

    SAMPLE_SIZE = 100 

    for filepath in csv_files:
        clean_name = filepath.replace(".csv", "").replace("_test", "").replace("theoremqa_", "").replace("mmlu_", "").replace("benchmark_", "")
        subject = clean_name.replace("_", " ").title()
        
        print(f"\n📖 [Multithreaded ingestion] Rapidly distilling subject ───> [{subject}]")
        
        try:
            # 🤖 Ultimate bulletproof data reader
            df = pd.read_csv(filepath)
            df.columns = [str(c).strip() for c in df.columns]

            q_col_name = None
            for col in df.columns:
                if col.lower() in ['question', 'content', 'text', 'prompt']:
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
                print(f"  ⚠️ Warning: no question data found in {filepath}; safely skipped!")
                continue
                
            sample_df = df.head(SAMPLE_SIZE)
            
            # 🚀 Start the multithreaded concurrency pool
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = [executor.submit(process_single_row, subject, str(row.get('Question', ''))) for _, row in sample_df.iterrows()]
                
                # Refresh the progress bar in step with tqdm
                for _ in tqdm(as_completed(futures), total=len(futures), desc=f"{subject}"):
                    pass
                    
        except Exception as e:
            print(f"  ❌ Skipping file {filepath}: unexpected error {e}")

    print("\n🌟 The turbo graph for all 12 top-scoring subjects has been successfully branded onto the Neo4j cloud!")
