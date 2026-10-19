# sources.md — Ch 5.3–5.4 引用到的仓库素材

> 按全组写作规范要求：列出本章所有数字与断言对应的仓库文件，**每个数字都必须能在此表找到出处**。
> 本表所有条目已于 2026-10-19 逐条打开核对。

## 1. 题库与陷阱数据

| 文件 | 用途 | 本章引用的具体数据 |
| :--- | :--- | :--- |
| `backend/app/data/seed_questions.py` | 12 道题、36 个陷阱的唯一权威数据源（657 行，集合变量 `SEED_QUESTIONS`） | 12 题；law/cs/econ/se 各 3 题；36 陷阱（每题 3 个）；难度分布 ★★★2/★★★★8/★★★★★2；`radar_hit` 分布 boundary 12 / recall 8 / trapDefense 7 / synthesis 7 / precision 2；12/12 题 `explanation` 带 `【权威考点解析】` 出处标注 |
| `backend/app/models/quiz.py` | `QuizItem` / `OptionItem` / `TrapDetail` / `GraphNode` / `GraphEdge` 的字段定义（181 行） | `TrapDetail` 四字段 `title` / `desc` / `prereq` / `radar_hit`（Table 5.5 的依据） |

## 2. 诊断算法

| 文件 | 用途 | 本章引用的具体事实 |
| :--- | :--- | :--- |
| `backend/app/services/diagnostic_service.py` | 诊断引擎实现（274 行） | 规则判对错 → 陷阱查表 → 双模式（LLM 可用则调用、否则本地兜底）→ 全局 failsafe；未知题号返回 200＋兜底而非 404 |
| `backend/app/routers/diagnose.py` | `POST /api/diagnose` 路由（无额外校验逻辑） | 伪代码语义的依据：路由层不做 404/422 分支，422 仅来自请求体 schema 校验 |
| `backend/app/services/llm_diagnostics.py` | LLM 连通性探测与失败分类（401 行，本周期已合并的 PR #10） | 5.4.2 关于"LLM 调用失败被分类并降级"的描述素材 |

## 3. 雷达聚合（5.4.3，方案 B：前端聚合）

| 文件 | 用途 | 本章引用的具体数据 |
| :--- | :--- | :--- |
| `frontend/app.js` | 会话内五维雷达的即时聚合实现 | 答对：`recall +4` / `trapDefense +5` / `synthesis +3` / `predictedScore +0.5`；答错：`trapDefense −6` / `boundary −4`；钳制：维度上限 100、答错路径下限 30、`predictedScore` 上限 99；初始基线 `recall 76 / boundary 62 / trapDefense 65 / synthesis 72 / precision 81`；前端未消费后端 `radar_dimension` / `score_delta`（引用次数 0） |

## 4. 测试与数据完整性

| 文件 | 用途 | 本章引用的具体数据 |
| :--- | :--- | :--- |
| `tests/test_quiz.py` | 题库数据结构测试 | 6 个测试用例 |
| `tests/test_adversarial_backend.py` | 对抗性/边界输入测试 | 25 个测试函数，分布在 6 个测试类 |
| 全量测试套件 | 第 6 章口径对齐用 | `pytest --collect-only` 实测 **150** 个测试 |

## 5. 图表来源

| 编号 | 来源 |
| :--- | :--- |
| Table 5.4 | `backend/app/data/seed_questions.py` 逐题汇总 |
| Table 5.5 | `backend/app/models/quiz.py` 的 `TrapDetail` 定义 ＋ `law_1 / trap_law_1` 真实取值 |
| Table 5.6 | 本章论述（查表 vs LLM 现场生成） |
| Figure 5.2 | 自绘（错选 → `trap_id` → `TrapDetail` → 诊断抽屉的因果链）；绘图源文件拟放 `reports/figures/` |

## 6. 任务书与规范

| 文件 | 用途 |
| :--- | :--- |
| `reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md` | 本任务包（结构、字数、雷区、导师三问）；其中 4 处数字与代码不符，已按实测修正 |
| `reports/cycle3_task_packs/README.md` | 全组写作规范（英式拼写、Harvard、图表编号锁定、禁止贴源码） |

## 7. 本章不引用的内容（重要）

| 内容 | 原因 |
| :--- | :--- |
| 陷阱描述中的"全校 64%""58%""71%""全班 60%" | 无统计来源，违反「每个数字必须可追溯」；改写为"依据教材与考纲标注的高频易错点" |
| 陷阱 `title` 的 🚨 emoji 原文 | 学术正文需转写为陈述句 |
| `report_service.py` / `/api/reports/trend` / `reports/report_data_contract.md` | 仓库中不存在；5.4.3 已按组长裁定改为引用 `frontend/app.js` |
