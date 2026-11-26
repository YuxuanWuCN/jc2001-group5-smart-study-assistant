---
description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `/memory/constitution.md`. This file is a template containing bracketed placeholder tokens (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments to dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require fewer or more principles than the template uses. Respect their count if specified - otherwise follow the generic template. You will update the document accordingly.

2. Collect/derive values for placeholders:
   - If the user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repository context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (ask or mark TODO if unknown); `LAST_AMENDED_DATE` is today if changes were made, otherwise keep the previous date.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward-incompatible governance/principle removals or redefinitions.
     - MINOR: Adding a new principle/section or materially expanding guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If the version bump type is ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (except intentionally retained template slots whose project-specific choice is not yet defined - explicitly state any retained slots).
   - Preserve heading hierarchy; comments may be removed after replacement unless they still provide clarifying guidance.
   - Ensure each principle section has a concise name line and a paragraph (or bullet list) capturing the non-negotiable rules, with explicit rationale where not obvious.
   - Ensure the Governance section lists amendment procedures, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert the previous checklist into active verification):
   - Read `/templates/plan-template.md` and ensure any "Constitution Check" or rules align with the updated principles.
   - Read `/templates/spec-template.md` to align scope/requirements - update if the constitution adds/removes mandatory sections or constraints.
   - Read `/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `/templates/commands/*.md` (including this one) to verify there are no outdated references (retain agent-specific names like CLAUDE only when generic guidance is needed).
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to changed principles.

5. Produce a Sync Impact Report (prepend as an HTML comment at the top of the constitution file after updating):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - List any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches the report.
   - Dates are in ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `/memory/constitution.md` (overwrite).

8. Output a final summary to the user:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting and style requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (ideally <100 characters), but do not enforce this with awkward line breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies a partial update (e.g., only one principle revision), still perform the validation and version decision steps.

If critical information is missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and list it under the deferred items in the Sync Impact Report.

Do not create a new template; always operate on the existing `/memory/constitution.md` file.
