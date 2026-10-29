# Oral Defense (Viva) Q&A — Chapter 5.5 (Xi Yusai, `50105989`)

## Q1: Why did you implement the misconception feedback as a right-hand slide-out Drawer (`Trap Drawer`, `42%` width) instead of a centred modal popup?

**Answer:**
> "A centred modal popup covers the question stem and the four option cards (`A`–`D`). During exam revision, when a student reads *why* their chosen option (`A`) was a trap (`TrapDetail.desc`), they constantly need to look back at the exact wording of the stem and compare Option A against Option B. By designing a right-hand slide-out Drawer occupying `42%` of the viewport width (`Figure 5.3`), the question stem and options remain unobstructed on the left (`58%`), enabling side-by-side cognitive comparison without closing and reopening popups."

## Q2: How does your UI design prevent the "Answer Spoiling" problem you criticised in ChatGPT in Chapter 1, and verify that it was engineered rather than generated as decorative fluff?

**Answer:**
> "Every visual element traces to a pedagogical rule in `Section 5.5.1` (`P1`–`P3`):
> 1. Under **`P1` (Answer Never Spoils Prior to Cognitive Commitment)**, when `GET /api/quiz` loads a question, the DOM renders only the stem and the four neutral option buttons; the answer key and explanation are withheld until the student commits to an option.
> 2. Under **`P2` (Progressive Disclosure)** and **`P3` (Data over Decoration)**, the 5-layer Trap Drawer maps 1-to-1 onto `TrapDetail` (`selected_option`, `title`, `desc`, `prereq`, and `explanation`/`socratic_prompt`), and the 5-axis radar (`Figure 5.4`) surfaces dimensional weakness within 3 seconds with zero decorative entrance animations. Because the entire frontend is zero-build vanilla CSS (`frontend/styles.css`, `73 KB`) and ES6+ (`frontend/app.js`, `259 KB`), any CSS token change takes effect immediately on browser refresh."

## Q3: What happens in the UI if a backend API request fails or the user opens the analytics dashboard at 0 attempts?

**Answer:**
> "We handle both boundary states explicitly (`Section 5.5.4` & `Table 5.5b`):
> 1. **Zero-Attempt Empty State (`attempt_count == 0`)**: Rather than dividing `0 / 0` in JavaScript and rendering `NaN%`, the UI inspects the `data_source` provenance badge returned by `/api/reports/summary` and displays **`Seed Baseline (0 Live Attempts)`** (`data_source: "seed_baseline"`, verified in `tests/test_reports.py`), switching to **`Live Session Telemetry`** (`"session_telemetry"`) after the first attempt.
> 2. **API Fault Degradation**: The centralised `apiFetch()` wrapper in `frontend/app.js` catches HTTP `401`/`404`/`422`/`500` responses and network timeouts, displaying a human-readable non-blocking diagnostic banner instead of crashing the DOM."
