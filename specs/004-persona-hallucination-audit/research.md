# Technical Research and Architecture Decisions: Persona Rationality Audit and Empirical Grounding of the Hallucination Claim

**Feature ID**: `004-persona-hallucination-audit`
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)
**Date**: 2026-10-18
**Status**: COMPLETED / READY FOR PHASE 1
**Input**: the "needs clarification" items in `specs/004-persona-hallucination-audit/spec.md` - the user's core question in m00001 is "**has it actually succeeded in reducing the probability of AI hallucination**", yet the repository has neither an operational definition of "hallucination" nor any single measurement of it, and also lacks a design-rationality argument that still holds under the premise that "the persona is a constructed assumption". This section resolves each item in turn.

---

## Decision 1: Lock the measurement target of "hallucination rate" to a finite, judgeable set rather than free text

- **Decision**: adopt the four-level taxonomy of spec §4.2, **report the numerator/denominator of each level separately**, and **do not merge them into a single "hallucination rate"**:

  | Layer | Numerator (number of erroneous items) | Denominator (number of judgeable items) | Judgement method | Offline-judgeable |
  | :-: | :--- | :--- | :--- | :-: |
  | **L1 content hallucination** | items where the option text / correct-answer flag / `TrapDetail.desc` / `prereq` disagrees with subject-matter facts | all 48 options + 36 traps = **84** | manual item-by-item judgement (machine pre-screens high-suspicion items) | ✅ |
  | **L2 attribution hallucination** | items where two options that semantically point to **different misconceptions** are mapped to the **same** `trap_name`, or where the trap title disagrees with the option's actual misconception | 36 trap mappings | rule-based detection + manual spot-checks | ✅ |
  | **L3 leakage hallucination** | questions where the correct option's **key entities** (key numbers / terms) appear in `socratic_guidance` / `trap_hint` | 12 questions | regex entity extraction + manual double judgement | ✅ |
  | **L4 reasoning hallucination** | samples in the online LLM path's output that contain untrue statements | by experimental sample size N (≥20 per cell) | ≥2 raters, independent and double-blind | ❌ requires an API key |

- **Rationale**:
  1. **The denominator must be explicit**. The repository's existing test style (`assert validated.trap_name is not None and len(validated.trap_name) > 0`, see `tests/test_empirical_stress.py:113-121`) only proves that a field is "non-empty", **it can never detect a problem** and can never compute a rate. The audit must adopt a different accounting method.
  2. **The L1–L3 denominators are 84 / 36 / 12, small enough for full manual coverage - this is the only structural advantage of a 12-question PoC** and must be fully exploited; unlike large-model benchmarks, sampling must not be used to hide individual errors.
  3. **L4 is a separate layer**, because it is the only layer that needs a network, an API key, and rater agreement. Mixing it with L1–L3 would pollute the framing so that "partially finished" counts as "finished".
  4. Make explicit that **"turning the LLM off" is not reducing hallucination but avoiding one layer of it**: in offline mode the system uses `fallback_mode=True` (`tests/test_empirical_stress.py:162`), at which point L4's generation surface does not exist at all, so the offline path's L4 rate is by definition recorded as `N/A (no generation surface)` and **must not be recorded as 0%**. Recording 0% would produce the absurd conclusion "our hallucination rate is 0%".

- **Alternatives considered**:
  - *Use one composite "hallucination rate" indicator*: rejected. The four levels have different denominators (84 / 36 / 12 / N); a weighted sum necessarily introduces subjective weights and collapses at the first defence question.
  - *Measure only L4 (because "hallucination" intuitively means LLM)*: rejected. This is exactly the current framing misalignment in the repository - the system's strongest evidential layer is L1–L3; measuring only the least provable layer while leaving the provable ones unmeasured is needlessly disarming oneself.
  - *LLM-as-a-judge automatic scoring for L4*: rejected. The judge model is itself a hallucination source; "using an LLM to judge whether an LLM hallucinates" cannot be self-justified at the same defence table; it also introduces an API dependency, violating NFR-2.

---

## Decision 2: Use "evidence levels + sentence-level binding" for personas, rather than conducting new research or pretending the personas hold

- **Decision**: do not run a new questionnaire (the cycle does not allow it); instead label every assertion in Table 1.3 with an E0–E3 level and bind the level to the **wording permitted in the report** for that assertion (see `contracts/report-claim-contract.md`). Decision rules are in spec §4.1.

- **Rationale**:
  1. The repository **already admits** that the personas are inferred (`reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md:50`: "Persona is inferred from literature and competitor behaviour, not based on a measured user persona"), and an honest defence position already exists (`reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:183`). The audit's job is not to erase this admission but to **turn it into a structural strength of the report**: a report that clearly states "this is an assumption, and here is how we would falsify it" is harder to attack than one pretending that research was done.
  2. **The level system prevents blanket exculpation**. If the report only says "personas were not measured", every conclusion that depends on personas is invalidated at once; sentence-level binding invalidates only the sentences that genuinely depend on E0/E1 assertions, leaving the rest of the argument (mechanism, economics, falsifiability) intact.
  3. The supplementary plan must still be written (spec FR-1.3's minimal plan: n=8–12 semi-structured interviews + a 12-item online questionnaire) and placed under Future Work rather than pretending it was done - this is isomorphic to the integrity red line in `07-ch6-testing-yang-mingjie.md:111`.

- **Alternatives considered**:
  - *Conduct a real questionnaire within two weeks*: rejected. Sample representativeness is insufficient (n<30, most likely classmates from the same programme), producing data that is "E2 but feels like E3", which is more dangerous than honestly labelling it E1.
  - *Delete the personas and describe "generic university students"*: rejected. The official Brief mandates `intended users or stakeholders` (see `01-ch1-introduction-lin-yongtong.md:11`); deleting them loses marks directly.
  - *Also write Persona C (teacher) as a target user*: rejected. This conflicts with the Ch2 R11–R14 Won't decision (`09-ch3-use-cases-xie-weixin.md:32`) and would create cross-chapter contradictions.

---

## Decision 3: Split design rationality into four external propositions, each with "what observation would overturn it"

- **Decision**: abandon the one-way "persona → design" proof and replace it with four propositions that **do not depend on a measured persona** and are **each falsifiable**:

  | Dimension | Proposition (falsifiable) | Overturning condition | Current evidence in this project |
  | :-: | :--- | :--- | :--- |
  | **D1 construct validity** | the 36 trap names correspond to **conceptual boundary confusions that genuinely exist within the subject**, not arbitrarily invented distractors | if any trap's "misconception" is not a common error in any mainstream textbook/precedent, that entry is fabricated | trap material can be traced to textbook article numbers (e.g. "Article 152 exclusion period / Article 188 limitation period") and standard CS/economics textbook concepts → **each must be given a citation individually** |
  | **D2 mechanism effectiveness** | option-level lookup places answer determination **before** any free generation, so L4's generation surface does not exist on the offline path | if any field in the diagnostic response depends on LLM free generation, then "eliminating the generation surface" does not hold | the `fallback_mode=True` response path is entirely constructed by `SEED_QUESTIONS` lookup → mechanism holds |
  | **D3 economics** | marginal inference cost 0 and offline operation constitute a practical advantage for the scenario of "2 weeks before exams, unstable network, scarce time" | if target users are in fact always online and LLMs are free, then the advantage provides no differentiation | competitor matrix (`01-ch1-introduction-lin-yongtong.md:54-61`) shows generic LLMs depend on the network and spoil answers |
  | **D4 honesty** | the system gives an explicit empty state when no answer path exists, instead of fabricating a diagnosis | if an unknown `question_id` returns 200 with a fabricated trap attribution, then the claim is overturned | `tests/test_empirical_stress.py:167-177` allows 404/422/200; it is necessary to **manually confirm that the 200 branch carries no fabricated attribution** |

- **Rationale**: these four form an argument chain **that does not depend on the personas being real** - even if the personas were entirely made up, D1 (are the traps real) and D2 (does the generation surface exist) can still be verified independently; D3 needs only competitor facts; D4 needs only one response check. **This is far stronger than the circular chain "the persona says students need it → we built it → therefore the design is reasonable", and every item's evidence can be opened on the spot during the defence.**

- **Alternatives considered**:
  - *Score "rationality" with SUS / TAM questionnaires*: rejected. It needs real users, which the cycle does not allow; and user satisfaction does not answer "was hallucination reduced".
  - *Use a literature review supporting "option-level feedback is effective" as proof of rationality*: rejected. The literature proves **general** conclusions (VanLehn 2011 etc.) and cannot be transferred directly to the correctness of this system's **specific implementation**; the literature can support D1's necessity but cannot substitute for the evidence of D1–D4.

---

## Decision 4: Make the online controlled experiment a first-class skippable citizen; use Wilson score intervals for confidence intervals

- **Decision**: `scripts/audit_online_baseline.py` uses three groups (A original Qwen free generation / B offline lookup / C graph-constrained + lookup), with N ≥ 20 samples per cell. When `QWEN_API_KEY` is absent it **writes `online_baseline.skipped.json` with exit code 0** (containing `reason`, `timestamp`, `env_fingerprint`) and does not treat this as a failure. All rate-type metrics use the **Wilson score interval (95%)**, never the normal approximation.

- **Rationale**:
  1. **With small samples and extreme rates** (e.g. "0 hallucinations out of 20"), the normal approximation gives intervals that go out of bounds (a negative lower bound or an upper bound >100%), whereas the Wilson interval remains well behaved when p is near 0/1 and n is small - exactly this project's situation.
  2. **A missing key is the norm, not an anomaly**: the repository's history already contains a DashScope cloud chain (`ORIGINAL_REQUEST.md` R3), while the project's main selling point is precisely that it runs offline. If the script hard-failed without a key, that would amount to requiring the audit to be completed in a networked environment - self-contradictory.
  3. Rater agreement uses **Cohen's κ**; when κ < 0.6 no point estimate is reported, only "raters disagree, so the conclusion does not hold" - preventing two team members from each judging L4 according to their own standard to get a preferred result.

- **Alternatives considered**:
  - *Treat MMLU's 4,445 accuracy records as the "hallucination rate"*: rejected (D-06). Accuracy measures "was it answered correctly"; hallucination measures "is what was said true"; an incorrectly answered question with an honest explanation is not hallucination, while a correctly answered question with a fabricated explanation is. The two are not interchangeable constructs.
  - *Single-group before/after comparison (measure before and after turning the LLM off)*: rejected. Without the free-generation baseline (group A), the word "reduction" has no reference point.
  - *Use bootstrap intervals*: a possible fallback, but n is very small and reproducibility would require implementing a random seed; Wilson is simpler and analytically reproducible.

---

## Decision 5: The audit outputs only "append" table numbers and never reorder the existing 17 figures / 21 tables

- **Decision**: `reports/cycle3_master_plan.md` has already allocated 17 figures / 21 tables whose numbers are cross-referenced between chapters (e.g. Table 1.3 is referenced from Ch2, Table 2.2 must match Table 6.5 verbatim). All tables from this audit are numbered by **suffix appending**: `Table 6.6 Hallucination taxonomy and measured rates`, `Table 1.4 Persona evidence levels`, `Table 6.7 Online vs offline baseline` (if the experiment is completed). Existing numbers of the 21 tables **do not change at all**.

- **Rationale**: `01-ch1-introduction-lin-yongtong.md:10` and `07-ch6-testing-yang-mingjie.md:210` both state explicitly that numbers "cannot change once issued" and that "IDs and wording must match verbatim". Reordering would invalidate all ten members' drafts.

- **Alternatives considered**:
  - *Cram the hallucination table into an extra column of Table 6.3*: rejected. It would create the implication "MMLU up = hallucination down", exactly the construct confusion that D-06 forbids.
  - *Open a new Chapter 8*: rejected. The official Brief has a fixed seven-chapter structure.

---

## Decision 6: Draw hard boundaries with existing evidence - accuracy, robustness and hallucination must not cite each other

- **Decision**: write a "forbidden cross-reference matrix" into the contract file `contracts/report-claim-contract.md`:

  | Evidence source | Can support | **Strictly forbidden** to support |
  | :--- | :--- | :--- |
  | MMLU Δ (`graphrag_final/final_systematic_report.csv`, n=4,445, 7 positive/3 neutral/2 negative) | "graph augmentation improved answering accuracy in some subjects" | "reduced hallucination" |
  | 145 pytest cases | "a regression baseline exists; endpoints do not crash under adversarial input" | "output content is correct", "hallucination rate is low" |
  | `fallback_mode=True` / offline demo | "the demo has no external dependency" | "hallucination rate 0%" |
  | this L1–L3 audit (84/36/12 denominators) | "on the offline deterministic path the L1–L3 error rates are x%/y%/z%" | "improved learning outcomes" |
  | this L4 experiment (if completed) | "relative to the free-generation baseline, the L4 point estimate is a→b (95% CI)" | "effective on real students" |

- **Rationale**: a symptom has already appeared around `reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md:50` - treating the 145 tests as evidence that "the system is correct", while the defence position at line 187 of the same file honestly says "it does not show the system is correct, only that a regression baseline exists". **Having two framings in the same report is an internal contradiction**; the audit must make that contradiction explicit and unify both framings onto the latter.

- **Alternatives considered**:
  - *Keep vague wording and clarify orally at the defence*: rejected. The examiner can simply quote the written report's self-contradiction back at you.
