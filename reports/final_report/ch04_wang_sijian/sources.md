# Chapter 4 — Sources and Evidence Register

**Owner:** 王思鉴 (50106045) · Chapter 4 System Design and Architecture
**Baseline:** `develop` @ `626d467`
**Purpose:** every number, figure and factual claim in the chapter must be traceable to a file. This register is the audit trail.

---

## 1. Code references cited in the chapter

| Section | Claim | Source file |
| :--- | :--- | :--- |
| 4.1.1 | Four-layer structure; routers under `/api`; `StaticFiles` mounted at root | `backend/app/main.py` |
| 4.1.1 | Layer 4 is a read-only module of 657 lines | `backend/app/data/seed_questions.py` |
| 4.1.1 | Same-origin deployment removes CORS from the production path | `backend/app/main.py` (`StaticFiles` mount), AD-6 |
| 4.1.2 | Layering discipline: routers → services → models | `backend/app/routers/`, `services/`, `models/` |
| 4.1.3 | Three routers, three services, three model modules | directory listing, Table 4.2 |
| 4.1.3 | LLM health probe classifies failures | `backend/app/services/llm_diagnostics.py` |
| 4.2.1 | Neo4j confined to the offline path | AD-5; `graphrag（终）/real_graph_engine.py` is not imported by `backend/app` |
| 4.2.2 | Diagnosis is a lookup, not an inference | `backend/app/services/diagnostic_service.py` lines 96–246 |
| 4.2.2 | Model call sits after the verdict, gated by key presence and timeout | `diagnostic_service.py` lines 202–225; `config.py` lines 23–29 |
| 4.3.1 | Four classes and their cardinalities | `backend/app/models/quiz.py` |
| 4.3.1 | 5 radar dimensions: recall, boundary, trapDefense, synthesis, precision | `seed_questions.py` (`radar_hit` values); `frontend/app.js` lines 1250–1254 |
| 4.4 | All seven decisions | `table_4_1_adr.md`, which carries its own source anchors |
| 4.5.1 | Start-up order: CORS → routers → static mount | `backend/app/main.py` lines 32–55 |
| 4.5.1 | Dual snake_case / camelCase serialisation | `backend/app/models/common.py` (`CamelModel`) |
| 4.5.2 | Three fallback exits, no 500 | `diagnostic_service.py` lines 107–128, 248–270 |
| 4.5.2 | Live probe never raises | `llm_diagnostics.py` lines 314–401 |
| 4.6 | Security posture: no auth, no origin restriction | `backend/app/main.py` lines 33–40; AD-6, AD-7 |

---

## 2. Measured numbers

All values below were measured on this working copy, not restated from any planning document.

### 2.1 Content set (AST count of constructor calls in `seed_questions.py`)

| Quantity | Value | Method |
| :--- | :--- | :--- |
| Question items | 12 | count of `QuizItem(` |
| Options | 48 | count of `OptionItem(` |
| Traps | 36 | count of `TrapDetail(` |
| Graph nodes | 60 | count of `GraphNode(` |
| Subjects | 4 (law, cs, econ, se) | distinct `subject` values |
| Radar dimensions | 5 | distinct `radar_hit` values |

### 2.2 Diagnostics latency

**Deterministic core** — question lookup, option resolution, trap lookup. Measured over 720 samples drawn from the 36 authored wrong-answer cases, after 200 warm-up iterations.

| Metric | Value |
| :--- | :--- |
| Median | 0.0006 ms (0.6 µs) |
| Mean | 0.0006 ms |
| p95 | 0.0007 ms |
| p99 | 0.0007 ms |
| Max | 0.0015 ms |

**End-to-end over HTTP** — local `uvicorn`, single worker, `POST /api/diagnose`, 200 iterations after 20 warm-up calls.

| Metric | `GET /api/quiz` | `POST /api/diagnose` |
| :--- | ---: | ---: |
| Median | 12.180 ms | 1.533 ms |
| Mean | 9.068 ms | 7.815 ms |
| p95 | 19.762 ms | 15.979 ms |
| p99 | 26.095 ms | 26.024 ms |
| Max | 27.368 ms | 27.071 ms |

> **How to quote these.** The chapter reports the median pair (0.6 µs algorithm, 1.5 ms request) and attributes the gap to framework and transport overhead. Do **not** quote "p95 < 5 ms" as a measured figure: the measured p95 for the HTTP path is 16 ms on this machine. The sub-5 ms claim appears in the task pack and in Chapter 5.4; if it is retained there, it must be re-measured on the machine that will be used for the demonstration, and the measurement conditions stated.

### 2.3 Infrastructure counts

| Quantity | Value | Method |
| :--- | :--- | :--- |
| Routers | 3 | files in `backend/app/routers/` excluding `__init__.py` |
| Endpoints | 4 | `@router` decorators |
| Services | 3 | files in `backend/app/services/` excluding `__init__.py` |
| Model modules | 3 | files in `backend/app/models/` excluding `__init__.py` |
| LLM timeout | 4.0 s | `config.py` line 29 |
| Default model | `qwen-turbo` | `config.py` line 28 |

---

## 3. Figures and tables

| Number | Source | Export | Size (px @2×) |
| :--- | :--- | :--- | :--- |
| Figure 4.1 | `figures/fig_4_1_four_layer_architecture.mmd` | `.png`, `.svg` | 5092×5104 |
| Figure 4.2 | `figures/fig_4_2_context_model.mmd` | `.png`, `.svg` | 4812×3952 |
| Figure 4.3 | `figures/fig_4_3_class_diagram.mmd` | `.png`, `.svg` | 5536×4016 |
| Figure 4.4 | `figures/fig_4_4_seq_diagnose.mmd` | `.png`, `.svg` | 5576×6588 |
| Table 4.1 | `table_4_1_adr.md` | Markdown → Word table | — |
| Table 4.2 | `draft.md` §4.1.3 | Markdown → Word table | — |

All four figures were re-exported from their committed `.mmd` sources after the last edit, so no figure is out of date relative to its source. Rendering notes are in `figures/README.md`.

---

## 4. Cross-chapter consistency obligations

These must be checked at merge time. Each is a place where this chapter and another chapter make a matching claim, and a mismatch would be visible to a marker.

| This chapter says | Must match | Owner |
| :--- | :--- | :--- |
| Diagnosis performs no model inference (§4.2.2) | Chapter 5.3–5.4, the "table lookup versus LLM generation" comparison | 董思钦 |
| Neo4j is offline-only (Figure 4.2, AD-5) | Chapter 6.3 evaluation framing; Chapter 5.6 deployment topology | 杨明杰 / 梁子铉 |
| 4 endpoints, 3 routers, 3 services (§4.1.3, Table 4.2) | Chapter 5.2 endpoint contract table | 江昊 |
| 12 questions / 48 options / 36 traps / 5 dimensions (§4.3.1) | Chapter 5.3 question bank description; Table 5.4 | 董思钦 |
| Security weaknesses: wildcard CORS, no authentication (AD-6, AD-7, §4.6) | Chapter 7 Limitations; Chapter 2.3 security NFR | 吴宇轩 / 张梓健 |
| Quality attributes as design consequences (§4.6) | Chapter 2.3 NFR table | 张梓健 |
| Instructor is a secondary external entity (§4.2.1) | Chapter 3 use-case diagram deliberately excludes teacher-side functions | 谢炜昕 |

> ⚠️ The planning document `cycle3_master_plan.md` §1.1 restates several of these numbers incorrectly (8 endpoints, 5 routers, 932 lines, 145 tests). This chapter uses measured values only. If Chapter 5 or 6 quotes the plan's values instead, the report will contradict itself across chapters.

---

## 5. Literature to cite (Harvard)

The chapter is currently written without inline citations beyond internal cross-references. The following are the appropriate anchors for the claims made, and must be added before submission.

| Claim location | Claim | Reference |
| :--- | :--- | :--- |
| §4.1.2 | Modular monolith versus microservices as an architectural trade-off | Sommerville, I. (2016) *Software Engineering*. 10th edn. Harlow: Pearson. |
| §4.1.2 | Architecture dictated by constraints rather than preference | Sommerville (2016), ch. 6. |
| §4.2 | Context models as the boundary-defining view | Sommerville (2016), ch. 5. |
| §4.2.2 | Sequence diagrams for interaction modelling | Sommerville (2016), ch. 5. |
| §4.3 | Class diagrams and domain modelling | Sommerville (2016), ch. 5. |
| §4.4 | Recording architectural decisions and their rationale | Sommerville (2016), ch. 6. |
| §4.2.2 | Hallucination risk in retrieval-augmented generation | Es, S. et al. (2023) 'RAGAS: Automated Evaluation of Retrieval Augmented Generation'. *arXiv preprint* arXiv:2309.15217. |
| §4.6 | Progressive disclosure as a usability pattern | Nielsen, J. (2006) 'Progressive Disclosure'. *Nielsen Norman Group*. |
| §4.6 | Measurable non-functional requirements | Sommerville (2016), ch. 4. |

**Format note:** the report requires Harvard style throughout and at least 25 references project-wide. This chapter contributes the entries above; the volume editor (谢炜昕) will merge them with the rest.

---

## 6. Open items before submission

1. **Chapter 5.4 P95 claim.** If Chapter 5.4 states "P95 < 5 ms", it must be reconciled with the 16 ms measured here, or re-measured under stated conditions.
2. **Subsection structure.** This draft uses six sections; `technical_report_draft.md` currently has three for Chapter 4. Confirm with 谢炜昕.
3. **Instructor wording.** Confirm with 谢炜昕 that a secondary external entity in the context model does not contradict Chapter 3's exclusion of teacher-side functions.
4. **Table 4.2 numbering.** Added during drafting and not in the global allocation in `cycle3_master_plan.md` §2.3. Either obtain a number from 吴宇轩 or fold the table into §4.1.3 prose.
5. **Inline citations.** Section 5 above lists the references; they still have to be inserted into the running text.
