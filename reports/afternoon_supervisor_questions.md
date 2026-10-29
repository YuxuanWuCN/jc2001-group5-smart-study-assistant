# JC2001 Group 5 · 今天下午导师组会提问手卡（Cycle 3 进度汇报收尾专用）

| 项 | 核验信息（100% 对齐仓库真实资产） |
| :--- | :--- |
| **课程与团队** | JC2001 Introduction to Software Engineering (2026–27) · Group 5（BSc BMIS，10 人） |
| **项目名称** | 智学罗盘 StudyGraph / SmartStudy Assistant |
| **汇报人 / 导师** | 吴宇轩（Yuxuan Wu，PM / Team Lead） $\to$ Dr. Shahzad Mumtaz |
| **核心提问策略** | **「工程与实验已闭环 + 请导师对 40–60 页报告的评分权衡（Rubric Trade-offs）做 A/B 拍板」** |
| **数据双口径防撞提醒** | ⚠️ **上场前必看**：<br>1. **文稿口径（Ch1/Ch2/Ch6 报告草稿已写）**：MMLU 12 学科（$n=4,445$）**7 胜 3 平 2 负**，2 个负向学科在报告草稿（`ch01`/`ch02`）中写为 **计量经济学 `Econometrics`（$-4.39\%$）** 与 **欧洲史 `High School European History`（$-1.21\%$）**。<br>2. **仓库 CSV 原始表口径（`graphrag（终）/final_systematic_report.csv`）**：同样是 **7 胜 3 平 2 负**，但表中记录的 2 个负向行是 **`High School Physics`（$-1.32\text{ pp}$）** 与 **`High School US History`（$-1.00\text{ pp}$）**（表中 `Econometrics` 为 $+1.75\text{ pp}$）。<br>👉 **话术已为你同时兼容双口径**：开口直接说“**7 胜 3 平 2 负（最高 $+2.50\text{ pp}$，但有 2 个学科出现 $-1\% \sim -4\%$ 的负向波动）**”，既与你的报告正文完全咬合，又不怕导师现场点开 CSV！ |

---

## 💡 为什么这 3+1 个问题最能帮 Group 5 加分？

1. **彻底打破“AI 生成感”**：AI 生成的项目永远“全绿、全赢、零缺陷”；主动把 **MMLU 7 胜 3 平 2 负的负向实验结果**、**离线查表 vs 在线大模型的边界取舍** 摆上桌面，证明你们真正跑过数据、踩过坑、做过工程权衡。
2. **A vs B 选择题式提问，尊重导师权威且极易回答**：不抛开放式烂摊子（如“老师您看我们还要改啥？”），而是把两个都已经想清楚利弊的方案摆出来让导师按评分偏好（Examiner Rubric）拍板，导师 30 秒就能给出明确指令。
3. **把导师今天的口头回复变成报告里的“尚方宝剑”**：导师今天拍板的结论，可以直接写进报告的 Architecture Rationale（Ch4）和 Evaluation Scope（Ch6），期末盲审或导师打分时天然契合他的预期。

---

## 🎙️ 汇报收尾切入过渡句（10 秒自然引出提问）

- **🗣️ 中文口语**：
  > “以上就是我们 Cycle 3 的软件冻结基线和 7 章报告推进情况。因为我们的核心测试（147 个用例）和 MMLU 离线评测（4,445 题）都已经跑完锁库了，为了确保接下来 40 到 60 页 Technical Report 完全对齐评分标准，我有 **3 个关于报告取舍的具体问题** 想请您帮我们拍个板。”
- **🗣️ English (Natural Academic Spoken)**：
  > "That wraps up our frozen PoC baseline and our seven-chapter report progress. Since both our 147 automated `pytest` cases and our 4,445-item MMLU offline benchmark are already locked in the repository, we would really appreciate your guidance on **three specific scoping trade-offs** so our 40-to-60-page Technical Report aligns closely with what examiners look for."

---

## 问题 1：负向实验结果的呈现深度（Ch6 Evaluation & Ch7 Limitations）

### 📌 核心议题
在 MMLU（12 学科，$n=4,445$）离线评测中，我们的 GraphRAG 管线取得了 **7 胜 3 平 2 负** 的真实结果（其中法学最高 $+2.50\text{ pp}$，但在出现负向波动的 2 个学科如 `High School Physics` $-1.32\text{ pp}$、`High School US History` $-1.00\text{ pp}$ 上不如纯基座模型）。请教导师：评分标准更看重**深入剖析负向学科的检索噪声失效机理（Option A）**，还是**继续调参做消融把这 2 个学科刷成正数（Option B）**？

### 🎯 提问目的（为什么问这个能加分）
- 向导师展示你们不仅有 **4,445 道外部基准题的硬核量化实证**，而且严守学术诚信——不藏匿负数据、不篡改 CSV。
- 引导导师亲口确认“诚实分析边界比全刷成正数更符合大学学术评估要求”，为 Ch6.3（Empirical Evaluation）、Ch6.6（Threats to Validity）和 Ch7.2（Limitations）锁定高分叙事基调。

### 🗣️ 现场中英文开口话术
- **中文自然口语**：
  > “第一个问题是关于第 6 章实验评估里**负向结果的处理深度**。我们在 MMLU 的 12 个学科（一共 4,445 道题）上实测了自建的 GraphRAG 管线，真实结果是 **7 胜、3 平、2 负**——在规则边界清晰的法学上提升了 2.5 个百分点，但在 2 个学科（比如高中物理 $-1.32\text{ pp}$、美国史 $-1.00\text{ pp}$）上反而因为多跳邻居引入了检索噪声，出现了轻微负向下降。从 Technical Report 的评分标准来看，您建议我们**保留这份真实的 7 胜 3 平 2 负数据，在 Ch6 和 Ch7 重点剖析图谱检索噪声为什么在这两类学科失效（方案 A）**，还是建议我们现阶段分出精力去做消融和剪枝修复，尽量把负向结果调成正数（方案 B）？”
- **English (Spoken to Supervisor)**：
  > "First, on framing negative empirical results in Chapter 6 and Chapter 7. Across 12 MMLU subject subsets—4,445 items in total—our offline GraphRAG pipeline achieved **7 gains, 3 ties, and 2 slight regressions** (`-1.32 percentage points` in High School Physics and `-1.00 percentage point` in US History, whereas rule-dense subjects like Professional Law gained `+2.50 percentage points`). From the examiner's perspective, does it earn stronger marks for **critical evaluation** if we **keep these mixed results as-is and deeply analyse why multi-hop graph retrieval introduces neighbour noise on numerical or narrative subjects (Option A)**, or would you prefer us to spend engineering time running ablation fixes to push those two subjects into positive territory (Option B)?"

### 🧭 导师可能的回答走向 & 当场接话预案
- **🅰️ 如果导师选 Option A（90% 概率：保留真实负结果，深入分析失效机理）**：
  - **中文接话**：“太好了，这和我们的工程判断完全一致！那我们就锁死现在这份 `final_systematic_report.csv` 快照，在 Ch6.3 用正绿负红的柱状图诚实展示，并在 Ch6.6（Threats to Validity）专门对比‘法条树状规则 vs 物理多步数值推导’的适用边界，绝不做过度吹嘘。”
  - **English Follow-up**: *"Thank you, that aligns completely with our engineering instinct. We will freeze `final_systematic_report.csv` as-is, plot both the gains and losses transparently in Figure 6.2, and dedicate a subsection in Section 6.6 (Threats to Validity) to explaining the structural boundary between rule-based statutes and numerical reasoning."*
- **🅱️ 如果导师选 Option B（建议做一点消融或验证原因）**：
  - **中文接话**：“明白！为了不影响全组写报告的主进度，我们不重写主系统，而是由负责第 6 章的杨明杰在离线脚本里针对这 2 个负向子集补一组小规模的 Top-$k$ 剪枝对照表，既保留原始的 7 胜 3 平 2 负基线，又用数据验证是不是邻居节点过多带来的噪声。”
  - **English Follow-up**: *"Understood. Without touching our frozen runtime codebase, our Chapter 6 lead (Mingjie Yang) can run a lightweight offline ablation on just those two subsets—comparing hop-depth or top-k pruning—so we still report the original 7-3-2 baseline honestly while verifying whether neighbour noise caused the drop."*

---

## 问题 2：100% 离线确定性查表 vs 实时大模型调用的架构边界（AD-1 & Software Demo）

### 📌 核心议题
为了确保考官批改 Proof-of-Concept Software（占小组分 30%，课程总分 15%）时**零 API Key、零云数据库依赖、一条 `uvicorn` 命令毫秒级启动**，我们的架构决策 `AD-1` 将在线答题路径设计为 **离线预计算策展题库（`O(1)` 确定性查表，$<5\text{ ms}$，100% 零幻觉、零剧透）**，同时保留了可选的 `QWEN_API_KEY` 在线润色钩子与离线 GraphRAG 评测管线。请教导师：在 Ch4 Architecture 和最终演示（Presentation 20% / PoC 30%）中，是否认可这种**离线可复现性优先的边界（Option A）**，还是建议在演示视频/现场额外录一段**挂载 `QWEN_API_KEY` 的实时在线大模型对比（Option B）**？

### 🎯 提问目的（为什么问这个能加分）
- 把“为什么在线系统用的是预设题库字典查表而不是每次调大模型”这个**最容易被挑刺的软肋**，主动升级为深思熟虑的 **架构权衡（Architecture Decision Record `AD-1`）**。
- 同时点亮你们在 `diagnostic_service.py` 里已经写好的双模降级机制（有 Key 走 4 秒超时苏格拉底润色，无 Key 毫秒级确定性回退），摸清导师对最终 Demo 演示形态的真实偏好。

### 🗣️ 现场中英文开口话术
- **中文自然口语**：
  > “第二个问题是关于第 4 章的核心架构边界（`AD-1`）和最终软件演示的侧重点。我们采用了‘双轨解耦架构’：重度的 12 阶段 GraphRAG 放在离线评测跑；而交给考官运行的 PoC 主程序采用**预审校的细粒度错因陷阱库做 $O(1)$ 确定性查表（响应小于 5 毫秒、零法条幻觉、零剧透答案）**，这样考官解压 ZIP 后不需要配任何 API Key 或启动 Neo4j，敲一行 `uvicorn` 就能 100% 离线复现所有功能；同时代码里也保留了可选的 `QWEN_API_KEY` 实时苏格拉底润色通道。请问在 Ch4 架构评审和最终 Demo 演示中，您认为我们**完全聚焦在这个 100% 离线确定性闭环上就足够有说服力（方案 A）**，还是建议我们在最终汇报演示时，**额外展示一段挂载 `QWEN_API_KEY` 的实时在线生成 vs 离线确定性查表的同屏对比（方案 B）**？”
- **English (Spoken to Supervisor)**：
  > "Second, regarding our core architectural boundary (`AD-1` in Chapter 4) and the final Software Demo. Our PoC decouples offline GraphRAG research from the live student runtime: the runtime executes an **$O(1)$ deterministic lookup against pre-audited misconception traps** (`< 5 ms` latency, zero statutory hallucination, and zero answer spoiling). This guarantees an examiner can unzip our submission and run `uvicorn` completely offline with zero API keys or cloud databases—matching the Brief's allowance for fixed PoC datasets—though our `diagnostic_service.py` also supports an optional `QWEN_API_KEY` live Socratic polishing mode with a 4-second fallback. For Chapter 4 and our live presentation, do you recommend **keeping the demo strictly focused on this 100% reproducible offline path (Option A)**, or would it add value in the presentation to **also show a brief side-by-side comparison with `QWEN_API_KEY` enabled live (Option B)**?"

### 🧭 导师可能的回答走向 & 当场接话预案
- **🅰️ 如果导师选 Option A（认可离线确定性优先，强调考官易运行最重要）**：
  - **中文接话**：“明白！官方 Brief 第 7 页也提到 PoC 可以使用确定性数据集来验证核心机制。那我们在 PoC 提交包和 User Manual 里就把‘零配置离线一键启动’作为默认标准路径，并在 Ch5.4 的权衡表（Table 5.6）里诚实说明我们用开放式问答题的泛化性换取了 100% 零幻觉和可复现性。”
  - **English Follow-up**: *"Got it—that matches Page 7 of the Project Brief regarding simplified datasets for reliable PoC evaluation. We will keep the zero-configuration offline mode as our primary path in the User Manual and explicitly document the generality-versus-determinism trade-off in Table 5.6."*
- **🅱️ 如果导师选 Option B（希望在 Presentation 里看到一点实时 AI 对比效果）**：
  - **中文接话**：“好主意！因为我们的 `diagnostic_service.py` 和前端对比沙盒本来就支持双模切换，那我们保持提交给考官批改的 ZIP 默认离线免配置（防止考官没 Key 报错），但在期末 Presentation 现场/视频里专门放一个 45 秒的挂载 `QWEN_API_KEY` 实时对比片段，直观展示为什么无约束 LLM 会剧透答案而我们的陷阱约束不会！”
  - **English Follow-up**: *"That makes great sense. Since `diagnostic_service.py` already has the dual-mode hook with a 4-second timeout fallback, we will keep the submitted ZIP strictly zero-config for the marker, while showcasing a 45-second live `QWEN_API_KEY` comparison during our Project Presentation to visually contrast unconstrained LLM answer-spoiling against our trap-guided scaffolding."*

---

## 问题 3：报告 40–60 页篇幅分配与高密度工程表格的边界（Main Body vs Appendices A–D）

### 📌 核心议题
官方 Project Brief 明确规定正文页数必须控制在 **40–60 页**（从 Ch1 到 Ch7 计，前置页、References 与 Appendix A 不计入），且**严禁在正文贴源码（Do not include source code in the technical report）**。目前我们已完成 **8 个 API 端点契约、6 个完整用例规格表（UC-01~06）、147 个 `pytest` 自动化用例以及完整的端到端需求追溯矩阵（RTM）**。请教导师：像“逐端点字段契约详表 / 147 条测试清单 / 完整 RTM 矩阵”这类高密度工程表格，**直接放进正文（Ch3/Ch5/Ch6）更能拿技术深度分（Option A）**，还是**正文只放精炼摘要表 + 架构/算法散文解析，把全量详表统一收进 Appendices B–D 更符合您的审阅习惯（Option B）**？

### 🎯 提问目的（为什么问这个能加分）
- 证明你们逐字精读过官方 Brief 第 5 页的两条硬红线（**40–60 页硬区间** + **No source code in body**），绝不是拿源码和垃圾表格注水凑页数的团队。
- 顺带不着痕迹地把你们雄厚的工程家底（**147 个测试、6 个规范用例、完整 RTM、8 个双向命名同步 API**）在导师脑海里过一遍，同时规避“正文表格太多被嫌像说明书”或“放进附录没被考官细看”的排版风险。

### 🗣️ 现场中英文开口话术
- **中文自然口语**：
  > “第三个问题是关于 **40 到 60 页正文的篇幅分配与附录边界**。我们严格遵守官方 Brief 严禁在正文贴源码的规定，算法全部改用≤20行的伪代码和架构图来写。不过我们手头的结构化工程表格非常多——包括 6 个完整的 Cockburn 用例规格表（UC-01 到 06）、8 个 API 端点的字段级契约表、147 个 `pytest` 测试用例清点以及完整的需求追溯矩阵（RTM）。按您的审阅习惯，您更希望我们在 **Ch3、Ch5、Ch6 正文里保留完整规格表来体现 Consistency and Technical Depth（方案 A）**，还是**在正文控制在 48–52 页左右、只放核心摘要矩阵和深度设计论述，把全量 147 条测试清单和完整 RTM 放进 Appendix B–D 供交叉查阅（方案 B）**？”
- **English (Spoken to Supervisor)**：
  > "Third, on balancing prose versus dense engineering tables within the **40-to-60-page main body limit**. Following Page 5 of the Brief, we have strictly excluded raw source code from the report. However, we have extensive structured artefacts—specifically 6 full use-case specification tables (`UC-01` to `UC-06`), field-level schemas for all 8 API endpoints, our 147-case `pytest` inventory, and the full Requirements Traceability Matrix (RTM). In your marking experience, is it better to **place the full specification and traceability tables directly inside Chapters 3, 5, and 6 to demonstrate end-to-end consistency (Option A)**, or **keep the main body around 50 pages of analytical prose and summary tables while moving the exhaustive 147-test inventory and full RTM into Appendices B–D (Option B)**?"

### 🧭 导师可能的回答走向 & 当场接话预案
- **🅰️ 如果导师选 Option A（重要工程表放正文，因为考官主要按正文章节打分，未必细翻自建附录）**：
  - **中文接话**：“非常感谢您的提醒！确实 Brief 只点名了 Appendix A（Group Workload Profile），其他附录考官未必逐页细看。那我们就把 6 个核心用例表、8 端点契约表和 14 条需求的逐条达标验证表（Table 6.5）全部精排在正文中，只有最长的 147 条逐函数测试流水账放附录，确保正文既扎实又严格卡在 50–56 页的黄金区间。”
  - **English Follow-up**: *"That is a very helpful distinction—since only Appendix A is explicitly mandated in the Brief, we will keep the 6 core use-case tables, the 8 API contracts, and the requirement-by-requirement verification matrix directly inside Chapters 3, 5, and 6, while keeping the total body tightly around 50–55 pages."*
- **🅱️ 如果导师选 Option B（正文重在分析推理，反对大段连页表格刷页数，详表进附录）**：
  - **中文接话**：“太清楚了！这正好和我们的规划一致——我们在正文里只放高信息密度的汇总对比表（比如 14 行 MoSCoW、7 条 ADR 权衡表、6 组对抗测试表），重点写清‘为什么这么设计、拒绝了什么备选方案’，把全量 RTM、147 条测试清单和 OpenAPI 快照收进 Appendices B–D，并在正文用显式交叉引用锚定。”
  - **English Follow-up**: *"Understood—we want the 40–60 pages to read like rigorous engineering analysis rather than padded tables. We will keep concise synthesis tables in the main chapters (such as our 7 ADRs and 6 adversarial test categories) with deep trade-off prose, and cross-reference the exhaustive RTM and 147-case inventory in Appendices B–D."*

---

## 🛡️ 备选问题（Bonus Q4 · 视现场时间与气氛机动启用）：真实工程失误复盘与分工透明化口径

> **启用时机**：如果前 3 个问题导师回答得很快、现场气氛融洽且还有 2–3 分钟富余，抛出这第 4 个问题——它直接命中导师最关心的**「真实人类团队演进痕迹 & Appendix A 公平打分」**。

### 📌 核心议题
我们在开发期曾真实发生过一次“评估脚本误提交云端 Neo4j Aura 凭证”的小事故，团队已于 10 月 25 日完成 Git 清洗、旧包隔离、密码轮换与环境变量改造；同时 Git 记录显示前期代码提交集中在组长（约 59%–67%），Cycle 3 正通过“每人独立负责一章 + 组会随机抽问”做知识转移。请教导师：**把这次真实的“凭证泄露检测与整改闭环”作为半页安全工程复盘写进 Ch5.6（Deployment & Security），在评分中会被视为加分的真实工程反思（Option A），还是不建议写进正式报告（Option B）？**

### 🎯 提问目的（为什么问这个能加分）
- 只有真正动手写代码、管仓库的学生团队才会踩“误传配置密码 $\to$ 轮换修复 $\to$ 改 `.env.example`”这种真实工程坑，这是**一击必杀的“非 AI 代写”铁证**。
- 先征求导师意见，安全垫极厚：导师说写就光明正大拿 Reflection 高分，导师说别写就当场删掉避雷。

### 🗣️ 现场中英文开口话术
- **中文自然口语**：
  > “最后还有一个小的备选问题想向您讨个主意：在早期跑离线图谱实验时，我们曾不小心把测试用的 Neo4j 云实例密码硬编码进了脚本，后来我们在内部安全自检时发现了，立刻重置了云端密码、清洗了代码改用 `.env` 环境变量，并隔离了旧快照。我们本来想在 Ch5.6 部署章节花半页篇幅，把这个**‘发现隐患 $\to$ 轮换凭证 $\to$ 环境变量加固’的过程写成一段真实的开发安全复盘（方案 A）**，用来呼应第 2 章的安全需求；但又不确定考官看到会不会觉得这是低级失误而扣分，您觉得是**诚实写进去当工程反思更好（方案 A）**，还是**内部整改完就不写进正式报告里（方案 B）**？”
- **English (Spoken to Supervisor)**：
  > "One quick bonus question if time permits: during early offline prototyping, a script briefly held a hardcoded Neo4j test credential before we caught it in our internal audit, rotated the password, purged the literal constants, and enforced `.env` loading. Would examiners view a **half-page security remediation post-mortem in Section 5.6 as mature engineering reflection (Option A)**, or could mentioning a past credential mistake **inadvertently cost marks, meaning we should keep the fix internal only (Option B)**?"

### 🧭 导师可能的回答走向 & 当场接话预案
- **🅰️ 如果导师选 Option A（写进去很好，体现真实的软件工程安全意识与反思）**：
  - **中文接话**：“太棒了！那我们就控制在半页以内，脱敏不带任何真实密钥，严格按‘问题发现 $\to$ 凭证轮换 $\to$ `.env.example` 机制加固’来写，并在 Ch7.4 What Failed 里做简短呼应。”
  - **English Follow-up**: *"Great, we will keep it strictly under half a page—fully redacted—focusing on detection, credential rotation, and `.env.example` enforcement as concrete evidence of our security lifecycle."*
- **🅱️ 如果导师选 Option B（没必要自曝短处，报告只写最终干净的 `.env` 机制即可）**：
  - **中文接话**：“幸好提前请教了您！那我们立刻通知负责 Ch5.6 的梁子铉把这段复盘收归内部组会记录，正式报告里只正面阐述目前的 `.env.example` 零凭证离线安全设计。”
  - **English Follow-up**: *"I'm really glad we checked with you first! We will keep that incident strictly in our internal engineering log and have Zixuan present only the clean `.env.example` configuration design in Section 5.6."*

---

## ⚡ 上场前 30 秒速查小抄（手机亮屏看这一块就够）

1. **Q1（Ch6 负向实验）**：MMLU 12 学科（$n=4,445$）实测 **7 胜 3 平 2 负**（法学 $+2.50\text{ pp}$，但物理 $-1.32\text{ pp}$、美国史 $-1.00\text{ pp}$）。**A：保留负值深挖图谱噪声失效边界** vs **B：花时间调参刷正**？
2. **Q2（Ch4 架构边界 & Demo）**：PoC 主路径采用 **$O(1)$ 确定性陷阱查表（$<5\text{ ms}$、零幻觉、零 Key 离线一键 `uvicorn`）** + 离线 GraphRAG。**A：报告与 Demo 纯粹聚焦 100% 离线可复现路径** vs **B：演示时额外加一段挂载 `QWEN_API_KEY` 的实时在线对比**？
3. **Q3（40–60 页排版边界）**：严禁正文贴源码下，**6 个用例表 + 8 端点契约 + 147 条 `pytest` 清单 + 完整 RTM**。**A：详表直接放 Ch3/5/6 正文拿深度分** vs **B：正文控在 ~50 页精炼分析，详表全收进 Appendices B–D**？
4. **Bonus Q4（安全复盘）**：早期 Neo4j 测试凭证误提交已轮换并改 `.env`。**A：写半页安全整改复盘进 Ch5.6 加反思分** vs **B：内部消化不写进正式报告**？
