# JC2001 Group 5 Project and Week 3 Planning Assumptions Log

**Project Name**: Smart Study Assistant System for STEM Undergraduates Based on Knowledge Graphs and Intelligent Troubleshooting  
**Course Code**: JC2001 Introduction to Software Engineering (2026–27)  
**Document Path**: `reports/assumptions.md`  
**Last Updated**: October 17, 2026  
**Baseline References**: `JC2001-GroupProjectDescription-and-Requirements-2026-27(1).pdf` and the existing PoC baseline

---

## 1. General Principles for the Boundary Between Facts and Assumptions

In line with software engineering norms and review discipline, the team strictly distinguishes "verified facts" from "inferred/stage assumptions", and prohibits treating unverified speculation as a basis for completion:

- **Verified Facts (Facts)**: Code that actually runs, automated tests that have been executed and passed (e.g., 114 pytest test cases), official course specification text, archived diagrams, or submitted proposals.
- **Stage Assumptions (Assumptions)**: Preconditions and expectations set at the current stage (Week 3 / M2.2 preparation period) to advance design and division of labor; these must later be confirmed, validated through user testing or integration testing, and thereby promoted or corrected.

---

## 2. List of Key Assumptions and Their Impact on Conclusions

| ID | Core Assumption (Assumption) | Grounding Fact | Impact on Conclusions/Architecture/Deliverables | Validation/Promotion Method | Current Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **ASM-01** | **"Half-complete" for the Reports module means the core business main flow is connected end to end (50% of the core path), not an accumulation of all features** | Supervisor feedback requires that it "looks too AI-made; bring reports to at least half progress next cycle" | The team concentrates on one vertical slice: "time/scope filtering -> core learning-progress metrics -> trends and distributions -> data source/timestamp", rather than spreading effort across ineffective static pages. | Report this definition to the supervisor early this week and obtain approval. | Pending confirmation (Pending) |
| **ASM-02** | **Learning-progress data in the Week 3 PoC stage may use clearly labeled Session / Mock data services** | The project is currently in the Phase 2 architecture design stage; the real cloud Neo4j full graph and persistent student answer logs are scheduled to go live in Phase 3 (M3.2) per the Proposal | Avoid over-engineering by forcing a heavy database into Week 3; the API explicitly returns `source: "mock"` or `source: "session"`, honestly reflecting the current stage of technical evolution. | The supervisor confirms that labeling mock data in the prototype stage is allowed; replace it with a real data source before final integration testing. | Active |
| **ASM-03** | **Reports prioritizes student self-diagnosis (Student Persona) over a teacher-facing dashboard** | The core goal in the Proposal is to help undergraduates cope with review overload and locate error causes; the current PoC is a student-side console | Defer the teacher-side class-level macro heatmap (Cohort Heatmap) in Week 3 to prevent scope creep from leaving both sides unfinished. | Include as question 2 in the Week 3 question list to confirm with the supervisor. | Active |
| **ASM-04** | **For the 40–60 page technical report, Week 3 only needs a locked-down skeleton and first drafts of core chapters (about 15–20 pages)** | The official grading criteria require the Technical Report to be submitted at the end of term, with 40–60 pages of body text, excluding code | Prevent team members from padding word counts while requirements and architecture are not yet frozen; Week 3 focuses on structure, the requirements traceability matrix (RTM), and core figures. | Align with the course's Week 6 pace and end-of-term progress requirements. | Active |
| **ASM-05** | **Local one-command startup (FastAPI + Vanilla JS SPA) meets the "Runnable Software" requirement in the PoC assessment** | The official PoC specification (Page 7) requires "Complete source code required to run and evaluate... does not need to be production-ready" | The team does not need to maintain a Docker/K8s cluster, lowering the barrier for team members to run the project and preserving the simplicity of high-quality undergraduate-level code. | Provide local one-command startup and test verification steps in the User Manual. | Active |
| **ASM-06** | **Socratic questioning (not directly revealing answers) is the core academic moat that distinguishes the system from conventional AI assistants** | Official grading emphasizes "Consistency with Technical Report" plus project innovation and educational value | The diagnosis API must maintain question-based elicitation under any degraded mode and must not print the standard answer directly just because the graph lookup misses. | Incorporate into the automated test contract (e.g., assertions in `test_diagnose.py`). | Active |

---

## 3. Contingency Plans for Assumption Failure

1. **If the supervisor insists that Reports must have real database storage**:
   - Immediately enable SQLite as a lightweight single-machine transitional database to record students' local answer logs; estimated additional effort of 3–4 hours, with no impact on the overall architecture.
2. **If the supervisor requires Reports to include a teacher perspective**:
   - Reserve a "role switch (Student / Instructor Preview)" simulated view in the frontend, and honestly state in the report that teacher aggregate data are algorithmic simulation samples.
