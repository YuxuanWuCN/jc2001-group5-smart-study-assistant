# 5.6 Deployment and Reproducibility — Section Outline

**Author:** Zixuan Liang (50106037) · Deployment and Media Lead
**Chapter:** 5.6, inside Chapter 5 (Implementation)
**Target:** 3–4 pages, 1,200–1,600 words of prose, Figure 5.5, Table 5.7
**Status:** outline (Step 1). The prose draft is `draft.md` in this folder.

---

## 1. Section spine

The section answers one question: *can an examiner reproduce the system on their own machine, and
why is that possible?* Every subsection below either states a property of the deployment or supplies
the evidence for it. Nothing in this section introduces a new feature.

| # | Subsection | Word budget | Claim it establishes |
| :-: | :--- | ---: | :--- |
| 5.6.1 | A Single Process as the Deployment Target | 380 | The deployment unit is one process on one port; the demo path needs no external service |
| 5.6.2 | Environment and Prerequisites | 150 + Table 5.7 | What a second machine must have |
| 5.6.3 | Deployment Procedure | 330 | Five commands, and the one command that does not work |
| 5.6.4 | Verification and Reproducibility | 340 | What can be re-run, and what cannot |
| 5.6.5 | Packaging for Submission | 300 | What goes into the archive and what must not |

---

## 2. Three-level structure

### 5.6.1 A Single Process as the Deployment Target

#### 5.6.1.1 One `uvicorn` process, two mounts
- `GET /api/*` → the FastAPI routers
- `GET /` → `StaticFiles(..., html=True)` serving `frontend/`
- Same origin ⇒ no CORS on the demonstration path
#### 5.6.1.2 Why a cloud deployment was rejected
- ADR-01; the assessed artefact runs on the examiner's machine
- Offline execution is a requirement, not a limitation
#### 5.6.1.3 Measured behaviour of the deployed shape
- Cold start 1.12 s; `GET /` 40,390 B in 50.9 ms
- `has_api_key: false` throughout ⇒ measurements taken offline

### 5.6.2 Environment and Prerequisites

#### 5.6.2.1 Declared versus enforced Python floor
- Declared 3.10+ in `requirements.txt` and README
- No `match`, no PEP 604 unions ⇒ policy, not constraint
#### 5.6.2.2 Dependency profile
- Twelve direct dependencies, all `>=`, none pinned
- Four of them serve the evaluation prototype, not the service
#### 5.6.2.3 Port, browser and disk
- Port 8000 default, overridable
- Any current browser; 3.99 MB extracted

### 5.6.3 Deployment Procedure

#### 5.6.3.1 The five-command path
- unpack → venv → install → start → browse
#### 5.6.3.2 No configuration before start
- `.env` optional; `.env.example` ships placeholders
#### 5.6.3.3 The documented start command is broken
- `python backend/run.py` → `ModuleNotFoundError`
- Working alternatives: `uvicorn backend.app.main:app`, `python -m backend.run`

### 5.6.4 Verification and Reproducibility

#### 5.6.4.1 Test evidence
- 150 passed / 1.79 s; 80 test functions in nine files
- Credentials cleared by the fixture ⇒ offline path is what is tested
#### 5.6.4.2 Content and data evidence
- `seed_questions.py` (657 lines) is the whole question bank
- `GET /api/quiz` returned twelve items
#### 5.6.4.3 What is not reproducible, and why
- Evaluation needs a Neo4j Aura instance whose credential was rotated
- `final_systematic_report.csv` is the traceable snapshot
- RAGAS metrics in the same position (Section 6.4)

### 5.6.5 Packaging for Submission

#### 5.6.5.1 Archive structure required by the brief
- `backend/`, `frontend/`, `tests/`, `requirements.txt`, `README.md`, `docs/User_Manual.pdf`, `graphrag(终)/`
#### 5.6.5.2 Four enforced exclusions
- no `.venv/`, no `__pycache__/`, no `.git/`, no `.env`
#### 5.6.5.3 Credential scan and the outstanding manual
- scan for `sk-`, `neo4j+ssc`, `password` before the archive is written
- three exploration scripts still carry inherited literal values; rotation owned by the project leader
- `docs/User_Manual.pdf` is required by the brief and does not exist yet

---

## 3. Material list (what this section draws on)

| Material | Repository path | Used for |
| :--- | :--- | :--- |
| Application assembly | `backend/app/main.py` | the two mounts, the CORS middleware, `app = create_app()` |
| Runtime configuration | `backend/app/config.py` | HOST/PORT defaults, `has_api_key`, `FRONTEND_DIR` |
| Start script | `backend/run.py` | the broken documented command |
| Dependency manifest | `requirements.txt` | twelve dependencies, no pins, Python floor statement |
| Test suite | `tests/` (9 test files + `conftest.py`) | 80 functions → 150 cases; credential-clearing fixture |
| Seed data | `backend/app/data/seed_questions.py` | the twelve-item bank, no database |
| Evaluation archive | `graphrag(终).zip` | 12 MMLU subject CSVs + `final_systematic_report.csv` |
| Environment template | `.env.example` | the optional keys and their placeholders |
| Format and numbering | `reports/cycle3_task_packs/08-...md`, `reports/cycle3_task_packs/README.md` | section budget, Figure 5.5 / Table 5.7 allocation |
| Architecture decisions | ADR-01, ADR-05 (Chapter 4) | single process, Neo4j offline only |

## 4. Figures and tables

| ID | Type | Content | Source of truth |
| :--- | :--- | :--- | :--- |
| Figure 5.5 | Deployment topology | one uvicorn process, `/api` + `/` mounts, browser, dashed Neo4j marked *offline evaluation only* | drawn from `backend/app/main.py`; `figures/fig5_5_deployment.svg` |
| Table 5.7 | Environment requirements | OS, Python, packages, port, browser, network, disk | `requirements.txt`, `backend/app/config.py`, measured sizes |

## 5. Boundaries with neighbouring sections

| This section says | Neighbouring section says |
| :--- | :--- |
| Single process and single port (a consequence of ADR-01) | Chapter 4 states ADR-01 itself |
| Neo4j is dashed and offline-only | Chapter 4, Figure 4.2 |
| 150 cases in 1.79 s | Section 6.1.2 must quote the same numbers |
| Partial reproducibility of the evaluation | Section 6.6 (threats to validity), Chapter 7 (limitations) |
| `docs/User_Manual.pdf` is required inside the archive | The manual itself is delivered by the testing chapter |
