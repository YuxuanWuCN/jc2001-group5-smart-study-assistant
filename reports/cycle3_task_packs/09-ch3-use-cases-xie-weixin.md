# 任务包 09 · 第 3 章 Use Cases and Requirements Modelling（＋附录 B）

| 项 | 内容 |
| :--- | :--- |
| **负责人** | 谢炜昕（50106034 · QA / 技术报告 Lead） |
| **章节** | 第 3 章 Use Cases and Requirements Modelling ＋ **附录 B Requirements Traceability Matrix** ＋ 全篇格式统稿 |
| **页数** | 6–7 页（约 **2,000–2,600 English words** + **1 张表 / 2 张图 / 6 个用例描述**） |
| **交付路径** | `reports/final_report/ch03_xie_weixin/` → `outline.md` → `draft.md` |
| **截止** | outline: Week A 周日 23:59 ／ draft: Week B 周日 23:59 |
| **依赖** | 张梓健的 Table 2.2（14 条 MoSCoW 需求）——你是本章的**独立章节负责人**，但案例必须能映射回他的需求 ID |
| **为什么是你** | 官方 Brief 把「Use Cases and Requirements Modelling」列为**独立必含章节**，评分点单列「Requirements and Use Cases」；你同时负责全篇格式，正好把这一章做成范例 |

---

## 1. 一句话说明你要交付什么

**把第 2 章的 14 条需求文字，"翻译"成 6 个可执行、可验收、可追溯到需求的用例——并画出图。**

一个常见的失败写法是「把功能列表改写成用例表格」，考官一眼就能看出来。合格的写法是：**每个用例都有前置条件、主流程、异常流、后置条件，且每条 NFR 都能挂到某个用例上。** 你还要顺手做一件只有你能做的事：**建立 RTM（需求追溯矩阵），让每一章都能看见彼此的钩子**——这正是评分点「Consistency」最直接的证据。

---

## 2. 逐节结构与字数预算

### 3.1 System Context and Actors (400–500 words)

写清三层边界（可配一张简短的系统边界说明，不必单独占图号）：

| 角色 | 类型 | 描述 | 对应 Ch1 的 Persona |
| :--- | :--- | :--- | :--- |
| **Student（备考学生）** | 主参与者（Primary） | 本项目唯一的目标操作者 | Persona A / B |
| **Instructor / Marker（教师/评分人）** | 次要参与者（Secondary） | 不直接操作系统，仅通过 PoC 与报告评审 | Persona C（明确为非目标用户） |
| **Group 5 Development Team** | 支持参与者（Supporting） | 开发、测试、部署 | — |

**必须写清一句边界声明**（这是 Ch2 的 lean scoping 在建模层的呼应）：
> 本项目有意**不建模**教师侧管理功能（班级管理、成绩导出、题目审批工作流），因为这些属于 R11–R14 中被显式划入 Won't 的范围。把它们画进用例图会把"做了但没做完"变成"看起来想做很多"，这与我们第 2 章的裁剪立场矛盾。

### 3.2 Use Case Diagram (**Figure 3.1**，本图已有资产，直接复用)

复用 `reports/figures/fig_use_case_diagram.png`（3457×932）及其 `.mmd` 源文件。

**但你必须做两件事，否则图会露馅**：
1. **核对图里的用例是否与 3.3 的 6 个 UC 一一对应**。多出来的删掉（或标为 future），少了的补进 3.3。图上画了 8 个但正文只写 6 个 = 一致性扣分。
2. **在正文里逐条引用图元**："Figure 3.1 shows six use cases..."，并说明 `«include»` / `«extend»` 关系为何这样画。特别是如果图里有 **`View Trap Detail` 作为 `Answer Question` 的 `«extend»`**，要解释理由（诊情抽屉只在错答时才展开）。

**Table 3.1：六用例摘要**（放在图后面，与图一一对应）

| ID | 用例名 | 主参与者 | 优先级 | 关联需求 | 关联章节 |
| :--- | :--- | :--- | :-: | :--- | :--- |
| UC-01 | Answer a Question | Student | Must | R01, R02 | Ch5.3 |
| UC-02 | View Trap-Level Diagnosis | Student | Must | R03 | Ch5.3–5.4 |
| UC-03 | View Radar and Progress Report | Student | Must | R04, R05 | Ch5.1 |
| UC-04 | Log In | Student | Must | R06 | Ch5.2 |
| UC-05 | Register a New Account | Student | Must | R06 | Ch5.2 |
| UC-06 | Switch Subject and Language | Student | Should | R01, R07 | Ch5.5 |

### 3.3 Key Use Case Descriptions (1,200–1,500 words，**6 个，每个 200–250 词**)

**统一模板（6 个都用同一个，考官看格式一致性）**：

> **UC-0X — Name**
> **Actor**: Student
> **Goal**: …（一句话，动词开头）
> **Preconditions**: …
> **Main Success Scenario**:
> 1. …
> 2. …
> 3. …
> **Alternate / Exception Flows**:
> 3a. 若 question_id 不存在 → 系统返回 404 并提示"题目已下线"
> 3b. 若 selected_option 非法 → 系统返回 422，不改变雷达分数
> **Postconditions**: …
> **Non-Functional Notes**: 响应 P95 < 100 ms（NFR-P1）；无网络依赖（NFR-R2）
> **Traces to**: R03

**六个用例的核心内容提示**（不要照抄，要写成你自己的话）：

- **UC-01 Answer a Question**：前置 = 已进入某学科且题目已加载；主流程 3–5 步（选答题→选选项→提交→收到判定）；异常 = 题目不存在 404 / 选项非法 422 / 重复提交幂等；后置 = 会话里新增一条作答记录。
- **UC-02 View Trap-Level Diagnosis**（**本章最重要，写 300 词也可以**）：前置 = UC-01 判定为错误；主流程 = 系统按 `trap_id` 查表 → 取出 `title/desc/prereq/radar_hit` → 渲染五层抽屉；异常 = 正确作答时不触发（这是 `«extend»` 的依据）；后置 = 雷达对应维度 −1（或按实现口径）。**必须写出"这是查表行为，不是模型推理"**，与 Ch5.4 呼应。
- **UC-03 View Radar and Progress Report**：前置 = 至少一次作答（否则进入空状态）；主流程 = 聚合 → 五维雷达 + 学情卡；异常 = 0 次作答 → 展示定义良好的空状态而不是 `NaN`（**这条直接来自测试 `test_reports.py` 的空状态用例，写进去**）。
- **UC-04 Log In**：前置 = 已注册或使用 demo 账号；主流程 = 输入 → 校验 → 本地保存会话；异常 = 密码错误 401；后置 = 前端进入主控制台。
- **UC-05 Register**：前置 = 用户名未被占用；异常 = 已存在 409 / 密码规则不符 422。
- **UC-06 Switch Subject and Language**：前置 = 已在主控制台；主流程 = 切换学科 → 重新拉取 `/api/quiz?subject=`；切换语言 → 不重新加载页面；**这条用于承载 R07/R08 两条 Should 需求。**

> ⚠️ **状态码必须回 `backend/app/` 核对**（router 里是 `HTTPException(status_code=...)`）。写错状态码是考官最容易抓的一致性错误。

### 3.4 Behavioural Modelling (400–500 words + **Figure 3.2**)

官方 Brief 要求 "business process models"。用一张**答题与诊断的状态机**（**Figure 3.2**，自绘，Mermaid `stateDiagram-v2` 即可）覆盖：

```
[*] → BrowsingSubject → QuestionPresented → OptionSelected → Submitted
Submitted → CorrectVerdict → NextQuestion → QuestionPresented
Submitted → MisconceptionVerdict → TrapDrawerOpen → RadarUpdated → NextQuestion
TrapDrawerOpen → NextQuestion (user closes drawer)
```

正文写清：**为什么用状态机而不是活动图**——因为本系统是单用户、单流程、无并发的交互，状态机比活动图更能表达"错了之后有第二条路径"这个核心分支。

**如果时间允许**，再补一张 activity diagram 表达 `POST /api/diagnose` 的服务端处理流（可作为 Figure 3.2 的 b 图，或省掉，不要为凑图而画）。

### 3.5 Requirements Traceability (300–400 words → **附录 B**)

正文里只写**方法**与**结论**，明细放附录 B：

1. **方法**：每条需求（R01–R14）→ 映射到 用例（UC-0X）→ 映射到 实现位置（章节 / 端点）→ 映射到 验证证据（测试文件或评估）。
2. **结论**：14 条 Must/Should 需求中，**13 条有实现与验证证据**，R10（GraphRAG 在线链路）为部分实现——**与 Ch6 Table 6.5 的口径必须一字不差**。
3. **附录 B**：完整的 RTM 表格（14 行 × 5 列：ID / 需求 / 用例 / 实现章节 / 验证证据）。

---

## 3. 你作为「格式统稿人」的额外职责（这是你被选中的真正原因）

在全部章节回收后（Week C），你要做一遍**全篇一致性手术**，逐项检查：

| 检查项 | 标准 |
| :--- | :--- |
| 图表编号连续性 | 17 图 + 14 表，编号无跳号、无重号（以 master plan §2.3 为准） |
| 术语一致 | `Trap Drawer` 不写成 `trap drawer`/`陷阱抽屉` 混用；`radar dimension` 统一；`GraphRAG` 大小写统一 |
| 需求 ID 一致 | R01–R14 全篇同编号同措辞（与你自己的 Table 3.1、杨明杰 Table 6.5 逐字对齐） |
| 页边距/字体/行距 | A4、2.54 cm、12 pt、Times New Roman、1.5 倍行距 |
| 引用格式 | Harvard，全部进 References，且正文引用与文献列表一一对应（无孤儿引用） |
| 图表标题格式 | `Figure N: caption.` / `Table N: caption.`（冒号，非句点） |
| 页数 | 正文（Ch1–Ch7）**40–60 页**，超了砍、少了补 |
| 无源码 | 全文搜索 `def ` / `import ` / ```python，清干净 |

---

## 4. 会被退回的雷区

1. ❌ **用例图有 8 个用例，正文只写 6 个** → 一致性直接扣分。
2. ❌ 用例没有 exception flow（只写 happy path）→ 这是最容易识别的"AI 生成味"。
3. ❌ 状态码写错（把 422 写成 400、把 409 写成 422）→ 回代码核对。
4. ❌ 漏掉 `«extend»` / `«include»` 的解释 → 图会被认为是从网上找的。
5. ❌ R10 写成"完全满足"→ 与 Ch6 冲突，直接失去 Consistency 分。
6. ❌ 附录 B 的 RTM 与 Table 3.1、Table 6.5 三处编号不一致。

---

## 5. 验收清单（DoD）

- [ ] 2,000–2,600 词，6–7 页
- [ ] **Figure 3.1** 用例图（复用）+ **Figure 3.2** 答题状态机（新绘）
- [ ] **Table 3.1** 六用例摘要，与图一一对应
- [ ] 6 个用例描述格式完全统一，每个都含 Preconditions / Main / Alternate / Postconditions
- [ ] 3.1 有"不建模教师侧"的边界声明
- [ ] 3.5 + 附录 B 的 RTM 覆盖 R01–R14
- [ ] R10 在正文与附录 B 中均标"部分实现"
- [ ] `sources.md` 已附
- [ ] 全篇格式统稿检查表（§3）在 Week C 完成并回报

---

## 6. 导师会问你的 3 个问题（准备好 30 秒答法）

**Q1. "UML 图是你自己画的还是拿工具生成的？"**
> 答：用例图与类图有 `.mmd` 源文件（`reports/figures/`），我们先用 Mermaid 写语义、再用 draw.io 精修导出的 PNG/SVG，两条链路的源文件都在仓库里可复现。状态机与架构图是本周新画的，源文件在 `reports/figures/` 下同名 `.mmd`。**（如果导师追问，直接打开文件给他看。）**

**Q2. "用例图里为什么没有教师？"**
> 答：因为教师被我们明确划在目标用户之外（Ch1 的 Persona C、Ch2 的 R11–R14 Won't 清单）。这不是漏画——如果把教师画进去，图会暗示我们要做班级管理，但我们没做，也不打算在这个周期做。图只画我们真的交付的东西。

**Q3. "需求追溯表不就是把东西抄两遍吗？"**
> 答：不是抄，是**验证覆盖**。RTM 的作用是让你一眼看出"哪条需求没有测试证据"。我们做出来就发现 R10 只有离线评估证据、没有在线链路证据，所以标了"部分实现"——这条如果不做追溯，很容易在报告里被写成"已实现"，然后在答辩时被当场问穿。

---

## 7. 提交方式

1. `git switch -c report/ch03-xie-weixin`
2. 文件放 `reports/final_report/ch03_xie_weixin/`
3. 提 PR 到 `develop`，标题：`docs(report): Ch3 use cases and requirements modelling + RTM`
4. 群里 @ 吴宇轩 + @ 张梓健（需求 ID 逐字对齐）
