# Viva Voce Q&A — Section 5.6 (Liang Zixuan, `50106037`)

## Q1: Why did you choose a single-port Uvicorn + FastAPI `StaticFiles` deployment topology (`Figure 5.5`) instead of Docker Compose with separate Nginx, FastAPI, and Neo4j containers?

- **Answer**: Our target user (`Persona A`, exam candidate studying in library/classroom networks) and course assessors require a **zero-configuration, one-command reproducible PoC** (`R09`, `AD-3`, `NFR-02 < 2.0 s` startup). Requiring Docker Desktop, Nginx, and a live Neo4j container adds $> 1.5\text{ GB}$ of image pulls and port-binding failure modes on university machines. By mounting the zero-build ES6+ `frontend/` directory directly via Starlette's `StaticFiles` after registering `/api/*` routers in `backend/app/main.py`, the entire stack launches on `http://127.0.0.1:8000` in **$0.65\text{ s}$** with zero CORS preflight overhead in production mode.

## Q2: On 25 October 2026 you rotated and scrubbed hardcoded credentials from the repository (`NFR-09`). How do you guarantee that an assessor cloning your ZIP without `.env` keys will not encounter startup crashes?

- **Answer**: We enforce a strict two-tier fallback contract (`AD-1`):
  1. The online PoC runtime (`backend/app/main.py` and `diagnostic_service.py`) defaults to the pre-verified in-memory `QUESTIONS_BY_ID` corpus when `QWEN_API_KEY` is unset, and wraps any optional live LLM call in a 4-second timeout `try...except` block.
  2. The offline audit script `scripts/audit_online_baseline.py` explicitly checks `os.getenv("QWEN_API_KEY")` and exits cleanly with return code `0` (`skipped`) rather than raising a `KeyError` or `401 Unauthorized` exception.

## Q3: Why is `app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True))` placed at the very bottom of `backend/app/main.py`?

- **Answer**: Starlette/FastAPI evaluates routes in registration order. Because `app.mount("/", ...)` is a prefix catch-all for every path starting with `/`, registering it *before* `app.include_router(quiz.router, prefix="/api")` would intercept `/api/questions` and return a `404 Not Found` from the static file handler. Mounting `/` last guarantees that `/api/*`, `/docs`, and `/openapi.json` are matched first by FastAPI's API router table.
