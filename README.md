# StudyGraph — Graph-Grounded Option-Level Misconception Diagnostic Assistant

We developed **StudyGraph** for **JC2001 Introduction to Software Engineering (2026–2027)** at the **University of Aberdeen** (BSc Business Management and Information Systems, Group 5, supervised by Dr. Shahzad Mumtaz).

Instead of stopping at a right/wrong mark or letting an unconstrained language model spoil answers, we pair a single-process **FastAPI + Pydantic v2** service and zero-build **HTML5 / CSS3 / ES6+** interface with a curated misconception bank (`17` questions across `9` subjects and `51` distractor traps) and a decoupled offline **GraphRAG** evaluation pipeline.

---

## Verified Submission Baseline

| Dimension | Verified State | Evidence Anchor |
| :--- | :--- | :--- |
| **Runtime Architecture** | Single-process FastAPI + static SPA served on port `8000` | [backend/app/main.py](backend/app/main.py) |
| **Curated Seed Bank** | `17` questions across `9` subjects, `68` options, `51` traps | [backend/app/data/seed_questions.py](backend/app/data/seed_questions.py) |
| **REST API Endpoints** | `9` endpoints (`/api/health`, `/api/health/llm`, `/api/quiz`, `/api/diagnose`, `/api/reports/summary`, `/api/reports/trend`, `/api/auth/demo-users`, `/api/auth/login`, `/api/auth/register`) | [backend/app/routers/](backend/app/routers) |
| **Offline Frontend Assets** | Zero-build ES6+ UI with locally vendored ECharts `5.5.1` | [frontend/vendor/echarts.min.js](frontend/vendor/echarts.min.js) |
| **Session Telemetry & Auth** | Thread-safe live attempt aggregation (`demo_baseline` cold start) and salted PBKDF2 password checks for registered accounts | [backend/app/services/report_service.py](backend/app/services/report_service.py), [backend/app/services/auth_service.py](backend/app/services/auth_service.py) |
| **Automated Regression Suite** | `189` offline `pytest` cases across `10` modules (`0` external network calls, `0` warnings) | [tests/](tests) |
| **Offline GraphRAG Evaluation** | `12` MMLU subject CSVs (`4,445` stored items; evaluated with a `200`-item per-subject cap, `n = 1,991` evaluated items): `7` gains, `3` ties, `2` regressions (`Law +2.50 pp`, `Physics -1.32 pp`, `US History -1.00 pp`) | [graphrag_final/final_systematic_report.csv](graphrag_final/final_systematic_report.csv) |

---

## Quick Start (Offline Zero-Config Launch)

We designed the submission so examiners can run the full application and test suite from a clean checkout without Neo4j or external API keys:

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the offline automated verification suite (189 tests)
python -m pytest tests/ -q

# 3. Start the integrated backend + static frontend server
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
# or:
python backend/run.py
```

Open `http://127.0.0.1:8000` in a browser. Optionally copy `.env.example` to `.env` if you want to enable live DashScope (`QWEN_API_KEY`) Socratic rephrasing; when no key is set, every diagnostic endpoint falls back locally with zero `500` errors.

---

## Repository Structure

```text
.
├── backend/
│   ├── run.py                       # Standalone launch script
│   └── app/
│       ├── config.py                # Environment configuration (.env)
│       ├── main.py                  # FastAPI factory & static SPA mount
│       ├── data/seed_questions.py   # 17 curated questions, 51 traps, 9 subjects
│       ├── models/                  # Pydantic v2 CamelModel contracts
│       ├── routers/                 # 9 REST API endpoints
│       └── services/                # Diagnostic, quiz, report & auth logic
├── frontend/
│   ├── index.html                   # Single-page portal & study console
│   ├── app.js                       # Client state, trap drawer & ECharts radar
│   ├── style.css                    # Light/dark theme tokens
│   └── vendor/echarts.min.js        # Local ECharts 5.5.1 bundle (offline safe)
├── graphrag_final/                  # Decoupled Neo4j/GraphRAG scripts & MMLU CSVs
├── reports/
│   ├── final_report/                # Final Technical Report PDF, LaTeX, drafts & figures
│   ├── ui-design/                   # Wireframes, design system & interactive prototype
│   ├── audit/                       # Hallucination & provenance audit outputs
│   ├── rtm.md / use_cases.md        # Bidirectional RTM & use-case specs
│   └── test_plan.md                 # Black-box test plan
├── scripts/                         # Report assembly, PDF build & audit utilities
├── specs/                           # Feature specifications (001–004)
├── tests/                           # 10 pytest modules (189 cases, zero network)
├── .env.example                     # Optional environment variable template
└── requirements.txt                 # Direct Python dependencies
```

---

## Group 5 Contributors & Responsibilities

We collaborated across requirements engineering, UML modelling, backend/frontend implementation, QA verification, and final technical reporting:

| Member | Role | Core Engineering & Report Ownership |
| :--- | :--- | :--- |
| **Wu Yuxuan** | Team Lead & Project Manager | Integration governance, `CamelModel` coordination, consistency audits, **Ch 7** & **Appendix A** |
| **Lin Yongtong** | Lead Business Analyst | Competitor analysis, stakeholder & educational framing, **Ch 1** |
| **Zhang Zijian** | Business Analyst | MoSCoW & NFR specifications, PR review merges, **Ch 2** |
| **Xie Weixin** | QA & Report Lead | Use-case modelling, state machine, **Ch 3** & **Appendix B (RTM)** |
| **Wang Sijian** | Software Architect | Four-layer architecture, UML 2.5 diagrams, ADR matrix, **Ch 4** |
| **Jiang Hao** | PoC Lead Developer | FastAPI app factory, REST contracts, **Ch 5.1–5.2** & **Appendix D** |
| **Dong Siqin** | PoC Logic & Data Lead | Seed bank & trap taxonomy, diagnostic lookup, LLM probe, **Ch 5.3–5.4** |
| **Xi Yusai** | UI/UX & Frontend Lead | Zero-build SPA, Trap Drawer, dual themes, English-only i18n resource layer, **Ch 5.5** |
| **Liang Zixuan** | Deployment & Media Lead | Single-port packaging, `.env` hygiene, reproducibility, **Ch 5.6** & demo |
| **Yang Mingjie** | Testing & Evaluation Lead | Automated `pytest` suite, adversarial testing, MMLU analysis, **Ch 6** & **Appendix C** |
| **Luo Wenxi** | Independent QA & Verification | Trap bank integrity & numerical cross-verification (**Ch 6** & **Appendix C**) |
