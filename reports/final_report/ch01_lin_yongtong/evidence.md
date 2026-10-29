# Verification Commands & Evidence — Chapter 1 (Lin Yongtong, `50106038`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify O1 (12 questions x 4 disciplines x 36 traps) and O3 (147 pytest cases passing)
python -m pytest tests/ -q

# 2. Verify Persona Provenance & Claim Audit (E1/E2 evidence levels, zero E0 unverified claims)
python scripts/audit_persona_claims.py

# 3. Verify L1–L3 Hallucination & Quantitative Claim Consistency
python scripts/audit_hallucination_l1_l3.py
```

## 2. Recorded Execution Output

- `python -m pytest tests/ -q` → `147 passed in 0.72s` (verifies `O1`, `O2` API contracts, and `O3`).
- `python scripts/audit_persona_claims.py` → `15 claims audited (E1: 12, E2: 3, E0: 0), 0 violations`.
- `reports/competitor_analysis.md` → Confirms the 5-competitor comparison matrix (Quizlet, Anki, Khanmigo, ChatGPT, Chegg) and 2D positioning axes used in Table 1.1 and Figure 1.2.
- `graphrag（终）/final_systematic_report.csv` → Confirms `O4` empirical split across $n = 4,445$ MMLU items: 7 subjects positive $\Delta$, 3 tied, 2 negative $\Delta$.

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
