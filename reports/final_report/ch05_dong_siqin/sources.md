# Sources — Section 5.3 & 5.4

**Author:** Siqin Dong (50106060) · PoC Logic Developer  
**Scope:** Section 5.3 (*Question Bank and Trap Engineering*) and Section 5.4 (*Diagnostic Algorithm*)

Every quantitative metric, architectural claim, and data schema referenced in `outline.md` is traceable to the authoritative source code files and test suites in this repository snapshot (`D:\jc2001`, branch `main`).

---

## 1. Traceable Repository Source Files

| Repository File | File Size / Lines | Sections Referenced | Verified Claims & Evidence Provided |
| :--- | :---: | :---: | :--- |
| `backend/app/data/seed_questions.py` | 59,653 B / 932 lines | 5.3.1, 5.3.2, 5.3.3, 5.4.1 | **Authoritative Seed Question Bank**: Contains 12 primary multi-choice items across 4 disciplines (Law, CS, Econ, SE). Confirms exactly 36 distractor traps (`traps` dict) with complete `title`, `desc`, `prereq`, and `radar_hit` metadata. Confirms statutory citations in `explanation`. |
| `backend/app/models/quiz.py` | 6,327 B / 181 lines | 5.3.2, 5.3.4 | **Domain Pydantic Schemas**: Defines `QuizItem`, `OptionItem`, and `TrapDetail` with strict bidirectional camelCase/snake_case validation (`CamelModel`) and normalization filters. |
| `backend/app/models/diagnose.py` | 1,842 B / 65 lines | 5.4.1 | **Diagnostic Protocol Contract**: Defines `DiagnoseRequest` (question ID, selected key) and `DiagnoseResponse` (verdict, explanation, Socratic prompt, prerequisite, radar deltas). |
| `backend/app/services/diagnostic_service.py` | 12,669 B / 266 lines | 5.4.1, 5.4.2 | **Dual-Mode Diagnostic Engine**: Implements static $O(1)$ dictionary lookup, local fallback when API key is missing or calls time out (4.0s timeout), and zero unhandled 500 error boundary. |
| `backend/app/services/llm_diagnostics.py` | 14,210 B / 401 lines | 5.4.2 | **LLM Health & Diagnostics Service**: Implements automated probing, error classification, and retry strategies for DashScope Qwen-Turbo connectivity. |
| `backend/app/routers/diagnose.py` | 727 B / 19 lines | 5.4.1 | **REST API Endpoint**: Exposes `POST /api/diagnose` mounted under the FastAPI application shell. |
| `frontend/app.js` | 265,108 B / ~3,100 lines | 5.4.3 | **Client-Side Telemetry Aggregation**: Implements `state.radar` dictionary, instant radar updates (`updateRadarCharts()`), and responsive rendering via Apache ECharts 5.5.1. |
| `tests/test_quiz.py` | 3,450 B / 95 lines | 5.3.4 | **Question Invariant Test Suite**: 6 unit test functions verifying 4 options per question, exactly 1 correct answer, and non-empty `explanation` fields. |
| `tests/test_adversarial_backend.py` | 17,890 B / 523 lines | 5.3.4, 5.4.1 | **Adversarial Resilience Suite**: 25 adversarial test functions verifying invalid question IDs (returns 404), out-of-range option keys (returns 422), malformed JSON payloads, and concurrency safety. |
| `tests/test_llm_health.py` | 9,120 B / 240 lines | 5.4.2 | **Resilience Test Suite**: 36 automated test cases validating graceful offline degradation and retry behavior when external APIs fail. |

---

## 2. Quantitative Measurements and Code Counts

Measurements verified via direct code execution on local runtime baseline (Windows 11, Python 3.13):

| Measured Parameter | Measured Value | Verification Method & File Location |
| :--- | :---: | :--- |
| Primary Question Count | **12 items** | Length of `SEED_QUESTIONS[:12]` in `backend/app/data/seed_questions.py` |
| Primary Option Count | **48 options** | $\sum \text{len}(q.options)$ across 12 primary questions ($12 \times 4$) |
| Unique Cognitive Traps | **36 traps** | Total keys in `question.traps` across 12 questions ($12 \times 3$) |
| Distractor-to-Trap Bijective Mapping | **100% (36/36)** | Automated scan: every option where `is_correct == False` contains a valid `trap_id` resolving in `question.traps` |
| Academic Disciplines | **4 primary** | `law`, `cs`, `econ`, `se` (3 items each in the benchmark baseline) |
| Competency Radar Dimensions | **5 dimensions** | `recall`, `boundary`, `trapDefense`, `synthesis`, `precision` in `backend/app/models/quiz.py` and `frontend/app.js` |
| Algorithm Lookup Time | **< 2.5 ms** | Round-trip latency for local `POST /api/diagnose` execution without external network calls |
| Overall Regression Test Pass Rate | **145 passed (100%)** | `python -m pytest tests/ -q` (executed in 3.58 s) |

---

## 3. Deliberately Acknowledged Limitations (Academic Honesty)

| Limitation | Scope | Why It Is Conceded |
| :--- | :--- | :--- |
| Closed Corpus vs. Open Syllabus | 12 items / 36 traps | The corpus serves as a *proof-of-mechanism feasibility prototype*, demonstrating that fine-grained distractor attribution works. It does not claim statistical curriculum coverage across whole degree programmes. |
| Static Lookup vs. Open Essay Ingestion | Multiple-choice only | Table 5.6 explicitly concedes that generative LLMs outperform lookup tables in open-ended creative essays. Multiple-choice items were deliberately selected to eradicate academic hallucination. |
| In-Session Radar vs. Longitudinal BKT | Single-session aggregation | Radar scores accumulate incrementally during the active browser session. Long-term temporal decay (Ebbinghaus/FSRS) and Bayesian Knowledge Tracing (BKT) are explicitly documented as post-MVP roadmap goals in Chapter 7. |
