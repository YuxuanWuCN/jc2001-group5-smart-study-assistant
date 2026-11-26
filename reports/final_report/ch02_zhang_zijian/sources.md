# Sources and Traceability Anchors — Chapter 2 (Zijian Zhang, `50106035`)

## 1. Requirements & Prior Personal Contributions

- `reports/rtm.md` (Part B): Original personal RTM extract authored by `50106035` for `UC-05` to `UC-08` (`FR-04`–`FR-10`, `NFR-02/03/04/07/08`), archived from GitHub PR #5 / PR #8 (`commit 9413a58`). Preserved unchanged for traceability alongside the Cycle 3 `R01`–`R14` MoSCoW baseline.
- `reports/use_cases.md` (Part B): Original personal use-case specifications for `UC-05` to `UC-08`.
- `reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md`: Frozen Cycle 3 `R01`–`R14` MoSCoW numbering (`Must 7 / Should 3 / Could 0 / Won't 4`) and five-category NFR structure (`NFR-U1`–`NFR-M2`).
- `reports/week_failure_retrospective_and_tasks_2026-11-02.md`: Group number registry and `T4-Ch2` alignment requirements (`R04` partial satisfaction, `51 traps`, plain-voice rewrite, and Rule F3 canonical `StudyGraph` / `Five Project Objectives` naming).
- `reports/competitor_analysis.md`: Competitor audit covering Anki, Quizlet, ChatGPT, and Khanmigo.
- `reports/audit/persona_provenance.csv`: Provenance grading (`E1`/`E2`, zero `E0` fabricated survey claims).

## 2. Inspected Implementation & Evaluation Files

- `backend/app/data/seed_questions.py`: 9 subjects, 17 curated questions, 68 options, 51 distractor traps, 939 lines (verified via `scripts/audit_report_numbers.py`).
- `backend/app/routers/quiz.py`, `diagnose.py`, `reports.py`, `auth.py`, `health.py`: 9 REST endpoints (`GET /api/quiz`, `POST /api/diagnose`, `GET /api/reports/summary`, `GET /api/reports/trend`, `GET /api/auth/demo-users`, `POST /api/auth/login`, `POST /api/auth/register`, `GET /api/health`, `GET /api/health/llm`).
- `backend/app/services/diagnostic_service.py`, `report_service.py`, `auth_service.py`, `quiz_service.py`, `llm_diagnostics.py`: Verified runtime lookup, fallback behaviour, fixed backend report baselines, and demo auth behaviour.
- `frontend/index.html`, `frontend/app.js`, `frontend/style.css`, `frontend/vendor/echarts.min.js`: Verified client-side session radar aggregation, the single-English-locale interface with dual-theme controls, and locally vendored ECharts rendering.
- `tests/test_*.py`: 10 test modules, 105 test functions, 189 collected `pytest` cases (`test_adversarial_backend.py`, `test_auth.py`, `test_cors.py`, `test_diagnose.py`, `test_e2e_frontend.py`, `test_empirical_stress.py`, `test_health.py`, `test_llm_health.py`, `test_quiz.py`, `test_reports.py`).
- `graphrag_final/final_systematic_report.csv`: 12-subject MMLU offline evaluation (`n = 4,445`: 7 wins, 3 ties, 2 losses; `Professional Law +2.50 pp`, `Econometrics +1.76 pp`, `High School US History -1.00 pp`, `High School Physics -1.32 pp`).

## 3. Cross-Chapter Alignment References

- Chapter 1 (`reports/final_report/ch01_lin_yongtong/draft.md`): Table 1.1 (competitors), Table 1.2 (Five Project Objectives 1–5), Table 1.3 (intended users and stakeholders).
- Chapter 3 (`reports/final_report/ch03_xie_weixin/draft.md`, `requirement_crosswalk.md`, `appendix_B_RTM.md`): `UC-01`–`UC-08`, original FR/NFR retention, and `R01`–`R14` semantic crosswalk.
- Chapter 4 (`reports/final_report/ch04_wang_sijian/table_4_1_adr.md`): Architecture Decision Records `AD-1`–`AD-7`.
- Chapter 5 (`reports/final_report/ch05_dong_siqin/draft.md`, Section 5.4.3): Seed bank composition and client-side five-dimension radar partial satisfaction.
- Chapter 6 (`reports/final_report/ch06_yang_mingjie/draft.md` & `xin/master` `requirement_crosswalk.md`): Table 6.1 test inventory, Table 6.3 MMLU breakdown, and Table 6.5 requirement audit.
