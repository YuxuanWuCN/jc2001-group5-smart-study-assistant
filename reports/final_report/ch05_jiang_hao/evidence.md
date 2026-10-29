# Verification Commands & Evidence — Chapter 5.1–5.2 (Jiang Hao, `50106065`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify all 10 API endpoints, Pydantic v2 validation, and CamelModel contracts
python -m pytest tests/test_health.py tests/test_quiz.py tests/test_diagnose.py tests/test_reports.py tests/test_auth.py -v

# 2. Verify CORS headers and same-origin static mounting
python -m pytest tests/test_cors.py tests/test_e2e_frontend.py -v
```

## 2. Code & Schema Anchors

- `requirements.txt` (Lines 1–22): Verifies exact version floors (`fastapi>=0.110.0`, `pydantic>=2.6.0`, `uvicorn[standard]>=0.28.0`, `pytest>=8.0.0`, `httpx>=0.27.0`, `neo4j>=5.18.0`).
- `backend/app/main.py` (Lines 1–50): Verifies `lifespan` startup check, `CORSMiddleware`, 4 router registrations, and `StaticFiles` mount at `"/"`.
- `backend/app/models/{common,quiz,report,auth}.py`: Verifies all 14 `CamelModel` domain classes documented in Table 5.3.
- `reports/api_frontend_mapping.md` & `reports/report_data_contract.md`: Verifies endpoint-to-frontend consumption mapping.
