# Viva Q&A — Chapter 7, Reflections & Project Management (Wu Yuxuan, `50106070`)

## Q1: How can you claim commercial viability when manual authoring of 12 questions took 9 hours (`~45 min/question`)?
**Answer**:
> "In `Section 7.2` we openly identify the 45-minute-per-question manual curation bottleneck as our #1 scalability limitation. However, in `Section 7.3.1` (`Table 7.1`) we design a **Human-in-the-Loop (HITL) Trap Authoring Pipeline**: our offline GraphRAG pipeline generates candidate distractor traps (`TrapDetail` drafts) at ~£0.015 per question in LLM tokens, and a domain teaching assistant reviews and approves each card in **8 minutes**—reducing human effort by **82%**. Because runtime diagnosis is an $O(1)$ lookup (`AD-1`), authoring cost is incurred **once per question version** while runtime marginal inference cost remains **£0.00 per 10,000 student clicks**."

## Q2: What was the hardest integration failure across your 10-person team, and how did you prevent it from recurring?
**Answer**:
> "In `Section 7.4` (`Failure 1`) we document our Week 5 `snake_case` vs. `camelCase` serialization failure: Python routers emitted `snake_case` (`trap_defense`) while JavaScript read `camelCase` (`trapDefense`), causing `HTTP 422` errors on option clicks and blank radar vertices. Rather than writing ad-hoc dictionary mappers, we introduced `CamelModel` (`backend/app/models/common.py`) using `ConfigDict(populate_by_name=True, alias_generator=to_camel)` with a dual-key `model_dump()` override, and locked it in with automated regression tests (`test_option_click_dual_naming_convention` in `tests/test_empirical_stress.py`)."

## Q3: Why did you keep the negative Physics result (`-1.32 pp`) in the report instead of filtering it out?
**Answer**:
> "Software engineering integrity (`004-persona-hallucination-audit`) forbids cherry-picking benchmark subsets. More importantly, the `-1.32 pp` regression in `High School Physics` (`Section 7.4`, `Failure 3`) gave us our strongest architectural insight: multi-hop graph neighbours introduce qualitative **neighbour noise** into multi-step algebraic derivations. That negative finding directly justified `AD-1` (decoupling live graph retrieval from the student-facing exam runtime) and motivated `Phase 1` of our 12-month roadmap (`Figure 7.1`, confidence-gated Top-$k$ graph pruning at $\tau = 0.72$)."
