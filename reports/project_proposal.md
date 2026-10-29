# JC2001 Software Engineering Project Proposal

## Proposal Title Page

**Course Title**: JC2001 Introduction to Software Engineering  
**Academic Year**: 2026–27  
**Degree Programme**: BSc in Business Management and Information Systems (BSc BMIS)  
**Group Designation**: Group 5  
**Project Title**: To Design and Implement a Smart Study Assistant System for University Students  
**Subtitle**: A GraphRAG and Knowledge Graph Diagnostic Approach to Misconception Remediation and Exam Preparation  
**Academic Supervisor**: Dr. Shahzad Mumtaz (shahzad.mumtaz@abdn.ac.uk)  
**Submission Date**: 25 September 2026  

### Team Member Roster (Group 5)

| No. | Full Name | Student ID | Designated Project Role | University Email |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Yuxuan Wu | 50106070 | Project Manager & Team Lead | u11yw25@abdn.ac.uk |
| 2 | Yongtong Lin | 50106038 | Principal Concept Co-Originator & Lead Domain Analyst | u19yl25@abdn.ac.uk |
| 3 | Sijian Wang | 50106045 | System Architect (UML & Knowledge Graph) | u14sw25@abdn.ac.uk |
| 4 | Hao Jiang | 50106065 | PoC Lead Developer (GraphRAG & Neo4j Engine) | h.jiang.25@abdn.ac.uk |
| 5 | Weixin Xie | 50106034 | Principal Concept Co-Originator & QA Lead | u02wx25@abdn.ac.uk |
| 6 | Zijian Zhang | 50106035 | Business Analyst (User Stories & Acceptance) | u17zz25@abdn.ac.uk |
| 7 | Yusai Xi | 50105989 | UI/UX Designer & Wireframe Lead | u02yx25@abdn.ac.uk |
| 8 | Siqin Dong | 50106060 | PoC Logic Developer (Diagnostic API & Quiz) | u20sd25@abdn.ac.uk |
| 9 | Mingjie Yang | 50106061 | Software Testing & User Manual Lead | u05my25@abdn.ac.uk |
| 10 | Zixuan Liang | 50106037 | Presentation, Media & Deployment Lead | u14zl25@abdn.ac.uk |

---

## 1. Project Title

**To Design and Implement a Smart Study Assistant System for University Students**  
*A GraphRAG and Knowledge Graph Diagnostic Approach to Misconception Remediation and Exam Preparation*

This project aims to help university students deal with revision fatigue and the challenge of mastering large, complex syllabi. Most existing tools focus on passive tasks—storing documents or running keyword searches—but they do little to help students actually understand where their knowledge breaks down. Our approach is different. We combine Retrieval-Augmented Generation (GraphRAG) [1], [2] with structured knowledge graphs built in Neo4j [3] to represent courses as networks of concepts, prerequisites, and common misconceptions. Drawing on Bloom's two-sigma tutoring research [4] and Sweller's Cognitive Load Theory [5], the system is designed to move students beyond rote memorization toward a deeper, more self-aware form of exam preparation.

---

## 2. Problem

Undergraduate students face several recurring problems during exam preparation, and we identified four that are especially damaging.

The most immediate is **cognitive overload from fragmented materials** [5]. Syllabi spread concepts across lecture slides, textbook chapters, and tutorial sheets with no unifying structure. Students end up spending more time locating information than actually learning it.

A related issue is **superficial memorization**. Conventional flashcards encourage students to recall isolated definitions without understanding how ideas connect. This creates a false sense of confidence—what psychologists call the illusion of explanatory depth—and leaves students unprepared for questions that require multi-step reasoning [6].

There is also a lack of **meaningful diagnostic feedback** [7]. When students practise past exams, they usually get a score and a set of correct answers. That tells them what they got wrong, but not why. It does not explain which misconception led to the error or which prerequisite concept needs revisiting.

Finally, general-purpose Large Language Models (LLMs) are unreliable in academic settings due to **knowledge hallucination** [2]. In our own preliminary testing, unguided LLMs produced modest accuracy in analytical subjects (61.00% in Law, 64.91% in Econometrics, 60.26% in Physics), and frequently generated fabricated prerequisites, flawed derivations, or made-up counterexamples. Without structured knowledge constraints, these models can actively mislead students rather than help them.

---

## 3. Solution

Group 5 proposes the **Smart Study Assistant System**, coupling GraphRAG retrieval with Neo4j cloud graph topology, automated diagnostic parsing, Socratic tutoring, dynamic quiz generation, and interactive radar visualization. Crucially, the system directly reduces academic knowledge hallucination rates by grounding generative reasoning onto verified conceptual and prerequisite subgraphs.

### 3.1 Neo4j Knowledge Graph Schema with Misconception Modeling
The system builds on a property graph in Neo4j [3]. Nodes labeled `:Concept` span four functional categories in English: `Core Concept`, `Prerequisite Condition`, `Misconception / Trap`, and `Operational Step`. The primary architectural innovation is the `:DEPENDS_ON` relationship (with property `type: "PRONE_TO_MISCONCEPTION"`), alongside `PREREQUISITE_OF`, `LOGICAL_DERIVATION`, and `COMPUTATIONAL_STEP`. Cypher upsert logic (`MERGE ... ON MATCH SET`) cumulatively aggregates distinct examination traps into enriched conceptual nodes without entity duplication.

### 3.2 Automated Diagnostic Ingestion via Qwen-Turbo
An automated pipeline using the DashScope Qwen-Turbo API ingests multi-disciplinary exam questions. Acting as a logic diagnostic engine rather than a generic answer generator, the model parses multiple-choice and analytical problems into structured JavaScript Object Notation (JSON) format specifying core concepts, strict boundary conditions, and distractor fallacy explanations. Exponential backoff with jitter mitigates HTTP 429 rate limits, and regex sanitization ensures robust JSON extraction.

### 3.3 GraphRAG Socratic Tutoring Engine
To eliminate passive answer copying, the backend implements an active Socratic tutoring engine. When querying a topic, the GraphRAG pipeline retrieves deterministic subgraphs from Neo4j (`LIMIT 40`) constructing explicit logic chains (e.g., (Concept A) -> PRONE_TO_MISCONCEPTION -> (Trap B)). The tutor is strictly constrained to withhold direct answers, instead using graph facts to pose focused Socratic questions (under 150 words) compelling students to identify missing boundary conditions and self-correct [4], [6].

### 3.4 Dynamic Quiz Generation & ECharts 5.5.1 Mastery Visualization
The adaptive quiz engine traverses the knowledge graph to detect fragile prerequisite nodes, dynamically assembling diagnostic quizzes whose distractors map to known misconceptions. Choosing an incorrect option triggers immediate, targeted remediation. The Single Page Application (SPA) frontend integrates Apache ECharts 5.5.1 to project a five-dimensional student mastery radar chart (Basic Recall, Boundary Deduction, Trap Defense, Cross-Topic Synthesis, Calculation Precision) with dark (`#1e293b`) / light (`#ffffff`) theme switching.

### 3.5 Empirical Benchmark Grounding & Noise Arbitration Gate
The proposed architecture is informed by preliminary proof-of-concept benchmarks across twelve academic corpora conducted during the proposal phase. Grounding retrieval in explicit Neo4j knowledge graphs directly suppresses hallucination rates and yields immediate accuracy gains in structured disciplines: **+2.50% in Professional Law** (61.00% to 63.50%), **+2.00% in High School Computer Science** (86.00% to 88.00%), **+1.82% in Public Relations** (72.73% to 74.55%), and **+1.75% in Econometrics** (64.91% to 66.67%). To eliminate knowledge noise and combat academic hallucinations in narrative domains (e.g., Physics divergence), the planned system enforces an Academic Arbitration Gate (`RAG_CONFIDENCE_THRESHOLD = 85`), pruning spurious nodes and hallucinated causal leaps before prompt synthesis.

---

## 4. Objectives

Group 5 defines five concrete objectives adhering to the SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound) concluding on or before **14 December 2026**:

1. **Objective 1 (Functional PoC Delivery)**: Design, develop, test, and containerize a functional Proof-of-Concept Smart Study Assistant system by **14 December 2026**, integrating Neo4j cloud storage, Qwen-Turbo diagnostics, Socratic tutoring, and ECharts 5.5.1 visualization into a runnable bundle.
2. **Objective 2 (Knowledge Graph Scale & Latency)**: Construct a domain graph comprising at least 250 concept nodes, 500 exam questions, and 300 explicit misconception relationships (`PRONE_TO_MISCONCEPTION`), maintaining sub-2.0-second (<2000ms) graph traversal latency on bidirectional Cypher queries (depth $\le 2$, `LIMIT 40`).
3. **Objective 3 (Diagnostic Precision & Hallucination Rate Reduction)**: Achieve automated diagnostic extraction accuracy of $\ge 85\%$ on exam distractors, enforce a strict confidence arbitration threshold ($\ge 85$) filtering out at least 85% of spurious graph relationships, and substantially curtail AI hallucination rates in academic tutoring through deterministic knowledge grounding.
4. **Objective 4 (Software Quality & Test Coverage)**: Engineer the platform under modular object-oriented principles [8], achieving 100% unit test coverage on core Cypher query wrappers, $\ge 80\%$ branch coverage across diagnostic logic with pytest, zero unhandled HTTP 429 exceptions, and full PEP 8 compliance.
5. **Objective 5 (Documentation Compliance)**: Deliver all mandatory JC2001 assessment deliverables by **14 December 2026 at 23:59 CST**, delivering a 40–60 page Technical Report (without raw code), an 8–12 page User Manual PDF, a 15-minute MP4 presentation video with slides, and an Appendix A Workload Profile signed by all ten members.

---

## 5. Benefits

The system delivers measurable value across key educational stakeholders:

### 5.1 Benefits to Students (Primary Stakeholders)
- **Reduced Revision Overhead**: Automated structuring of fragmented notes into a coherent concept graph reduces study collation time by 30–40%.
- **Targeted Trap Remediation**: Mapping questions to directional misconception edges (`PRONE_TO_MISCONCEPTION`) reveals root causes of error, preventing repetitive mistakes [6].
- **Metacognitive Retention**: Socratic dialogue compels students to articulate boundary conditions rather than passively memorizing answers [4].
- **Visual Competency Tracking**: Five-dimensional ECharts radar analytics provide transparent feedback on knowledge gaps, mitigating exam anxiety.

### 5.2 Benefits to Instructors & Teaching Assistants
- **Cohort Misconception Heatmaps**: Aggregated diagnostic logs expose systemic curriculum blind spots, guiding targeted tutorial review.
- **Automated Quiz Generation**: Instructors can dynamically generate diagnostic quizzes aligned with syllabus learning outcomes.
- **Consultation Efficiency & Institutional Value**: Automated remediation of recurring misconceptions frees teaching assistants for higher-order academic mentoring while establishing reusable digital curriculum assets.

---

## 6. Timeline

The project schedule spans four chronological phases from 14 September 2026 to 14 December 2026: Phase 1 (Requirements & Proposal), Phase 2 (Architecture & UML), Phase 3 (PoC Implementation & Verification), and Phase 4 (Final Documentation & Presentation), strictly aligned with JC2001 course milestones:

### Project Milestones Schedule

| Phase | Milestone ID | Milestone Description & Deliverables | Target Completion Date |
| :--- | :---: | :--- | :---: |
| **Phase 1** | **M1.1** | Group Formation, Leadership Election & MyAberdeen Enrolment | 14 September 2026 |
| | **M1.2** | Supervisor Allocation & Formal Kick-off Meeting Briefing | 18 September 2026 |
| | **M1.3** | Formal Project Proposal Submission on MyAberdeen (PDF) | 25 September 2026 |
| **Phase 2** | **M2.1** | Requirements Traceability Matrix & Formal Use Case Modeling | 10 October 2026 |
| | **M2.2** | UML Architectural Design Package & Neo4j Ontology Baseline | 20 October 2026 |
| | **M2.3** | Mandatory Project Update 1 Submission on MyAberdeen | 23 October 2026 |
| | **M2.4** | Mid-Term Architecture Baseline & Supervisor Check-in | 31 October 2026 |
| **Phase 3** | **M3.1** | Mandatory Project Update 2 Submission on MyAberdeen | 06 November 2026 |
| | **M3.2** | GraphRAG Engine & Cloud Neo4j AuraDB Integration | 15 November 2026 |
| | **M3.3** | Dynamic Quiz Generation & ECharts 5.5.1 Mastery Dashboard | 22 November 2026 |
| | **M3.4** | Mandatory Project Update 3 Submission on MyAberdeen | 25 November 2026 |
| | **M3.5** | Multi-Discipline Empirical Benchmarking & Verification Suite | 30 November 2026 |
| **Phase 4** | **M4.1** | Optional Project Update 4 Buffer Submission on MyAberdeen | 04 December 2026 |
| | **M4.2** | Technical Report Master Draft (40–60 pages) & Workload Review | 08 December 2026 |
| | **M4.3** | User Manual PDF (8–12 pages) & PoC Runnable Bundle Packaging | 10 December 2026 |
| | **M4.4** | 15-Minute MP4 Video Recording & Final Presentation Slides | 12 December 2026 |
| | **M4.5** | Final Course Deliverables Submission on MyAberdeen | 14 December 2026 |

---

## 7. Action Plan

The foundational research concept and diagnostic problem formulation of this project were originally initiated by **Yongtong Lin** and **Weixin Xie** (*Principal Concept Co-Originators*). To ensure balanced workload distribution across all ten group members throughout the 12-week development lifecycle, the Work Breakdown Structure (WBS) assigns specific engineering activities linked directly to project objectives:

### Work Breakdown Structure (WBS) Matrix

| WBS ID | Action Activity & Technical Deliverable | Linked Objective | Responsible Member(s) | Student ID | Deadline | Progress Status |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| **WBS 1.1** | Requirements Elicitation & Domain Concept Modeling | Obj 1, 5 | Yongtong Lin, Zijian Zhang | 50106038, 50106035 | 2026-09-25 | Completed |
| **WBS 1.2** | Project Proposal Governance, Editing & Formatting | Obj 5 | Yuxuan Wu, Weixin Xie | 50106070, 50106034 | 2026-09-25 | Completed |
| **WBS 2.1** | Neo4j Graph Ontology & `PRONE_TO_MISCONCEPTION` Schema Specification | Obj 2 | Sijian Wang, Hao Jiang | 50106045, 50106065 | 2026-10-20 | In-progress |
| **WBS 2.2** | UML Class, Sequence, Package & Activity Diagrams | Obj 1, 4 | Sijian Wang, Yusai Xi | 50106045, 50105989 | 2026-10-31 | In-progress |
| **WBS 3.1** | Qwen-Turbo LLM Diagnostic Question Parser & Regex | Obj 3 | Siqin Dong, Hao Jiang | 50106060, 50106065 | 2026-11-15 | In-progress |
| **WBS 3.2** | GraphRAG Retrieval Pipeline & Socratic Dialogue Core | Obj 1, 2 | Hao Jiang, Yuxuan Wu | 50106065, 50106070 | 2026-11-20 | In-progress |
| **WBS 3.3** | Dynamic Quiz Generation & ECharts 5.5.1 Mastery SPA | Obj 1, 3 | Yusai Xi, Siqin Dong | 50105989, 50106060 | 2026-11-25 | Pending |
| **WBS 3.4** | Pytest Test Suite, Cypher Mocks & Stress Backoff | Obj 4 | Mingjie Yang, Weixin Xie | 50106061, 50106034 | 2026-11-30 | Pending |
| **WBS 4.1** | Empirical Benchmark Testing & Noise Filtering Gate | Obj 3, 4 | Weixin Xie, Siqin Dong | 50106034, 50106060 | 2026-12-05 | Pending |
| **WBS 4.2** | Technical Report Authoring (40–60 pages) & Workload Profile | Obj 5 | Weixin Xie, Yongtong Lin, All Members | 50106034, 50106038 | 2026-12-08 | In-progress |
| **WBS 4.3** | User Manual Authoring (8–12 pages) & PoC Deployment ZIP | Obj 1, 5 | Mingjie Yang, Zixuan Liang | 50106061, 50106037 | 2026-12-10 | Pending |
| **WBS 4.4** | 15-Minute MP4 Video Production & Slide Deck Preparation | Obj 5 | Zixuan Liang, Yuxuan Wu, All Members | 50106037, 50106070 | 2026-12-12 | Pending |
| **WBS 4.5** | Final Deliverable Quality Gate & MyAberdeen Submission | Obj 1, 5 | Yuxuan Wu | 50106070 | 2026-12-14 | Pending |

---

## References

[1] P. Lewis et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *NeurIPS*, vol. 33, pp. 9459–9474, 2020.

[2] D. Edge et al., "From local to global: A graph rag approach to query-focused summarization," *arXiv:2404.16130*, 2024.

[3] I. Robinson, J. Webber, and E. Eifrem, *Graph Databases: New Opportunities for Connected Data*, 2nd ed. Sebastopol, CA: O'Reilly, 2015.

[4] B. S. Bloom, "The 2 sigma problem: Methods of group instruction as effective as one-to-one tutoring," *Educ. Researcher*, vol. 13, no. 6, pp. 4–16, 1984.

[5] J. Sweller, "Cognitive load theory and educational technology," *ETR&D*, vol. 68, no. 1, pp. 1–16, 2020.

[6] K. VanLehn, "The relative effectiveness of human tutoring, intelligent tutoring systems, and other systems," *Educ. Psychologist*, vol. 46, no. 4, pp. 197–221, 2011.

[7] P. M. Sadler, "The role of distractor analysis in educational assessment and misconception diagnosis," *J. Educ. Meas.*, vol. 35, no. 3, pp. 211–229, 1998.

[8] I. Sommerville, *Software Engineering*, 10th ed. Boston, MA: Pearson, 2016.
