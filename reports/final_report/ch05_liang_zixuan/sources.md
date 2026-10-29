# Sources — Section 5.6

Every factual claim in `draft.md` is traceable to one of the files below. Where a value was obtained
by execution rather than by reading, the measurement conditions are stated. Repository snapshot:
`xin-315/my-first-github`, branch `develop`, head `626d46707f4d3296b354b47c3fcba5d8a80ba1fc`
(read on 19 October 2026).

## 1. Files read

| Path | Size | Used in | Claim it supports |
| :--- | ---: | :--- | :--- |
| `backend/app/main.py` | 2,008 B | 5.6.1, 5.6.3 | Single process; `StaticFiles(directory=..., html=True)` mounted at `/`; three routers under `/api`; permissive CORS middleware |
| `backend/app/config.py` | 1,215 B | 5.6.2, 5.6.3 | `HOST=127.0.0.1`, `PORT=8000` defaults; `QWEN_API_KEY`/`DASHSCOPE_API_KEY` from the environment; `FRONTEND_DIR` |
| `backend/run.py` | 378 B | 5.6.3 | The docstring that documents the start command which fails |
| `requirements.txt` | 435 B | 5.6.2 | Twelve direct dependencies; all `>=`; no pin; "Python 3.10+ compatible" header |
| `README.md` | 4,372 B | 5.6.2, 5.6.3 | The declared Python floor; the quick-start that omits backend startup |
| `.env.example` | 471 B | 5.6.3, 5.6.5 | Which keys exist, and that they ship as placeholders |
| `tests/conftest.py` | 2,791 B | 5.6.4 | The session fixture that deletes `DASHSCOPE_API_KEY` and `QWEN_API_KEY` |
| `tests/*.py` (9 test files) | — | 5.6.4 | 80 test functions → 150 collected cases |
| `backend/app/data/seed_questions.py` | 59,653 B / 657 lines | 5.6.1, 5.6.4 | The question bank is source code, not a database export |
| `frontend/index.html` | 40,390 B | 5.6.1 | Size match with the `GET /` response |
| `graphrag(终)/` (directory) | 17 files | 5.6.4, 5.6.5 | 12 MMLU subject CSVs; `final_systematic_report.csv` (741 B); the evaluation scripts, now reading credentials from the environment |

## 2. Measurements taken by execution

Environment: Windows 11, Python 3.14.0 (virtual environment), localhost only, no credentials
present, 19 October 2026.

| Measurement | Value | How it was taken |
| :--- | :--- | :--- |
| Cold start (process launch → first `200` on `/api/health`) | 1.12 s | uvicorn launched as a subprocess, polled every 50 ms |
| `GET /` | 200, `text/html; charset=utf-8`, 40,390 B, 50.9 ms | direct request against the running service |
| `/api/health` payload | `{"status":"ok","service":"smartstudy-poc","version":"1.0.0","mode":"dual-mode","has_api_key":false}` | direct request; proves offline mode |
| Test suite | `150 passed, 1 warning in 1.79 s` | `python -m pytest tests/ -q` |
| Virtual environment creation | 7.6 s | `python -m venv .venv`, timed with a stopwatch |
| Full dependency installation (`-r requirements.txt`) | 396.7 s, 63 packages, 416 MB environment | fresh virtual environment, `pip install -r requirements.txt`, exit code 0 |
| Minimal installation (7 runtime/test packages) | 43.9 s (9.0 s venv + 34.8 s pip), 32 packages, 50 MB environment | `pip install fastapi uvicorn[standard] pydantic httpx pytest python-dotenv requests` |
| Test suite on the minimal installation | `150 passed in 3.07 s` | proves the trimmed manifest is sufficient |
| Submission archive built and unpacked | 48 entries, 1.05 MB, top-level folder `jc2001-group5-poc/`, no `__pycache__`/`.venv`/`.env` | built from the `develop` snapshot with the four exclusions; unpacked into an empty directory, where `pytest` reported 150 passed and `/api/health` returned 200 |
| Repository size | 3.99 MB extracted; 2.78 MB as ZIP | filesystem measurement of the downloaded archive |
| Virtual environment size | 350 MB (full `requirements.txt`) | filesystem measurement after installation |
| `python backend/run.py` | fails: `ModuleNotFoundError: No module named 'backend'` | executed from the repository root |
| `python -m backend.run` | starts and answers `200` | executed from the repository root |
| `uvicorn backend.app.main:app` | starts and answers `200` | executed from the repository root |

## 3. Not independently verified (stated as claims, not measurements)

| Claim | Why it is not verified here |
| :--- | :--- |
| The evaluation produced the accuracy figures in Chapter 6 | Re-running requires a Neo4j Aura instance; the credential has been rotated. The snapshot `final_systematic_report.csv` is the only traceable artefact |
| RAGAS metric values | Same dependency; see Section 6.4 |
| Installation on macOS and Linux | Only Windows 11 was exercised in this environment |

## 4. Reproducing the measurements

```bash
git clone https://github.com/xin-315/my-first-github && cd my-first-github
python -m venv .venv && .venv/Scripts/activate
pip install -r requirements.txt
python -m pytest tests/ -q          # expect: 150 passed
uvicorn backend.app.main:app --port 8000
```

The figures in Section 2 were produced with this sequence, with no `.env` file present.
