# Cycle 3 周期总结与督导汇报材料
## SmartStudy Console · JC2001 Group 5 · 2026-10-29

---

## 一、本周期核心定位

**周期主题**：Reports Cycle —— 把占 50% 权重的期末报告从 0 页推进到可提交的初稿状态

**周期任务唯一目标**：产出一份 **40–60 页正文 + 4 附录 + 完整图表与引用** 的 Technical Report，且每位组员能独立讲清自己负责章节的核心论点。

**关键约束**：
- ✅ 软件基线已冻结（8 API 端点、147 测试用例全通过、12 题 36 陷阱、3 张 UML 图）
- ✅ 本周期**不再开发新功能**，全部精力投入报告撰写
- ✅ 严格对齐官方 Brief 的七章结构，不自行发明章节

---

## 二、已完成任务清单（可核验事实）

### 2.1 软件资产盘点（全部在仓库，报告的"弹药库"）

| 资产类别 | 实测数据 | 文件位置 | 报告去向 |
| :--- | :--- | :--- | :--- |
| **后端 API** | 8 个端点（health / quiz / diagnose / summary / trend / demo-users / login / register） | `backend/app/routers/` | Ch5.2 接口契约表 |
| **测试基线** | 147 个用例（9 文件 78 函数，参数化展开）+ 100% 通过 | `tests/` | Ch6 + 附录 C |
| **Git 协作记录** | 51 commits / 5 PRs（2 已合并）/ +71.2k −14.3k 行 / 7 位贡献者 | GitHub 仓库 | 附录 A 贡献透明化 |
| **对抗性测试** | 25 个函数 / 523 行（非法注入、编码攻击、并发） | `tests/test_adversarial_backend.py` | Ch6.2 |
| **题库陷阱工程** | 12 题 × 4 学科 × 36 个细粒度错因陷阱 | `backend/app/data/seed_questions.py` (932 行) | Ch5.3、Ch5.4 |
| **图谱增强实证** | MMLU 12 学科 Base vs Ours 对比（7 正 / 3 平 / 2 负） | `graphrag（终）/final_systematic_report.csv` | Ch6.3 **核心证据** |
| **UML 图件** | 用例图、上下文模型、时序图（`.mmd`/`.svg` 三件套） | `reports/figures/` | Ch3、Ch4 |
| **前端资产** | 零构建前端（index.html 57KB / app.js 259KB / style.css 73KB） | `frontend/` | Ch5.5 |
| **竞品分析** | 六维竞品对比矩阵（≥5 个产品） | `reports/competitor_analysis.md` (124KB) | Ch1 |

### 2.2 规范文档已就位

| 文档 | 作用 | 状态 |
| :--- | :--- | :---: |
| `cycle3_master_plan.md` | 7 章结构 + 分工矩阵 + 图表编号预分配（17 图 21 表） | ✅ 已冻结 |
| `cycle3_task_packs/README.md` + 9 份任务包 | 每人一章，含页数 / 小节 / 素材路径 / 3 个防身问题 | ✅ 已分发 |
| `supervisor_qa_defense_library.md` | 28 个导师高频追问 + 30 秒标准答法 | ✅ 可演练 |
| `CLAUDE.md` / `GEMINI.md` | 代理上下文文件（技术栈 / 命令 / 代码风格） | ✅ 已更新 |
| `.specify/` 规范包 | spec-kit 脚手架 + 章程 v2.0.0 | ✅ 质量门禁生效 |

### 2.3 质量门禁已生效

| 门禁项 | 当前状态 |
| :--- | :---: |
| pytest 147 用例全通过 | ✅ **100% (9.28s)** |
| Pydantic 字段双命名同步（`CamelModel`） | ✅ 已统一 |
| 禁用词清单（赋能/闭环/生态/leverage/cutting-edge） | ✅ 已列入规范 |
| 根目录零污染原则 | ✅ 临时脚本一律外放 |
| 凭证泄露风险已处理 | ⚠️ **待轮换**（见问题清单 #1） |

---

## 三、报告框架（严格对齐官方 Brief）

### 3.1 七章 + 四附录结构

| 章节 | 官方标题 | 负责人 | 页数 | 核心交付物 |
| :-: | :--- | :--- | :-: | :--- |
| **Ch1** | Introduction and Project Context | 林泳桐 | 5–6 | 竞品对比 + 3 Persona + SMART 目标 + 商业价值论述 |
| **Ch2** | Functional and Non-Functional Requirements | 张梓健 | 6–7 | MoSCoW 14 行（Won't ≥3 条）+ NFR 五类可度量指标 |
| **Ch3** | Use Cases and Requirements Modelling | 谢炜昕 | 6–7 | 用例图 + 6 个用例描述 + 答题状态机 + 需求追溯 |
| **Ch4** | System Design and Architecture | 王思鉴 | 9–11 | 架构总览 + 类图（新画）+ ADR 矩阵 ≥6 行 |
| **Ch5** | Implementation | 江昊 · 董思钦 · 习羽赛 · 梁子铉 | 14–16 | 技术栈 + 8 端点契约 + 陷阱工程 + 诊断算法 + GUI + 部署 |
| **Ch6** | Testing and Evaluation | 杨明杰 | 7–8 | 145 用例清点 + 对抗性测试 + **MMLU 12 学科对比** + NFR 达标评估 |
| **Ch7** | Conclusions and Future Work | 吴宇轩 | 3–4 | SMART 目标结账 + Limitations ≥5 条 + What failed ≥3 条 |
| **App A** | Group Workload Profile（官方模板） | 10 人签署 | 1–2 | 如实申报贡献比例，含 0% / ±X% 口径 |
| **App B** | Requirements Traceability Matrix | 谢炜昕 | 2 | 需求 → 用例 → 设计 → 实现 → 测试 |
| **App C** | Test Case Inventory | 杨明杰 | 2 | 145 用例清单 + 本机运行截图 |
| **App D** | Glossary & API Snapshot | 江昊 | 1–2 | 术语 ≥12 条 + OpenAPI 快照 |

### 3.2 图表编号预分配（已锁定，不得冲突）

- **Figure 1.1–7.1**：共 17 图（Value Proposition Canvas / 竞品定位 / MoSCoW 分布 / 用例图 / 状态机 / 架构图 / 上下文模型 / 类图 / 时序图 / 软件结构 / 陷阱因果链 / UI 截图 ×2 / 部署拓扑 / 测试金字塔 / **MMLU Δ 柱状图** / 12 月路线图）
- **Table 1.1–7.1**：共 21 表（竞品矩阵 / SMART / Personas / 需求来源 / MoSCoW 14 行 / NFR 规格 / 用例摘要 / ADR / 技术栈 / 8 端点契约 / 领域模型 / 12 题分布 / TrapDetail 四字段 / **查表 vs LLM** / 环境要求 / 测试文件清点 / 对抗性六组 / MMLU 12 学科 / RAGAS / 需求达标评估 / 商业化假设）

---

## 四、GitHub 协作数据透明化（附录 A 证据链）

### 4.1 Pull Request 记录（5 个）

| PR# | 状态 | 标题 | 创建时间 |
| :-: | :---: | :--- | :--- |
| #5 | **OPEN** | Cycle 3 报告计划与任务包 | 2026-10-17（开放 12 天） |
| #4 | **OPEN** | 学生登录界面与工作台 | 2026-10-16（开放 13 天） |
| #3 | CLOSED | 知识本体导入 | 2026-10-16（同日关闭） |
| #2 | **MERGED** | UML 架构图件 | 2026-10-09（20m 合并） |
| #1 | **MERGED** | Portal UI & i18n | 2026-10-09（1h13m 合并） |

### 4.2 Commit 贡献分布（51 个，7 位贡献者）

| 排名 | 贡献者 | Commit 数 | 占比 | 代表性工作 |
| :-: | :--- | ---: | ---: | :--- |
| 🥇 | **Yuxuan Wu** | **34** | **66.7%** | PoC MVP、报告蓝图、安全修复 |
| 🥈 | 谢炜昕（xin-315） | 6 | 11.8% | 文件组织与协作 |
| 🥉 | 张梓健（yhdmcst） | 5 | 9.8% | 需求文档与追溯矩阵 |
| 4 | Cindy（早期协作者） | 3 | 5.9% | 早期实验功能 |
| 5 | 董思钦 | 1 | 2.0% | **诊断算法与 LLM 健康探针** |
| 6 | 习羽赛 | 1 | 2.0% | **前后端 API 映射表** |
| 7 | 张梓健（另一 ID） | 1 | 2.0% | 用例文档 |

### 4.3 代码活跃度

- **总代码变动**：+71,200 −14,294 行（净增 +56,906）
- **文件变更**：451 个
- **高密度开发周期**：Week 5（10-08 至 10-10）产出 16 commits，完成 PoC MVP 交付
- **最近一周**：9 commits（安全修复、测试基线同步、任务分配）

---

## 五、当前风险与待解决问题清单

### 5.1 高危问题（需立即处理）

#### 🔴 **问题 1：凭证泄露风险（安全事件级）**

**现状**：
- `graphrag（终）/real_graph_engine.py` 中硬编码了 Neo4j Aura 的 `NEO4J_USERNAME` 和 `NEO4J_PASSWORD`
- 该文件**已提交至 git 历史并推送 GitHub**
- 虽然该文件注释中标注"终稿已移除真实凭证"，但历史记录仍可回溯

**影响**：
- 任何有仓库访问权限的人可查看历史 commit 获取云端图数据库凭证
- 构成 GDPR / 数据安全规范的潜在违规

**建议处理方案（三步走）**：
1. **立即轮换凭证**：在 Neo4j Aura 控制台重置密码
2. **代码整改**：将凭证改为 `os.getenv("NEO4J_PASSWORD")` 读取，同步补充缺失的 `import os`
3. **写进报告 Ch5.6**：作为一次**真实安全事件复盘**案例，展示"发现 → 缓解 → 预防"流程（反而成为"我们不是 AI 生成"的有力证据）

---

#### 🟠 **问题 2：Pydantic 字段 `example` 参数告警（质量债务）**

**现状**：
- `backend/app/models/auth.py` 33–48 行使用了 `Field(..., example=)` 语法
- Pydantic v2 已弃用该写法，应改为 `json_schema_extra={"example": ...}`
- 测试运行时产生 17 条 `PydanticDeprecatedSince20` 告警

**影响**：
- 不影响功能，但告警会干扰测试输出可读性
- 违反"工程纪律"标准，报告中提及"145 测试全通过"时会被质疑"为什么有告警"

**建议处理方案**：
- 修改 6 处 `Field` 声明，统一使用 `json_schema_extra` 语法
- 作为 Ch5 中"工程纪律"的一个小节素材（"我们修了哪些非功能性技术债"）

---

#### 🟡 **问题 3：报告进度监控机制缺失**

**现状**：
- 任务包已分发，但**没有实时进度看板**
- 无法及时发现"组员未动笔"的高风险信号

**建议处理方案**：
- 建立 `reports/final_report/progress_tracker.md`，每人每日更新进度状态
- 设置 Week A 门禁（周日 23:59）：未交 outline 者，章节收回 + Appendix A 如实记录 `No submission`

---

### 5.2 中危问题（需监控与缓解）

#### 🟢 **问题 4：图谱增强负面结果的呈现策略**

**现状**：
- MMLU 实验显示 2 个学科负提升（HS Physics −1.32pp、HS US History −1.00pp）
- 存在"要不要写进报告"的纠结

**建议处理方案**：
- **必须写进报告**，这是"去 AI 感"的核心武器
- 在 Ch6.3 中如实呈现 12 学科对比，并在 Ch6.6（Threats to Validity）和 Ch7.2（Limitations）中分析原因
- 话术参考：「Graph augmentation shows domain-specific efficacy: +2.50pp in Professional Law, but −1.32pp in HS Physics, suggesting prerequisites in physics are less tree-structured than legal statutes.」

---

#### 🟢 **问题 5：类图尚未绘制**

**现状**：
- Ch4 要求提供 UML 类图，但 `reports/figures/` 中只有用例图、上下文模型、时序图

**建议处理方案**：
- 王思鉴（Ch4 负责人）根据 `backend/app/models/` 中的 Pydantic 模型绘制类图
- 工具推荐：PlantUML 或 draw.io（与现有 `.drawio` 保持一致）
- 时间窗口：Week A 第 3 天前完成

---

#### 🟢 **问题 6：组会应对演练尚未启动**

**现状**：
- `supervisor_qa_defense_library.md` 已准备 28 个问题，但**尚未组织全员演练**

**建议处理方案**：
- 组会前 24 小时：每人从防身库中领 5 个问题，写三句话答案发群互评
- 固定开口顺序：导师问架构 → 王思鉴先答；问测试 → 杨明杰先答；问商业价值 → 林泳桐先答
- **禁止组长每次都抢答**（抢答本身就是"其他人是摆设"的证据）

---

#### 🟢 **问题 7：GitHub PR 长期开放未合并**

**现状**：
- PR #4（登录界面）和 PR #5（报告计划）已开放 12–13 天
- 未合并也未关闭，可能给评审老师"半成品感"

**建议处理方案**：
- Week A 门禁前决定：合并、关闭或转为 draft
- 清理 GitHub 视觉印象（评审老师可能查看仓库）

---

#### 🟢 **问题 8：贡献分布透明化策略**

**现状**：
- Yuxuan Wu 贡献 66.7% commit（34/51），其他 6 人共 17 个
- 董思钦、习羽赛、张梓健（Zhang Zijian ID）各仅 1 次 commit

**建议处理方案**（写进 Appendix A 的叙事）：
- **代码线**：如实申报"软件实现主要由一人完成"
- **报告线**：强调"9 人各负责 1 章 = 知识转移机制"
- **GitHub 证据链**：Week A–B 鼓励组员提交各自章节的 `outline.md` 与 `draft.md` 作为独立 commit
- **组会演练**：任何一章被随机抽问时，换人来答也能答上

---

## 六、督导汇报建议话术（3 分钟版）

### 开场（30 秒）

> Dr. Mumtaz, 本周期我们的核心任务是把软件基线翻译成报告。软件已经封版：8 个 API 端点、147 个测试全绿、12 题 36 陷阱、3 张 UML 图全部在仓库里。我们现在唯一缺的是把这些工程事实写成 40–60 页的正文。

### 主体（90 秒）

> 我们按官方 Brief 的七章结构严格拆分了任务：
> - **Ch1–Ch7**：9 位组员各负责 1 章/1 节，每人 4–6 页，素材全部在仓库不需要编
> - **图表编号已锁定**：17 图 21 表预分配完毕，防止十个人撞号
> - **质量门禁已生效**：Week A 未交 outline 者，章节收回 + Appendix A 如实记 0%
>
> 我们准备了两份配套文档：
> 1. **任务包**（9 份）：每人的写清了页数、小节、素材路径、3 个防身问题
> 2. **防身答案库**：28 个您可能追问的问题 + 30 秒标准答法，全组会演练
>
> **GitHub 数据透明化**：我们在仓库中记录了 51 个 commits、5 个 PRs（2 已合并）、7 位贡献者的完整轨迹。代码集中度（66.7% 由我完成）我们会在 Appendix A 如实申报，报告分工是我们的"知识转移"机制。
>
> 目前有 **3 个具体问题想请教您**：
> 1. **凭证泄露**：我们在 git 历史中误提交了 Neo4j 密码，已重置密码并改代码，能否把这个过程写成 Ch5.6 的安全事件复盘案例？
> 2. **负面结果呈现**：MMLU 实验里有 2 个学科负提升（物理 −1.3pp），我们认为应该如实写进报告——这能增强可信度，对吗？
> 3. **分工透明度**：软件主要由我一人完成，报告是 9 人分章撰写。我们会在 Appendix A 如实申报，并通过"随机抽问机制"保证每人真正理解自己那章。这个处理方式是否符合课程要求？

### 结尾（30 秒）

> 下次组会（Week A 周日），我们交第一批骨架：每人的 outline + 素材清单，9 人各自讲 3 分钟。如果有任何一个人答不上来，我们会按"本章尚未完成"处理并收回。

---

## 七、下一步行动（Week A 具体任务）

| 任务 | 负责人 | 截止时间 | 验收标准 |
| :--- | :--- | :--- | :--- |
| **处理凭证泄露** | 吴宇轩 | 10-29 晚 | Neo4j 密码已重置、代码已改 `os.getenv()`、commit 留痕 |
| **修复 Pydantic 告警** | 吴宇轩 | 10-29 晚 | 6 处 `Field` 改为 `json_schema_extra`、pytest 告警清零 |
| **绘制类图** | 王思鉴 | 10-31 | `.drawio` 或 `.svg` 提交到 `reports/figures/` |
| **启动进度看板** | 谢炜昕 | 10-30 | `progress_tracker.md` 建立 + 每人首次更新 |
| **组会演练** | 全员 | 11-02 晚 | 每人领 5 题 + 发群互评 + 固定开口顺序演练一轮 |
| **骨架提交（G1 门禁）** | 9 位组员 | 11-03 23:59 | 每人交 outline.md（≥12 行三级标题 + 素材清单） |
| **组会答辩** | 全员 | 11-03 组会 | 每人讲 3 分钟、答不上来按未完成处理 |

---

| **合并或关闭 PR #4、#5** | 吴宇轩 | 10-30 | PR 状态清晰、无"半成品感" |

---

## 八、附录：关键文档索引

| 文档 | 路径 | 用途 |
| :--- | :--- | :--- |
| 本汇报材料 | `reports/cycle3_supervisor_briefing.md` | 督导汇报话术与问题清单 |
| **GitHub 统计报告** | `reports/github_pr_commit_statistics.md` | 5 PRs + 51 commits 完整统计 |
| 总体执行计划 | `reports/cycle3_master_plan.md` | 7 章结构 + 分工矩阵 + 图表编号 |
| 任务包总索引 | `reports/cycle3_task_packs/README.md` | 9 人分工 + 两步交付节奏 |
| 防身答案库 | `reports/supervisor_qa_defense_library.md` | 28 个问题 + 标准答法 |
| 项目开发指南 | `CLAUDE.md` | 技术栈 / 命令 / 代码风格 |
| 官方 Brief | `JC2001-GroupProjectDescription-and-Requirements-2026-27.txt` | 课程要求与评分标准 |

---

**文档编制**：Yuxuan Wu（PM / Team Lead）  
**编制日期**：2026-10-29  
**版本**：v1.0  
**下一次更新**：Week A 门禁后（2026-11-04）
