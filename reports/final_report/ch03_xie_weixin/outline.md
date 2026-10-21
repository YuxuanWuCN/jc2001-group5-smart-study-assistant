# Chapter 3 Use Cases and Requirements Modelling

**Prepared by:** Weixin Xie  
**Course and group:** JC2001 Group 5  
**Deliverable:** Chapter outline and material inventory  
**Status:** Chapter outline accompanying the GitHub handover  
**Date:** 21 October 2026

This chapter will consolidate the existing UC-01 to UC-08 specifications into a coherent report chapter. It will preserve their identifiers, distinguish specified behaviour from verified implementation, and connect the use cases to requirements and validation evidence. It will not duplicate the personal UC-05 to UC-08 document already reproduced in the consolidated file.

The chapter uses the eight confirmed use cases UC-01 to UC-08. Its section structure follows the agreed chapter plan.

## 3.1 System Context and Actors

### 3.1.1 Student Goals and Learning Workflow
Describe how a university student selects practice questions, receives misconception feedback, examines evidence and knowledge relationships, and reviews learning information. Use the existing specifications as the starting point rather than introducing unrelated functions.

### 3.1.2 System Boundary and Supporting Services
Define the browser, local application service, curated question data and optional external tutor service. Establish the implementation snapshot before describing endpoints or technologies. The supplied use-case files describe a standard-library service and JSON/SVG; the Cycle 3 task pack describes a different FastAPI-based snapshot. Do not combine those architectures into one claimed implementation.

### 3.1.3 Actor Responsibilities and Scope Limits
Identify the Student as the primary actor. Include an external model only where it actually participates in an optional interaction. Do not model the marker as an application user solely because they assess the project. Separate delivered functions, partial functions and future targets. Do not introduce login and registration as replacements for existing UC identifiers without an agreed scope change.

## 3.2 Global Use Case Diagram and Summary

### 3.2.1 Diagram Scope and Identifier Consistency
Prepare Figure 3.1 using the same UC-01 to UC-08 identifiers as the consolidated file. Show the system boundary and relevant actors. Label unimplemented or partial functions clearly, or separate future targets visually. Reuse an existing diagram only after checking every node against the selected baseline.

### 3.2.2 Relationships Between Use Cases
Explain any include or extend relationship from the actual interaction and its condition. Assess the relationship between ordinary practice and incorrect-answer diagnosis, and the optional transition from diagnosis to tutor follow-up. Do not infer an include relationship merely because two use cases are related. Confirm the diagram notation and arrow directions before export.

### 3.2.3 Use Case Summary
Prepare Table 3.1 with the use case identifier, name, student goal, primary actor, related requirements and implementation status. Keep the table consistent with the diagram and detailed specifications.

| ID | Existing use case | Planned treatment |
| --- | --- | --- |
| UC-01 | Intelligent Misconception Diagnosis | Explain incorrect-answer feedback and submission failure handling |
| UC-02 | Domain-Based Question Practice and Answer Submission | Explain question selection, navigation, submission and retry |
| UC-03 | Inspect Supporting Evidence and Provenance | Explain evidence, source notes and review status; do not relabel it as implemented free-text search |
| UC-04 | Explore the Question-Specific Knowledge Map | Explain the question-specific graph; verify whether the delivered graph is static or backed by a live service |
| UC-05 | Five-Dimension Learning Analysis | Describe calculation rules and insufficient-evidence targets; verify current coverage |
| UC-06 | Wrong-Answer History | Distinguish stored attempts from a completed history, filter and retry interface |
| UC-07 | Adaptive Supplementary Practice | Retain as an unimplemented target unless new implementation evidence establishes otherwise |
| UC-08 | Socratic AI Tutor Follow-up | Explain contextual guidance, local and external modes, and remaining acceptance gaps |

## 3.3 Detailed Use Case Specifications

All eight descriptions will use a consistent format: ID and name, actor, trigger, preconditions, main success scenario, alternate and exception flows, postconditions, special requirements and acceptance criteria, requirement links and implementation status. Preserve important exceptions and the original meaning when condensing the source material.

### 3.3.1 UC-01 Intelligent Misconception Diagnosis
Use Part A of the consolidated file. Cover valid incorrect options, misconception and prerequisite feedback, duplicate-click controls, request rejection and failed submissions. Verify whether the final implementation stores an attempt and whether it has any independent fallback before claiming either behaviour.

### 3.3.2 UC-02 Domain-Based Question Practice and Answer Submission
Use Part A of the consolidated file. Cover subject filtering, question information, navigation, correct and incorrect submissions, retry and record creation. Check the available domains and actual question and answer endpoints against the selected implementation snapshot.

### 3.3.3 UC-03 Inspect Supporting Evidence and Provenance
Use Part A of the consolidated file. Cover evidence entries, source notes and visible review status. Distinguish project-supplied evidence from completed independent review. Identify cross-topic free-text search as a separate unsupported target if it remains outside the delivered scope.

### 3.3.4 UC-04 Explore the Question-Specific Knowledge Map
Use Part A of the consolidated file. Cover graph display, node selection, detail updates and invalid graph references. Check keyboard interaction separately from a mouse-click smoke test. Do not describe a local JSON/SVG graph as live Neo4j traversal without evidence.

### 3.3.5 UC-05 Five-Dimension Learning Analysis
Use the original personal specification and its reproduced version in Part B. Cover dimensional evidence, scores, counts, empty states, unreadable records and insufficient evidence. Verify the implemented calculation method rather than adopting either a target percentage formula or demonstration score updates as an established fact.

### 3.3.6 UC-06 Wrong-Answer History
Use the original personal specification and Part B. Cover history display, filtering, original attempt details, retry and deletion confirmation as specified targets. Identify which functions are actually delivered. Do not infer a completed history interface merely because local attempt records exist.

### 3.3.7 UC-07 Adaptive Supplementary Practice
Use the original personal specification and Part B. Cover the target recommendation trigger, knowledge-point matching, a different eligible question, explanation of the recommendation and no-match conditions. Preserve the distinction between an isomorphic variant and an ordinary question on the same topic. The source records this function as not implemented; retain that status unless verified new evidence changes it.

### 3.3.8 UC-08 Socratic AI Tutor Follow-up
Use the original personal specification and Part B. Cover question context, student input, guided responses and mode labelling. Treat input-length validation, model failure handling, answer withholding and stale-response protection as acceptance criteria whose implementation must be checked individually. Do not describe all target protections as passed tests.

## 3.4 Behavioural Modelling

### 3.4.1 Question Selection and Answer Submission
Prepare Figure 3.2 as a state or activity model covering question readiness, option selection, a pending request and a completed or rejected submission. Distinguish navigation and retry from a new accepted answer.

### 3.4.2 Correct and Incorrect Feedback Paths
Show the correct branch and the incorrect branch leading to UC-01. Show evidence inspection, the knowledge map or tutor follow-up as optional interactions where appropriate. Include attempt storage only if the chosen implementation supports it.

### 3.4.3 Failure Recovery and Learning Indicator Updates
Model actual request failure behaviour and its effect on answer controls and attempt records. Do not mix the earlier service's error-and-retry behaviour with a later browser fallback unless both are present in the agreed snapshot. Explain why the selected diagram helps describe this interaction.

## 3.5 Requirements Traceability

### 3.5.1 Requirement and Use Case Mapping Method
Describe how requirements link to use cases, design or implementation locations, and acceptance or test evidence. Reconcile the existing FR/NFR references with the Cycle 3 R01-R14 index before assigning final mappings. Different identifier schemes are not interchangeable without an explicit crosswalk.

### 3.5.2 Implementation Coverage and Outstanding Gaps
Report verified, partial, unimplemented and out-of-scope items separately. Refer to executable evidence when available. Do not equate a written acceptance criterion with a passing test, or label an excluded requirement as completed.

### 3.5.3 Appendix B Integration
Place the full requirements traceability matrix in Appendix B and keep the method and coverage discussion in this section. Coordinate requirement wording with the requirements owner and verification evidence with the testing owner. Keep the Chapter 3 summary, Appendix B and Chapter 6 evaluation consistent.

## Planned Figures and Tables

| Item | Purpose | Material or action |
| --- | --- | --- |
| Figure 3.1 | Global use case diagram | Check and revise the existing diagram against UC-01 to UC-08 |
| Table 3.1 | Eight-use-case summary | Consolidate goals, actors, requirement references and status |
| Figure 3.2 | Answer and diagnosis behaviour model | Create from the agreed implementation flow |
| Appendix B | Full requirements traceability matrix | Reconcile requirement schemes and attach implementation and validation evidence |

## Material Inventory

| Material | Planned use | Evidence limit |
| --- | --- | --- |
| reports/use_cases.md | Main baseline for all eight use cases | Combined draft; not proof of implementation |
| reports/add-use-cases-and-rtm-227/use_cases.md | Original UC-05 to UC-08 exceptions, acceptance criteria and status | Already reproduced in the combined file; do not duplicate it |
| reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md in PR 13 | Chapter structure, modelling and traceability deliverables | Conflicts with the existing eight-case scheme |
| reports/cycle3_master_plan.md in PR 13 | Report integration, figure allocation and formatting | Does not resolve implementation conflicts by itself |
| server.py, frontend/app.js, data/curated/questions.json | Check the earlier baseline described by the supplied specifications | Inspect the selected commit before use; earlier notes are not current execution evidence |
| backend/app/main.py, backend/app/routers/, backend/app/services/ | Check the alternative Cycle 3 backend and its actual routes | Use only if this snapshot is selected for the delivered report |
| Existing RTM and current Chapter 2 requirement table | Build the requirement identifier crosswalk | Exact mappings remain to be confirmed |
| Actual test files and execution records | Support acceptance and implementation status | Cite only located tests and results actually obtained |
| reports/figures/fig_use_case_diagram.mmd and exported image | Candidate diagram source | Existing node names and numbering require reconciliation |

## Delivery Basis

The report uses the develop implementation recorded in sources.md and retains the eight existing UC identifiers. The original FR/NFR identifiers and requirement descriptions are retained. See draft.md for the implementation findings and Appendix B for gaps.

Eight use cases are confirmed for this contribution. Cross-chapter alignment is deferred until the other chapters are submitted.
