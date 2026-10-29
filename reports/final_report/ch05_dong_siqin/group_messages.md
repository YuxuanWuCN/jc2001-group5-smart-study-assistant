# 群消息（可直接复制粘贴）

> 每条独立，按需要发。发送前把 `<...>` 占位符替换掉。

---

## 1. 给吴宇轩：任务包 06 的 8 处修正

```
@吴宇轩 任务包 06 我拿 develop 的代码逐条核了一遍，有 8 处要修正（实测版我已经写进 PR #16 的 outline 和 draft）：

1) seed_questions.py：932 行 → 实际 657 行
2) 5.3.2 表格里 law_1 的 radar_hit：写的是 boundary → 实际是 trapDefense
3) 5.3.3 "子网划分 2^n−2" 举例：题库里没有这道题（cs 只有流水线 / Cache / TLB）
4) 5.3.3 "供需弹性因果倒置" 举例：econ 三题都是计量经济学（共线性 / IV / 异方差），没有弹性题
5) 5.3.3 "单元测试 vs 集成测试" 举例：没有这道题（可用 se_3 的"变异测试 vs 性能压测"替代）
6) 5.4.3 的 report_service.py 和 /api/reports/trend：都不存在（你已裁定改读 frontend/app.js，谢谢）
7) 5.4.1 伪代码里的 404 / 422：实际实现是 200 + 优雅兜底，422 只在请求体 schema 校验失败时出现
8) 端点数量：README 写 8 个，实际 4 个（/api/quiz、/api/diagnose、/api/health、/api/health/llm）

另外提一句：5.3.3 涉及的 4 条陷阱描述里有"全校 64% / 58% / 71% / 全班 60%"这类无出处数字，建议正文一律不引用，避免被追问样本来源。

我这边 Ch5.3–5.4 的英文初稿已按实测数据写完（PR #16），不影响你改任务包。
```

---

## 2. 给张梓健：Ch2 里 R04 的措辞要同步

```
@张梓健 同步一个会影响你 Ch2 MoSCoW 表的定性：R04「五维能力雷达与趋势」实际是**部分满足**。

代码事实（我核过 frontend/app.js）：
· 五维雷达有，答完题立刻更新；
· 但聚合是**前端会话内**计算，不做跨会话持久化，也没有时间衰减；
· 后端没有 /api/reports/trend 这类聚合接口（后端只有 4 个端点）。

建议 Ch2 的 R04 行写成 "Must — partially satisfied (session-scoped client-side aggregation; no cross-session trend)"，
或者你在表下加一条脚注说明。这样 Ch6 的达标评估和 Ch7 的 Limitations 才能对上口径。
我 Ch5.4.3 也是按这个口径写的，三章一致。
```

---

## 3. 给杨明杰：Ch6 的达标评估与测试数

```
@杨明杰 两条会直接影响你 Ch6 的数据，先同步：

1) 测试总数是 **150**（`pytest --collect-only` 实测），不是 145 或 114。
   其中 test_quiz.py 6 个用例、test_adversarial_backend.py 25 个函数（分布在 6 个测试类）。

2) R04「五维能力雷达与趋势」在 Ch6 的达标评估里应写成**部分满足**：
   前端有会话内聚合（答对 recall +4 / trapDefense +5 / synthesis +3；答错 trapDefense −6 / boundary −4，下限 30、上限 100），
   但没有跨会话持久化和时间衰减，后端也没有聚合端点。

3) 我 Ch5.4.3 写了这个口径，你 Ch6 表 6.5 可以直接引用；如果需要我把"R04 部分满足"的判断依据写成一小段给你，说一声。
```

---

## 4. （可选）给习羽赛 / 梁子铉：雷达文案 +6 vs 代码 +5

```
@习羽赛 @梁子铉 发现一个 1 行的文案不一致，麻烦顺手修掉：
frontend/app.js:1104 和 :1189 的 feedbackCorrectTip 写的是 "Defense Index +6" / "排雷防守指数 +6"，
但 :2388 实际执行的是 Math.min(100, state.radar.trapDefense + 5)。

建议以代码为准把文案改成 +5（若反过来把代码改成 +6，请告诉我，我 Ch5.4.3 的数值要同步改）。
```

---

## 5. （可选）安全提醒：前端硬编码 Key

```
@吴宇轩 @梁子铉 @江昊 安全提醒，今天需要处理：

仓库是 public，但前端有两处明文 API Key：
· frontend/app.js:1207  const GEMINI_DEFAULT_KEY = "sk-6a8d…"
· frontend/index.html:619  <input ... value="sk-6a8d…">

处理顺序（先吊销再改代码，删代码不会让密钥失效）：
1) 该 Key 所属账号本人去百炼控制台 API-KEY 管理里【删除】，并看一眼近期用量/账单有无异常；
2) 代码侧两处移除硬编码，前端改为只读用户自己填入的 Key；
3) 不建议重写 git 历史（10 人协作，force-push 会打乱所有分支）；吊销后历史里的旧 Key 已失效，
   但最终提交的 ZIP 里必须确认没有明文。

@梁子铉 这块归你的 Git 规范，麻烦一并盯一下；之后建议加 pre-commit 密钥扫描（graphrag 的 Neo4j 密码已经出过一次）。
```
