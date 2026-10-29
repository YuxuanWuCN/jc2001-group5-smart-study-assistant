# Oral Defense (Viva) Q&A — Chapter 3 (Xie Weixin, `50106034`)

## Q1: In Figure 3.1 (Use Case Diagram), why does the dashed arrow for `«include»` point from `UC-02` to `UC-04`, whereas the dashed arrow for `«extend»` points from `UC-03` back to `UC-02`?

**Answer:**
Under UML 2.5 semantics (as covered in Week 5 Lecture 6 and the Use Case Lab), arrow direction represents **dependency direction**:
1. **`UC-02 ──«include»──► UC-04`**: `UC-02` (*Submit Answer & Trigger Diagnosis*) depends unconditionally on `UC-04` (*Update Session Telemetry*). In `backend/app/routers/diagnose.py`, every valid submission calls `_record_diagnosis(question_id, result.correct, trap_title)` before returning `DiagnoseResponse`. Therefore, the base use case (`UC-02`) points to the included sub-use case (`UC-04`).
2. **`UC-03 ──«extend»──► UC-02`**: `UC-03` (*Inspect Knowledge-Graph Prerequisite Subgraph & Socratic Prompt*) is **conditional**: it executes only at the extension point `Wrong Option Selected [correct == False]`. When a student selects the right answer (`correct == True`), `UC-02` completes without invoking `UC-03`. Because `UC-02` is self-contained and unaware of optional extensions, the extending use case (`UC-03`) points back to the base use case (`UC-02`).

## Q2: Walk us through the exception flows of `UC-02` when a client sends malformed input. How are they verified?

**Answer:**
`UC-02` defines two distinct exception flows mapped to exact HTTP status codes in `backend/app/routers/diagnose.py` and `backend/app/models/quiz.py`:
1. **Invalid Option Format (`HTTP 422 Unprocessable Entity`)**: `DiagnoseRequest.selected_option` enforces the Pydantic v2 regex pattern `^[A-D]$`. If a client submits `"E"`, lowercase `"a"`, an empty string `""`, or an injection payload, FastAPI rejects the request at the schema boundary with HTTP `422` before reaching `diagnostic_service.py`.
2. **Unknown Question Identifier (`HTTP 404 Not Found`)**: If `selected_option` is valid (`"A"`–`"D"`) but `question_id` does not exist in `QUESTIONS_BY_ID` (e.g., `"nonexistent_99"`), `diagnose_answer()` raises `KeyError`, which the router translates into HTTP `404 Not Found` (`{"detail": "Question 'nonexistent_99' not found"}`).
Both exception flows are verified across 30 test cases in `tests/test_diagnose.py` and 36 adversarial cases in `tests/test_adversarial.py`, with zero unhandled `500` errors.

## Q3: Why did you model a Behavioural State Machine (Figure 3.2) in addition to the Use Case Diagram (Figure 3.1)?

**Answer:**
Use case diagrams capture *static boundary interactions* between actors and system functions, but they do not show *temporal state transitions* or guard conditions within an active study session. Figure 3.2 models the five internal states of a question attempt (`Idle / Browsing` → `Question Active` → `Option Selected` → `Submitting & Validating` → guarded branch into `Correct Verified` or `Trap Diagnosed` → `Telemetry Updated`). Explicitly modelling these guard conditions (`[selected_option == answer]` vs. `[selected_option != answer]`) directly guided our frontend state machine in `frontend/app.js` and prevented UI race conditions such as stale trap drawers remaining open when switching questions.
