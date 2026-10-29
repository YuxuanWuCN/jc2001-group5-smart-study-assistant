# JC2001 Group 5 · Cycle 3 总体执行计划
## 周期主题：**Reports Cycle —— 把占小组分 50% 权重的期末大报告写成一家初创公司的技术与落地报告**

| 项 | 内容 |
| :--- | :--- |
| 课程 | JC2001 Introduction to Software Engineering (2026–27), University of Aberdeen |
| 团队 | Group 5 · BSc BMIS · 10 人 |
| 导师 | Dr. Shahzad Mumtaz (`shahzad.mumtaz@abdn.ac.uk`) |
| 组长 | 吴宇轩（50106070，PM / Team Lead） |
| 周期定位 | **Phase 3 / Cycle 3**：冻结软件基线，全力攻报告 |
| 权重口径 | 小组项目占课程总分 **50%**；其中 **Technical Report 50%、PoC 软件 30%、Project Presentation 20%**（即折算到课程总分为 25% / 15% / 10%） |
| 报告篇幅 | **正文 40–60 页**（官方硬性下限 40、上限 60，从第 1 章到第 7 章计） |
| 本周期唯一 DoD | Cycle 3 结束时产出一份**可提交级初稿**：7 章正文齐全 + ≥18 张图表 + ≥25 条 Harvard 引用 + 10 人各自署名 ≥3 页 |
| 官方依据 | [`JC2001-GroupProjectDescription-and-Requirements-2026-27.txt`](../JC2001-GroupProjectDescription-and-Requirements-2026-27.txt) |
| 配套规范包 | [`specs/003-cycle3-startup-report/spec.md`](../specs/003-cycle3-startup-report/spec.md) |
| 任务包目录 | [`reports/cycle3_task_packs/`](cycle3_task_packs/README.md) |
| 组会防身库 | [`reports/supervisor_qa_defense_library.md`](supervisor_qa_defense_library.md) |

---

## 0. 一句话结论

> 软件已经够了（8 个 API 端点、145 个测试用例全绿、3 张 UML 图、62 万字节前端资产），**它唯一的问题是不会替自己说话**。
> Cycle 3 不写新功能，只做一件事：**把已经存在的工程事实，翻译成一份像初创公司交付的、而不是像 AI 生成的报告**，并且让另外 9 个人真正成为这份报告的作者。

### 0.1 与官方 Brief 的强制对齐（这是本计划的骨架，不能自行发挥）

官方 Project Brief 明确规定了 Technical Report 的**内容顺序**。评审按这 7 块打分，我们**不得增删章节、不得改顺序**——"初创感"要长在这个骨架里，而不是靠改结构。下表右列是本章负责人：

| 官方要求章节（原文） | 我们的章 | 负责人 | 官方要求本章必须回答什么 |
| :--- | :-: | :--- | :--- |
| Introduction and Project Context | Ch1 | 林泳桐 | problem、background、objectives、**intended users/stakeholders**、main features、**potential practical or business value** |
| Functional and Non-Functional Requirements | Ch2 | 张梓健 | 功能需求 + 质量需求（usability / performance / reliability / security / maintainability） |
| Use Cases and Requirements Modelling | Ch3 | 谢炜昕 | **use case diagram(s) + descriptions of the key use cases** |
| System Design and Architecture | Ch4 | 王思鉴 | architecture、key components、relationships、**important design decisions**；context models / business process models / architecture diagrams / class diagrams / sequence diagrams |
| Implementation | Ch5 | 江昊 · 董思钦 · 习羽赛 · 梁子铉 | technologies、tools、frameworks、software structure、algorithms、**important technical decisions**、GUI design and implementation |
| Testing and Evaluation | Ch6 | 杨明杰 | test cases、testing methods、results，**并对照第 2 章声明的功能/非功能需求逐条评估**（unit / component / interface / performance） |
| Conclusions and Future Work | Ch7 | 吴宇轩 | outcomes、limitations、**realistic** opportunities for further development |
| References | — | 谢炜昕统稿 | 统一学术风格（Harvard） |
| **Appendix A – Group Workload Profile** | A | 吴宇轩统筹 · 10 人签署 | **必须用 MyAberdeen 提供的模板**；0% / +X% / −X% 口径 |

> ⚠️ **上一版计划的三个结构性错误，已在本版修正**（写在这里是为了留下决策痕迹，也顺便成为报告"过程反思"的素材）：
> 1. 原计划只有 7 章但没有把 **Use Cases and Requirements Modelling 单列为独立章节** → 官方明确要求它与需求章分开，缺了直接扣分。现列为 Ch3，独立负责人。
> 2. 原计划自拟了"Deployment"与"Startup Viability"两章 → 官方章节表里没有这两个标题，另开章节会被判"结构不符合要求"。现分别并入 **Ch5.6（Implementation 的部署与可复现性）** 与 **Ch7（Conclusions and Future Work 中的商业化展望）**。
> 3. 原计划把 Appendix A 写成自定义的"Individual Contribution Audit" → 官方要求 Appendix A **必须是 MyAberdeen 模板的 Group Workload Profile**。现改名并改为模板填报，个人的实质贡献叙述移入模板的说明栏。
>
> 另两条官方硬性约束：**正文严禁贴源码**（"Do not include source code in the technical report"）；**A4 / 2.54 cm 四边距 / 单栏 / 12 pt / Arial 或 Times New Roman / 1.5 倍行距**。

---

## 1. 现状诊断（基于仓库可核验事实，不含猜测）

### 1.1 资产盘点（这些是报告的全部弹药，别再写新代码）

| 资产 | 实测事实 | 报告去向 |
| :--- | :--- | :--- |
| 后端 | `backend/app/`：5 个 router、5 个 service、5 个 model 模块 | Ch4、Ch5.1 |
| API 端点 | **8 个**：`GET /api/health`、`GET /api/quiz`、`POST /api/diagnose`、`GET /api/reports/summary`、`GET /api/reports/trend`、`GET /api/auth/demo-users`、`POST /api/auth/login`、`POST /api/auth/register` | Ch5.2 接口契约表 |
| 测试 | **9 个测试文件 / 78 个 test 函数 / 参数化展开后 145 个用例全部通过**（`python -m pytest tests/ -q` → `145 passed, 17 warnings in 3.56s`） | Ch6 + 附录 C |
| 对抗性测试 | `tests/test_adversarial_backend.py`：**25 个对抗性测试函数 / 523 行**（非法参数注入、重复 ID、编码攻击、并发） | Ch6.2 |
| 题库 | `backend/app/data/seed_questions.py`（**932 行**）：**12 道题 × 4 学科（law / cs / econ / se）× 36 个细粒度错因陷阱**，每题带 `explanation`，每个陷阱带 `title/desc/prereq/radar_hit` | Ch5.3、Ch5.4 |
| 图谱增强实证 | `graphrag（终）/final_systematic_report.csv`：**MMLU 12 个学科子集上 Base vs Ours 的对比实测** | Ch6.3（本报告最硬的证据） |
| UML | `reports/figures/`：上下文模型图、全局用例图、排雷全时序图（`.mmd`/`.png`/`.svg` 三件套）+ `reports/diagrams/JC2001_Week6_UML_Lab_Practices.drawio` | Ch3（用例图）、Ch4（上下文/时序），类图需新画 |
| 前端 | `frontend/index.html` 57 KB / `app.js` 259 KB / `style.css` 73 KB，深色控制台 + 双语 + `localStorage` | Ch5.5 |
| 可运行性 | `backend/run.py`（394 B）、`requirements.txt`（457 B）、`.env.example`（487 B）、根目录 `README.md` | Ch5.6 |
| 既有文档 | `reports/competitor_analysis.md`（124 KB，含六维竞品对比矩阵）、`reports/project_proposal.md`、`reports/phase2_cycle2_progress_report.md`（936 行 / 9 节）、`reports/api_frontend_mapping.md`、`reports/report_data_contract.md`、`reports/assumptions.md` | Ch1、Ch2 素材 |

### 1.2 三个真问题（按严重度排序）

1. **【致命】报告 50% 的分数目前是 0 分** —— 组内 10 人尚未动笔，报告不存在。
2. **【致命】"太像 AI agent 做的项目"** —— 导师的原话指的不是代码差，而是：**没有商业动机、没有取舍痕迹、没有失败记录**。一个从第一天就完美的系统，在学术评审眼里等于"不是你们做的"。
3. **【高】知识集中在一个人身上** —— 代码由组长一人完成，组会上其他成员无法回答基础问题。这既是 Appendix A（Group Workload Profile）的扣分项，也是"是不是买的/生成的"这一质疑的根源。

### 1.3 因此本周期**不做**什么（主动裁剪，写进 Ch2 当"精益裁剪"证据用）

- ❌ 不新增业务功能（不写新 API、不写新页面）
- ❌ 不引入新依赖、不引入数据库、不重构
- ❌ 不追求"技术更炫"，只追求"决策更可解释"
- ✅ 唯一允许的代码动作：修测试告警（`backend/app/models/auth.py` 的 `Field(..., example=)` 应改 `json_schema_extra`），作为"工程纪律"的证据留痕

---

## 2. 报告蓝图（7 章正文 + 4 附录，正文 48–57 页）

> 一句话叙事主线：**一个 10 人学生团队，用 12 周、零预算、必须离网演示的约束，为"刷题只看对错"的大学生做了一款能诊断错因的助学 MVP——并且诚实地报告了它在哪些学科上有效、哪些无效。**

### 2.1 前置页（不计入 40–60 页）

| 项 | 页数 | 负责人 |
| :--- | :-: | :--- |
| Title Page（必须含：项目标题、Group 5、**BSc BMIS**、10 人学号与姓名） | 1 | 吴宇轩 |
| Declaration / Academic Integrity statement | 1 | 吴宇轩 |
| Abstract（250–300 词） | 1 | 吴宇轩 |
| Table of Contents + List of Figures + List of Tables | 2–3 | 谢炜昕 |

### 2.2 正文章节（这部分才计入 40–60 页）

| 章 | 官方标题 | 我们的章节结构 | 页数 | 负责人 | 本章要回答的核心问题 |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **1** | Introduction and Project Context | 1.1 Problem context（binary feedback 陷阱）· 1.2 Background & related work（通用 LLM 的 Answer Spoiling 与幻觉）· 1.3 Competitor analysis（≥5 竞品）· 1.4 Intended users & stakeholders（3 Persona）· 1.5 Project objectives（SMART ×5）· 1.6 Main features & **business value** | 5–6 | **林泳桐** | 为什么值得做？市面上缺什么？这门生意/这个工具的潜在价值在哪？ |
| **2** | Functional and Non-Functional Requirements | 2.1 Requirements elicitation & sources · 2.2 Functional requirements（**14 行 MoSCoW，Won't 是重点**）· 2.3 **Non-functional requirements**（usability / performance / reliability / security / maintainability 五类，每类给可度量指标）· 2.4 Lean scoping：我们主动砍掉了什么、为什么 | 6–7 | **张梓健** | 系统必须做什么？我们**主动没做**什么？质量指标怎么度量？ |
| **3** | Use Cases and Requirements Modelling | 3.1 System context & actors · 3.2 **Use case diagram**（复用 `fig_use_case_diagram`）· 3.3 **Key use case descriptions ×6**（UC-01 作答、UC-02 看诊断、UC-03 看雷达、UC-04 登录、UC-05 注册、UC-06 切换学科；每个含前置条件/主流程/异常流/后置条件）· 3.4 Activity / state models（答题状态机）· 3.5 Requirements traceability（→ 附录 B） | 6–7 | **谢炜昕** | 谁在什么条件下做什么？用例和需求怎么对得上？ |
| **4** | System Design and Architecture | 4.1 Architectural overview（**Figure: 四层架构图，自绘**）· 4.2 Context & behaviour models（复用 `fig_context_model`、`fig_seq_diagnose`）· 4.3 **Class diagram（新画）**· 4.4 **ADR 权衡矩阵 ≥6 行**（每行必须有"否决的备选 + 否决理由"）· 4.5 Control flow（诊断链路）· 4.6 Non-functional design（对应 Ch2.3 的五个质量属性） | 9–11 | **王思鉴** | 系统怎么分层？**每个技术选择否决了哪个备选方案、为什么**？ |
| **5** | Implementation | 5.1 Technology stack, tools & software structure（`requirements.txt`、目录结构、`run.py`）· 5.2 API contracts & domain data model（8 端点表 + 4 模型字段表）· 5.3 Question bank & trap engineering（36 陷阱的教学法设计）· 5.4 Diagnostic algorithm（**"诊断是查表不是推理"**）· 5.5 GUI design and implementation（零构建前端、Trap Drawer、i18n/主题）· 5.6 Deployment & reproducibility（离网 ZIP 一键运行、成本、回滚） | 14–16 | **江昊**(5.1–5.2) · **董思钦**(5.3–5.4) · **习羽赛**(5.5) · **梁子铉**(5.6) | 到底怎么实现的？关键技术与算法决策是什么？界面怎么设计出来的？ |
| **6** | Testing and Evaluation | 6.1 Test strategy & test pyramid（**Table: 9 文件清点，含 78→145 参数化说明**）· 6.2 Adversarial testing（25 个函数归为 6 组）· 6.3 **Empirical evaluation：MMLU 12 学科 Base vs Ours**（含 3 平、2 负）· 6.4 RAGAS 评估 · 6.5 **Evaluation against the requirements**（回 Ch2.3 的五类 NFR 逐条打分，官方指定动作）· 6.6 Threats to validity（≥5 条） | 7–8 | **杨明杰** | 145 个用例证明了什么？图谱增强**真的有效吗**？我们离达标差在哪？ |
| **7** | Conclusions and Future Work | 7.1 Summary of outcomes（对照 Ch1.5 的 5 条 SMART 目标逐条结账）· 7.2 **Limitations**（≥5 条，与 6.6 呼应但不重复）· 7.3 **Realistic future work**（含商业化路径：3 种收费假设，必须标为假设）· 7.4 Reflection（What worked / **What failed ≥3 条** / 团队学到了什么） | 3–4 | **吴宇轩** | 哪些做成了、哪些砸了、下一步现实的路是什么？ |
| | **正文合计** | | **48–59** | | |
| — | References（Harvard, ≥25 条） | | 2 | 谢炜昕统稿 | 不计入页数 |
| **A** | **Group Workload Profile**（官方 MyAberdeen 模板，10 人签署） | | 1–2 | 吴宇轩统筹 | 不计入页数 |
| B | Requirements Traceability Matrix（需求 → 用例 → 设计 → 实现 → 测试） | | 2 | 谢炜昕 | 不计入页数 |
| C | Test Case Inventory（145 用例清单 + 本机运行截图） | | 2 | 杨明杰 | 不计入页数 |
| D | Glossary & API Snapshot（术语 ≥12 条 + OpenAPI 快照） | | 1–2 | 江昊 | 不计入页数 |

### 2.3 全篇图表预分配（防止十个人撞号，Week A 就锁死）

| 编号 | 图表名 | 所属章 |
| :--- | :--- | :-: |
| Figure 1.1 | Value Proposition Canvas | 1 |
| Figure 1.2 | Competitor positioning map（二维定位图） | 1 |
| Figure 2.1 | MoSCoW distribution（Must/Should/Could/Won't 柱状图） | 2 |
| Figure 3.1 | **Use case diagram**（复用 `fig_use_case_diagram.svg`） | 3 |
| Figure 3.2 | Answering state machine（答题状态机） | 3 |
| Figure 4.1 | **Four-layer architecture（自绘）** | 4 |
| Figure 4.2 | System context model（复用 `fig_context_model.svg`） | 4 |
| Figure 4.3 | **UML class diagram（新画）** | 4 |
| Figure 4.4 | Diagnose sequence diagram（复用 `fig_seq_diagnose.svg`） | 4 |
| Figure 5.1 | Software structure / package diagram | 5 |
| Figure 5.2 | Trap detail structure（陷阱三段式） | 5 |
| Figure 5.3 | Trap Drawer UI screenshot | 5 |
| Figure 5.4 | Main console UI screenshot | 5 |
| Figure 5.5 | Deployment topology（单进程单端口） | 5 |
| Figure 6.1 | Test pyramid | 6 |
| Figure 6.2 | **MMLU Δ bar chart（12 学科，正绿负红）** | 6 |
| Figure 7.1 | 12-month roadmap（里程碑表或 Gantt） | 7 |
| Table 1.1 | Competitor comparison matrix（≥5 产品 × 4 维度） | 1 |
| Table 1.2 | SMART objectives ×5 | 1 |
| Table 1.3 | **Personas ×3**（Persona C 教师明确列为非目标用户） | 1 |
| Table 2.1 | Requirements sources / elicitation（四来源 + 局限） | 2 |
| Table 2.2 | **MoSCoW matrix（14 行 R01–R14）** | 2 |
| Table 2.3 | **NFR specification（5 类 × 指标 × 度量方法）** | 2 |
| Table 3.1 | Use case summary（6 个用例一行一个） | 3 |
| Table 4.1 | **ADR matrix（≥6 行，代价列不得为空）** | 4 |
| Table 5.1 | Technology stack | 5 |
| Table 5.2 | **8 端点 API contract** | 5 |
| Table 5.3 | Domain model fields（5 模型） | 5 |
| Table 5.4 | 12 题分布（4 学科 × 陷阱数 × 雷达维度） | 5 |
| Table 5.5 | TrapDetail 四字段教学功能 | 5 |
| Table 5.6 | **查表 vs LLM 生成（含「我们输掉的那一行」）** | 5 |
| Table 5.7 | Environment requirements（部署环境要求） | 5 |
| Table 6.1 | **Test file inventory（9 文件 / 78 函数 → 145 用例）** | 6 |
| Table 6.2 | Adversarial test groups ×6 | 6 |
| Table 6.3 | **MMLU 12 学科 Base vs Ours** | 6 |
| Table 6.4 | RAGAS evaluation（数值不足则写「未跑完」） | 6 |
| Table 6.5 | **Requirements achievement evaluation（逐条对 R01–R14）** | 6 |
| Table 7.1 | Commercialisation assumptions（3 种情景） | 7 |

> 共 **17 图 / 21 表**，满足"≥18 张图表"的门槛。此表与 `reports/cycle3_task_packs/README.md` §5.1 逐行一致（已交叉核对）；任何新增图表须向吴宇轩申请编号。

### 2.4 各章硬性写作要素（少一项即视为未完成）

- **Ch1**：竞品对比表（≥5 个 × 4 维度，素材来自 `reports/competitor_analysis.md`）+ Value Proposition Canvas + **3 个 Persona（Table 1.3）+ stakeholders 表** + 5 条可度量 SMART 目标 + **一段明确的 business value 论述**（官方 Brief 点名要求）。
- **Ch2**：需求获取四来源表（Table 2.1，含局限声明）+ 14 行 MoSCoW（**Won't ≥3 条**，这是"初创感"的核心）+ **NFR 五类可度量指标表** + 四条 Won't 的"是什么/为何诱惑/为何砍掉"三段式论证。
- **Ch3**：用例图 + **6 个用例描述**（每个必备前置条件/主流程/异常流/后置条件四段）+ 答题状态机 + 用例↔需求映射。
- **Ch4**：架构总览图（自绘）+ 复用 2 张 UML + **新画类图** + **ADR 矩阵 ≥6 行，每行写明"否决的方案 + 否决理由 + 付出的代价"** + 控制流图。
- **Ch5**：技术栈表 + 8 端点契约表 + 领域模型字段表 + 类图关系说明 + 陷阱四类生成规则 + 诊断伪代码（≤20 行）+ 一张"错选 → trap_id → 前置知识缺口 → 雷达维度"因果链示意 + UI 截图 ≥2 张 + 一键启动命令。
- **Ch6**：测试金字塔 + 145 用例分布表（**必须解释 78 → 145 的参数化关系**）+ 25 个对抗性用例归 6 组 + **MMLU 12 学科表（3 平、2 负必须如实呈现并解释）** + **NFR 逐条达标评估表** + Threats to Validity ≥5 条。
- **Ch7**：5 条 SMART 目标逐条结账 + Limitations ≥5 条 + 3 种商业化假设（标明为假设）+ **What failed ≥3 条，不准只写成功** + 12 个月路线图。

---

## 3. "去 AI 感 / 出初创感"十条硬规矩（全组强制执行）

> 导师说"太像 AI agent 做的"——这一节的每一条都是针对那句话的解药。评审老师识别 AI 文风只用三招：有没有取舍、有没有失败、有没有具体数字。

1. **每个技术选择必须写"被否决的备选方案 + 否决理由 + 代价"**。只写"我们用了 X"= 不合格；"我们用了 X，因为我们评估过 Y 和 Z，Y 因为…被否决，代价是…"= 合格。
2. **必须报告负面结果**。`final_systematic_report.csv` 里有 3 个学科 0 提升、2 个负提升（US History −1.0 pp、HS Physics −1.3 pp），这是**加分项**，不许删。
3. **每个数字必须有出处**。正文出现的任何数字后面标注来源文件路径（例如 "145 test cases, source: `tests/`"）。编造数字 = 直接重写。
4. **禁用空词**：赋能、闭环、生态、全方位、深度融合、显著提升、"综上所述"。全文检索到即删。
5. **图 > 表 > 文字**。每章至少 2 张图/表，每张必须有 `Figure N: ...` / `Table N: ...` 编号 + 一句话说明 + 数据来源。
6. **先写约束，再写能力**。开头强调"12 周 / 10 人 / 零预算 / 必须离网"，后面的东西才显得合理，而不是显得浮夸。
7. **第一人称复数 + 具体 commit/周次**。"In Week 4 we merged commit `a0b1efd`…" 比 "the system was developed" 可信一百倍。
8. **英式拼写 + 短句**：organisation / prioritise / behaviour；单句不超过 30 词；禁止中文式长链定语。
9. **引用真实文献**：Sommerville（软件工程）、Cockburn（用例）、Ries（精益创业）、Osterwalder（商业模式画布）、Nielsen（可用性）、Es et al. 2023（RAGAS）。≥25 条，Harvard 格式。
10. **不许整段生成后直接贴**。每段必须由署名作者口述确认过内容，然后再落笔成英文——**能被组会追问三段而不卡壳**，是本节唯一验收标准。

---

## 4. 分工矩阵（10 人 · 责权到人 · 每人署名 ≥3 页）

| # | 成员 | 学号 | 角色 | Cycle 3 负责内容 | 页数 | 任务包 |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 1 | 吴宇轩 | 50106070 | PM / Lead | Title/Abstract + **Ch7** + 附录 A 统筹 + 全篇统稿与提交 | 5–6 | （组长自留） |
| 2 | 林泳桐 | 50106038 | Lead BA | **Ch1** Introduction and Project Context | 5–6 | [01](cycle3_task_packs/01-ch1-introduction-lin-yongtong.md) |
| 3 | 张梓健 | 50106035 | BA | **Ch2** Functional and Non-Functional Requirements | 6–7 | [02](cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md) |
| 4 | 谢炜昕 | 50106034 | QA / 报告 Lead | **Ch3** Use Cases and Requirements Modelling + 附录 B + 全篇格式统稿 | 6–7 | [09](cycle3_task_packs/09-ch3-use-cases-xie-weixin.md) |
| 5 | 王思鉴 | 50106045 | 架构 | **Ch4** System Design and Architecture | 9–11 | [04](cycle3_task_packs/04-ch4-architecture-wang-sijian.md) |
| 6 | 江昊 | 50106065 | PoC Lead Dev | **Ch5.1–5.2** 技术栈/软件结构/接口契约/领域模型 + 附录 D | 5–6 | [05](cycle3_task_packs/05-ch5-1-2-implementation-jiang-hao.md) |
| 7 | 董思钦 | 50106060 | PoC 逻辑 | **Ch5.3–5.4** 题库陷阱工程 + 诊断算法 | 5–6 | [06](cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md) |
| 8 | 习羽赛 | 50105989 | UI/UX | **Ch5.5** GUI design and implementation | 4–5 | [03](cycle3_task_packs/03-ch5-5-gui-xi-yusai.md) |
| 9 | 梁子铉 | 50106037 | 部署/媒体 | **Ch5.6** Deployment & reproducibility + 视频/PPT 大纲 | 3–4 | [08](cycle3_task_packs/08-ch5-6-deployment-liang-zixuan.md) |
| 10 | 杨明杰 | 50106061 | 测试 | **Ch6** Testing and Evaluation + 附录 C | 7–8 | [07](cycle3_task_packs/07-ch6-testing-yang-mingjie.md) |

**交叉审校（Peer Review）配对**——防止"各写各的、谁也不懂谁"：

| 审稿人 | 被审章节 | 目的 |
| :--- | :--- | :--- |
| 谢炜昕 | Ch5（全） | 报告 Lead 必须通读实现章 |
| 林泳桐 | Ch2、Ch3 | BA 视角校验需求与用例一致性 |
| 张梓健 | Ch1、Ch7 | 价值主张与结论必须口径一致 |
| 王思鉴 | Ch4 的自审 + Ch6 | 架构视角校验证据链 |
| 江昊 | Ch5.3–5.6 | 实现视角校验同伴内容 |
| 杨明杰 | Ch4.6、Ch6.5 | 质量属性必须与 NFR 表对得上 |

---

## 5. 三周里程碑与两道质量门禁

### Week A（第 1 周）：骨架与素材 —— 门禁 G1

| 交付 | 负责人 | 完成标准 |
| :--- | :--- | :--- |
| 各章 `outline.md`（≥12 行三级标题）+ 素材清单（用了哪些仓库文件/图/数据） | 9 位组员 | 提交到自己分支的 `reports/final_report/chXX/outline.md` |
| 全篇图表编号表（Figure 1.1–7.1 / Table 1.1–6.4 预分配，见 §2.3） | 吴宇轩 | 无编号冲突 |
| 统一模板（Times New Roman 12pt / 行距 1.5 / 页边距 2.54 cm / A4 单栏） | 谢炜昕 | `reports/final_report/_template/` |
| 组内 30 分钟答辩：每人讲自己那章 3 分钟 | 全员 | 讲不出来 → 打回重认领 |

> **G1 门禁**：逾期未交 outline 者，在 Appendix A（Group Workload Profile）中按模板如实记 `No submission`，并把章节收回由 PM 代写。这条规矩必须提前在群里说清楚。

### Week B（第 2 周）：初稿 —— 门禁 G2

| 交付 | 完成标准 |
| :--- | :--- |
| 各章初稿 | 达到目标页数 60% 以上，图表已就位，引用已标注 |
| 交叉审校意见 | 每位审稿人对被审章节给出 ≥5 条书面意见（`reports/final_report/reviews/`） |
| 组会演练 | 全员能回答 `supervisor_qa_defense_library.md` 中自己章节相关的 ≥5 个问题 |

> **G2 门禁**：初稿查重与文风扫描——检索第 3 节禁用词清单；任一段落无法被作者口述解释，退回重写。

### Week C（第 3 周）：合稿与提交

1. 谢炜昕统稿：统一术语、统一图表编号、统一 Harvard 引用、统一英式拼写；
2. 吴宇轩导出 DOCX + PDF，检查目录 / List of Figures / List of Tables / 页码为自动域；
3. 全篇朗读检查 + 数字溯源抽查（随机抽 10 个数字核对源文件）；
4. 提交前审计（见第 7 节清单）。

---

## 6. 组会应对策略（把"回答不上来"变成"有备而来"）

1. **每次组会前 24 小时**：每人从 `supervisor_qa_defense_library.md` 中领 5 个问题，用中文写三句话答案，发群里互评。
2. **组会中固定开口顺序**：导师问架构 → 王思鉴先答；问测试 → 杨明杰先答；问商业价值 → 林泳桐先答；问用例/需求 → 谢炜昕、张梓健答；问实现 → 江昊、董思钦、习羽赛答；组长只做总结与兜底，**不许每次都抢答**（抢答本身就是"其他人是摆设"的证据）。
3. **答不上来时的标准动作**：不要说"这个是我组员做的"，要说 **"这一块我们本周正在补数据，会在报告第 X 章给出，我下周带着实测数字来回答"**——承认 + 给出交付时间 + 落成文字。
4. **主动抛问题**：每次组会至少主动提一个"我们正在纠结的决策点"（例如：是否该把图谱增强在物理学科的负提升写进报告），让导师参与决策。**这是打破"AI 自导自演"印象最有效的一招。**

---

## 7. 风险登记与提交前必做清单

| 风险 | 等级 | 触发信号 | 缓解措施 |
| :--- | :-: | :--- | :--- |
| 组员继续不动笔 | **高** | Week A 第 3 天仍无 outline 提交 | 立刻启用"章节回收 + Appendix A 如实记录"；同步单独约谈 |
| 报告写成"功能说明书" | **高** | 全文出现"本系统具有…功能"句式 >5 次 | 强制补充每章"被否决的方案"小节 |
| 结构偏离官方章节表 | **高** | 出现 Brief 里没有的章标题 | 提交前用 §0.1 对照表逐节勾选 |
| 数字与仓库不一致 | 中 | 抽查 10 个数字有 ≥1 个对不上 | 建立 `reports/final_report/_evidence/number_registry.md` 逐条登记来源 |
| 图表编号/引用错乱 | 中 | 交叉引用出现 "Figure ?" | Week C 只在合稿阶段统一编号 |
| 组长再次单点承担 | **高** | 组长第 2 周写稿时间 > 全组 40% | 严格执行第 4 节责权到人 |

### 提交前必做（一个都不能漏）

- [ ] **⚠️ 立刻轮换泄露的凭证**：`graphrag（终）/real_graph_engine.py` 中硬编码了云端 Neo4j 的用户名与密码，且该文件**已在 git 历史中提交并推送到 GitHub**。请立刻在 Neo4j Aura 控制台**重置密码**，并把常量改为 `os.getenv()` 读取（同文件的 `DASHSCOPE_API_KEY` 已用 `os.getenv`，但 `import os` 缺失，顺手补上）。这件事可以直接写成 Ch5.6 的一次安全事件复盘——**真实、可核查、极有说服力**。
- [ ] 报告 PDF 内不含任何真实 API Key / 密码 / 学号以外的隐私数据；
- [ ] **正文无源码**（官方硬性禁止）；伪代码 ≤20 行；JSON 示例不算源码，可以保留；
- [ ] 格式合规：A4 / 四边 2.54 cm / 单栏 / 12 pt / Arial 或 Times New Roman / 1.5 倍行距；
- [ ] 目录、List of Figures、List of Tables、页码为 Word 自动域，导出 PDF 后逐页检查；
- [ ] 正文页数落在 **40–60 页**（不含前置页、References、附录）；
- [ ] Harvard 引用与正文一一对应，无孤立引用；
- [ ] **Appendix A 使用 MyAberdeen 官方模板**，10 人全部签署；有异议者按 Brief 规定不签字并邮件 Course Coordinator；
- [ ] 全文检索第 3 节禁用词清单，命中数为 0；
- [ ] 视频（20% 权重，15 分钟，**MP4 且必须出镜**）脚本与 Ch1/Ch6/Ch7 口径一致，避免自相矛盾；
- [ ] PoC 软件 ZIP 含：源码 + 可运行版本 + 依赖 + **User Manual（PDF，8–12 页）**。

---

## 8. 工件索引

- 本计划：[`reports/cycle3_master_plan.md`](cycle3_master_plan.md)
- 9 份任务包：[`reports/cycle3_task_packs/README.md`](cycle3_task_packs/README.md)
- 组会防身库：[`reports/supervisor_qa_defense_library.md`](supervisor_qa_defense_library.md)
- Spec Kit 规范包：[`spec.md`](../specs/003-cycle3-startup-report/spec.md) · [`plan.md`](../specs/003-cycle3-startup-report/plan.md) · [`tasks.md`](../specs/003-cycle3-startup-report/tasks.md)
- 官方 Brief：[`JC2001-GroupProjectDescription-and-Requirements-2026-27.txt`](../JC2001-GroupProjectDescription-and-Requirements-2026-27.txt)
- 历史素材：[`competitor_analysis.md`](competitor_analysis.md) · [`phase2_cycle2_progress_report.md`](phase2_cycle2_progress_report.md) · [`project_proposal.md`](project_proposal.md) · [`api_frontend_mapping.md`](api_frontend_mapping.md) · [`report_data_contract.md`](report_data_contract.md) · [`figures/`](figures/README.md)
