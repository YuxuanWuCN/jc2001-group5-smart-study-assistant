# sources.md -- Repository Material Cited in Ch 5.3-5.4

> As required by the whole-group writing convention: this table lists the repository files behind every number and assertion in this chapter, and **every number must be traceable here**.
> Every entry in this table was opened and checked one by one on 2026-10-19.

## 1. Question Bank and Trap Data

| File | Purpose | Specific data cited in this chapter |
| :--- | :--- | :--- |
| `backend/app/data/seed_questions.py` | The single authoritative data source for the 12 questions and 36 traps (657 lines, collection variable `SEED_QUESTIONS`) | 12 questions; law/cs/econ/se 3 each; 36 traps (3 per question); difficulty distribution ★★★2/★★★★8/★★★★★2; `radar_hit` distribution boundary 12 / recall 8 / trapDefense 7 / synthesis 7 / precision 2; the `explanation` of 12/12 questions carries an `[Authoritative exam-point analysis]` source annotation |
| `backend/app/models/quiz.py` | Field definitions of `QuizItem` / `OptionItem` / `TrapDetail` / `GraphNode` / `GraphEdge` (181 lines) | The four `TrapDetail` fields `title` / `desc` / `prereq` / `radar_hit` (the basis of Table 5.5) |

## 2. Diagnostic Algorithm

| File | Purpose | Specific facts cited in this chapter |
| :--- | :--- | :--- |
| `backend/app/services/diagnostic_service.py` | Diagnostic engine implementation (274 lines) | Rule-based right/wrong judgement -> trap lookup -> dual mode (call the LLM if available, otherwise local fallback) -> global failsafe; an unknown question ID returns 200 + fallback rather than 404 |
| `backend/app/routers/diagnose.py` | The `POST /api/diagnose` route (no extra validation logic) | Basis for the pseudocode semantics: the router layer has no 404/422 branches; 422 comes only from request-body schema validation |
| `backend/app/services/llm_diagnostics.py` | LLM connectivity probing and failure classification (401 lines, PR #10 merged this cycle) | Source material for the 5.4.2 description of "LLM call failures are classified and degraded" |

## 3. Radar Aggregation (5.4.3, option B: frontend aggregation)

| File | Purpose | Specific data cited in this chapter |
| :--- | :--- | :--- |
| `frontend/app.js` | The live aggregation of the five-dimension radar within a session | Correct: `recall +4` / `trapDefense +5` / `synthesis +3` / `predictedScore +0.5`; wrong: `trapDefense -6` / `boundary -4`; clamping: dimension cap 100, wrong-path floor 30, `predictedScore` cap 99; initial baseline `recall 76 / boundary 62 / trapDefense 65 / synthesis 72 / precision 81`; the frontend does not consume the backend's `radar_dimension` / `score_delta` (0 references) |

## 4. Tests and Data Integrity

| File | Purpose | Specific data cited in this chapter |
| :--- | :--- | :--- |
| `tests/test_quiz.py` | Question-bank data-structure tests | 6 test cases |
| `tests/test_adversarial_backend.py` | Adversarial/boundary input tests | 25 test functions across 6 test classes |
| Full test suite | Used for Chapter 6 wording alignment | Measured with `pytest --collect-only`: **189** tests |

## 5. Graphics Sources

| Number | Source |
| :--- | :--- |
| Table 5.4 | Per-question summary of `backend/app/data/seed_questions.py` |
| Table 5.5 | The `TrapDetail` definition in `backend/app/models/quiz.py` + the real values of `law_1 / trap_law_1` |
| Table 5.6 | The discussion in this chapter (table lookup vs live LLM generation) |
| Figure 5.2 | Self-drawn causal chain (wrong option -> `trap_id` -> `TrapDetail` -> diagnosis drawer); source file `reports/figures/fig_trap_causal_chain.mmd`, vector `reports/figures/fig_trap_causal_chain.svg` (prefer the SVG when inserting into the report) |

## 5.1 Literature Cited in This Chapter (volume/issue/pages and DOI all checked against Crossref)

| Reference | Supports | Check result |
| :--- | :--- | :--- |
| VanLehn (2011), *Educational Psychologist* 46(4), 197-221 | Effectiveness of fine-grained feedback | ✅ vol/issue/pages/DOI all consistent |
| Corbett and Anderson (1994), *User Modeling and User-Adapted Interaction* 4(4), 253-278 | Independent accumulation of ability dimensions (knowledge tracing) | ⚠️ Crossref records the publication year as **1995**, while the literature most often cites 1994; before submission, follow the publisher page and be consistent throughout |
| Koedinger, Corbett and Perfetti (2012), *Cognitive Science* 36(5), 757-798 | Necessity of prerequisite knowledge for robust learning | ✅ consistent |
| Haladyna, Downing and Rodriguez (2002), *Applied Measurement in Education* 15(3), 309-333 | Item-writing convention that distractors must be explainable | ✅ consistent (DOI 10.1207/s15324818ame1503_5) |

## 6. Task Specifications and Conventions

| File | Purpose |
| :--- | :--- |
| `reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md` | This task package (structure, word count, pitfalls, three supervisor questions); 4 of its numbers do not match the code and have been corrected to the measured values |
| `reports/cycle3_task_packs/README.md` | Whole-group writing conventions (British spelling, Harvard, locked figure numbering, no pasted source code) |

## 7. Content Not Cited in This Chapter (important)

| Content | Reason |
| :--- | :--- |
| The "64% of the whole school", "58%", "71%" and "60% of the class" figures in the trap descriptions | No statistical source, which violates "every number must be traceable"; rewritten as "high-frequency error-prone points annotated from textbooks and syllabi" |
| The verbatim 🚨 emoji text of the trap `title` fields | Academic body text must rewrite it as a declarative sentence |
| `report_service.py` / `/api/reports/trend` / `reports/report_data_contract.md` | These do not exist in the repository; 5.4.3 now cites `frontend/app.js` as ruled by the team lead |
