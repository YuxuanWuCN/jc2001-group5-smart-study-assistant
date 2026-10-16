"""
Knowledge Service - Multi-Discipline Knowledge Graph and Concept Management
Integrates Year 2 Semester 1 ("大二上") curriculum ontologies with existing subjects.
"""

from typing import List, Dict, Optional
from backend.app.models.knowledge import SubjectMeta, ConceptDetail, KnowledgeGraphResponse, SubjectListResponse
from backend.app.models.quiz import GraphData, GraphNode, GraphEdge
from backend.app.data.daershang_knowledge import DAERSHANG_SUBJECTS, DAERSHANG_KNOWLEDGE_MAP
from backend.app.data.seed_questions import SEED_QUESTIONS

# Baseline 4 disciplines from existing seed questions
BASELINE_SUBJECTS: List[SubjectMeta] = [
    SubjectMeta(
        code="law",
        name="民商法学与民法典",
        name_en="Civil & Commercial Law",
        badge="基准核心",
        category="humanities",
        semester="通识法学",
        icon="⚖️",
        description="《民法典》撤销权除斥期间、动产善意取得制度与表见代理权利外观责任。"
    ),
    SubjectMeta(
        code="cs",
        name="计算机体系结构",
        name_en="Computer Architecture",
        badge="基准核心",
        category="stem",
        semester="专业基础",
        icon="💻",
        description="Amdahl定律加速比瓶颈、流水线结构/数据/控制冲突以及虚拟内存TLB分级缓存分页。"
    ),
    SubjectMeta(
        code="econ",
        name="计量经济学",
        name_en="Econometrics",
        badge="基准核心",
        category="business",
        semester="专业基础",
        icon="📈",
        description="高斯-马尔可夫定理BLUE估计、异方差性对OLS标准误影响以及内生性遗漏变量偏差与工具变量。"
    ),
    SubjectMeta(
        code="se",
        name="软件工程导论",
        name_en="Software Engineering",
        badge="JC2001课程核心",
        category="stem",
        semester="专业必修",
        icon="⚙️",
        description="瀑布与敏捷过程模型权衡、SOLID设计原则与依赖倒置(DIP)、边界值分析与变异测试杀伤率。"
    )
]

# Universal subject alias mapping
KNOWLEDGE_SUBJECT_ALIASES: Dict[str, str] = {
    # OR
    "or": "or",
    "operations_research": "or",
    "operations-research": "or",
    "运筹学": "or",
    "运筹": "or",
    "规划建模": "or",

    # MIS
    "mis": "mis",
    "management_information_systems": "mis",
    "management-information-systems": "mis",
    "管理信息系统": "mis",
    "信管": "mis",
    "信息系统": "mis",

    # Probability & Statistics
    "prob_stat": "prob_stat",
    "probability": "prob_stat",
    "statistics": "prob_stat",
    "prob": "prob_stat",
    "stat": "prob_stat",
    "math": "prob_stat",
    "数学": "prob_stat",
    "概率论": "prob_stat",
    "概率论与数理统计": "prob_stat",
    "数理统计": "prob_stat",

    # Marketing
    "mkt": "mkt",
    "marketing": "mkt",
    "市场营销": "mkt",
    "市场营销学": "mkt",
    "营销": "mkt",

    # English
    "eng": "eng",
    "english": "eng",
    "academic_english": "eng",
    "eap": "eng",
    "学术英语": "eng",
    "英语": "eng",
    "基础英语": "eng",
    "学英": "eng",

    # Baseline subjects
    "law": "law",
    "民商法学": "law",
    "民商法": "law",
    "法学": "law",

    "cs": "cs",
    "计算机体系结构": "cs",
    "计算机": "cs",

    "econ": "econ",
    "计量经济学": "econ",
    "计量": "econ",

    "se": "se",
    "软件工程": "se",
    "软工": "se",
}


class KnowledgeService:
    """Service providing unified access to multi-discipline knowledge graphs."""

    def __init__(self):
        # Build comprehensive subjects registry: baseline + daershang
        self._all_subjects: List[SubjectMeta] = list(BASELINE_SUBJECTS) + list(DAERSHANG_SUBJECTS)
        self._subjects_by_code: Dict[str, SubjectMeta] = {s.code: s for s in self._all_subjects}

    @staticmethod
    def normalize_subject_code(raw: Optional[str]) -> Optional[str]:
        """Normalize any subject input or alias to canonical code."""
        if not raw:
            return None
        cleaned = str(raw).strip().lower()
        return KNOWLEDGE_SUBJECT_ALIASES.get(cleaned, cleaned)

    def list_all_subjects(self, category: Optional[str] = None, semester: Optional[str] = None) -> SubjectListResponse:
        """List all registered academic subjects with optional filtering."""
        items = list(self._all_subjects)
        if category:
            items = [s for s in items if s.category.lower() == category.lower()]
        if semester:
            items = [s for s in items if semester.lower() in s.semester.lower()]
        return SubjectListResponse(total=len(items), subjects=items)

    def get_subject_meta(self, subject: str) -> Optional[SubjectMeta]:
        """Look up metadata for a single discipline."""
        code = self.normalize_subject_code(subject)
        return self._subjects_by_code.get(code)

    def get_subject_knowledge_graph(self, subject: str) -> Optional[KnowledgeGraphResponse]:
        """
        Return the complete knowledge graph for a subject.
        Directly returns high-resolution ontologies for Daershang subjects,
        or synthesizes graph from seed items for baseline subjects.
        """
        code = self.normalize_subject_code(subject)
        if not code:
            return None

        # Check Daershang repository first
        if code in DAERSHANG_KNOWLEDGE_MAP:
            entry = DAERSHANG_KNOWLEDGE_MAP[code]
            meta: SubjectMeta = entry["meta"]
            concepts: List[ConceptDetail] = entry["concepts"]
            graph: GraphData = entry["graph"]

            return KnowledgeGraphResponse(
                subject=code,
                subject_name=meta.name,
                graph=graph,
                concepts=concepts,
                total_concepts=len(concepts),
                total_edges=len(graph.edges)
            )

        # Baseline subjects: aggregate from SEED_QUESTIONS
        meta = self._subjects_by_code.get(code)
        if not meta:
            return None

        matched_questions = [q for q in SEED_QUESTIONS if q.subject.lower() == code]
        all_nodes: List[GraphNode] = []
        all_edges: List[GraphEdge] = []
        concept_details: List[ConceptDetail] = []
        seen_node_ids = set()

        for idx, q in enumerate(matched_questions):
            # Formulate concept detail
            c_id = f"{code}_c{idx+1}"
            trap_titles = [t.title for t in q.traps.values()]
            prereq_titles = [t.prereq for t in q.traps.values()]
            concept_details.append(ConceptDetail(
                id=c_id,
                label=q.tag or f"{meta.name}核心考点{idx+1}",
                subject=code,
                definition=q.explanation,
                prerequisites=prereq_titles,
                traps=trap_titles,
                applications=["考试考点真题研析"]
            ))

            if q.graph:
                for n in q.graph.nodes:
                    if n.id not in seen_node_ids:
                        all_nodes.append(n)
                        seen_node_ids.add(n.id)
                for e in q.graph.edges:
                    all_edges.append(e)

        graph = GraphData(
            title=f"{meta.name}·综合考点拓扑图谱",
            nodes=all_nodes,
            edges=all_edges
        )

        return KnowledgeGraphResponse(
            subject=code,
            subject_name=meta.name,
            graph=graph,
            concepts=concept_details,
            total_concepts=len(concept_details),
            total_edges=len(all_edges)
        )

    def search_concepts(self, query: str, subject: Optional[str] = None) -> List[ConceptDetail]:
        """Search concepts by title, definition, or keywords."""
        q_clean = query.strip().lower()
        target_subject = self.normalize_subject_code(subject)

        results: List[ConceptDetail] = []
        # Search Daershang
        for code, entry in DAERSHANG_KNOWLEDGE_MAP.items():
            if target_subject and code != target_subject:
                continue
            for c in entry["concepts"]:
                if (q_clean in c.label.lower() or 
                    q_clean in c.definition.lower() or 
                    any(q_clean in p.lower() for p in c.prerequisites) or
                    any(q_clean in t.lower() for t in c.traps)):
                    results.append(c)

        return results


knowledge_service = KnowledgeService()
