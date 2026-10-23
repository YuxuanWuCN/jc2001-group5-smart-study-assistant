# JC2001 Group 5: Smart Study Assistant System (智学罗盘)

An intelligent study and misconception-diagnostic assistant powered by Knowledge Graphs and LLMs, developed for undergraduate STEM and professional exam preparation.

Course: **JC2001 Introduction to Software Engineering (Academic Year 2026–27)**  
Institution: **University of Aberdeen**  
Degree Programme: **BSc in Business Management and Information Systems (BSc BMIS)**  
Academic Supervisor: **Dr. Shahzad Mumtaz** (`shahzad.mumtaz@abdn.ac.uk`)  

---

## 🧭 当前周期

> **Cycle 3 · Reports Cycle**——软件基线已冻结，本周期**不写新功能**，唯一目标是把 50% 权重的期末 Technical Report 从「0 页」推进到「可提交的初创级技术与落地报告」。
> 与 004 审计并行（见下方"并行周期"）。

| 项 | 事实（可核验） |
| :--- | :--- |
| 软件基线 | 8 个 API 端点 · **145 个 pytest 用例全绿** · 12 题 × 4 学科 × 36 陷阱 · 3 张 UML 图 |
| 报告硬指标 | 正文 40–60 页 · ≥18 张图表 · ≥25 条 Harvard 引用 · 10 人各署名 ≥3 页 · 正文禁贴源码 |
| 总纲文档 | [`reports/cycle3_master_plan.md`](reports/cycle3_master_plan.md) |
| 规范包 | [`specs/003-cycle3-startup-report/spec.md`](specs/003-cycle3-startup-report/spec.md) |

---

## 👥 Team Roster & 全周期团队分工全景 (Group 5)

本团队共 10 人，严格遵循 JC2001 软件工程全生命周期治理规范。下表记录全员在 **Cycle 1（概念与立项）**、**Cycle 2（需求、UML与MVP）** 与 **Cycle 3（期末大报告与交付）** 中的职责映射与产出归属：

| # | 姓名 / 学号 | 团队角色 | Cycle 1 · 概念与立项 (09-14 → 09-25) | Cycle 2 · 需求建模与 PoC MVP (09-28 → 10-16) | Cycle 3 · 期末大报告与交付收口 (10-17 → 12-14) | 任务包 / 章节归属 |
| :-: | :--- | :--- | :--- | :--- | :--- | :-: |
| 1 | **吴宇轩**<br>`50106070` | **Team Leader<br>& Project Manager** | 项目总治理、立项提案统筹、导师 Kick-off 会议组织、WBS 工时治理 | Sprint 迭代规划与风险登记、基线合并管理、UML 交叉审核、004 实证审计 | 前置页（Title/Decl/Abstract/TOC）+ **Ch7** 结论与未来展望 + **附录 A** 全员工时档案统筹 + 全篇总集成提交 | 组长统筹 / Ch7 |
| 2 | **林泳桐**<br>`50106038` | **Lead Business Analyst<br>& 联合课题奠基人** | **Phase 1 Lead**：课题构想发起、痛点调研、考点概念建模、提案背景与目标起草 | 需求规格深化、全局用例图建模、用户旅程图设计、需求追踪矩阵构建 | **Ch1** Introduction and Project Context（5–6 页：问题陈述、竞品矩阵、SMART 目标、认知架构） | [任务包 01](reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md) |
| 3 | **王思鉴**<br>`50106045` | **System Architect<br>(UML & Knowledge Graph)** | 技术可行性分析、GraphRAG 拓扑设计、系统架构范围界定 | **Phase 2 Co-Lead**：UML 2.5 核心模型设计（Class图、Sequence时序图、Component组件图）、Neo4j 知识本体建模 | **Ch4** System Design and Architecture（9–11 页：四层架构、ADR 决策、上下文模型、图拓扑） | [任务包 04](reports/cycle3_task_packs/04-ch4-architecture-wang-sijian.md) |
| 4 | **江昊**<br>`50106065` | **PoC Lead Developer<br>(GraphRAG & Backend)** | 原型可行性预研、Neo4j AuraDB 云端连通性与 API 压测 | **Phase 3 Co-Lead**：FastAPI 后端脚手架、Pydantic CamelModel 规范契约、Cypher 遍历引擎实现 | **Ch5.1–5.2** 技术栈、软件结构、API 契约、领域模型 + **附录 D** 技术栈规格表（5–6 页） | [任务包 05](reports/cycle3_task_packs/05-ch5-1-2-implementation-jiang-hao.md) |
| 5 | **谢炜昕**<br>`50106034` | **Lead QA & Report Lead<br>& 联合课题奠基人** | **课题奠基人**：提案学术规范审核、格式合规检查、学术诚信声明签署 | 测试策略制定、UML 一致性审计、评测引擎基线对比（`systematic_eval_engine.py`） | **Ch3** Use Cases and Requirements Modelling（6–7 页）+ **附录 B** 全量用例规格书 + 全篇格式统稿 | [任务包 09](reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md) |
| 6 | **张梓健**<br>`50106035` | **Business Analyst<br>(User Stories & NFR)** | 用户画像（Persona）定义、备考压力问卷分析、系统收益模型 | **Phase 2 Co-Lead**：用户故事拆解、Gherkin 验收标准、非功能需求（NFR）与 MoSCoW 边界矩阵 | **Ch2** Functional and Non-Functional Requirements（6–7 页：14 条 MoSCoW 规格、NFR 度量） | [任务包 02](reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md) |
| 7 | **习羽赛**<br>`50105989` | **UI/UX Designer<br>& Frontend Engineer** | 初始交互线框草图绘制、交互流程设计、提案 UI 配图 | 高保真交互设计、Cyber Obsidian 深浅双主题、ECharts 五维认知雷达图集成、对比沙盒组件 | **Ch5.5** Graphical User Interface（4–5 页：设计哲学、组件状态机、响应式适配走查） | [任务包 03](reports/cycle3_task_packs/03-ch5-5-gui-xi-yusai.md) |
| 8 | **董思钦**<br>`50106060` | **PoC Logic Developer<br>(Diagnosis & Quiz)** | 诊断考点结构调研、SMART 目标细化、MMLU 基准题库收集 | **Phase 3 Co-Lead**：认知陷阱工程与诊断算法、12 题 36 陷阱矩阵设计、苏格拉底追问逻辑实现 | **Ch5.3–5.4** 题库陷阱工程与认知诊断算法（5–6 页：因果拓扑链、算法复杂度分析） | [任务包 06](reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md) |
| 9 | **杨明杰**<br>`50106061` | **Software Testing Lead<br>& User Manual Author** | 质量度量与测试方案规划、pytest 工具链选型与评估 | 自动化测试用例编写、边界与负向测试、HTTP 429 容错与重试测试、**145 个用例全绿基线** | **Ch6** Testing and Evaluation（7–8 页）+ **附录 C** 测试日志 + 8–12 页 PoC User Manual PDF | [任务包 07](reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md) |
| 10 | **梁子铉**<br>`50106037` | **Deployment & Media Lead<br>(DevOps & Video)** | 团队协同环境搭建、演示时间线规划、媒体素材准备 | 环境容器化与部署脚本、Git 工作流守则执行监控、PoC 演示运行环境保障 | **Ch5.6** Deployment and Reproducibility（3–4 页，初稿已就绪）+ 15 分钟演示视频制作 + 演示 PPT | [任务包 08](reports/cycle3_task_packs/08-ch5-6-deployment-liang-zixuan.md) |

---

## 📦 文件周期归属

判定依据：git 提交时间 + 里程碑合并提交 + 各 `specs/0xx/spec.md` 创建日期（`reports/` 目录曾在 2026-10-09 被删除重建，因此**不采用文件修改时间**）。

### Cycle 1 · 概念、组队与可行性（2026-09-23 起）

**产出**：项目立项、团队分工、初步可行性论证与竞品分析。这是"问题值不值得做"的周期。

| 路径 | 内容 |
| :--- | :--- |
| `docs/archive/practical1_deliverables.md` | Practical 1 破冰、角色分配与团队协作记录 |
| `docs/archive/ORIGINAL_REQUEST.md` | Cycle 1 原始需求存档（含交付验收清单） |
| `reports/project_proposal.md` / `.pdf` / `.docx` | 正式项目提案（9 月 25 日提交版） |
| `reports/week1_team_review_pack.pdf` / `_zh.docx` | Week 1 团队复盘包（中英两版） |
| `reports/competitor_analysis.md` | 六维竞品对比矩阵与认知架构分析（后续 Ch1 素材） |
| `reports/JC2001_Group5_项目规划书.pdf` / `.docx` | 项目规划书（中文版） |
| `scripts/verify_week1_deliverables.py` | Week 1 交付物一致性校验脚本 |
| `scripts/generate_proposal_docs.py` | 提案 docx / pdf 自动生成脚本 |
| `scripts/generate_project_plan_cn.py` | 中文规划书生成脚本 |
| `scripts/generate_review_pack.py` / `_zh.py` | 复盘包生成脚本 |

### Cycle 2 · 需求工程、系统建模与 PoC MVP（2026-10-08 → 10-16 里程碑）

**产出**：可运行 MVP + 需求基线 + UML 模型 + 测试套件 + Cycle 2 进度报告。这是"把东西做出来"的周期。

| 路径 | 内容 |
| :--- | :--- |
| `backend/` | FastAPI 后端（`app/models`、`app/routers`、`app/services`、`app/data/seed_questions.py`、`run.py`） |
| `frontend/` | 零构建前端（`index.html` / `style.css` / `app.js`），深色控制台 + 双语 |
| `tests/` | 9 个测试文件、78 个 test 函数、参数化展开后 **145 个用例** |
| `specs/001-landing-and-auth-portal/` | 门户与学号登录规范包（spec / plan / research / data-model / contracts / quickstart） |
| `specs/002-frontend-visual-overhaul/` | Cyber Obsidian 视觉体系、对比沙盒、Reasoning Accordion 规范包 |
| `reports/phase2_tasks/` | 四路并行任务包（需求 / 架构 / 后端 / QA 报告） |
| `reports/week2_execution_guide.md` | Phase 2 第 2 周团队执行计划 |
| `reports/week3_plan.md` + `week3_supervisor_briefing_and_qa.*` | Week 3 计划与导师简报问答 |
| `reports/phase2_cycle2_progress_report.md` / `.docx` / `.pdf` | **Cycle 2 里程碑进度报告**（936 行 / 9 节） |
| `reports/phase2_supervisor_briefing_bilingual.docx` + `_check.json` | 中英双语导师简报 + 校验结果 |
| `reports/api_frontend_mapping.md` + `api_frontend_mapping/` | 前端–后端 API 全量映射（md / mmd / png / svg） |
| `reports/figures/` | 上下文模型图、全局用例图、排雷时序图（`.mmd` / `.png` / `.svg` 三件套） |
| `reports/diagrams/` | `JC2001_Week6_UML_Lab_Practices.drawio` 与 drawio 打开页 |
| `reports/assumptions.md` / `report_data_contract.md` | 假设登记表与报告数据契约 |
| `reports/week6_lab_submission_guide.md` | Week 6 UML 实验提交指南 |
| `scripts/verify_poc.py` | PoC 端到端自检脚本 |
| `scripts/generate_phase2_briefing.py` | 导师简报生成脚本 |
| `graphrag（终）/` | GraphRAG 自建管线（`auto_builder.py`、`real_graph_engine.py`、`systematic_eval_engine.py`、`ragas_evaluator.py`）+ MMLU 12 学科 CSV |
| `.env.example` / `requirements.txt` / `.gitignore` | 环境与依赖基线 |

### Cycle 3 · Reports Cycle（2026-10-17 起，当前周期）

**产出**：期末大报告 7 章正文 + 4 附录、9 份组员任务包、导师问答库、部署与视频素材。软件基线冻结。

| 路径 | 内容 | 状态 |
| :--- | :--- | :-: |
| `reports/cycle3_master_plan.md` | **Cycle 3 总纲**：报告蓝图、分工矩阵、三周里程碑、风险登记 | ✅ |
| `specs/003-cycle3-startup-report/` | Cycle 3 规范包（spec / plan / tasks） | ✅ |
| `reports/cycle3_task_packs/` | 9 份组员任务包（Ch1–Ch7 逐章拆解）+ README | ✅ |
| `reports/supervisor_qa_defense_library.md` | 组会问答防身库 | ✅ |
| `reports/final_report/ch05_liang_zixuan/` | Ch5.6 部署与可复现性初稿、图 5.5、演示大纲、来源清单 | 🟡 初稿 |
| `README.md`（本文件） | 周期归属清单 + 当前周期任务看板 | 🟡 本次更新 |

> 说明：其余章节（Ch1–Ch4、Ch5.1–5.5、Ch6、Ch7、附录 A–D）尚未在仓库落地，责任人见下方待办表。

### 并行周期 004 · 画像与幻觉主张实证审计（2026-10-18 起）

**产出**：一组可复现的审计证据 + 诚实结论 + 报告句子级改写清单。**不新增产品功能。**

| 路径 | 内容 | 状态 |
| :--- | :--- | :-: |
| `specs/004-persona-hallucination-audit/spec.md` | 审计规格（E0–E3 证据等级 / L1–L4 幻觉分级 / V0–V3 结论等级） | ✅ |
| `specs/004-persona-hallucination-audit/tasks.md` | T001–T024 任务清单 | ✅ |
| `specs/004-persona-hallucination-audit/contracts/` | 四份契约（audit-result schema / online-experiment / report-claim-contract / quickstart） | ✅ |
| `specs/004-persona-hallucination-audit/plan.md` | 实现计划（含本次 README 整理的周期判定依据） | ✅ |
| `scripts/audit_hallucination_l1_l3.py` | L1 内容 / L2 归因 / L3 泄漏审计器 | ✅ |
| `scripts/audit_persona_claims.py` | 画像断言溯源与需求映射审计器 | ✅ |
| `scripts/audit_online_baseline.py` | 在线 LLM 基线对照脚手架（无 Key 时退出码 0 跳过） | ✅ |
| `reports/audit/*.csv` + `verdict.json` | 审计产物（L1 84 行 / L2 36 行 / L3 12 行） | ✅ |

### 课程输入（非周期产物，仅作依据）

仓库内已 tracked：`docs/course/2026-27-GroupProjectDescription-and-Requirements.txt`（官方 Brief）、`docs/course/2026-27-Week1-Lecture1-Introduction&CourseOverview.txt`、`docs/course/2026-27-Week1-Practical1-IntroductionsGroups&Projects.txt`。

其余讲义（`JC2001-GroupProject-SupervisorAllocation.pdf`、`(Week1/4/5/6/7)-*.pdf`、`Lecture 4.pdf`、`1-Scenario Based Architecture.pdf`、`UML Draw Practices.pdf`、`User-Case-Diagram-Lab.pdf`、`project_proposal-SM.pdf`）按 `.gitignore` 的 `/*.txt`、`/*.pdf` 规则**不入库**，留在本地 `docs/course/` 即可。

### 根目录清理与工作区卫生治理（已于 2026-10-23 全面闭环）

严格遵循宪章原则 V「根目录零污染」，已实现工作区 100% 洁净基线：

| 类别 / 原位置 | 现位置 / 处置 | 治理意义 |
| :--- | :--- | :--- |
| `practical1_deliverables.md` | → `docs/archive/practical1_deliverables.md` | 历史立项存档，已同步更新自动化验证路径 |
| `ORIGINAL_REQUEST.md` | → `docs/archive/ORIGINAL_REQUEST.md` | 原始需求凭据归档 |
| `project-proposal-draft.md` | 物理删除 | 清理重复无用的未定稿草稿 |
| `(Week1)*.txt`、`JC2001-GroupProjectDescription*.txt` | → `docs/course/` | 官方课程说明规范归位 |
| 根目录 14 份课程 PDF 讲义与实验材料 | → `docs/course/` | 课件全部移入子目录，根目录不再散落讲义 |
| `scraped_*.js/html`、`_extract_*.py`、`_unpack.py`、`_week5_*` | 彻底物理删除 | 清理爬虫临时反编译碎屑与缓存，消除根目录垃圾 |
| `graphrag（终）/` 与 `backend/` 泄露密钥 | 环境变量脱敏 (`os.getenv`) | 杜绝凭证泄露风险，符合学术诚信与代码安全准则 |
| `.gitignore` 规则固化 | 固化 `/*.pdf`、`/*.txt`、临时脚本过滤 | 彻底防止未来会话再次产生根目录污染 |

---

## 🎯 当前周期（Cycle 3）待办

### 分工矩阵 · 每人负责一章（责权到人，见 `cycle3_master_plan.md` §4）

| 成员 | 负责章节 | 页数 | 任务包 | 交付状态 |
| :--- | :--- | :-: | :--- | :-: |
| 吴宇轩 | Title/Abstract + **Ch7** + 附录 A 统筹 + 全篇统稿提交 | 5–6 | （组长自留） | ⬜ |
| 林泳桐 | **Ch1** Introduction and Project Context | 5–6 | [01](reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md) | ⬜ |
| 张梓健 | **Ch2** Functional and Non-Functional Requirements | 6–7 | [02](reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md) | ⬜ |
| 谢炜昕 | **Ch3** Use Cases and Requirements Modelling + 附录 B + 全篇格式统稿 | 6–7 | [09](reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md) | ⬜ |
| 王思鉴 | **Ch4** System Design and Architecture | 9–11 | [04](reports/cycle3_task_packs/04-ch4-architecture-wang-sijian.md) | ⬜ |
| 江昊 | **Ch5.1–5.2** 技术栈 / 软件结构 / 接口契约 / 领域模型 + 附录 D | 5–6 | [05](reports/cycle3_task_packs/05-ch5-1-2-implementation-jiang-hao.md) | ⬜ |
| 董思钦 | **Ch5.3–5.4** 题库陷阱工程 + 诊断算法 | 5–6 | [06](reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md) | ⬜ |
| 习羽赛 | **Ch5.5** GUI design and implementation | 4–5 | [03](reports/cycle3_task_packs/03-ch5-5-gui-xi-yusai.md) | ⬜ |
| 梁子铉 | **Ch5.6** Deployment & reproducibility + 视频/PPT 大纲 | 3–4 | [08](reports/cycle3_task_packs/08-ch5-6-deployment-liang-zixuan.md) | 🟡 初稿已提交 |
| 杨明杰 | **Ch6** Testing and Evaluation + 附录 C | 7–8 | [07](reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md) | ⬜ |

### 三道关卡

**Week A · 骨架与素材（门禁 G1）**
- [ ] 每人提交 `reports/final_report/chXX/outline.md`（≥12 行三级标题）+ 素材清单，说明用了哪些仓库文件 / 图 / 数据
- [ ] 吴宇轩：全篇图表编号表（Figure 1.1–7.1 / Table 1.1–6.4 预分配，见总纲 §2.3）
- [ ] 谢炜昕：统一模板 `reports/final_report/_template/`（Times New Roman 12pt / 1.5 倍行距 / 页边距 2.54 cm / A4 单栏）
- [ ] 全员：组内 30 分钟答辩，每人讲自己那章 3 分钟；讲不出来 → 打回重认领

**Week B · 初稿（门禁 G2）**
- [ ] 各章初稿达到目标页数 60% 以上，图表已就位，引用已标注
- [ ] 交叉审校：每位审稿人对被审章节给出 ≥5 条书面意见，落 `reports/final_report/reviews/`
- [ ] 全员：能回答 `supervisor_qa_defense_library.md` 中自己章节相关 ≥5 个问题
- [ ] 文风扫描：检索总纲 §3 禁用词清单，命中数为 0；任一段落无法被作者口述解释则退回重写

**Week C · 合稿与提交**
- [ ] 谢炜昕统稿：统一术语、图表编号、Harvard 引用、英式拼写
- [ ] 吴宇轩导出 DOCX + PDF，核对目录 / List of Figures / List of Tables / 页码为自动域
- [ ] 全篇朗读检查 + 随机抽 10 个数字核对源文件

### 交叉审校配对

| 审稿人 | 被审章节 |
| :--- | :--- |
| 谢炜昕 | Ch5（全） |
| 林泳桐 | Ch2、Ch3 |
| 张梓健 | Ch1、Ch7 |
| 王思鉴 | Ch4 自审 + Ch6 |
| 江昊 | Ch5.3–5.6 |
| 杨明杰 | Ch4.6、Ch6.5 |

### 提交前必做清单（一个都不能漏）

- [x] **已完成凭证脱敏与轮换**：`real_graph_engine.py`、`auto_builder.py`、`frontend/index.html` 的硬编码 Key / 密码已全面替换为 `os.getenv()` 环境变量动态注入与空缺占位，避免安全泄露。
- [x] **已完成根目录彻底清理与课件归位**：14 份课程 PDF 已归入 `docs/course/`，所有临时反编译/抓取碎屑已全部物理删除，经 `python -m pytest tests/ -q` 验证 145 用例零回归全绿。
- [ ] 报告 PDF 内不含任何真实 API Key / 密码 / 学号以外的隐私数据
- [ ] **正文无源码**（官方硬性禁止）；伪代码 ≤20 行；JSON 示例不算源码
- [ ] 格式合规：A4 / 四边 2.54 cm / 单栏 / 12 pt / Arial 或 Times New Roman / 1.5 倍行距
- [ ] 目录、List of Figures、List of Tables、页码为 Word 自动域，导出 PDF 后逐页检查
- [ ] 正文页数落在 **40–60 页**（不含前置页、References、附录）
- [ ] Harvard 引用与正文一一对应，无孤立引用
- [ ] **Appendix A 使用 MyAberdeen 官方模板**，10 人全部签署
- [ ] 全文检索禁用词清单，命中数为 0
- [ ] 视频（20% 权重，15 分钟，MP4 且必须出镜）脚本与 Ch1 / Ch6 / Ch7 口径一致
- [ ] PoC 软件 ZIP 含：源码 + 可运行版本 + 依赖 + **User Manual（PDF，8–12 页）**

---

## 🔬 并行周期 004 待办（画像与幻觉主张审计）

任务清单全文见 [`specs/004-persona-hallucination-audit/tasks.md`](specs/004-persona-hallucination-audit/tasks.md)。当前进度：**T001–T021 已落地**（审计脚本与产物已在 `reports/audit/`），待收尾项：

- [ ] T022 用 `contracts/audit-result.schema.json` 对 `reports/audit/verdict.json` 做全模式强校验
- [ ] T023 复跑 `python -m pytest tests/ -q`，确认 145 用例零回归
- [ ] T024 根目录零污染审查（与上方提交前清单最后一项合并执行）
- [ ] 把审计结论 V1（离线消除生成面）与改写对照表回灌 Ch1 / Ch2 / Ch6 正文

命令：

```powershell
python scripts/audit_hallucination_l1_l3.py
python scripts/audit_persona_claims.py
python scripts/audit_online_baseline.py     # 无 QWEN_API_KEY 时以退出码 0 跳过
```

---

## 🚀 Quickstart for Team Members

### 1. Environment Setup

```powershell
pip install -r requirements.txt
```

Python 3.13 recommended（当前基线实测为 3.13）。

### 2. 启动后端

```powershell
python backend/app/main.py
```

### 3. 打开前端

直接在浏览器打开 `frontend/index.html`（Chrome / Edge / Firefox，零构建）。

### 4. 回归验证

```powershell
python -m pytest tests/ -q     # 期望：145 passed
```

---

## 📜 Git 工作流（主仓库分支 + PR）

主仓库：`https://github.com/YuxuanWuCN/jc2001-group5-smart-study-assistant`（协作者权限为 **Write** 即可直接推分支）。

```powershell
# 开始每一项新工作前（这一步取代 "sync fork"）
git switch main
git pull origin main

# 从最新 main 切特性分支（命名参考：feature/<姓名拼音>-<内容>）
git switch -c feature/ch06-testing-yangmingjie

# 提交
git add -A
git commit -m "docs(ch6): outline and draft"

# 推送并开 PR
git push -u origin feature/ch06-testing-yangmingjie
```

规则：
- 直接在**主仓库**开分支，不再使用个人 fork 中转（`my-first-github` 上那两份 fork 仅作个人备份）。
- 绝不要提交凭证（`.env`、API token）或临时缓存。
- 提交前必须 `python -m pytest tests/ -q` 全绿（章程原则 III）。
- 根目录零污染（章程原则 V）：临时脚本放仓库外。
