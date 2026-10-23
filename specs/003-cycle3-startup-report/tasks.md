# Tasks: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Feature**: [`spec.md`](spec.md) · **Plan**: [`plan.md`](plan.md)
**Branch**: `feature/cycle3-startup-report-plan`
**Legend**: `[P]` 可并行 · `[US-1..4]` 对应用户故事 · ✅ 已完成 · ⏳ 待执行

> **本周期无代码任务。** 所有任务都是文本产出，因此依赖关系只看「素材是否已核实」与「编号是否已冻结」，不看编译/部署。

---

## Phase 1 — 事实勘查（阻塞全部后续任务）

| ID | 任务 | 产出物 | 状态 |
| :--- | :--- | :--- | :-: |
| T0.1 | 读官方 Brief，提取章节顺序 / 40–60 页 / 格式 / 评分点 / PoC / 视频硬约束 | 内化为 plan §2 与 master plan §0.1 | ✅ |
| T0.2 | 核实后端事实：8 端点、5 router、5 service、5 model、`StaticFiles` 单端口挂载 | 事实清单 | ✅ |
| T0.3 | 核实测试事实：9 文件 / 78 函数 / 145 用例 / 3.6 秒 | 事实清单 | ✅ |
| T0.4 | 核实题库事实：932 行 / 12 题 / 4 学科 / 36 陷阱 / 5 雷达维度 | 事实清单 | ✅ |
| T0.5 | 核实 MMLU 实证：12 学科 Base→Ours，**7 正 / 3 平 / 2 负** | `graphrag（终）/final_systematic_report.csv` | ✅ |
| T0.6 | 核实既有图表资产可用性与尺寸（三张 UML 图 PNG 分辨率） | 事实清单 | ✅ |
| T0.7 | 发现安全项：`graphrag（终）/real_graph_engine.py` 明文 Neo4j 凭证且已被 git 跟踪 | 风险登记表 R8 + 提交前清单首条 | ✅ |

**门禁 G0**：T0.1–T0.7 全部完成前，不得开始写作任何章节。**（已通过）**

---

## Phase 2 — 报告蓝图（US-1）

| ID | 任务 | 产出物 | 依赖 | 状态 |
| :--- | :--- | :--- | :--- | :-: |
| T1.1 | 七章结构对齐官方 Brief（**含三次纠偏：补 Ch3 / 拆 Deployment→Ch5.6、Viability→Ch7 / Appendix A 改官方模板**） | master plan §2.2 | G0 | ✅ |
| T1.2 | 页数预算：各章区间相加落在 40–60 页（当前 48–59） | master plan §2.2 | T1.1 | ✅ |
| T1.3 | 17 图 + 21 表编号锁定并写入蓝图 | master plan §2.3 | T1.1 | ✅ |
| T1.4 | 各章硬性写作要素（官方六项必含、五类 NFR、逐条需求评估） | master plan §2.4 | T1.1 | ✅ |
| T1.5 | 「去 AI 感」十条硬规矩 | master plan §3 | T1.1 | ✅ |
| T1.6 | 分工矩阵 + 交叉审校配对 | master plan §4 | T1.2 | ✅ |
| T1.7 | 三周里程碑（Week A/B/C）+ G1/G2 门禁 | master plan §5 | T1.2 | ✅ |
| T1.8 | 风险登记表 + 提交前必做清单 | master plan §7 | T1.3 | ✅ |
| T1.9 | 交叉核对 master plan §2.3 与 task_packs README §5.1 的图表编号表一致 | — | T1.3 | ✅ |

---

## Phase 3 — 9 份任务包（US-2）

每份任务包的固定结构（AC-2.2）：负责人与页数 / 一句话目标 / 逐节字数 / 素材路径表 / 雷区 / DoD / 导师 3 问。

| ID | 任务包 | 负责人 | 章节 | 页数 | 状态 |
| :--- | :--- | :--- | :--- | :--- | :-: |
| T2.1 | `01-ch1-introduction-lin-yongtong.md` | 林泳桐 50106038 | Ch1 Introduction and Project Context | 5–6p | ✅ |
| T2.2 | `02-ch2-requirements-moscow-zhang-zijian.md` | 张梓健 50106035 | Ch2 Functional & Non-Functional Requirements | 6–7p | ✅ |
| T2.3 | `09-ch3-use-cases-xie-weixin.md` | 谢炜昕 50106034 | Ch3 Use Cases and Requirements Modelling + 附录 B + 统稿 | 6–7p | ✅ |
| T2.4 | `04-ch4-architecture-wang-sijian.md` | 王思鉴 50106045 | Ch4 System Design and Architecture | 9–11p | ✅ |
| T2.5 | `05-ch5-1-2-implementation-jiang-hao.md` | 江昊 50106065 | Ch5.1–5.2 Implementation: stack + API contracts + 附录 D | 5–6p | ✅ |
| T2.6 | `06-ch5-3-4-trap-diagnosis-dong-siqin.md` | 董思钦 50106060 | Ch5.3–5.4 题库陷阱工程 + 诊断算法 | 5–6p | ✅ |
| T2.7 | `03-ch5-5-gui-xi-yusai.md` | 习羽赛 50105989 | Ch5.5 GUI | 3–4p | ✅ |
| T2.8 | `08-ch5-6-deployment-liang-zixuan.md` | 梁子铉 50106037 | Ch5.6 部署与可复现性 + 视频/PPT | 3–4p | ✅ |
| T2.9 | `07-ch6-testing-yang-mingjie.md` | 杨明杰 50106061 | Ch6 Testing and Evaluation + 附录 C + User Manual | 7–8p | ✅ |
| T2.10 | `README.md` 总索引（分工表 / 分发话术 / 写作规范 / R01–R14 冻结 / 图表编号） | 吴宇轩 50106070 | 全篇 | — | ✅ |
| T2.11 | 删除旧编号的 3 份任务包（Ch2.4 UX / Ch3 架构 / Ch4 API 的早期版本） | 吴宇轩 | — | — | ✅ |

**门禁 G1**（Week A 周日 23:59）：每人提交 outline；**逾期由 PM 回收代写，并在附录 A 记 `0%`**。

---

## Phase 4 — 组会问答防身库（US-3）

| ID | 任务 | 内容 | 状态 |
| :--- | :--- | :--- | :-: |
| T3.1 | §0 三句定场话（定义 / 差异 / 边界） | 30 秒可背 | ✅ |
| T3.2 | §1 为什么这么复杂、像 AI 系统 | 复杂度在数据建模 + 不隐瞒 AI 辅助 | ✅ |
| T3.3 | §2 对比 Quizlet / ChatGPT | 三处结构性差异 + 文献依据 + 诚实定位 | ✅ |
| T3.4 | §3 十人如何协同、你做了多少 | 如实申报「代码一人写」 | ✅ |
| T3.5 | §4 断网 / 欠费 / 缓存 / 数据丢失 | 含主动承认凭证泄露与处置 | ✅ |
| T3.6 | §5 实证数据与 145 测试的意义 + What failed | 含 MMLU 负值的正确说法 | ✅ |
| T3.7 | §6 十行危险问题速查表 | 一问一答一句话 | ✅ |
| T3.8 | §7 学术诚信三条红线 | 不虚构调研 / 不虚报数据 / 不虚报分工 | ✅ |

---

## Phase 5 — Speckit 留痕与 PR（US-4）

| ID | 任务 | 产出物 | 依赖 | 状态 |
| :--- | :--- | :--- | :--- | :-: |
| T4.1 | 写 `spec.md`（US-1..4 / AC / D1–D14 / NFR / NG / DoD） | `specs/003-cycle3-startup-report/spec.md` | Phase 2–4 | ✅ |
| T4.2 | 写 `plan.md`（Constitution Check + Phase + PD-1..7 + 风险 + 验收） | `specs/003-cycle3-startup-report/plan.md` | T4.1 | ✅ |
| T4.3 | 写 `tasks.md`（本文件） | `specs/003-cycle3-startup-report/tasks.md` | T4.2 | ✅ |
| T4.4 | 删除错前提目录 `specs/003-cycle3-reports-and-question-mgmt/`（7 文件） | — | — | ✅ |
| T4.5 | 用 `git worktree add -b feature/cycle3-startup-report-plan D:\jc2001-cycle3-pr develop` 隔离提交 | 干净工作树 | — | ⏳ |
| T4.6 | 只把 13 个新文件复制进 worktree 并 commit（**不含 5 个他人脏文件**） | commit | T4.5 | ⏳ |
| T4.7 | `git push -u origin feature/cycle3-startup-report-plan` | 远端分支 | T4.6 | ⏳ |
| T4.8 | `gh pr create --base develop` 并附变更说明 | PR 链接 | T4.7 | ⏳ |
| T4.9 | `git worktree remove D:\jc2001-cycle3-pr`，主工作树保持原样 | 清理 | T4.8 | ⏳ |

**PR 必须只包含这 15 个新文件**：
`reports/cycle3_master_plan.md`、`reports/supervisor_qa_defense_library.md`、`reports/cycle3_task_packs/`（README + 01–09 共 10 个）、`specs/003-cycle3-startup-report/`（spec/plan/tasks 共 3 个）。

**不得出现在 PR 中的文件**：
`backend/app/data/seed_questions.py`、`frontend/app.js`、`frontend/index.html`、`graphrag（终）/auto_builder.py`、`graphrag（终）/real_graph_engine.py`。

---

## Phase 6 — 分发（PR 之后，非代码任务）

| ID | 任务 | 验收 |
| :--- | :--- | :--- |
| T5.1 | 在群里发 README §4 的分发话术 + 各自任务包链接 | 9 人确认收到 |
| T5.2 | 公告需求编号冻结（R01–R14）并 @谢炜昕 @杨明杰 | 两人回复确认 |
| T5.3 | 公告图表编号冻结（17 图 21 表） | 全组无异议 |
| T5.4 | 排 Week A 组会（G1 门禁） | 已定时间 |
| T5.5 | 组长自测：不看稿讲完三句定场话 + 任意三类追问 | 通过 |

---

## 依赖关系图

```
G0 事实勘查
   └─> T1.x 蓝图 ──> T2.x 九任务包 ──> T5.x 分发
            │              │
            └──────> T3.x 问答库
                           │
                     T4.1 spec ─> T4.2 plan ─> T4.3 tasks
                                                  │
                                          T4.5 worktree ─> T4.6 commit
                                                  └─> T4.7 push ─> T4.8 PR ─> T4.9 清理
```

---

## 剩余工作（本文件写完后）

- [x] T1.9 图表编号两表交叉核对（master plan §2.3 与 README §5.1 已统一为 **17 图 / 21 表**，Persona 归 Table 1.3、需求来源归 Table 2.1、NFR 达标评估归 Table 6.5）
- [x] T4.5 worktree 从 `origin/develop` 创建并隔离提交
- [x] T4.6 仅提交 15 份文档（commit `6112954`）
- [x] T4.7 推送 `feature/cycle3-startup-report-plan`
- [x] T4.8 创建 PR #5：<https://github.com/YuxuanWuCN/jc2001-group5-smart-study-assistant/pull/5>
- [x] T4.9 已核验 PR 仅含 15 份文档；临时 worktree 待清理
- [ ] T5.1–T5.5 分发与组长自测（PR 合并后执行）
