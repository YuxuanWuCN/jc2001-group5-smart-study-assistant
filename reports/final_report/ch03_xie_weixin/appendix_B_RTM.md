# Appendix B Requirements Traceability Matrix

This matrix links requirements to use cases, implementation locations and verification evidence. Implementation findings are based on source inspection. API, browser and performance acceptance tests have not been executed.

| Requirement ID and description | Use case | Implementation evidence | Verification evidence | Status and gap |
| --- | --- | --- | --- | --- |
| FR-01 / Select a study domain | UC-02 | switchSubject; initSubjectSelector | test_quiz.py; not executed | Subject flow present; UI unexecuted |
| FR-02 / Submit one answer per on-screen attempt | UC-01, UC-02 | handleSelectOption; models/quiz.py | test_diagnose.py; not executed | Answer flow present; public quiz exposes answer and traps |
| FR-03 / Identify misconception and missing prerequisite | UC-01 | diagnostic_service.py; seed_questions.py | test_diagnose.py; not executed | Option mapping present; content accuracy not independently checked |
| FR-05 / Inspect evidence, source and content-review status | UC-03 | Question renderer and model fields inspected | No dedicated provenance test found; not executed | Source/review-status workflow not established in current renderer |
| FR-06 / Inspect question-specific knowledge subgraph | UC-04 | renderGraph in app.js | No node-detail acceptance test established; not executed | Graph rendering present; node click/detail and keyboard not established |
| NFR-01 / Secure API and credential handling | UC-01, UC-02 | models/quiz.py; routers/quiz.py | test_quiz.py is not proof of hidden keys; not executed | Gap: quiz response model exposes answer, explanation and traps |
| NFR-02 / Local reliability / no cloud dependency | UC-01, UC-02 | handleSelectOption local fallback | test_diagnose.py (backend); not executed | Local data fallback exists; clean-machine air-gap test pending |
| NFR-03 / Transparent diagnosis and provenance | UC-01, UC-03, UC-04 | diagnostic_service.py; question rendering | test_diagnose.py; not executed | Diagnosis supported; provenance/review display gap |
| NFR-04 / Keyboard accessibility | UC-02, UC-04 | renderGraph; option-card div creation | No keyboard audit executed; not executed | Keyboard acceptance not established |
| NFR-05 / Responsive layout | UC-02, UC-04 | frontend/style.css | No viewport run executed; not executed | Responsive styles only; acceptance pending |
| NFR-06 / Reproducible provenance and evaluation | UC-03 (evidence linkage) | Evidence schema and renderer inspection | No controlled evaluation executed; not executed | Old provenance/evaluation workflow not established |
| NFR-07 / Local performance | UC-01, UC-02 | Local endpoints | No benchmark executed; not executed | Timing target not verified |
| NFR-08 / Modular software organisation | UC-01–UC-04 | backend/app/routers and services; frontend/ | Existing test source only; not executed | Modular source present; reproducibility run pending |
| FR-04 / Five-dimension learning radar and mastery analysis | UC-05 | state.radar; updateRadarCharts | No dimension acceptance run; not executed | Partial: fixed initial scores and heuristic deltas, not target correct-rate formula |
| FR-05 / Socratic guided follow-up | UC-08 | handleUserChatMessage; getLocalSmartReply | No tutor acceptance run; not executed | Partial: local/online chat; provider failure shows error rather than local chat fallback |
| FR-06 / Same-knowledge-point variant or supplementary question recommendation | UC-07 | No recommendation flow located | No recommendation test established; not executed | Not implemented in inspected workflow |
| FR-07 / Search, filter and retry historical wrong answers | UC-06 | localStorage writes; navigation functions | No history acceptance test established; not executed | Persistent attempt history, filters and retry archive not established |
| FR-08 / Traceable question evidence, source and review status | UC-05, UC-07, UC-08 | Question rendering and quiz model | No provenance acceptance test established; not executed | Evidence/source/review-status workflow not established |
| FR-09 / Hints and student-requested explanations | UC-05, UC-08 | handleSelectOption result drawer | No request-only disclosure acceptance run; not executed | Gap: explanation may appear automatically; correct option highlighted |
| FR-10 / Save, read and clear learning records | UC-05, UC-06, UC-07 | All localStorage.setItem calls reviewed | No persistence/deletion run; not executed | Settings/profile writes found; persistent attempts and confirmed deletion not established |
| NFR-02 / Fallback behaviour when an external model or service fails | UC-05, UC-06, UC-07, UC-08 | Answer fallback and tutor exception branches | test_diagnose.py covers backend fallback; not executed | Partial: answer/backend fallback differs from tutor chat recovery |
| NFR-03 / Usability and accessibility | UC-05, UC-06, UC-07, UC-08 | initTheme; result drawer labels; renderGraph | No accessibility run executed; not executed | Theme and text feedback present; full accessibility unverified |
| NFR-04 / Learning-record privacy and answer protection | UC-05, UC-06, UC-07, UC-08 | models/quiz.py; localStorage writes | No privacy acceptance run; not executed | Gap: public answer/traps; attempt deletion not established |
| NFR-07 / Clear explanations without overstating results | UC-05, UC-07, UC-08 | state.stats; state.radar; loadQuestion | No clarity acceptance run; not executed | Gap: demonstration values; no verified insufficient-evidence threshold |
| NFR-08 / Mobile and desktop support | UC-05, UC-06, UC-07, UC-08 | frontend/style.css | No mobile/desktop browser run; not executed | Responsive styles present; viewport acceptance pending |
