# Verification Commands & Evidence — Chapter 5.5 (Xi Yusai, `50105989`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify frontend static asset serving, DOM structure, and API-to-frontend field alignment
python -m pytest tests/test_e2e_frontend.py tests/test_health.py -v

# 2. Verify bilingual fields on all 12 questions and 36 traps + 0-attempt empty state in reports
python -m pytest tests/test_quiz.py tests/test_reports.py -v
```

## 2. Code & Visual Artefact Anchors

- `frontend/index.html`, `frontend/app.js`, `frontend/styles.css`: Implements Principles `P1`–`P3`, the 5-layer slide-out Trap Drawer, the 5-axis Competency Radar, `I18N` bilingual switching (`R07`), and CSS Custom Property dual themes (`R08`, `NFR-06`).
- `reports/api_frontend_mapping.md`: Traces every frontend fetch handler to its backend router and `CamelModel` response field.
