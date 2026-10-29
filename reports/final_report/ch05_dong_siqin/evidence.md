# Verification Commands & Evidence — Chapter 5.3–5.4 (Dong Siqin, `50106060`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify all 36 distractor traps (12 questions x 3 wrong options) return valid TrapDetail + GraphData
python -m pytest tests/test_diagnose.py -v

# 2. Verify bijective 1:1 distractor-to-trap mapping (answer key excluded from traps, 4 options per item)
python -m pytest tests/test_quiz.py -v

# 3. Verify offline GraphRAG pipeline & MMLU 12-subject CSV integrity
python scripts/audit_hallucination_l1_l3.py
```

## 2. Code & Data Artefact Anchors

- `backend/app/services/diagnostic_service.py` (Lines 1–46): Implements `diagnose_answer(question_id, selected_option)` via $O(1)$ hash lookups in `QUESTIONS_BY_ID` and `item.traps`.
- `backend/app/data/seed_questions.py` (Lines 1–1257): Defines `SEED_QUESTIONS` (12 items across `law`, `cs`, `econ`, `se`, 36 `TrapDetail` instances, and 12 embedded `GraphData` subgraphs) and `QUESTIONS_BY_ID`.
- `graphrag（终）/graphrag_pipeline.py` (Lines 1–787): Implements the 12-stage offline GraphRAG research pipeline (`Stage 1` entity extraction through `Stage 12` answer synthesis).

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
