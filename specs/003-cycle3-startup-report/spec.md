# Feature Specification: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Feature Branch**: `feature/cycle3-startup-report-plan`
**Created**: 2026-10-18
**Status**: Ready for planning
**Input**: 用户（组长 吴宇轩）在明确项目现状后批准的第三周期方案：把 50% 权重的期末 Technical Report 从「0 页」推进到「可提交的初创级技术与落地报告」，并把它拆成 9 份可执行的组员任务包 + 一套组会问答防身库。

> **本周期不做新功能。** 软件基线已冻结（8 个 API 端点、145 个测试用例、12 题 36 陷阱、3 张 UML 图）。本周期唯一交付物是**文字**：一份 40–60 页的英文技术报告、9 份组员任务包、1 份导师问答库。

---

## 1. 背景与问题陈述

导师（Dr. Shahzad Mumtaz）对现有交付物给出的判断是：**系统太先进，不像初创项目，像 AI agent 做的 agent 系统**；并明确要求**把项目的报告打造成一家初创公司的报告**。

三个可验证的现状约束：

| # | 约束 | 证据 |
| :-: | :--- | :--- |
| C1 | Technical Report 占组内权重 **50%**（= 课程总分 25%），当前实际进度 **0 页** | 官方 Brief；`reports/` 下无 final report 目录 |
| C2 | 代码与系统知识**集中在组长一人**，其余 9 人未参与写作 | 用户亲述（m00107） |
| C3 | 组长最怕的场景是**组会回答不上导师的问题** | 用户亲述（m00107） |

由此推出三个必须同时解决的问题：**（P1）报告写不出来；（P2）组员无法贡献；（P3）组会无法自证。**

---

## 2. 用户场景与验收标准

### US-1 · 报告主笔（组长视角）P1

> 作为组长，我需要一份**章节结构、页数预算、图表编号、责任人都已锁定**的报告蓝图，这样我不必在写作过程中反复做结构决策。

**验收标准**：
- **AC-1.1** 报告章节**严格对齐官方 Brief 的七章顺序**，一章不多、一章不少：① Introduction and Project Context ② Functional and Non-Functional Requirements ③ Use Cases and Requirements Modelling ④ System Design and Architecture ⑤ Implementation ⑥ Testing and Evaluation ⑦ Conclusions and Future Work → References → Appendix A Group Workload Profile。
- **AC-1.2** 每章有**页数预算**，正文合计落在 **40–60 页**（不含前置页/参考文献/附录）。
- **AC-1.3** 全篇图表编号**唯一且连续**（17 图 / 21 表），编号表随蓝图一并产出，后续不允许临时加号。
- **AC-1.4** 蓝图明确写出**官方六项必含内容**在第 1 章的位置：problem / background / objectives / intended users or stakeholders / main features / potential practical or business value。
- **AC-1.5** 蓝图明确写出**官方五类 NFR** 在第 2 章的位置：usability / performance / reliability / security / maintainability。
- **AC-1.6** 蓝图明确写出第 6 章必须含**「逐条对照第 2 章需求」的评估小节**（官方指定动作）。

### US-2 · 组员任务包（组员视角）P2

> 作为组员，我需要一份**傻瓜式到不需要问人**的任务包：我知道我负责哪几页、每小节写什么、素材在仓库哪个文件、什么写法会被退回、老师可能问我什么。

**验收标准**：
- **AC-2.1** 9 位组员**每人一份**任务包，文件命名含章节号与姓名，存放在 `reports/cycle3_task_packs/`。
- **AC-2.2** 每份任务包必须含七项固定内容：① 负责人与页数预算 ② 一句话交付目标 ③ 逐节结构与字数 ④ 素材路径表（可点击的仓库相对路径） ⑤ 会被退回的雷区清单 ⑥ 验收清单（DoD） ⑦ 导师 3 问 + 30 秒答法。
- **AC-2.3** 每份任务包含**两级截止**：outline（Week A 周日 23:59）与 draft（Week B 周日 23:59）。
- **AC-2.4** 任务包内的所有数字（端点/测试/题库/MMLU）必须与仓库现状一致，**不得出现凭记忆编造的数**。
- **AC-2.5** 存在一份总索引 `README.md`，含分工表、两步交付节奏、微信群分发话术、全组写作规范、冻结的需求编号 R01–R14 与图表编号。
- **AC-2.6** 任务包必须**禁止编造数据**并明确写出替代口径（见 §4 约束 NFR-4）。

### US-3 · 组会问答防身库 P3

> 作为组长，我需要针对导师高频追问的标准答法，让我在组会上能 30 秒内给出有依据、有边界、承认弱点的回答。

**验收标准**：
- **AC-3.1** 覆盖原定四类追问：① 为什么这么复杂 / 像 AI 系统 ② 解决了 Quizlet 与 ChatGPT 解决不了什么问题 ③ 10 人如何协同、你做了多少 ④ 断网 / 欠费 / 数据丢失会怎样。
- **AC-3.2** 另覆盖两类高频追问：⑤ 实证数据（MMLU / 145 测试的意义）⑥ 失败与反思（what failed / would do differently）。
- **AC-3.3** 每条答案 ≤60 秒可讲完，且**至少引用一个可追溯的仓库文件或数字**。
- **AC-3.4** 含**危险问题速查表**（一问一答的一句话版本）。
- **AC-3.5** 含**学术诚信三条红线**：不虚构用户调研、不虚报实验数据、不虚报分工。

### US-4 · Speckit 规范留痕（项目治理视角）

**验收标准**：
- **AC-4.1** 本周期在 `specs/003-cycle3-startup-report/` 下有 `spec.md` / `plan.md` / `tasks.md` 三件套。
- **AC-4.2** 前期因误判「Reports = 软件内学情看板」而产生的 `specs/003-cycle3-reports-and-question-mgmt/` **已删除**，不进入版本库。
- **AC-4.3** 本周期变更以**独立分支 + PR** 进入 `develop`，不改动既有脏工作树。

---

## 3. 功能需求（本周期交付物清单）

| ID | 交付物 | 落点 | 状态 |
| :--- | :--- | :--- | :--- |
| D1 | 周期总计划（含章节蓝图、页数预算、图表编号、分工矩阵、里程碑、风险登记） | `reports/cycle3_master_plan.md` | ✅ |
| D2 | 任务包总索引 | `reports/cycle3_task_packs/README.md` | ✅ |
| D3 | 任务包 01 · 林泳桐 · Ch1 | `reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md` | ✅ |
| D4 | 任务包 02 · 张梓健 · Ch2 | `reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md` | ✅ |
| D5 | 任务包 03 · 习羽赛 · Ch5.5 | `reports/cycle3_task_packs/03-ch5-5-gui-xi-yusai.md` | ✅ |
| D6 | 任务包 04 · 王思鉴 · Ch4 | `reports/cycle3_task_packs/04-ch4-architecture-wang-sijian.md` | ✅ |
| D7 | 任务包 05 · 江昊 · Ch5.1–5.2 + 附录 D | `reports/cycle3_task_packs/05-ch5-1-2-implementation-jiang-hao.md` | ✅ |
| D8 | 任务包 06 · 董思钦 · Ch5.3–5.4 | `reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md` | ✅ |
| D9 | 任务包 07 · 杨明杰 · Ch6 + 附录 C + User Manual | `reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md` | ✅ |
| D10 | 任务包 08 · 梁子铉 · Ch5.6 + 视频/PPT | `reports/cycle3_task_packs/08-ch5-6-deployment-liang-zixuan.md` | ✅ |
| D11 | 任务包 09 · 谢炜昕 · Ch3 + 附录 B + 统稿 | `reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md` | ✅ |
| D12 | 组会问答防身库 | `reports/supervisor_qa_defense_library.md` | ✅ |
| D13 | Speckit 三件套 | `specs/003-cycle3-startup-report/{spec,plan,tasks}.md` | ✅ |
| D14 | PR 合入 `develop` | GitHub PR | ⏳ |

---

## 4. 非功能需求与约束

| ID | 类别 | 要求 |
| :--- | :--- | :--- |
| NFR-1 | 可验证性 | 任何一个报告中出现的数字，必须能在仓库中定位到来源文件（题库/测试/CSV/代码）。**写不出出处的数字必须删除。** |
| NFR-2 | 官方合规 | 交付物必须同时满足 Brief 的格式要求（A4 / 2.54 cm / 单栏 / 12 pt / Times New Roman / 1.5 倍行距 / 单 PDF / Turnitin）与「正文禁止贴源码」。 |
| NFR-3 | 零破坏 | 本周期**不修改** `backend/`、`frontend/`、`tests/` 任何文件；不动既有脏工作树（`seed_questions.py`、`app.js`、`index.html`、`graphrag（终）/*.py`）。 |
| NFR-4 | 学术诚信 | **禁止**虚构用户调研（不得出现未做的问卷样本量）、禁止虚报 MMLU 结果（必须报告 7 正 / 3 平 / 2 负）、禁止虚报分工（附录 A 需全员签署）。 |
| NFR-5 | 可执行性 | 任务包必须让组员**无需额外提问**即可开工：素材路径可直接打开，字数与页数有明确区间，退稿标准可自查。 |
| NFR-6 | 术语一致 | 全组共用同一套编号体系：R01–R14（需求）、UC-01–UC-06（用例）、AD-1–AD-7（架构决策）、Figure 1.1–7.1、Table 1.1–7.1。 |
| NFR-7 | 安全 | 交付 ZIP 与版本库中不得含明文凭证；已知泄露项（Neo4j 凭证）必须在提交前完成轮换并被记入提交前清单。 |
| NFR-8 | 语言 | 报告正文**英文**（英式拼写）；任务包与问答库**中文**（面向组员与组长）。 |

---

## 5. 明确不做的事（Non-Goals）

| # | 不做 | 理由 |
| :-: | :--- | :--- |
| NG-1 | 不新增任何 API 端点或前端功能 | 软件基线已冻结；新增功能会破坏 145 用例的稳定性，且不服务 50% 的报告权重 |
| NG-2 | 不重构代码、不做性能优化 | 本周期无工程收益；唯一允许的代码改动是修 `backend/app/models/auth.py:46` 的 `Field(..., example=)` 弃用告警（可选，属技术债清理） |
| NG-3 | 不做「学情遥测看板」类新功能 | 这是前期的错误前提，已推翻。Reports 指期末技术报告。 |
| NG-4 | 不接入 Neo4j 到在线演示链路 | 云端实例会休眠、考场断网即 500；保持 ADR-05 的离线评估定位 |
| NG-5 | 不承诺商业可行性 | 12 题、10 周、零预算，定位是 feasibility prototype；商业化只作为 Ch7 的 future work 写明路径 |
| NG-6 | 不在本周期内完成 PoC User Manual 与演示视频 | 属于交付包的一部分，但由杨明杰 / 梁子铉在报告主线完成后再做（任务包中已含大纲与时间分配） |

---

## 6. 成功判定（Definition of Done）

本周期视为完成，当且仅当：

1. 上述 D1–D14 全部落地，且 PR 已合入 `develop`；
2. 9 份任务包已**实际分发**给 9 位组员（群公告 + 各自确认收到）；
3. 组长能**不看稿**讲完第 0 节三句定场话 + 任意三类追问的标准答法；
4. 全篇章节结构与官方 Brief 的七章**逐条对齐**，且 17 图 / 21 表编号表已锁定并公布；
5. 报告中不出现任何一个**无法追溯出处**的数字。
