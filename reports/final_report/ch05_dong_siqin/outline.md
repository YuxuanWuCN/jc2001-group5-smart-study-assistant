# Ch 5.3–5.4 写作骨架（G1 交付）

| 项 | 内容 |
| :--- | :--- |
| 负责人 | 董思钦（50106060 · PoC 逻辑） |
| 章节 | 5.3 Question Bank and Trap Engineering ＋ 5.4 Diagnostic Algorithm |
| 目标篇幅 | 5–6 页 / 1,800–2,400 English words |
| 必配图表 | Table 5.4、Table 5.5、Table 5.6、Figure 5.2（编号已全组锁定，不得改） |
| 交付路径 | `reports/final_report/ch05_dong_siqin/`（outline.md → draft.md） |
| 本文件状态 | G1 骨架（Week A 周日 23:59 前提交） |
| 正文语言 | 英文（本骨架用中文写说明，最终 draft 转英文） |

> **本骨架的全部数字已回代码核对**（2026-10-19）。任务包 06 原文有 4 处与代码不符，本文件已按实测值修正，见文末「与任务包 06 的差异」。

---

## 一、报告正文标题结构（供 draft 直接沿用）

```text
5.  Implementation
    5.3  Question Bank and Trap Engineering
        5.3.1  Scale and Composition of the Question Bank
        5.3.2  The Three-Part Anatomy of a Trap
        5.3.3  Trap Design Methodology and Its Limits
        5.3.4  Automated Data-Integrity Assurance
    5.4  Diagnostic Algorithm
        5.4.1  Diagnosis Is a Lookup, Not an Inference
        5.4.2  Why the Diagnostician Is Not an LLM
        5.4.3  Aggregating the Five-Dimension Radar
```

（报告正文 9 个标题；配合本骨架的 Tables / Figures / Sources 三节，满足 G1「≥12 行三级标题＋素材清单」。）

---

## 二、逐节写作说明

### 5.3 Question Bank and Trap Engineering（预算 900–1,200 词＋ Table 5.4 / 5.5 ＋ Figure 5.2）

#### 5.3.1 Scale and Composition of the Question Bank
- **要写什么**：先把盘子摊开，证明"12 道题是真做了、不是凑数"；给出学科分布与难度分布；说明"每题恰好 3 个干扰项"不是巧合而是设计约束。
- **素材**：`backend/app/data/seed_questions.py`（657 行；`SEED_QUESTIONS` 共 12 项）
- **实测数字（照抄）**：
  - 题目 12 道；学科 law 3 / cs 3 / econ 3 / se 3
  - 干扰项陷阱 36 个，**每题恰好 3 个**（均值 3.00）
  - 难度：★★★☆☆ 2 题、★★★★☆ 8 题、★★★★★ 2 题
- **配 Table 5.4**：12 题分布表（Subject / Question ID / Difficulty / Trap count / Knowledge point），数据见本文件第四节
- **忌**：不要说"题库规模可观"——12 道题就是 feasibility prototype，直说

#### 5.3.2 The Three-Part Anatomy of a Trap
- **要写什么**：`TrapDetail` 四个字段在教学上各司其职；核心论点——**普通题库只给二元对错，我们给"错在哪个概念 + 缺哪块前置 + 记到哪个维度"的三分量反馈**。
- **素材**：`backend/app/models/quiz.py`（`TrapDetail` 定义）；真实样本用 `law_1 / trap_law_1`
- **配 Table 5.5**：四字段教学功能表（字段 / 教学功能 / 真实取值）
- **配 Figure 5.2**：错选 → `trap_id` → `TrapDetail(title/desc/prereq/radar_hit)` → 诊断抽屉展示 的因果链（与江昊 5.2 的类图不重复：他画结构，你画数据流动）
- **⚠️ 引用规范**：陷阱 `title` 原文带 🚨 前缀且口语化（如"🚨 典型混淆陷阱：把'形成权除斥期间'错套为'3年普通诉讼时效'"），**正文必须转写为陈述句**，不要直接引用 emoji 原文

#### 5.3.3 Trap Design Methodology and Its Limits
- **要写什么**：归纳四类陷阱生成规则，**每类配一道真实题目**；末尾写"诚实的局限性"——12 题/36 陷阱不足以宣称统计显著，这是 feasibility evidence 而非 benchmark。
- **素材**：从 36 条陷阱里挑（真实配对见本文件第五节）
- **关键**：这一节是"去 AI 感"的核心，必须写清人工审校过程（谁审、依据哪本教材/考纲），否则有学术诚信风险
- **⚠️ 死线提醒**：代码里 4 条陷阱描述含**无出处的百分比**（"全校 64%""58%""71%""全班 60%"）。**正文绝对不要引用这些数字**，否则违反「每个数字必须可追溯」的硬规矩。改写为"依据教材与考纲标注的高频易错点"，并把"未做大规模实证验证"放进 Limitations。

#### 5.3.4 Automated Data-Integrity Assurance
- **要写什么**：数据规则如何被强制（只描述规则 + 引用测试文件，**不贴代码**），并对齐第 6 章口径。
- **实测（可断言）**：12/12 题选项数 = 4；每题恰 1 个 `is_correct`；无悬挂 `trap_id`；四字段无空缺；12/12 题的 `explanation` 均带 `【权威考点解析 · …】` 权威出处标注
- **素材**：`tests/test_quiz.py`（6 个用例）、`tests/test_adversarial_backend.py`（25 个对抗性测试函数，分布在 6 个测试类）
- **诚实加分项**：前端 `frontend/app.js` 内嵌了一份**中英双语题库镜像**（19 个题目块、57 处 `radarHit` 标注），与后端 `seed_questions.py` 不是同一份数据源。写成"已知的工程简化/双份数据源风险"，比假装单一数据源更可信。

### 5.4 Diagnostic Algorithm（预算 700–900 词＋ 伪代码 ＋ Table 5.6）

#### 5.4.1 Diagnosis Is a Lookup, Not an Inference
- **要写什么**：段首放金句 **"Diagnosis is a lookup, not an inference."**；给出 ≤20 行伪代码（**不是 Python**）。
- **伪代码必须按真实实现写**（任务包原来的 404/422 与代码不符）：查不到题目 → **200 + 优雅兜底**（返回"题目检索未命中"、`fallback_mode=true`），不是 404；选项不匹配 → 同样兜底；422 只出现在请求体 schema 校验失败时。
- **素材**：`backend/app/services/diagnostic_service.py`（274 行）、`backend/app/routers/diagnose.py`

#### 5.4.2 Why the Diagnostician Is Not an LLM
- **要写什么**：Table 5.6 逐维对比"确定性查表 vs LLM 现场生成"（延迟 / 离线 / 可复现 / 可测试 / 教学正确性 / 覆盖面）。
- **必写**：**最后一行承认我们输掉的那一项**——开放问答场景查表失效，这正是选择闭式选择题界面的根本原因（呼应 Ch2 的 R01/R02 范围裁剪）。
- **可引一句实测**：LLM 现场生成在法条/公式上可能写出"2 年/3 年"这类教学事故级错误；查表由人工审校的权威出处保证正确性。

#### 5.4.3 Aggregating the Five-Dimension Radar
- **数据源已由组长裁定改为 `frontend/app.js`**（方案 B：前端轻量聚合、无复杂时间衰减），不再引用不存在的 `report_service.py` / `/api/reports/trend`。
- **实测口径（必须照此写，不得自创公式）**：

| 情况 | 维度变动 | 钳制 |
| :--- | :--- | :--- |
| 答对 | `recall +4`、`trapDefense +5`、`synthesis +3`、`predictedScore +0.5` | 各维度上限 100；predictedScore 上限 99 |
| 答错 | `trapDefense −6`、`boundary −4` | 下限 30 |

- **两个必须如实写的关键事实**：
  1. 前端**完全没有消费**后端的 `radar_dimension` / `score_delta`（`app.js` 中引用次数为 0）——增量是按"对/错"固定发放的启发式，**不随具体陷阱的 `radar_hit` 变化**。
  2. 初始（0 次作答）雷达不是零值，而是预置基线：`recall 76 / boundary 62 / trapDefense 65 / synthesis 72 / precision 81`。
- **已发现的文案 bug（建议先修再写，或写进 Limitations）**：UI 提示写"Defense Index **+6**"，实际代码加的是 **+5**。建议让梁子铉/习羽赛改成 +5，或报告里注明以代码为准。
- **定性结论**：写成"session-scoped, rule-based aggregation without temporal decay"，并列入 Ch7 Limitations（R04 因此为"部分满足"）。

---

## 三、图表清单（编号已锁定，不得改动）

| 编号 | 内容 | 数据来源 | 状态 |
| :--- | :--- | :--- | :--- |
| Table 5.4 | 12 题分布表 | `seed_questions.py`（见第四节） | 数据已备好 |
| Table 5.5 | `TrapDetail` 四字段教学功能 | `law_1 / trap_law_1` | 数据已备好 |
| Table 5.6 | 查表 vs LLM 对比（**含劣势行**） | 本节论述 | 待写 |
| Figure 5.2 | 陷阱因果链（错选→trap→诊断反馈） | 自绘（Mermaid 或 draw.io） | 待画 |

---

## 四、Table 5.4 数据（已核对，可直接用）

| ID | Subject | Difficulty | Traps | Knowledge point |
| :--- | :--- | :-: | :-: | :--- |
| law_1 | Law | ★★★☆☆ | 3 | Revocable juristic acts · limitation period for the right of revocation |
| law_2 | Law | ★★★★☆ | 3 | Property law · requirements and defences of bona fide acquisition |
| law_3 | Law | ★★★★☆ | 3 | General provisions · apparent authority and appearance-based liability |
| cs_1 | CS | ★★★★☆ | 3 | RISC pipeline · hazard handling and forwarding/bypassing |
| cs_2 | CS | ★★★★☆ | 3 | Memory hierarchy · set-associative cache mapping and miss analysis |
| cs_3 | CS | ★★★★★ | 3 | Virtual memory · TLB and page-fault handling sequence |
| econ_1 | Econ | ★★★★☆ | 3 | Violations of classical assumptions · multicollinearity and omitted-variable bias |
| econ_2 | Econ | ★★★★★ | 3 | Causal inference · instrumental variables (IV/2SLS) and weak instruments |
| econ_3 | Econ | ★★★★☆ | 3 | Violations of classical assumptions · heteroskedasticity, White test, robust SEs |
| se_1 | SE | ★★★☆☆ | 3 | Process models · Scrum versus waterfall trade-off |
| se_2 | SE | ★★★★☆ | 3 | OO architecture · SOLID and the dependency-inversion principle |
| se_3 | SE | ★★★★☆ | 3 | Quality assurance · boundary-value analysis and mutation testing |

雷达维度真实分布（写 5.3.1 或 5.4.3 时用）：`boundary` 12、`recall` 8、`trapDefense` 7、`synthesis` 7、`precision` 2。

---

## 五、四类陷阱的真实配对（替换任务包里的虚构举例）

| 陷阱类型 | 用这题 | 陷阱 ID | `radar_hit` | 一句话错因 |
| :--- | :--- | :--- | :--- | :--- |
| Conceptual neighbour | `law_1` | `trap_law_1` | **`trapDefense`** | 把形成权的除斥期间错套为 3 年普通诉讼时效 |
| Boundary condition | `cs_2` | `trap_cs_2_2` | `boundary` | 块大小盲目增大 → 组数被压缩、冲突缺失加剧 |
| Causal inversion | `econ_3` | `trap_econ_3_1` | `recall` | 把"有效性受损"误判为"估计量失去无偏性" |
| Terminology contamination | `se_3` | `trap_se_3_3` | `recall` | 把"变异测试"误判为"性能压测" |

（备选：`cs_3 / trap_cs_3_2`（Fault 重执 vs Interrupt 返回 PC+4，boundary）、`cs_3 / trap_cs_3_1`（TLB Miss ≠ Page Fault，trapDefense）、`econ_1 / trap_econ_1`（精度不足 ≠ 有偏，recall）。）

---

## 六、引用（Crossref 已核）

1. VanLehn, K. (2011) 'The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems', *Educational Psychologist*, 46(4), pp. 197–221. doi:10.1080/00461520.2011.611369.
2. Corbett, A.T. and Anderson, J.R. (1994) 'Knowledge tracing: Modeling the acquisition of procedural knowledge', *User Modeling and User-Adapted Interaction*, 4(4), pp. 253–278. doi:10.1007/BF01099821.
   ⚠️ Crossref 的出版年份记为 **1995**，学界多引作 1994；提交前请以出版社页面为准并全篇统一。
3. Koedinger, K.R., Corbett, A.T. and Perfetti, C. (2012) 'The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning', *Cognitive Science*, 36(5), pp. 757–798. doi:10.1111/j.1551-6709.2012.01245.x.

---

## 七、DoD 自检（draft 阶段逐项打勾）

- [ ] 1,800–2,400 词，5–6 页
- [ ] Table 5.4 / 5.5 / 5.6 ＋ Figure 5.2 齐备，编号与全组锁定表一致
- [ ] 四类陷阱各配**真实题目**举例（见第五节）
- [ ] 5.4.1 伪代码 ≤20 行且非 Python，语义与实现一致（200＋兜底）
- [ ] 5.3.3 末尾有诚实局限性段
- [ ] 5.4.3 口径与 `app.js` 完全一致（+4/+5/+3、−6/−4、floor 30、基线值）
- [ ] 雷达维度名逐字一致：`recall` / `boundary` / `trapDefense` / `synthesis` / `precision`
- [ ] 正文**无源码**（搜索 `def ` / `import ` / ```python）
- [ ] Harvard 引用 ≥4 条，卷期页码已核
- [ ] `sources.md` 已附（见同目录）
- [ ] 能不看稿讲 4 分钟；能答 Q1–Q3

---

## 八、与任务包 06 的差异（已按实测修正，建议同步告知吴宇轩）

| 任务包 06 原文 | 实测 | 本骨架采用 |
| :--- | :--- | :--- |
| `seed_questions.py` 932 行 | 657 行 | 657 |
| 5.3.2 表：`law_1` 的 `radar_hit` = `boundary` | `trapDefense` | `trapDefense` |
| 5.3.3 举例：子网划分 `2^n−2` | 题库中无此题型 | 换成 `cs_2 / trap_cs_2_2` |
| 5.3.3 举例：供需弹性因果倒置 | econ 三题均为计量经济学 | 换成 `econ_3 / trap_econ_3_1` |
| 5.3.3 举例：单元测试 vs 集成测试 | 无此题型 | 换成 `se_3 / trap_se_3_3` |
| 5.4.3 读 `report_service.py` / `/api/reports/trend` | 两者均不存在 | 改读 `frontend/app.js`（组长已裁定） |
| 伪代码 404 / 422 | 实现为 200＋兜底 | 按实际写 |
| 端点 8 个（总索引 README） | 4 个 | 不写端点数或写 4 |

---

## 九、已知风险（写作前必须处理）

1. **凭证泄露（安全事件，优先级最高）**：`frontend/app.js` 第 1207 行硬编码了一个 `sk-` 开头的 API Key（变量 `GEMINI_DEFAULT_KEY`，长度 67），并作为默认值预填入界面输入框。仓库是 public，**任何人可读取并盗用额度**。必须：控制台吊销该 Key → 从代码与 git 历史中移除 → 全组自查。此事与 5.3/5.4 无直接关系，但属于必须在提交前处理的问题（对应总清单里"凭证泄露已处理"一项）。
2. **无出处百分比**（4 处）：不得进入正文，见 5.3.3 提醒。
3. **emoji 陷阱标题**：正文需转写，不得原文引用。
4. **前端/后端双份题库**：5.3.4 如实说明，或由梁子铉后续统一数据源。
5. **+6 / +5 文案不一致**：建议修正 UI 文案为 +5。
