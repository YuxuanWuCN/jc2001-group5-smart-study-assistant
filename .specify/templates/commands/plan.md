---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `{SCRIPT}` from the repository root and parse the JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `/memory/constitution.md`. Load the IMPL_PLAN template (already copied).

3. **Execute the plan workflow**: Follow the structure in the IMPL_PLAN template:
   - Fill the Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill the Constitution Check section from the constitution
   - Evaluate gates (error if violations are unjustified)
   - Phase 0: Generate research.md (resolve all "NEEDS CLARIFICATION")
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update the agent context by running the agent script
   - Re-evaluate the Constitution Check after design

4. **Stop and report**: The command ends after Phase 2 planning. Report the branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from the Technical Context above**:
   - For each "NEEDS CLARIFICATION" → research task
   - For each dependency → best-practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in the Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings in `research.md`** using the format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else was evaluated]

**Output**: research.md with all "NEEDS CLARIFICATION" resolved

### Phase 1: Design & Contracts

**Prerequisites**: `research.md` complete

1. **Extract entities from the feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts from functional requirements**:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schemas to `/contracts/`

3. **Agent context update**:
   - Run `{AGENT_SCRIPT}`
   - These scripts detect the AI agent in use
   - Update the appropriate agent-specific context file
   - Add only new technologies from the current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- Error on gate failures or unresolved clarifications
