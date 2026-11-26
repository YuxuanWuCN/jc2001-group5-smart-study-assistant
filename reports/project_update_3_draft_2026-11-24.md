# Project Update 3 — Ready-to-Submit Answers (BMIS - Group 5 · StudyGraph)

**Date:** 24 November 2026  
**PDF Deliverables:** `reports/project_update_3_pdfs/` (and synced under `D:/jc2001-cycle4-master/reports/final_report/ch07_wu_yuxuan/cycle4/project_update_3_pdfs/`)

---

## Question 1: What is your group name:

```text
BMIS - Group 5 (StudyGraph)
```

## Question 2: Have you met with your supervisor and discussed the progress to be recorded here?

Select **`True`** only if your group has actually met with Dr. Shahzad Mumtaz to discuss this Cycle 4 update; otherwise select **`False`** honestly.

## Question 3: Summary of the Work Done to Date

```text
Since Project Update 2, BMIS Group 5 shifted from Cycle 3 report drafting to Cycle 4 evidence-led PoC slices, independent QA verification, and configuration-controlled reproducibility for StudyGraph. Following distributed configuration management practice, all 10 Cycle 4 task packs (reports/cycle4_task_packs/) anchor to master as the single mainline.

1. Component Reuse & Question Pack Ingestion Gate (PR #25 merged): Reusing existing QuizItem/QuizService models and FastAPI/Pydantic frameworks, we added backend/app/services/question_parser.py, CLI scripts/validate_question_pack.py, and optional quiz_repo dependency injection in DiagnosticService. Valid packs exit 0 (2 items accepted, end-to-end diagnosis verified on law_1:A); invalid packs exit 1 (12 errors, 1 warning with JSON paths).

2. Bounded Offline GraphRAG Prototype: Isolated a zero-credential retrieval module (graphrag_prototype.py and scripts/run_graphrag_prototype.py) reusing the 17 curated questions (9 subjects, 85 nodes, 68 directed edges). It compares binary baselines against triple-grounded feedback, parses graphrag/final_systematic_report.csv (12 MMLU subjects, n = 4,445: 7 wins, 3 ties, 2 losses; Law +2.50 pp, Econometrics +1.76 pp, US History -1.00 pp, Physics -1.32 pp), and documents where retrieval fails.

3. Dynamic Quiz User Flow Prototype (Zero CDN): Built a standalone flow prototype (ch05_xi_yusai/cycle4/prototype/dynamic_quiz_flow.html and .js) demonstrating ready, loading, empty, error, and offline-fallback states with recovery controls and the shared five-dimension radar contract (recall, boundary, trapDefense, synthesis, precision).

4. Architecture, Requirements Scenarios, Release & Independent QA: Delivered implemented-only architecture/sequence diagrams mapped to code (Ch4, Adapter/Strategy patterns), release-reproduction probe verify_clean_start.py (overall_pass: true, 0 .zip files), five requirements-based user scenarios with trial observations (Ch1), an independent QA verification runner (ch08_luo_wenxi/cycle4/run_verification.py) following product/process standards, and reconciled Ch2 requirements (51 traps, 9 REST routes, R04 marked partially satisfied). Open PR #28 (traceability & 12-finding review log) and PR #29 (30 defect/failure tests) are reviewed and ready for merge.

5. Incremental Regression Baseline: Automated pytest coverage grew from 183 passed at Update 2 to 244 passed, 0 failed, 0 errors in 4.55 s offline (183 baseline + 49 parser + 8 GraphRAG + 4 quiz-flow checks), with 30 more tests (26 passed, 4 strict xfail) in PR #29.
```

## Question 4: Challenges faced and solutions

```text
1. Defect Testing Surfacing Interface & Edge Bugs (C4-01 & C4-02): Unlike validation tests on happy paths, defect testing in PR #29 exposed two real edge flaws: invalid UTF-8 inputs raise UnicodeDecodeError (CLI exit 2 instead of coded exit 1), and pack export drops optional graph/socratic_prompt fields. Solution: Merged review logs keep strict xfail guards visible; PR #28/#29 will merge first, followed by fault-repair patches.

2. Quality-Attribute Trade-Off & Third-Party Reuse Risk: Improving offline reliability exposed a reuse dependency in frontend/index.html (external ECharts CDN), which breaks uncached air-gapped rendering. Solution: Built the Cycle 4 quiz prototype with zero external assets for offline demos and scheduled local echarts.min.js vendoring.

3. Controlled Software Evolution & Legacy Debt: Independent QA reviews flagged legacy technical debt: /api/quiz still exposes answer/trap fields, /api/reports/summary labels static demo baselines 'session_telemetry', seed_questions.py uses mostly Chinese text, and app.js uses 'stat_1' vs. 'prob_stat_1'. Solution: Logged transparently in discrepancies_and_risks.md (DR-05 to DR-08) for separate public response schemas and 'demo_baseline' relabelling.

4. Robustness vs. Retrieval Noise Trade-Off: MMLU regressions in High School Physics (-1.32 pp) and US History (-1.00 pp) confirmed that unpruned graph context hurts numerical or narrative reasoning. Solution: Kept POST /api/diagnose deterministic via curated lookup (AD-4/AD-5) while confining GraphRAG retrieval to an auditable offline prototype.

5. Metrics Caveat & Process Standards (Working Rule 6): Passing 244 regression tests verifies baseline stability, not absence of all defects or individual comprehension. We kept all new Cycle 4 packs honestly marked NEEDS REVIEW pending English oral walkthroughs, reconciled Zijian Zhang's Ch2 work, and flagged his missing Cycle 4 row for supervisor review.
```

## Question 5: Next Steps

```text
1. Distributed CM Merge & Regression Rerun: Merge reviewed PR #28 (Weixin Xie), PR #29 (Mingjie Yang), and completed Week 3 Cycle 4 branches into master, then rerun pytest and ch08_luo_wenxi/cycle4/run_verification.py (expecting 270 passed, 4 strict xfail before fault-repair fixes).

2. Fault-Repair & Adaptive Maintenance (Lecture 12): Fix C4-01 (handle UnicodeError with CLI exit 1) and C4-02 (preserve or specify reduced export for graph/socratic_prompt), vendor echarts.min.js locally in frontend/ for air-gapped adaptation, relabel static report defaults to 'demo_baseline', and align stat_1 with prob_stat_1.

3. Process-Standard Oral Checkpoints: Conduct brief English live walkthroughs with each member before 30 November using cycle4/viva_cycle4.md so verified contributions can be legitimately promoted from NEEDS REVIEW to UNDERSTOOD.

4. Supervisor Scope Confirmation: Confirm Cycle 4 task ownership for Zijian Zhang (50106035) and finalise report page-budget and submission packaging details.

5. Release Reproduction & Acceptance Rehearsal (by 30 November): Run an end-to-end clean-checkout rehearsal covering single-command offline launch, dynamic quiz five-state transitions, CLI pack validation (exit 0/1), and bounded GraphRAG baseline comparison.
```
