---
description: Execute the implementation plan by processing and executing all tasks defined in tasks.md
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. Run `{SCRIPT}` from the repository root and parse FEATURE_DIR and the AVAILABLE_DOCS list. All paths must be absolute. For single quotes in arguments like "I'm Groot", use escape syntax: e.g. 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Check checklist status** (if FEATURE_DIR/checklists/ exists):
   - Scan all checklist files in the checklists/ directory
   - For each checklist, count:
     - Total items: all lines matching `- [ ]` or `- [X]` or `- [x]`
     - Completed items: lines matching `- [X]` or `- [x]`
     - Incomplete items: lines matching `- [ ]`
   - Create a status table:

     ```text
     | Checklist | Total | Completed | Incomplete | Status |
     |-----------|-------|-----------|------------|--------|
     | ux.md     | 12    | 12        | 0          | ✓ PASS |
     | test.md   | 8     | 5         | 3          | ✗ FAIL |
     | security.md | 6   | 6         | 0          | ✓ PASS |
     ```

   - Calculate overall status:
     - **PASS**: All checklists have 0 incomplete items
     - **FAIL**: One or more checklists have incomplete items

   - **If any checklist is incomplete**:
     - Display the table with incomplete item counts
     - **STOP** and ask: "Some checklists are incomplete. Do you still want to proceed with implementation? (yes/no)"
     - Wait for the user's response before continuing
     - If the user says "no", "wait", or "stop", then stop execution
     - If the user says "yes", "proceed", or "continue", then continue to step 3

   - **If all checklists are complete**:
     - Display the table showing all checklists passed
     - Automatically continue to step 3

3. Load and analyze the implementation context:
   - **REQUIRED**: Read tasks.md for the complete task list and execution plan
   - **REQUIRED**: Read plan.md for the tech stack, architecture, and file structure
   - **IF EXISTS**: Read data-model.md for entities and relationships
   - **IF EXISTS**: Read contracts/ for API specifications and test requirements
   - **IF EXISTS**: Read research.md for technical decisions and constraints
   - **IF EXISTS**: Read quickstart.md for integration scenarios

4. **Project setup verification**:
   - **REQUIRED**: Create/verify ignore files based on the actual project setup:

   **Detection and creation logic**:
   - Check whether the following command succeeds to determine whether the repository is a git repository (if so, create/verify .gitignore):

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```

   - Check whether Dockerfile* exists or Docker is referenced in plan.md → create/verify .dockerignore
   - Check whether .eslintrc* or eslint.config.* exists → create/verify .eslintignore
   - Check whether .prettierrc* exists → create/verify .prettierignore
   - Check whether .npmrc or package.json exists → create/verify .npmignore (if publishing)
   - Check whether terraform files (*.tf) exist → create/verify .terraformignore
   - Check whether .helmignore is needed (helm charts present) → create/verify .helmignore

   **If an ignore file already exists**: Verify it contains essential patterns, append only missing critical patterns
   **If an ignore file is missing**: Create it with a complete pattern set for the detected technologies

   **Common patterns by technology** (from the plan.md tech stack):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `Makefile`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Tool-specific patterns**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

5. Parse the tasks.md structure and extract:
   - **Task phases**: Setup, Tests, Core, Integration, Polish
   - **Task dependencies**: Sequential vs parallel execution rules
   - **Task details**: IDs, descriptions, file paths, parallel markers [P]
   - **Execution flow**: Ordering and dependency requirements

6. Execute the implementation following the task plan:
   - **Phase-by-phase execution**: Complete each phase before moving to the next
   - **Respect dependencies**: Run sequential tasks in order; parallel tasks [P] can run together  
   - **Follow TDD approach**: Execute test tasks before their corresponding implementation tasks
   - **File-based coordination**: Tasks affecting the same files must run sequentially
   - **Validation checkpoints**: Verify each phase's completion before continuing

7. Implementation execution rules:
   - **Setup first**: Initialize the project structure, dependencies, configuration
   - **Tests before code**: If tests need to be written for contracts, entities, and integration scenarios
   - **Core development**: Implement models, services, CLI commands, endpoints
   - **Integration work**: Database connections, middleware, logging, external services
   - **Polish and validation**: Unit tests, performance optimization, documentation

8. Progress tracking and error handling:
   - Report progress after each completed task
   - Stop execution if any non-parallel task fails
   - For parallel tasks [P], continue with the successful tasks and report the failed ones
   - Provide clear error messages and debugging context
   - Suggest next steps if implementation cannot continue
   - **IMPORTANT** For completed tasks, make sure to mark them as [X] in the task file.

9. Completion validation:
   - Verify that all required tasks are completed
   - Check that the implemented feature matches the original spec
   - Verify tests pass and coverage meets the requirements
   - Confirm the implementation follows the technical plan
   - Report the final status and a summary of the completed work

Note: This command assumes a complete task breakdown exists in tasks.md. If tasks are incomplete or missing, suggest running `/speckit.tasks` first to regenerate the task list.
