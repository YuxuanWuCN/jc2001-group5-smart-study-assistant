---
description: Non-destructively analyze spec.md, plan.md, and tasks.md for cross-artifact consistency and quality after task generation.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, duplications, ambiguities, and underspecified items across the three core artifacts (`spec.md`, `plan.md`, `tasks.md`) before implementation. This command MUST run only after `/speckit.tasks` has successfully produced a complete `tasks.md`.

## Operating Constraints

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report. Offer an optional remediation plan (the user must explicitly approve it before any follow-up editing commands are invoked manually).

**Constitution Authority**: The project constitution (`/memory/constitution.md`) is **non-negotiable** within this analysis scope. Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or tasks - not dilution, reinterpretation, or silent ignoring of the principle. If a principle itself needs to change, that must happen in a separate, explicit constitution update outside `/speckit.analyze`.

## Execution Steps

### 1. Initialize Analysis Context

Run `{SCRIPT}` once from the repository root and parse the JSON for FEATURE_DIR and AVAILABLE_DOCS. Derive absolute paths:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Abort with an error message if any required file is missing (instruct the user to run the missing prerequisite command).
For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

### 2. Load Artifacts (Progressive Disclosure)

Load only the minimal necessary context from each artifact:

**From spec.md:**

- Overview/Context
- Functional Requirements
- Non-Functional Requirements
- User Stories
- Edge Cases (if present)

**From plan.md:**

- Architecture/stack choices
- Data Model references
- Phases
- Technical constraints

**From tasks.md:**

- Task IDs
- Descriptions
- Phase grouping
- Parallel markers [P]
- Referenced file paths

**From constitution:**

- Load `/memory/constitution.md` for principle validation

### 3. Build Semantic Models

Create internal representations (do not include raw artifacts in output):

- **Requirements inventory**: each functional + non-functional requirement with a stable key (derive a slug from the imperative sentence; e.g., "Users can upload a file" → `user-can-upload-file`)
- **User story/action inventory**: discrete user actions with acceptance criteria
- **Task coverage mapping**: map each task to one or more requirements or stories (infer via keyword/explicit reference patterns such as IDs or key terms)
- **Constitution rule set**: extract principle names and MUST/SHOULD normative statements

### 4. Detection Passes (Token-Efficient Analysis)

Focus on high-signal findings. Limit to 50 findings total; aggregate the rest in an overflow summary.

#### A. Duplication Detection

- Identify near-duplicate requirements
- Mark lower-quality phrasing for consolidation

#### B. Ambiguity Detection

- Flag vague adjectives lacking measurable criteria (fast, scalable, secure, intuitive, robust)
- Flag unresolved placeholders (TODO, TKTK, ???, `<placeholder>`, etc.)

#### C. Underspecification

- Requirements with verbs but missing objects or measurable outcomes
- User stories missing acceptance criteria alignment
- Tasks referencing files or components not defined in the spec/plan

#### D. Constitution Alignment

- Any requirement or plan element conflicting with a MUST principle
- Missing mandated sections or quality gates from constitution

#### E. Coverage Gaps

- Requirements with no associated tasks
- Tasks with no mapped requirement/story
- Non-functional requirements not reflected in tasks (e.g., performance, security)

#### F. Inconsistency

- Terminology drift (the same concept named differently across files)
- Data entities referenced in the plan but missing in the spec (and vice versa)
- Task ordering contradictions (e.g., integration tasks before foundational setup tasks without a dependency note)
- Conflicting requirements (e.g., one requirement demands Next.js while another specifies Vue)

### 5. Severity Assignment

Use this heuristic to prioritize findings:

- **CRITICAL**: Violates constitution MUST, missing core spec artifact, or a requirement with zero coverage that blocks baseline functionality
- **HIGH**: Duplicate or conflicting requirements, ambiguous security/performance attributes, untestable acceptance criteria
- **MEDIUM**: Terminology drift, missing non-functional task coverage, underspecified edge cases
- **LOW**: Style/wording improvements, minor redundancies that do not affect execution order

### 6. Produce a Compact Analysis Report

Output a Markdown report (do NOT write to file) with the following structure:

## Specification Analysis Report

| ID | Category | Severity | Location | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge wording; keep the clearer version |

(Add one row per finding; generate stable IDs prefixed with the category initial.)

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|

**Constitution Alignment Issues:** (if any)

**Unmapped Tasks:** (if any)

**Metrics:**

- Total Requirements
- Total Tasks
- Coverage % (requirements with >=1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

### 7. Provide Next Actions

At the end of the report, output a concise Next Actions block:

- If CRITICAL issues exist: recommend resolving before `/speckit.implement`
- If only LOW/MEDIUM: the user may proceed, but offer improvement suggestions
- Provide explicit command suggestions: e.g., "Run /speckit.specify with refinements", "Run /speckit.plan to adjust architecture", "Manually edit tasks.md to add coverage for 'performance-metrics'"

### 8. Offer Remediation

Ask the user: "Would you like me to suggest concrete remediation edits for the top N issues?" (Do NOT apply them automatically.)

## Operating Principles

### Context Efficiency

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; do not dump everything into the analysis
- **Token-efficient output**: Limit findings tables to 50 rows; summarize overflow
- **Deterministic results**: Re-running without changes should produce consistent IDs and counts

### Analysis Guidelines

- **NEVER modify files** (this is read-only analysis)
- **NEVER hallucinate missing sections** (if absent, report them accurately)
- **Prioritize constitution violations** (these are always CRITICAL)
- **Use examples over exhaustive rules** (cite specific instances, not generic patterns)
- **Report zero issues gracefully** (emit a success report with coverage statistics)

## Context

{ARGS}
