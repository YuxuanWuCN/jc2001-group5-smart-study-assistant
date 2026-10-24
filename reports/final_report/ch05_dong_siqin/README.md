# Chapter 5.3 & 5.4 Delivery Package

**Author:** Siqin Dong (50106060) · PoC Logic Developer  
**Deliverable:** Task Pack 06 — Section 5.3 *Question Bank and Trap Engineering* and Section 5.4 *Diagnostic Algorithm* (inside Chapter 5 *Implementation*)  
**Repository Baseline:** `D:\jc2001`, branch `main`, verified against 145/145 passing pytest test cases  
**Step 1 Milestone Date:** Week A Milestone (24 October 2026)

---

## 1. Contents

| File | What it is | Status / Description |
| :--- | :--- | :--- |
| `outline.md` | **Step 1 Outline**: Three-level structure, word budgets, required tables/figures, pseudocode, and oral defense strategies | Complete (exceeds 12-line requirement; fully aligned with Task Pack 06) |
| `sources.md` | **Traceability Matrix**: Maps every quantitative claim, code invariant, and latency metric to exact repository files | Complete (traceable to `seed_questions.py`, `diagnostic_service.py`, `tests/`) |
| `figures/fig5_2_trap_causal_chain.svg` | **Figure 5.2 (Vector SVG)**: Crisp, presentation-ready vector diagram of the distractor diagnostic causal chain | Complete |
| `figures/fig5_2_trap_causal_chain.mmd` | **Figure 5.2 (Mermaid Source)**: Source code for redrawing or markdown preview | Complete |

---

## 2. Quantitative Claims Verified in This Package

| Claim | Verified Value | Authoritative Code Origin |
| :--- | :---: | :--- |
| Primary Question Corpus | **12 items** | `backend/app/data/seed_questions.py` |
| Curated Cognitive Traps | **36 traps** | Primary $12 \times 3$ distractor items in `seed_questions.py` |
| Bijective Trap Mapping | **100% (36/36)** | Every incorrect option maps to an existing `TrapDetail` key |
| Diagnostic Time Complexity | **$O(1)$** | Static dictionary lookup in `diagnostic_service.py` |
| Measured Local Latency | **< 2.5 ms** | Local execution of `POST /api/diagnose` |
| Test Suite Regression Baseline | **145 passed (100%)** | `python -m pytest tests/ -q` (zero regressions) |

---

## 3. Integration Guidelines for Chapter 5 Co-Authors

1. **Alignment with Section 5.2 (Jiang Hao):**  
   The data entities discussed in Section 5.3 (`QuizItem`, `OptionItem`, `TrapDetail`) strictly inherit from `CamelModel` as defined in Jiang Hao's Section 5.2. Terminology and field casing (`radar_hit` / `radarHit`) are strictly synchronised.
2. **Alignment with Section 5.5 (Xi Yusai):**  
   The visual presentation of the diagnostic output (`Trap Drawer`, Socratic reflection card, and ECharts 5D radar chart updates) directly aligns with Xi Yusai's UI design system.
3. **Alignment with Chapter 6 (Yang Mingjie):**  
   The data integrity invariants cited in Section 5.3.4 correspond to the 6 test cases in `tests/test_quiz.py` and the 25 adversarial cases in `tests/test_adversarial_backend.py`.
