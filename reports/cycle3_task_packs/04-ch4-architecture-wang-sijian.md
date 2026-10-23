# 任务包 04 · 第 4 章 System Design and Architecture

| 项 | 内容 |
| :--- | :--- |
| **负责人** | 王思鉴（50106045 · 架构） |
| **章节** | 第 4 章 System Design and Architecture（全篇最长、技术深度评分的主要承载章） |
| **页数** | **9–11 页**（约 **2,600–3,400 English words** + **4 张图 / 1 张表**） |
| **交付路径** | `reports/final_report/ch04_wang_sijian/` → `outline.md` → `draft.md` |
| **截止** | outline: Week A 周日 23:59 ／ draft: Week B 周日 23:59 |
| **依赖** | 无上游阻塞；但你产出的 Figure 4.1 / 4.3 会被谢炜昕 Ch3 与江昊 Ch5.2 引用 |
| **上游硬约束** | 官方 Brief 明确要求本章含 **context models / business process models / architecture diagrams / class diagrams / sequence diagrams** —— 五类图缺一不可 |

---

## 1. 一句话说明你要交付什么

**用四张图和一张 ADR 矩阵，证明"我们不是搭了个玩具，而是在明确的约束下做了一组彼此自洽的工程取舍"。**

这一章是「去 AI 感」的主战场。AI 生成的项目在这一章会写成"我们采用了微服务架构、使用了 React + Redux + PostgreSQL"——而你们恰恰**没有**用这些。所以你的写法必须是：**每一个技术选择都对应一个被明确拒绝的替代方案，并给出拒绝理由。** Table 4.1 的 ADR（Architecture Decision Record）矩阵就是这份报告最值钱的一张表。

---

## 2. 逐节结构与字数预算

### 4.1 Architectural Overview (700–900 words + **Figure 4.1**)

#### 4.1.1 四层架构（**Figure 4.1，必须自绘**）

用 Mermaid `flowchart` 或 draw.io 画一张**单进程单端口**的四层图：

```
┌──────────────────────────────────────────────────────────┐
│  Layer 1 · Presentation  (frontend/)                      │
│  index.html (57 KB) │ app.js (259 KB) │ style.css (73 KB) │
│  原生 ES6 · CSS Variables · localStorage · i18n            │
└───────────────────────────┬──────────────────────────────┘
                            │  HTTP / JSON  (same origin)
┌───────────────────────────┴──────────────────────────────┐
│  Layer 2 · API / Interface  (backend/app/routers/)        │
│  health │ quiz │ diagnose │ reports │ auth   ← 8 endpoints │
└───────────────────────────┬──────────────────────────────┘
┌───────────────────────────┴──────────────────────────────┐
│  Layer 3 · Domain Services  (backend/app/services/)       │
│  question │ diagnostic │ report │ auth │ graph             │
└───────────────────────────┬──────────────────────────────┘
┌───────────────────────────┴──────────────────────────────┐
│  Layer 4 · Data / Knowledge  (backend/app/data/)          │
│  seed_questions.py (932 lines · 12 questions · 36 traps)  │
│  Pydantic models (backend/app/models/)                    │
└──────────────────────────────────────────────────────────┘
        ▲ 单进程 uvicorn  :8000  ─┐
        └─ StaticFiles(html=True) 挂载 "/"  → 前端与 API 同源
```

**图里必须标出三个关键事实**（评委看不出来就白画了）：
1. **只有一个进程、一个端口** —— `uvicorn` 同时提供 API 与静态文件；
2. **前端与 API 同源** —— 因此生产路径上不需要 CORS；
3. **没有数据库** —— Layer 4 是**只读的 Python 源文件**，这是 ADR-03 的直接后果。

#### 4.1.2 为什么是模块化单体（Modular Monolith）

写 3 段，每段 3–4 句：
- **物理部署的简单性**：一个 ZIP、一条 `uvicorn` 命令、一个端口，考官在自己电脑上就能跑——这直接对应 PoC 评分项的 Reproducibility。
- **逻辑上的分层纪律**：routers（只做 I/O 与校验）→ services（业务）→ data/models（数据与类型）。**这一层分离是"模块化"的全部含义**，而不是拆成多个可独立部署的服务。
- **如果换微服务会付出什么**：需要容器编排、服务发现、跨服务事务、分布式追踪——**这些成本全落在 10 周、10 个学生的课程项目上，而收益（弹性伸缩）在单机演示场景下为零**。

### 4.2 Context and Behavioural Models (600–800 words + **Figure 4.2 / 4.4**)

#### 4.2.1 System Context Model（**Figure 4.2，复用**）

直接复用 `reports/figures/fig_context_model.png`（2248×1880）及其 `.mmd`。正文写清：系统边界、三个外部实体（Student / Instructor / Neo4j Aura —— **注意 Neo4j 必须画虚线并标注 "offline evaluation only"**，这是 ADR-05 的视觉证据）。

#### 4.2.2 Sequence Model for Diagnosis（**Figure 4.4，复用**）

复用 `reports/figures/fig_seq_diagnose.png`（3610×3568）及其 `.mmd`。正文写清一次 `POST /api/diagnose` 的调用时序：Browser → Router（Pydantic 校验）→ DiagnosticService（查表）→ QuestionBank（内存字典）→ Response（含 trap 四字段）。

**必须写的一句话**（与董思钦 Ch5.4 口径一致）：
> 诊断链路上**没有任何模型调用**；`diagnose` 的全部行为是 O(1) 字典查找与字段拼装，这就是它能做到 P95 < 5 ms 与完全离线的原因。

> ⚠️ **如果 `fig_seq_diagnose.mmd` 里画了 LLM 或 Neo4j 调用，必须重画。** 图与文字不一致会被当场抓住。

### 4.3 Domain Class Model (**Figure 4.3，必须新画**)

**这一张是本次唯一的全新技术图，不能复用旧的**（官方 Brief 明确要求 class diagrams）。

画 `QuizItem` / `OptionItem` / `TrapDetail` / `RadarDimension` 四者的关系：

| 类 | 关键属性 | 关系 |
| :--- | :--- | :--- |
| `QuizItem` | `id`, `subject`, `stem`, `options[4]`, `traps: dict`, `explanation` | 1 — * `OptionItem` |
| `OptionItem` | `key`, `text`, `is_correct`, `trap_id` | * — 1 `TrapDetail`（仅错项） |
| `TrapDetail` | `title`, `desc`, `prereq`, `radar_hit` | 1 — 1 `RadarDimension` |
| `RadarDimension` | 5 个枚举值 | — |

**正文必须点出这张图的设计洞见**（这是你的技术贡献，不是画图作业）：
> **陷阱挂在「选项」上，而不是挂在「题目」上。** 因为同一个错误选项在不同情境下的误解是不同的；把陷阱绑到选项，使得"诊断"退化为一次外键查找，而不是一次推理。**这个建模决定（ADR-04）是整个诊断算法得以确定性化的前提。**

### 4.4 Architecture Decision Records (**Table 4.1，本章核心**)

**Table 4.1：ADR 矩阵（≥6 行）**

| ID | 决策 | 被拒绝的替代方案 | 拒绝理由 | 代价 / 已知风险 |
| :--- | :--- | :--- | :--- | :--- |
| AD-1 | **模块化单体**（单进程单端口） | 微服务拆分 | 10 周×10 人不需要弹性伸缩；编排与分布式调试成本远超收益 | 无法水平扩展（本项目无此需求） |
| AD-2 | **原生 ES6 零构建**（无打包器） | React + Vite + Tailwind | FCP < 100 ms；考官环境零 `npm install`；离线 ZIP 即开 | 手工管理模块加载顺序；无生态组件库 |
| AD-3 | **静态 Python 题库**（只读源文件） | PostgreSQL / SQLite | 无数据库即无迁移、无连接池、无 `database is locked`；ZIP 交付即可运行 | 题库不可在线编辑；内容更新需发版 |
| AD-4 | **选项级陷阱 + 确定性查表** | 让 LLM 现场生成诊断 | 法条/公式幻觉是教学事故级风险；查表可复现、可测试、< 5 ms | 只能覆盖预定义陷阱（见 Ch5.4.2 对比表） |
| AD-5 | **Neo4j 仅用于离线评估链路** | 把图谱放进在线演示链路 | 云端实例会休眠、断网即 500；考场环境不可依赖外网 | 图谱增强的收益无法在演示中现场展示，只能用离线 CSV 佐证 |
| AD-6 | **`allow_origins=["*"]`** | 显式白名单 | 演示环境为同源 + 本地任意端口，通配让本地调试零配置 | **生产化必须收紧**（已在 Ch7 Limitations 与提交前清单中声明） |
| AD-7 | **`localStorage` 会话** | JWT + 服务端会话表 | 无状态单机演示；无需密钥管理与会话存储 | 无法做多设备同步；无真正的权限边界 |

**写作要求**：
- 每个 AD 在正文另配 **80–120 词的段落**展开，不要只在表里出现；
- **"代价 / 已知风险"这一列不许留空，也不许写"无"** —— 一个没有代价的架构决策，通常意味着你没想清楚；
- AD-6 与 AD-7 这两行的诚实声明是你**主动交出的弱点**，这在评分点是加分不是减分（Consistency 与 Technical Depth）。

### 4.5 Key Algorithms and Control Flow (400–500 words)

写清三条控制流（可配一张小流程图，或直接用编号列表，**不必为凑图而画**）：
1. **启动流**：`create_app()` → 注册 CORS → 注册 5 个 router（`prefix="/api"`）→ 挂载 `StaticFiles(directory=frontend_dir, html=True)` → 单端口就绪。
2. **请求流**：请求 → 路由匹配 → Pydantic 校验（422 出口）→ service → 响应模型序列化。
3. **诊断流**：`question_id` 索引 → `selected_option` 索引 → `option.is_correct` 分支 → `traps[option.trap_id]` 查表 → 组装 `DiagnoseResponse`。

### 4.6 Non-Functional Design (300–400 words)

把 NFR 从"要求"变成"设计约束的产物"（呼应张梓健 Ch2.3 的五类 NFR）：

| NFR 类别 | 设计上如何保证 |
| :--- | :--- |
| Usability | 单页零跳转；Trap Drawer 五层渐进披露；中英双语 + 双主题 |
| Performance | 无数据库、无网络、无模型调用；内存字典查找；P95 < 100 ms |
| Reliability | 静态资源与 API 同进程；无外部依赖；空状态有定义良好的降级 |
| Security | Pydantic 输入校验 + 无 SQL（无注入面）；**已知弱项：CORS 通配、无真正鉴权** |
| Maintainability | 四层分层 + 145 个测试作为回归网；单文件规模受控（背端按 router/service/model 拆分） |

---

## 3. 你需要的素材

| 素材 | 路径 |
| :--- | :--- |
| 应用装配 | `backend/app/main.py`（`create_app()` / CORS / `include_router` / `StaticFiles`） |
| 分层结构 | `backend/app/routers/`、`services/`、`models/`、`data/` |
| 复用图源 | `reports/figures/fig_context_model.{mmd,png,svg}`、`fig_seq_diagnose.{mmd,png,svg}` |
| 端点清单 | `reports/api_frontend_mapping.md` |
| 数据契约 | `reports/report_data_contract.md` |
| 前序可复用段落 | `reports/phase2_cycle2_progress_report.md` §4 Architecture & PoC |

---

## 4. 会被退回的雷区

1. ❌ **ADR 表只夸不认**（代价列全填"无"）→ 直接退回。
2. ❌ 架构图画成三层但正文说四层（或漏掉 `StaticFiles` 单端口这个关键事实）。
3. ❌ 类图直接复用旧的时序图/用例图冒充。
4. ❌ 序列图里画了 LLM / Neo4j 调用 → 与 4.2.2 的文字矛盾。
5. ❌ 提到"微服务""云原生""高可用"等与自己实现矛盾的词。
6. ❌ 贴 `main.py` 源码 → Brief 禁止；用结构化列表描述装配顺序。

---

## 5. 验收清单（DoD）

- [ ] 2,600–3,400 词，9–11 页
- [ ] **Figure 4.1** 四层架构（自绘，标出单进程/单端口/无数据库）
- [ ] **Figure 4.2** context model（复用，Neo4j 虚线标注 offline only）
- [ ] **Figure 4.3** 类图（**新画**，四类三关系）
- [ ] **Figure 4.4** 诊断时序（复用，**已核对无 LLM/Neo4j 调用**）
- [ ] **Table 4.1** ADR ≥7 行，代价列无空缺
- [ ] 每个 AD 在正文有 80–120 词展开
- [ ] 4.6 非功能设计表五类齐全，Security 行诚实标注弱项
- [ ] `sources.md` 已附
- [ ] 能不看稿讲 6 分钟

---

## 6. 导师会问你的 3 个问题（准备好 30 秒答法）

**Q1. "你用了 Neo4j，是不是为了炫技？"**
> 答：Neo4j **不在在线演示链路上**，只在离线评估链路上，这一点架构图和 ADR-05 都写清了。用它是因为我们用 MMLU 的 12 个学科做了「有图谱约束 vs 无图谱约束」的对照实验（Ch6.3），7 个学科涨、3 个平、2 个跌。**如果只是为了炫技，我们不会把两个负值写进报告。** 而且正因为云实例会休眠、考场可能断网，我们主动把它移出了演示路径。

**Q2. "为什么不拆微服务？做一个微服务架构不是更专业吗？"**
> 答：专业不是复杂度，是**匹配**。10 周、10 个学生、单机演示、零外部依赖——这些约束下，微服务要付出的成本（容器编排、服务发现、分布式调试、跨服务事务）全部落在我们身上，而它能带来的收益（独立扩缩容、团队并行部署）在这个规模下等于零。我们的分层纪律（router / service / data）已经拿到了模块化的好处，只是没有付部署的代价。

**Q3. "CORS 全开、没有真正的鉴权，这不是安全隐患吗？"**
> 答：是隐患，我们没藏着。ADR-06 明确写了"生产化必须收紧"，ADR-07 写了 localStorage 会话没有权限边界。这个取舍的理由是演示场景：考官在自己机器上用任意端口打开页面，白名单会让本地调试处处报错。**我们在 Ch7 的 Limitations 里把它列为已知限制，并在 Future Work 里给出了 JWT + 白名单 + 限流的具体替换方案。** ——如果导师追问"为什么演示环境就不能白名单"，答：可以，但需要在启动时读取环境变量并配置多个候选端口，这会把"一条命令跑起来"变成"先配环境变量"，对 PoC 评分的 Reproducibility 不利。

---

## 7. 提交方式

1. `git switch -c report/ch04-wang-sijian`
2. 文件放 `reports/final_report/ch04_wang_sijian/`，图放 `reports/final_report/ch04_wang_sijian/figures/`
3. **新图的 `.mmd` 源文件一并提交**（可复现性是加分项）
4. 提 PR 到 `develop`，标题：`docs(report): Ch4 system design and architecture + ADR matrix`
5. 群里 @ 吴宇轩 + @ 江昊（类图与 5.2 领域模型对齐）+ @ 谢炜昕（格式统稿）
