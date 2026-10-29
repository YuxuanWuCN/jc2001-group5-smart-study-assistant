# 在线对照实验契约 (Online Experiment Contract)

**功能编号**：`004-persona-hallucination-audit`
**对应脚本**：`scripts/audit_online_baseline.py`
**对应产物**：`reports/audit/online_baseline.csv`（跑成） 或 `reports/audit/online_baseline.skipped.json`（跳过）
**上游决策**：`research.md` 决策 1（L4 定义）、决策 4（三分组 + Wilson 区间）

---

## 一、实验设计

### 1.1 三分组

| 组 | 名称 | 输入 | 约束强度 | 回答 Q3 时的角色 |
| :-: | :--- | :--- | :--- | :--- |
| **A** | `free_generation` | 题干 + 4 选项 + "请给出诊断反馈" | 无（模型自由生成） | **基线**：代表"没有本系统时的 AI 幻觉水平" |
| **B** | `offline_lookup` | 题干 + 4 选项 + 用户所选错误选项 → 服务端查表 | 强（完全无生成） | **下界参照**：幻觉面被结构性消除 |
| **C** | `graph_constrained` | 题干 + 4 选项 + 用户所选错误选项 + 图谱邻接（前置概念/陷阱节点）→ 查表 + 图谱约束话术 | 中（查表定结论，生成仅用于组织语言） | **本系统真实形态**：与 A 对比即为"降低幅度" |

### 1.2 分组必须成对

- **A ↔ C 才是本系统的"降低幻觉"证据**：两者都有生成面，差别只在有无选项级约束。
- **B 不参与"降低"计算**，只用来证明"离线路径的 L4 生成面为 0"（机制事实）。把 B 放进"A→B 降低 x%"是**构念作弊**，因为 B 根本没有生成。

### 1.3 采样

- 12 道题 × 每题至少 2 次调用 × 3 组 ⇒ 每格 N ≥ 20（取 `N=24`：12 题 × 2 次）。
- 温度固定 `temperature=0.7`；`seed` 若供应商支持则固定，否则在 `env_fingerprint` 中记录"不可复现性提示"。
- 顺序：**交错执行**（A1,B1,C1,A2,B2,C2…），避免供应商侧时间漂移污染组间差异。

---

## 二、输出字段契约

`reports/audit/online_baseline.csv` 的列（顺序固定）：

| 列名 | 类型 | 必填 | 说明 |
| :--- | :--- | :-: | :--- |
| `sample_id` | string | ✅ | `A-law_1-r1` 形式：`<组>-<question_id>-<重复序号>` |
| `group` | enum | ✅ | `A_free_generation` / `B_offline_lookup` / `C_graph_constrained` |
| `question_id` | string | ✅ | `law_1` … `se_3` |
| `repeat_index` | int | ✅ | 1 起 |
| `prompt_hash` | string | ✅ | 实际发送 prompt 的 SHA-256（前 16 位即可），用于事后核对是否误改 |
| `raw_output` | string | ✅ | 模型原始输出（B 组为服务端返回的 JSON 文本）；换行须转义 |
| `model_id` | string | ✅ | 实际调用的模型标识（如 `qwen-turbo`） |
| `latency_ms` | int | ✅ | 端到端耗时 |
| `rater_1_verdict` | enum | ✅ | `HALLUCINATED` / `NOT_HALLUCINATED` / `UNSURE` |
| `rater_2_verdict` | enum | ✅ | 同上，**独立盲评**（看不到 rater_1 结果、看不到来源组） |
| `adjudicated_verdict` | enum | ✅ | 若两人一致取该值；不一致则由第三人裁决，且本字段填裁决值并在 `adjudication_note` 说明 |
| `adjudication_note` | string | ⚠️ | 不一致或 `UNSURE` 时必填 |
| `hallucination_span` | string | ⚠️ | `HALLUCINATED` 时必填：指出不实陈述的原文片段 |
| `hallucination_type` | enum | ⚠️ | `factual_error` / `unsupported_attribution` / `overclaiming` / `fabricated_citation` |

**判定口径（L4 定义，必须写在评分表首页）**
> 一段输出被判为 `HALLUCINATED`，当且仅当它包含一个**可被证伪且为假**的具体陈述——包括：错误的学科事实、把不存在的知识漏洞说成用户的漏洞、编造教材/条文出处。**语气不自信、表述含糊、内容空泛但无误** ⇒ `NOT_HALLUCINATED`（这是"无用"，不是"虚假"，二者不可混计）。

---

## 三、汇总契约

### 3.1 Wilson 95% 区间（唯一允许的区间算法）

对组 g，分子 `k`、分母 `n`（`n` = 该组样本数，不含 `adjudicated_verdict` 缺失者）：

```
z = 1.959963984540054
p̂ = k / n
den   = 1 + z²/n
centre= (p̂ + z²/(2n)) / den
half  = z * sqrt(p̂(1-p̂)/n + z²/(4n²)) / den
ci_low, ci_high = max(0, centre-half), min(1, centre+half)
```

**禁止使用**正态近似 `p̂ ± 1.96·sqrt(p̂(1-p̂)/n)`：本实验 n≈24 且预期 p 接近 0，正态近似下界会为负。

### 3.2 评分者一致性

- 对每一对评分计算 **Cohen's κ**（二分类合并 `UNSURE` 为第三类时改用 Fleiss' κ 并注明）。
- **κ ≥ 0.6**：报告 A、C 的 `rate` 与 `CI`，并报告 `rate_A - rate_C` 及两者 CI 是否重叠。
- **κ < 0.6**：**禁止报告点估计**。`verdict.json` 中 `l4.status` 置 `skipped`，`note` 写 `rater_agreement_below_threshold kappa=<value>`，并说明需重新培训评分者。

### 3.3 结论措辞（强制）

- CI **重叠** ⟹ 只能写"本实验**未能**检测到差异（N=24/格，功效不足）"。
- CI **不重叠** ⟹ 可写"在本实验条件下，A 组点估计 a（CI …）高于 C 组 b（CI …）"。
- **任何情况下**不得写"显著降低"（样本量不足以做假设检验，且"显著"已在禁用词表）。

---

## 四、跳过路径（无 API Key 时的正式行为）

当环境变量 `QWEN_API_KEY` 缺失或为空：

1. **不发起任何网络请求**（脚本启动时即检查，不做探测性调用）。
2. 写 `reports/audit/online_baseline.skipped.json`，结构：

```json
{
  "status": "skipped",
  "reason": "QWEN_API_KEY not set",
  "timestamp_utc": "2026-10-18T12:34:56Z",
  "env_fingerprint": { "python_version": "3.13.14", "git_commit": "…", "branch": "…" },
  "what_would_have_run": "3 groups x 12 questions x 2 repeats = 72 samples",
  "how_to_run": "set QWEN_API_KEY=<your key> && python scripts/audit_online_baseline.py",
  "report_usage": "L4 记为 N/A（未测量），结论等级停在 V1"
}
```

3. **退出码 0**。跳过是合法状态，不是失败（`research.md` 决策 4）。
4. 该文件存在时，`verdict.json` 的 `l4.status` 必须是 `skipped`（**不是** `na_no_generation_face`——后者专指离线路径无生成面）。

---

## 五、与既有产物的接口

| 上游 | 用法 |
| :--- | :--- |
| `backend/app/data/seed_questions.py` | 12 道题的题干/选项/陷阱/图谱，A、B、C 三组共用同一份素材 |
| `backend/app` 的 `/api/diagnose` | B 组与 C 组通过真实 API 调用（而非直接 import），保证测的是系统实际行为 |
| `reports/audit/verdict.json` | 写入 `l4` 字段；`status=measured` 时才可能达到 V2 |

**禁止**：在实验脚本里绕过 API 直接调用内部函数——那测的是"库函数"而不是"系统"。若无法启动服务器，B/C 组记为 `skipped` 并在 note 说明。
