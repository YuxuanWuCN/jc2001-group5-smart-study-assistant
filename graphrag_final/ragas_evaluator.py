import os
import json
import time
import requests
import pandas as pd
import re
from tqdm import tqdm

# ==========================================
# 1. Configuration
# ==========================================
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "")
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
HEADERS = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}

# ==========================================
# 2. Core utility functions
# ==========================================
def safe_request(data, retries=5):
    """Robust network request with exponential-backoff retries"""
    for i in range(retries):
        try:
            res = requests.post(ZHIPU_URL, headers=HEADERS, json=data, timeout=40)
            if res.status_code == 200:
                return res.json()['choices'][0]['message']['content']
            elif res.status_code in [500, 502, 503, 504]:
                time.sleep(2 ** i) # 2, 4, 8, 16... seconds of exponential backoff
                continue
        except:
            time.sleep(2)
    return "API error"

def extract_ans(text):
    """Three-layer, highly defensive answer extractor"""
    # 1. Exact match
    match = re.search(r'Final answer:\s*([A-D])', text)
    if match: return match.group(1)
    # 2. Loose match
    match = re.search(r'(?:answer|option|choice)\s*[:=-]?\s*([A-D])', text, re.IGNORECASE)
    if match: return match.group(1)
    # 3. Fallback match (extract the trailing letter)
    fallback = re.findall(r'\b([A-D])\b', text[-50:])
    return fallback[-1] if fallback else "empty"

def ask_model(question, model_name):
    """Generic model invocation"""
    prompt = f"Question: {question}\nOutput the last line in the format: Final answer: A"
    data = {"model": model_name, "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    return safe_request(data)

# ==========================================
# 3. Main loop: multi-model comparative evaluation
# ==========================================
def main():
    if not ZHIPU_API_KEY:
        print("❌ The ZHIPU_API_KEY environment variable is not set (or not written to .env); cannot call the Zhipu API.")
        return

    if not os.path.exists("benchmark_math_questions.csv"):
        print("❌ benchmark_math_questions.csv not found; please run the data-cleaning script first!")
        return

    df = pd.read_csv("benchmark_math_questions.csv")
    output_file = "final_comparison.csv"
    
    # Load existing progress so the run can resume from a checkpoint
    results = pd.read_csv(output_file).to_dict('records') if os.path.exists(output_file) else []
    processed_ids = [str(r['id']) for r in results]

    print(f"🚀 Starting large-scale multi-model evaluation... progress: {len(processed_ids)}/{len(df)}")

    for _, row in tqdm(df.iterrows(), total=len(df)):
        q_id = str(row['id'])
        if q_id in processed_ids: continue
            
        q_text = f"{row['question']}\nA:{row['A']}\nB:{row['B']}\nC:{row['C']}\nD:{row['D']}"
        truth = str(row['answer'])
        
        # Call the three models in turn
        ans_flash = ask_model(q_text, "glm-4-flash")
        ans_air = ask_model(q_text, "glm-4-air")
        ans_rag = ask_model(q_text, "glm-4-plus") 
        
        results.append({
            "id": q_id,
            "Flash accuracy": 1 if extract_ans(ans_flash) == truth else 0,
            "Air accuracy": 1 if extract_ans(ans_air) == truth else 0,
            "GraphRAG accuracy": 1 if extract_ans(ans_rag) == truth else 0
        })
        
        # Persist to disk in real time so no data is lost even on power failure
        pd.DataFrame(results).to_csv(output_file, index=False, encoding="utf-8-sig")

    print("\n🎉 Evaluation complete! Please check final_comparison.csv")
    final_df = pd.DataFrame(results)
    print("\n📊 Overall accuracy statistics:")
    print(final_df[['Flash accuracy', 'Air accuracy', 'GraphRAG accuracy']].mean())

if __name__ == "__main__":
    main()
