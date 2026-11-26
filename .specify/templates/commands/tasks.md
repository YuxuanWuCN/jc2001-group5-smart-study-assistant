---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json
  ps: scripts/powershell/check-prerequisites.ps1 -Json
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `{SCRIPT}` from the repository root and parse FEATURE_DIR and the AVAILABLE_DOCS list. All paths must be absolute. For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what is available.

3. **Execute task generation workflow**:
   - Load plan.md and extract the tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map them to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see task generation rules below)
   - Generate a dependency graph showing user story completion order
   - Create parallel execution examples for each user story
   - Validate task completeness (each user story has all needed tasks and is independently testable)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as the structure, filling in:
   - The correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story, in priority order from spec.md
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final phase: Polish and cross-cutting concerns
   - All tasks must follow the strict checklist format (see task generation rules below)
   - Clear file paths for each task
   - Dependency section showing story completion order
   - Parallel execution examples for each story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output the generated tasks.md path and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically User Story 1 only)
   - Format validation: Confirm that ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: {ARGS}

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks must be organized by user story to enable independent implementation and testing.

**Tests are optional**: Generate test tasks only when explicitly requested in the feature specification or when the user requests a TDD approach.

### Checklist Format (REQUIRED)

Every task must strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number in execution order (T001, T002, T003...)
3. **[P] marker**: Include ONLY if the task is parallelizable (different file, no dependency on incomplete tasks)
4. **[Story] label**: Required ONLY for user story phase tasks
   - Format: [US1], [US2], [US3], etc. (maps to the user stories in spec.md)
   - Setup phase: No story label
   - Foundational phase: No story label  
   - User story phases: MUST have a story label
   - Polish phase: No story label
5. **Description**: Clear action with the exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure according to the implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests are requested: specific tests for that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests are requested: each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If an entity serves multiple stories: put it in the earliest story or the setup phase
   - Relationships → service layer tasks in the appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish and cross-cutting concerns
