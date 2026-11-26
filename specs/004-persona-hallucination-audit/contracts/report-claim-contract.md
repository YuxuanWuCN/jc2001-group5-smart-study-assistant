# Report Claim Contract

**Feature ID**: `004-persona-hallucination-audit`
**Scope**: all Cycle 3 delivery text under `reports/` (`cycle3_master_plan.md` and every `cycle3_task_packs/*.md`)
**Nature**: this document is a "wording licence agreement", not a suggestion. Any sentence that cannot find a corresponding "supportable" row in this contract must not be written into the report.

---

## 1. Evidence-Source Register

| ID | Evidence source | Type | Scale | Owning file | Reproduction command |
| :-: | :--- | :--- | :--- | :--- | :--- |
| `EVID-MMLU` | MMLU 12-subject GraphRAG controlled comparison | offline empirical | n=4,445 | `graphrag_final/final_systematic_report.csv` | `python scripts/run_mmlu_eval.py` (historical script) |
| `EVID-PYTEST` | pytest test suite | regression baseline | 9 files / 145 cases | `tests/` | `python -m pytest tests/ -q` |
| `EVID-OFFLINE` | offline table-lookup fallback path | mechanistic fact | 12 questions | `backend/app/data/seed_questions.py` | `python scripts/audit_hallucination_l1_l3.py` |
| `EVID-L1` | L1 content hallucination audit | offline empirical | denominator 84 | `reports/audit/l1_content_audit.csv` | same as above |
| `EVID-L2` | L2 attribution hallucination audit | offline empirical | denominator 36 | `reports/audit/l2_attribution_audit.csv` | same as above |
| `EVID-L3` | L3 leakage hallucination audit | offline empirical | denominator 12 | `reports/audit/l3_leakage_audit.csv` | same as above |
| `EVID-L4` | online three-group comparison | online experiment (**may be skipped**) | N≥20 per cell | `reports/audit/online_baseline.csv` \| `online_baseline.skipped.json` | `python scripts/audit_online_baseline.py` |
| `EVID-PERSONA` | persona provenance audit | documentation audit | PA-01…PA-nn | `reports/audit/persona_provenance.csv` | `python scripts/audit_persona_claims.py` |

---

## 2. Forbidden Cross-Reference Matrix (hard constraint)

> How to read: row = the evidence you hold; "✅" = conclusion types this evidence may support; "⛔" = conclusion types it is strictly forbidden to support. Any ⛔ combination appearing in the report body or a defence presentation counts as an academic-integrity violation.

| Evidence ↓ \ Conclusion → | Improved answering accuracy | Reduced hallucination rate | Correct output content | System robust and does not crash | Improved learning outcomes | Real students benefit |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| `EVID-MMLU` (n=4,445) | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| `EVID-PYTEST` (145) | ⛔ | ⛔ | ⛔ | ✅ | ⛔ | ⛔ |
| `EVID-OFFLINE` (fallback) | ⛔ | ⛔ (especially "=0%") | ✅ only "this path's content is human-written" | ✅ | ⛔ | ⛔ |
| `EVID-L1`/`L2`/`L3` | ⛔ | ✅ **only for the offline deterministic path** | ✅ only for the audited objects | ⛔ | ⛔ | ⛔ |
| `EVID-L4` | ⛔ | ✅ only relative comparison under experimental conditions | ⛔ | ⛔ | ⛔ | ⛔ |
| `EVID-PERSONA` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ (can only support "persona dependence level") |

**The three most frequent pitfalls (guaranteed defence questions)**
1. `EVID-MMLU` → "reduced hallucination rate": MMLU measures "whether the right option was chosen"; hallucination measures "whether what was said is true". **Answering correctly but fabricating the explanation = hallucination; answering wrongly but honestly saying you do not know = no hallucination.** They are different constructs and cannot be interchanged.
2. `EVID-OFFLINE` → "hallucination rate 0%": the offline path has no generation surface, so by definition it cannot produce L4; recording "no generation" as "generated correctly" is a logical fallacy (a denominator of 0 does not constitute 0%).
3. `EVID-PYTEST` → "content is correct": `tests/test_empirical_stress.py:113-121` only asserts that `trap_name` is non-empty; a field having a value ≠ the field being true.

---

## 3. Wording Licence by Persona Evidence Level

| Level | Definition | **Permitted** wording | **Forbidden** wording |
| :-: | :--- | :--- | :--- |
| **E0** | pure construction, no external source whatsoever | "we **assume** the target user is…", "**we expect**…", "if this assumption holds, then…" | "users **need**…", "**data show**…", "research **indicates**…", "**typical** students…" |
| **E1** | secondary sources exist (literature / publicly observable competitor behaviour) | "according to the public material of XXX, **this group commonly**…", "competitor XXX offers this feature, **suggesting** the need exists" | "**our** users…", "during **interviews**, users mentioned…" |
| **E2** | informal verification among team members or classmates (n≈10) | "in an informal **within-team** verification with n=10, most members said… (**non-representative sample**)" | "**user feedback** shows…" (without stating the sample, this is a vague reference), "**research** confirmed…" |
| **E3** | representative sampling + explicit method (n≥8 semi-structured interviews, etc.) | may be stated directly, but **must** give n, sampling method, time and place | — (universal quantifiers such as "all users" remain forbidden) |

**Key rule**: the level is **per assertion**, not per persona. Within the same Persona A, "second-year student" (E1, checkable in the literature) and "will open the answer-sharing group in the two weeks before an exam" (E0, pure construction) must be labelled separately. **Giving a whole persona a single overall level is forbidden** - that amounts to using high-level assertions to vouch for low-level assertions.

---

## 4. External Wording Templates for Verdict Levels (V0–V3)

| Level | Trigger condition | One-sentence conclusion writable in the report (template) | What to acknowledge proactively at the defence |
| :-: | :--- | :--- | :--- |
| **V0** | L1–L3 coverage incomplete | "This project has **not yet** completed a measurement of hallucination; the existing accuracy and test results **cannot** be used to infer hallucination levels." | "We are currently not entitled to claim that hallucination was reduced." |
| **V1** | L1–L3 fully covered, L4 not measured | "On the offline deterministic path we audited all 84 option/trap factual assertions, 36 attribution mappings, and the guidance text of 12 questions, with error rates of x% / y% / z% respectively; **the hallucination rate of the online free-generation path was not measured**." | "V1 only covers 'the content we hard-coded', not 'the content the model makes up on the fly'." |
| **V2** | V1 + L4 three-group with Wilson CI, κ≥0.6 | "Relative to the unconstrained free-generation baseline, option-level constraints reduced the L4 hallucination point estimate from a to b (95% Wilson CI [..], [..]), with rater agreement κ=…." | "The experimental sample is N≥20 per cell; this is a **mechanistic difference demonstration** and does not represent real students' learning outcomes." |
| **V3** | V2 + user-side measurable benefit | may claim "a measurable benefit for real students" | explicitly out of scope under W1 of this specification, **currently unreachable** |

---

## 5. Banned-Word List (inherits and extends the existing list in `cycle3_master_plan.md`)

**Chinese-origin terms**: empower, closed loop, ecosystem, all-round, deep integration, significantly improve, in summary.
**English terms**: leverage, cutting-edge, seamlessly, revolutionise.

**New bans introduced by this contract (specific to the hallucination context)**:
| Banned wording | Reason | Replace with |
| :--- | :--- | :--- |
| "effectively reduces hallucination" | without a control there is no "reduction" | "the measured error rate on path X is y%" |
| "hallucination rate 0%" / "zero hallucination" | pseudo-conclusion when the denominator is 0 | "the offline path has no generation surface; L4 is recorded as N/A" |
| "fundamentally solves" | unfalsifiable | "coverage is 100% across layers L1–L3" |
| "verified that the design is correct" | no external standard | "the observed results for D1–D4 among the four falsifiable propositions are as shown in Table 6.6" |
| "significant" (for rate comparisons) | no statistical test performed on a small sample | give the Wilson CI and state whether the intervals overlap |
| "proves the AI is more trustworthy" | trustworthiness ≠ truthfulness | report L1/L2/L3/L4 separately |

---

## 6. Binding of the Audit Script Output to This Document

`scripts/audit_hallucination_l1_l3.py` and `scripts/audit_persona_claims.py` generate the `claim_matrix` field in `reports/audit/verdict.json`, whose content is **derived directly from sections 2 and 4 of this contract**:

```json
"claim_matrix": {
  "verdict_level": "V1",
  "allowed_sentences": [ "... (sentences filled into the section 4 templates)" ],
  "forbidden_sentences": [ "... (the ⛔ combinations derived from the section 2 matrix)" ],
  "banned_terms_found": []          // scans the report body for banned terms and returns hit locations
}
```

**Acceptance**: `banned_terms_found` must be an empty array; otherwise the script exits with code 0 but prints a `WARN` to stdout noting that manual revision is required (non-blocking, because the report body may be written after the audit script has run).
