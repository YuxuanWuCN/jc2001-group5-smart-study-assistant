import os
import streamlit as st
import httpx
import json
from neo4j import GraphDatabase
from streamlit_agraph import agraph, Node, Edge, Config 

# 🚨 Core fix: the page configuration must be the absolute first st. command!
st.set_page_config(page_title="Logic Quenching Bench | Intelligent Trap-Defence Tutor", layout="wide")

# ==========================================
# 1. Infrastructure configuration (ssc enabled)
# ==========================================
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "") 
NEO4J_URI = os.getenv("NEO4J_URI", "")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")

@st.cache_resource
def init_neo4j_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

try:
    driver = init_neo4j_driver()
except Exception as e:
    st.error(f"❌ Cannot connect to the cloud Neo4j database; please check the network or credentials: {e}")

# ==========================================
# 2. Core algorithm: industrial-grade all-purpose fuzzy graph retrieval engine
# ==========================================
def fetch_fuzzy_graph_from_neo4j(user_keyword):
    agraph_nodes = []
    agraph_edges = []
    node_set = set()
    
    logic_statements = [] 
    
    color_map = {
        "Core concept": "#3498db",  
        "Theorem condition": "#2ecc71",  
        "Common-error blind spot": "#e74c3c",  
        "Computational operation": "#f39c12"   
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
            s_type = record["source_type"] or "Core concept"
            s_color = color_map.get(s_type, "#95a5a6")
            
            if s_name not in node_set:
                agraph_nodes.append(Node(id=s_name, label=s_name, color=s_color, size=15, font={"color": "white"}))
                node_set.add(s_name)
                
            t_name = record["target_name"]
            t_type = record["target_type"] or "Associated concept"
            t_color = color_map.get(t_type, "#95a5a6")
            rel_type = record["relation_type"] or "Logical association"
            
            if t_name:
                if t_name not in node_set:
                    agraph_nodes.append(Node(id=t_name, label=t_name, color=t_color, size=15, font={"color": "white"}))
                    node_set.add(t_name)
                
                agraph_edges.append(Edge(source=s_name, target=t_name, label=rel_type, color="#7f8c8d", width=1, type="CURVE_SMOOTH"))
                
                logic_statements.append(f"[{s_name}] -> {rel_type} -> [{t_name}]")
                
    return {"nodes": agraph_nodes, "edges": agraph_edges, "raw_logic": logic_statements}

# ==========================================
# 3. Bio-inspired Socratic intelligent dialogue engine
# ==========================================
def call_socrates_chat(messages, graph_context):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
    
    graph_info = ""
    if graph_context and "raw_logic" in graph_context:
        graph_info = "\n".join(graph_context["raw_logic"])
    
    system_prompt = f"""
    You are a stern, profound and highly illuminating [Socratic intelligent tutor].
    You must never tell the student the answer directly. Your sole task is to use the [deterministic subject-topology facts supplied below by the Neo4j graph database] to keep asking follow-up questions and setting checkpoints, cornering the student relentlessly until you have dug out and locked down every logical hole and unmastered point.

    [Absolute facts currently locked in the graph database]:
    {graph_info}

    [Iron commands for the dialogue]:
    1. Cling tightly to the "prerequisites" and "common-error blind spots" in the graph.
    2. If the student's concepts are vague, if they answer by intuition, or if they misremember a formula, point it out at once in a stern academic tone and throw out a concrete fill-in-the-blank question to force them to think.
    3. Be incisive; keep every reply within 150 words, and force the student to keep engaging with you.
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
# 4. Streamlit front-end interaction UI orchestration
# ==========================================
st.title("🧠 Logic Quenching Bench | GraphRAG Intelligent Tutor Engine")
st.caption("Project capability: all-subject target-range data ingestion | cross-network incremental graph weaving | topological causal lock-in drive")
st.markdown("---")

col_left, col_right = st.columns([1.1, 0.9])

with col_right:
    st.subheader("🗺️ Knowledge topology referenced by the current diagnosis")
    search_keyword = st.text_input(
        "🔍 Step 1: enter a subject keyword you want to study to trigger pathfinding:", 
        value="voltage",  # Default changed to a physics term present in the test set, to avoid an immediate error
        placeholder="e.g. voltage, cell, algorithm, right..."
    )
    
    graph_data = fetch_fuzzy_graph_from_neo4j(search_keyword)
    
    if graph_data and len(graph_data["nodes"]) > 0:
        st.success(f"🔗 Successfully fuzzy-matched and bidirectionally traced {len(graph_data['nodes'])} cross-disciplinary logic operators from Neo4j!")
        
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
        st.error(f'🚨 Fuzzy matching found no node containing "{search_keyword}"! Please try another word (e.g. cell, voltage, algorithm).')
        graph_data = {"nodes": [], "edges": [], "raw_logic": []}

with col_left:
    st.subheader("💬 Tutoring area")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f'Hello, I am your intelligent tutor. I have retrieved the underlying causal logic chain for "{search_keyword}". Please explain your understanding of this examination point, or paste in the question you got wrong, and I will dig out your logical holes on the spot!'}
        ]
        
    if st.session_state.get("last_keyword") != search_keyword:
        st.session_state.last_keyword = search_keyword
        st.session_state.messages = [
            {"role": "assistant", "content": f'The subject target range has been switched for you! I have retrieved the underlying logic chain for "{search_keyword}". Please explain your understanding of this theorem or the error you hit, and prepare for my logical interrogation!'}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_reply := st.chat_input("Explain your understanding or the error you hit to the tutor..."):
        st.session_state.messages.append({"role": "user", "content": user_reply})
        with st.chat_message("user"):
            st.write(user_reply)
            
        with st.chat_message("assistant"):
            with st.spinner("The tutor is examining your logical holes..."):
                response_text = call_socrates_chat(st.session_state.messages, graph_data)
                st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
