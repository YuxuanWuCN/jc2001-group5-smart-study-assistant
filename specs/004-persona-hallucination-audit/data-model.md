# 数据模型：审计实体与结果契约

**功能编号**：`004-persona-hallucination-audit`
**日期**：2026-10-18
**上游**：[spec.md](spec.md) §4 定义 · [research.md](research.md) 决策 1/2/3/5
**状态**：PHASE 1 OUTPUT

本文件定义审计产物中**六个实体**的字段、值域与必填规则。所有实体最终序列化为 `reports/audit/` 下的 CSV/JSON，字段名即契约名（`contracts/` 中的 schema 以此为准）。

---

## 1. `PersonaClaim`（画像断言）

一条 Table 1.3（`reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:76-84`）中的可判定断言。

| 字段 | 类型 | 必填 | 值域 / 规则 |
| :--- | :--- | :-: | :--- |
| `claim_id` | string | ✅ | `PA-01` … `PA-nn`，稳定不复用 |
| `persona` | enum | ✅ | `A_突击型考试生` / `B_系统复习者` / `C_课程教师` |
| `claim_text` | string | ✅ | 断言原文摘录（≤80 字），必须能定位到源行号 |
| `claim_kind` | enum | ✅ | `身份` / `当前工具` / `痛点` / `期待` / `是否目标用户` |
| `source_type` | enum | ✅ | `文献` / `竞品行为` / `组内讨论` / `无来源` |
| `source_locator` | string | ⚠️ | `source_type=无来源` 时允许空；否则必须是 `文件:行号` 或文献条目 |
| `evidence_level` | enum | ✅ | `E0` / `E1` / `E2` / `E3`（见 spec §4.1） |
| `is_core` | bool | ✅ | 是否是该 Persona 的**核心痛点/期待**（决定 spec §4.1 判定规则的触发） |
| `allowed_usage` | string | ✅ | 由 `evidence_level` 自动导出，禁止手工覆盖 |
| `auditor` | string | ✅ | 执行审计的成员姓名 + 日期 |

**校验规则**
- V1：`evidence_level=E0` ⟺ `source_type=无来源`（双向）。
- V2：`is_core=true` 且 `evidence_level ∈ {E0}` ⟹ 该断言不得出现在任何 SMART 目标（Table 1.2）或 MoSCoW 需求（Table 2.2）的"依据"列中。审计脚本需交叉检查并输出违规列表。
- V3：`evidence_level=E3` 必须携带样本说明（n、抽样方式），否则脚本拒绝写盘。

---

## 2. `RequirementMapping`（需求—画像映射）

Ch2 的 14 条 MoSCoW 需求（R01–R14）到画像/痛点/幻觉层的映射。

| 字段 | 类型 | 必填 | 值域 / 规则 |
| :--- | :--- | :-: | :--- |
| `requirement_id` | string | ✅ | `R01` … `R14`，**与 Ch2 Table 2.2 逐字一致** |
| `requirement_text` | string | ✅ | 摘录，不改写 |
| `moscow` | enum | ✅ | `Must` / `Should` / `Could` / `Won't` |
| `served_personas` | string[] | ✅ | `[A]` / `[A,B]` / `[]`（空数组必须给 `gap_reason`） |
| `served_pain_points` | string[] | ✅ | 引用 `PersonaClaim.claim_id` |
| `assumption_driven` | bool | ✅ | 其依据是否来自 E0/E1 断言 |
| `hallucination_layers` | enum[] | ✅ | 该需求主要约束哪几层 `L1..L4`；不相关填 `[]` |
| `external_falsifiable_claim` | string | ⚠️ | `assumption_driven=true` 时必填：改写后的可证伪命题 |
| `gap_reason` | string | ⚠️ | `served_personas` 为空时必填 |

**校验规则**
- V4：`served_personas` 为空 ⟹ `moscow ∈ {Could, Won't}`，否则报"有 Must 功能但无画像支撑"违规（预期命中 R10 需重判）。
- V5：所有出现在 `served_pain_points` 中的 `claim_id` 必须存在于 `PersonaClaim` 表（外键完整性）。

---

## 3. `HallucinationFinding`（L1 内容审计条目）

| 字段 | 类型 | 必填 | 值域 / 规则 |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L1-<question_id>-<option_key>` 或 `L1-<question_id>-<trap_id>` |
| `question_id` | string | ✅ | `law_1` … `se_3` |
| `subject` | enum | ✅ | `law` / `cs` / `econ` / `se` |
| `artifact_kind` | enum | ✅ | `option_text` / `correct_flag` / `trap_title` / `trap_desc` / `trap_prereq` / `graph_node` / `graph_edge` |
| `artifact_ref` | string | ✅ | 具体对象标识（`option_key` 或 `trap_id` 或 `node_id`） |
| `claim_under_test` | string | ✅ | 被检验的学科命题（如"民法典 152 条除斥期间自知道之日起 1 年"） |
| `machine_flag` | enum | ✅ | `OK` / `SUSPECT` / `NA`（机器初筛结论） |
| `machine_reason` | string | ⚠️ | `machine_flag=SUSPECT` 时必填 |
| `human_verdict` | enum | ✅ | `TRUE` / `FALSE` / `UNDECIDABLE` / `PENDING` |
| `human_note` | string | ⚠️ | `human_verdict ∈ {FALSE, UNDECIDABLE}` 时必填 |
| `is_in_denominator` | bool | ✅ | `UNDECIDABLE` 仍**留在分母**（research 决策 1），只有 `artifact_kind` 不构成事实断言的条目才可置 `false` |
| `reviewer` | string | ⚠️ | `human_verdict != PENDING` 时必填 |

**汇总输出（写入 `verdict.json`）**
```
L1.denominator = count(is_in_denominator = true)          # 预期 84（48 选项 + 36 陷阱）
L1.false_count = count(human_verdict = FALSE)
L1.undecidable = count(human_verdict = UNDECIDABLE)
L1.rate        = false_count / denominator
L1.coverage    = count(human_verdict != PENDING) / denominator   # 必须 = 1.0 才允许宣称 L1 结论
```

---

## 4. `AttributionFinding`（L2 归因审计条目）

| 字段 | 类型 | 必填 | 值域 / 规则 |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L2-<question_id>-<trap_id>` |
| `option_key` | string | ✅ | 该陷阱挂载的干扰项 |
| `trap_name` | string | ✅ | `TrapDetail.title` |
| `misconception` | string | ✅ | `TrapDetail.desc` 所描述的**学生可能的错误概念**，需被归一化为短标签 |
| `duplicate_group` | string | ⚠️ | 若同题内两个不同 `option_key` 归一化到**同一** `misconception` 标签则填该标签 |
| `distinguishable` | bool | ✅ | `duplicate_group` 为空时为 `true` |
| `human_verdict` | enum | ✅ | `CONSISTENT` / `INCONSISTENT` / `PENDING` |

**校验规则**
- V6：`distinguishable=false` 的条目计入 L2 分子（归因不可区分 = 归因幻觉）。
- V7：`human_verdict=PENDING` 为 0 才允许宣称 L2 结论。

---

## 5. `LeakageFinding`（L3 泄漏审计条目）

| 字段 | 类型 | 必填 | 值域 / 规则 |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L3-<question_id>` |
| `correct_option_key` | string | ✅ | 正确选项 |
| `answer_entities` | string[] | ✅ | 从正确选项文本抽取的关键实体（数字/条文号/专有术语） |
| `guidance_field` | enum | ✅ | `socratic_prompt` / `trap_hint` / `explanation` |
| `leaked_entities` | string[] | ✅ | 在引导字段中出现的实体 |
| `is_leak` | bool | ✅ | 规则：`leaked_entities` 覆盖 **全部** `answer_entities` 时判 `true`（部分命中记 `partial` 但不算泄漏） |
| `detector_precision_note` | string | ⚠️ | `is_leak=true` 时必填，说明为何不是"知识性正常引用"（假阳性来源须显式记录，见 US-03 验收 2） |
| `human_verdict` | enum | ✅ | `CONFIRMED_LEAK` / `FALSE_POSITIVE` / `PENDING` |

**校验规则**
- V8：`human_verdict=FALSE_POSITIVE` 的条目仍保留在 CSV 中（保证审计可复查），但不计入 L3 分子。
- V9：分母 = 12（每题一条），缺少任一道题即脚本报错。

---

## 6. `Verdict`（结论实体 → `reports/audit/verdict.json`）

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :-: | :--- |
| `verdict_level` | enum | ✅ | `V0` / `V1` / `V2` / `V3`（spec §4.3，必须由证据自动推出，不得手填） |
| `verdict_rationale` | string | ✅ | 一段话说明为何是这个等级 |
| `persona_level_min` | enum | ✅ | 三张 Persona 中核心痛点最差的证据等级 |
| `l1` / `l2` / `l3` / `l4` | object | ✅ | 各自 `{denominator, numerator, rate, coverage, status}`；`l4.status ∈ {measured, skipped, na_no_generation_face}` |
| `claim_matrix` | object | ✅ | 依据 `contracts/report-claim-contract.md` 推导出的"允许写的句子 / 禁止写的句子" |
| `env_fingerprint` | object | ✅ | `python_version`, `pandas_version`, `git_commit`, `branch`, `timestamp_utc`, `host_os` |
| `determinism_check` | object | ✅ | `run_1_hash`, `run_2_hash`, `identical: bool`（必须 `true`） |
| `outstanding_reviews` | string[] | ✅ | 所有 `PENDING` 条目清单；非空时 `verdict_level` 不得高于 `V1` |

**约束**
- `verdict_level=V0` 当且仅当 L1–L3 覆盖不全。
- `verdict_level≥V2` 要求 `l4.status=measured` 且 L4 评分者 κ ≥ 0.6。
- `verdict_level=V3` 要求存在用户侧证据实体（本规格 W1 明确不做，故预期**不可达**，脚本应断言 `V3` 不可达并在 rationale 中说明原因）。

---

## 状态流转

```text
PersonaClaim:  (录入) -> 标注 source_type -> 派生 evidence_level -> 校验 V1..V3 -> 定稿
HallucinationFinding:
    machine_flag=SUSPECT -> 人工 human_verdict      (主路径)
    machine_flag=OK/NA   -> 人工抽查 30% -> human_verdict
    PENDING 为 0 -> 允许进入 Verdict 汇总
Verdict:  coverage 全满 -> 自 V1 起算 -> 若 l4=measured 则 V2 -> V3 断言不可达
```

## 数据落盘清单

| 文件 | 实体 | 格式 |
| :--- | :--- | :--- |
| `reports/audit/persona_provenance.csv` | `PersonaClaim` | CSV (UTF-8 + BOM) |
| `reports/audit/requirement_persona_map.csv` | `RequirementMapping` | CSV (UTF-8 + BOM) |
| `reports/audit/l1_content_audit.csv` | `HallucinationFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/l2_attribution_audit.csv` | `AttributionFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/l3_leakage_audit.csv` | `LeakageFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/verdict.json` | `Verdict` | JSON (UTF-8, `ensure_ascii=False`, 2 空格缩进) |
| `reports/audit/online_baseline.csv` 或 `online_baseline.skipped.json` | L4 实验记录 | 二选一，**不允许两者都缺** |
