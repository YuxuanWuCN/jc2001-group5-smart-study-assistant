# 实现计划：主仓库文件周期归属整理 + 根 README 周期任务看板

**分支**：`004-persona-hallucination-audit` | **日期**：2026-10-20 | **规格**：[spec.md](spec.md)
**输入**：用户原话（m00026）："把主仓库里面的文件整理一下哪一些是第一个周期做的哪一个是什么周期做的，然后把每一个周期就是现在周期要做的事放在主的 readme 里面可以吗"

## 概要

仓库已积累 Cycle 1 / Cycle 2 / Cycle 3 三个周期 + 一个进行中的审计周期（004）的资产，但根 `README.md` 仍停留在 Week 1–2 的旧结构（还在描述 `reports/project_proposal.pdf`、`scripts/verify_week1_deliverables.py` 这类早期文件），新成员无法判断**哪个文件属于哪个周期、当前周期该做什么**。

本计划交付的是**一份可核对的文档改进**，不新增功能代码：

1. 为仓库根下每个目录/关键文件标注所属周期（C1 / C2 / C3 / 004），依据是 git 提交日期 + 各周期规格包 + `reports/cycle3_master_plan.md` §1.1 资产盘点。
2. 把**当前周期（Cycle 3 报告周期 + 并行的 004 审计）的待办事项**写进根 `README.md`，作为全组唯一的任务入口。

## 技术背景

**语言/版本**：不涉及代码改动；文档为 Markdown，与仓库既有中文正文规范一致
**主要依赖项**：无新增依赖（章程原则"不引入新依赖"）
**存储**：不适用
**测试**：文档任务不改变代码，但提交前必须复跑 `python -m pytest tests/ -q` 守住 145 用例零回归（原则 III）
**目标平台**：GitHub 网页渲染（主仓库 `YuxuanWuCN/jc2001-group5-smart-study-assistant`）
**项目类型**：文档基线维护（Spec Kit 规范包 004）
**性能目标**：不适用
**约束条件**：根目录零污染（原则 V）；中文正文并禁用词清单（`reports/cycle3_master_plan.md` §3）；所有周期判定必须有仓库内可核验依据，不得凭记忆
**规模/范围**：1 个文件改写（`README.md`），1 个计划工件（本文件）

## 周期判定依据

| 周期 | 时间窗口（git 可核验） | 判定依据 |
| :--- | :--- | :--- |
| **Cycle 1**（概念与可行性） | 2026-09-23 起 | `d73e548 chore: initialize JC2001 Group 5 project repository with Week 1/2 baselines`；`practical1_deliverables.md`、Week 1 团队复盘包、`project_proposal.*` |
| **Cycle 2**（需求 / 建模 / PoC MVP） | 2026-10-08 ~ 2026-10-10，里程碑合并 2026-10-16 | `4b5c88c feat(poc): deliver end-to-end runnable MVP PoC`、`10d69d6 Merge develop into main: Phase 2 / Cycle 2 milestone`、`reports/phase2_cycle2_progress_report.md`、`specs/001-*`、`specs/002-*` |
| **Cycle 3**（Reports Cycle，软件基线冻结） | 2026-10-17 起（含 10-18 / 10-19 提交） | `acded7f docs(cycle3): startup-grade technical report blueprint + 9 task packs`、`reports/cycle3_master_plan.md`、`specs/003-cycle3-startup-report/` |
| **004 审计（与 C3 并行）** | 2026-10-18 起 | `specs/004-persona-hallucination-audit/`、`scripts/audit_*.py`、`reports/audit/` |
| **课程输入（非周期产物）** | — | 根目录 `*.pdf` / `*.txt` 教学材料、`JC2001-GroupProjectDescription-and-Requirements-2026-27.*` |

## 宪章检查

*关卡：必须在第 0 阶段研究前通过。在第 1 阶段设计后重新检查。*

| 原则 | 检查结论 |
| :--- | :--- |
| 原则 I 视觉审美 | 不涉及 UI，无冲突 |
| 原则 II 零构建 | 纯 Markdown，无新构建步骤 |
| 原则 III 零回归 | 不改代码；文档描述的数字必须与实测一致（`145 passed` 已复跑确认） |
| 原则 IV 双主题/双语 | 不涉及 |
| 原则 V 根目录零污染 | README 为既有根文件改写，不新增根目录文件 |

**门禁结论**：通过，无未正当化的违规。

## 项目结构

### 文档（此功能）

```text
specs/004-persona-hallucination-audit/
├── plan.md              # 本文件
├── spec.md              # 既有审计规格
├── tasks.md             # 既有任务清单
└── contracts/           # 既有契约
README.md                # 本次唯一改写目标（仓库根）
```

## 阶段 0：研究

**决策**：周期归属以 git 提交时间 + 里程碑合并提交为准，辅以各 `specs/0xx/spec.md` 的创建日期，不采用"最近修改时间"。
**理由**：`reports/` 目录曾在 2026-10-09 被删除重建（`84207d9 Delete reports directory`、`d6a32ba Add files via upload`），文件 mtime 不可靠；提交历史才是可核验事实。
**考虑的替代方案**：按目录名猜（如 `reports/final_report/` 一律算 C3）——被否决，因为 `reports/api_frontend_mapping/` 是 C2 产物却放在同一层。

**决策**：以"当前周期任务"而非"全部历史任务"作为 README 的核心内容。
**理由**：README 的主要读者是需要立刻动手的组员；历史任务已完成，保留会稀释注意力。
**考虑的替代方案**：逐周流水账——被否决。

## 阶段 1：设计与交付物

1. **`README.md` 结构**（替换现有 §📂 Repository Structure 与 §🚀 Quickstart 之间内容）：
   - 顶部加"周期地图"，一行说明当前处于哪个周期；
   - `## 📦 文件周期归属`：按 Cycle 1 / 2 / 3 / 004 / 课程输入 分组的表格，列出路径 + 内容 + 状态；
   - `## 🎯 当前周期（Cycle 3 报告周期）待办`：取自 `reports/cycle3_master_plan.md` §4 分工矩阵 + §5 两道门禁（G1/G2）+ §7 提交前清单；
   - `## 🔬 并行周期 004 审计待办`：取自 `specs/004-persona-hallucination-audit/tasks.md`；
   - 保留团队名册、Quickstart、Git 规范，并把 Git 规范改为"主仓库分支 + PR"流程（不再鼓励 fork）。
2. **契约/quickstart**：本次不新增 API 契约；`quickstart.md` 中"本地运行"步骤保持有效，无需改动。
3. **代理上下文更新**：运行 `update-agent-context.ps1 -AgentType claude` 已在仓库维护中，本次不改动 `CLAUDE.md` 手动段。

## 阶段 2：停止点

文档改写完成 + 145 用例复跑通过即结束；不进入任务拆解（task.md 已存在且属于 004 审计本身）。
