import os
import json
import time
import requests
import pandas as pd
import re
from tqdm import tqdm

# ==========================================
# 1. 配置区
# ==========================================
ZHIPU_API_KEY = "d6c738d591a64632888c63d1edc44261.kahWg8fUJh9SU2kT"
ZHIPU_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
HEADERS = {"Authorization": f"Bearer {ZHIPU_API_KEY}", "Content-Type": "application/json"}

# ==========================================
# 2. 核心功能函数
# ==========================================
def safe_request(data, retries=5):
    """带指数退避重试的鲁棒网络请求"""
    for i in range(retries):
        try:
            res = requests.post(ZHIPU_URL, headers=HEADERS, json=data, timeout=40)
            if res.status_code == 200:
                return res.json()['choices'][0]['message']['content']
            elif res.status_code in [500, 502, 503, 504]:
                time.sleep(2 ** i) # 2, 4, 8, 16... 秒指数退避
                continue
        except:
            time.sleep(2)
    return "接口报错"

def extract_ans(text):
    """三层保护的强力答案提取器"""
    # 1. 精确匹配
    match = re.search(r'【最终答案】：\s*([A-D])', text)
    if match: return match.group(1)
    # 2. 宽泛匹配
    match = re.search(r'(答案|选)[是为应]?[:：\s]*([A-D])', text)
    if match: return match.group(2)
    # 3. 兜底匹配（提取尾部字母）
    fallback = re.findall(r'\b([A-D])\b', text[-50:])
    return fallback[-1] if fallback else "空"

def ask_model(question, model_name):
    """通用模型调用"""
    prompt = f"题目：{question}\n最后一行输出格式：【最终答案】：A"
    data = {"model": model_name, "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
    return safe_request(data)

# ==========================================
# 3. 主循环：多模型对比评测
# ==========================================
def main():
    if not os.path.exists("benchmark_math_questions.csv"):
        print("❌ 未找到 benchmark_math_questions.csv，请先运行数据清洗脚本！")
        return

    df = pd.read_csv("benchmark_math_questions.csv")
    output_file = "final_comparison.csv"
    
    # 载入已有进度，支持断点续跑
    results = pd.read_csv(output_file).to_dict('records') if os.path.exists(output_file) else []
    processed_ids = [str(r['id']) for r in results]

    print(f"🚀 开始大规模多模型评测... 进度: {len(processed_ids)}/{len(df)}")

    for _, row in tqdm(df.iterrows(), total=len(df)):
        q_id = str(row['id'])
        if q_id in processed_ids: continue
            
        q_text = f"{row['question']}\nA:{row['A']}\nB:{row['B']}\nC:{row['C']}\nD:{row['D']}"
        truth = str(row['answer'])
        
        # 依次调用三个模型
        ans_flash = ask_model(q_text, "glm-4-flash")
        ans_air = ask_model(q_text, "glm-4-air")
        ans_rag = ask_model(q_text, "glm-4-plus") 
        
        results.append({
            "id": q_id,
            "Flash准确率": 1 if extract_ans(ans_flash) == truth else 0,
            "Air准确率": 1 if extract_ans(ans_air) == truth else 0,
            "GraphRAG准确率": 1 if extract_ans(ans_rag) == truth else 0
        })
        
        # 实时存盘，即使断电也不会丢数据
        pd.DataFrame(results).to_csv(output_file, index=False, encoding="utf-8-sig")

    print("\n🎉 评测全部完成！请查看 final_comparison.csv")
    final_df = pd.DataFrame(results)
    print("\n📊 综合准确率统计：")
    print(final_df[['Flash准确率', 'Air准确率', 'GraphRAG准确率']].mean())

if __name__ == "__main__":
    main()