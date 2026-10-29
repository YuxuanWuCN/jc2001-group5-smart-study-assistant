# Verification Commands & Evidence — Chapter 4 (Wang Sijian, `50106045`)

## 1. Automated Verification Commands

Run from repository root (`D:\jc2001`):

```powershell
# 1. Verify CamelModel bidirectional snake_case <-> camelCase contract (AD-4, NFR-07)
python -m pytest tests/test_reports.py -k "camel" -v

# 2. Verify Single-Process Static Mount & Health Lifespan (AD-6, R09, NFR-02)
python -m pytest tests/test_health_and_static.py -v

# 3. Verify Full 4-Layer Architectural Integrity across all 147 test cases
python -m pytest tests/ -q
```

## 2. Architectural Artefact & Diagram Verification

- **Figure 4.1 (`figures/fig4_1_context.svg`)**: Verifies System Context Boundary separating `127.0.0.1:8000` single-process runtime from the offline `graphrag（终）/` research pipeline (`AD-1`).
- **Figure 4.2 (`figures/fig4_2_layered_arch.svg`)**: Verifies 4-Layer Modular Monolith (`frontend/` → `backend/app/routers/` → `backend/app/services/ + models/` → `backend/app/data/`).
- **Figure 4.3 (`figures/fig4_3_class_diagram.svg`)**: Verifies UML 2.5 Class Diagram for all 14 `CamelModel` subclasses (`backend/app/models/{common,quiz,report,auth}.py`).
- **Figure 4.4 (`figures/fig_seq_diagnose.svg`)**: Verifies synchronous runtime sequence and `404`/`422` guards for `POST /api/diagnose`.
- **Table 4.1**: Documents all 7 Architecture Decision Records (`AD-1` to `AD-7`) with explicit rejected alternatives and accepted trade-offs (aligned with Week 6 Architecture Review criteria).

## 3. Forbidden Buzzword Check

Checked `draft.md` against the banned vocabulary list (`leverage`, `cutting-edge`, `seamlessly`, `revolutionise`, `empower`, `ecosystem`, `holistic`, `synergy`): **0 matches**.
