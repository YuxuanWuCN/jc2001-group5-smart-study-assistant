# Table 4.1 — Architecture Decision Records

**Chapter 4.4 · 王思鉴 (50106045)**
**Baseline:** `develop` @ `626d467`

All seven decisions below are traceable to the current implementation. Each entry has, in the body text (4.4.2), an 80–120 word expansion; the table exists to make the trade-off structure visible at a glance.

| ID | Decision | Rejected alternative | Rejection rationale | Cost / known risk |
| :-: | :--- | :--- | :--- | :--- |
| **AD-1** | **Modular monolith** — one process, one port; `routers → services → data/models` | Splitting into microservices | Ten weeks, ten students, one machine for the demonstration. The benefits of independent scaling are worth zero here, while service discovery, container orchestration, cross-service transactions and distributed tracing would all have to be paid for. | Cannot scale horizontally. No independent deployment of components. Accepted because the demonstration is single-user. |
| **AD-2** | **Zero-build front end** — native ES6, CSS variables, no bundler or framework | React + Vite + Tailwind | The examiner must run the project from a ZIP with no `npm install`. A build step would turn a one-command start into a toolchain prerequisite. | Module load order is managed by hand; no component ecosystem; larger raw payload than a tree-shaken bundle. |
| **AD-3** | **Static Python question bank** — read-only source module, no database | PostgreSQL / SQLite | No database means no migrations, no connection pool, no `database is locked` under concurrent requests, and no seeding step. It is the main reason the package runs from a clean machine. | Content cannot be edited at runtime; any content change requires a release. Query flexibility is limited to in-memory dictionary access. |
| **AD-4** | **Option-level traps resolved by table lookup** — `traps[option.trap_id]` | Letting the LLM generate the diagnosis | A hallucinated statute or formula in a law or numerics question is a teaching-level failure. A table is reproducible, testable, and answers in well under a millisecond. | Only covers traps authored in advance. Items outside the 36 authored traps cannot be diagnosed. |
| **AD-5** | **Neo4j confined to the offline evaluation path** | Putting the graph on the online demonstration path | The Aura instance sleeps when idle and the examination room may have no network; a graph call on the demo path would turn into a 500 at the worst possible moment. | The graph's measured benefit cannot be shown live; it can only be evidenced by the offline CSV. This is the weakest of the seven decisions from a demonstration standpoint. |
| **AD-6** | **`allow_origins=["*"]`** in the CORS middleware | An explicit origin allow-list | The demonstration runs same-origin, but the marker may open it from any local port or from `file://`. A allow-list would make local debugging fail at every turn. | **Must be tightened before any production use.** No origin restriction and `allow_credentials=True` are contradictory in production. This is declared again in Chapter 7. |
| **AD-7** | **`localStorage` session state** — attempts held in the browser | JWT plus a server-side session table | The demonstration is stateless and single-machine. Server sessions add key management, expiry, and a store to the deployment story for no demonstrable gain. | No cross-device sync, no real authorisation boundary, and clearing browser data erases progress. Progress is not a trustworthy record. |

---

## Notes for the report writer

- **No row may have an empty or "none" cost column.** Task pack §4.4 treats a cost-free decision as evidence that the decision was not thought through, and §4 lists it as an automatic rejection.
- **AD-5 and AD-6/AD-7 are the honest disclosures.** They are deliberately stated as weaknesses. The marking scheme rewards consistency and technical depth, and a report that claims no weaknesses contradicts the empirical results in Chapter 6.
- **Cross-references that must stay aligned:**
  - AD-4 ↔ Chapter 5.4 (董思钦) comparison of table lookup versus LLM generation;
  - AD-5 ↔ Figure 4.2 (dashed Neo4j marked *offline evaluation only*) and Chapter 6.3 (MMLU results);
  - AD-6, AD-7 ↔ Chapter 7 Limitations and Chapter 2.3 security NFR.
- **Word budget:** 300–400 words for §4.4 in total, of which each AD gets 80–120 words in the body. The table itself does not count toward the word total.

## Source anchors

| Decision | Where it lives in the code |
| :--- | :--- |
| AD-1 | `backend/app/main.py` — `create_app()`, three `include_router` calls, one `StaticFiles` mount |
| AD-2 | `frontend/index.html`, `frontend/app.js` — no `package.json`, no build output |
| AD-3 | `backend/app/data/seed_questions.py` — 657 lines, 12 items, imported at start-up |
| AD-4 | `backend/app/services/diagnostic_service.py` — `traps[option.trap_id]` lookup |
| AD-5 | `graphrag（终）/real_graph_engine.py` — separate offline scripts, not imported by `backend/app` |
| AD-6 | `backend/app/main.py` — `CORSMiddleware(allow_origins=["*"], allow_credentials=True)` |
| AD-7 | `frontend/app.js` — `localStorage` reads and writes for attempts and theme |
