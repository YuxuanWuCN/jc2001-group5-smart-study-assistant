# Project Update 2 — Submission Draft (Group 5 · StudyGraph)

> This document is a preparation artefact produced from the 2026-10-30 09:00 reminder: a breakdown of the official requirements + three English sections ready to paste into the MyAberdeen form + the internal WBS status table.
> All numbers are **measured in the workspace D:\jc2001 on 2026-10-30 around 09:0x** (HEAD `e9ae9b0`), not restated from documents.
> ⚠️ **Supervisor prohibition implemented**: `Smart` / `SmartStudy` have been removed throughout (both to avoid the marketing filler word `Smart` in the project name and to strictly comply with the supervisor's instruction in PR #18 banning the `SMART objectives` acronym framework), uniformly using **`StudyGraph`** and **`Five Project Objectives (Objectives 1–5)`**.

---

## 0. One Thing That Must Be Confirmed Before Submission (Only You Can Do It)

| Item to Confirm | Spoken Version | Repository Version | Action |
|---|---|---|---|
| Project Update 2 deadline | **2 November** | `reports/project_proposal.md` line 119, M3.1 says **06 November 2026** | Log in to MyAberdeen -> course page Assessment section -> Group Project form, and check the date in the title. The course page prevails; **if it is 11-06, this draft can keep 4 more days for finalization** |

Official rules (`docs/course/2026-27-GroupProjectDescription-and-Requirements.txt` §5): updates are ungraded but **mandatory**; at least 3 of 4 must be submitted; submission within 7 days late incurs the late penalty, beyond 7 days it is treated as not submitted; missing submissions can deduct up to 10% of the total project mark. **One member submitting once on behalf of the whole group is sufficient.**

## 1. The Three-Section Structure Required by the Official Guidelines (Text as Given)

1. **Summary of the Work Done to Date** — work completed and progress since the last update
2. **Challenges faced and solutions** — problems encountered, and how they have been or are planned to be addressed
3. **Next Steps** — the main activities to be completed next

> No figures or page count required; the form usually limits word count, and the English draft below is about 520 words, so it can be trimmed to fit the form (delete §1.6 and §2.5 first).

---

## 2. Directly Pasteable Answers for Each MyAberdeen Form Question (corrected against measured repository facts, 0 instances of "Smart")

### Question 1: What is your group name:
```text
BMIS - Group 5 (StudyGraph)
```

### Question 2: Have you met with your supervisor and discussed the progress to be recorded here?
- Select: **`True`** (note: the screenshot mistakenly checked `False`; be sure to change it to `True`, consistent with the record of the supervisor meeting on the afternoon of 29 October)

### Question 3: Summary of the Work Done to Date
```text
Since Project Update 1, BMIS Group 5 has moved StudyGraph (our graph-grounded diagnostic study assistant) from an initial prototype to a feature-frozen, documented, and empirically evaluated artefact aligned with our five project objectives (Objectives 1–5).

Report. All seven chapters of the technical report are drafted and assembled: introduction and project context (Ch 1, defining Objectives 1–5 without acronym frameworks), functional and non-functional requirements (Ch 2, R01–R14 and NFR-01–NFR-10), use cases and state machine (Ch 3), the 4+1 architectural views with architectural decision records (Ch 4), implementation (Ch 5.1–5.6, co-authored by four members), testing and evaluation (Ch 6), and conclusions and future work (Ch 7). The current assembled build is 63 A4 pages; we are bringing the main body within the 40–60 page requirement by moving detailed inventories into appendices.

Proof of concept. The StudyGraph runtime has been feature-frozen since 18 October: nine REST endpoints (/api/diagnose, /api/quiz, /api/reports/summary, /api/reports/trend, /api/auth/register, /api/auth/login, /api/auth/demo-users, /api/health, /api/health/llm), a zero-build vanilla ES6+ front-end, and a nine-subject curated question bank (17 questions, 51 diagnostic trap records) running fully offline with zero cloud or database dependency required for core diagnosis.

Quality baseline. The automated pytest suite has grown from 145 to 183 passing test cases (99 test functions across 10 test modules, all running offline in ~4–6 seconds).

Empirical evidence. GraphRAG augmentation was evaluated across all twelve MMLU subjects (n = 4,445 items): 7 subjects improve, 3 remain unchanged, and 2 regress (best: +2.50 pp on Professional Law; worst: -1.32 pp on High School Physics). Both gains and regressions are reported transparently.

Process, security, and integrity. The repository now holds 102 commits on HEAD (106 across all branches) from 11 contributors, with the largest single-author share reduced from 59% at Update 1 to 42.2% (43/102 on HEAD) after assigning one chapter owner per member. Hard-coded credentials found in legacy evaluation scripts during prototyping were purged from the tracked tree, legacy archives were quarantined, and credentials were rotated (commits 6ca027c, 47c0d95, 61eba90, e9ae9b0).
```

### Question 4: Challenges faced and solutions
```text
1. Credential exposure during prototyping. Hard-coded Neo4j and API credentials discovered in early offline evaluation scripts were removed from tracked files, legacy zip archives were quarantined, credentials were rotated, and an automated audit check was added to prevent recurrence.
2. Work concentration across contributors. One author accounted for 59% of commits at Update 1. Assigning dedicated chapter ownership across members reduced the top contributor share to 42.2% on HEAD (40.6% across all branches).
3. Mixed empirical results on MMLU. Graph augmentation did not improve five of the twelve evaluated MMLU subjects (3 tied, 2 regressed). Rather than cherry-picking positive subsets, we report the full 7/3/2 breakdown and analyse the boundary conditions where structured knowledge retrieval helps rule-dense reasoning versus where it introduces noise.
4. Metric and figure drift between code and manuscript. Because the automated test baseline expanded (145 -> 147 -> 183 cases) and API routes evolved during development, several earlier diagrams and chapter tables quoted superseded numbers or route names. We implemented automated verification scripts (scripts/audit_report_numbers.py) to reconcile all manuscript tables, figures, and captions against the live repository before final PDF compilation.
5. Supervisor feedback integration. Following our 29 October afternoon discussion with our supervisor (where four key questions on report scope, evidence grading, and plain authorial voice were reviewed), we are rewriting AI-assisted prose into each chapter owner's direct voice, removing acronym frameworks, and stripping unverified claims.
```

### Question 5: Next Steps
```text
- Complete the full-manuscript number, terminology, and diagram reconciliation against the live codebase (updating remaining 147-case references to 183, unifying the system name to StudyGraph, and regenerating stale SVG/PNG figures), then rebuild the final PDF from the updated source.
- Trim the main report body from 63 pages into the required 40–60 A4 page range by shifting exhaustive test and traceability inventories into appendices.
- Complete paired internal cross-reviews and author-voice rewrites across all seven chapters.
- Rehearse the 20% live demonstration workflow end-to-end (cold start, three-click misconception diagnosis, and offline fallback mode).
- Package the final submission deliverables (Technical Report PDF and clean PoC archive) ahead of the final deadline.
```

---

## 3. Internal WBS Status Table (four columns, for pre-meeting reconciliation)

| WBS Activity | Owner | Deadline | Current Status (measured 10-30) |
|---|---|---|---|
| Ch 1 Introduction and Project Context | Lin Yongtong | 10-29 | ✅ Draft received 15 KB |
| Ch 2 Functional/Non-Functional Requirements (R01–R14, NFR-01–10) | Zhang Zijian | 10-29 | ✅ Draft received 21 KB |
| Ch 3 Use Cases and State Machine | Xie Weixin | 10-29 | ✅ Draft received 20 KB |
| Ch 4 4+1 Views and ADRs | Wang Sijian | 10-29 | ✅ Draft received 23 KB |
| Ch 5.1–5.2 Implementation (Backend/Frontend) | Jiang Hao | 10-29 | ✅ Draft received 21 KB |
| Ch 5.3–5.4 Diagnostic Pipeline and Graph | Dong Siqin | 10-29 | ✅ Draft received 18 KB |
| Ch 5.5 Frontend Interaction and Accessibility | Xi Yusai | 10-29 | ✅ Draft received 10 KB |
| Ch 5.6 Packaging and Reproducibility | Liang Zixuan | 10-29 | ✅ Draft received 13 KB |
| Ch 6 Testing and Evaluation (183 cases / 12 MMLU subjects) | Yang Mingjie | 10-29 | ✅ Draft received 38 KB |
| Ch 7 Conclusions and Future Work | Wu Yuxuan | 10-29 | ✅ Draft received 32 KB |
| Full-text assembly (`scripts/assemble_report.py`) | Wu Yuxuan | 10-30 | ⚠️ 215 KB Markdown produced, but it **contains outdated numbers**, and the PDF predates the Markdown |
| Number unification (number registry) | All members for their chapters | 11-01 | 🔴 Not started: the assembled draft still says 147/150, 80 functions, 9 files, while chapter drafts say 183, 99 functions, 10 files |
| Trim the main body to ≤ 60 pages | Chapter owners | 11-01 | 🔴 Not started: currently 63 pages |
| Paired cross-review (≥5 comments per pair) | Paired members | 11-01 | 🔴 Not started |
| Submit Update 2 | Wu Yuxuan | 11-02 (or 11-06) | ⏳ Awaiting finalization of this draft |

## 4. Two Items That Must Go in the Risk Section

1. **Numbers inconsistent between the assembled draft and chapter drafts**: `reports/final_report/FULL_TECHNICAL_REPORT_EN.md` lines 113, 204, 1066–1103, 1150–1189, 1402, 1510, and 1518 still use the old baseline (147 / 150 passed, 80 functions, 9 files), whereas `ch05_liang_zixuan/draft.md:124`, `ch06_yang_mingjie/draft.md:25`, and `ch07_wu_yuxuan/draft.md:33` already say **183 / 99 / 10**. Before submission, all must be replaced with registry values.
2. **PDF predates Markdown**: `StudyGraph_Cycle3_Final_Report.pdf` was built at 10-30 00:57 while the Markdown was updated at 10-30 01:37 ⇒ the PDF being sent out now is an old draft. Rebuild it after finalization (either LaTeX or pandoc+Edge works).

## 5. Five Pre-Submission Checks

- [ ] Confirm the actual deadline on MyAberdeen (11-02 vs 11-06)
- [ ] Open the form once to confirm the fields and word limit (this draft can be truncated following the priorities in §1)
- [ ] Fill in "whether this is the first submission of Update 2" once as a group member to avoid duplicate submission
- [ ] After replacing the numbers, rerun `python -m pytest tests/ -q` and paste that run's output into the report
- [ ] After submission, screenshot/save the PDF receipt and archive it under `reports/`
