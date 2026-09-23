# Original User Request

## 2026-09-16T06:55:14Z

Deliver a complete JC2001 Software Engineering Week 1 package for Group 5 (BSc BMIS, 10 members, Leader: 吴宇轩 50106070). This includes: (1) Practical Session 1 deliverables (icebreaker profile, 10-member role assignment matrix, project vision, and supervisor kickoff email), and (2) a submission-ready, academically rigorous 4-8 page Project Proposal in Markdown, DOCX, and PDF formats based on the "Smart Study Assistant System" powered by GraphRAG and Neo4j diagnostic engines.

Working directory: d:/jc2001
Integrity mode: benchmark

## Team Metadata
- **Course**: JC2001 Introduction to Software Engineering (2026-27)
- **Group Number**: Group 5
- **Programme of Study**: BSc (BMIS)
- **Team Leader & PM**: 吴宇轩 (50106070)
- **Team Members (10)**:
  1. 吴宇轩 (50106070) — Project Manager & Team Lead
  2. 林泳桐 (50106038) — Lead Business Analyst (Requirements Capture)
  3. 王思鉴 (50106045) — System Architect (UML & Knowledge Graph Architecture)
  4. 江昊 (50106065) — PoC Lead Developer (GraphRAG & Neo4j Engine)
  5. 谢炜昕 (50106034) — QA & Technical Report Lead
  6. 张梓健 (50106035) — Business Analyst (User Stories & Acceptance Criteria)
  7. 习羽赛 (50105989) — UI/UX Designer & Wireframe Lead
  8. 董思钦 (50106060) — PoC Logic Developer (Diagnostic API & Quiz Engine)
  9. 杨明杰 (50106061) — Software Testing & User Manual Lead
  10. 梁子铉 (50106037) — Presentation, Media & Deployment Lead

## Requirements

### R1. Practical 1 Session Deliverables Pack (`practical1_deliverables.md`)
Produce a complete practical session record matching JC2001 Practical 1 sheet:
- Comprehensive 10-member icebreaker answers covering all 5 questions from socards.org (instant cheer-ups, favourite food memory, hometown highlights, historical moments, energy restoration).
- 10-member role allocation matrix explicitly detailing responsibilities across all 4 project phases (Requirements, Design/UML, PoC Development, Report/Testing/Presentation).
- Project Topic definition addressing: WHAT the system does, WHO it targets, major technical/time constraints, and long-term vision.
- Formal academic email draft addressed to the academic supervisor from Team Leader 吴宇轩 requesting the Week 1/2 kick-off meeting to discuss project scope.

### R2. Submission-Grade Project Proposal (`reports/project_proposal.md`)
Develop an in-depth, academically rigorous proposal meeting JC2001 specifications:
- Proposal Title Page (Group 5, BSc BMIS, full roster of 10 student names and IDs).
- Section 1: Project Title: "To Design and Implement a Smart Study Assistant System for University Students".
- Section 2: Problem: Academic stress, disorganised learning materials, rote memorisation inefficiencies, and the critical lack of structured diagnostic feedback on conceptual blind spots and examination traps.
- Section 3: Solution: GraphRAG-powered smart study assistant integrating Neo4j knowledge graphs, automated exam question diagnostic parsing via LLM (Qwen/DashScope), trap/misconception relationship mapping ("易错于"), dynamic quiz generation, and student mastery visualization.
- Section 4: Objectives: Specific, Measurable, Achievable, Relevant, and Time-bound (SMART) objectives ensuring functional PoC delivery on or before 14 December 2026.
- Section 5: Benefits: Tangible academic and cognitive benefits for undergraduate students and instructors.
- Section 6: Timeline: 4 distinct project phases with explicit milestones from 14 September 2026 through 14 December 2026.
- Section 7: Action Plan: Full Work Breakdown Structure (WBS) table with specific tasks, assigned member(s), deadlines, and current progress status.
- Section 8: Formatting & Academic Integrity compliance declarations.

### R3. Automated Dual-Format Compilation (`scripts/generate_proposal_docs.py`)
Provide an automated Python compilation script converting the proposal into both `.docx` and `.pdf`:
- Strict formatting compliance: A4 paper, standard 1-inch (2.54 cm / 72 pt) margins on all 4 sides, single-column layout, 12pt Arial or Times New Roman body text, 1.5 line spacing.
- Dedicated unnumbered Proposal Title Page as required by the course guidelines.
- Body length strictly between 4 and 8 pages (excluding title page).
- Output files placed in `reports/project_proposal.docx` and `reports/project_proposal.pdf`.

### R4. Automated Verification & Quality Gate (`scripts/verify_week1_deliverables.py`)
Implement a standalone verification script that validates:
- Presence and non-emptiness of all required deliverables (`practical1_deliverables.md`, `reports/project_proposal.md`, `reports/project_proposal.docx`, `reports/project_proposal.pdf`).
- Absence of unresolved placeholders or bracketed marks.
- Page count of the compiled PDF/DOCX strictly between 4 and 8 pages (excluding Title Page).
- Inclusion of all 10 real group members and leader 吴宇轩 in both documents.

## Acceptance Criteria

### Output Files & Structure
- [ ] `practical1_deliverables.md` is generated with 10-member icebreaker answers, role matrix, project vision, and supervisor email draft.
- [ ] `reports/project_proposal.md` contains all 7 mandatory sections plus Title Page, properly structured with academic citations and technical depth.
- [ ] `scripts/generate_proposal_docs.py` compiles `reports/project_proposal.docx` and `reports/project_proposal.pdf` without runtime errors.
- [ ] The generated PDF proposal body length is verified to be between 4 and 8 pages (excluding Title Page).
- [ ] Typography conforms to A4, 1-inch margins, 12pt font, and 1.5 line spacing.
- [ ] `scripts/verify_week1_deliverables.py` passes all checks with return code 0.

## 2026-09-16T07:19:12Z

[User Request Update] 用户补充需求：全部交付物完成后，请另外生成一份专门供 10 位组员审阅检查的汇总版 PDF 文档（如 `reports/week1_team_review_pack.pdf`），包含：
1. 第一周任务总体完成情况与关键提交节点（9月25日 Proposal 提交要求）；
2. 10 位组员具体分工职责矩阵、破冰记录核对；
3. 开题报告（Project Proposal）核心设计精要与审查要点速览；
4. 导师首期开题会议沟通邮件草稿及组内准备事项；
5. 组员审阅确认清单（Review Checklist & Sign-off Table），便于全组同学在微信群或邮件中逐项核对确认。
请在生成完主交付物后确保该汇总审查 PDF 同步生成。

## 2026-09-17T00:40:08Z

Conduct an in-depth architectural and algorithmic competitive analysis of smart study, AI tutoring, and adaptive test-prep platforms (including commercial products like Khanmigo, Quizlet, Duolingo, and domestic test-prep apps, as well as foundational cognitive science models such as BKT, DKT, and IRT). Pinpoint the common underlying mechanisms shared across these competitors that our current "Smart Study Assistant" (Neo4j GraphRAG + Qwen-Turbo trap extractor + Socratic prompt) lacks, and formulate an actionable engineering evolution roadmap tailored to the JC2001 course scope.

Working directory: d:/jc2001
Integrity mode: development

## Requirements

### R1. Broad-Spectrum Competitor & Paradigm Deconstruction
Deconstruct the architectural foundations of leading market products and classical cognitive frameworks across four key categories:
1. **Generative LLM Socratic Tutors**: e.g., Khanmigo (Khan Academy), Socratic (Google), AI study agents.
2. **Spaced Repetition & Retention Engines**: e.g., Quizlet (Q-Chat, Leitner/SM-2 spaced repetition), Anki algorithms.
3. **Gamified Adaptive Practice**: e.g., Duolingo (Birdbrain adaptive difficulty adjustment, mastery learning loops).
4. **Classical Educational Data Mining & Cognitive Models**: e.g., Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), Item Response Theory (IRT), and computerized adaptive testing (CAT).

### R2. Common Underlying Logic Extraction (The "Shared DNA")
Identify and formulate the universal architectural and mathematical patterns that mature systems rely on, focusing on:
- Dynamic learner mastery state modeling (how student competence changes continuously over time).
- Memory retention and temporal decay curves (forgetting dynamics).
- Question difficulty and discrimination calibration (IRT parameter estimation vs. static question tagging).
- Error attribution and generative variant practice loops (closing the loop from diagnosis to remedial reinforcement).
- Scaffolding and pacing control (how systems prevent premature answer reveal or student frustration).

### R3. Systematic Gap Analysis Against Group 5 System
Directly benchmark the identified competitor mechanics against our current architecture:
- Current: Neo4j GraphRAG (考点/定理/易错于 连边), Qwen-Turbo zero-shot trap extractor, Socratic chat prompts, and static 5-dimension ECharts radar chart.
- Target: Identify exact missing layers (e.g., student-level temporal state tracking, dynamic difficulty weighting, variant problem synthesis).
- Compile an exhaustive comparison matrix highlighting mechanism, competitor implementation, our current status, and gap severity.

### R4. Actionable JC2001 Engineering Roadmap & Prototypes
Synthesize high-impact, realistic recommendations that Group 5 can incorporate into the JC2001 Technical Report (40–60 pages) and PoC software:
- Propose 1–2 lightweight algorithms (e.g., simplified BKT or Leitner memory decay queue on top of Neo4j nodes) feasible within the 12-week timeline.
- Provide sample schema enhancements for Neo4j and API contract specs.

## Acceptance Criteria

### Analytical Breadth & Depth
- [ ] Thoroughly covers all 4 competitor categories with explicit analysis of their algorithmic / state-machine foundations (not just UI/surface features).
- [ ] Formulates at least 4 common underlying mechanisms shared across competitors that our system currently lacks (e.g., dynamic knowledge tracing, retention decay, difficulty adaptation, remedial variant loops).

### Comparative Rigor
- [ ] Includes a structured comparison matrix contrasting Competitors vs. Our System across at least 6 core engineering dimensions.
- [ ] Clearly articulates the architectural bottlenecks of our current static GraphRAG approach when compared against stateful student modeling.

### Deliverable Feasibility
- [ ] Deliverable is generated and saved as a comprehensive technical report: `reports/competitor_analysis.md`.
- [ ] Includes concrete, executable recommendations and architectural design sketches (UML / schema extensions) directly reusable in the JC2001 Technical Report.

## 2026-09-22T04:50:39Z

将 **智学罗盘 SmartStudy AI** 的前端（`d:\jc2001\frontend\`，含 `index.html` 与 `style.css`）的整体视觉风格重构为 **DeepSeek Eval Harness 评测控制台风格**：深色背景默认主题、指标卡片、数据表格、进度条布局。`app.js` 中所有业务逻辑**严禁改动**，只允许修改 HTML 结构与 CSS。

Working directory: d:\jc2001\frontend
Integrity mode: demo

---

## Requirements

### R1. DeepSeek Eval Harness 视觉风格重构（style.css）

重写 `style.css`，使整体 UI 对齐 DeepSeek Eval Harness 评测控制台的设计语言：

- **色彩系统**：深色主题为默认（背景 ~`#0d1117` 或等效深蓝黑），亮色切换保留；品牌主色改为 DeepSeek 蓝（~`#4f8ef7` 或等效）。
- **布局**：导航栏改为左侧固定深色侧边栏（sidebar），右侧为主内容区域；在侧边栏宽度不足时可折叠为顶部 Tab。
- **组件**：统计卡片采用 `border + monospace 大数字` 样式，表格行采用条纹背景，进度条带百分比标签，图谱面板保持独立全宽展示区。
- **字体排印**：正文采用 `JetBrains Mono` 或 `Fira Code` 等 monospace 风格增强数据感；中文标题保留 sans-serif。
- **动效**：去除大量过渡动画，保留 hover 高亮与 active 状态即可，整体更「克制」。

### R2. HTML 结构微调（index.html）

在不破坏任何 `app.js` 引用的 `id`、`class`、`data-*` 属性的前提下：

- 将 `<header class="navbar">` 结构重构为左侧垂直 sidebar（`<aside class="sidebar">`）+ 右侧主区（`<main class="main-content">`）。
- 统计卡片（`analytics-grid`）布局改为 2 列表格式卡片，每张卡片显示指标名 + 大数字 + 子说明行。
- 学情诊断视图（`view-report`）中的薄弱点列表改为数据表格样式（`<table>` 或等价 CSS grid 行）。
- 其余三个视图（quiz / tutor / graph）保持功能不变，仅调整容器样式与配色。

### R3. 兼容性与功能保全

- `app.js` 文件**不得修改**。
- `app.js` 依赖的所有 DOM 选择器（`id`、`class`、`data-view`、`data-subject`）在重构后必须完整保留，不得删除或重命名。
- ECharts（CDN 加载）与 SVG 图谱相关容器尺寸需合理适配新布局，图表不能出现渲染为 0×0 的情况。
- 亮/暗主题切换按钮保留，切换后两套主题均需完整呈现（不能白屏或样式丢失）。

---

## Acceptance Criteria

### 无 JS 错误
- [ ] 在浏览器 Console 中打开 `index.html`，无任何红色 Error（仅网络类 warning 可接受，例如 CSP 无法加载 CDN 字体）。

### 四大视图功能正常
- [ ] **刷题视图**：点击选项卡可切换学科，题目题干与选项正常渲染，点击选项后 diagnostic-drawer 展开/收起。
- [ ] **聊天视图**：输入框可输入文字，点击发送后消息气泡出现在 `chat-msgs-container`。
- [ ] **图谱视图**：SVG 画布非空，图谱节点可见（不全白/全黑）。
- [ ] **学情视图**：ECharts 雷达图正常渲染（非零尺寸），薄弱点列表有内容。

### DeepSeek Eval Harness 视觉对标
- [ ] 页面默认以深色主题加载（`body` 背景 luminance < 0.1）。
- [ ] 侧边栏（或顶部 Tab）导航可见，品牌名与四个功能项清晰展示。
- [ ] 统计卡片数字区域使用等宽字体（monospace 系列）。
- [ ] 整体界面去除圆角过大、渐变色过重等「学生端轻奢」特征，对齐「工程/评测控制台」审美。

### 主题切换
- [ ] 点击亮/暗切换按钮，背景、文字、卡片颜色均正确翻转，无裸露白块或黑块。
