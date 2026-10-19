# Figure & Table index — Chapter 4

**Owner:** 王思鉴 (50106045) · Chapter 4 System Design and Architecture
**Baseline:** `develop` @ `626d467`

| ID | Title | Source | Export | Size (px @2×) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Figure 4.1 | Four-layer architecture and single-port deployment | `fig_4_1_four_layer_architecture.mmd` | `.png` / `.svg` | 2548×2553 | ✅ new |
| Figure 4.2 | System context model | `fig_4_2_context_model.mmd` | `.png` / `.svg` | 2408×1978 | ✅ rebuilt |
| Figure 4.3 | UML class diagram (domain model) | `fig_4_3_class_diagram.mmd` | `.png` / `.svg` | 2770×2009 | ✅ new |
| Figure 4.4 | Diagnose sequence diagram | `fig_4_4_seq_diagnose.mmd` | `.png` / `.svg` | 2789×3294 | ✅ redrawn |
| Table 4.1 | Architecture decision records | `../table_4_1_adr.md` | Markdown → Word | — | ✅ draft |

---

## What changed against the previous figures in `reports/figures/`

| Figure | Change | Reason |
| :--- | :--- | :--- |
| 4.1 | **New.** Did not exist before. | Task pack §4.1.1 requires a self-drawn four-layer diagram showing single process, single port and no database. |
| 4.2 | Backend renamed `server.py` → `FastAPI 业务中枢 / backend/app/main.py`; store renamed `questions.json` → `seed_questions.py`; **Instructor added** as secondary external entity; Neo4j made dashed and labelled `offline evaluation only`. | The previous version still described the retired stdlib HTTP server. Task pack §4.2.1 requires three external entities including Instructor, and AD-05 must be visible. |
| 4.3 | **New.** Did not exist before. | Official Brief requires class diagrams; task pack §4.3 marks this as the only wholly-new technical figure. |
| 4.4 | **Neo4j removed from the online path entirely**; the model call reduced to an optional post-diagnosis `opt` fragment; participants renamed to the real FastAPI modules; request/response fields aligned to `backend/app/models/diagnose.py`. | The previous version drew LLM and Neo4j calls on the diagnosis path, contradicting the required §4.2.2 statement. Task pack §4.2.2 explicitly says such a figure **must be redrawn**, and §4 lists it as an automatic-rejection item. |

## Consistency checks

- **No model call on the diagnosis path.** `diagnostic_service.py:161-181` handles a correct answer and `:227-246` an incorrect one; the DashScope call sits behind `if settings.has_api_key and req.include_socratic` and only produces `socratic_guidance` *after* `is_correct` is decided. The verdict never depends on it.
- **Neo4j is absent from Figure 4.4** and appears only in Figure 4.2, dashed, marked `offline evaluation only` — matching AD-05 and the answer prepared in `supervisor_qa_defense_library.md`.
- **Source and export agree.** All four `.png`/`.svg` were regenerated from the `.mmd` in this directory; there is no edited-source-only figure.

## Regeneration notes (reproducibility)

Rendered with Mermaid 11 via headless Chrome, 2× device scale, 22 px padding, white background. Three Mermaid-11 behaviours had to be worked around and are documented inside each `.mmd` header so the files stay editable by hand:

1. **Node labels must not contain ASCII parentheses** — `()` is the node-shape delimiter and breaks the parse. The figures use fullwidth `（）` instead.
2. **A comment line may not be just `%%`** — a bare `%%` breaks the flowchart preprocessor. Use `%% ` (with a trailing space).
3. **A `%%{init:...}%%` directive with a nested `flowchart` JSON object is rejected** by the v11 flowchart parser (the `class` and `sequence` forms are accepted). Rendering configuration is therefore applied through `mermaid.initialize()` at render time rather than inside the diagram source.

These are rendering quirks, not content decisions; the diagrams remain valid Mermaid and can be pasted into <https://mermaid.live> unchanged.
