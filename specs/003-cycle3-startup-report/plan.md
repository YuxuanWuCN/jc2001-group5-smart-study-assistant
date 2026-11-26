# Implementation Plan: Cycle 3 — Startup-Grade Technical Report and Team Distribution

**Branch**: `feature/cycle3-startup-report-plan` | **Spec**: [`spec.md`](spec.md)
**Input**: User-approved Cycle 3 plan (A: report overhaul / B: 9 task packs / C: team-meeting Q&A library) + official Brief hard constraints
**Date**: 2026-10-18

---

## 1. Summary (one sentence)

This cycle writes no code and produces only **text assets**: organise the facts already present in the software baseline into a 40–60 page English technical report blueprint following the official Brief's seven-chapter structure, then split it into 9 member task packs that can be executed directly, plus 1 supervisor Q&A defence library and 1 set of Speckit specification records.

---

## 2. Technical Context (this cycle's "technology" = documents and repository facts)

| Item | Value |
| :--- | :--- |
| Language/format | Markdown delivery (members may convert to DOCX/PDF themselves); report body in English (British) |
| Main dependencies | No new dependencies; only read/write text in `reports/`, `specs/`, `docs` |
| Code changes | **Zero** (NFR-3); the only optional item is fixing the Pydantic deprecation warning at `backend/app/models/auth.py:46` |
| Fact sources (read-only) | `backend/app/` (8 endpoints / 5 routers / 5 services / 5 models), `tests/` (9 files / 78 functions / 145 cases), `backend/app/data/seed_questions.py` (932 lines / 12 questions / 36 traps), `graphrag_final/final_systematic_report.csv` (12 subjects), `reports/` (existing assets), `JC2001-GroupProjectDescription-and-Requirements-2026-27.txt` (official Brief) |
| Target deliverables | `reports/cycle3_master_plan.md`, `reports/cycle3_task_packs/` (10 files), `reports/supervisor_qa_defense_library.md`, `specs/003-cycle3-startup-report/` (3 files) |
| Version control | Independent worktree + branch `feature/cycle3-startup-report-plan`, PR → `develop` |

---

## 3. Constitution Check (`.specify/memory/constitution.md` v2.0.0)

| Principle | Compliant this cycle | Notes |
| :--- | :-: | :--- |
| **I · Top-tier academic and cutting-edge visual aesthetics** | ✅ PASS | Task packs directly constrain chart standards (Figure/Table numbering, caption format, self-drawing requirements) and turn "removing the AI feel" into ten executable rules |
| **II · Native instant loading with zero bundling** | ✅ PASS | Does not touch `frontend/`; task packs 03/05 write "zero build" as a report argument (tech-stack Table 5.1, ADR-02), not just a slogan |
| **III · Zero-breakage compatibility and test gate** | ✅ PASS | Does not modify any backend/test file; task pack 07 uses **145 cases** (not the constitution's original 114) as the source of truth, and **explicitly corrects the outdated endpoints in the constitution** (`/api/graph` and `/api/tutor` no longer exist; the real state is 5 routers / 8 endpoints) |
| **IV · Dual-mode dual-theme WCAG AA + bilingual** | ✅ PASS | Task pack 03 §5.5.5 requires an honest statement on contrast verification and bilingual coverage; task pack 02 registers these as R07/R08 and NFR-U2 |
| **V · File system and workspace discipline** | ✅ PASS | All new files land under `reports/` and `specs/`; worktree operations avoid polluting the existing dirty working tree; no one else's assets are deleted (only the self-created wrong-premise directory `specs/003-cycle3-reports-and-question-mgmt/` is removed) |

> **Constitution deviation record (the constitution itself must be corrected later; not done this cycle)**: Principle III of the constitution states "114 pytest tests" and lists endpoints `/api/health, /api/quiz, /api/diagnose, /api/graph, /api/tutor`; both are outdated. The actual state is **145 cases**, 5 routers, 8 endpoints, and `/api/graph` and `/api/tutor` do not exist. All documents this cycle follow the repository code; the constitution revision is deferred to the next cycle.

---

## 4. Phase Structure (this cycle is essentially complete)

### Phase 0 — Fact-finding (Research)
- Read the official Brief and extract all hard constraints (chapter order, page counts, format, marking points, PoC/video requirements)
- Verify repository facts: endpoint count, test count, question-bank size, MMLU data, existing chart assets
- **Output**: fact list (internalised into the plan and task packs)
- **Key corrections**: three structural corrections - (1) add a standalone Ch3 Use Cases chapter; (2) remove the self-devised Deployment / Viability chapters and merge them into Ch5.6 and Ch7 respectively; (3) change Appendix A to the official Group Workload Profile template

### Phase 1 — Report blueprint (D1)
- Seven chapters + page budgets + owners + front matter + appendices A–D
- 17-figure / 21-table numbering table locked
- Three-week milestones (Week A/B/C) + G1/G2 gates
- Ten hard "remove the AI feel" rules, cross-review pairing, risk register, pre-submission checklist
- **Output**: `reports/cycle3_master_plan.md`

### Phase 2 — 9 task packs + master index (D2–D11)
- Seven fixed items per pack (owner / goal / per-section word counts / source paths / pitfalls / DoD / supervisor's 3 questions)
- Each pack includes two-level deadlines and the branch/PR process
- The master index includes the division-of-labour table, distribution script, whole-team writing conventions, frozen R01–R14, and figure/table numbers
- **Output**: `reports/cycle3_task_packs/` (README + 01–09)

### Phase 3 — Team-meeting Q&A defence library (D12)
- Six follow-up categories (the original four + empirical data + failure reflection)
- Quick-reference table of dangerous questions, three red lines of academic integrity
- **Output**: `reports/supervisor_qa_defense_library.md`

### Phase 4 — Speckit records (D13) and PR (D14)
- `spec.md` / `plan.md` / `tasks.md`
- Delete the wrong-premise directory `specs/003-cycle3-reports-and-question-mgmt/`
- Raise a PR from the worktree to `develop`

---

## 5. Key Design Decisions (this cycle's own ADRs)

| ID | Decision | Alternative | Rationale |
| :--- | :--- | :--- | :--- |
| PD-1 | **Chapter structure fully follows the official Brief**, no self-devised chapters | Keep the original self-devised 8 chapters (Deployment / Viability as standalone chapters) | The official chapter order is fixed and must not be added to or removed from; self-devised chapters would directly lose marks. Deployment has therefore been merged into Ch5.6 and Viability into Ch7 |
| PD-2 | **One person per chapter + task packs**, rather than the team lead writing alone | The team lead writes all 48 pages | Not enough time; and "knowledge concentrated in one person" is exactly the source of the supervisor's doubt; one person per chapter also turns "the report can be questioned at random" into organisational pressure |
| PD-3 | **Task packs provide numbers and source paths**, rather than requiring members to research themselves | Let members improvise | Members lack project context; providing fixed material guarantees the 40–60 page output while avoiding invented data |
| PD-4 | **Report arguments are built on the repository's real state** (12 questions / 145 cases / 7 positive, 3 neutral, 2 negative) | Write a "huge market + full coverage" startup narrative | Scale and data that do not match will be exposed immediately when questioned; "acknowledging this is a feasibility prototype" is more credible |
| PD-5 | **Raise a PR from a worktree**, without touching the main working tree | Checkout develop and commit directly | The main working tree has 5 dirty files from others plus untracked assets; switching branches would conflict or accidentally commit them |
| PD-6 | **Delete the wrong-premise 003 directory** and create `003-cycle3-startup-report` | Keep it and rewrite in place | The old directory name and content premise ("Reports = software dashboard") are wholly wrong; keeping it would pollute later references |
| PD-7 | Use the `write`/`edit` tools to write Chinese Markdown | Use PowerShell `Get-Content`+`Set-Content` for bulk replacement | PowerShell has been measured to corrupt Chinese Markdown through double encoding (see §7 risk R1) |

---

## 6. Acceptance and Verification Methods

| Acceptance Item | Verification Method |
| :--- | :--- |
| Seven chapters aligned with the official Brief | Compare the Brief's chapter list item by item with master plan §2.2; a missing or extra chapter means failure |
| Page budget 40–60 pages | Sum the per-chapter ranges in master plan §2.2 (currently 48–59) |
| Figure/table numbering unique and continuous | Check that the two tables in master plan §2.3 and README §5.1 agree, with no duplicate numbers |
| All 9 task packs present | One each of 01–09 under `reports/cycle3_task_packs/`, with all README index links reachable |
| All seven items present in each task pack | Check the §1–§7 structure of each pack |
| Numbers consistent with the repository | Spot-check: 145 cases (`pytest --collect-only`), 12 questions / 36 traps (`seed_questions.py`), 8 endpoints (`main.py`), MMLU 12 subjects (`final_systematic_report.csv`) |
| No source-code pasting risk | Task packs explicitly forbid pasting source code; the final editor (Weixin Xie) full-text searches the report body for `def ` / `import ` |
| Zero breakage | `git status` confirms no new changes in `backend/`, `frontend/`, `tests/` |
| PR compliance | The PR contains only `reports/cycle3_master_plan.md`, `reports/cycle3_task_packs/**`, `reports/supervisor_qa_defense_library.md`, `specs/003-cycle3-startup-report/**` |

---

## 7. Risk Register

| ID | Risk | Probability | Impact | Mitigation |
| :-: | :--- | :-: | :--- | :--- |
| **R1** | Bulk-editing Chinese documents with PowerShell corrupts the encoding (**has already happened once**) | High (if repeated) | Medium | Always use the `write`/`edit` tools; never use `Get-Content`+`Set-Content` on Chinese Markdown |
| **R2** | Members miss the deadline and the report has gaps | High | High | G1 gate: if the Week A outline is not submitted, the PM reclaims and writes it, recording `0%` in Appendix A; task packs make "90 minutes of typing" the denominator |
| **R3** | Misreported contribution causes Appendix A to be refused for signature | Medium | High | Declare truthfully; use "report division of labour + random questioning" to offset knowledge concentration; do not gloss over it |
| **R4** | Fabricated research data is discovered | Medium | **Fatal** | Three places (task packs 01/02, Q&A library §7) explicitly state the true position that "no formal survey was conducted" |
| **R5** | Negative MMLU results are written up as "all improved" | Medium | High | Five documents lock in the "7 positive / 3 neutral / 2 negative" position and state that the single sampling is not significant |
| **R6** | The report violates the "no source code in the body" rule | Medium | Medium | The final editor performs a full-text search; pseudocode (≤20 lines) and JSON are allowed |
| **R7** | The report exceeds 60 pages and is truncated | Medium | Medium | Per-chapter page budgets are locked; the final editor decides on cuts in Week C |
| **R8** | Neo4j plaintext credentials leak in the delivered ZIP | Medium | High | First item on the pre-submission checklist: move to environment variables + reset the Aura password + full-text search the ZIP for `neo4j+ssc` / `password` |
| **R9** | Nobody appears in the demo video / Team Participation is missing | Medium | Medium (10% weight) | Task pack 08 explicitly requires "all 10 people on camera for ≥30 seconds each" and provides a 15-minute time-allocation table |

---

## 8. Deliverables List (file level)

```
reports/
├── cycle3_master_plan.md                          # D1 cycle master plan (seven-chapter blueprint/chart numbering/milestones/risks)
├── supervisor_qa_defense_library.md               # D12 team-meeting Q&A defence library (six follow-up categories)
└── cycle3_task_packs/
    ├── README.md                                  # D2 master index + distribution script + writing conventions + R01–R14
    ├── 01-ch1-introduction-lin-yongtong.md        # D3  Ch1  5–6p
    ├── 02-ch2-requirements-moscow-zhang-zijian.md  # D4  Ch2  6–7p
    ├── 03-ch5-5-gui-xi-yusai.md                   # D5  Ch5.5 3–4p
    ├── 04-ch4-architecture-wang-sijian.md          # D6  Ch4  9–11p
    ├── 05-ch5-1-2-implementation-jiang-hao.md      # D7  Ch5.1–5.2 5–6p
    ├── 06-ch5-3-4-trap-diagnosis-dong-siqin.md     # D8  Ch5.3–5.4 5–6p
    ├── 07-ch6-testing-yang-mingjie.md              # D9  Ch6  7–8p
    ├── 08-ch5-6-deployment-liang-zixuan.md         # D10 Ch5.6 3–4p + video/PPT
    └── 09-ch3-use-cases-xie-weixin.md              # D11 Ch3  6–7p + Appendix B + final consolidation
specs/003-cycle3-startup-report/
├── spec.md                                        # D13
├── plan.md                                        # D13 (this file)
└── tasks.md                                       # D13
```

---

## 9. Interfaces to Later Cycles (not executed this cycle)

1. **Constitution revision**: update Principle III's "114 tests / 5 endpoints including `/api/graph`, `/api/tutor`" to "145 cases / 8 endpoints", and add the architectural fact of the single-port `StaticFiles` setup.
2. **Technical-debt cleanup**: change `Field(..., example=11)` at `backend/app/models/auth.py:46` to `json_schema_extra`.
3. **PoC delivery package**: User Manual (8–12 page PDF), demo MP4 (all members on camera), PPTX.
4. **If time permits**: one accessibility (a11y) audit of the npm-free frontend, turning WCAG AA from a "promise" into a "measured report".
