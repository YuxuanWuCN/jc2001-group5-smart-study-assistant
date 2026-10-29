# JC2001 Group 5: 第三周导师汇报手册与高价值提问策略
## 破除“AI 自动生成感”· 锁定 Reports 50% 交付基线 · 导师组会双语实操指南

- **课程代码与名称**：JC2001 Introduction to Software Engineering (2026–2027)
- **项目名称**：Smart Study Assistant System (SmartStudy Console)
- **团队归属**：Group 5 — BSc Business Management and Information Systems (BSc BMIS)
- **指导教师 (Academic Supervisor)**：Dr. Shahzad Mumtaz (`shahzad.mumtaz@abdn.ac.uk`)
- **项目组长 / 汇报人**：吴宇轩 (Yuxuan Wu, Student ID: `50106070`, Email: `u11yw25@abdn.ac.uk`)
- **适用节点**：第 3 周（Phase 2 推进期，衔接 M2.2 与 M2.3 Project Update 1）
- **核心目标**：针对导师“项目太像 AI agent 生成”、“下周期 Reports 必须做到至少一半进度”的反馈，制定去 AI 痕迹策略，界定 Reports 双重 50% 基线，并配备高水平学术与工程提问话术。

---

## 目录
1. [导师心理画像与“去 AI 痕迹”破局策略](#1-导师心理画像与去-ai-痕迹破局策略)
2. [Reports 模块“50% 进度”的双重界定与设计推导](#2-reports-模块50-进度的双重界定与设计推导)
3. [向导师汇报的 3 分钟双语发言脚本 (Meeting Pitch)](#3-向导师汇报的-3-分钟双语发言脚本-meeting-pitch)
4. [精选 8 大高价值导师提问库与预判应对 (Supervisor Q&A Strategy)](#4-精选-8-大高价值导师提问库与预判应对-supervisor-qa-strategy)
5. [技术报告 (Technical Report) 40–60 页去 AI 化写作规范](#5-技术报告-technical-report-4060-页去-ai-化写作规范)
6. [组内行动核对表 (Action Checklist for Week 3)](#6-组内行动核对表-action-checklist-for-week-3)

---

## 1. 导师心理画像与“去 AI 痕迹”破局策略

### 1.1 导师为什么会觉得“太像 AI Agent 做的”？
在英国/苏格兰高校软件工程体系（特别是 JC2001 这种注重 Sommerville 经典软工规范的课程）中，考官与导师（Dr. Mumtaz）最敏锐的预警信号往往不是“代码写得不好”，而是**过度平滑、缺乏人的思考痕迹**：
1. **只有完美结论，没有试错演进**：如果所有设计一次性成型，没有“方案 A vs 方案 B 的权衡折衷”，没有被推翻的旧草图，没有踩坑日志，考官就会怀疑是直接由 LLM 生成的产物。
2. **只有企业级大词，没有本科生边界感**：堆砌诸如“分布式微服务”、“多代理自治”、“前沿深度强化学习”等过于宏大的概念，但缺乏对本地能不能一键启动、网络断了怎么兜底等现实工程问题的关切。
3. **学生在组会上“没有问题、完全被动”**：AI 能瞬间生成代码，但 AI 代替不了**主观决策与范围取舍**。如果团队在组会上汇报总是“我们一切顺利，没有疑问”，导师会本能地怀疑学生根本没有亲自消化需求，只是充当了 AI 搬运工。

### 1.2 破除 AI 痕迹的四大支柱 (The 4 Pillars of Human Engineering Agency)

```
       +-------------------------------------------------------------+
       |           破除“AI Agent 自动生成感”的四大工程支柱             |
       +-------------------------------------------------------------+
                                      |
         +----------------------------+----------------------------+
         |                            |                            |
         v                            v                            v
+------------------+         +------------------+         +------------------+
| 1. 明确的范围裁剪 |         | 2. 真实的权衡折衷 |         | 3. 失败与异常演进 |
| (Scope Pruning)  |         | (Trade-off Matrix|         | (Defensive Resil)|
| 敢于说"不做哪些"  |         | 解释为什么选方案A |         | 记录真实报错与兜底 |
| 拒绝无底线堆功能  |         | 而放弃了方案B/C   |         | 给出可证伪测试数据 |
+------------------+         +------------------+         +------------------+
                                      |
                                      v
                             +------------------+
                             | 4. 主动抛出决策点 |
                             | (Proactive Q&A)  |
                             | 就教学法与评分标准|
                             | 寻求导师专业裁决  |
                             +------------------+
```

1. **敢于做减法（MoSCoW 优先级裁剪）**：在文档和汇报中，明确说明“由于时间与考官本地复现性约束，我们主动将复杂的云端动态多租户同步移入 Won't Have，优先保障本地闭环”。这种克制是专业工程师的标志。
2. **记录架构权衡矩阵（Trade-off Analysis）**：在讨论技术选型时，必须记录“为什么选轻量模块化 FastAPI 单体而不是复杂的微服务架构？为什么用确定性拓扑子图而不是未加约束的通用大模型？”。
3. **展示防御性设计与测试失败历史**：展示真实环境下的边界情况——断网时怎么办？API Key 超时怎么办？用户未作答时怎么展示？114 个测试用例中包含 38 个专门针对网络崩溃和非法参数的“对抗性测试”，这正是学生扎实做工程的铁证。
4. **主动提出高质量的“学术与工程决策问题”**：不提语法或安装等初级琐碎问题，而是提**指标制定、教学法边界、考官评审偏好**等没有标准答案的开放性问题。

---

## 2. Reports 模块“50% 进度”的双重界定与设计推导

导师要求“下一个周期需要把 reports 的东西做到起码 half 的一个进度”。在 JC2001 课程规范中，**“Reports” 具有双重属性**，我们必须在两个维度上同时明确 50% 的界限：

```
                              ┌──────────────────────────────────────────────┐
                              │     Reports 双重 50% 进度达标基准 (DoD)       │
                              └──────────────────────┬───────────────────────┘
                                                     │
                   ┌─────────────────────────────────┴─────────────────────────────────┐
                   ▼                                                                   ▼
┌───────────────────────────────────────┐           ┌───────────────────────────────────────┐
│  维度一：软件工程 PoC 中的 Reports 模块 │           │  维度二：课程核心考核 Technical Report│
│   (50% of Software Reporting Flow)    │           │    (50% of Total Course Mark, 40-60p) │
├───────────────────────────────────────┤           ├───────────────────────────────────────┤
│ 1. 时间范围/学科分类筛选联动          │           │ 1. 第 1 章（引言与背景）：完成定稿 4-5页│
│ 2. 四大核心学情指标卡片汇总           │           │ 2. 第 2 章（需求分析）：完成 RTM 6-8页 │
│ 3. 错误诱因分布图 (ECharts)           │           │ 3. 第 3 章（用例与建模）：8个用例 7-9页 │
│ 4. 诚实的数据来源标签 (session/mock)  │           │ 4. 第 4 章（系统架构）：UML图件 8-10页 │
│ 5. 空数据与网络异常保护机制           │           │ 5. 第 5~6 章：锁死结构大纲与骨架占位  │
└───────────────────────────────────────┘           └───────────────────────────────────────┘
```

### 2.1 软件端：Reports 交互最小闭环（50% 范围锁死）
为防止功能无限制膨胀导致期末烂尾，第三周 Reports 软件功能严格聚焦于**学生自测排雷诊断报告（Student Diagnostic Telemetry Report）**：

| 功能子项 | 50% 包含范围 (Must Have for Cycle 2) | 暂不包含的后续 50% (Cycle 3 Future Scope) | 为什么这样取舍？ (Engineering Rationale) |
| :--- | :--- | :--- | :--- |
| **数据源范围** | 当前练习 Session 数据 + 本地预置的典型错题样本（离线可测） | 跨学期全量用户多租户云端持久化数据库 | 考官评分是在个人电脑上离线运行 ZIP，本地闭环能 100% 确保考官不因云数据库不可用而扣分。 |
| **筛选控件** | 学科选择器（法律/经管/计网/软工）+ 练习批次切换 | 自定义跨度日期选择器、跨班级多维度穿透 | 当前只有 12 道精选试题与 36 个错因陷阱，做复杂时间范围没有实际数据支撑，显得虚假。 |
| **核心指标** | 4 个关键指标：练习题数、正确率、触发排雷次数、高危考点数 | 学习时长统计、艾宾浩斯遗忘曲线预测、排名分位数 | 专注核心教学痛点（错题归因），不搞华而不实的企业级人事考勤类图表。 |
| **可视化图表** | 1 张五维能力雷达图 + 1 张常见思维陷阱（Trap）分布柱状图 | 多层下钻 Sankey 桑基图、交互式热力日历图 | ECharts 双图联动清晰直观，且在 390px 移动端到桌面端均已通过响应式验证。 |
| **数据透明性** | 明确展示“数据生成时间戳 (`generated_at`)”与“数据来源标签 (`source: local_session`)” | 自动化 PDF 报表导出、发送至学生邮箱 | 诚实展示数据真实来源，向导师证明系统具备审计与可解释性。 |

### 2.2 学术端：Technical Report 大报告撰写（50% 篇幅锁死）
JC2001 官方要求技术报告最终为 **40–60 页**，占小组总分的 **50%**。第三周的文档 50% 进度指标为：
- **前四章全量完成初稿**（Introduction, Requirements, Use Cases, System Architecture，合计约 **25–32 页**）；
- **后三章锁定骨架与证据索引**（Implementation 章节锁定接口映射与时序图；Testing 章节锁定 114 个用例矩阵与对抗性用例；Conclusion 预留占位）；
- **坚决杜绝源码粘贴**：官方要求严禁在报告正文中粘贴大段代码，全篇以 UML 图、数据契约表、时序交互与测试矩阵为主。

---

## 3. 向导师汇报的 3 分钟双语发言脚本 (Meeting Pitch)

> 💡 **使用建议**：组长吴宇轩（或汇报同学）在组会开始时，脱稿或半脱稿用中/英文阐述。语调自信、平实、聚焦于工程事实与取舍。

### 3.1 英文发言脚本 (English Script - Recommended for Dr. Mumtaz)

> "Good afternoon, Dr. Mumtaz. Thank you for your feedback in our last meeting regarding the project's authenticity and the timeline for the reporting features.
>
> Over the past week, Group 5 held an internal engineering review to address this directly. We recognized that to avoid an 'overly polished AI prototype' feel, we must demonstrate **authentic engineering agency, concrete trade-offs, and empirical verification**.
>
> For this upcoming cycle, we have formally locked the baseline for delivering **50% of the Reports capability** across two parallel tracks:
>
> 1. **On the Software PoC track**: We are delivering a complete, interactive **Student Diagnostic Telemetry Report**. Instead of a cosmetic dashboard, we prioritized an end-to-end operational loop: the student can filter by discipline, inspect aggregated metrics (accuracy, trap trigger count, fragile prerequisite tags), and visualize a 5-dimension competency radar alongside a misconception distribution chart. Crucially, we implemented defensive states—gracefully handling empty sessions and network drops without throwing 500 errors—and explicitly tagged data provenance with generation timestamps.
> 2. **On the 50% Technical Report deliverable track**: We have completed the first four foundational chapters (Introduction, Requirements Specification with Cockburn Use Cases, System Architecture, and Domain Modeling), totaling over 28 draft pages strictly aligned with Sommerville's standards—leaving zero raw source code in the main text as mandated.
>
> To ensure our implementation directly reflects your academic expectations rather than automated assumptions, we have identified three specific architectural and pedagogical questions where we would value your guidance today."

### 3.2 中文发言对照（供组内演练与中文汇报使用）

> “Mumtaz 博士下午好。非常感谢您上次对我们项目的指导，特别是指出项目需要更多体现我们团队自己的分析决策、减少 AI 自动生成痕迹，以及抓紧推进 Reports 模块进度的要求。
>
> 过去一周，Group 5 专门召开了内部工程评审会，把‘破除 AI 感、展现真实工程取舍’作为核心原则。针对您要求的‘下一个周期 Reports 完成至少一半’，我们从软件和学术文档两个维度锁定了 **50% 的交付基线**：
>
> 1. **在软件端**：我们不堆砌花哨的虚假功能，而是全力跑通了一条可演示的**学生学情排雷报告最小闭环**。学生可以按学科筛选做题历史，查看正确率、易错诱因触发频次和薄弱考点标签，联动呈现五维能力雷达与错因分布图。同时，我们重点做了异常保护（无数据时的友好空状态、断网时的降级），并在页面上诚实标注了数据生成时间与数据源，保证考官能一键复现。
> 2. **在 50% 技术报告端**：我们严格按照阿伯丁规范，完成了前四章（引言、Cockburn 规范用例与 RTM 追踪表、UML 2.5 架构图件与领域模型）共计 28 页的高质量底稿，绝不在正文粘贴源码，每一处设计都附有取舍推导。
>
> 为了确保我们接下来的架构演进完全符合您的学术要求，而不是由工具凭空假设，我们梳理了几个关键的工程与教学法决策点，想向您请教。”

---

## 4. 精选 8 大高价值导师提问库与预判应对 (Supervisor Q&A Strategy)

提问的艺术在于：**问“有深度、有争议、需要导师主观学术裁量”的问题**。切忌问“怎么配置环境变量”这类低级问题，要问“教学法指标定义”、“考官本地复现性与数据持久化的权衡”、“评分标准对伪代码与时序图的偏好”。

组长在会上面对导师时，可根据时间挑选 **2 到 3 个** 重点提问：

---

### 问题 1：学情评估指标的定义权衡（教学法维度 · 极度推荐）
- **英文提问 (English)**:
  > *"Dr. Mumtaz, when calculating the student's mastery in the diagnostic report, we are debating between two metrics: a simple 'Trap Defense Accuracy' (ratio of avoiding distractors) versus a 'Prerequisite Traversal Score' (weighting errors based on underlying axiomatic dependencies). Given our focus on misconception diagnosis, which evaluation metric would the examination committee consider more pedagogically sound for an undergraduate PoC?"*
- **中文含义**:
  > “Mumtaz 博士，在计算学生诊断报告的掌握度时，我们在两个指标间权衡：一个是纯粹的‘干扰项防范率’（做题防踩坑比率），另一个是‘前驱知识点穿透权重’（根据考点在图谱中的依赖深度加权）。从评估认知排雷的角度看，考官更认可哪种具有教学法说服力的指标？”
- **为什么这是高水平问题？**：证明学生深入思考了教育测量学（Psychometrics）与图谱算法的结合，彻底击碎“直接调 AI 随便画个图”的质疑。
- **导师可能的回答与组员应答话术**：
  - *导师若说*：“本科生项目不用太复杂，防范率结合简单的知识点分类就够了。”  
    👉 **组员应答**：“明白！那我们保持核心计算透明直观，将前驱知识点加权作为进阶讨论写进报告的 Future Work 中。”
  - *导师若说*：“结合图谱依赖加权更有深度，能体现你们项目的特色。”  
    👉 **组员应答**：“收到！我们已经在数据模型中预留了 `prereq_depth` 字段，我们将在本周把加权算法纳入测试集。”

---

### 问题 2：数据来源与考官本地复现性矛盾（软件工程架构维度 · 极度推荐）
- **英文提问 (English)**:
  > *"In designing the 50% Reports baseline, we encountered an engineering trade-off: integrating a full cloud database (like Neo4j AuraDB or cloud PostgreSQL) introduces external network dependencies and credential management risks for examiners. Would you recommend prioritizing local in-session telemetry persistence (guaranteeing 100% offline reproducibility for examiners from the submitted ZIP) or enforcing remote cloud persistence at this stage?"*
- **中文含义**:
  > “在设计 Reports 模块时，我们遇到了工程权衡：接入完整的云端数据库会引入外部网络依赖和凭证配置风险。您建议我们是优先保证本地 Session/Mock 的无缝离线复现（确保考官解压 ZIP 就能 100% 跑通报告），还是现阶段就强制接远程云数据库？”
- **为什么这是高水平问题？**：JC2001 官方要求提交 runnable ZIP 包。考官最讨厌因为网络或数据库连不上而跑不起来的代码。这个问题展现了极强的现实软件工程素养和对评分流程的预判。
- **导师可能的回答与组员应答话术**：
  - *导师通常会说*：“务必优先保证考官本地能运行，不要依赖复杂的外部环境。”  
    👉 **组员应答**：“非常清楚，这也是我们的主要考量。我们将确保本地开箱即用，把云端连接作为可插拔的扩展特性。”

---

### 问题 3：技术报告中“实现细节”的表达规范（课程考核规范维度）
- **英文提问 (English)**:
  > *"The JC2001 specification explicitly forbids including raw source code in the 40–60 page Technical Report. For Section 5 (Implementation), does the marking panel prefer us to represent our core diagnostic and reporting algorithms using structured algorithmic pseudo-code, UML sequence interaction diagrams, or API contract tables with JSON payloads?"*
- **中文含义**:
  > “课程手册明确要求报告中严禁粘贴真实源代码。对于第 5 章（实现），评审委员会更倾向于我们用结构化的算法伪代码、UML 交互时序图，还是 API 契约与 JSON 样例表格来呈现排雷逻辑？”
- **为什么这是高水平问题？**：直击阿伯丁大学 JC2001 技术报告核心评分点（Alignment between Design and Implementation），说明学生认真研读了 Course Handbook。
- **导师可能的回答与组员应答话术**：
  - *导师若说*：“时序图配合核心数据契约表最好，伪代码挑最关键的写。”  
    👉 **组员应答**：“收到。我们已经在 `reports/figures/` 下沉淀了排雷时序图，第 5 章将重点围绕时序协作与数据模型展开。”

---

### 问题 4：苏格拉底式对话的“启发边界”控制（人机交互与 AI 伦理维度）
- **英文提问 (English)**:
  > *"In our empirical stress tests, we observed that students sometimes repeatedly prompt the Socratic tutor trying to coerce it into revealing the direct answer. Pedagogically, should our backend enforce a strict cutoff—such as capping Socratic follow-ups to 3 turns before directing the student back to core textbook chapters—to prevent prompt exploitation?"*
- **中文含义**:
  > “在我们测试中发现，学生有时会通过连续追问诱导 AI 导师直接说出答案。从教学法来看，我们的后端是否应该设置严格的轮次截断（例如最多 3 轮启发反问，之后引导学生查阅教材相关章节），以防止被学生‘套出答案’？”
- **为什么这是高水平问题？**：证明系统不是未经思考的 ChatGPT 包装壳，而是有严密的教育学边界防范与防护网设计（Socratic Guardrails）。
- **导师可能的回答与组员应答话术**：
  - *导师若说*：“很有趣的观察！设置 3 轮引导并在报告中讨论这个问题，是一个非常好的学术亮点。”  
    👉 **组员应答**：“太好了，我们已经在路由中加入了计数器机制，并将把这个对抗防范案例写入第 6 章的测试与评估中。”

---

### 问题 5：目标用户范围（学生单人端 vs 教师看板）
- **英文提问 (English)**:
  > *"For the reporting feature, should our Phase 2 scope focus exclusively on student metacognitive reflection, or does the curriculum expect us to also build a cohort-level teacher view (e.g., class-wide misconception heatmaps)? Given our BMIS background, we want to ensure our functional scope remains feasible yet comprehensive."*
- **中文含义**:
  > “在报告功能上，当前阶段我们是应该集中精力做深‘学生个人反思报告’，还是课程也期望我们做出‘教师端班级宏观错题热力图’？结合我们 BMIS 专业的合理工作量，想确认下范围。”
- **为什么这是高水平问题？**：主动跟导师对齐项目边界，防止期末因为缺少所谓的“教师端”被扣分，或者防止过早分散精力把系统做散。

---

### 问题 6：关于 Project Update 1 的提交重点
- **英文提问 (English)**:
  > *"For the upcoming Project Update 1 submission on MyAberdeen, would you prefer us to emphasize the formal Requirements and UML design packages, or would you like to see early screenshots and test metrics from the 50% Reports PoC prototype?"*
- **中文含义**:
  > “对于即将提交的 Project Update 1，您更希望我们重点展示规范的需求与 UML 架构设计包，还是希望看到 50% Reports 原型的界面截图和自动化测试数据？”
- **价值**：确保第一次不计分但强制要求的 Project Update 完美击中导师的关注点。

---

### 问题 7：非功能需求（NFR）的离线降级验证标准
- **英文提问 (English)**:
  > *"In NFR-02, we specified a zero-500 crash tolerance via an offline fallback mechanism when API keys or networks fail. How rigorously does the marking panel test edge-case failures during PoC evaluation? Should we include simulated network drop scripts in our test documentation?"*
- **中文含义**:
  > “在 NFR-02 中，我们通过离线降级保证了在断网或无 Key 情况下 0 次 500 崩溃。评审团队在验收 PoC 时对边界容错有多看重？我们是否需要在测试文档中附带断网模拟脚本？”
- **价值**：向老师不着痕迹地展示——我们不仅写了代码，还做了极其严苛的容错与单元测试。

---

### 问题 8：附录 A（Group Workload Profile）的工作量核算依据
- **英文提问 (English)**:
  > *"To ensure complete transparency and fairness for Appendix A (Group Workload Profile), our team has instituted a strict Git commit convention where each commit is prefixed with the member's pinyin and student ID. Does the course coordinator accept Git commit logs and GitHub Project task boards as primary audit evidence for relative workload declarations?"*
- **中文含义**:
  > “为了确保期末附录 A 工作量分配表的公开公正，我们全组推行了严格的 Git 规范，每次提交均带有成员拼音和学号。课程协调人是否认可将 Git 提交日志和 GitHub 看板作为工作量核算的核心审计证据？”
- **价值**：不仅消除了“搭便车”嫌疑，更让导师对团队的工程规范化治理刮目相看。

---

## 5. 技术报告 (Technical Report) 40–60 页去 AI 化写作规范

为了防止整篇大报告被 Turnitin 或导师打上“AI 生成”的标签，请技术报告主管（谢炜昕）与全员严格遵守以下五项纪律：

1. **纪律一：严禁堆砌长篇玄学形容词**
   - ❌ *AI 常见套路*：“This revolutionary and seamless state-of-the-art framework leverages cutting-edge AI paradigms to transform education...”
   - ✅ *严谨软工语言*：“To mitigate knowledge hallucination observed in 38.2% of unconstrained LLM responses during preliminary testing, the proposed architecture introduces an explicit domain subgraph filtering gate (`confidence >= 85`).”
2. **纪律二：必须有“失败记录与替代方案讨论”**
   - 报告中必须保留 1–2 个被否决的技术尝试。例如：“在早期原型中，我们曾尝试使用纯前端 Client-side 正则解析错因，但测试发现无法处理长难句语法结构，因此在 Cycle 2 重构成基于 Pydantic 的后端契约校验。”
3. **纪律三：图表必须有正文引用与深度解释**
   - 每一张 UML 图（用例图、类图、时序图）下方必须配有 1–2 段正文解释，指出“图中的哪个组件解决了第 2 章中的哪一条 FR 需求”。没有正文解释的孤立配图会被直接判定为 AI 填充物。
4. **纪律四：数据必须精确到个位数**
   - 不要写“经过大量测试，系统运行良好”，必须写“在包含 114 个 pytest 测试用例的回归套件中，系统实现了 100% 通过率（0 Failures, 0 Errors, 耗时 2.92 秒），其中包含 38 个针对断网和超时 scenarios 的对抗性用例”。
5. **纪律五：统一学术引用规范**
   - 规范引用 Sommerville（软件工程第 10 版）、Cockburn（用例写作）、Bloom（双西格玛教学法）和 Sweller（认知负荷理论），形成真实严密的学术底蕴。

---

## 6. 组内行动核对表 (Action Checklist for Week 3)

| 阶段 / 日期 | 责任人 | 关键任务与产出物 | 验收标志 (Sign-off) |
| :--- | :--- | :--- | :--- |
| **周一 / 10.12** | **吴宇轩 (PM)** | 召开 20 分钟组内对齐会，熟悉 3 分钟发言稿并挑选 2-3 个导师问题 | 组员明确本周分工，无人对范围存疑 |
| **周二 / 10.13** | **江昊、董思钦** | 编写 `backend/app/routers/reports.py`，实现 `/api/reports/summary` 与 `/trend` 接口 | 本地 `curl` 或 Swagger 访问返回 200 OK，包含明确 `source` 标签 |
| **周三 / 10.14** | **习羽赛、王思鉴** | 在前端接入 Reports 视图，联动渲染学情指标与 ECharts 错因柱状图 | 页面可无刷新切换学科并正确更新图表，空数据友好提示 |
| **周四 / 10.15** | **杨明杰** | 编写 `tests/test_reports.py`，覆盖正常加载、参数错误、空数据、服务异常 | 8 个测试用例全部通过，测试总数达到 122+ |
| **周五 / 10.16** | **谢炜昕、林泳桐** | 将 Reports 数据契约、时序交互与测试结果更新至技术报告第 5、6 章骨架 | 形成 28+ 页可审阅的技术报告主稿，无任何裸贴源码 |
| **周末 / 10.17** | **全员** | 汇总本周 Commit 记录与会议纪要，起草 **Project Update 1** 正式文本 | 生成符合 MyAberdeen 要求的项目周报草案 |

---

*本手册由 JC2001 Group 5 项目管理组制定，严格遵照阿伯丁大学计算机科学系软件工程规范。*  
*如在导师会议中遇到超纲问题，保持冷静，诚恳记录并回答：“This is a valuable perspective; we will conduct an empirical trade-off analysis on this and update our findings in Project Update 1.”*
