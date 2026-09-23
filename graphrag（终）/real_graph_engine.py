import streamlit as st
import httpx
import json
from neo4j import GraphDatabase
from streamlit_agraph import agraph, Node, Edge, Config 

# 🚨 核心修复：网页配置必须放在所有 st. 命令的绝对第一行！
st.set_page_config(page_title="逻辑淬火台 | 智能排雷导师", layout="wide")

# ==========================================
# 1. 基建配置 (已开启 ssc)
# ==========================================
DASHSCOPE_API_KEY = "sk-294bcfe0ecc9403c975dcaf411f9080c" 
NEO4J_URI = "neo4j+ssc://5f97bf4d.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "JEGZu0b0z6qKT4T29YcOgn8b1RcP333EPmPt1xgI0-Y"

@st.cache_resource
def init_neo4j_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

try:
    driver = init_neo4j_driver()
except Exception as e:
    st.error(f"❌ 无法连接到云端 Neo4j 数据库，请检查网络或凭证: {e}")

# ==========================================
# 2. 核心算法：工业级全能模糊图谱捞取引擎
# ==========================================
def fetch_fuzzy_graph_from_neo4j(user_keyword):
    agraph_nodes = []
    agraph_edges = []
    node_set = set()
    
    logic_statements = [] 
    
    color_map = {
        "核心考点": "#3498db",  
        "定理条件": "#2ecc71",  
        "易错漏洞": "#e74c3c",  
        "计算操作": "#f39c12"   
    }
    
    cypher_query = """
    MATCH (n:Concept)
    WHERE n.name CONTAINS $keyword
    OPTIONAL MATCH (n)-[r:DEPENDS_ON]-(m:Concept)
    RETURN n.name AS source_name, n.type AS source_type,
           m.name AS target_name, m.type AS target_type,
           r.type AS relation_type
    LIMIT 40
    """
    
    with driver.session() as session:
        result = session.run(cypher_query, keyword=user_keyword)
        records = list(result)
        
        if not records:
            return None
            
        for record in records:
            s_name = record["source_name"]
            s_type = record["source_type"] or "核心概念"
            s_color = color_map.get(s_type, "#95a5a6")
            
            if s_name not in node_set:
                agraph_nodes.append(Node(id=s_name, label=s_name, color=s_color, size=15, font={"color": "white"}))
                node_set.add(s_name)
                
            t_name = record["target_name"]
            t_type = record["target_type"] or "关联概念"
            t_color = color_map.get(t_type, "#95a5a6")
            rel_type = record["relation_type"] or "逻辑关联"
            
            if t_name:
                if t_name not in node_set:
                    agraph_nodes.append(Node(id=t_name, label=t_name, color=t_color, size=15, font={"color": "white"}))
                    node_set.add(t_name)
                
                agraph_edges.append(Edge(source=s_name, target=t_name, label=rel_type, color="#7f8c8d", width=1, type="CURVE_SMOOTH"))
                
                logic_statements.append(f"[{s_name}] -> {rel_type} -> [{t_name}]")
                
    return {"nodes": agraph_nodes, "edges": agraph_edges, "raw_logic": logic_statements}

# ==========================================
# 3. 仿生苏格拉底智能对话引擎
# ==========================================
def call_socrates_chat(messages, graph_context):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
    
    graph_info = ""
    if graph_context and "raw_logic" in graph_context:
        graph_info = "\n".join(graph_context["raw_logic"])
    
    system_prompt = f"""
    你是一个严厉、深刻、极具启发性的【苏格拉底式智能导师】。
    你绝不能直接告诉学生答案。你的唯一任务是根据下方【Neo4j 图数据库提供的确定性学科拓扑事实】，连续追问、设卡，死卡学生的脖子，直到彻底扒出并锁死学生的逻辑漏洞和未掌握点！
    
    【当前锁定的图数据库绝对事实】：
    {graph_info}
    
    【对话死命令】：
    1. 紧紧咬住图谱里的“前置条件”和“易错盲区”。
    2. 如果学生的概念模糊、用直觉做题、或公式记错，立刻用严厉的学术口吻指出，并抛出具体的填空问题逼他思考。
    3. 说话要一针见血，每次回答字数控制在 150 字以内，逼学生不断和你对线。
    """
    
    formatted_messages = [{"role": "system", "content": system_prompt}]
    for msg in messages:
        formatted_messages.append({"role": msg["role"], "content": msg["content"]})
        
    payload = {
        "model": "qwen-turbo",
        "input": {"messages": formatted_messages},
        "parameters": {"result_format": "message"}
    }
    
    response = httpx.post(url, json=payload, headers=headers, timeout=30.0).json()
    return response["output"]["choices"][0]["message"]["content"]

# ==========================================
# 4. Streamlit 前端交互 UI 编排
# ==========================================
st.title("🧠 逻辑淬火台 | GraphRAG 智能导师引擎")
st.caption("项目功能：全学科靶场数据吞噬 | 跨网增量织网 | 拓扑图谱因果锁死驱动")
st.markdown("---")

col_left, col_right = st.columns([1.1, 0.9])

with col_right:
    st.subheader("🗺️ 当前诊断参考的知识拓扑")
    search_keyword = st.text_input(
        "🔍 第一步：输入你想学习的学科关键词触发寻路：", 
        value="电压",  # 默认值已修改为你测试集里包含的物理词汇，防止开局报错
        placeholder="例如：电压、细胞、算法、权利..."
    )
    
    graph_data = fetch_fuzzy_graph_from_neo4j(search_keyword)
    
    if graph_data and len(graph_data["nodes"]) > 0:
        st.success(f"🔗 成功从 Neo4j 模糊匹配并双向溯源到 {len(graph_data['nodes'])} 个跨学科逻辑算子！")
        
        config = Config(
            width="100%",
            height=550, 
            directed=True, 
            physics=True, 
            hierarchical=False,
            nodeHighlightBehavior=True,
            highlightColor="#F7A7A6",
            collapsible=False
        )
        agraph(nodes=graph_data["nodes"], edges=graph_data["edges"], config=config)
    else:
        st.error(f"🚨 模糊匹配未查到包含“{search_keyword}”的节点！请换个词试试（如：细胞，电压，算法等）。")
        graph_data = {"nodes": [], "edges": [], "raw_logic": []}

with col_left:
    st.subheader("💬 教学指导区域")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"你好，我是你的智能导师。我已经调出了关于“{search_keyword}”的底层因果逻辑链。请阐述你对该考点的理解，或者直接贴出你的错题，我来现场扒出你的逻辑漏洞！"}
        ]
        
    if st.session_state.get("last_keyword") != search_keyword:
        st.session_state.last_keyword = search_keyword
        st.session_state.messages = [
            {"role": "assistant", "content": f"已经为你切换学科靶场！我已经调出了关于“{search_keyword}”的底层逻辑链。请阐述你对该定理的理解或报错情况，准备接受我的逻辑盘问！"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_reply := st.chat_input("向导师阐述你的理解或报错情况..."):
        st.session_state.messages.append({"role": "user", "content": user_reply})
        with st.chat_message("user"):
            st.write(user_reply)
            
        with st.chat_message("assistant"):
            with st.spinner("导师正在透视你的逻辑漏洞..."):
                response_text = call_socrates_chat(st.session_state.messages, graph_data)
                st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})