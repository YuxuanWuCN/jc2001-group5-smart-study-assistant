# Implementation Plan: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Branch**: `feature/cycle3-startup-report-plan` | **Spec**: [`spec.md`](spec.md)
**Input**: 用户批准的 Cycle 3 方案（A 报告重构 / B 9 份任务包 / C 组会问答库）+ 官方 Brief 硬约束
**Date**: 2026-10-18

---

## 1. Summary（一句话）

本周期不写代码，只产出**文字资产**：把软件基线里已经存在的事实，按官方 Brief 的七章结构组织成一份 40–60 页的英文技术报告蓝图，并把它切成 9 份组员可直接执行的任务包 + 1 份导师问答防身库 + 1 套 Speckit 规范留痕。

---

## 2. Technical Context（本周期「技术」= 文档与仓库事实）

| 项 | 值 |
| :--- | :--- |
| 语言/格式 | Markdown 交付（组员可自行转 DOCX/PDF）；报告正文英文（英式） |
| 主要依赖 | 无新增依赖；仅读写 `reports/`、`specs/`、`docs` 文本 |
| 代码改动 | **零**（NFR-3）；唯一可选项是修 `backend/app/models/auth.py:46` 的 Pydantic 弃用告警 |
| 事实来源（只读） | `backend/app/`（8 端点 / 5 router / 5 service / 5 model）、`tests/`（9 文件 / 78 函数 / 145 用例）、`backend/app/data/seed_questions.py`（932 行 / 12 题 / 36 陷阱）、`graphrag（终）/final_systematic_report.csv`（12 学科）、`reports/`（既有资产）、`JC2001-GroupProjectDescription-and-Requirements-2026-27.txt`（官方 Brief） |
| 目标交付 | `reports/cycle3_master_plan.md`、`reports/cycle3_task_packs/`（10 文件）、`reports/supervisor_qa_defense_library.md`、`specs/003-cycle3-startup-report/`（3 文件） |
| 版本控制 | 独立 worktree + 分支 `feature/cycle3-startup-report-plan`，PR → `develop` |

---

## 3. Constitution Check（`.specify/memory/constitution.md` v2.0.0）

| 原则 | 本周期是否符合 | 说明 |
| :--- | :-: | :--- |
| **I · 顶刊级学术与前沿视觉审美** | ✅ PASS | 任务包直接约束图表规范（Figure/Table 编号、caption 格式、自绘要求），并把"去 AI 感"落成十条可执行规矩 |
| **II · 原生极速加载零打包** | ✅ PASS | 不触碰 `frontend/`；任务包 03/05 把"零构建"写成报告论点（技术栈 Table 5.1、ADR-02），而非仅口号 |
| **III · 零破坏性兼容与测试门禁** | ✅ PASS | 不修改任何后端/测试文件；任务包 07 以 **145 用例**（非章程原文的 114）为准，并**明确纠正章程中的过期端点**（`/api/graph`、`/api/tutor` 已不存在，实际情况为 5 router / 8 端点）|
| **IV · 双模双主题 WCAG AA + 双语** | ✅ PASS | 任务包 03 §5.5.5 要求对照度验证与双语覆盖的诚实说明；任务包 02 将其登记为 R07/R08 与 NFR-U2 |
| **V · 文件系统与空间纪律** | ✅ PASS | 新文件全部落在 `reports/` 与 `specs/` 下；通过 worktree 操作避免污染既有脏工作树；不删除任何他人资产（仅删除自造的错前提目录 `specs/003-cycle3-reports-and-question-mgmt/`） |

> **章程偏差记录（需后续修正章程本身，不在本周期执行）**：章程第 III 条写的「114 个 pytest 测试」与端点清单 `/api/health, /api/quiz, /api/diagnose, /api/graph, /api/tutor` 已过期。实际为 **145 个用例**、5 router、8 端点，`/api/graph` 与 `/api/tutor` 不存在。本周期所有文档以仓库代码为准，章程修订留待下一周期。

---

## 4. Phase 结构（本周期已基本执行完毕）

### Phase 0 — 事实勘查（Research）
- 读官方 Brief，提取全部硬约束（章节顺序、页数、格式、评分点、PoC/视频要求）
- 核实仓库事实：端点数、测试数、题库规模、MMLU 数据、既有图表资产
- **产出**：事实清单（已内化进 plan 与任务包）
- **关键纠正**：三次结构性纠偏——（1）补 Ch3 Use Cases 独立章；（2）删去自拟的 Deployment / Viability 章，分别并入 Ch5.6 与 Ch7；（3）Appendix A 改为官方 Group Workload Profile 模板

### Phase 1 — 报告蓝图（D1）
- 七章 + 页数预算 + 责任人 + 前置页 + 附录 A–D
- 17 图 / 21 表编号表锁定
- 三周里程碑（Week A/B/C）+ G1/G2 门禁
- 「去 AI 感」十条硬规矩、交叉审校配对、风险登记表、提交前清单
- **产出**：`reports/cycle3_master_plan.md`

### Phase 2 — 9 份任务包 + 总索引（D2–D11）
- 每份七项固定内容（负责人/目标/逐节字数/素材路径/雷区/DoD/导师 3 问）
- 每份含两级截止与分支/PR 流程
- 总索引含分工表、分发话术、全组写作规范、冻结的 R01–R14 与图表编号
- **产出**：`reports/cycle3_task_packs/`（README + 01–09）

### Phase 3 — 组会问答防身库（D12）
- 六类追问（原定四类 + 实证数据 + 失败反思）
- 危险问题速查表、三条学术诚信红线
- **产出**：`reports/supervisor_qa_defense_library.md`

### Phase 4 — Speckit 留痕（D13）与 PR（D14）
- `spec.md` / `plan.md` / `tasks.md`
- 删除错前提目录 `specs/003-cycle3-reports-and-question-mgmt/`
- worktree 提 PR 到 `develop`

---

## 5. 关键设计决策（本周期自己的 ADR）

| ID | 决策 | 替代方案 | 理由 |
| :--- | :--- | :--- | :--- |
| PD-1 | **章节结构完全服从官方 Brief**，不做自拟定 | 保留原自拟 8 章（Deployment / Viability 独立成章） | 官方章节顺序固定、不得增删；自拟章会直接丢分。已因此把 Deployment 并入 Ch5.6、Viability 并入 Ch7 |
| PD-2 | **一人一章 + 任务包**，而非由组长独写 | 组长自己写 48 页 | 时间不足；且"知识集中在一人"正是导师质疑的来源；一人一章还能把"报告可被抽问"变成组织压力 |
| PD-3 | **任务包给出数字与素材路径**，而非要求组员自己调研 | 让组员自由发挥 | 组员没有项目上下文；给死素材能保证 40–60 页的产能，同时避免编造数据 |
| PD-4 | **报告论点建立在仓库真实现状上**（12 题 / 145 用例 / 7 正 3 平 2 负） | 写"宏大市场 + 全面覆盖"的初创叙事 | 规模与数据对不上会当场被问穿；"承认这是 feasibility prototype"反而更可信 |
| PD-5 | **worktree 提 PR**，不动主工作树 | 直接 checkout develop 提交 | 主工作树有 5 个他人脏文件与 untracked 资产，切换分支会冲突/误提交 |
| PD-6 | **删除错前提的 003 目录**，新建 `003-cycle3-startup-report` | 保留并在其中改写 | 旧目录名与内容前提（Reports = 软件看板）整体错误，保留会造成后续引用污染 |
| PD-7 | 用 `write`/`edit` 工具写中文 Markdown | 用 PowerShell `Get-Content`+`Set-Content` 批量替换 | 已实测 PowerShell 会把中文 Markdown 双重编码损坏（见 §7 风险 R1） |

---

## 6. 验收与验证方式

| 验收项 | 验证方法 |
| :--- | :--- |
| 七章对齐官方 Brief | 逐条比对 Brief 的章节列表与 master plan §2.2；缺章/多章即失败 |
| 页数预算 40–60 页 | 相加 master plan §2.2 各章区间（当前 48–59） |
| 图表编号唯一连续 | 检查 master plan §2.3 与 README §5.1 两张表一致，无重号 |
| 9 份任务包齐全 | `reports/cycle3_task_packs/` 下 01–09 各一份，README 索引链接全部可达 |
| 每份任务包七项齐全 | 逐份核对 §1–§7 结构 |
| 数字与仓库一致 | 抽查：145 用例（`pytest --collect-only`）、12 题 36 陷阱（`seed_questions.py`）、8 端点（`main.py`）、MMLU 12 学科（`final_systematic_report.csv`） |
| 无源码粘贴风险 | 任务包内明确禁止贴源码；报告正文由统稿人（谢炜昕）全文搜索 `def ` / `import ` |
| 零破坏 | `git status` 确认 `backend/`、`frontend/`、`tests/` 无新增改动 |
| PR 合规 | PR 只含 `reports/cycle3_master_plan.md`、`reports/cycle3_task_packs/**`、`reports/supervisor_qa_defense_library.md`、`specs/003-cycle3-startup-report/**` |

---

## 7. 风险登记表

| ID | 风险 | 概率 | 影响 | 缓解 |
| :-: | :--- | :-: | :--- | :--- |
| **R1** | 用 PowerShell 批量改中文文档导致编码损坏（**已发生过一次**） | 高（若重犯） | 中 | 一律使用 `write`/`edit` 工具；不对中文 Markdown 用 `Get-Content`+`Set-Content` |
| **R2** | 组员逾期不交，报告缺口 | 高 | 高 | G1 门禁：Week A 未交 outline 由 PM 回收代写，并在附录 A 记 `0%`；任务包把"打字 90 分钟"写成分母 |
| **R3** | 虚报贡献导致 Appendix A 拒签 | 中 | 高 | 如实申报；用"报告分工 + 随机抽问"抵消知识集中；不粉饰 |
| **R4** | 虚构调研数据被查 | 中 | **致命** | 三处（任务包 01/02、问答库 §7）明确写出"未做正式调研"的真实口径 |
| **R5** | MMLU 负值被写成"全部提升" | 中 | 高 | 5 处文档锁定「7 正 / 3 平 / 2 负」口径，并写明单次采样不显著 |
| **R6** | 报告违反"正文禁止贴源码" | 中 | 中 | 统稿人全文搜索；伪代码（≤20 行）与 JSON 允许 |
| **R7** | 页数超 60 页被截 | 中 | 中 | 各章页数预算已锁定；Week C 由统稿人裁决删减 |
| **R8** | Neo4j 明文凭证随交付 ZIP 泄露 | 中 | 高 | 提交前清单首条：移环境变量 + 重置 Aura 密码 + ZIP 全文搜索 `neo4j+ssc` / `password` |
| **R9** | 演示视频无人出镜 / 缺 Team Participation | 中 | 中（10% 权重） | 任务包 08 明确"10 人每人 ≥30 秒出镜"，并给出 15 分钟时间分配表 |

---

## 8. 交付物清单（文件级）

```
reports/
├── cycle3_master_plan.md                          # D1 周期总计划（七章蓝图/图表编号/里程碑/风险）
├── supervisor_qa_defense_library.md               # D12 组会问答防身库（六类追问）
└── cycle3_task_packs/
    ├── README.md                                  # D2 总索引 + 分发话术 + 写作规范 + R01–R14
    ├── 01-ch1-introduction-lin-yongtong.md        # D3  Ch1  5–6p
    ├── 02-ch2-requirements-moscow-zhang-zijian.md  # D4  Ch2  6–7p
    ├── 03-ch5-5-gui-xi-yusai.md                   # D5  Ch5.5 3–4p
    ├── 04-ch4-architecture-wang-sijian.md          # D6  Ch4  9–11p
    ├── 05-ch5-1-2-implementation-jiang-hao.md      # D7  Ch5.1–5.2 5–6p
    ├── 06-ch5-3-4-trap-diagnosis-dong-siqin.md     # D8  Ch5.3–5.4 5–6p
    ├── 07-ch6-testing-yang-mingjie.md              # D9  Ch6  7–8p
    ├── 08-ch5-6-deployment-liang-zixuan.md         # D10 Ch5.6 3–4p + 视频/PPT
    └── 09-ch3-use-cases-xie-weixin.md              # D11 Ch3  6–7p + 附录 B + 统稿
specs/003-cycle3-startup-report/
├── spec.md                                        # D13
├── plan.md                                        # D13（本文件）
└── tasks.md                                       # D13
```

---

## 9. 后续周期接口（不在本周期执行）

1. **章程修订**：把第 III 条的「114 测试 / 5 端点含 `/api/graph`、`/api/tutor`」更新为「145 用例 / 8 端点」，并补入 `StaticFiles` 单端口这一架构事实。
2. **技术债清理**：`backend/app/models/auth.py:46` 的 `Field(..., example=11)` → `json_schema_extra`。
3. **PoC 交付包**：User Manual（8–12 页 PDF）、演示 MP4（全员出镜）、PPTX。
4. **若时间允许**：`npm`-free 前端的一次可访问性（a11y）审计，把 WCAG AA 从"承诺"变成"实测报告"。
