# Chapter 4 System Design and Architecture — Outline (Week A)

**王思鉴 (50106045)** · branch `report/ch04-wang-sijian` · baseline `develop` @ `626d467`
**Target:** 9–11 pages · 2,600–3,400 English words · 4 figures + 2 tables

## Thesis

> We are not delivering a feature list; we are delivering a set of mutually consistent engineering trade-offs.

Write the constraints first (12 weeks · 10 contributors · zero budget · must demonstrate offline). Every capability claim in this chapter is presented as a consequence of those constraints.

---

## 4.1 Architectural Overview — 700–900 words · Figure 4.1

### 4.1.1 Layered structure and physical deployment

Four layers. Three facts a marker must be able to see in the figure: one process, one port, no database. `StaticFiles(html=True)` mounts at `/`, so the front end and the API share an origin and the production path never crosses an origin boundary.

### 4.1.2 Why a modular monolith

Open with the honest history: the first service (`86dd6d6`, 23 September) was one 228-line file. We replaced it because it could not absorb a second contributor and its rules could not be tested without an HTTP server. Then the cost argument: orchestration, discovery, distributed transactions and tracing would have fallen on ten students in twelve weeks, and independent scaling is worth nothing at demonstration scale.

### 4.1.3 Component inventory and responsibilities

Nine components across four layers; only one holds rules. Table 4.2 is a dependency check, not an inventory. Leave the endpoint contract and field schema to Chapter 5.2.

## 4.2 Context and Behavioural Models — 600–800 words · Figure 4.2 / Figure 4.4

### 4.2.1 System context model

Three external entities: Student (primary, operates the system), Instructor (secondary stakeholder, does not operate it), Neo4j AuraDB (dashed, labelled *offline evaluation only* — the visual evidence for AD-5). State explicitly that including a stakeholder is not the same as promising them features.

### 4.2.2 Sequence model for diagnosis

Browser → router (Pydantic) → diagnostic service → question bank → response. The model call happens after the verdict, with a four-second timeout, and cannot change the answer.

**Required sentence** (must match 董思钦 Chapter 5.4):

> The diagnosis path performs no model inference. Every diagnosis is a dictionary lookup followed by field assembly.

**Measured latency to quote** — core 0.6 µs median (p95 0.7 µs, 720 samples); HTTP round trip 1.5 ms median. Report both. Do **not** quote "p95 < 5 ms": the measured HTTP p95 is 16 ms.

## 4.3 Domain Class Model — 400–500 words · Figure 4.3

### 4.3.1 Four domain classes and their relationships

`QuizItem` 1—* `OptionItem` (12 / 48); `OptionItem` *—1 `TrapDetail` (wrong options only, 36 traps); `TrapDetail` 1—1 `RadarDimension` (recall, boundary, trapDefense, synthesis, precision). `GraphData` / `GraphNode` / `GraphEdge` shown as a secondary aggregate that carries no diagnostic weight.

### 4.3.2 The modelling decision that made diagnosis deterministic

**The trap hangs on the option, not on the question.** Attaching it to the question forces the system to infer which misconception a wrong answer represents. Attaching it to the option makes diagnosis a foreign-key lookup. This is AD-4 and the premise of every determinism claim in the chapter.

## 4.4 Architecture Decision Records — 300–400 words · Table 4.1

### 4.4.1 Decision record format and evaluation criteria

Four mandatory fields: decision, rejected alternative, rationale, cost. State the criterion plainly — an empty cost column is evidence of insufficient thought, not of a good choice.

### 4.4.2 What we got wrong

This subsection is the de-AI counterweight and should be kept. Four documented failures: silent degradation (fixed by `0feb82d`), our own diagram going stale inside a day, schema churn absorbed by dual-case aliases, and broad exception handling that hid real faults.

## 4.5 Key Algorithms and Control Flow — 400–500 words

### 4.5.1 Startup and request flow

Start-up order matters: routers registered before the catch-all static mount. Request path: route match → Pydantic validation (422 exit) → service → response serialisation with dual naming conventions.

### 4.5.2 Diagnosis control flow

Index lookup → selected-key normalisation → single option scan → key comparison → trap lookup on a wrong answer. Three exits bound the path, and the final guard exists so a live demonstration cannot produce a 500. This subsection carries the official *business process model* requirement; render it as control flow, not as a decorative flowchart.

## 4.6 Non-Functional Design — 300–400 words

### 4.6.1 Quality attributes as design consequences

Rewrite 张梓健's five NFR classes as consequences of the decisions in 4.4, not as aspirations:

| Attribute | Mechanism | Known weakness |
| :--- | :--- | :--- |
| Usability | Single page; progressive disclosure in the diagnostic drawer; dual theme and language | — |
| Performance | No database, no network, no model call on the verdict path | — |
| Reliability | Static assets and API share a process; nothing external on the demo path | — |
| Security | Typed request validation; no SQL surface | Wildcard CORS, no authentication (AD-6, AD-7) |
| Maintainability | Layer separation; regression suite | — |

The Security row must state the weakness. A report claiming no weaknesses contradicts Chapter 6.

---

## Figures and table register

| Number | Title | Source | Size (px @2×) |
| :--- | :--- | :--- | :--- |
| Figure 4.1 | Four-layer architecture and single-port deployment | `figures/fig_4_1_four_layer_architecture.mmd` | 5092×5104 |
| Figure 4.2 | System context model | `figures/fig_4_2_context_model.mmd` | 4812×3952 |
| Figure 4.3 | UML class diagram | `figures/fig_4_3_class_diagram.mmd` | 5536×4016 |
| Figure 4.4 | Diagnose sequence diagram | `figures/fig_4_4_seq_diagnose.mmd` | 5576×6588 |
| Table 4.1 | Architecture decision records | `table_4_1_adr.md` | — |
| Table 4.2 | Component responsibilities and permitted dependencies | draft §4.1.3 | — |

Table 4.2 was added during drafting and is not in the global allocation in `cycle3_master_plan.md` §2.3. Either obtain a number from 吴宇轩 or fold it into the §4.1.3 prose.

## Materials register

Baseline `develop` @ `626d467`. Status: ✅ usable ｜ ⚠️ exists but needs checking ｜ ❌ missing.

### Verified and usable

| Material | Path | Use |
| :--- | :--- | :--- |
| Application assembly | `backend/app/main.py` | 4.1.1, 4.5.1, AD-1, AD-6 |
| Routers (4 endpoints) | `backend/app/routers/{health,quiz,diagnose}.py` | 4.1.3, 4.5.1 |
| Diagnostic service | `backend/app/services/diagnostic_service.py` | 4.2.2, 4.5.2, AD-4 |
| LLM diagnostics | `backend/app/services/llm_diagnostics.py` | 4.4.2, 4.5.2 |
| Quiz and trap models | `backend/app/models/quiz.py` | Figure 4.3 |
| Question data | `backend/app/data/seed_questions.py` | 4.3.1, AD-3 |
| Configuration | `backend/app/config.py` | 4.2.2 (timeout, model) |

### Exists but needs checking

| Material | Path | Issue |
| :--- | :--- | :--- |
| Report draft | `reports/technical_report_draft.md` | Ch4 has three subsections; this outline has six. Confirm with 谢炜昕 |
| API mapping | `reports/api_frontend_mapping.md` | Documents the retired stdlib backend (`/api/answer`, `/api/tutor`) |

### Missing from the repository

`reports/report_data_contract.md`, `reports/phase2_cycle2_progress_report.md`, `reports/diagrams/*.drawio`, `reports/competitor_analysis.md`, `reports/project_proposal.md`, `reports/assumptions.md`, the PoC user manual PDF, and `reports/final_report/_template/`. None can be cited until they exist.

## Verified numbers

Measured on `develop@626d467`. Use these, not the plan's restated values.

| Quantity | Value | How to verify |
| :--- | :--- | :--- |
| Routers | 3 | `backend/app/routers/` excluding `__init__.py` |
| Endpoints | 4 | `@router` decorators |
| Services | 3 | `backend/app/services/` |
| Model modules | 3 | `backend/app/models/` |
| Questions | 12 | AST count of `QuizItem(` |
| Options | 48 | AST count of `OptionItem(` |
| Traps | 36 | AST count of `TrapDetail(` |
| Graph nodes | 60 | AST count of `GraphNode(` |
| Radar dimensions | 5 | `radar_hit` values; `frontend/app.js:1250-1254` |
| LLM timeout | 4.0 s | `config.py:29` |
| Core latency | 0.6 µs median, p95 0.7 µs | 720 samples over 36 wrong-answer cases |
| HTTP latency | 1.5 ms median `POST /api/diagnose` | 200 iterations, local uvicorn |
| Model calls on verdict path | 0 | `diagnostic_service.py` branch structure |

The plan's restatements (8 endpoints, 5 routers / 5 services / 5 models, 932 lines, 57/259/73 KB, 145 tests) do not match the code. Flag the discrepancy at merge time.

## Automatic-rejection risks

| # | Risk | Status |
| :-: | :--- | :--- |
| R-01 | Figure 4.4 shows LLM or Neo4j on the diagnosis path | Resolved; verified absent from the diagram body |
| R-02 | Figure 4.2 still says `server.py` | Resolved; now `backend/app/main.py` |
| R-03 | Diagram source and export disagree | All exports regenerated from the committed `.mmd` |
| R-04 | Instructor required here (task pack 04) but excluded from the use-case diagram (task pack 09) | Context model includes it; confirm wording with 谢炜昕 |
| R-05 | Quoting numbers that do not match the code | Only the verified table is used |
| R-06 | Overlap with Chapters 5.1 / 5.2 | This chapter explains why; endpoint and field tables stay in 5.2 |
| R-07 | Subsection structure differs from the current report draft | Raise with 谢炜昕 before merging |

## Still to do

1. Insert Harvard inline citations — `sources.md` §5 lists nine references that are not yet in the running text.
2. Confirm subsection structure and Instructor wording with 谢炜昕 (R-04, R-07).
3. Obtain a number for Table 4.2 from 吴宇轩, or fold it into prose.
4. Peer-review Chapter 6 as assigned in `cycle3_master_plan.md` §4.
