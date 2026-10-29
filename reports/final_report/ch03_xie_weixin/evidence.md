# Verification Commands & Evidence — Chapter 3 (Xie Weixin, `50106034`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify UC-01 (Question Filtering & Bilingual Fields)
python -m pytest tests/test_quiz.py -v

# 2. Verify UC-02 & UC-03 (Submit Answer, 36 Trap Diagnoses, and 404/422 Exception Flows)
python -m pytest tests/test_diagnose.py -v

# 3. Verify UC-04 (5-Axis Radar Summary, Telemetry Accumulation via «include», and Reset)
python -m pytest tests/test_reports.py -v

# 4. Verify UC-05 (Local Session Authentication & 401/409 Exception Flows)
python -m pytest tests/test_auth.py -v

# 5. Verify UC-06 (Offline Audit Scripts & Optional R10 Skip Behavior)
python scripts/audit_hallucination_l1_l3.py
python scripts/audit_persona_claims.py
python scripts/audit_online_baseline.py
```

## 2. UML 2.5 Alignment Check (Week 5 Lecture 6 & Lab Criteria)

1. **System Boundary**: Explicitly drawn around `UC-01` through `UC-06` in `figures/fig3_1_use_case.svg`.
2. **Actors**: Primary human actors (`Student`, `Evaluator / Developer`) on the left; secondary data/pipeline actor (`Offline Seed & Graph Store`) on the right.
3. **`«include»` Direction**: Dashed arrow points **from base use case `UC-02` to included use case `UC-04`** (`_record_diagnosis` is invoked unconditionally on every `/api/diagnose` call).
4. **`«extend»` Direction**: Dashed arrow points **from extending use case `UC-03` to base use case `UC-02`** with explicit extension point `Wrong Option Selected [correct == False]`.
5. **State Machine**: `figures/fig3_2_state_machine.svg` models all 5 states and guard transitions (`[selected_option == answer]` vs. `[selected_option != answer]`).

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
