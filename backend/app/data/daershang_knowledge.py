"""
Curriculum Knowledge Ontologies & Topologies for Year 2 Semester 1 ("大二上")
Covers 5 core subjects:
  1. Operations Research (运筹学 · or) - Hamdy Taha mathematical programming & modeling
  2. Management Information Systems (管理信息系统 · mis) - Laudon IS frameworks, value chain, C2M supply chain
  3. Probability & Mathematical Statistics (概率论与数理统计 · prob_stat) - Kolmogorov axioms, Bayes, random variables
  4. Marketing Management (市场营销学 · mkt) - STP, 4Ps, Porter's Five Forces, Luckin vs Cotti cases
  5. Academic English & Communication (学术英语与沟通 · eng) - IMRaD, hedging, anti-plagiarism referencing
"""

from typing import Dict, List
from backend.app.models.knowledge import SubjectMeta, ConceptDetail, KnowledgeGraphResponse
from backend.app.models.quiz import GraphData, GraphNode, GraphEdge

# =============================================================================
# 1. Subject Metadata Registry
# =============================================================================
DAERSHANG_SUBJECTS: List[SubjectMeta] = [
    SubjectMeta(
        code="or",
        name="运筹学与优化建模",
        name_en="Operations Research & Optimization",
        badge="大二上核心必修",
        category="stem",
        semester="大二上",
        icon="📐",
        description="系统优化与定量决策科学，涵盖线性规划建模范式、可行域凸多面体、单纯形极点性质与灵敏度分析。"
    ),
    SubjectMeta(
        code="mis",
        name="管理信息系统",
        name_en="Management Information Systems (MIS)",
        badge="大二上专业核心",
        category="business",
        semester="大二上",
        icon="🌐",
        description="Laudon经典信息系统架构，涵盖数据-信息-知识转换价值链、TPS/MIS/DSS/ESS层级、ERP/SCM中枢与C2M反向供应链。"
    ),
    SubjectMeta(
        code="prob_stat",
        name="概率论与数理统计",
        name_en="Probability & Mathematical Statistics",
        badge="大二上数学基础",
        category="stem",
        semester="大二上",
        icon="🎲",
        description="柯尔莫哥洛夫公理化体系、条件概率与全概率/贝叶斯反转更新、离散型与连续型随机变量分布律。"
    ),
    SubjectMeta(
        code="mkt",
        name="市场营销学",
        name_en="Marketing Management",
        badge="大二上管理必修",
        category="business",
        semester="大二上",
        icon="🎯",
        description="STP战略定位（细分/目标/定位）、4Ps营销组合协同、波特五力与行业竞争壁垒（瑞幸vs库迪实战案例）。"
    ),
    SubjectMeta(
        code="eng",
        name="学术英语与学术写作",
        name_en="Academic English & Communication (EAP)",
        badge="大二上通识进阶",
        category="humanities",
        semester="大二上",
        icon="✍️",
        description="学术语篇IMRaD经典范式、学术语域客观对冲语（Hedging）、严谨引证防抄袭规范与逻辑主位推进。"
    )
]

# =============================================================================
# 2. Detailed Knowledge Concepts & Subgraphs for Each Subject
# =============================================================================

# -----------------------------------------------------------------------------
# 2.1 运筹学 (Operations Research - or)
# -----------------------------------------------------------------------------
OR_CONCEPTS: List[ConceptDetail] = [
    ConceptDetail(
        id="or_c1",
        label="运筹学系统建模范式 (OR Modeling Paradigm)",
        subject="or",
        definition="运用定量方法和数学模型为复杂决策系统寻找最优或满意策略的跨学科科学。六阶段闭环：问题识别、模型构建、算法求解、解的验证、控制与实际实施。",
        prerequisites=["系统工程导论", "数学建模基础"],
        traps=["直接跳过问题本质分析而盲目套用求解软件", "将现实非线性关系武断无损简化为线性导致模型失效"],
        applications=["制造业生产排程", "冷链物流路径规划 (VRP)", "航空机组人员智能调度"]
    ),
    ConceptDetail(
        id="or_c2",
        label="规划模型三要素 (Three Elements of Mathematical Programming)",
        subject="or",
        definition="任何规划模型的数学基石：① 决策变量 (Decision Variables $x_j$)：受控可调参数；② 目标函数 (Objective Function $Z$)：效益最大化或成本最小化度量；③ 约束条件组 (Constraints)：资源、技术与物理边界限制。",
        prerequisites=["代数方程组与不等式", "多元函数微积分"],
        traps=["遗漏决策变量非负约束 (Non-negativity $x_j \\ge 0$) 导致产销量出现荒谬负数", "多目标优化时未做无量纲归一化直接加权求和"],
        applications=["投资组合资产配置", "混合饲料配比最低成本计算", "广告投放渠道预算分配"]
    ),
    ConceptDetail(
        id="or_c3",
        label="可行域与凸多面体几何 (Feasible Region & Convex Polyhedron)",
        subject="or",
        definition="由所有线性约束不等式围成的欧氏空间超平面交集。线性规划的可行域必然是凸集（Convex Set）。极点定理证明：若线性规划存在有限最优解，必在可行域的某一个或多个极点（Vertex）上取得。",
        prerequisites=["向量空间", "解析几何超平面理论", "凸分析基础"],
        traps=["误把非凸可行域当作凸多面体，盲目应用单纯形法导致陷入局部次优点", "混淆可行域有界性与最优解存在性"],
        applications=["双变量图解法教学演示", "多维资源瓶颈几何投影分析"]
    ),
    ConceptDetail(
        id="or_c4",
        label="规划解的分类与状态判别 (Classification of Programming Solutions)",
        subject="or",
        definition="规划解的状态空间：① 可行解 (Feasible)：满足全部约束；② 基可行解 (BFS)：对应凸多面体极点；③ 最优解 (Optimal)：使目标函数达到极值；④ 无界解 (Unbounded)：约束方向缺少封顶致使目标可趋于无穷；⑤ 无可行解 (Infeasible)：约束互斥交集为空。",
        prerequisites=["线性方程组基础解系", "高斯-约旦消元法"],
        traps=["混淆'无可行解'（条件冲突无解）与'无界解'（条件不全导致无限利润）", "退化解（Degenerate BFS）引发的单纯形循环摆动"],
        applications=["生产能力瓶颈约束预警", "供应链死锁状态判定"]
    )
]

OR_GRAPH = GraphData(
    title="运筹学·线性规划与系统优化决策拓扑图谱",
    nodes=[
        GraphNode(id="or_c2", label="规划三要素(变量/目标/约束)", type="core", x=260, y=140),
        GraphNode(id="or_p1", label="先修: 线性代数与向量空间", type="prereq", x=120, y=50),
        GraphNode(id="or_p2", label="先修: 凸集性质与极点定理", type="prereq", x=400, y=50),
        GraphNode(id="or_t1", label="陷阱: 遗漏非负性物理约束", type="trap", x=120, y=250),
        GraphNode(id="or_t2", label="陷阱: 混淆无界解与无可行解", type="trap", x=400, y=250),
    ],
    edges=[
        GraphEdge(from_node="or_p1", to_node="or_c2", label="基向量与维度支撑"),
        GraphEdge(from_node="or_p2", to_node="or_c2", label="凸多面体极点最优保证"),
        GraphEdge(from_node="or_c2", to_node="or_t1", label="易错于 (数学变量脱离现实意义)"),
        GraphEdge(from_node="or_c2", to_node="or_t2", label="易错于 (解空间边界判别模糊)"),
    ]
)

# -----------------------------------------------------------------------------
# 2.2 管理信息系统 (Management Information Systems - mis)
# -----------------------------------------------------------------------------
MIS_CONCEPTS: List[ConceptDetail] = [
    ConceptDetail(
        id="mis_c1",
        label="信息系统社会技术范式 (Sociotechnical Systems Perspective)",
        subject="mis",
        definition="强调管理信息系统不仅仅是计算机软件与网络硬件（IT），而是由技术（Technology）、组织结构（Organization）、管理策略（Management）和人（People）四大支柱相互协同构成的复杂社会技术系统。",
        prerequisites=["管理学原理", "组织行为学概论"],
        traps=["技术决定论陷阱：误以为斥资购买昂贵系统就能自动实现业务增长，忽视组织文化和流程再造", "轻视用户参与度引发员工抵制新系统实施"],
        applications=["跨国企业数字化转型顶层设计", "政企OA协同办公平台架构规划"]
    ),
    ConceptDetail(
        id="mis_c2",
        label="商业信息价值链 (Business Information Value Chain)",
        subject="mis",
        definition="原始数据（Raw Data）经过系统性收集、录入、清洗、转换加工与智能分析，升华为指导企业战术经营与战略决策的高价值商业信息（Information）与组织知识（Knowledge）的闭环转化流。",
        prerequisites=["数据库原理", "统计分析方法"],
        traps=["混淆'数据'与'信息'：以为拥有海量未清洗的数据流水就是掌握了商业洞察", "忽视数据源头质量（GIGO：Garbage In, Garbage Out）"],
        applications=["金融风控实时欺诈识别", "电商个性化推荐与动态定价引擎"]
    ),
    ConceptDetail(
        id="mis_c3",
        label="组织核心系统金字塔层级 (Organizational Systems Pyramid: TPS/MIS/DSS/ESS)",
        subject="mis",
        definition="企业四级信息系统架构：① TPS（事务处理系统）：底层记录日常基本交易（如POS机刷卡、仓库出入库）；② MIS（管理信息系统）：中层提供结构化定期汇总报表；③ DSS（决策支持系统）：结合优化模型支持半结构化决策；④ ESS（高管支持系统）：顶层图形化看板支撑非结构化宏观战略分析。",
        prerequisites=["企业运营管理", "决策科学导论"],
        traps=["系统定位与数据颗粒度错配：将底层高频未经汇总的流水直接报送高管，或试图用高度汇总指标执行日常事务对账", "系统孤岛割裂导致跨层级数据无法穿透穿透溯源"],
        applications=["现代商业银行核心交易系统与风控驾驶舱", "零售巨头智慧门店进销存集成平台"]
    ),
    ConceptDetail(
        id="mis_c4",
        label="数字化新商业模式与 C2M 反向供应链 (Digital Business Models & C2M Supply Chain)",
        subject="mis",
        definition="结合拼多多等前沿数字化案例：通过社交裂变聚拢碎片化长尾消费者需求，直连制造源头工厂（Customer-to-Manufacturer）。依托算法驱动的精准订单预测消除多级中间代理商，降低牛鞭效应（Bullwhip Effect）与高额库存积压损耗。",
        prerequisites=["供应链管理 (SCM)", "网络经济学与平台商业模式"],
        traps=["忽视反向供应链对工厂柔性制造（FMS）和快速响应交付的严苛要求", "只看前端低价流量聚集，忽视售后质量品控合规与长期商誉"],
        applications=["农产品产地直供冷链网络", "产业带白牌制造业自主品牌破局"]
    ),
    ConceptDetail(
        id="mis_c5",
        label="企业一体化系统集成 (Enterprise Integrated Systems: ERP / SCM / CRM)",
        subject="mis",
        definition="将分散在财务、销售、生产、采购和客户服务中的跨部门业务流程统一集成到中央数据库中，消除'信息孤岛'（Information Silos），实现全企业范围端到端单一真理来源（Single Source of Truth）。",
        prerequisites=["业务流程重组 (BPR)", "数据治理与主数据管理"],
        traps=["盲目定制化二次开发导致ERP版本无法升级维护", "部门利益本位主义阻碍主数据口径统一"],
        applications=["大型集团SAP/Oracle全套系统部署", "制造业精益敏捷生产集成"]
    )
]

MIS_GRAPH = GraphData(
    title="管理信息系统·社会技术范式与企业集成架构拓扑图谱",
    nodes=[
        GraphNode(id="mis_c3", label="企业系统层级(TPS/MIS/DSS/ESS)", type="core", x=260, y=140),
        GraphNode(id="mis_p1", label="先修: 商业信息价值链(Data->Info)", type="prereq", x=120, y=50),
        GraphNode(id="mis_p2", label="先修: 业务流程重组与社会技术范式", type="prereq", x=400, y=50),
        GraphNode(id="mis_t1", label="陷阱: 技术决定论(忽视组织流程变革)", type="trap", x=120, y=250),
        GraphNode(id="mis_t2", label="陷阱: 数据颗粒度与系统层级错配", type="trap", x=400, y=250),
    ],
    edges=[
        GraphEdge(from_node="mis_p1", to_node="mis_c3", label="数据从底层向决策层升华"),
        GraphEdge(from_node="mis_p2", to_node="mis_c3", label="组织结构匹配技术架构"),
        GraphEdge(from_node="mis_c3", to_node="mis_t1", label="易错于 (工具崇拜误区)"),
        GraphEdge(from_node="mis_c3", to_node="mis_t2", label="易错于 (高管看明细/操作无底据)"),
    ]
)

# -----------------------------------------------------------------------------
# 2.3 概率论与数理统计 (Probability & Mathematical Statistics - prob_stat)
# -----------------------------------------------------------------------------
PROB_STAT_CONCEPTS: List[ConceptDetail] = [
    ConceptDetail(
        id="stat_c1",
        label="柯尔莫哥洛夫公理化体系 (Kolmogorov Axioms of Probability)",
        subject="prob_stat",
        definition="现代概率论的严密测度基石。设样本空间为 $\\Omega$、事件域为 $\\mathcal{F}$，概率测度 $P$ 必须严格满足三大公理：① 非负性：$P(A) \\ge 0$；② 规范性：$P(\\Omega) = 1$；③ 可列可加性：对两两互斥事件序列 $A_i$，有 $P(\\bigcup A_i) = \\sum P(A_i)$。",
        prerequisites=["实分析测度论初步", "集合论代数运算（德摩根定律）"],
        traps=["将概率公理化定义与经验频率等同，误认为频率等同于理论概率测度", "在涉及无限样本空间时忽视可列可加性与有限可加性的关键区别"],
        applications=["量子力学波函数坍缩几率建模", "现代精算学与复杂金融衍生品定价风险中性测度"]
    ),
    ConceptDetail(
        id="stat_c2",
        label="条件概率与乘法公式 (Conditional Probability & Multiplication Rule)",
        subject="prob_stat",
        definition="在已知事件 $B$ 已经发生的先验约束下，事件 $A$ 发生的更新测度：$P(A|B) = \\frac{P(AB)}{P(B)}$（要求 $P(B) > 0$）。本质是将全样本空间缩减至 $B$ 子集重新归一化。联合概率乘法公式：$P(AB) = P(B)P(A|B) = P(A)P(B|A)$。",
        prerequisites=["集合交集运算", "公理化测度归一化"],
        traps=["对零概率事件进行无防备条件化导致未定义数学错误", "混淆条件概率 $P(A|B)$ 与联合概率 $P(AB)$"],
        applications=["垃圾邮件贝叶斯过滤分类器", "基因遗传病隐性携带概率测算"]
    ),
    ConceptDetail(
        id="stat_c3",
        label="全概率公式与贝叶斯定理 (Total Probability & Bayes' Theorem)",
        subject="prob_stat",
        definition="设 $B_1, \\dots, B_n$ 构成样本空间的一个完备划分。全概率公式实现综合先验求边缘结果：$P(A) = \\sum P(B_i)P(A|B_i)$。贝叶斯定理实现'执果索因'的反向后验更新：$P(B_k|A) = \\frac{P(B_k)P(A|B_k)}{\\sum P(B_i)P(A|B_i)}$。",
        prerequisites=["完备事件群划分充分必要条件", "条件概率乘法定理"],
        traps=["基准率谬误 (Base Rate Fallacy)：罕见病筛查中忽略极低的先验患病率，将高检测敏感度误等同于阳性确诊率", "划分不完备或不互斥直接套用全概率公式"],
        applications=["临床医学诊断假阳性/假阴性校准", "自动驾驶传感器多源卡尔曼滤波融合"]
    ),
    ConceptDetail(
        id="stat_c4",
        label="随机变量与离散分布律 (Random Variables & PMF)",
        subject="prob_stat",
        definition="随机变量是定义在样本空间上的单值实值函数 $X: \\Omega \\to \\mathbb{R}$。离散型随机变量由概率质量函数（PMF）$p_k = P(X = x_k)$ 完整刻画，严格满足归一化条件 $\\sum p_k = 1$。经典模型包括0-1分布、二项分布 $B(n, p)$ 与泊松分布 $P(\\lambda)$。",
        prerequisites=["单值实函数映射定义", "级数收敛性"],
        traps=["随机变量定义混淆：误把随机变量当成常数或简单集合，而非样本点到实数的映射算子", "二项分布独立重复试验（伯努利试验）先决条件不满足时强行套用公式"],
        applications=["呼叫中心每小时话务并发量排队论模型 (Poisson)", "工业生产线抽检缺陷品率合格评定 (Binomial)"]
    ),
    ConceptDetail(
        id="stat_c5",
        label="事件独立性辨析 (Stochastic Independence)",
        subject="prob_stat",
        definition="两事件 $A$ 与 $B$ 统计独立当且仅当 $P(AB) = P(A)P(B)$。独立意味着 $B$ 的发生与否完全不改变 $A$ 发生的条件几率：$P(A|B) = P(A)$。两两独立（Pairwise Independence）不等同于相互独立（Mutual Independence）。",
        prerequisites=["条件概率定义", "乘法公式"],
        traps=["高危认知混淆：把'互不相容/互斥 ($AB = \\emptyset$)'与'相互独立 ($P(AB)=P(A)P(B)$)'混为一谈（正概率下互斥必定不独立！）", "误以为三个事件两两独立就自动构成相互独立"],
        applications=["容错分布式系统高可用多副本可靠性计算", "密码学伪随机数发生器独立性检测"]
    )
]

PROB_STAT_GRAPH = GraphData(
    title="概率统计·公理化测度与贝叶斯先验后验拓扑图谱",
    nodes=[
        GraphNode(id="stat_c3", label="贝叶斯定理(先验向后验更新)", type="core", x=260, y=140),
        GraphNode(id="stat_p1", label="先修: 柯氏公理与条件概率", type="prereq", x=120, y=50),
        GraphNode(id="stat_p2", label="先修: 完备事件群划分与全概率", type="prereq", x=400, y=50),
        GraphNode(id="stat_t1", label="陷阱: 混淆互斥与相互独立", type="trap", x=120, y=250),
        GraphNode(id="stat_t2", label="陷阱: 基准率遗漏(Base Rate Fallacy)", type="trap", x=400, y=250),
    ],
    edges=[
        GraphEdge(from_node="stat_p1", to_node="stat_c3", label="条件几率测度基础"),
        GraphEdge(from_node="stat_p2", to_node="stat_c3", label="分母全概率边缘归一化"),
        GraphEdge(from_node="stat_c3", to_node="stat_t1", label="易错于 (几何交集空与信息独立混为一谈)"),
        GraphEdge(from_node="stat_c3", to_node="stat_t2", label="易错于 (罕见事件后验误判)"),
    ]
)

# -----------------------------------------------------------------------------
# 2.4 市场营销学 (Marketing Management - mkt)
# -----------------------------------------------------------------------------
MKT_CONCEPTS: List[ConceptDetail] = [
    ConceptDetail(
        id="mkt_c1",
        label="经典 STP 战略分析框架 (STP Strategic Marketing Framework)",
        subject="mkt",
        definition="现代营销战略的核心中枢：① 市场细分 (Segmentation)：按地理、人口、心理和行为变量把异质市场划分为同质子市场；② 目标市场选择 (Targeting)：评估细分市场吸引力并选择无差异、差异化或集中化进入策略；③ 市场定位 (Positioning)：在目标消费者心智中确立独特、差异化且不可替代的价值空间。",
        prerequisites=["消费者行为学基础", "产业组织理论与市场结构"],
        traps=["目标定位泛化：试图成为'适合所有人的品牌'，导致资源分散且心智面目模糊", "混淆市场细分标准，把企业内部组织架构当成外部市场细分依据"],
        applications=["新消费品牌冷启动客群定位", "高端车企子品牌年轻化矩阵拆分"]
    ),
    ConceptDetail(
        id="mkt_c2",
        label="营销组合 4Ps 协同模型 (The 4Ps Marketing Mix)",
        subject="mkt",
        definition="企业可控战术工具的集成：① Product（产品）：产品线广度深度、核心利益与品牌包装；② Price（价格）：成本加成、认知价值与渗透/撇脂定价；③ Place（渠道）：经销商网络、直营体验店与线上线下全渠道（OMO）；④ Promotion（推广）：广告、公关、人员推销与数字整合营销传播（IMC）。",
        prerequisites=["微观经济学价格弹性", "渠道供应链物流基础"],
        traps=["割裂4Ps要素协同：如推出高奢定位产品却采用低俗恶俗的下沉促销手段，造成品牌调性崩塌", "误把营销（Marketing）狭隘等同于促销推广（Promotion/Selling）"],
        applications=["新产品上市全套GTM（Go-to-Market）方案制定", "连锁餐饮爆品引流与利润品组合设计"]
    ),
    ConceptDetail(
        id="mkt_c3",
        label="波特五力与行业竞争策略 (Porter's Five Forces & Competitive Strategies)",
        subject="mkt",
        definition="评估行业长期盈利能力的五种竞争驱动力：同业竞争者激烈度、潜在进入者壁垒、替代品威胁、买方议价力与供应商议价力。基于此制定波特三大经典竞争战略：成本领先（Cost Leadership）、差异化（Differentiation）与聚焦战略（Focus）。",
        prerequisites=["产业经济学", "战略管理导论"],
        traps=["陷入'夹在中间'（Stuck in the Middle）困境：既无规模成本优势，又无明显品质品牌差异化", "忽视非显性跨界替代品颠覆威胁（如数码相机被智能手机颠覆）"],
        applications=["瑞幸咖啡与库迪咖啡万店下沉市场攻防战分析", "新能源汽车动力电池产业链上下游话语权博弈"]
    ),
    ConceptDetail(
        id="mkt_c4",
        label="消费者涉入度与决策路径 (Consumer Involvement & Decision Funnel)",
        subject="mkt",
        definition="根据消费者对产品购买决策的个人相关度与感知风险，划分为高涉入度（深度调研、理性多属性评估，如房产、汽车）与低涉入度（冲动购买、情感刺激、习惯性复购，如快消零食、日常咖啡）。指导从触达认知、兴趣、考虑、转化到忠诚裂变的漏斗设计。",
        prerequisites=["认知心理学知觉态度理论", "数字营销漏斗模型"],
        traps=["错配沟通触点：对低涉入度日常快消品使用冗长复杂的学术论文式说理，或对高涉入度昂贵商品试图仅靠快照冲动诱导下单", "忽视售后阶段客户关怀导致负面口碑口碑发酵"],
        applications=["B2B企业级软件长期客户线索培育", "即时零售美妆日化即兴下单场景转化"]
    )
]

MKT_GRAPH = GraphData(
    title="市场营销·STP战略定位与4Ps协同竞争拓扑图谱",
    nodes=[
        GraphNode(id="mkt_c1", label="STP战略核心(细分/目标/定位)", type="core", x=260, y=140),
        GraphNode(id="mkt_p1", label="先修: 消费者画像与需求弹性", type="prereq", x=120, y=50),
        GraphNode(id="mkt_p2", label="先修: 行业竞争壁垒与心智定位", type="prereq", x=400, y=50),
        GraphNode(id="mkt_t1", label="陷阱: 目标泛化(试图迎合所有人)", type="trap", x=120, y=250),
        GraphNode(id="mkt_t2", label="陷阱: 狭隘促销陷阱(营销≠推销打折)", type="trap", x=400, y=250),
    ],
    edges=[
        GraphEdge(from_node="mkt_p1", to_node="mkt_c1", label="基于需求差异进行细分"),
        GraphEdge(from_node="mkt_p2", to_node="mkt_c1", label="基于心智空缺确立定位"),
        GraphEdge(from_node="mkt_c1", to_node="mkt_t1", label="易错于 (缺乏战略取舍舍弃勇气)"),
        GraphEdge(from_node="mkt_c1", to_node="mkt_t2", label="易错于 (战术打折蚕食品牌资产)"),
    ]
)

# -----------------------------------------------------------------------------
# 2.5 学术英语与商务沟通 (Academic English & EAP - eng)
# -----------------------------------------------------------------------------
ENG_CONCEPTS: List[ConceptDetail] = [
    ConceptDetail(
        id="eng_c1",
        label="学术论文 IMRaD 结构范式 (IMRaD Structural Framework)",
        subject="eng",
        definition="全球顶尖学术发表的标准宏观语篇架构：① Introduction（引言：背景确立、研究缺口Research Gap与核心目标）；② Methods（方法：实验方案、数据采集与严格复现标准）；③ Results（结果：客观事实、数据统计与图表呈现）；④ Discussion（讨论：深入阐释意义、揭示机制、客观承认局限性Limitations与未来展望）。",
        prerequisites=["科学研究方法论", "学术文体学常识"],
        traps=["把Results与Discussion混淆：在结果部分主观下结论，或在讨论部分罗列未呈现的新数据", "引言文献回顾罗列流水账，未能提炼并论证自身研究缺口（Gap）"],
        applications=["国际顶级期刊SCI/SSCI论文撰写", "本科/硕博毕业论文开题与技术报告答辩"]
    ),
    ConceptDetail(
        id="eng_c2",
        label="学术语域与对冲语修辞 (Academic Register & Hedging Devices)",
        subject="eng",
        definition="学术英语要求严谨、客观、不带主观偏见的语域特征。对冲语（Hedging / Epistemic Modality：如 may, might, indicate, suggest, potentially, to some extent）是学术诚信的体现，用以精确控制断言的确定性程度，避免武断与绝对化结论被同行证伪。",
        prerequisites=["语用学情态动词语义分析", "学术严谨性哲学"],
        traps=["绝对化断言谬误：频繁使用 always, absolutely, prove 造成学术过度承诺与漏洞", "混淆口语体与正式学术书面体（如在论文中随意使用 kids, a lot of, stuff 等非正式词）"],
        applications=["同行评审审稿意见辩驳回复 (Rebuttal Letter)", "科研论文结论段客观表述"]
    ),
    ConceptDetail(
        id="eng_c3",
        label="学术严谨引用与反抄袭准则 (Academic Referencing & Anti-Plagiarism)",
        subject="eng",
        definition="捍卫学术诚信的最高红线。要求对所有借鉴的他方事实、理论、数据与观点做详尽规范标注（Harvard / APA格式）。关键技能为'合规释义'（Paraphrasing）：在彻底理解原文内涵的基础上，使用完全属于自己的句式结构与词汇重新组织，杜绝任何形式的拼贴抄袭（Patchwriting）。",
        prerequisites=["学术伦理道德规范", "精读理解与结构化转述能力"],
        traps=["拼贴式抄袭陷阱：仅机械替换少量同义词但原封不动保留原作者特殊语序结构，在Turnitin查重中仍被判定为抄袭", "二次引用（Secondary Citation）未注明出处导致文献断链"],
        applications=["文献综述撰写防查重合规审核", "跨学科联合研究知识产权归属标注"]
    ),
    ConceptDetail(
        id="eng_c4",
        label="信息主位推进与逻辑连贯 (Thematic Progression & Coherence)",
        subject="eng",
        definition="句子内部从'已知信息'（Theme/主位）平滑过渡到'核心新信息'（Rheme/述位）的衔接契约（Given-to-New Contract）。段落通过首句明确的主题句（Topic Sentence）、论据支撑以及恰当的逻辑过渡词（Transitional Signals）实现整体逻辑紧凑无跳跃。",
        prerequisites=["语篇语言学语法衔接手段", "论证逻辑链条设计"],
        traps=["机械堆叠连接词：滥用 However, Therefore, Furthermore 但上下文前后句子实际上毫无逻辑因果关系", "主题句缺失导致读者在无序事实细节中迷失"],
        applications=["高分学术雅思/托福写作 Task 2 篇章组织", "商业咨询报告执行摘要（Executive Summary）拟定"]
    )
]

ENG_GRAPH = GraphData(
    title="学术英语·IMRaD范式与客观对冲语篇拓扑图谱",
    nodes=[
        GraphNode(id="eng_c1", label="IMRaD宏观学术范式", type="core", x=260, y=140),
        GraphNode(id="eng_p1", label="先修: 学术语域与客观对冲语", type="prereq", x=120, y=50),
        GraphNode(id="eng_p2", label="先修: 规范释义与反抄袭引证", type="prereq", x=400, y=50),
        GraphNode(id="eng_t1", label="陷阱: 绝对化过度承诺(缺乏Hedging)", type="trap", x=120, y=250),
        GraphNode(id="eng_t2", label="陷阱: 机械同义词拼贴抄袭(Patchwriting)", type="trap", x=400, y=250),
    ],
    edges=[
        GraphEdge(from_node="eng_p1", to_node="eng_c1", label="赋予讨论部分严谨科学度"),
        GraphEdge(from_node="eng_p2", to_node="eng_c1", label="支撑引言与方法论合法性"),
        GraphEdge(from_node="eng_c1", to_node="eng_t1", label="易错于 (绝对化武断断言被证伪)"),
        GraphEdge(from_node="eng_c1", to_node="eng_t2", label="易错于 (伪释义被Turnitin查重标记)"),
    ]
)

# =============================================================================
# 3. Master Mapping Dictionary
# =============================================================================
DAERSHANG_KNOWLEDGE_MAP: Dict[str, Dict[str, any]] = {
    "or": {
        "meta": next(s for s in DAERSHANG_SUBJECTS if s.code == "or"),
        "concepts": OR_CONCEPTS,
        "graph": OR_GRAPH,
    },
    "mis": {
        "meta": next(s for s in DAERSHANG_SUBJECTS if s.code == "mis"),
        "concepts": MIS_CONCEPTS,
        "graph": MIS_GRAPH,
    },
    "prob_stat": {
        "meta": next(s for s in DAERSHANG_SUBJECTS if s.code == "prob_stat"),
        "concepts": PROB_STAT_CONCEPTS,
        "graph": PROB_STAT_GRAPH,
    },
    "mkt": {
        "meta": next(s for s in DAERSHANG_SUBJECTS if s.code == "mkt"),
        "concepts": MKT_CONCEPTS,
        "graph": MKT_GRAPH,
    },
    "eng": {
        "meta": next(s for s in DAERSHANG_SUBJECTS if s.code == "eng"),
        "concepts": ENG_CONCEPTS,
        "graph": ENG_GRAPH,
    },
}
