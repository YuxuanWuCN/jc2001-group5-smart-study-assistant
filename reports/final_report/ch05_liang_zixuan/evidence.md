# Evidence & Verification Commands — Section 5.6 (Liang Zixuan, `50106037`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify single-port FastAPI launch & StaticFiles mount
python backend/run.py

# 2. Verify 147 automated pytest cases pass offline
python -m pytest tests/ -q

# 3. Verify zero hardcoded credentials and clean online-baseline fallback
python scripts/audit_online_baseline.py
```

## 2. Key Code & Document Anchors

- `backend/app/main.py`: FastAPI application factory, CORS middleware, `/api/*` router mounting, and `StaticFiles(directory=FRONTEND_DIR, html=True)` mount at `/`.
- `backend/run.py`: Uvicorn single-port (`127.0.0.1:8000`) bootstrap entry point.
- `requirements.txt` & `.env.example`: Reproducible dependency manifest and environment variable template (`QWEN_API_KEY`, `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD`).
- `figures/fig5_5_deployment.svg`: Vector deployment topology diagram (`Figure 5.5`).
