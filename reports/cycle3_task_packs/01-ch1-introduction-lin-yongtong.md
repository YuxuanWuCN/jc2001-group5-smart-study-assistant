# 任务包 01 · 第 1 章 Introduction and Project Context

| 项 | 内容 |
| :--- | :--- |
| **负责人** | 林泳桐（50106038 · Lead BA） |
| **章节** | 第 1 章 Introduction and Project Context（官方七章之首，全书地基） |
| **页数** | 5–6 页（约 **1,900–2,400 English words** + **3 张表 / 2 张图**） |
| **交付路径** | `reports/final_report/ch01_lin_yongtong/` → `outline.md` → `draft.md` |
| **截止** | outline: Week A 周日 23:59 ／ draft: Week B 周日 23:59 |
| **依赖** | 无，可立即开工。但你的 **Table 1.2（SMART）会被第 7 章逐条对照**，你的 **Table 1.3（Personas）会被第 2 章直接引用**，编号一旦发出不能改 |
| **官方硬要求** | 本章必须覆盖 **problem / background / objectives / intended users or stakeholders / main features / potential practical or business value** 六项，缺一项扣一项分 |

---

## 1. 一句话说明你要交付什么

**说服考官：这个项目值得做，市面上真的缺这东西，而且我们知道自己在给谁做。**

官方要求里最容易漏的是**最后两项**：`intended users or stakeholders` 与 `potential practical or business value`。很多报告把第 1 章写成"背景 + 目标 + 章节导览"，直接丢掉商业价值论证——而导师恰恰最想看到这一段（他一直说"要把报告做成一家初创公司的报告"）。

所以你的第 1 章要有**创业路演的骨架**：痛点 → 为什么现有方案不管用 → 市场空白 → 我们给谁做 → 我们承诺什么 → 为什么这有价值。

---

## 2. 逐节结构与字数预算

### 1.1 Problem and Context: The "Binary Feedback" Trap (500–650 words)

必须回答三件事，按顺序：

1. **场景**：大学生备考的真实形态——考前 2–3 周集中刷题，手上是历年真题、PPT、同学的错题本；
2. **现象**：现有题库工具（包括学校的在线练习）反馈是**二元的**——只给 ✔/✘ 加一段通用解析，不告诉你"你错在哪个概念上"；
3. **后果**：学生把错因归结为"没背熟"，于是重复记忆**同一道题**，考场上换一个问法继续错——**同一个误区会重复三次以上**。

**写法硬要求**：
- **先描述现象，再给术语**：`binary feedback` 是你引入的术语，第一次出现要给定义（例如 *we use the term "binary feedback" to denote the answer-level correctness signal that carries no information about which concept was misunderstood*）。
- **禁止开场白**："随着教育信息化的发展""在当今数字化时代"一律退回。第一句直接进场景。
- **给一个具体的小场景**（50–80 词）比十句抽象论述有用：一个学生在复习《民法典》总则部分，连错三道撤销权相关的题，每次都以为自己"条文没背熟"，实际上是混淆了 152 条的除斥期间与 188 条的诉讼时效。

### 1.2 Background and Related Work (400–500 words)

用三段式写清学术脉络（每段 2–3 句，**每段必须有引用**）：

1. **反馈粒度与学习效果**：细粒度、指向概念的错误反馈显著优于对错反馈（引 VanLehn 2011 的人类/AI 导师对比元分析；Hattie & Timperley 2007 的反馈层级）。
2. **知识追踪与能力维度**：把"掌握程度"建模成多维能力而非单一正确率（引 Corbett & Anderson 1994 的 BKT；Koedinger et al. 2012 的前置知识框架）。
3. **检索练习与间隔重复**：Anki 一类工具证明间隔重复有效（引 Roediger & Karpicke 2006 的 testing effect），但它们不解决"为什么错"。

**这一段的作用**：证明你们的"选项级诊断"不是拍脑袋，而是**站在有名字的学术传统上**。考官评分点里的 Technical Depth 就靠这里起步。

### 1.3 Competitive Landscape (**Table 1.1 + Figure 1.2**)

**Table 1.1：竞品对比（≥5 个产品 × 4 个维度）**

| Product | Feedback granularity | Diagnoses the misconception? | Works offline | Cost to student |
| :--- | :--- | :--- | :--- | :--- |
| Quizlet | Answer-level (✔/✘) | No | Paid tier only | Freemium |
| Anki | Self-assessed (again/hard/good) | No | Yes | Free |
| Khanmigo | Chat-based hints | Partially (LLM) | No | Subscription |
| ChatGPT / general LLM | Full explanation, immediate | No — and spoils the answer | No | Free / subscription |
| Chegg | Worked solutions | No | No | Paid |
| **SmartStudy（本系统）** | **Per-distractor trap** | **Yes — by construction** | **Yes** | **£0** |

**图 Figure 1.2：竞品定位图**（自绘，二维散点：X = 诊断粒度（题级 → 选项级），Y = 离线可用性）。把六个产品点上去，**在每个点旁边写一句它能做什么**——这样图本身就是论证，而不是装饰。

**素材**：`reports/competitor_analysis.md`（124 KB，含 Khanmigo / Socratic / Quizlet Q-Chat / Leitner–SM-2–FSRS / Duolingo Birdbrain / BKT–DKT–IRT–CAT 的拆解，§3.3 有六维对比矩阵）。**读完后压缩成 1 表 1 图 2 段，不要复述整份文档。**

段落里必须有一句**空白定位**：
> 现有产品要么诊断粒度停在**整题**，要么依赖联网的大模型；没有一款产品在**错误选项**这一层做归因，并且能在完全离线的条件下运行。这个空缺不大，但它足够真实，也正是我们决定用 10 周去填它的原因。

> ⚠️ **注意"这个空缺不大"这句必须保留**。声称"这是一个百亿市场"会显得不专业（也与我们只做了 12 道题的规模相矛盾）；承认它是"小空缺"反而可信。

### 1.4 Intended Users and Stakeholders (**Table 1.3，官方强制项**)

#### 1.4.1 三个 Persona（**Table 1.3**）

| | **Persona A · 突击型考试生** | **Persona B · 系统复习者** | **Persona C · 课程教师** |
| :--- | :--- | :--- | :--- |
| 身份 | 大二/大三，4 门考试集中在 2 周 | 研究生，长期系统性复习 | 本课程讲师 / 助教 |
| 当前工具 | Quizlet 卡片、同学错题本、群里的"答案汇总" | Anki、笔记软件、论文 | 学习平台后台、Excel |
| 最大痛点 | 错了不知道为什么错，没时间深究 | 知道自己弱，但看不出"弱在哪个能力维度" | 无法在批改之外看到学生的具体误区分布 |
| 对我们系统的期待 | 5 分钟内知道该补哪一块 | 看到能力维度的长期趋势 | （不直接使用） |
| 是否目标用户 | ✅ 主要 | ✅ 主要 | ⚠️ **明确为非目标用户** |

> 🔴 **Persona C 必须明确写成"非目标用户"**。这不是漏掉了教师端，而是第 2 章 R11 的 lean scoping 决策在第 1 章的呼应。考官会问"老师为什么不能用"，你必须能答"因为我们主动砍掉了教师侧功能，理由是……"。

#### 1.4.2 Stakeholder 表（简短，3–5 行即可）

区分 **users**（操作者）与 **stakeholders**（有利益关系但不操作）：学生（用户）、课程教师（受益方/评估方）、Group 5 团队（开发方）、University of Aberdeen（课程交付方可信度）。

### 1.5 Objectives: Five SMART Goals (**Table 1.2**)

5 条可度量目标，每条必须带数值阈值与验证方式：

**Table 1.2：SMART objectives**

| # | Objective | Metric | Target | Verified by |
| :-: | :--- | :--- | :--- | :--- |
| **O1** | Diagnose misconceptions at option level | Traps seeded per question | ≥3 per question, **36 in total** | `backend/app/data/seed_questions.py` |
| **O2** | Demonstrate with zero external dependencies | External calls at demo time | **0** | Offline rehearsal log |
| **O3** | Maintain an automated regression baseline | pytest cases passing | **145 / 145** | `python -m pytest tests/ -q` |
| **O4** | Provide evidence that graph augmentation helps | MMLU subjects with positive delta | **≥7 of 12** | `graphrag（终）/final_systematic_report.csv` |
| **O5** | Distribute authorship across the team | Members authoring ≥3 pages | **10 of 10** | Appendix A workload profile |

> ⚠️ **O4 必须写"≥7 of 12"**：实测是 7 正 / 3 平 / 2 负。写"全部提升"就是虚假陈述，而且与第 6 章的表直接矛盾。**这条是全篇最容易被自己人打脸的地方。**

> ⚠️ **O5 要谨慎**：如果到提交时实际不是 10/10（有人没交），要么把那人的贡献如实调整、要么把这条目标改成实际数字并在 Appendix A 说明。**不要为了好看而虚报工作量分配**——Appendix A 是要全员签署的。

### 1.6 Main Features and Business Value (400–500 words)

#### 1.6.1 主要功能（一段话 + 4 个 bullet，不要长篇）

用一句话概括产品，再用 4 条 bullet 列功能（**每条一句话，对应一个需求 ID**）：
- 按学科浏览并作答（R01–R02）；
- **选项级陷阱诊断**——错选后给出误区命名、错因解释、缺失前置知识、雷达维度归因（R03）；
- 五维能力雷达与学情摘要（R04–R05）；
- 完全离线、零构建、中英双语双主题（R07–R09）。

#### 1.6.2 Business and Practical Value（**本节是加分点，官方强制项**）

写清四层价值，每层 2–3 句：

1. **对学生**：把"我错了"变成"我缺哪块前置知识"，把复习从**重刷题**转向**补短板**——单位时间的学习产出更高。
2. **对教师**：无需改变教学流程，即可通过维度分布看到班级的共性误区（作为未来工作，不做承诺）。
3. **对成本结构**：因为诊断是**确定性查表**而不是模型推理，边际推理成本为 **£0**，且可在**无网络环境**运行——这在网络不稳定或按 token 计费的场景下是硬优势。
4. **可迁移性**：题库与陷阱是**内容**而不是代码，同一套机制可平移到任何有标准答案与明确误区的学科（法律、医学、语言考试）。

**然后给一句诚实的商业化定性**（这一段非常"初创报告"，也是导师想看的）：
> 我们**不声称这是一个可行的商业产品**。以 12 道题、10 周、零预算的交付形态，它更接近一个 **feasibility prototype**：它证明了"选项级诊断在技术上便宜、在教学上可行"，而真正决定商业可行性的是内容规模（题库与陷阱的人工编写成本）与分发渠道——这两件事我们都在第 7 章的 Future Work 里给出了具体路径，而不是含糊地说"未来可以推广"。

### 1.7 Report Structure (120–150 words)

一段话说明后面六章各写什么，一句话一章。**不要复制目录**，要写"每章在论证链条上承担什么角色"，例如：*Chapter 2 fixes the scope by listing what we deliberately did not build; Chapter 3 formalises it into use cases…*

---

## 3. 你需要的素材（全部在仓库里，只读，不要改）

| 素材 | 路径 | 用法 |
| :--- | :--- | :--- |
| 竞品深度分析 | `reports/competitor_analysis.md` | 1.3 的全部弹药 |
| 立项书 | `reports/project_proposal.md` | 1.1 / 1.6 的早期口径，**不要照抄**，逻辑已更新 |
| 上一周期进展 | `reports/phase2_cycle2_progress_report.md` §1–2 | 1.1 场景说明可复用其调研口径 |
| 题库结构 | `backend/app/data/seed_questions.py` | 证明 per-distractor trap 不是口号（12 题 / 4 学科 / 36 陷阱） |
| 图谱增强实测 | `graphrag（终）/final_systematic_report.csv` | O4 的数据来源 |
| 官方 Brief | `JC2001-GroupProjectDescription-and-Requirements-2026-27.txt` | 确认六项必含内容 |

---

## 4. 会被退回的雷区

1. ❌ 开头"随着人工智能的快速发展"→ 立刻重写。
2. ❌ **漏掉 1.4（用户与利益相关者）或 1.6.2（商业价值）** → 违反官方必含项，直接扣分。
3. ❌ 竞品表里出现"其他产品：功能弱"这类不可核查判断，每格必须有事实依据。
4. ❌ SMART 写"提升用户体验"这类不可度量目标。
5. ❌ 通篇没有数字。
6. ❌ 直接把 `reports/competitor_analysis.md` 的段落翻译过来 → 查重会撞，且那份文风正是导师说的"AI 感"。**压缩到 1/20。**
7. ❌ 出现 `leverage` / `cutting-edge` / `seamlessly` / `revolutionise`。
8. ❌ 声称"这是一个巨大的市场"→ 与 12 道题的规模自相矛盾。

---

## 5. 验收清单（DoD）

- [ ] 1,900–2,400 词，5–6 页
- [ ] **Table 1.1** 竞品（≥5 产品 × 4 维度）+ **Table 1.2** 5 条 SMART + **Table 1.3** 三 Persona
- [ ] **Figure 1.1** Value Proposition Canvas（自绘）+ **Figure 1.2** 竞品定位散点图（自绘）
- [ ] `binary feedback` 与 `per-distractor misconception diagnosis` 首次出现各有定义
- [ ] 1.4 Persona C 明确标"非目标用户"
- [ ] 1.6.2 四层价值 + "不声称是商业产品"的诚实定性
- [ ] 官方六项必含内容逐项自查打勾（problem / background / objectives / users / features / business value）
- [ ] ≥6 条 Harvard 引用（VanLehn 2011、Hattie & Timperley 2007、Corbett & Anderson 1994、Koedinger et al. 2012、Roediger & Karpicke 2006、Ries 2011、Osterwalder & Pigneur 2014、Sommerville 2020 —— **卷期页码自己核对，不许凭记忆写 DOI**）
- [ ] `sources.md` 列出用到的仓库文件
- [ ] 能不看稿讲 3 分钟

---

## 6. 导师会问你的 3 个问题（准备好 30 秒答法）

**Q1. "你们和 Quizlet、ChatGPT 的区别，一句话说清楚。"**
> 答：Quizlet 只告诉你对错，ChatGPT 直接把答案给你。我们在你选错的**那个选项**上挂了一个错因标签，告诉你"你混淆的是哪两个概念、缺哪块前置知识"——诊断粒度到**选项**而不是**题**，而且完全离线可跑。

**Q2. "为什么大学生需要这个？有证据吗？"**
> 答：**我们没有做正式问卷，这一点在 1.1 和第 6 章的 Threats to Validity 里都写明了。** 我们的依据是三条：文献里的细粒度反馈研究、竞品行为分析（现有产品确实只给对错）、以及组内 10 人的非正式验证。所以我们在报告里把它定位为"有据可依的假设"，而不是"已验证的用户事实"——我们认为把没做的调研说成做了，比承认没做更危险。

**Q3. "O4 那条目标，你们真的达到 7/12 了吗？"**
> 答：达到了，但口径是"7 个正提升"，另外 3 个持平、2 个是负的（US History −1.0pp、HS Physics −1.3pp）。我们把两个负值也写进了第 6 章，并讨论了可能原因（物理题需要多步数值推理，图谱的结构化约束在这里更像噪声）。**我们宁愿报一个诚实的 58%，也不要一个漂亮但不成立的 100%。**

---

## 7. 提交方式

1. `git switch -c report/ch01-lin-yongtong`（从 `develop` 切）
2. 文件放 `reports/final_report/ch01_lin_yongtong/`，图放 `figures/`
3. 提 PR 到 `develop`，标题：`docs(report): Ch1 introduction and project context`
4. 群里 @ 吴宇轩，并附一句"我这章的核心论点是：……"
