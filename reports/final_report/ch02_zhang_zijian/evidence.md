# Verification Commands & Evidence — Chapter 2 (Zhang Zijian, `50106035`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify R01-R09 and NFR-01/NFR-04/NFR-07/NFR-09 across all 147 pytest cases
python -m pytest tests/ -q

# 2. Verify R10 (Optional Online LLM Baseline Audit Hook exits 0 when QWEN_API_KEY is absent)
python scripts/audit_online_baseline.py

# 3. Verify NFR-10 (Persona & Hallucination Provenance Contracts)
python scripts/audit_persona_claims.py
python scripts/audit_hallucination_l1_l3.py
```

## 2. Requirement-to-Test Mapping Summary

- `R01`: `tests/test_quiz.py` (`TestGetQuiz` — 9 cases verifying 12 items, 4 categories, and empty-list fallback).
- `R02` & `R03`: `tests/test_diagnose.py` (66 cases verifying 12 correct submissions, 36 wrong-option `TrapDetail` payloads, and `404`/`422` error contracts).
- `R04` & `R05`: `tests/test_reports.py` (30 cases verifying 5-axis radar bounds $[0, 100]$, session telemetry accumulation, `data_source` provenance, and `/api/reports/reset`).
- `R06`: `tests/test_auth.py` (16 cases verifying login, registration, `/api/auth/me`, logout, and `401`/`409` handling).
- `R07`, `R08`, `R09`: `tests/test_health_and_static.py` (6 cases) + `tests/test_adversarial.py` (36 cases).
- `R10`: `scripts/audit_online_baseline.py` returns exit code `0` (`skipped`) when `QWEN_API_KEY` is unset.

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
