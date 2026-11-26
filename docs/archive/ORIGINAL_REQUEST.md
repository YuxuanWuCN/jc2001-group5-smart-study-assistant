# Original User Request

## 2026-09-16T06:55:14Z

Deliver a complete JC2001 Software Engineering Week 1 package for Group 5 (BSc BMIS, 10 members, Leader: Wu Yuxuan 50106070). This includes: (1) Practical Session 1 deliverables (icebreaker profile, 10-member role assignment matrix, project vision, and supervisor kickoff email), and (2) a submission-ready, academically rigorous 4-8 page Project Proposal in Markdown, DOCX, and PDF formats based on the "Smart Study Assistant System" powered by GraphRAG and Neo4j diagnostic engines.

Working directory: d:/jc2001
Integrity mode: benchmark

## Team Metadata
- **Course**: JC2001 Introduction to Software Engineering (2026-27)
- **Group Number**: Group 5
- **Programme of Study**: BSc (BMIS)
- **Team Leader & PM**: Wu Yuxuan (50106070)
- **Team Members (10)**:
  1. Wu Yuxuan (50106070) — Project Manager & Team Lead
  2. Lin Yongtong (50106038) — Lead Business Analyst (Requirements Capture)
  3. Wang Sijian (50106045) — System Architect (UML & Knowledge Graph Architecture)
  4. Jiang Hao (50106065) — PoC Lead Developer (GraphRAG & Neo4j Engine)
  5. Xie Weixin (50106034) — QA & Technical Report Lead
  6. Zhang Zijian (50106035) — Business Analyst (User Stories & Acceptance Criteria)
  7. Xi Yusai (50105989) — UI/UX Designer & Wireframe Lead
  8. Dong Siqin (50106060) — PoC Logic Developer (Diagnostic API & Quiz Engine)
  9. Yang Mingjie (50106061) — Software Testing & User Manual Lead
  10. Liang Zixuan (50106037) — Presentation, Media & Deployment Lead

## Requirements

### R1. Practical 1 Session Deliverables Pack (`practical1_deliverables.md`)
Produce a complete practical session record matching JC2001 Practical 1 sheet:
- Comprehensive 10-member icebreaker answers covering all 5 questions from socards.org (instant cheer-ups, favourite food memory, hometown highlights, historical moments, energy restoration).
- 10-member role allocation matrix explicitly detailing responsibilities across all 4 project phases (Requirements, Design/UML, PoC Development, Report/Testing/Presentation).
- Project Topic definition addressing: WHAT the system does, WHO it targets, major technical/time constraints, and long-term vision.
- Formal academic email draft addressed to the academic supervisor from Team Leader Wu Yuxuan requesting the Week 1/2 kick-off meeting to discuss project scope.

### R2. Submission-Grade Project Proposal (`reports/project_proposal.md`)
Develop an in-depth, academically rigorous proposal meeting JC2001 specifications:
- Proposal Title Page (Group 5, BSc BMIS, full roster of 10 student names and IDs).
- Section 1: Project Title: "To Design and Implement a Smart Study Assistant System for University Students".
- Section 2: Problem: Academic stress, disorganised learning materials, rote memorisation inefficiencies, and the critical lack of structured diagnostic feedback on conceptual blind spots and examination traps.
- Section 3: Solution: GraphRAG-powered smart study assistant integrating Neo4j knowledge graphs, automated exam question diagnostic parsing via LLM (Qwen/DashScope), trap/misconception relationship mapping ("error-prone at"), dynamic quiz generation, and student mastery visualization.
- Section 4: Objectives: Specific, Measurable, Achievable, Relevant, and Time-bound (SMART) objectives ensuring functional PoC delivery on or before 14 December 2026.
- Section 5: Benefits: Tangible academic and cognitive benefits for undergraduate students and instructors.
- Section 6: Timeline: 4 distinct project phases with explicit milestones from 14 September 2026 through 14 December 2026.
- Section 7: Action Plan: Full Work Breakdown Structure (WBS) table with specific tasks, assigned member(s), deadlines, and current progress status.
- Section 8: Formatting & Academic Integrity compliance declarations.

### R3. Automated Dual-Format Compilation (`scripts/generate_proposal_docs.py`)
Provide an automated Python compilation script converting the proposal into both `.docx` and `.pdf`:
- Strict formatting compliance: A4 paper, standard 1-inch (2.54 cm / 72 pt) margins on all 4 sides, single-column layout, 12pt Arial or Times New Roman body text, 1.5 line spacing.
- Dedicated unnumbered Proposal Title Page as required by the course guidelines.
- Body length strictly between 4 and 8 pages (excluding title page).
- Output files placed in `reports/project_proposal.docx` and `reports/project_proposal.pdf`.

### R4. Automated Verification & Quality Gate (`scripts/verify_week1_deliverables.py`)
Implement a standalone verification script that validates:
- Presence and non-emptiness of all required deliverables (`practical1_deliverables.md`, `reports/project_proposal.md`, `reports/project_proposal.docx`, `reports/project_proposal.pdf`).
- Absence of unresolved placeholders or bracketed marks.
- Page count of the compiled PDF/DOCX strictly between 4 and 8 pages (excluding Title Page).
- Inclusion of all 10 real group members and leader Wu Yuxuan in both documents.

## Acceptance Criteria

### Output Files & Structure
- [ ] `practical1_deliverables.md` is generated with 10-member icebreaker answers, role matrix, project vision, and supervisor email draft.
- [ ] `reports/project_proposal.md` contains all 7 mandatory sections plus Title Page, properly structured with academic citations and technical depth.
- [ ] `scripts/generate_proposal_docs.py` compiles `reports/project_proposal.docx` and `reports/project_proposal.pdf` without runtime errors.
- [ ] The generated PDF proposal body length is verified to be between 4 and 8 pages (excluding Title Page).
- [ ] Typography conforms to A4, 1-inch margins, 12pt font, and 1.5 line spacing.
- [ ] `scripts/verify_week1_deliverables.py` passes all checks with return code 0.

## 2026-09-16T07:19:12Z

[User Request Update] Supplementary user request: after all deliverables are complete, please additionally generate a consolidated PDF document for the ten team members to review and check (e.g. `reports/week1_team_review_pack.pdf`), containing:
1. Overall completion status of the Week 1 tasks and the key submission milestones (Proposal submission on 25 September);
2. The specific responsibility matrix for the ten team members, and verification of the icebreaker records;
3. A quick overview of the core design highlights and review points of the Project Proposal;
4. The draft email for the supervisor kick-off meeting and the related internal preparation items;
5. A member review and confirmation checklist (Review Checklist & Sign-off Table), so that all team members can verify and confirm it item by item in the WeChat group or by email.
Please make sure this consolidated review PDF is generated together with the main deliverables.

## 2026-09-17T00:40:08Z

Conduct an in-depth architectural and algorithmic competitive analysis of smart study, AI tutoring, and adaptive test-prep platforms (including commercial products like Khanmigo, Quizlet, Duolingo, and domestic test-prep apps, as well as foundational cognitive science models such as BKT, DKT, and IRT). Pinpoint the common underlying mechanisms shared across these competitors that our current "Smart Study Assistant" (Neo4j GraphRAG + Qwen-Turbo trap extractor + Socratic prompt) lacks, and formulate an actionable engineering evolution roadmap tailored to the JC2001 course scope.

Working directory: d:/jc2001
Integrity mode: development

## Requirements

### R1. Broad-Spectrum Competitor & Paradigm Deconstruction
Deconstruct the architectural foundations of leading market products and classical cognitive frameworks across four key categories:
1. **Generative LLM Socratic Tutors**: e.g., Khanmigo (Khan Academy), Socratic (Google), AI study agents.
2. **Spaced Repetition & Retention Engines**: e.g., Quizlet (Q-Chat, Leitner/SM-2 spaced repetition), Anki algorithms.
3. **Gamified Adaptive Practice**: e.g., Duolingo (Birdbrain adaptive difficulty adjustment, mastery learning loops).
4. **Classical Educational Data Mining & Cognitive Models**: e.g., Bayesian Knowledge Tracing (BKT), Deep Knowledge Tracing (DKT), Item Response Theory (IRT), and computerized adaptive testing (CAT).

### R2. Common Underlying Logic Extraction (The "Shared DNA")
Identify and formulate the universal architectural and mathematical patterns that mature systems rely on, focusing on:
- Dynamic learner mastery state modeling (how student competence changes continuously over time).
- Memory retention and temporal decay curves (forgetting dynamics).
- Question difficulty and discrimination calibration (IRT parameter estimation vs. static question tagging).
- Error attribution and generative variant practice loops (closing the loop from diagnosis to remedial reinforcement).
- Scaffolding and pacing control (how systems prevent premature answer reveal or student frustration).

### R3. Systematic Gap Analysis Against Group 5 System
Directly benchmark the identified competitor mechanics against our current architecture:
- Current: Neo4j GraphRAG (exam point/theorem/error-prone edge types), Qwen-Turbo zero-shot trap extractor, Socratic chat prompts, and static 5-dimension ECharts radar chart.
- Target: Identify exact missing layers (e.g., student-level temporal state tracking, dynamic difficulty weighting, variant problem synthesis).
- Compile an exhaustive comparison matrix highlighting mechanism, competitor implementation, our current status, and gap severity.

### R4. Actionable JC2001 Engineering Roadmap & Prototypes
Synthesize high-impact, realistic recommendations that Group 5 can incorporate into the JC2001 Technical Report (40–60 pages) and PoC software:
- Propose 1–2 lightweight algorithms (e.g., simplified BKT or Leitner memory decay queue on top of Neo4j nodes) feasible within the 12-week timeline.
- Provide sample schema enhancements for Neo4j and API contract specs.

## Acceptance Criteria

### Analytical Breadth & Depth
- [ ] Thoroughly covers all 4 competitor categories with explicit analysis of their algorithmic / state-machine foundations (not just UI/surface features).
- [ ] Formulates at least 4 common underlying mechanisms shared across competitors that our system currently lacks (e.g., dynamic knowledge tracing, retention decay, difficulty adaptation, remedial variant loops).

### Comparative Rigor
- [ ] Includes a structured comparison matrix contrasting Competitors vs. Our System across at least 6 core engineering dimensions.
- [ ] Clearly articulates the architectural bottlenecks of our current static GraphRAG approach when compared against stateful student modeling.

### Deliverable Feasibility
- [ ] Deliverable is generated and saved as a comprehensive technical report: `reports/competitor_analysis.md`.
- [ ] Includes concrete, executable recommendations and architectural design sketches (UML / schema extensions) directly reusable in the JC2001 Technical Report.

## 2026-09-22T04:50:39Z

Refactor the overall visual style of the **SmartStudy AI** frontend (`d:\jc2001\frontend\`, including `index.html` and `style.css`) into the **DeepSeek Eval Harness evaluation console style**: a dark background as the default theme, metric cards, data tables, and a progress-bar layout. All business logic in `app.js` **must not be modified**; only the HTML structure and CSS may be changed.

Working directory: d:\jc2001\frontend
Integrity mode: demo

---

## Requirements

### R1. DeepSeek Eval Harness Visual Style Refactor (style.css)

Rewrite `style.css` so that the overall UI aligns with the design language of the DeepSeek Eval Harness evaluation console:

- **Color system**: the dark theme is the default (background ~`#0d1117` or an equivalent dark blue-black), while the light theme toggle is retained; the primary brand color is changed to DeepSeek blue (~`#4f8ef7` or equivalent).
- **Layout**: change the navigation bar into a fixed dark sidebar on the left, with the main content area on the right; when the sidebar width is insufficient, it may collapse into top tabs.
- **Components**: statistic cards use a `border + monospace large number` style, table rows use striped backgrounds, progress bars carry percentage labels, and the graph panel keeps an independent full-width display area.
- **Typography**: body text uses a monospace style such as `JetBrains Mono` or `Fira Code` to strengthen the data-oriented feel; headings retain sans-serif.
- **Motion**: remove most transition animations, keeping only hover highlighting and active states, for a more restrained overall feel.

### R2. HTML Structure Fine-Tuning (index.html)

Without breaking any `id`, `class`, or `data-*` attributes referenced by `app.js`:

- Refactor the `<header class="navbar">` structure into a left vertical sidebar (`<aside class="sidebar">`) plus a right main area (`<main class="main-content">`).
- Change the statistic card (`analytics-grid`) layout into two-column grid cards, each card showing the metric name, a large number, and a sub-description line.
- Change the weak-point list in the learning diagnosis view (`view-report`) into a data-table style (`<table>` or equivalent CSS grid rows).
- The other three views (quiz / tutor / graph) keep their functionality unchanged; only the container styles and color schemes are adjusted.

### R3. Compatibility and Functionality Preservation

- The `app.js` file **must not be modified**.
- All DOM selectors that `app.js` depends on (`id`, `class`, `data-view`, `data-subject`) must be fully retained after the refactor and must not be deleted or renamed.
- The containers related to ECharts (loaded via CDN) and the SVG graph must adapt reasonably to the new layout; charts must not render at 0x0.
- Keep the light/dark theme toggle button; after switching, both themes must render completely (no white screen or missing styles).

---

## Acceptance Criteria

### No JS Errors
- [ ] Open `index.html` in the browser Console, with no red Error messages (only network-type warnings are acceptable, e.g. CSP blocking CDN fonts).

### All Four Views Function Correctly
- [ ] **Quiz view**: clicking the tabs switches subjects, question stems and options render correctly, and clicking an option expands/collapses the diagnostic-drawer.
- [ ] **Chat view**: the input box accepts text, and after clicking send the message bubble appears in `chat-msgs-container`.
- [ ] **Graph view**: the SVG canvas is non-empty and graph nodes are visible (not all white or all black).
- [ ] **Learning diagnosis view**: the ECharts radar chart renders correctly (non-zero size) and the weak-point list has content.

### DeepSeek Eval Harness Visual Benchmark
- [ ] The page loads with the dark theme by default (`body` background luminance < 0.1).
- [ ] Sidebar (or top tab) navigation is visible, with the brand name and the four function items clearly displayed.
- [ ] The number area of the statistic cards uses a monospace font family.
- [ ] The overall interface removes "student-side light-luxury" features such as excessive rounded corners and heavy gradients, aligning with an "engineering/evaluation console" aesthetic.

### Theme Switching
- [ ] Clicking the light/dark toggle button correctly flips the background, text, and card colors, with no exposed white or black blocks.


## 2026-10-08T01:34:27Z

Build an end-to-end runnable Proof-of-Concept (PoC) MVP for the JC2001 Smart Study Assistant System. The PoC integrates the existing DeepSeek-style console frontend with a lightweight, robust FastAPI backend that delivers question loading, distractor trap misconception diagnosis, Socratic hints, and automated verification tests.

Working directory: d:/jc2001
Integrity mode: development
Requested team: Full team (architecture, backend, frontend, and QA testing in parallel with multi-role collaboration)

Special User Directive:
The user specifically requested: "Remember to build the frontend so I can see it." Ensure the frontend (`frontend/index.html` + `frontend/app.js`) is completely and smoothly wired up to the backend, fully runnable via local HTTP server / uvicorn / static mount, with zero CORS issues, fluid interactive diagnostic drawer, and clear instructions/preview links for the user to view and test it immediately.

## Requirements

### R1. Lightweight FastAPI Backend & API Contracts
Implement a modular, runnable FastAPI backend service under `backend/` following clean architecture. The service must expose:
- `GET /api/health`: Health status probe.
- `GET /api/quiz`: Load question sets by discipline/subject with choices and distractor tags conforming to the `QuizItem` Pydantic schema.
- `POST /api/diagnose`: Receive a student's answer choice, match the pre-tagged misconception/trap, query knowledge concepts, and generate Socratic diagnosis guidance.
- Strict Pydantic model validations for all request and response payloads, ensuring compatibility with defined project contracts.

### R2. DeepSeek Console Frontend Integration & CORS
Connect the existing frontend (`frontend/index.html`, `frontend/app.js`) to the FastAPI backend:
- Configure FastAPI CORS middleware to allow cross-origin requests from local browser sessions (`http://localhost:*`, `http://127.0.0.1:*`, or local `file://` protocol).
- Ensure that selecting a question option triggers `POST /api/diagnose`, renders the returned misconception analysis in the right-side Diagnostic Drawer, and maintains fluid UI interactions without JavaScript console errors.
- Mount or provide convenient serving of `frontend/` so the user can open `http://127.0.0.1:8000/` or `frontend/index.html` directly to preview the interactive application.

### R3. Resilient Diagnostic Service & Seed Data
Provide a dual-mode diagnostic engine:
- Live LLM diagnostic synthesis using DashScope (Qwen-Turbo) when `QWEN_API_KEY` is present.
- Automatic, robust offline fallback mode when the API key is missing or network times out, returning pre-compiled domain misconceptions from local seed knowledge graphs so the system never crashes (500 error) during testing.
- Seed the backend with questions across STEM, economics, or computer science derived from the project's evaluation datasets.

### R4. Automated Pytest Suite & Reproducible Launch
Deliver a comprehensive automated test suite and developer documentation:
- Pytest unit and integration tests under `tests/` covering API endpoint contracts, schema validation, diagnostic fallback mechanisms, and CORS headers.
- Update `requirements.txt` with minimal, non-conflicting dependencies (`fastapi`, `uvicorn`, `pydantic`, `pytest`, `requests`, `python-dotenv`).
- Provide clear instructions to start the service and run tests with a single command.

## Acceptance Criteria

### API Functionality & Schema Validation
- [ ] `uvicorn` starts the FastAPI app on port 8000, and `GET /api/health` returns `200 OK` with `{"status": "ok"}`.
- [ ] `GET /api/quiz?subject=economics` (or another valid subject) returns HTTP 200 with a list of questions conforming to `QuizItem`.
- [ ] `POST /api/diagnose` with a valid `DiagnoseRequest` payload returns HTTP 200 with a response strictly conforming to `DiagnoseResponse`.

### Robustness & Fault Tolerance
- [ ] In the absence of external network or API keys, `POST /api/diagnose` gracefully returns a valid `DiagnoseResponse` with `fallback_mode=true` without raising unhandled 500 exceptions.

### Frontend Integration & User Preview
- [ ] Opening `frontend/index.html` (or the served frontend URL) in a web browser and selecting an option in the quiz view successfully communicates with the running backend, rendering diagnosis in the drawer without browser console exceptions.
- [ ] Provide clear local preview verification for the user.

### Test Automation & Quality Gate
- [ ] Executing `pytest tests/` in the project root executes all test suites and passes with 100% success rate (exit code 0).
- [ ] No temporary debug scripts or unorganized files remain in the root directory.
