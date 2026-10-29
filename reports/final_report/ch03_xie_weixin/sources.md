# Sources and implementation evidence

## Delivered implementation baseline

Repository: https://github.com/xin-315/my-first-github
Branch: develop
Commit: 626d46707f4d3296b354b47c3fcba5d8a80ba1fc

The user selected the implementation available in GitHub develop as the delivery basis. Commit identifiers are recorded here for reproducibility and are not task or use-case numbers.

## Requirements Documents

- reports/use_cases.md: specifications for UC-01 to UC-08.
- reports/rtm.md: functional and non-functional requirement definitions.
- reports/add-use-cases-and-rtm-227/use_cases.md and rtm.md: original peer specification and traceability extract.
- reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md at PR13 commit fae990e139630e82830982ad3aee374da291693a: chapter and handover structure. Its six-case scheme is superseded in this contribution by the existing eight-case identifiers agreed during review; the group plan should be aligned during integration.

The original specifications describe an older service. They are used as requirement targets, not as proof that the current code delivers their behaviours.

## Inspected implementation files

- frontend/app.js: handleSelectOption, loadQuestion, switchSubject, renderGraph, handleUserChatMessage, radar and localStorage writes.
- backend/app/main.py and routers/: mounted FastAPI API structure.
- backend/app/services/diagnostic_service.py: option mapping and diagnostic fallback.
- backend/app/models/quiz.py and diagnose.py: public response and request fields.
- backend/app/data/seed_questions.py: question and trap schema.
- tests/test_quiz.py, tests/test_diagnose.py, tests/test_e2e_frontend.py: located verification source; not executed acceptance results.

## Verification limits

Static source review and seven key file byte comparisons were completed between develop and PR13. Direct Pydantic model probes confirmed that question serialisation includes answer and traps and that the request model accepts selected option Z. These probes are not HTTP or browser acceptance tests. Full pytest/API/browser/performance execution was not completed because the execution environment lacked pytest, fastapi and httpx. No new test-passing count, performance result or user-study result is claimed.

## Requirement Identifiers

The matrix retains the original FR/NFR identifiers and requirement descriptions. Where identifiers repeat, the requirement description distinguishes the entries. The comparison with R01-R14 records semantic relationships without changing the original requirement meanings.

## Exact source links

- https://github.com/xin-315/my-first-github/blob/626d46707f4d3296b354b47c3fcba5d8a80ba1fc/reports/use_cases.md
- https://github.com/xin-315/my-first-github/blob/626d46707f4d3296b354b47c3fcba5d8a80ba1fc/reports/rtm.md
- https://github.com/xin-315/my-first-github/blob/626d46707f4d3296b354b47c3fcba5d8a80ba1fc/reports/add-use-cases-and-rtm-227/rtm.md
- https://github.com/xin-315/my-first-github/blob/626d46707f4d3296b354b47c3fcba5d8a80ba1fc/frontend/app.js
- https://github.com/xin-315/my-first-github/blob/626d46707f4d3296b354b47c3fcba5d8a80ba1fc/backend/app/models/quiz.py

Eight use cases are confirmed for this contribution. Cross-chapter alignment is deferred until the other chapters are submitted.
