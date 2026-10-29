# Oral Defense (Viva) Q&A — Chapter 4 (Wang Sijian, `50106045`)

## Q1: Why did you choose a Single-Process Modular Monolith (`AD-6`) with an in-memory seed store (`AD-3`) rather than deploying Neo4j and PostgreSQL in Docker Compose?

**Answer:**
Our architecture is driven by `R09` (*100% Offline Single-Process Execution*) and `NFR-02` (*Cold start < 2.0 s*). In an academic assessment and student revision context, requiring Docker Desktop, a live Neo4j Bolt daemon (`bolt://localhost:7687`), and database migrations introduces severe reproducibility fragility on lab machines. By embedding the verified 1-hop prerequisite subgraphs (`GraphData`) directly inside `seed_questions.py` and mounting the vanilla ES6+ frontend via FastAPI's `StaticFiles` (`backend/app/main.py`), the entire system boots in $0.65\text{ s}$ from a single `uvicorn` command with zero CORS issues and zero external daemons, while keeping the heavyweight 12-stage GraphRAG pipeline decoupled in `graphrag（终）/` (`AD-1`).

## Q2: Explain how `CamelModel` (`AD-4`) works in `backend/app/models/common.py` and what problem it solved for your 10-person team.

**Answer:**
Early in integration, our backend routers returned Python `snake_case` keys (`radar_scores`, `trap_defense`, `socratic_prompt_en`), while our frontend JavaScript expected `camelCase` (`radarScores`, `trapDefense`, `socraticPromptEn`), causing silent `undefined` values in ECharts and the Trap Drawer. Rather than writing error-prone manual dictionary conversions in every router, we implemented `CamelModel` using Pydantic v2's `ConfigDict(populate_by_name=True, alias_generator=to_camel)` and overrode `model_dump()` to emit both `snake_case` and `camelCase` keys recursively. This guaranteed 100% schema compatibility across all 14 domain models (`Figure 4.3`) and is locked in by two regression tests in `tests/test_reports.py`.

## Q3: In Table 4.1 (`AD-2`), you rejected React/Vite in favour of Vanilla ES6+ and CSS Custom Properties. What was the trade-off of that decision?

**Answer:**
The primary benefit of `AD-2` is zero build-step fragility: markers never have to run `npm install` or debug Node.js / Webpack version conflicts (`NFR-08`), and editing `frontend/app.js` or `frontend/styles.css` takes effect immediately on browser refresh. The accepted trade-off is that without React's virtual DOM, we had to structure `frontend/app.js` (~1,150 lines) around explicit, disciplined DOM render helpers (`renderQuestion()`, `openTrapDrawer()`, `updateRadarChart()`, `applyLanguage()`) to keep UI state synchronised across language (`R07`) and theme (`R08`) switches.
