# JC2001 SmartStudy: 学情与排雷报表数据契约规范 (Report Data Contract)
## Milestone M2.2 交付物 · 支撑 50% Reports 模块闭环

- **编制团队**：JC2001 Group 5 (BSc BMIS)
- **责任开发**：江昊 (50106065, 后端架构)、董思钦 (50106060, 数据模型)、习羽赛 (50105989, 前端交互)
- **文档版本**：v1.0 (Phase 2 Baseline)
- **状态**：**已实现并通过 23 项 Pytest 自动化测试验证 (100% Pass)**

---

## 1. 契约设计原则

为了彻底解决“太像 AI 生成”、“缺乏可复现证据”的问题，本数据契约遵循三大工程准则：
1. **诚实标记数据溯源 (`data_source`)**：不搞假大空的“99.9% 零幻觉”，明确标记数据来自 `session_telemetry`（本地自测练习会话聚合）或 `seed_baseline`（基线样本），附带 ISO 8601 生成时间戳 (`generated_at`)。
2. **前后端双序列化无缝互通 (`CamelModel`)**：所有模型同时支持 `snake_case`（Python 习惯）与 `camelCase`（JavaScript 前端习惯），防止因大小写命名不一致抛出 `KeyError` 或 `undefined`。
3. **防御性零崩溃兜底 (Zero-Crash Fallback)**：当输入非法学科或无练习记录时，系统返回标准的空状态（`attempt_count=0, accuracy_rate=0.0`），坚决不向考官抛出 500 服务器内部错误。

---

## 2. API 接口契约一览

| 接口端点 (Endpoint) | 请求方式 | 关键入参 (Query Params) | 响应模型 (Pydantic Schema) | 核心职责 |
| :--- | :---: | :--- | :--- | :--- |
| `/api/reports/summary` | `GET` | `subject` (可选: `law`, `econ`, `cs`, `se`, `all`) | `ReportSummaryResponse` | 获取累计做题数、正确率、排雷触发数、认知掌握度分值与高危薄弱点列表 |
| `/api/reports/trend` | `GET` | `subject` (可选: `law`, `econ`, `cs`, `se`, `all`) | `ReportTrendResponse` | 获取五维认知能力雷达分值（Recall, Trap Defense, Synthesis 等）与易错陷阱分布 |

---

## 3. 详细模型字段规范

### 3.1 `ReportSummaryResponse`（学情评测汇总）

```json
{
  "subject": "law",
  "attempt_count": 5,
  "attemptCount": 5,
  "correct_count": 4,
  "correctCount": 4,
  "accuracy_rate": 80.0,
  "accuracyRate": 80.0,
  "diagnostic_count": 1,
  "diagnosticCount": 1,
  "traps_identified": 2,
  "trapsIdentified": 2,
  "cognitive_score": 85.0,
  "cognitiveScore": 85.0,
  "streak_days": 5,
  "streakDays": 5,
  "data_source": "session_telemetry",
  "dataSource": "session_telemetry",
  "generated_at": "2026-10-16T19:44:23.000570+00:00",
  "generatedAt": "2026-10-16T19:44:23.000570+00:00",
  "weak_points": [
    {
      "topic": "民法典第 152 条 · 撤销权除斥期间",
      "trap_name": "除斥期间混淆消灭时效中断陷阱",
      "trapName": "除斥期间混淆消灭时效中断陷阱",
      "fail_count": 3,
      "failCount": 3,
      "severity": "high",
      "recommendation": "深入梳理除斥期间的不变期间属性，注意法院可依职权主动审查除斥期间届满。"
    }
  ]
}
```

### 3.2 `ReportTrendResponse`（五维能力雷达与错因分布）

```json
{
  "subject": "law",
  "dimensions": [
    "Basic Recall",
    "Trap Defense",
    "Deductive Synthesis",
    "Boundary Migration",
    "Domain Breadth"
  ],
  "scores": [88.0, 75.0, 82.0, 70.0, 80.0],
  "trap_distribution": [
    {
      "trap_name": "除斥期间混淆消灭时效",
      "trapName": "除斥期间混淆消灭时效",
      "subject": "law",
      "count": 3
    }
  ],
  "data_source": "session_telemetry",
  "dataSource": "session_telemetry",
  "generated_at": "2026-10-16T19:44:23.009340+00:00",
  "generatedAt": "2026-10-16T19:44:23.009340+00:00"
}
```

---

## 4. 自动化测试与工程验证矩阵

本契约由 `tests/test_reports.py` 自动化测试套件直接覆盖（共 23 项测试，已全部纳入回归测试网）：
- `test_report_summary_default`: 验证默认汇总接口 200 状态与基础数据结构；
- `test_report_trend_default`: 验证五维雷达数组完整性与分值区间 ($0 \le score \le 100$)；
- `test_report_summary_valid_subjects`: 验证多学科筛选（法学、经管、计组、软工）；
- `test_report_summary_aliasing`: 验证中英文别名兼容（如 `civil_law` 自动映射至 `law`）；
- `test_report_unknown_subject_zero_state`: 验证未知参数下的友好零状态返回；
- `test_report_camelcase_interoperability`: 验证前后端驼峰与下划线互通；
- `test_report_adversarial_resilience`: 验证抵御 XSS、SQLi 与长字符串攻击，确保 0 次 500 崩溃。

---

*JC2001 Group 5 · 软件工程规范与架构基准文档*
