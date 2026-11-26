# Verification Commands & Evidence — Chapter 7 & Appendices A–D (Wu Yuxuan, `50106070`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify Objectives 1–3 (189 pytest cases passing in < 5s, 0 external calls)
python -m pytest tests/ -q

# 2. Verify Objective 4 (MMLU 12-subject evaluation: 7 wins, 3 ties, 2 losses) and L1–L3 / Persona provenance
python scripts/audit_hallucination_l1_l3.py
python scripts/audit_persona_claims.py
```

## 2. Artefact Anchors

- `Table 7.1a`: Cross-checks all 5 project objectives defined in Chapter 1 (`Table 1.2`) against verified metrics (`17 questions × 51 traps`, `0.65 s` cold start, `189 passed`, `7/3/2` MMLU split, `11/11` member workload).
- `Table 7.1`: Explicitly labels all 3 commercialisation scenarios (`Conservative`, `Baseline`, `Optimistic`) as forward-looking assumptions (`004-persona-hallucination-audit`).
- `Appendix A`: Official 11-member workload profile (`50106070`, `50106038`, `50106035`, `50106034`, `50106045`, `50106065`, `50106060`, `50105989`, `50106037`, `50106061`, `50106012`).
