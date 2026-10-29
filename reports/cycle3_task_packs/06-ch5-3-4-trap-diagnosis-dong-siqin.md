# 任务包 06 · 第 5 章 5.3–5.4 题库陷阱工程与诊断算法

| 项 | 内容 |
| :--- | :--- |
| **负责人** | 董思钦（50106060 · PoC 逻辑） |
| **章节** | 第 5.3 节 Question Bank & Trap Engineering ＋ 第 5.4 节 Diagnostic Algorithm（属第 5 章 Implementation） |
| **页数** | 5–6 页（约 **1,800–2,400 English words** + **3 张表 / 1 张图 / 1 段伪代码**） |
| **交付路径** | `reports/final_report/ch05_dong_siqin/` → `outline.md` → `draft.md` |
| **截止** | outline: Week A 周日 23:59 ／ draft: Week B 周日 23:59 |
| **依赖** | 江昊的 5.2 领域模型（你接着他的模型往下写，术语必须一致） |
| **上游硬约束** | 官方 Brief 明令 **正文禁止贴源码**；伪代码可以（≤20 行）；JSON 示例可以 |

---

## 1. 一句话说明你要交付什么

**证明那 36 个陷阱不是随手编的，而是有教学法依据的；并证明诊断算法为什么必须是确定的查表。**

江昊写"陷阱数据结构长什么样"，你写**"这些陷阱为什么长这样、诊断为什么这么算"**。这一章是整份报告**最不可能被 AI 代笔**的地方——因为 AI 不知道你们为什么把法学那道题的 B 选项设成"1 年"而不是"2 年"。**这是你的护城河。**

---

## 2. 逐节结构与字数预算

### 5.3 Question Bank and Trap Engineering (900–1,200 words + **Table 5.4 / 5.5 + Figure 5.2**)

#### 5.3.1 题库规模与构成

先把盘子摊开（数字必须回代码核对）：

| 维度 | 数量 | 说明 |
| :--- | :-: | :--- |
| 题目总数 | **12** | `backend/app/data/seed_questions.py`（932 行） |
| 学科 | **4** | Law / Computer Science / Economics / Software Engineering |
| 干扰项陷阱 | **36** | 平均 3 个／题 |
| 每个错误选项 | 1 个 `trap_id` | 一一对应，无遗漏 |
| 雷达维度 | **5** | 枚举 `radar_hit` 的全部取值写在这儿（自己 grep 代码确认，不要猜） |

**Table 5.4：12 道题的分布表**（Subject / Question ID / Difficulty / 陷阱数 / 对应知识点）。这张表能一秒证明"你们真做了 12 道题"。

#### 5.3.2 陷阱的三段式结构（本节核心，配 **Figure 5.2**）

每个 `TrapDetail` 有四个字段，写清它们在**教学**上的分工：

| 字段 | 教学功能 | 举例（用真实题目） |
| :--- | :--- | :--- |
| `title` | 给这个误区**命名**（学生能记住的标签） | 例："把撤销权除斥期间当作诉讼时效" |
| `desc` | 说明**错在哪**（制造认知冲突） | 学生把《民法典》152 条的 1 年除斥期间与 188 条的 3 年诉讼时效混为一谈 |
| `prereq` | 指出**缺哪个前置知识**（补救方向） | 需先区分"形成权"与"请求权"的时效规则 |
| `radar_hit` | 把这次错误**记到哪个能力维度**上 | → `boundary`（边界条件识别） |

**Figure 5.2**：画一张"错选 → `trap_id` → `TrapDetail(title/desc/prereq/radar_hit)` → 排雷抽屉五层展示"的因果链示意图（Mermaid 或 draw.io 均可）。江昊的 5.2 有类图，你的是**数据如何变成教学反馈**的流动图，两者不重复。

**这一段必须写透一句话**：普通题库只给 `is_correct` 布尔值（binary feedback），学生只知道"我错了"；我们给的是"**我错在哪个概念、缺哪块前置、该补哪个维度**"三分量反馈。这就是本项目的核心贡献，也是 `desc`/`prereq`/`radar_hit` 三个字段存在的全部理由。

#### 5.3.3 陷阱设计方法论（**去 AI 感的黄金段落**）

写清你们的**四类陷阱生成规则**（每种举一个真实题目为例）：

1. **概念近邻型**（conceptual neighbour）：把两个相邻概念互换。法学那道题的"除斥期间 vs 诉讼时效"就是这一类。
2. **边界条件型**（boundary condition）：正确公式套错边界。计算机网络子网划分题把"可用主机数"算成 `2^n` 而不是 `2^n − 2`。
3. **因果倒置型**（causal inversion）：把 A→B 写成 B→A。经济学供需弹性题里把"价格上升导致需求下降"写成"需求下降导致价格上升"。
4. **术语污染型**（terminology contamination）：用行业黑话伪装错误答案。软件工程里把"单元测试"与"集成测试"的覆盖目标对调。

然后写一段**诚实的局限性**（导师最爱这类段落）：
> 12 道题、36 个陷阱的规模不足以宣称统计显著性。我们的目标不是"题库产品"，而是"证明选项级诊断这条路在教学上可行"——这是一份 **feasibility evidence**，不是 benchmark。

#### 5.3.4 数据完整性的自动化保障

写清数据规则怎么被强制（**描述规则 + 引用测试文件，不贴代码**）：
- 每题 `options` 长度必须为 4；
- 错误选项必须带 `trap_id`，且必须能在该题 `traps` 字典里查到（防悬挂引用）；
- `is_correct` 有且仅有一个为真；
- `explanation` 必含权威出处（法学题带 `【权威考点解析 · 民法典第152条】` 式标注）；
- 由 `tests/test_quiz.py`（6 个用例）与 `tests/test_adversarial_backend.py`（25 个对抗性函数）覆盖——**把这条与第 6 章口径对齐**。

### 5.4 Diagnostic Algorithm (700–900 words + **伪代码 + Table 5.6**)

#### 5.4.1 算法：确定性查表，而非模型推理

**全章金句，放段首**：

> **诊断是查表，不是推理（Diagnosis is a lookup, not an inference）。**

给出 ≤20 行**伪代码**（不要贴 Python）：

```
FUNCTION diagnose(question_id, selected_option):
    question ← question_bank[question_id]        # O(1) dictionary index
    IF question IS NULL:
        RETURN 404
    option ← question.options[selected_option]
    IF option IS NULL:
        RETURN 422
    IF option.is_correct:
        RETURN { verdict: "correct", radar_delta: +1 on target dimension }
    trap ← question.traps[option.trap_id]        # trap is attached to the option
    RETURN {
        verdict:      "misconception",
        trap_title:   trap.title,
        explanation:  trap.desc,
        prerequisite: trap.prereq,
        radar_target: trap.radar_hit,
        authoritative: question.explanation      # contains statutory / formula source
    }
END
```

#### 5.4.2 为什么不用 LLM 做诊断（**必写，导师一定会问**）

**Table 5.6：查表 vs LLM 现场生成**

| 维度 | 查表（我们的方案） | LLM 现场生成 |
| :--- | :--- | :--- |
| 延迟 | < 5 ms，本地 | 1–5 s，受网络与配额影响 |
| 离线可用 | ✅ 零外部调用 | ❌ 断网即废 |
| 可复现 | ✅ 同一输入必得同一输出 | ❌ 温度与版本漂移 |
| 可测试 | ✅ 可写断言 | ❌ 难以断言具体措辞 |
| 教学正确性 | ✅ 由人工审校过的权威出处保证 | ❌ 法条/公式幻觉风险 |
| 覆盖面 | ❌ 只能覆盖预定义陷阱 | ✅ 可应对开放回答 |

**最后一行必须写"我们输掉的那一项"**：承认在开放问答场景下查表失效，并说明这正是我们选择闭式选择题界面的根本原因（呼应 Ch2 的 R01/R02 范围决策）。承认边界比假装全能更可信。

#### 5.4.3 雷达分数的会话聚合（初创轻量架构 · 方案 B）

说明 5 个能力维度（Recall, Boundary, Defense, Synthesis, Precision）如何从答题事件中即时累积（**读 `frontend/app.js` 的 `state.radar` 与 `updateRadarCharts()` 实现口径，不要自己发明公式**）：
- **即时增量与削减机制**：
  - 正确作答：`state.radar.recall = min(100, +4)`, `trapDefense = min(100, +5)`, `synthesis = min(100, +3)`；
  - 答错踩坑：`state.radar.trapDefense = max(30, -6)`, `boundary = max(30, -4)`；
  - 每次作答后前端即时驱动 ECharts 重绘，实现零网络开销、零毫秒延迟响应。
- **初创架构取舍（Trade-off Analysis，重点论据）**：
  - 明确写明：本 MVP 采用“前端会话即时增量聚合 + 预置学科基准映射”的精益方案，优先保障单机离线可用，不依赖后端重型事件数据库；
  - 诚实指出简化：当前实现**未引入跨学期时间加权衰减（如艾宾浩斯遗忘曲线或 FSRS 算法）**，学生会话刷新后仅保留基础状态；
  - 呼应第七章：在 Ch7 的 Limitations 与 Future Work 里将“长周期贝叶斯知识追踪（BKT）与时间衰减”列为下一阶段工程演进目标。

---

## 3. 你需要的素材

| 素材 | 路径 |
| :--- | :--- |
| 题库全文（12 题 36 陷阱） | `backend/app/data/seed_questions.py` |
| 诊断服务实现 | `backend/app/services/diagnostic_service.py` |
| 前端雷达即时聚合逻辑 | `frontend/app.js`（搜索 `state.radar` 与 `updateRadarCharts`） |
| 相关测试 | `tests/test_quiz.py`、`tests/test_adversarial_backend.py` |
| 数据契约 | `reports/report_data_contract.md` |

---

## 4. 必读的 3 篇文献（用来支撑"这不是瞎编"）

1. **VanLehn, K. (2011)** 'The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems', *Educational Psychologist*, 46(4), pp. 197–221. → 支撑"为什么细粒度反馈有效"。
2. **Corbett, A.T. and Anderson, J.R. (1994)** 'Knowledge tracing: Modeling the acquisition of procedural knowledge', *User Modeling and User-Adapted Interaction*, 4(4), pp. 253–278. → 支撑"按维度累积能力"。
3. **Koedinger, K.R., Corbett, A.T. and Perfetti, C. (2012)** 'The Knowledge-Learning-Instruction framework', *Cognitive Science*, 36(5), pp. 757–798. → 支撑"前置知识（prerequisite）"概念。

> ⚠️ 这三条是真实存在的经典文献，但**你必须自己核对卷期页码**（Aberdeen 对 Harvard 格式查得严）。**不要凭记忆写 DOI。**

---

## 5. 会被退回的雷区

1. ❌ 只描述数据结构，不解释"为什么这个陷阱有效" → 退回，5.3.3 是本章灵魂。
2. ❌ 说"我们用 AI 生成了陷阱"却不说明人工审校过程 → 学术诚信风险，必须写清"由 X 人审校，依据 Y 教材"。
3. ❌ Table 5.6 只列优势不列劣势 → 退回，导师会当场抓住。
4. ❌ 雷达维度名与代码不一致（`trapDefense` 写成 `trap_defense`）。
5. ❌ 编造文献页码。
6. ❌ **贴 Python 源码**（官方 Brief 禁止；伪代码与 JSON 不算）。

---

## 6. 验收清单（DoD）

- [ ] 1,800–2,400 词，5–6 页
- [ ] **Table 5.4** 12 题分布表 + **Table 5.5** TrapDetail 四字段教学功能表 + **Table 5.6** 查表 vs LLM 对比表
- [ ] **Figure 5.2** 陷阱因果链示意图
- [ ] 四类陷阱生成规则各有真实题目举例
- [ ] 5.4.1 伪代码 ≤20 行，且不是 Python
- [ ] 5.3.3 末尾的诚实局限性段落（12 题不足以统计显著）
- [ ] ≥4 条 Harvard 引用（含上述 3 篇）
- [ ] 雷达维度名与 `seed_questions.py` 完全一致
- [ ] `sources.md` 已附
- [ ] 能不看稿讲 4 分钟

---

## 7. 导师会问你的 3 个问题（准备好 30 秒答法）

**Q1. "就 12 道题也叫题库？这不就是个 demo 吗？"**
> 答：是 demo，我们从来没说它是产品。这 12 道题的作用是**证明机制可行**，不是证明题库规模，报告 5.3.3 末尾明确写了这一点。真正能证明"机制有用"的不是题量，而是那 36 个陷阱每一个都对应一个可命名、可追溯、可补救的具体误区——只要这一层跑通，扩到 1,200 道题是原料问题，不是架构问题。

**Q2. "这些陷阱是你自己想出来的，凭什么说它是学生真实会犯的错？"**
> 答：三类来源。第一，四个学科各自教材与考纲里被反复强调的易错点（如子网划分的 `2^n − 2`）；第二，法学题直接挂在《民法典》152 条与 188 条的真实差异上，这两个条文本身就是学生最容易混淆的一对；第三，我们做了组内交叉评审——36 个陷阱由组内成员互相检查，凡说不出具体错因的一律改成正确选项。**但我们不宣称做过大规模实证验证**，这正是我们列在 Limitations 里的第一条。

**Q3. "为什么不让大模型直接判断学生的误解？现在 LLM 这么强。"**
> 答：因为我们不敢在法条和公式上用会漂移的东西。这道题的正确解析写着"《民法典》第 152 条：自知道或应当知道撤销事由之日起一年内"，如果让模型现场生成，它可能写成"两年"或"三年"——这是教学事故级别的错误。查表的代价是只能覆盖预定义陷阱，收益是**正确性和可复现性**，而这两样恰好是教育场景最不可妥协的。这个取舍写在第 5.4.2 的对比表里，包括我们输掉的那一行。

---

## 8. 提交方式

1. `git switch -c report/ch05-dong-siqin`
2. 文件放 `reports/final_report/ch05_dong_siqin/`
3. 提 PR 到 `develop`，标题：`docs(report): Ch5.3 trap engineering and Ch5.4 diagnostic algorithm`
4. 群里 @ 吴宇轩 + @ 江昊（术语与 5.2 对齐）+ @ 杨明杰（你的诊断链路会被第 6 章引用）
