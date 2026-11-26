# Tasks: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Feature**: [`spec.md`](spec.md) · **Plan**: [`plan.md`](plan.md)
**Branch**: `feature/cycle3-startup-report-plan`
**Legend**: `[P]` parallelisable · `[US-1..4]` maps to user stories · ✅ done · ⏳ pending

> **No code tasks this cycle.** All tasks are text outputs, so dependencies only consider "is the source material verified" and "are the numbers frozen", not compilation/deployment.

---

## Phase 1 — Fact-Finding (blocks all subsequent tasks)

| ID | Task | Output | Status |
| :--- | :--- | :--- | :-: |
| T0.1 | Read the official Brief and extract hard constraints on chapter order / 40–60 pages / format / marking points / PoC / video | Internalised into plan §2 and master plan §0.1 | ✅ |
| T0.2 | Verify backend facts: 8 endpoints, 5 routers, 5 services, 5 models, `StaticFiles` single-port mounting | Fact list | ✅ |
| T0.3 | Verify test facts: 9 files / 78 functions / 145 cases / 3.6 seconds | Fact list | ✅ |
| T0.4 | Verify question-bank facts: 932 lines / 12 questions / 4 subjects / 36 traps / 5 radar dimensions | Fact list | ✅ |
| T0.5 | Verify MMLU evidence: 12 subjects Base→Ours, **7 positive / 3 neutral / 2 negative** | `graphrag_final/final_systematic_report.csv` | ✅ |
| T0.6 | Verify the usability and dimensions of existing chart assets (PNG resolution of the three UML diagrams) | Fact list | ✅ |
| T0.7 | Identify a security issue: `graphrag_final/real_graph_engine.py` contains plaintext Neo4j credentials and is already tracked by git | Risk register R8 + first item on the pre-submission checklist | ✅ |

**Gate G0**: no chapter may be written until T0.1–T0.7 are all complete. **(Passed)**

---

## Phase 2 — Report Blueprint (US-1)

| ID | Task | Output | Dependency | Status |
| :--- | :--- | :--- | :--- | :-: |
| T1.1 | Align the seven-chapter structure with the official Brief (**including three corrections: add Ch3 / split Deployment→Ch5.6, Viability→Ch7 / change Appendix A to the official template**) | master plan §2.2 | G0 | ✅ |
| T1.2 | Page budgets: the sum of per-chapter ranges falls within 40–60 pages (currently 48–59) | master plan §2.2 | T1.1 | ✅ |
| T1.3 | Lock 17 figures + 21 tables and write the numbering into the blueprint | master plan §2.3 | T1.1 | ✅ |
| T1.4 | Mandatory writing elements per chapter (official six mandatory items, five NFR categories, item-by-item requirement evaluation) | master plan §2.4 | T1.1 | ✅ |
| T1.5 | Ten hard "remove the AI feel" rules | master plan §3 | T1.1 | ✅ |
| T1.6 | Division-of-labour matrix + cross-review pairing | master plan §4 | T1.2 | ✅ |
| T1.7 | Three-week milestones (Week A/B/C) + G1/G2 gates | master plan §5 | T1.2 | ✅ |
| T1.8 | Risk register + pre-submission mandatory checklist | master plan §7 | T1.3 | ✅ |
| T1.9 | Cross-check that the figure/table numbering tables in master plan §2.3 and task_packs README §5.1 agree | — | T1.3 | ✅ |

---

## Phase 3 — 9 Task Packs (US-2)

Fixed structure of each task pack (AC-2.2): owner and page budget / one-sentence goal / per-section word count / source-path table / pitfalls / DoD / supervisor's 3 questions.

| ID | Task Pack | Owner | Chapter | Pages | Status |
| :--- | :--- | :--- | :--- | :--- | :-: |
| T2.1 | `01-ch1-introduction-lin-yongtong.md` | Yongtong Lin 50106038 | Ch1 Introduction and Project Context | 5–6p | ✅ |
| T2.2 | `02-ch2-requirements-moscow-zhang-zijian.md` | Zijian Zhang 50106035 | Ch2 Functional & Non-Functional Requirements | 6–7p | ✅ |
| T2.3 | `09-ch3-use-cases-xie-weixin.md` | Weixin Xie 50106034 | Ch3 Use Cases and Requirements Modelling + Appendix B + final consolidation | 6–7p | ✅ |
| T2.4 | `04-ch4-architecture-wang-sijian.md` | Sijian Wang 50106045 | Ch4 System Design and Architecture | 9–11p | ✅ |
| T2.5 | `05-ch5-1-2-implementation-jiang-hao.md` | Hao Jiang 50106065 | Ch5.1–5.2 Implementation: stack + API contracts + Appendix D | 5–6p | ✅ |
| T2.6 | `06-ch5-3-4-trap-diagnosis-dong-siqin.md` | Siqin Dong 50106060 | Ch5.3–5.4 Question-bank trap engineering + diagnosis algorithm | 5–6p | ✅ |
| T2.7 | `03-ch5-5-gui-xi-yusai.md` | Yusai Xi 50105989 | Ch5.5 GUI | 3–4p | ✅ |
| T2.8 | `08-ch5-6-deployment-liang-zixuan.md` | Zixuan Liang 50106037 | Ch5.6 Deployment and reproducibility + video/PPT | 3–4p | ✅ |
| T2.9 | `07-ch6-testing-yang-mingjie.md` | Mingjie Yang 50106061 | Ch6 Testing and Evaluation + Appendix C + User Manual | 7–8p | ✅ |
| T2.10 | `README.md` master index (division-of-labour table / distribution script / writing conventions / R01–R14 frozen / figure-table numbering) | Yuxuan Wu 50106070 | Whole document | — | ✅ |
| T2.11 | Delete the three task packs under the old numbering (early versions of Ch2.4 UX / Ch3 architecture / Ch4 API) | Yuxuan Wu | — | — | ✅ |

**Gate G1** (Sunday 23:59 of Week A): each member submits an outline; **if late, the PM reclaims and writes it, recording `0%` in Appendix A**.

---

## Phase 4 — Team-Meeting Q&A Defence Library (US-3)

| ID | Task | Content | Status |
| :--- | :--- | :--- | :-: |
| T3.1 | §0 Three opening sentences (definition / difference / boundary) | Memorisable in 30 seconds | ✅ |
| T3.2 | §1 Why is it so complex, like an AI system | Complexity lies in data modelling + no concealment of AI assistance | ✅ |
| T3.3 | §2 Comparison with Quizlet / ChatGPT | Three structural differences + literature basis + honest positioning | ✅ |
| T3.4 | §3 How ten people collaborate, and how much you did | Truthfully declare "the code was written by one person" | ✅ |
| T3.5 | §4 No network / unpaid bills / cache / data loss | Includes proactively admitting the credential leak and its handling | ✅ |
| T3.6 | §5 Empirical data and the meaning of the 145 tests + What failed | Includes the correct wording for the negative MMLU results | ✅ |
| T3.7 | §6 Ten-line quick-reference table of dangerous questions | One question, one answer, one sentence | ✅ |
| T3.8 | §7 Three red lines of academic integrity | No fabricated research / no misreported data / no misreported division of labour | ✅ |

---

## Phase 5 — Speckit Records and PR (US-4)

| ID | Task | Output | Dependency | Status |
| :--- | :--- | :--- | :--- | :-: |
| T4.1 | Write `spec.md` (US-1..4 / AC / D1–D14 / NFR / NG / DoD) | `specs/003-cycle3-startup-report/spec.md` | Phase 2–4 | ✅ |
| T4.2 | Write `plan.md` (Constitution Check + Phases + PD-1..7 + risks + acceptance) | `specs/003-cycle3-startup-report/plan.md` | T4.1 | ✅ |
| T4.3 | Write `tasks.md` (this file) | `specs/003-cycle3-startup-report/tasks.md` | T4.2 | ✅ |
| T4.4 | Delete the wrong-premise directory `specs/003-cycle3-reports-and-question-mgmt/` (7 files) | — | — | ✅ |
| T4.5 | Isolate the commit using `git worktree add -b feature/cycle3-startup-report-plan D:\jc2001-cycle3-pr develop` | Clean working tree | — | ⏳ |
| T4.6 | Copy only the 13 new files into the worktree and commit (**excluding the 5 dirty files from others**) | commit | T4.5 | ⏳ |
| T4.7 | `git push -u origin feature/cycle3-startup-report-plan` | Remote branch | T4.6 | ⏳ |
| T4.8 | `gh pr create --base develop` with a change description | PR link | T4.7 | ⏳ |
| T4.9 | `git worktree remove D:\jc2001-cycle3-pr`, leaving the main working tree untouched | Cleanup | T4.8 | ⏳ |

**The PR must contain only these 15 new files**:
`reports/cycle3_master_plan.md`, `reports/supervisor_qa_defense_library.md`, `reports/cycle3_task_packs/` (README + 01–09, 10 files in total), `specs/003-cycle3-startup-report/` (spec/plan/tasks, 3 files in total).

**Files that must NOT appear in the PR**:
`backend/app/data/seed_questions.py`, `frontend/app.js`, `frontend/index.html`, `graphrag_final/auto_builder.py`, `graphrag_final/real_graph_engine.py`.

---

## Phase 6 — Distribution (after the PR; not a code task)

| ID | Task | Acceptance |
| :--- | :--- | :--- |
| T5.1 | Post the distribution script from README §4 and the link to each member's task pack in the group | All 9 members confirm receipt |
| T5.2 | Announce that the requirement IDs (R01–R14) are frozen and @Weixin Xie @Mingjie Yang | Both reply to confirm |
| T5.3 | Announce that the figure/table numbering (17 figures, 21 tables) is frozen | No objections from the whole team |
| T5.4 | Schedule the Week A team meeting (G1 gate) | Time fixed |
| T5.5 | Team-lead self-test: deliver the three opening sentences and any three follow-up categories without reading from a script | Passed |

---

## Dependency Graph

```
G0 fact-finding
   └─> T1.x blueprint ──> T2.x nine task packs ──> T5.x distribution
            │              │
            └──────> T3.x Q&A library
                           │
                     T4.1 spec ─> T4.2 plan ─> T4.3 tasks
                                                  │
                                          T4.5 worktree ─> T4.6 commit
                                                  └─> T4.7 push ─> T4.8 PR ─> T4.9 cleanup
```

---

## Remaining Work (after this file was written)

- [x] T1.9 Cross-check the two figure/table numbering tables (master plan §2.3 and README §5.1 are now unified at **17 figures / 21 tables**; Persona is Table 1.3, requirement sources are Table 2.1, NFR compliance evaluation is Table 6.5)
- [x] T4.5 Worktree created from `origin/develop` with an isolated commit
- [x] T4.6 Committed only the 15 documents (commit `6112954`)
- [x] T4.7 Pushed `feature/cycle3-startup-report-plan`
- [x] T4.8 Created PR #5: <https://github.com/YuxuanWuCN/jc2001-group5-smart-study-assistant/pull/5>
- [x] T4.9 Verified the PR contains only the 15 documents; the temporary worktree is awaiting cleanup
- [ ] T5.1–T5.5 Distribution and team-lead self-test (executed after the PR is merged)
