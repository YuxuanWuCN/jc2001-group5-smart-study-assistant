# Verification Commands & Evidence — Chapter 2 (Zijian Zhang, `50106035`)

## 1. Automated Verification Commands

Run from the repository root (`D:\jc2001`):

```powershell
# 1. Verify ground-truth question bank counts (9 subjects, 17 questions, 51 traps, 68 options, 939 lines)
python scripts/audit_report_numbers.py

# 2. Run the full 10-module automated test suite (105 test functions, 189 collected cases)
python -m pytest tests/ -q

# 3. Verify optional online baseline hook skips cleanly (exit code 0) when QWEN_API_KEY is unset
python scripts/audit_online_baseline.py

# 4. Verify persona provenance (E1/E2) and L1-L3 deterministic content/attribution audits
python scripts/audit_persona_claims.py
python scripts/audit_hallucination_l1_l3.py
```

## 2. Requirement-to-Code and Test Mapping Summary

All endpoints below match the 9 REST routes implemented in `backend/app/routers/`:

- `R01`: `GET /api/quiz` (`backend/app/routers/quiz.py`, `backend/app/services/quiz_service.py`, `backend/app/data/seed_questions.py`: 9 subjects, 17 curated questions, 68 options) -> `tests/test_quiz.py` (6 functions / 21 cases).
- `R02` & `R03`: `POST /api/diagnose` (`backend/app/routers/diagnose.py`, `backend/app/services/diagnostic_service.py`: 51 distractor traps across 17 curated questions, schema validation `422`, structured `fallback_mode: true` on unknown question IDs) -> `tests/test_diagnose.py` (8 functions / 10 cases) and `tests/test_adversarial_backend.py` (25 functions / 38 cases).
- `R04` (`Must — partially satisfied: session-scoped client-side aggregation`): `GET /api/reports/trend` (`backend/app/routers/reports.py`, `backend/app/services/report_service.py`) and browser in-session radar updates in `frontend/app.js` (starting values `76, 62, 65, 72, 81`; correct `+4/+5/+3`, wrong `-6/-4`, clamped `[30, 100]`, no cross-session persistence or temporal decay) -> `tests/test_reports.py` (9 functions / 23 cases) and cross-checked with Section 5.4.3 and Chapter 6 (`Table 6.5`).
- `R05`: `GET /api/reports/summary` (`backend/app/routers/reports.py`, `report_service.py`: summary fields + zero-value unknown-subject fallback) -> `tests/test_reports.py`.
- `R06`: `GET /api/auth/demo-users`, `POST /api/auth/login`, `POST /api/auth/register` (`backend/app/routers/auth.py`, `auth_service.py`: 11 group members + 1 guest profile; demo-only local sessions without persistent `409` uniqueness or production password auth per `AD-7`) -> `tests/test_auth.py` (10 functions / 10 cases).
- `R07` & `R08`: Runtime interface locale layer with one English locale shipped (`frontend/app.js`) and `dark`/`light` themes (`frontend/style.css`, `localStorage`) -> `tests/test_e2e_frontend.py` (8 functions / 8 cases) and Section 5.5 walkthrough.
- `R09` & `NFR-R1`: Single-process FastAPI static mount (`backend/app/main.py`, `GET /api/health`) -> `tests/test_health.py` (5 functions / 8 cases), `tests/test_cors.py` (4 functions / 19 cases), `tests/test_e2e_frontend.py` (8 functions / 8 cases), `tests/test_empirical_stress.py` (7 functions / 12 cases). Apache ECharts `5.5.1` is vendored at `frontend/vendor/echarts.min.js`, so fresh uncached offline browser loads also render charts.
- `R10` & `NFR-S2`: Offline 12-subject MMLU benchmark (`graphrag_final/final_systematic_report.csv`, `n = 4,445`: 7 wins, 3 ties, 2 losses; `Professional Law +2.50 pp`, `Econometrics +1.76 pp`, `High School US History -1.00 pp`, `High School Physics -1.32 pp`), `GET /api/health/llm`, and `scripts/audit_online_baseline.py` -> `tests/test_llm_health.py` (19 functions / 36 cases).

## 3. Scope, Naming, and Banned-Term Verification

Checked all deliverables in `reports/final_report/ch02_zhang_zijian/` (`draft.md`, `evidence.md`, `viva_qa.md`, `README.md`, `sources.md`, and `figures/fig2_1_moscow_distribution.svg`):

- Legacy project-name and objective-acronym wording banned by `reports/week_failure_retrospective_and_tasks_2026-11-02.md` (Rule F3): **0 matches** (uses `StudyGraph` and `Five Project Objectives` exclusively).
- `BANNED_TERMS` marketing list in `scripts/audit_hallucination_l1_l3.py`: **0 matches**.
- `scripts/audit_report_numbers.py` numeric consistency scan against `backend/app/data/seed_questions.py` (`9` subjects, `17` questions, `51` traps, `68` options, `939` lines): **0 contradictions**.
- Route and test-module audit: references only the 9 real endpoints in `backend/app/routers/` and the 10 real test modules in `tests/` (105 functions / 189 cases).
