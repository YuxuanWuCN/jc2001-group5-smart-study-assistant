# Quickstart: Running the Persona-Rationality and Hallucination Audit

**Feature ID**: `004-persona-hallucination-audit`
**Branch**: `004-persona-hallucination-audit`
**Target audience**: any team member (no prior understanding of the audit design required)
**Estimated time**: offline part < 30 minutes (including manual review); online part about 10 minutes (requires an API key)

> This file is a **verification guide**, not an implementation guide. It describes "once the audit scripts are written, how to confirm they have done the job correctly". Implementing the scripts themselves belongs to the `/speckit.tasks` + `/speckit.implement` phase.

---

## 0. Prerequisites

```powershell
# Run in the repository root D:\jc2001
git branch --show-current          # must be 004-persona-hallucination-audit
python --version                   # expected 3.13.x
python -c "import pandas; print(pandas.__version__)"   # expected 3.x, no new dependencies
```

**Hard constraints** (violation means failure):
- No new `requirements.txt` dependencies (NFR-5).
- No temporary files created in the repository root (NFR-4 / Constitution Principle V).

---

## 1. Offline Audit: L1–L3 from a Single Command

```powershell
python scripts/audit_hallucination_l1_l3.py
echo $LASTEXITCODE     # expected 0
```

**Expected outputs** (all under `reports/audit/`):

| File | Assertion |
| :--- | :--- |
| `l1_content_audit.csv` | row count = **84** (48 options + 36 traps) |
| `l2_attribution_audit.csv` | row count = **36** |
| `l3_leakage_audit.csv` | row count = **12** |
| `verdict.json` | passes validation against `contracts/audit-result.schema.json`; `determinism_check.identical == true` |

**Acceptance checks**

1. **The denominator must not shrink**: if the `l1` row count is less than 84, some entries were silently skipped - this is the most serious failure mode, because a shrunken denominator makes the error rate look better. The script must **raise an error and exit**, not skip.
2. **UNDECIDABLE stays in the denominator**: spot-check any row with `human_verdict=UNDECIDABLE` and confirm `is_in_denominator=true`.
3. **No generation surface offline**: `l4.status` in `verdict.json` must be `na_no_generation_face`, and `l4.rate` must be `null` (**not 0**). Confirm with:

```powershell
python -c "import json;v=json.load(open('reports/audit/verdict.json',encoding='utf-8'));print(v['l4'])"
# {'layer': 'L4_reasoning', 'denominator': 0, 'numerator': 0, 'rate': None, 'coverage': 1.0, 'status': 'na_no_generation_face'}
```

4. **Reproducibility**:
```powershell
python scripts/audit_hallucination_l1_l3.py
python -c "import json;print(json.load(open('reports/audit/verdict.json',encoding='utf-8'))['determinism_check'])"
# identical must be True, with both hashes matching
```

---

## 2. Persona Provenance Audit

```powershell
python scripts/audit_persona_claims.py
echo $LASTEXITCODE     # expected 0
```

**Expected outputs**: `reports/audit/persona_provenance.csv`, `reports/audit/requirement_persona_map.csv`

**Acceptance checks**

1. **All three personas covered**: at least one "pain point" assertion is labelled for each persona, with the `persona` column taking values `A_EXAM_CRAMMER` / `B_SYSTEMATIC_REVIEWER` / `C_COURSE_TEACHER`.
2. **E0 must have no source**: filter rows with `evidence_level=E0`; `source_locator` should be empty; filter rows with `source_type=no_source`; `evidence_level` must be `E0` (consistent in both directions).
3. **Circular-argument detection works**: `requirement_persona_map.csv` should contain at least one requirement, R09 or R10, marked `assumption_driven=true` with a non-empty `external_falsifiable_claim`.
4. **Manual backfill**: rows with `human_verdict=PENDING` must be filled in one by one by a human - the audit script performs machine pre-screening only and **must not** automatically treat PENDING as TRUE.

> This step is the **most time-consuming** part of the whole audit (estimated 1–2 hours per person). Suggested approach: first look only at rows with `machine_flag=SUSPECT` (expected to be far fewer than 84), then spot-check 30% of the rest.

---

## 3. Online Controlled Experiment (optional)

```powershell
# Without a key: should print a clear message and exit with code 0
python scripts/audit_online_baseline.py
echo $LASTEXITCODE     # expected 0 (not 1)
cat reports/audit/online_baseline.skipped.json
```

```powershell
# With a key
$env:QWEN_API_KEY = "<your key>"
python scripts/audit_online_baseline.py
echo $LASTEXITCODE     # expected 0
```

**Acceptance checks**

1. **Skipping is a legitimate state**: without a key there must be **no** network requests and **no** error exit.
2. **Three groups paired**: the `group` column of `online_baseline.csv` must contain both `A_free_generation` and `C_graph_constrained`. The presence of group A alone means the B/C grouping did not take effect.
3. **N ≥ 20 per cell**:
```powershell
python -c "import pandas as p;d=p.read_csv('reports/audit/online_baseline.csv');print(d.groupby('group').size())"
```
4. **Intervals use Wilson**: `l4.ci_method` in `verdict.json` must be `'wilson_95'`.
5. **κ check**: if `l4.status == 'skipped'` and the note contains `rater_agreement_below_threshold`, the raters were insufficiently trained - retrain and rerun; **do not** bend the criteria to fit the data.

---

## 4. Regression Verification (ensure zero breakage)

```powershell
python -m pytest tests/ -q
# expected: 145 passed (consistent with Table 6.1)
```

**Note**: the audit scripts **must not** be added to `tests/`. The case count in `tests/` is an established fact in the report (Table 6.1); adding files there would invalidate the number 145 and thereby conflict with `07-ch6-testing-yang-mingjie.md`. Audit scripts go in `scripts/` and are verified by exit code (see the structural decision in `plan.md`).

---

## 5. How to Use the Results

Open `reports/audit/verdict.json` and read `verdict_level` first:

| Level | Sentences you may write now | What you still may not write |
| :-: | :--- | :--- |
| **V0** | "hallucination measurement not yet complete" | any "reduction" |
| **V1** | "on the offline deterministic path the L1/L2/L3 error rates are x/y/z" | the hallucination rate of online free generation |
| **V2** | "relative to the free-generation baseline, the L4 point estimate on the constrained path drops from a to b (CI …)" | real students' learning outcomes |
| **V3** | — (Won't in this specification; should not appear) | — |

**Required reading before writing**: the forbidden cross-reference matrix in section 2 of [`contracts/report-claim-contract.md`](contracts/report-claim-contract.md). Three pitfalls that will definitely be asked about: MMLU ≠ hallucination, offline ≠ 0%, 145 cases ≠ correct content.

---

## 6. Common Failures and Remedies

| Symptom | Cause | Remedy |
| :--- | :--- | :--- |
| `l1_content_audit.csv` row count < 84 | some question lacks `traps` or was silently skipped | fix the script so it **raises an error**; skipping is not allowed |
| `l4.rate == 0` | "no generation surface" was written as 0% | change to `rate: null, status: na_no_generation_face` |
| `determinism_check.identical == false` | timestamps / random ordering leaked into the results | hash only the data rows, excluding `timestamp_utc` |
| Two runs differ in `git_commit` | a commit happened between the runs | rerun under the same commit |
| `pytest` goes from 145 to 146 | the audit script was placed under `tests/` | move it out to `scripts/` |
| Banned words hit in the report body | "effectively reduces hallucination" was used while writing | replace per section 5 of the contract |
