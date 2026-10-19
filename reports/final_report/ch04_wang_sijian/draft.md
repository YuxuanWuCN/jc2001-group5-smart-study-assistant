# 4. System Design and Architecture

## 4.1 Architectural Overview

### 4.1.1 Layered structure and physical deployment

The constraint came first. Twelve weeks, ten contributors, no budget, and a demonstration that has to run on an examiner's laptop with the network switched off. Every decision in this chapter follows from that sentence, and the ones that do not fit it were rejected.

What we built is a layered modular monolith: one `uvicorn` process, one port. Figure 4.1 shows the four layers. Layer 1 is the static front end in `frontend/`. Layer 2 is three FastAPI routers exposing four endpoints. Layer 3 holds the domain services. Layer 4 is a curated question module and the Pydantic models that describe it.

Two properties of this deployment matter more than the layer names. First, there is one process and only one. Second, the running system holds no database, so there is no query, no connection pool and no migration anywhere in it. Layer 4 is a read-only Python module of 657 lines, loaded into memory at start-up.

Front end and API share an origin. `create_app()` registers the routers under `/api` and then mounts `StaticFiles` at the root. A page request and a diagnosis request therefore terminate in the same process. Nothing in the demonstration crosses an origin boundary.

That has a consequence we did not plan for. Because production traffic never crosses an origin, our permissive CORS configuration is never exercised in the deployment we actually demonstrate. It exists for local debugging. It is untested where it would matter. We accept that weakness in AD-6. We do not claim a security property we have not demonstrated.

### 4.1.2 Why a modular monolith

We did not begin with a layered design. The first working service, commit `86dd6d6` on 23 September, was one file. It served static assets, parsed JSON bodies, evaluated answers and generated tutor replies. It worked, and it had one honest advantage: an examiner could read it from top to bottom.

We replaced it because it could not absorb a second contributor. Every new behaviour meant editing the same 228-line handler, and none of the rules could be tested without starting an HTTP server. The layering in Figure 4.1 is the response to that. Routers handle transport and validation. Services hold rules. Models own the schema.

Physical simplicity was a second deliberate objective, not a side effect. One archive, one command, one port. A service mesh would have replaced that instruction with a toolchain prerequisite, and reproducibility is one of the criteria the proof of concept is marked against.

We considered splitting into microservices and rejected it on cost, not on principle. Orchestration, service discovery, cross-service transactions and distributed tracing would all have fallen on ten students in twelve weeks. What they buy is independent scaling, which is worth nothing when the system serves one user on one laptop. Architecture is a response to constraints rather than a measure of sophistication (Sommerville, 2016, ch. 6).

### 4.1.3 Component inventory and responsibilities

Nine components sit across the four layers, and only one of them holds rules.

The presentation layer is three static files and a browser storage key. It renders views and keeps attempt history locally. It knows nothing about traps, scores or dimensions beyond the shape of the JSON it receives.

The API layer is three routers. Two of them are thin by design. The health router returns a fixed identity plus one boolean indicating whether a model key is configured. The LLM health router runs one live probe and reports a classified outcome. The question router normalises subject aliases against a lookup table and applies an optional limit. The diagnosis router validates its request body and delegates immediately.

The domain layer is three services. The question service owns lookup and normalisation. The diagnostic service owns the trap-resolution rules, and it is the only component whose behaviour a marker would call business logic. The diagnostics service classifies external-call failures and has no dependency on anything.

The data layer is the curated question module and the models that describe it.

Table 4.2 states the same inventory as permitted dependencies. We use it as a review instrument rather than an inventory. A component placed on the wrong row would contradict Section 4.1.2, so the table is a fast way to check that the layering claim still holds after a merge.

**Table 4.2 — Component responsibilities and permitted dependencies**

| Layer | Component | Responsibility | May depend on |
| :--- | :--- | :--- | :--- |
| 1 Presentation | HTML shell, stylesheet, script | Render views, hold session state in browser storage | Layer 2, over HTTP |
| 2 API | Health router | Report service identity and key presence | Layer 3 |
| 2 API | LLM health router | Run one live probe, classify the failure | Layer 3 |
| 2 API | Question router | Filter by subject, apply limit, normalise aliases | Layer 3 |
| 2 API | Diagnosis router | Validate the body, delegate the verdict | Layer 3 |
| 3 Domain | Question service | Question lookup and subject normalisation | Layer 4 |
| 3 Domain | Diagnostic service | Resolve the option, read the trap, assemble the response | Layer 4 |
| 3 Domain | LLM diagnostics | Classify external-call failures | Nothing |
| 4 Data | Question module, Pydantic models | Own the schema and the content | Nothing |

The endpoint contract and the field-level schema belong to Chapter 5.2, and we do not repeat them here. The reason for the boundary does belong to this chapter. A router must not hold rules, because rules that live in a router cannot be tested without an HTTP client.

## 4.2 Context and Behavioural Models

### 4.2.1 System context model

Figure 4.2 places three external entities outside the boundary. A context model exists to fix that boundary before any functional decomposition begins (Sommerville, 2016, ch. 5).

The student operates the system, through a browser and nothing else. The instructor does not operate it. We include the instructor because they are a genuine stakeholder in the artefact, and we exclude every teacher-side function because we cut that scope deliberately in Chapter 2. Whether an actor appears in the context model and whether their features are built are separate questions, and we answer them separately.

That separation has a cost we can name. A marker reading only the context model could infer that teacher tooling exists, so Chapter 3 states the boundary explicitly and this chapter does not soften it. Including a stakeholder is not the same as promising them features.

Neo4j AuraDB is the third entity, and it is drawn dashed. The dashes are a decision, not a style. Aura instances sleep when idle, and the presentation room may have no network. A graph call on the demonstration path would turn an environmental problem into an application error at the worst possible moment. We moved the graph off that path. Chapter 6.3 carries the evaluation results that justify keeping it at all.

### 4.2.2 Sequence model for diagnosis

Figure 4.4 traces one diagnosis from the browser to the response. Interaction models of this kind expose ordering and failure paths that a structural diagram hides (Sommerville, 2016, ch. 5). The front end posts a question identifier and a selected option key. The router validates the body against a typed model. From there the diagnostic service resolves the question, finds the selected option, reads its correctness flag, and on a wrong answer reads the trap attached to that option.

What matters most is what the figure leaves out. The diagnosis performs no model inference. It is a dictionary lookup followed by field assembly.

This is a decision with a specific failure in mind. A language model can produce a statute that does not exist, or a formula that holds in general and fails at the boundary the question is testing. Retrieval-grounded generation reduces but does not remove this risk, which is why grounding must be measured rather than assumed (Es et al., 2023). In a teaching tool that is a teaching error, not a quality regression. A lookup table fails differently: it can only be right about questions we wrote, and it cannot invent.

We measured the deterministic core over 720 samples drawn from the 36 wrong-answer cases. The core is question lookup, option resolution and trap lookup. Median was 0.6 microseconds and p95 was 0.7 microseconds. End to end over HTTP on a local `uvicorn` worker, the median round trip was 1.5 milliseconds. Framework and transport overhead account for the gap. We report both numbers instead of choosing the flattering one.

Model calls happen after the verdict. When an answer is wrong and a key is configured, the service asks the model for a short Socratic prompt with a four-second timeout. If the key is absent, the call fails, or the timeout expires, the service returns a prompt assembled from the same reviewed evidence. The verdict is already fixed, so the model can improve the wording and cannot change the answer.

That boundary is the one we would defend hardest in a viva. A deterministic judgement and a probabilistic explanation fail independently.

## 4.3 Domain Class Model

### 4.3.1 Four domain classes and their relationships

Figure 4.3 shows the domain model as it exists in `backend/app/models/quiz.py`. Class models record the relationships that the implementation must enforce, not merely the fields each object carries (Sommerville, 2016, ch. 5).

A question aggregates four options. The shipped set is twelve questions and forty-eight options. Each option carries a key, text, a correctness flag and an optional trap identifier. Correct options carry no trap identifier at all, and that absence is load-bearing. A question is well formed only when exactly three options carry one, so integrity can be checked by counting. The validator uses that property directly.

A trap describes one misconception with four fields: title, description, prerequisite, radar dimension. The set contains thirty-six traps, three per question, matching the three incorrect options. Those four fields are not decorative. Title names the misconception in the student's own vocabulary, description explains it, prerequisite points at what to revise, and dimension tells the interface which axis to move.

Five radar dimensions exist: recall, boundary, trap defence, synthesis and precision. The front end renders them as a five-axis chart. A trap's dimension decides which axis an attempt moves.

A graph structure hangs off the question for the interface to draw as a small knowledge map. We show it in the figure for completeness. It carries no diagnostic weight.

### 4.3.2 The modelling decision that made diagnosis deterministic

Where the trap is attached is the decision that matters, and we had it wrong first.

Attaching traps to the question reads naturally. A question is hard because it tests a misconception, so the misconception belongs to the question. We tried that shape first. It forces the system to decide which misconception a given wrong answer represents, and that decision is inference. The replies we produced under it were plausible and not traceable to anything the student had actually done, which is the defect that pushed us to the option-level model.

Attaching the trap to the option removes the inference. The wrong option already identifies the misconception because we wrote it that way. Diagnosis becomes a lookup from the selected option to its trap record. The answer to "why is this wrong" is stored, not computed.

This is AD-4, and every determinism claim in this chapter rests on it. Once the trap is a column on the option there is nothing to guess. The cost sits in the same table: we can only diagnose misconceptions we anticipated.

## 4.4 Architecture Decision Records

### 4.4.1 Decision record format and evaluation criteria

Table 4.1 records seven decisions, with four fields each: the decision, the alternative rejected, the reason, and the cost we accepted.

The fourth field is the one that does the work. Design rationale is itself a design artefact: a decision recorded without its rejected alternatives cannot be reviewed or revisited (Sommerville, 2016, ch. 6). A decision presented without a cost is usually a decision that was not examined. We therefore read an empty cost column as insufficient thought, not as a good choice. Two entries, AD-6 and AD-7, exist mainly to disclose weaknesses. A report claiming no weaknesses would contradict the results in Chapter 6.

### 4.4.2 What we got wrong

Four things failed first, and they are more informative than the decisions that worked.

**The diagnosis path needed a second answer.** The first `diagnostic_service.py` degraded to the local fallback whenever the live model call failed. That is the right behaviour. It also made failures invisible. A missing key, a revoked key, a rate limit and an unreachable host all produced the same silent fallback. `/api/health` reported only a boolean, so an operator could not tell those four cases apart. Commit `0feb82d` on 10 October added the probe behind `GET /api/health/llm` so they became distinguishable. The comment at the top of `llm_diagnostics.py` states the problem in the words we used at the time.

**Our own diagram went stale.** The sequence diagram we committed on 9 October in `35e6cd4` described a `POST /api/answer` call carrying a `selected` field. Within a day the backend spoke `POST /api/diagnose` with `selected_option`. Both of those endpoint names are now historical: the first no longer exists. The figure was accurate when drawn and wrong when the report was assembled. The figure was accurate when drawn and wrong when the report was assembled. We regenerated every figure from its source for this chapter, and we now treat a figure as a build artefact rather than a document.

**The schema churned.** The diagnosis response changed shape during the first week: `correct` became `is_correct`, `trap_name` became `trap_title`, and structured guidance was added. Rather than freeze the schema early, we made the response model accept both naming conventions. `backend/app/models/diagnose.py` now carries snake-case and camel-case aliases for every field. It is verbose, and it removed a whole category of integration defect between the Python and JavaScript sides.

**Silent exception handling hid real faults.** The original service caught broad exceptions and returned a generic failure. That suppressed the information needed to fix anything, and it is the practice we removed first. Where an exception is caught now, it is classified and logged with a category the operator can act on.

## 4.5 Key Algorithms and Control Flow

### 4.5.1 Startup and request flow

Start-up follows a fixed order. The factory constructs the application and registers CORS. It then includes the three routers under `/api`, and finally mounts the static front end at the root. The order is not cosmetic. The routers are registered before the catch-all mount, so API paths reach a router rather than the static handler.

A request passes four stages. Route matching selects a handler. Pydantic validation admits the body or returns a 422 without reaching business code. The service does its work. The response model serialises the result, including both naming conventions.

That last point cost us a week of avoidable friction, so we state it plainly. Supporting two naming conventions is tedious. It also removed a whole class of client-side defects.

### 4.5.2 Diagnosis control flow

The algorithm is short. That is itself a result.

It resolves the question identifier through an in-memory index. An unknown identifier yields a clearly flagged degraded response rather than an error. It normalises the selected key and scans the options once, capturing both the correct option and the student's option. It compares the two keys. A correct answer returns immediately. A wrong answer reads the trap identifier off the student's option, looks it up in the question's trap dictionary, and assembles the response from the trap's four fields.

Three exits bound the path. An unknown question identifier degrades. An invalid parameter is rejected before the service is entered. Any unexpected exception produces a final defensive response, so the endpoint does not return a server error. We treat a 500 during a live demonstration as unacceptable, and the guard costs one try block.

This section carries the business process model the brief requires. We render it as control flow. A flowchart of eight sequential statements would add a figure and no information.

The second health endpoint is worth one paragraph. It performs a single live probe and classifies the outcome into a stable category with an actionable suggestion. It exists because of the silent-degradation problem described in Section 4.4.2. It never raises, so an unusable key is reported as data rather than as a failure.

## 4.6 Non-Functional Design

The quality attributes in Chapter 2 follow from the decisions in Section 4.4. They are not aspirations attached afterwards, and each traces to a mechanism.

Usability comes from the single page and from progressive disclosure. The diagnostic drawer reveals a trap in layers, so a student meets one idea at a time. Progressive disclosure trades completeness for comprehension, and it is appropriate where the secondary material would distract from the primary task (Nielsen, 2006).

Performance comes from the absence of a database, a network call and a model call on the verdict path. The figures in Section 4.2.2 follow from the design; they were not obtained by optimisation.

Reliability comes from packaging. Static assets and API share a process, so there is no partial deployment in which the page loads and the API does not. Nothing on the demonstration path is external, so a network outage changes nothing.

Security comes from a small surface, not from a security layer. Input is validated by typed models, and there is no SQL to inject into because there is no database. Both are real and both are limited: there is no authentication and no origin restriction, as AD-6 and AD-7 record. We describe the security posture as small and known. It is not strong.

Maintainability comes from the layering and from the test suite. A rule change touches a service. A schema change touches a model. Neither requires editing transport code, and the suite is what lets us check that claim instead of asserting it.

## Figure and table register

Chapter 4 contributes four figures and two tables. The numbers follow the global allocation in `cycle3_master_plan.md` §2.3 and must not be changed locally.

| Number | Title | File | First referenced |
| :--- | :--- | :--- | :--- |
| Figure 4.1 | Four-layer architecture and single-port deployment | `figures/fig_4_1_four_layer_architecture.png` | §4.1.1 |
| Figure 4.2 | System context model | `figures/fig_4_2_context_model.png` | §4.2.1 |
| Figure 4.3 | UML class diagram of the domain model | `figures/fig_4_3_class_diagram.png` | §4.3.1 |
| Figure 4.4 | Diagnose sequence diagram | `figures/fig_4_4_seq_diagnose.png` | §4.2.2 |
| Table 4.1 | Architecture decision records | `table_4_1_adr.md` | §4.4.1 |
| Table 4.2 | Component responsibilities and permitted dependencies | §4.1.3 | §4.1.3 |

Figure 4.3 is the only wholly new technical diagram in this chapter, and the brief requires class diagrams explicitly. Table 4.2 was added during drafting and is not in the global allocation; if the allocation is closed it can be folded into the prose of §4.1.3 without losing content.

## Chapter 4 references

The chapter cites three sources. All three are cited in the running text above and are listed here in Harvard style. The volume editor should merge this list into the consolidated reference list and renumber.

Es, S., James, J., Espinosa-Anke, L. and Schockaert, S. (2023) 'RAGAS: Automated Evaluation of Retrieval Augmented Generation'. *arXiv preprint* arXiv:2309.15217.

Nielsen, J. (2006) 'Progressive Disclosure'. *Nielsen Norman Group*, 3 December. Available at: https://www.nngroup.com/articles/progressive-disclosure/ (Accessed: 19 October 2026).

Sommerville, I. (2016) *Software Engineering*. 10th edn. Harlow: Pearson Education.
