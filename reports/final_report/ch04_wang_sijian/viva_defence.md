# Chapter 4 — Viva Defence Answers

**王思鉴 (50106045)** · architecture · Chapter 4 System Design and Architecture
Allocation from `cycle3_master_plan.md` §4: **Ch4 self-defence + Ch6 cross-review**

Each answer is written to be spoken in 30–60 seconds. Structure: conclusion first, then reason, then the weakness we are volunteering.

---

## ⚠️ Read this before the meeting: four numbers are contested

The defence library and the planning document both quote figures that **do not match the code**. If you answer with the library's numbers while Chapter 4 prints the measured ones, the examiner can catch the contradiction across your own report.

| Quantity | Defence library / plan says | Measured on `develop@626d467` |
| :--- | :--- | :--- |
| API endpoints | 8 | **4** |
| Routers | 5 | **3** |
| `seed_questions.py` | 932 lines | **657** |
| Tests | 145 cases | 8 files / 80 `def test_` functions |
| Diagnosis latency | P95 < 5 ms | median 0.6 µs core; **median 1.5 ms HTTP**, p95 16 ms |

**What to do.** Answer with the measured number and say so explicitly: *"The plan quoted eight endpoints; when I wrote Chapter 4 I re-counted against the code and found four. The chapter uses the measured figure."* That is a strength, not a slip — it shows the report was checked against the artefact. Do not silently repeat the plan's numbers.

---

## Q1. "你用了 Neo4j，是不是为了炫技？" (AD-5)

> Neo4j 不在在线演示链路上，只在离线评估链路上。架构图里它是虚线框，标着 *offline evaluation only*，这就是 AD-5 的视觉证据。
>
> 用它是因为我们跑了 12 个 MMLU 学科的对照实验，7 个涨、3 个平、2 个跌。**如果只是为了炫技，我们不会把两个负值写进报告。**
>
> 而且正因为它会休眠、考场可能断网，我们主动把它移出了演示路径。代价是图谱的收益没法在现场演示，只能靠离线 CSV 佐证 —— 这个代价写在 Table 4.1 里。

**可能的追问：** "那它到底算不算你的系统的一部分？"
> 算，但属于评估基础设施，不属于运行时。这个区分在 Figure 4.2 里就是虚线和实线的差别。

---

## Q2. "为什么不拆微服务？做个微服务架构不是更专业吗？" (AD-1)

> 专业不是复杂度，是匹配。10 周、10 个人、单机演示、零外部依赖 —— 这些约束下，微服务要付的成本（容器编排、服务发现、分布式调试、跨服务事务）全落在我们身上，而它的收益（独立扩缩容、团队并行部署）在这个规模下等于零。
>
> 我们的分层纪律 —— router / service / data —— 已经拿到了模块化的好处，只是没付部署的代价。**模块性是依赖图的属性，不是部署单元的数量。**
>
> 代价写清楚了：无法水平扩展。这个我们承认，而且本场景不需要。

**可能的追问：** "那你为什么不至少拆成两个服务？"
> 因为拆两个仍然要付服务发现和跨服务事务的成本，而收益仍然为零。中间态没有意义。

---

## Q3. "为什么不用 LLM 现场生成诊断？现在的模型很强。" (AD-4)

> 因为这个场景下正确性不能漂移。我们法学那道题的正确解析引用《民法典》第 152 条：自知道或应当知道撤销事由之日起一年内。模型如果写成两年，在教育场景里这是教学事故级错误。
>
> 我们的做法是把陷阱挂在**选项**上，不是挂在题目上。错选项本身就已经标识了误解，所以诊断退化成一次外键查找。**没有推理，就没有幻觉。**
>
> 代价同样明确：只能覆盖预先设计的陷阱。我们设计了 36 个。开放问答场景下这个方案完全失效 —— 这也是我们选择闭式选择题界面的根本原因，不是界面偷懒。

**可能的追问：** "那模型在系统里干什么？"
> 只做一件事：答错之后生成一句苏格拉底式追问。它有 4 秒超时，失败就回落到本地种子文案。**判定已经完成，模型只能改措辞，改不了答案。** 这个边界是我们在 viva 里最愿意守的一条。

---

## Q4. "断网 / Neo4j 过期 / API 欠费会怎样？" (AD-5, Figure 4.1)

> 一切正常。演示路径零外部依赖：无数据库、无 LLM API、无云服务。
>
> 前端静态文件由同一个 uvicorn 进程通过 `StaticFiles` 挂在 `/`，API 挂 `/api`，**同端口同源**。所以演示时不存在"前端能打开但 API 挂了"这种半死状态。
>
> 这不是运气，是 Figure 4.1 里那三个事实的直接后果：单进程、单端口、无数据库。

**可能的追问：** "你怎么证明它真能离线跑？"
> 我们的健康检查端点返回 `has_api_key: false` 时就说明模型不可用，而整个诊断流程仍然完整工作 —— 这是测试里覆盖的分支。

---

## Q5. "CORS 全开、没有鉴权，这不是安全隐患吗？" (AD-6, AD-7)

> 是隐患，我们没藏着。ADR-06 写了"生产化必须收紧"，ADR-07 写了 `localStorage` 会话没有权限边界。
>
> 取舍的理由是演示场景：考官在自己机器上用任意端口打开页面，白名单会让本地调试处处报错。**而且有一个我们没预料到的后果**：正因为生产和演示都是同源，那个 CORS 配置在我们的部署里从未被真正执行过 —— 它既没被验证，也没被需要。这一点我写进了 Chapter 4 的 4.1.1。
>
> Ch7 的 Limitations 把它列为已知限制，Future Work 给了 JWT + 白名单 + 限流的替换方案。

**可能的追问：** "为什么不干脆删掉 CORS 中间件？"
> 因为留着它对本地调试有用，而删掉不会提高安全性 —— 同源部署本来就不靠它。真正的修复是加鉴权，那是 Future Work。

---

## Q6. "你的章节里说诊断是查表，那你的技术贡献到底是什么？" (Q2.3 变体)

> 我们不主张发明了算法 —— 诊断就是一次字典查找，报告里明说了。贡献是三项工程工作：
>
> 1. **选项级陷阱的数据模型**：`OptionItem.trap_id → TrapDetail{title, desc, prereq, radar_hit}`。它把诊断从推理降级成查表，从而做到离线、可测试、亚毫秒。
> 2. **一个可复现的零构建交付形态**：单进程单端口，一条命令。
> 3. **一组诚实的取舍记录**：Table 4.1 的七条 ADR，每条都有代价。
>
> 我们把它定位成 feasibility evidence，不是 research contribution。

---

## Q7. "报告是不是 AI 生成的？" — 架构视角的答法

> 我这章有一个自检口径：**报告里每个数字都能追到文件，而且和代码对得上。** AI 生成的内容通常数字对不上 —— 我们计划书里写 8 个端点，实际代码是 4 个，我写 Chapter 4 时按代码重新数了一遍，报告用的是 4。
>
> 第二个口径是**主动交弱点**：4.4.2 整节写的是我们做错了什么 —— 图过期、schema 反复改、宽泛异常吞掉真实故障。AI 生成的项目不会主动写这些。
>
> 第三个口径是**图能复现**：四张图的 `.mmd` 源文件都在仓库里，改一行就能重出。

---

## 会前 5 分钟速查

| 被问 | 一句话答 | 对应决策 |
| :--- | :--- | :--- |
| Neo4j 炫技？ | 不在在线链路，虚线标注 offline only，负结果也写了 | AD-5 |
| 为什么不微服务？ | 成本落在我们身上，收益为零；模块性是依赖图属性 | AD-1 |
| 为什么不用 LLM 生成诊断？ | 正确性不能漂移；查表无推理即无幻觉；代价是只覆盖预设陷阱 | AD-4 |
| 断网怎么办？ | 单进程单端口无数据库，零外部依赖 | Figure 4.1 |
| CORS 全开安全吗？ | 不安全，已声明；且同源部署下它从未被执行 | AD-6 |
| 你的贡献是什么？ | 选项级陷阱模型 + 零构建交付 + 诚实的取舍记录 | 4.3.2 |
| 报告是 AI 写的吗？ | 数字可追溯且与代码一致、主动写弱点、图可复现 | 4.4.2 |

---

## 交叉审校任务（Week B 第二项）—— 目前阻塞

计划 §4 分配给架构角色的是 **Ch6 的交叉审校**（"架构视角校验证据链"）。

**当前状态：无法执行。** `reports/final_report/` 下只有 `ch04_wang_sijian/` 一个目录，Ch6 初稿不存在。`reports/final_report/reviews/` 目录也尚未创建。

**建议动作：**
1. 等杨明杰的 `ch06` 初稿落到 `develop`（或在群里直接向他要一份 markdown）；
2. 收到后按计划要求给 **≥5 条书面意见**，重点看三处：
   - 6.3 的 MMLU 数字是否与 `graphrag（终）/final_systematic_report.csv` 一致；
   - 6.5 的 NFR 逐条评估是否用了和 Ch2.3、Ch4.6 相同的五类口径；
   - 测试计数（145 用例）的口径是否与 Ch4 应用的实测值冲突 —— 这是我这一章最容易被抓的不一致点；
3. 意见写到 `reports/final_report/reviews/wang-sijian_review_ch06.md`。

在拿到 Ch6 之前，这一项只能标为 pending，不能标为完成。
