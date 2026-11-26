# Data Model: Audit Entities and Result Contracts

**Feature ID**: `004-persona-hallucination-audit`
**Date**: 2026-10-18
**Upstream**: [spec.md](spec.md) §4 definitions · [research.md](research.md) decisions 1/2/3/5
**Status**: PHASE 1 OUTPUT

This document defines the fields, value domains and required-field rules of the **six entities** in the audit outputs. All entities are ultimately serialised into CSV/JSON under `reports/audit/`; the field names are the contract names (the schemas in `contracts/` take these as authoritative).

---

## 1. `PersonaClaim` (persona assertion)

One judgeable assertion in Table 1.3 (`reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:76-84`).

| Field | Type | Required | Value domain / rule |
| :--- | :--- | :-: | :--- |
| `claim_id` | string | ✅ | `PA-01` … `PA-nn`, stable and never reused |
| `persona` | enum | ✅ | `A_EXAM_CRAMMER` / `B_SYSTEMATIC_REVIEWER` / `C_COURSE_TEACHER` |
| `claim_text` | string | ✅ | Verbatim excerpt of the assertion (≤80 characters) that must be traceable to a source line number |
| `claim_kind` | enum | ✅ | `identity` / `current_tools` / `pain_point` / `expectation` / `is_target_user` |
| `source_type` | enum | ✅ | `literature` / `competitor_behaviour` / `team_discussion` / `no_source` |
| `source_locator` | string | ⚠️ | May be empty when `source_type=no_source`; otherwise it must be a `file:line` reference or a literature entry |
| `evidence_level` | enum | ✅ | `E0` / `E1` / `E2` / `E3` (see spec §4.1) |
| `is_core` | bool | ✅ | Whether it is the persona's **core pain point / expectation** (this triggers the decision rule in spec §4.1) |
| `allowed_usage` | string | ✅ | Derived automatically from `evidence_level`; manual overriding is forbidden |
| `auditor` | string | ✅ | Name of the team member who performed the audit + date |

**Validation Rules**
- V1: `evidence_level=E0` ⟺ `source_type=no_source` (both directions).
- V2: if `is_core=true` and `evidence_level ∈ {E0}`, ⟹ the assertion must not appear in the "basis" column of any SMART goal (Table 1.2) or MoSCoW requirement (Table 2.2). The audit script must cross-check and output a list of violations.
- V3: `evidence_level=E3` must carry a sample description (n, sampling method), otherwise the script refuses to write to disk.

---

## 2. `RequirementMapping` (requirement-persona mapping)

The mapping of the 14 MoSCoW requirements (R01–R14) in Ch2 to personas / pain points / hallucination layers.

| Field | Type | Required | Value domain / rule |
| :--- | :--- | :-: | :--- |
| `requirement_id` | string | ✅ | `R01` … `R14`, **verbatim identical to Ch2 Table 2.2** |
| `requirement_text` | string | ✅ | Excerpt, not rewritten |
| `moscow` | enum | ✅ | `Must` / `Should` / `Could` / `Won't` |
| `served_personas` | string[] | ✅ | `[A]` / `[A,B]` / `[]` (an empty array requires `gap_reason`) |
| `served_pain_points` | string[] | ✅ | References `PersonaClaim.claim_id` |
| `assumption_driven` | bool | ✅ | Whether its basis comes from an E0/E1 assertion |
| `hallucination_layers` | enum[] | ✅ | Which `L1..L4` layers this requirement mainly constrains; use `[]` if unrelated |
| `external_falsifiable_claim` | string | ⚠️ | Required when `assumption_driven=true`: the rewritten falsifiable proposition |
| `gap_reason` | string | ⚠️ | Required when `served_personas` is empty |

**Validation Rules**
- V4: if `served_personas` is empty ⟹ `moscow ∈ {Could, Won't}`; otherwise report a "Must feature with no persona support" violation (expected hit: R10 needs re-judging).
- V5: every `claim_id` appearing in `served_pain_points` must exist in the `PersonaClaim` table (foreign-key integrity).

---

## 3. `HallucinationFinding` (L1 content audit item)

| Field | Type | Required | Value domain / rule |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L1-<question_id>-<option_key>` or `L1-<question_id>-<trap_id>` |
| `question_id` | string | ✅ | `law_1` … `se_3` |
| `subject` | enum | ✅ | `law` / `cs` / `econ` / `se` |
| `artifact_kind` | enum | ✅ | `option_text` / `correct_flag` / `trap_title` / `trap_desc` / `trap_prereq` / `graph_node` / `graph_edge` |
| `artifact_ref` | string | ✅ | Concrete object identifier (`option_key`, `trap_id`, or `node_id`) |
| `claim_under_test` | string | ✅ | The subject-matter proposition under test (e.g. "the exclusion period in Article 152 of the Civil Code runs for 1 year from the date of knowledge") |
| `machine_flag` | enum | ✅ | `OK` / `SUSPECT` / `NA` (machine pre-screening conclusion) |
| `machine_reason` | string | ⚠️ | Required when `machine_flag=SUSPECT` |
| `human_verdict` | enum | ✅ | `TRUE` / `FALSE` / `UNDECIDABLE` / `PENDING` |
| `human_note` | string | ⚠️ | Required when `human_verdict ∈ {FALSE, UNDECIDABLE}` |
| `is_in_denominator` | bool | ✅ | `UNDECIDABLE` items still **stay in the denominator** (research decision 1); only entries whose `artifact_kind` does not constitute a factual assertion may be set to `false` |
| `reviewer` | string | ⚠️ | Required when `human_verdict != PENDING` |

**Aggregate Output (written to `verdict.json`)**
```
L1.denominator = count(is_in_denominator = true)          # expected 84 (48 options + 36 traps)
L1.false_count = count(human_verdict = FALSE)
L1.undecidable = count(human_verdict = UNDECIDABLE)
L1.rate        = false_count / denominator
L1.coverage    = count(human_verdict != PENDING) / denominator   # must = 1.0 before any L1 conclusion may be claimed
```

---

## 4. `AttributionFinding` (L2 attribution audit item)

| Field | Type | Required | Value domain / rule |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L2-<question_id>-<trap_id>` |
| `option_key` | string | ✅ | The distractor to which this trap is attached |
| `trap_name` | string | ✅ | `TrapDetail.title` |
| `misconception` | string | ✅ | The **plausible student misconception** described by `TrapDetail.desc`, which must be normalised into a short label |
| `duplicate_group` | string | ⚠️ | If two different `option_key` values within the same question normalise to the **same** `misconception` label, fill in that label |
| `distinguishable` | bool | ✅ | `true` when `duplicate_group` is empty |
| `human_verdict` | enum | ✅ | `CONSISTENT` / `INCONSISTENT` / `PENDING` |

**Validation Rules**
- V6: entries with `distinguishable=false` count towards the L2 numerator (indistinguishable attribution = attribution hallucination).
- V7: an L2 conclusion may be claimed only when the number of `human_verdict=PENDING` entries is 0.

---

## 5. `LeakageFinding` (L3 leakage audit item)

| Field | Type | Required | Value domain / rule |
| :--- | :--- | :-: | :--- |
| `finding_id` | string | ✅ | `L3-<question_id>` |
| `correct_option_key` | string | ✅ | The correct option |
| `answer_entities` | string[] | ✅ | Key entities extracted from the correct-option text (numbers / article numbers / proper terms) |
| `guidance_field` | enum | ✅ | `socratic_prompt` / `trap_hint` / `explanation` |
| `leaked_entities` | string[] | ✅ | Entities that appear in the guidance field |
| `is_leak` | bool | ✅ | Rule: `true` when `leaked_entities` covers **all** `answer_entities` (partial matches are recorded as `partial` but do not count as leakage) |
| `detector_precision_note` | string | ⚠️ | Required when `is_leak=true`; explains why this is not a "legitimate knowledge reference" (sources of false positives must be explicitly recorded, see US-03 acceptance 2) |
| `human_verdict` | enum | ✅ | `CONFIRMED_LEAK` / `FALSE_POSITIVE` / `PENDING` |

**Validation Rules**
- V8: entries with `human_verdict=FALSE_POSITIVE` stay in the CSV (so the audit remains re-checkable) but do not count towards the L3 numerator.
- V9: denominator = 12 (one per question); if any question is missing the script must raise an error.

---

## 6. `Verdict` (verdict entity → `reports/audit/verdict.json`)

| Field | Type | Required | Description |
| :--- | :--- | :-: | :--- |
| `verdict_level` | enum | ✅ | `V0` / `V1` / `V2` / `V3` (spec §4.3; must be derived automatically from evidence, never filled in by hand) |
| `verdict_rationale` | string | ✅ | One paragraph explaining why this level was reached |
| `persona_level_min` | enum | ✅ | The worst evidence level among the core pain points of the three Personas |
| `l1` / `l2` / `l3` / `l4` | object | ✅ | Each `{denominator, numerator, rate, coverage, status}`; `l4.status ∈ {measured, skipped, na_no_generation_face}` |
| `claim_matrix` | object | ✅ | The "sentences allowed / sentences forbidden" derived from `contracts/report-claim-contract.md` |
| `env_fingerprint` | object | ✅ | `python_version`, `pandas_version`, `git_commit`, `branch`, `timestamp_utc`, `host_os` |
| `determinism_check` | object | ✅ | `run_1_hash`, `run_2_hash`, `identical: bool` (must be `true`) |
| `outstanding_reviews` | string[] | ✅ | List of all `PENDING` entries; when non-empty, `verdict_level` must not be higher than `V1` |

**Constraints**
- `verdict_level=V0` if and only if L1–L3 coverage is incomplete.
- `verdict_level≥V2` requires `l4.status=measured` and L4 rater κ ≥ 0.6.
- `verdict_level=V3` requires a user-side evidence entity (explicitly out of scope under W1 of this specification, so it is expected to be **unreachable**; the script should assert that `V3` is unreachable and explain why in the rationale).

---

## State Transitions

```text
PersonaClaim:  (entry) -> annotate source_type -> derive evidence_level -> validate V1..V3 -> finalise
HallucinationFinding:
    machine_flag=SUSPECT -> human human_verdict      (main path)
    machine_flag=OK/NA   -> human 30% spot-check -> human_verdict
    PENDING count 0 -> allowed into Verdict aggregation
Verdict:  coverage full -> count from V1 upwards -> if l4=measured then V2 -> assert V3 unreachable
```

## Data Persistence Inventory

| File | Entity | Format |
| :--- | :--- | :--- |
| `reports/audit/persona_provenance.csv` | `PersonaClaim` | CSV (UTF-8 + BOM) |
| `reports/audit/requirement_persona_map.csv` | `RequirementMapping` | CSV (UTF-8 + BOM) |
| `reports/audit/l1_content_audit.csv` | `HallucinationFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/l2_attribution_audit.csv` | `AttributionFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/l3_leakage_audit.csv` | `LeakageFinding` | CSV (UTF-8 + BOM) |
| `reports/audit/verdict.json` | `Verdict` | JSON (UTF-8, `ensure_ascii=False`, 2-space indent) |
| `reports/audit/online_baseline.csv` or `online_baseline.skipped.json` | L4 experiment record | one of the two; **both missing is not allowed** |
