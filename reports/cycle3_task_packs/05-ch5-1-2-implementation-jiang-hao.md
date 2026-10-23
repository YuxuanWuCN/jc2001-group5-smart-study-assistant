# 任务包 05 · 第 5 章 5.1–5.2 实现技术栈与接口契约（＋附录 D）

| 项 | 内容 |
| :--- | :--- |
| **负责人** | 江昊（50106065 · PoC Lead Dev） |
| **章节** | 第 5.1 节 Technologies, Tools, Frameworks and Software Structure ＋ 第 5.2 节 API Contracts and Domain Model ＋ **附录 D Glossary and API Snapshot** |
| **页数** | 5–6 页（约 **1,800–2,300 English words** + **3 张表 / 1 张图 / 3 段 JSON**） |
| **交付路径** | `reports/final_report/ch05_jiang_hao/` → `outline.md` → `draft.md` |
| **截止** | outline: Week A 周日 23:59 ／ draft: Week B 周日 23:59 |
| **依赖** | 王思鉴的 Figure 4.3 类图（你写 5.2 时必须与它同一套类名与关系） |
| **上游硬约束** | 官方 Brief：Implementation 章需含 technologies / tools / frameworks / software structure / algorithms / important technical decisions / GUI；**但禁止贴源码** |

---

## 1. 一句话说明你要交付什么

**把"我们用了什么、怎么拼在一起、对外承诺了什么"写成一份可被外部开发者照着重实现的接口文档。**

你和董思钦合写第 5 章：他写 5.3–5.4（算法内部），你写 5.1–5.2（技术底座与对外契约）；习羽赛写 5.5（界面），梁子铉写 5.6（部署）。**你的部分必须做到：任何一个同学拿着你的 5.2 就能写出一个能跑的前端。**

---

## 2. 逐节结构与字数预算

### 5.1 Technologies, Tools, Frameworks and Software Structure (800–1,000 words + **Table 5.1 + Figure 5.1**)

#### 5.1.1 技术栈表（**Table 5.1**）

| 层 | 技术 | 版本 | 选它的理由（一句话） | 被拒绝的替代 |
| :--- | :--- | :--- | :--- | :--- |
| API 框架 | FastAPI | 回 `requirements.txt` 核对 | 自动 Pydantic 校验 + 自动 OpenAPI 文档 | Flask（无内建校验）、Django（过重） |
| 数据校验 | Pydantic v2 | 同上 | 模型即契约，422 自动生成 | 手写 `if` 校验 |
| ASGI 服务器 | uvicorn | 同上 | 一条命令起服务，支持静态挂载 | gunicorn（多进程无必要） |
| 前端 | 原生 HTML5 / CSS3 / ES6+ | — | 零构建、FCP < 100 ms、离线可跑 | React + Vite、Vue、Tailwind |
| 样式体系 | CSS Variables（设计 Token） | — | 主题切换零重渲染 | SASS/LESS 预处理器 |
| 状态持久化 | `localStorage` | — | 无后端会话表 | JWT、Cookie+Session |
| 图表 | 回 `frontend/app.js` 核对（自绘 SVG 还是 ECharts） | — | **必须核对，不要猜** | — |
| 测试 | pytest | 回 `tests/` 与 CI 配置核对 | 145 用例 3.6 秒 | unittest |
| 图谱（离线） | Neo4j Aura + 自建 GraphRAG 脚本 | — | 仅离线评估链路 | 无 |

> ⚠️ **版本号必须从 `requirements.txt` / `package.json`（如有）实读**，不要写"最新版"。考官会数这个。

#### 5.1.2 软件结构（**Figure 5.1，包图/目录树图**）

画一张后端包结构图（可直接画目录树）：

```
backend/app/
├── main.py              # create_app() · CORS · 5 routers · StaticFiles("/")
├── routers/             # 5 个：health, quiz, diagnose, reports, auth
├── services/            # 5 个：question, diagnostic, report, auth, graph
├── models/              # 5 个 Pydantic 模型模块
└── data/seed_questions.py   # 932 行 · 12 题 · 36 陷阱
frontend/
├── index.html  (57 KB)
├── app.js      (259 KB)
└── style.css   (73 KB)
tests/                    # 9 文件 / 78 函数 → 145 用例
```

**正文必须解释三件事**：
1. **为什么 router 与 service 分离**：router 只做 I/O 与校验，service 承载业务，这样 service 可以脱离 HTTP 单测（这也解释了为什么 145 个用例跑得那么快）。
2. **为什么 `data/` 是 Python 源文件而不是 JSON**：类型检查、IDE 补全、import 即用、无文件 I/O 与路径问题——但代价见 ADR-03。
3. **为什么前端不拆分模块文件**：零构建下多文件需要自己实现加载顺序管理，收益不抵成本；`app.js` 内部按功能分区（注释分区）而不是 ES Module 动态加载。

#### 5.1.3 关键实现决定（3–4 条，每条 60–80 词）

挑 4 条**只有写过这段代码的人才知道的**决定（这就是去 AI 感）：
- 例如「我们选择让 `StaticFiles(html=True)` 挂在 `/`，使前端与 API 同源，从而在生产路径上完全不需要 CORS」；
- 例如「`/api/reports/trend` 的聚合在服务层做而不是前端做，因为前端要在 0 次作答时展示空状态，让前端做聚合会把 `NaN` 泄漏到 UI」；
- 例如「陷阱数据结构里 `traps` 用 dict 而不是 list，因为诊断时需要 O(1) 按 `trap_id` 查找」；
- 例如「`app.js` 里的静态资源版本号用 query string 控制缓存（见提交 `09ae770`），因为浏览器缓存曾导致更新后界面不刷新」——**这条有真实 commit 佐证，写进去极有说服力。**

### 5.2 API Contracts and Domain Model (1,000–1,300 words + **Table 5.2 / 5.3 + 3 段 JSON**)

#### 5.2.1 八端点契约表（**Table 5.2**）

| # | Method | Path | 用途 | Request Model | Response Model | 状态码 |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | GET | `/api/health` | 健康探针 | — | `HealthResponse` | 200 |
| 2 | GET | `/api/quiz` | 按学科取题 | query `subject?` | `List[QuizItem]` | 200 / 422 |
| 3 | POST | `/api/diagnose` | 选项级诊断 | `DiagnoseRequest` | `DiagnoseResponse` | 200 / 404 / 422 |
| 4 | GET | `/api/reports/summary` | 学情摘要卡 | query | `ReportSummaryResponse` | 200 / 422 |
| 5 | GET | `/api/reports/trend` | 五维雷达趋势 | query | `ReportTrendResponse` | 200 / 422 |
| 6 | GET | `/api/auth/demo-users` | 演示账号列表 | — | `DemoUsersResponse` | 200 |
| 7 | POST | `/api/auth/login` | 登录 | `LoginRequest` | `AuthResponse` | 200 / 401 / 422 |
| 8 | POST | `/api/auth/register` | 注册 | `RegisterRequest` | `AuthResponse` | 200 / 409 / 422 |

> ⚠️ **八个端点的路径、方法名、模型名、状态码必须逐条回 `backend/app/routers/` 核对**。这张表是全报告被交叉引用最多的表（Ch3 的用例、Ch6 的需求评估都会引用它），错一个就三处不一致。

#### 5.2.2 三段 JSON 示例（只贴 3 个，不要贴 8 个）

1. **`POST /api/diagnose` 成功（200）**：必须展示 `verdict` / `trap`（含 `title`/`desc`/`prereq`/`radar_hit`）/ `explanation` 三层结构。
2. **`POST /api/diagnose` 失败（404 与 422）**：各给一小段，说明错误体的形状。
3. **`GET /api/reports/trend` 成功（200）**：展示五维雷达的数组结构。

**贴 JSON 的规定**：用等宽字体、≤25 行、`{ }` 内的字段**必须与真实响应逐字一致**（建议直接 `curl` 一次拷回来）。

#### 5.2.3 领域模型表（**Table 5.3**，与王思鉴 Figure 4.3 同一套）

| 模型 | 字段 | 类型 | 约束 / 说明 |
| :--- | :--- | :--- | :--- |
| `QuizItem` | `id`, `subject`, `stem`, `options`, `traps`, `explanation` | str / str / str / `List[OptionItem]` / `Dict[str, TrapDetail]` / str | `id` 全局唯一；`options` 恒为 4 |
| `OptionItem` | `key`, `text`, `is_correct`, `trap_id` | str / str / bool / str | 恰有一个 `is_correct=True`；错项 `trap_id` 必须能在 `traps` 中查到 |
| `TrapDetail` | `title`, `desc`, `prereq`, `radar_hit` | str ×4 | `radar_hit` ∈ 5 个雷达维度枚举 |
| `DiagnoseRequest` | `question_id`, `selected_option` | str | 两者均必填 |
| `DiagnoseResponse` | `verdict`, `trap`, `explanation`, … | — | `verdict ∈ {correct, misconception}` |
| `ReportSummaryResponse` / `ReportTrendResponse` | 见 `reports/report_data_contract.md` | — | 字段口径以契约文件为准 |

**必须写的核心论断**（与王思鉴 Ch4.3、董思钦 Ch5.3 三处口径一致）：
> **陷阱挂在选项上，而不是题目上。** `OptionItem.trap_id` 是一条指向 `QuizItem.traps[trap_id]` 的外键。这个建模决定使诊断退化为一次字典查找，而不是一次推理。

#### 5.2.4 契约的自动化保障

- Pydantic 模型即契约：字段类型与必填性由框架强制，非法输入自动 422；
- 契约与测试同源：`tests/test_diagnose.py`（8 用例）与 `test_reports.py`（9 用例）直接断言响应字段；
- 契约与前端映射：`reports/api_frontend_mapping.md` 记录每个端点被前端哪个函数消费——**这是"报告与代码一致"的证据链**。

### 附录 D Glossary and API Snapshot

1. **术语表 ≥12 条**（每条 1–2 句），建议收：`trap`、`trap_id`、`distractor`、`binary feedback`、`misconception`、`prerequisite`、`radar dimension`、`GraphRAG`、`deterministic lookup`、`modular monolith`、`zero-build frontend`、`MoSCoW`、`MMLU`、`RAGAS`。
2. **API 快照**：八端点的一页速查（可直接由 FastAPI 自动生成的 `/docs` 截图，**截图比手抄可信**）。

---

## 3. 你需要的素材

| 素材 | 路径 |
| :--- | :--- |
| 应用装配 | `backend/app/main.py` |
| 全部路由 | `backend/app/routers/*.py` |
| 全部模型 | `backend/app/models/*.py` |
| 依赖版本 | `requirements.txt`（或 `backend/requirements.txt`，自行定位） |
| 数据契约 | `reports/report_data_contract.md` |
| 前后端映射 | `reports/api_frontend_mapping.md` |
| 自动文档 | 本地起服务后访问 `http://127.0.0.1:8000/docs`（OpenAPI UI，截图用） |

---

## 4. 会被退回的雷区

1. ❌ **贴源码**（`def ...` / `@router.get` 全删）→ Brief 禁止，删掉。
2. ❌ 端点表漏掉 `/api/auth/*` 三条中的一个，或把 status code 写成"200 或 200"。
3. ❌ 版本号写"latest"。
4. ❌ 领域模型类名与王思鉴 Figure 4.3 不一致（`TrapDetail` 写成 `Trap`）。
5. ❌ JSON 示例手写编造字段 → 必须 curl 真实拷回。
6. ❌ 附录 D 术语表只有 5 条。

---

## 5. 验收清单（DoD）

- [ ] 1,800–2,300 词，5–6 页
- [ ] **Table 5.1** 技术栈（含版本与被拒替代）+ **Table 5.2** 八端点 + **Table 5.3** 领域模型
- [ ] **Figure 5.1** 软件结构包图
- [ ] 3 段真实 JSON（含 404/422 错误体）
- [ ] 5.1.3 至少 1 条带 commit hash 的真实实现细节（如 `09ae770` 的缓存版本号）
- [ ] 附录 D 术语表 ≥12 条 + `/docs` 截图
- [ ] `sources.md` 已附
- [ ] 能不看稿讲 5 分钟

---

## 6. 导师会问你的 3 个问题（准备好 30 秒答法）

**Q1. "为什么 `diagnose` 用 POST？它不是幂等的吗？"**
> 答：语义上它确实是幂等的（同样的题 + 同样的选项必得同样的诊断），用 GET 也没有问题。我们选 POST 的原因是**把作答当作一次事件提交**而不是资源读取——请求体里有 `question_id` + `selected_option` 两部分，放 query string 既难看又会在日志里泄露学生答案。而且我们后续如果要加"提交时间戳 / 会话 ID"这类字段，POST 不需要改接口形状。**这是可读性优先于纯 REST 教条的取舍。**

**Q2. "如果前端传了一个不存在的题号，会发生什么？"**
> 答：返回 **404**，不是 500。这条由 `tests/test_adversarial_backend.py` 里的对抗性用例钉住（A1 组：不存在的 ID / 负数 / 字符串）。选项非法则返回 **422**（Pydantic 校验层拦下），也不会 500。**我们的设计原则是：所有非法输入都被显式分类，任何一种都不应导致未捕获异常。**

**Q3. "陷阱为什么挂在选项上，挂在题目上不是更简单？"**
> 答：因为**同一道题的每个错误选项，误解是不同的**。比如法学那道题，选"1 年"是除斥期间混淆，选"3 年"是诉讼时效混淆，选"20 年"是最长保护期混淆——三个错项对应三个完全不同的补救方向。如果陷阱挂在题目上，无论学生选哪个错项，系统只能给出同一句"你答错了"。挂到选项上，诊断才能精确到"你缺哪块前置知识"。代价是数据编写成本翻三倍（36 个陷阱 vs 12 个），这是我们愿意付的成本。

---

## 7. 提交方式

1. `git switch -c report/ch05-jiang-hao`
2. 文件放 `reports/final_report/ch05_jiang_hao/`
3. 提 PR 到 `develop`，标题：`docs(report): Ch5.1 tech stack and structure + Ch5.2 API contracts + glossary`
4. 群里 @ 吴宇轩 + @ 王思鉴（类图对齐）+ @ 谢炜昕（八端点表会被 Ch3/Ch6 引用，改一处要通知）
