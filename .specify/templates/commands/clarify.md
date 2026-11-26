---
description: Identify underspecified areas in the current feature spec by asking up to 5 highly targeted clarification questions and encoding the answers back into the spec.
scripts:
   sh: scripts/bash/check-prerequisites.sh --json --paths-only
   ps: scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

Goal: Detect and reduce ambiguity or missing decision points in the active feature specification, and record the clarifications directly in the spec file.

Note: This clarification workflow is expected to run (and complete) before `/speckit.plan` is invoked. If the user explicitly states they are skipping clarification (e.g., exploratory spike), you may proceed, but MUST warn that downstream rework risk increases.

Execution steps:

1. Run `{SCRIPT}` once from the repository root (combined `--json --paths-only` mode / `-Json -PathsOnly`). Parse the minimal JSON payload fields:
   - `FEATURE_DIR`
   - `FEATURE_SPEC`
   - (Optionally capture `IMPL_PLAN`, `TASKS` for future chained flows.)
   - If JSON parsing fails, abort and instruct the user to re-run `/speckit.specify` or verify the feature-branch environment.
   - For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. Load the current spec file. Perform a structured ambiguity and coverage scan using this taxonomy. For each category, mark the status: Clear / Partial / Missing. Produce an internal coverage map for prioritization (do not output raw diagrams unless asking questions).

   Functional scope and behaviour:
   - Core user goals and success criteria
   - Explicit out-of-scope declarations
   - User roles / persona differentiation

   Domain and data model:
   - Entities, attributes, relationships
   - Identity and uniqueness rules
   - Lifecycle/state transitions
   - Data volume / scale assumptions

   Interaction and UX flows:
   - Critical user journeys / sequences
   - Error/empty/loading states
   - Accessibility or localization notes

   Non-functional quality attributes:
   - Performance (latency, throughput targets)
   - Scalability (horizontal/vertical, limits)
   - Reliability and availability (uptime, recovery expectations)
   - Observability (logging, metrics, tracing signals)
   - Security and privacy (authentication/authorization, data protection, threat assumptions)
   - Compliance / regulatory constraints (if any)

   Integration and external dependencies:
   - External services/APIs and failure modes
   - Data import/export formats
   - Protocol/versioning assumptions

   Edge cases and failure handling:
   - Negative scenarios
   - Rate limiting / throttling
   - Conflict resolution (e.g., concurrent edits)

   Constraints and tradeoffs:
   - Technical constraints (language, storage, hosting)
   - Explicit tradeoffs or rejected alternatives

   Terminology and consistency:
   - Canonical glossary terms
   - Avoided synonyms / deprecated terms

   Completion signals:
   - Acceptance criteria testability
   - Measurable definition-of-done style metrics

   Misc / placeholders:
   - TODO markers / unresolved decisions
   - Vague adjectives lacking quantification ("robust", "intuitive")

   For each category with status Partial or Missing, add a candidate question opportunity unless:
   - Clarification would not materially change implementation or validation strategy
   - Better deferred to planning phase (note internally)

3. Generate (internally) a prioritized queue of candidate clarification questions (max 5). Do not output all questions at once. Apply these constraints:
    - Maximum of 10 questions across the whole session.
    - Each question must be answerable with either:
       - A short multiple-choice selection (2-5 distinct, mutually exclusive options), or
       - A one-word / short-phrase answer (explicit constraint: "Answer in <=5 words").
    - Only include questions whose answers materially impact architecture, data modelling, task decomposition, test design, UX behaviour, operational readiness, or compliance validation.
    - Ensure category coverage balance: attempt to cover the highest-impact unresolved categories first; avoid asking two low-impact questions while a single high-impact area (e.g., security posture) is unresolved.
    - Exclude questions already answered, trivial stylistic preferences, or plan-level execution details (unless blocking correctness).
    - Favour clarifications that reduce downstream rework risk or prevent inconsistent acceptance tests.
    - If more than 5 categories remain unresolved, select the top 5 by (impact * uncertainty) heuristic.

4. Sequential questioning loop (interactive):
    - Present EXACTLY ONE question at a time.
    - For multiple-choice questions:
       - **Analyze all options** and determine the **most suitable option** based on:
          - Best practices for the project type
          - Common patterns in similar implementations
          - Risk reduction (security, performance, maintainability)
          - Alignment with any explicit project goals or constraints visible in the spec
       - Present your **recommended option prominently** at the top with clear reasoning (1-2 sentences explaining why this is the best choice).
       - Format as: `**Recommended:** Option [X] - <reasoning>`
       - Then render all options as a Markdown table:

       | Option | Description |
       |--------|-------------|
       | A | <Option A description> |
       | B | <Option B description> |
       | C | <Option C description> (add D/E as needed up to 5) |
       | Short | Provide a different short answer (<=5 words) (include only if the free-form alternative is appropriate) |

       - After the table add: `You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer.`
    - For short-answer style (no meaningful discrete options):
       - Provide your **suggested answer** based on best practices and context.
       - Format as: `**Suggested:** <your proposed answer> - <brief reasoning>`
       - Then output: `Format: Short answer (<=5 words). You can accept the suggestion by saying "yes" or "suggested", or provide your own answer.`
    - After the user answers:
       - If the user replies "yes", "recommended", or "suggested", use your previously stated recommendation/suggestion as the answer.
       - Otherwise, validate the answer maps to one option or fits the <=5 word constraint.
       - If ambiguous, ask for quick clarification (the count still belongs to the same question; do not move on).
       - Once satisfied, record it in working memory (do not write to disk yet) and move to the next queued question.
    - Stop asking further questions when:
       - All critical ambiguities are resolved early (remaining queued items become unnecessary), OR
       - The user signals completion ("done", "good", "no more"), OR
       - You reach 5 asked questions.
    - Never reveal future queued questions in advance.
    - If no valid questions exist at the start, immediately report that there are no critical ambiguities.

5. Integration after EACH accepted answer (incremental update approach):
    - Maintain the in-memory representation of the spec (loaded once at start) plus the raw file content.
    - For the first integrated answer in this session:
       - Ensure a `## Clarifications` section exists (create it just after the highest-level context/overview section in the spec template if missing).
       - Under it, create (if not present) a `### Session YYYY-MM-DD` subheading for today.
    - Append a bullet line immediately after acceptance: `- Q: <question> → A: <final answer>`.
    - Then immediately apply the clarification to the most appropriate section(s):
       - Functional ambiguity → Update or add a bullet in Functional Requirements.
       - User interaction / actor distinction → Update User Stories or Actors subsection (if present) with the clarified role, constraint, or scenario.
       - Data shape / entities → Update Data Model (add fields, types, relationships) preserving ordering; note added constraints concisely.
       - Non-functional constraint → Add/modify measurable criteria in Non-Functional / Quality Attributes section (convert vague adjective to metric or explicit target).
       - Edge case / negative flow → Add a new bullet under Edge Cases / Error Handling (or create such a subsection if the template provides a placeholder).
       - Terminology conflict → Normalize the term across the spec; preserve the original term only if necessary, adding `(formerly referred to as "X")` once.
    - If the clarification invalidates an earlier ambiguous statement, replace that statement instead of duplicating it; do not leave stale contradictory text.
    - Save the spec file after each integration to minimize context-loss risk (atomic overwrite).
    - Preserve formatting: do not reorder unrelated sections; keep heading hierarchy intact.
    - Keep each inserted clarification minimal and testable (avoid narrative drift).

6. Validation (performed after each write plus a final pass):
   - The Clarifications session contains exactly one bullet per accepted answer (no duplicates).
   - Total asked (accepted) questions <= 5.
   - The updated sections contain no lingering vague placeholders the new answer was meant to resolve.
   - No contradictory earlier statements remain (scan for removed invalid alternative choices).
   - Markdown structure is valid; only these new headings are allowed: `## Clarifications`, `### Session YYYY-MM-DD`.
   - Terminology consistency: all updated sections use the same canonical term.

7. Write the updated spec back to `FEATURE_SPEC`.

8. Report completion (after the questioning loop ends or early termination):
   - Number of questions asked and answered.
   - Path to the updated spec.
   - Sections touched (list names).
   - Coverage summary table listing each taxonomy category with Status: Resolved (was Partial/Missing and addressed), Deferred (exceeded question quota or better suited to planning), Clear (already sufficient), Outstanding (still Partial/Missing but low impact).
   - If any Outstanding or Deferred remain, recommend whether to proceed to `/speckit.plan` or run `/speckit.clarify` again later.
   - Suggested next command.

Behaviour rules:

- If no meaningful ambiguities are found (or all potential questions would be low-impact), respond: "No critical ambiguities detected worth formal clarification." and suggest proceeding.
- If the spec file is missing, instruct the user to run `/speckit.specify` first (do not create a new spec here).
- Never exceed 5 total asked questions (clarification retries for a single question do not count as new questions).
- Avoid speculative tech-stack questions unless a missing decision blocks functional clarity.
- Respect the user's early termination signals ("stop", "done", "proceed").
- If questions are skipped due to full coverage, output a compact coverage summary (all categories Clear) then suggest advancing.
- If the quota is reached while high-impact categories remain unresolved, explicitly mark them as Deferred with rationale.

Priority context: {ARGS}
