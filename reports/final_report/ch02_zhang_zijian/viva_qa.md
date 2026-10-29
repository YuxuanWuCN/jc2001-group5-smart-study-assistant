# Oral Defense (Viva) Q&A — Chapter 2 (Zhang Zijian, `50106035`)

## Q1: Why did you classify R09 (100% Offline Single-Process Execution) as a "Must Have" functional requirement rather than just a non-functional deployment preference?

**Answer:**
In our project context, 100% offline single-process execution (`R09`) is both an operational requirement for university exam candidates revising in low-connectivity environments (commuter trains, library basements, restricted campus networks) and a strict assessment reproducibility guarantee for markers evaluating `jc2001-group5-poc.zip`. If the application required an active OpenAI/Qwen API key or an external Neo4j server to boot, a marker without cloud credentials would encounter a broken demo (`500 Internal Server Error`). Elevating `R09` to a `Must Have` functional requirement forced us to decouple offline GraphRAG evaluation from the runtime FastAPI service (`AD-1`).

## Q2: You cut R12 (Live Cloud LLM Generation on the Runtime Critical Path) as "Won't Have". Doesn't removing live LLM calls make your system less "intelligent" than ChatGPT?

**Answer:**
Quite the opposite—for structured exam misconception diagnosis, **deterministic precision beats unconstrained generation**. Our own offline evaluation across 4,445 MMLU items (`Chapter 6.3`) proved that live LLM/GraphRAG generation suffers from $1.5\text{–}4.0\text{ s}$ latency and can degrade accuracy when retrieved graph neighbours introduce noise (e.g., `-4.39%` in Econometrics). By pre-engineering and expert-verifying all 36 distractor traps (`TrapDetail`) offline and serving them in memory (`P95 < 5 ms`), we guarantee zero statutory hallucination, zero answer-spoiling, and £0.00 marginal cost while retaining an optional online comparison hook (`R10`, `scripts/audit_online_baseline.py`).

## Q3: How did you ensure that your Non-Functional Requirements (Table 2.2) followed IEEE 830 / Sommerville standards rather than vague marketing claims?

**Answer:**
Every NFR in Table 2.2 is bound to a **numerical threshold** and an **automated or auditable verification method**. For example, instead of writing *"The system should respond quickly"*, `NFR-01` specifies `POST /api/diagnose` P95 latency $< 5.0\text{ ms}$ (verified at $3.4\text{ ms}$). Instead of *"The system should handle bad inputs gracefully"*, `NFR-04` requires zero `500 Internal Server Error` responses across 36 adversarial payloads in `tests/test_adversarial.py`. Instead of *"The UI should be readable"*, `NFR-06` specifies WCAG 2.1 AA contrast ratios ($\ge 4.5:1$), verified directly against our CSS custom property hex values in `frontend/styles.css`.
