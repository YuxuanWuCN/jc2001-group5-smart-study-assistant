# Oral Defense (Viva) Q&A — Chapter 5.1–5.2 & Appendix D (Jiang Hao, `50106065`)

## Q1: Why does `POST /api/diagnose` use HTTP `POST` when option lookup is deterministic and repeatable?

**Answer:**
> "While reading a static trap is mathematically idempotent, submitting an answer attempt is a **state-changing domain event**: each call to `/api/diagnose` increments session attempt counters (`attempt_count`), updates `trap_distribution` frequencies, and recalculates the 5-axis competency radar in `report_service.py`. Furthermore, sending `question_id` and `selected_option` inside a JSON `POST` body prevents student answers from leaking into URL query strings or browser history logs, and allows future extensions (such as attempt timestamps or confidence ratings) without breaking the endpoint signature."

## Q2: What happens if the frontend sends a nonexistent `question_id` or an invalid option letter like `"Z"`?

**Answer:**
> "Our API contract (`Table 5.2`) strictly separates domain-lookup misses from schema-validation errors, and guarantees **zero unhandled HTTP `500` exceptions**:
> 1. If `question_id` does not exist in `seed_questions.py` (e.g., `"nonexistent_999"`), `diagnostic_service.py` raises a controlled `404 Not Found` (or structured fallback payload verified by `tests/test_adversarial_backend.py` and `tests/test_diagnose.py`).
> 2. If `selected_option` is missing or outside `A`–`D` (e.g., `"Z"` or an SQLi string), Pydantic v2 rejects the payload at the router boundary with `HTTP 422 Unprocessable Entity` before domain code runs."

## Q3: Why are misconception traps bound to individual options (`OptionItem.trap_id -> QuizItem.traps[trap_id]`) instead of the question stem?

**Answer:**
> "Because on a multi-step academic question, **every wrong option represents a different cognitive failure**. For example, on our Civil Law question (`law_1`), choosing Option A (`3 years`) confuses a preclusive period with a limitation period (`Civil Code Art. 188`), whereas choosing Option C (`5 years`) confuses the general 1-year rescission rule with the 5-year long-stop rule (`Art. 152`). If traps were attached to the question stem, both students would receive the same generic explanation. Binding `TrapDetail` (`title`, `desc`, `prereq`, `radar_hit`) to each individual distractor option allows $O(1)$ dictionary lookup of the exact prerequisite the student missed, at the deliberate cost of authoring 36 traps across 12 questions (`seed_questions.py`)."
