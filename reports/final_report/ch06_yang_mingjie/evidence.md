# Verification Commands & Evidence — Chapter 6 & Appendix C (Yang Mingjie, `50106061`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify all 10 test modules (105 functions -> 189 collected cases) pass 100% offline
python -m pytest tests/ -q

# 2. Verify Adversarial Backend Suite (25 functions / 523 lines) & Empirical Stress Suite
python -m pytest tests/test_adversarial_backend.py tests/test_empirical_stress.py -v

# 3. Verify MMLU 12-Subject CSV Integrity & L1-L3 Hallucination Audit
python scripts/audit_hallucination_l1_l3.py
python scripts/audit_persona_claims.py
```

## 2. Authoritative Repository Evidence Anchors

- **Test Suite Inventory (`Table 6.1`, `Figure 6.1`, `Appendix C.1`)**:
  - `tests/test_health.py` (5 functions)
  - `tests/test_quiz.py` (6 functions)
  - `tests/test_diagnose.py` (8 functions)
  - `tests/test_reports.py` (11 functions = 7 baseline + 2 `CamelModel` dual-key regression tests added 2026-10-25 + 2 session-telemetry aggregation tests added in the final hardening pass)
  - `tests/test_auth.py` (12 functions)
  - `tests/test_cors.py` (4 functions)
  - `tests/test_e2e_frontend.py` (8 functions)
  - `tests/test_adversarial_backend.py` (25 functions, 523 lines)
  - `tests/test_empirical_stress.py` (7 functions)
  - `tests/test_llm_health.py` (19 functions, 380 lines, 36 cases)
  - **Total**: 105 functions expanded via `@pytest.mark.parametrize` to **189 passed cases** (145 frozen baseline → 147 after the dual-naming regressions → 183 after `test_llm_health.py` → 189 after the final hardening pass).
- **MMLU Empirical Benchmark (`Table 6.3`, `Figure 6.2`)**:
  - `graphrag_final/final_systematic_report.csv` (12 MMLU subsets, $n = 4,445$ items):
    - **7 Positive Gains**: `Professional Law` (`+2.50 pp`), `HS Computer Science` (`+2.00 pp`), `Public Relations` (`+1.82 pp`), `Econometrics` (`+1.75 pp` / `+1.76 pp`), `Miscellaneous` (`+0.50 pp`), `HS Biology` (`+0.50 pp`), `Professional Psychology` (`+0.50 pp`).
    - **3 Ties**: `Electrical Engineering` (`0.00 pp`), `Human Aging` (`0.00 pp`), `World Religions` (`0.00 pp`).
    - **2 Negative Deltas**: `HS US History` (`-1.00 pp`), `HS Physics` (`-1.32 pp`).
- **RAGAS Evaluation Script (`Table 6.4`)**:
  - `graphrag_final/ragas_evaluator.py` (96 lines): Multi-model benchmark loop (`glm-4-flash`, `glm-4-air`, `glm-4-plus`) with exponential backoff (`safe_request`) and checkpointing (`final_comparison.csv`).

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
