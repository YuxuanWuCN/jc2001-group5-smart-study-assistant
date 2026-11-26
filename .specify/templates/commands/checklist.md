---
description: Generate a custom checklist for the current feature based on user requirements.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json
  ps: scripts/powershell/check-prerequisites.ps1 -Json
---

## Checklist Purpose: "Unit Tests for the Requirements"

**KEY CONCEPT**: A checklist is a **unit test suite for the requirements** - it verifies the quality, clarity, and completeness of requirements in a specific domain.

**NOT for verification/testing**:

- ❌ NOT "verify the button clicks correctly"
- ❌ NOT "test that error handling works"
- ❌ NOT "confirm the API returns 200"
- ❌ NOT checking whether code/implementation matches the spec

**FOR requirements quality validation**:

- ✅ "Are visual hierarchy requirements defined for all card types?" (completeness)
- ✅ "Is 'prominent display' quantified with specific sizing/positioning?" (clarity)
- ✅ "Are hover state requirements consistent across all interactive elements?" (consistency)
- ✅ "Are accessibility requirements defined for keyboard navigation?" (coverage)
- ✅ "Does the spec define what happens when the logo image fails to load?" (edge cases)

**Metaphor**: If your spec is code written in English, the checklist is its unit test suite. You are testing whether the requirements are well-written, complete, unambiguous, and ready for implementation - not testing whether the implementation works.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Execution Steps

1. **Setup**: Run `{SCRIPT}` from the repository root and parse the JSON for FEATURE_DIR and the AVAILABLE_DOCS list.
   - All file paths must be absolute.
   - For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Clarify intent (dynamic)**: Derive up to three initial contextual clarifying questions (no preset catalogue). They MUST:
   - Be generated from the user's wording plus signals extracted from the spec/plan/tasks
   - Only ask for information that would materially change checklist content
   - Skip an individual question if it is already explicit in `$ARGUMENTS`
   - Prioritize precision over breadth

   Generation algorithm:
   1. Extract signals: feature-domain keywords (e.g., auth, latency, UX, API), risk indicators ("critical", "must", "compliance"), stakeholder hints ("QA", "review", "security team"), and explicit deliverables ("a11y", "rollback", "contracts").
   2. Cluster the signals into candidate focus areas (max 4), ordered by relevance.
   3. Identify the likely audience and timing (author, reviewer, QA, release) if not explicit.
   4. Detect missing dimensions: scope breadth, depth/rigor, risk emphasis, exclusion boundaries, measurable acceptance criteria.
   5. Formulate questions from these archetypes:
      - Scope refinement (e.g., "Should this include the integration touchpoints with X and Y, or stay limited to local module correctness?")
      - Risk prioritization (e.g., "Which of these potential risk areas should receive mandatory gating checks?")
      - Depth calibration (e.g., "Is this a lightweight pre-commit sanity list or a formal release gate?")
      - Audience framing (e.g., "Will this be used by the author only, or by peers during PR review?")
      - Boundary exclusion (e.g., "Should we explicitly exclude performance-tuning items this round?")
      - Scenario-class gaps (e.g., "No recovery flows detected - are rollback/partial-failure paths in scope?")

   Question formatting rules:
   - If offering options, generate a compact table with columns: Option | Candidate | Why It Matters
   - Limit to a maximum of A-E options; omit the table if a free-form answer is clearer
   - Never ask the user to restate what they already said
   - Avoid speculative categories (no hallucination). If unsure, ask explicitly: "Confirm whether X is in scope."

   Defaults when interaction is impossible:
   - Depth: Standard
   - Audience: Reviewer (PR) if code-related; otherwise Author
   - Focus: The top 2 relevance clusters

   Output the questions (labelled Q1/Q2/Q3). After the answers: if >= 2 scenario classes (alternate/exception/recovery/non-functional areas) remain unclear, you may ask up to two more targeted follow-ups (Q4/Q5), each with a one-line justification (e.g., "unresolved recovery-path risk"). Do not exceed five questions total. Skip the escalation if the user explicitly declines further questions.

3. **Understand the user request**: Combine `$ARGUMENTS` + the clarifying answers:
   - Derive the checklist theme (e.g., security, review, deployment, UX)
   - Consolidate any explicit must-have items the user mentioned
   - Map the focus selection to category scaffolding
   - Infer any missing context from the spec/plan/tasks (do not hallucinate)

4. **Load feature context**: Read from FEATURE_DIR:
   - spec.md: functional requirements and scope
   - plan.md (if present): technical details, dependencies
   - tasks.md (if present): implementation tasks

   **Context loading strategy**:
   - Load only the necessary parts related to the active focus areas (avoid full file dumps)
   - Prefer summarizing long passages into concise scenario/requirement bullets
   - Use progressive disclosure: add follow-up retrieval only when a gap is detected
   - If a source document is large, generate intermediate summary items instead of embedding raw text

5. **Generate the checklist** - create "unit tests for the requirements":
   - Create the `FEATURE_DIR/checklists/` directory if it does not exist
   - Generate a unique checklist file name:
     - Use a short, domain-based descriptive name (e.g., `ux.md`, `api.md`, `security.md`)
     - Format: `[domain].md`
     - If the file exists, append to the existing file
   - Number items sequentially starting from CHK001
   - Each `/speckit.checklist` run creates a new file (never overwrite an existing checklist)

   **CORE PRINCIPLE - Test the requirements, not the implementation**:
   Every checklist item must evaluate the requirement itself:
   - **Completeness**: Are all necessary requirements present?
   - **Clarity**: Are the requirements unambiguous and specific?
   - **Consistency**: Do the requirements align with each other?
   - **Measurability**: Can the requirements be objectively verified?
   - **Coverage**: Are all scenarios/edge cases addressed?

   **Category structure** - group items by requirements quality dimension:
   - **Requirement Completeness** (are all necessary requirements documented?)
   - **Requirement Clarity** (are the requirements specific and unambiguous?)
   - **Requirement Consistency** (do the requirements align without conflicts?)
   - **Acceptance Criteria Quality** (are success criteria measurable?)
   - **Scenario Coverage** (are all flows/cases addressed?)
   - **Edge Case Coverage** (are boundary conditions defined?)
   - **Non-Functional Requirements** (performance, security, accessibility, etc. - are they specified?)
   - **Dependencies & Assumptions** (are they documented and validated?)
   - **Ambiguities & Conflicts** (what needs clarification?)

   **HOW TO WRITE CHECKLIST ITEMS - "Unit Tests for English"**:

   ❌ **WRONG** (testing implementation):
   - "Verify the landing page displays 3 episode cards"
   - "Test that the hover state works on desktop"
   - "Confirm clicking the logo navigates to the home page"

   ✅ **CORRECT** (testing requirements quality):
   - "Are the exact number and layout of featured episodes explicitly specified?" [Completeness]
   - "Is 'prominent display' quantified with specific sizing/positioning?" [Clarity]
   - "Are hover state requirements consistent across all interactive elements?" [Consistency]
   - "Are keyboard navigation requirements defined for all interactive UI?" [Coverage]
   - "Is fallback behaviour specified when the logo image fails to load?" [Edge Cases]
   - "Are loading states defined for asynchronous episode data?" [Completeness]
   - "Does the spec define the visual hierarchy for competing UI elements?" [Clarity]

   **ITEM STRUCTURE**:
   Each item should follow this pattern:
   - A question format that interrogates requirements quality
   - Focus on what is written (or not written) in the spec/plan
   - Include the quality dimension in brackets [Completeness/Clarity/Consistency/etc.]
   - Reference the spec section `[Spec §X.Y]` when checking existing requirements
   - Use the `[Gap]` marker to flag missing requirements

   **EXAMPLES BY QUALITY DIMENSION**:

   Completeness:
   - "Are error handling requirements defined for all API failure modes? [Gap]"
   - "Are accessibility requirements specified for all interactive elements? [Completeness]"
   - "Are mobile breakpoint requirements defined for responsive layouts? [Gap]"

   Clarity:
   - "Is 'fast loading' quantified with specific timing thresholds? [Clarity, Spec §NFR-2]"
   - "Are 'related episodes' selection criteria explicitly defined? [Clarity, Spec §FR-5]"
   - "Is 'prominent' defined with measurable visual properties? [Ambiguity, Spec §FR-4]"

   Consistency:
   - "Do navigation requirements align across all pages? [Consistency, Spec §FR-10]"
   - "Are card component requirements consistent between landing and detail pages? [Consistency]"

   Coverage:
   - "Are requirements defined for zero-state scenarios (no episodes)? [Coverage, Edge Case]"
   - "Are concurrent user interaction scenarios addressed? [Coverage, Gap]"
   - "Are requirements specified for partial data loading failures? [Coverage, Exception Flow]"

   Measurability:
   - "Are visual hierarchy requirements measurable/testable? [Acceptance Criteria, Spec §FR-1]"
   - "Can 'balanced visual weight' be objectively verified? [Measurability, Spec §FR-2]"

   **SCENARIO CLASSIFYING AND COVERAGE** (requirements quality focus):
   - Check whether requirements exist for: primary, alternate, exception/error, recovery, and non-functional scenarios
   - For each scenario class, ask: "Are [scenario type] requirements complete, clear, and consistent?"
   - If a scenario class is missing: "Are [scenario type] requirements intentionally excluded or missing? [Gap]"
   - Include resilience/rollback when state changes: "Are rollback requirements defined for migration failures? [Gap]"

   **TRACEABILITY REQUIREMENTS**:
   - MINIMUM: >= 80% of items must include at least one traceability reference
   - Each item should reference: the spec section `[Spec §X.Y]`, or use markers: `[Gap]`, `[Ambiguity]`, `[Conflict]`, `[Assumption]`
   - If no ID system exists: "Is a requirement and acceptance-criteria ID scheme established? [Traceability]"

   **SURFACE AND RESOLVE PROBLEMS** (requirements quality problems):
   Ask questions about the requirements themselves:
   - Ambiguity: "Is the term 'fast' quantified with specific metrics? [Ambiguity, Spec §NFR-1]"
   - Conflict: "Do the navigation requirements in §FR-10 and §FR-10a conflict? [Conflict]"
   - Assumption: "Is the 'always-available podcast API' assumption validated? [Assumption]"
   - Dependency: "Are external podcast API requirements documented? [Dependency, Gap]"
   - Missing definition: "Is 'visual hierarchy' defined with measurable criteria? [Gap]"

   **CONTENT CONSOLIDATION**:
   - Soft cap: If raw candidate items > 40, prioritize by risk/impact
   - Merge near-duplicates that check the same requirements facet
   - If >5 low-impact edge cases, create a single item: "Are edge cases X, Y, Z addressed in requirements? [Coverage]"

   **🚫 ABSOLUTELY PROHIBITED** - These make it an implementation test, not a requirements test:
   - ❌ Any item starting with "Verify", "Test", "Confirm", "Check" + implementation behaviour
   - ❌ References to code execution, user actions, system behaviour
   - ❌ "Displays correctly", "works properly", "functions as expected"
   - ❌ "Click", "navigate", "render", "load", "execute"
   - ❌ Test cases, test plans, QA procedures
   - ❌ Implementation details (frameworks, APIs, algorithms)

   **✅ REQUIRED PATTERNS** - These test requirements quality:
   - ✅ "Are [requirement type] defined/specified/documented for [scenario]?"
   - ✅ "Is [vague term] quantified/clarified with specific criteria?"
   - ✅ "Are requirements consistent between [section A] and [section B]?"
   - ✅ "Can [requirement] be objectively measured/verified?"
   - ✅ "Are [edge cases/scenarios] addressed in the requirements?"
   - ✅ "Does the spec define [missing aspect]?"

6. **Structure reference**: Generate the checklist following the canonical template in `templates/checklist-template.md`, including title, meta section, category headings, and ID formatting. If the template is unavailable, use: H1 title, a Purpose/Created meta line, `##` category sections containing `- [ ] CHK### <requirement item>` lines, with IDs incrementing globally from CHK001.

7. **Report**: Output the full path of the created checklist, the item count, and remind the user that each run creates a new file. Summarize:
   - The chosen focus areas
   - The depth level
   - The audience/timing
   - Any explicit must-have items the user included

**IMPORTANT**: Every `/speckit.checklist` command invocation creates a checklist file using a short, descriptive name, unless the file already exists. This allows:

- Multiple checklists of different types (e.g., `ux.md`, `test.md`, `security.md`)
- Simple, memorable file names that indicate the checklist's purpose
- Easy identification and navigation within the `checklists/` folder

To avoid clutter, use descriptive types and clean up stale checklists once done.

## Example Checklist Types and Sample Items

**UX Requirements Quality:** `ux.md`

Sample items (testing requirements, not implementation):

- "Are visual hierarchy requirements defined with measurable criteria? [Clarity, Spec §FR-1]"
- "Are the number and positioning of UI elements explicitly defined? [Completeness, Spec §FR-1]"
- "Are interaction state requirements (hover, focus, active) consistently defined? [Consistency]"
- "Are accessibility requirements specified for all interactive elements? [Coverage, Gap]"
- "Is fallback behaviour defined when images fail to load? [Edge Case, Gap]"
- "Can 'prominent display' be objectively measured? [Measurability, Spec §FR-4]"

**API Requirements Quality:** `api.md`

Sample items:

- "Are error response formats specified for all failure scenarios? [Completeness]"
- "Are rate limiting requirements quantified with specific thresholds? [Clarity]"
- "Are authentication requirements consistent across all endpoints? [Consistency]"
- "Are retry/timeout requirements defined for external dependencies? [Coverage, Gap]"
- "Is the versioning strategy documented in the requirements? [Gap]"

**Performance Requirements Quality:** `performance.md`

Sample items:

- "Are performance requirements quantified with specific metrics? [Clarity]"
- "Are performance targets defined for all critical user journeys? [Coverage]"
- "Are performance requirements specified for different load conditions? [Completeness]"
- "Can performance requirements be objectively measured? [Measurability]"
- "Are degradation requirements defined for high-load scenarios? [Edge Case, Gap]"

**Security Requirements Quality:** `security.md`

Sample items:

- "Are authentication requirements specified for all protected resources? [Coverage]"
- "Are data protection requirements defined for sensitive information? [Completeness]"
- "Is the threat model documented and aligned with the requirements? [Traceability]"
- "Do the security requirements align with compliance obligations? [Consistency]"
- "Are security failure/breach response requirements defined? [Gap, Exception Flow]"

## Anti-Examples: What NOT to Do

**❌ WRONG - These test implementation, not requirements:**

```markdown
- [ ] CHK001 - Verify the landing page displays 3 episode cards [Spec §FR-001]
- [ ] CHK002 - Test that the hover state works correctly on desktop [Spec §FR-003]
- [ ] CHK003 - Confirm clicking the logo navigates to the home page [Spec §FR-010]
- [ ] CHK004 - Check that the related episodes section displays 3-5 items [Spec §FR-005]
```

**✅ CORRECT - These test requirements quality:**

```markdown
- [ ] CHK001 - Are the number and layout of featured episodes explicitly defined? [Completeness, Spec §FR-001]
- [ ] CHK002 - Are hover state requirements consistently defined for all interactive elements? [Consistency, Spec §FR-003]
- [ ] CHK003 - Are navigation requirements clear for all clickable brand elements? [Clarity, Spec §FR-010]
- [ ] CHK004 - Are related-episode selection criteria documented? [Gap, Spec §FR-005]
- [ ] CHK005 - Are loading state requirements defined for asynchronous episode data? [Gap]
- [ ] CHK006 - Can the "visual hierarchy" requirements be objectively measured? [Measurability, Spec §FR-001]
```

**Key differences:**

- Wrong: Tests whether the system works
- Correct: Tests whether the requirements are written correctly
- Wrong: Behaviour verification
- Correct: Requirements quality validation
- Wrong: "Does it do X?"
- Correct: "Is X clearly defined?"
