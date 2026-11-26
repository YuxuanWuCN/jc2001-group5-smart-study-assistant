# `reports/figures/` -- Figure Source Files and Export Notes

**Owner**: Wang Sijian (50106045) | **Deliverable**: Kickoff task package (II) deliverable 1
**Corresponding report chapters**: Chapter 3 Modelling, Chapter 4 System Design and Architecture

---

## 1. Directory Contents

| File | Description |
| :--- | :--- |
| `fig_context_model.mmd` | Figure 1 source file -- system top-level context model (System Context Model) |
| `fig_context_model.png` / `.svg` | Figure 1 exports (PNG 2248x1880, SVG vector) |
| `fig_use_case_diagram.mmd` | Figure 2 source file -- global UML use case diagram |
| `fig_use_case_diagram.png` / `.svg` | Figure 2 exports (PNG 3457x932, SVG vector) |
| `fig_seq_diagnose.mmd` | Figure 3 source file -- full wrong-answer trap diagnosis sequence diagram |
| `fig_seq_diagnose.png` / `.svg` | Figure 3 exports (PNG 3610x3568, SVG vector) |

Naming follows the task package's designated `fig_context_model`, `fig_use_case_diagram` and `fig_seq_diagnose`.
**Prefer `.svg` when inserting into the report**: vector images stay sharp when scaled in Word/PDF, and the SVGs in this directory already embed a white background and padding, so they can be dragged in directly.

---

## 2. Revision History of the Three Figures against the Task-Package Skeleton

The skeleton code itself has several defects that make "the figure render but the content be wrong"; all have been fixed. These are problems **exposed only by actual rendering**, not stylistic adjustments:

| # | Problem | Impact | Handling |
| :-: | :--- | :--- | :--- |
| 1 | Mermaid's HTML tag sanitizer strips `<...>` inside edge labels as unknown tags, so `"<&lt;include&gt;>"` finally renders as `<>` (**silent failure, no error**) | The `<<include>>` / `<<extend>>` stereotypes are all lost and Figure 2 loses its UML semantics | The source uses monospace placeholders `[[ST_INCLUDE]]` / `[[ST_EXTEND]]`, substituted with the real stereotypes at export time with matching label widths; the source comments explain this |
| 2 | Extend relationship direction reversed (`UC-01 -. extend .-> UC-08`) | Opposite to UML 2.5: the extending use case should point at the base use case | Changed to `UC-06/UC-07 -. extend .-> UC-01`; `<<include>>` keeps "included -> including" |
| 3 | The use case list omits `UC-06` and mixes the 7 use cases | The global use case diagram should cover the complete set of IDs already defined by the requirements group | Added `UC-06`; split into `UC-01..UC-05` / `UC-06..UC-08` regions and annotated the implementation status of each: `[Implemented]` / `[Frontend-computed]` / `[Planned]` / `[Optional]` |
| 4 | Figure 3 treats `POST /api/diagnose`, `selected_option` and Neo4j as mandatory path items | Inconsistent with the live implementation, so the report and the code do not match | Changed to `POST /api/answer {question_id, selected}`; the Neo4j branch is marked `[Planned]`, the model branch `[Optional]`, and the degraded branch maps to NFR-02 |
| 5 | Figure 3 lacks the "follow-up" business closed loop | Cannot express FR-07 guided tutoring | Added an `opt` fragment: `POST /api/tutor {question_id, message}`, with model and local dual branches |
| 6 | The skeleton does not show local degradation | NFR-02 "offline reliability" is a core argument of this project | Both figures make "on failure degrade to local curated content" an explicit branch |

> **Note**: if you paste the `.mmd` files in this directory straight into [mermaid.live](https://mermaid.live) for preview, the edge labels display the `[[ST_INCLUDE]]` placeholders -- that is the normal behaviour of the placeholders. To get the real stereotypes, re-export with the commands in section 3, or manually replace the placeholders with `&lt;&lt;include&gt;&gt;` and widen the label backgrounds accordingly.

---

## 3. Re-Exporting (Optional)

`.png` / `.svg` were generated with this delivery and **do not need to be regenerated**. If the `.mmd` files are modified later and need re-exporting, it is simplest to use mermaid.live (export SVG, then convert to PNG), or to use the following minimal pipeline inside the project:

1. Open a local HTML page that inlines Mermaid 11 (`type="module"` + CDN ESM) in headless Chrome and render each figure into the DOM;
2. Capture the figure bounding box precisely with `Page.captureScreenshot`'s `clip`, setting `scale` to 2 for a high-resolution PNG;
3. Substitute the stereotype placeholders, recompute the label widths, then serialise the SVG.

The pipeline script is not committed to the repository (a one-off tool that also depends on the local Chrome path); if you want it fixed under `tools/`, confirm with the team lead before submitting.

---

## 4. Recommended Sizes for Inserting into the Report

| Figure | Native ratio | Recommended layout | Notes |
| :--- | :--- | :--- | :--- |
| Figure 1 Context model | 1124x940 (close to 6:5) | **Portrait page, half or full column**, width 12-13 cm | The graphic is nearly square, so a full-column insertion is clearest |
| Figure 2 Use case diagram | 1728x466 (about 3.7:1) | **Full landscape page**, width 15-16 cm | Very wide and short; at full page width the text is about 7.5 pt, which is readable |
| Figure 3 Sequence diagram | 1805x1784 (about 1:1) | **A separate landscape page**, width 24 cm | Many messages; on a portrait page it shrinks below 5 pt and becomes unreadable; this figure suits a full landscape page |

If Figure 3 must go on a portrait page, split it along the `alt`/`opt` boundaries into two sub-figures, "Answer Judging and Diagnosis" and "Guided Follow-Up"; the existing `.mmd` yields them by deleting blocks, with no redrawing needed.

---

## 5. Team Peer Review and Code Traceability Alignment

**Reviewers**: Wu Yuxuan (50106070, team lead), Jiang Hao (50106065, reviewer) | **Date**: 2026-10-09

Following the JC2001 course rubric (which requires 100% strict traceability across system architecture diagrams, implementation code and automated tests) and the UML 2.5 standard, the `.mmd` sources were aligned for compliance as follows:

| # | Alignment item | Original source state | Compliance/code alignment fix | Rationale and marker's grading point |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Figure 2 use case diagram `<<extend>>` arrow direction** | Source lines 34-37 wrote `UC01 -. extend .-> UC08` (base use case pointing at the extending use case) | Changed to `UC08/UC07/UC06 -. extend .-> UC01` (extending use case pointing at the base use case) | **Strict UML 2.5 compliance**: an extending use case is a conditional aspect inserted into the base use case and must point at the extended base use case, avoiding lost marks in the defence. |
| 2 | **Figure 3 sequence diagram core API routes and contracts** | Written as `POST /api/answer {question_id, selected}` with a single-file `server.py` | Aligned to the real endpoint `POST /api/diagnose {question_id, selected_option}` and the layered architecture `backend/app` | **Code traceability closed loop**: the current repository and all 114 automated tests run against `POST /api/diagnose`, so the report must match the actually running code and test results exactly. |
| 3 | **Figure 1 context model backend and question-bank labels** | Labelled `server.py` and `data/curated/questions.json` | Labelled `FastAPI modular service hub (backend/app/main.py)` and `backend/app/data/seed_questions.py` | **Real architecture presentation**: reflects the modular three-layer engineering delivered by the team. |
| 4 | **Tutor multi-round follow-up marking** | Written as an immediately delivered `POST /api/tutor` | Marked `[Planned · tutor follow-up extension]` | **Academic honesty**: the basic Socratic guidance ships with `/api/diagnose`; the multi-round session gateway is still planned, avoiding a request during the defence to jointly test an undelivered standalone endpoint. |
