# Feature Specification: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Feature Branch**: `feature/cycle3-startup-report-plan`
**Created**: 2026-10-18
**Status**: Ready for planning
**Input**: The third-cycle plan approved by the user (team lead Yuxuan Wu) after confirming the current project state: move the final Technical Report, worth 50% of the grade, from "0 pages" to "a submittable startup-grade technical and delivery report", and break it into 9 executable task packs for team members plus a set of team-meeting Q&A defence material.

> **No new features this cycle.** The software baseline is frozen (8 API endpoints, 145 test cases, 12 questions / 36 traps, 3 UML diagrams). The only deliverable this cycle is **text**: one 40–60 page English technical report, 9 member task packs, and 1 supervisor Q&A library.

---

## 1. Background and Problem Statement

The supervisor (Dr. Shahzad Mumtaz) judged the existing deliverables as follows: **the system is too advanced - it does not look like a startup project, but like an agent system built by AI agents**; and explicitly required **turning the project report into a startup-company report**.

Three verifiable current constraints:

| # | Constraint | Evidence |
| :-: | :--- | :--- |
| C1 | The Technical Report accounts for **50%** of the group mark (= 25% of the total course mark), and the current actual progress is **0 pages** | Official Brief; no final report directory under `reports/` |
| C2 | Code and system knowledge are **concentrated in the team lead alone**; the other 9 members did not participate in writing | User's own account (m00107) |
| C3 | The team lead's biggest fear is **being unable to answer the supervisor's questions at the team meeting** | User's own account (m00107) |

Hence three problems that must be solved simultaneously: **(P1) the report cannot be written; (P2) team members cannot contribute; (P3) the team meeting cannot be justified.**

---

## 2. User Scenarios and Acceptance Criteria

### US-1 · Report Lead Author (team-lead perspective) P1

> As the team lead, I need a report blueprint in which **chapter structure, page budgets, figure/table numbering, and owners are all locked down**, so I do not have to make structural decisions repeatedly while writing.

**Acceptance Criteria**:
- **AC-1.1** The report chapters **strictly align with the seven-chapter order of the official Brief**, with no chapter added or omitted: ① Introduction and Project Context ② Functional and Non-Functional Requirements ③ Use Cases and Requirements Modelling ④ System Design and Architecture ⑤ Implementation ⑥ Testing and Evaluation ⑦ Conclusions and Future Work → References → Appendix A Group Workload Profile.
- **AC-1.2** Every chapter has a **page budget**, with body text totalling **40–60 pages** (excluding front matter / references / appendices).
- **AC-1.3** Figure and table numbering across the document is **unique and continuous** (17 figures / 21 tables); the numbering table is produced together with the blueprint, and ad-hoc number additions are not allowed later.
- **AC-1.4** The blueprint explicitly states where the **six official mandatory content items** go in Chapter 1: problem / background / objectives / intended users or stakeholders / main features / potential practical or business value.
- **AC-1.5** The blueprint explicitly states where the **five official NFR categories** go in Chapter 2: usability / performance / reliability / security / maintainability.
- **AC-1.6** The blueprint explicitly states that Chapter 6 must contain **an evaluation subsection that checks against the Chapter 2 requirements item by item** (officially specified action).

### US-2 · Member Task Packs (member perspective) P2

> As a team member, I need a task pack that is **foolproof enough that I need not ask anyone**: I know which pages I own, what each subsection should say, which repository file holds the source material, which writing styles will be rejected, and what the supervisor might ask me.

**Acceptance Criteria**:
- **AC-2.1** Each of the 9 members receives **one task pack**, with the filename containing the chapter number and name, stored in `reports/cycle3_task_packs/`.
- **AC-2.2** Each task pack must contain seven fixed items: ① owner and page budget ② a one-sentence delivery goal ③ section-by-section structure and word count ④ source-material path table (clickable repository-relative paths) ⑤ list of pitfalls that will cause rejection ⑥ acceptance checklist (DoD) ⑦ supervisor's 3 questions + 30-second answers.
- **AC-2.3** Each task pack includes **two deadlines**: outline (Sunday 23:59 of Week A) and draft (Sunday 23:59 of Week B).
- **AC-2.4** All numbers in the task packs (endpoints / tests / question bank / MMLU) must match the repository's current state; **no numbers invented from memory**.
- **AC-2.5** A master index `README.md` exists, containing the division-of-labour table, the two-step delivery cadence, the WeChat-group distribution script, whole-team writing conventions, and the frozen requirement IDs R01–R14 and figure/table numbers.
- **AC-2.6** Task packs must **forbid fabricating data** and explicitly state the substitute wording (see §4 constraint NFR-4).

### US-3 · Team-Meeting Q&A Defence Library P3

> As the team lead, I need standard answers to the supervisor's high-frequency follow-up questions, so that at the team meeting I can respond within 30 seconds with evidence, clear boundaries, and acknowledgement of weaknesses.

**Acceptance Criteria**:
- **AC-3.1** Covers the four originally planned follow-up categories: ① why is it so complex / like an AI system ② what problems does it solve that Quizlet and ChatGPT cannot ③ how do 10 people collaborate and how much did you do ④ what happens with no network / unpaid bills / data loss.
- **AC-3.2** Additionally covers two high-frequency follow-up categories: ⑤ empirical data (the significance of MMLU / the 145 tests) ⑥ failures and reflections (what failed / what would be done differently).
- **AC-3.3** Each answer can be spoken in ≤60 seconds and **cites at least one traceable repository file or number**.
- **AC-3.4** Includes a **quick-reference table of dangerous questions** (single-sentence one-question-one-answer versions).
- **AC-3.5** Includes **three red lines of academic integrity**: no fabricated user research, no misreported experimental data, no misreported division of labour.

### US-4 · Speckit Specification Trace (project governance perspective)

**Acceptance Criteria**:
- **AC-4.1** This cycle has the `spec.md` / `plan.md` / `tasks.md` trio under `specs/003-cycle3-startup-report/`.
- **AC-4.2** The earlier `specs/003-cycle3-reports-and-question-mgmt/` directory, created from the mistaken premise that "Reports = in-software learning dashboard", has been **deleted** and does not enter version control.
- **AC-4.3** This cycle's changes enter `develop` via an **independent branch + PR**, without touching the existing dirty working tree.

---

## 3. Functional Requirements (deliverables list for this cycle)

| ID | Deliverable | Location | Status |
| :--- | :--- | :--- | :--- |
| D1 | Cycle master plan (chapter blueprint, page budgets, figure/table numbering, division-of-labour matrix, milestones, risk register) | `reports/cycle3_master_plan.md` | ✅ |
| D2 | Task-pack master index | `reports/cycle3_task_packs/README.md` | ✅ |
| D3 | Task pack 01 · Yongtong Lin · Ch1 | `reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md` | ✅ |
| D4 | Task pack 02 · Zijian Zhang · Ch2 | `reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md` | ✅ |
| D5 | Task pack 03 · Yusai Xi · Ch5.5 | `reports/cycle3_task_packs/03-ch5-5-gui-xi-yusai.md` | ✅ |
| D6 | Task pack 04 · Sijian Wang · Ch4 | `reports/cycle3_task_packs/04-ch4-architecture-wang-sijian.md` | ✅ |
| D7 | Task pack 05 · Hao Jiang · Ch5.1–5.2 + Appendix D | `reports/cycle3_task_packs/05-ch5-1-2-implementation-jiang-hao.md` | ✅ |
| D8 | Task pack 06 · Siqin Dong · Ch5.3–5.4 | `reports/cycle3_task_packs/06-ch5-3-4-trap-diagnosis-dong-siqin.md` | ✅ |
| D9 | Task pack 07 · Mingjie Yang · Ch6 + Appendix C + User Manual | `reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md` | ✅ |
| D10 | Task pack 08 · Zixuan Liang · Ch5.6 + video/PPT | `reports/cycle3_task_packs/08-ch5-6-deployment-liang-zixuan.md` | ✅ |
| D11 | Task pack 09 · Weixin Xie · Ch3 + Appendix B + final consolidation | `reports/cycle3_task_packs/09-ch3-use-cases-xie-weixin.md` | ✅ |
| D12 | Team-meeting Q&A defence library | `reports/supervisor_qa_defense_library.md` | ✅ |
| D13 | Speckit specification trio | `specs/003-cycle3-startup-report/{spec,plan,tasks}.md` | ✅ |
| D14 | PR merged into `develop` | GitHub PR | ⏳ |

---

## 4. Non-Functional Requirements and Constraints

| ID | Category | Requirement |
| :--- | :--- | :--- |
| NFR-1 | Verifiability | Any number appearing in the report must be locatable to a source file in the repository (question bank / tests / CSV / code). **Numbers without a traceable source must be deleted.** |
| NFR-2 | Official compliance | Deliverables must simultaneously satisfy the Brief's format requirements (A4 / 2.54 cm / single column / 12 pt / Times New Roman / 1.5 line spacing / single PDF / Turnitin) and the rule that "pasting source code into the body is forbidden". |
| NFR-3 | Zero breakage | This cycle **does not modify** any file in `backend/`, `frontend/`, or `tests/`; it does not touch the existing dirty working tree (`seed_questions.py`, `app.js`, `index.html`, `graphrag_final/*.py`). |
| NFR-4 | Academic integrity | **Forbidden** to fabricate user research (no questionnaire sample sizes that were never run), to misreport MMLU results (must report 7 positive / 3 neutral / 2 negative), or to misreport the division of labour (Appendix A requires all members' signatures). |
| NFR-5 | Executability | Task packs must let members start **without asking extra questions**: source paths can be opened directly, word/page counts have explicit ranges, and rejection criteria are self-checkable. |
| NFR-6 | Terminology consistency | The whole team shares one numbering system: R01–R14 (requirements), UC-01–UC-06 (use cases), AD-1–AD-7 (architecture decisions), Figure 1.1–7.1, Table 1.1–7.1. |
| NFR-7 | Security | The delivered ZIP and the version-control repository must not contain plaintext credentials; the known leaked item (Neo4j credentials) must be rotated before submission and recorded in the pre-submission checklist. |
| NFR-8 | Language | Report body in **English** (British spelling); task packs and Q&A library in **Chinese** (for team members and the team lead). |

---

## 5. Non-Goals

| # | Not Doing | Reason |
| :-: | :--- | :--- |
| NG-1 | No new API endpoints or frontend features | The software baseline is frozen; new features would destabilise the 145 test cases and do not serve the 50% report weight |
| NG-2 | No code refactoring or performance optimisation | No engineering payoff this cycle; the only permitted code change is fixing the `Field(..., example=)` deprecation warning at `backend/app/models/auth.py:46` (optional, technical-debt cleanup) |
| NG-3 | No "learning telemetry dashboard"-style new features | This was an earlier mistaken premise, now overturned. "Reports" means the final technical report. |
| NG-4 | Do not wire Neo4j into the online demo path | Cloud instances sleep, and offline exam-room networks produce 500s; keep the offline-evaluation positioning of ADR-05 |
| NG-5 | Do not promise commercial viability | With 12 questions, 10 weeks, and zero budget, the positioning is a feasibility prototype; commercialisation appears only as a future-work path in Ch7 |
| NG-6 | Do not complete the PoC User Manual and demo video this cycle | They are part of the delivery package, but are done by Mingjie Yang / Zixuan Liang after the report main line is finished (the outline and time allocation are already in the task packs) |

---

## 6. Definition of Done

This cycle counts as complete if and only if:

1. D1–D14 above are all delivered and the PR has merged into `develop`;
2. The 9 task packs have been **actually distributed** to the 9 members (group announcement + each member confirms receipt);
3. The team lead can deliver the three opening sentences of Section 0 and the standard answers to any three follow-up categories **without reading from a script**;
4. The whole document's chapter structure **aligns item by item** with the official Brief's seven chapters, and the 17-figure / 21-table numbering table is locked and published;
5. No number in the report lacks a traceable source.
