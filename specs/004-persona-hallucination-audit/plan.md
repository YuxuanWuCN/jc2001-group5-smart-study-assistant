# Implementation Plan: Main-Repository File Cycle Attribution + Root README Cycle Task Board

**Branch**: `004-persona-hallucination-audit` | **Date**: 2026-10-20 | **Spec**: [spec.md](spec.md)
**Input**: User's original words (m00026): "Tidy up the files in the main repository - work out which ones were done in the first cycle and which cycle the rest belong to, then put what each cycle, i.e. what the current cycle needs to do, in the main README. Is that OK?"

## Summary

The repository has accumulated assets from three cycles - Cycle 1 / Cycle 2 / Cycle 3 - plus an in-progress audit cycle (004), but the root `README.md` still reflects the old Week 1–2 structure (it still describes early files such as `reports/project_proposal.pdf` and `scripts/verify_week1_deliverables.py`). New members therefore cannot tell **which file belongs to which cycle, or what the current cycle should be doing**.

This plan delivers **a verifiable documentation improvement**, without adding feature code:

1. Label every directory / key file under the repository root with its owning cycle (C1 / C2 / C3 / 004), based on git commit dates + each cycle's specification pack + the asset inventory in `reports/cycle3_master_plan.md` §1.1.
2. Write **the current cycle's to-do items (the Cycle 3 report cycle and the parallel 004 audit)** into the root `README.md`, as the whole team's single task entry point.

## Technical Context

**Language / version**: no code changes involved; documentation is Markdown, consistent with the repository's existing body-text conventions
**Main dependencies**: no new dependencies (Constitution principle "introduce no new dependencies")
**Storage**: not applicable
**Testing**: the documentation task does not change code, but before committing `python -m pytest tests/ -q` must be re-run to keep the 145 cases at zero regression (Principle III)
**Target platform**: GitHub web rendering (main repository `YuxuanWuCN/jc2001-group5-smart-study-assistant`)
**Project type**: documentation baseline maintenance (Spec Kit specification package 004)
**Performance goals**: not applicable
**Constraints**: zero root-directory pollution (Principle V); English body text plus the banned-word list (`reports/cycle3_master_plan.md` §3); every cycle determination must be verifiable within the repository and must not rely on memory
**Scale / scope**: one file rewritten (`README.md`), one planning artifact (this file)

## Cycle Determination Basis

| Cycle | Time window (git-verifiable) | Basis for determination |
| :--- | :--- | :--- |
| **Cycle 1** (concept and feasibility) | from 2026-09-23 | `d73e548 chore: initialize JC2001 Group 5 project repository with Week 1/2 baselines`; `practical1_deliverables.md`, the Week 1 team retrospective pack, `project_proposal.*` |
| **Cycle 2** (requirements / modelling / PoC MVP) | 2026-10-08 ~ 2026-10-10, milestone merged 2026-10-16 | `4b5c88c feat(poc): deliver end-to-end runnable MVP PoC`, `10d69d6 Merge develop into main: Phase 2 / Cycle 2 milestone`, `reports/phase2_cycle2_progress_report.md`, `specs/001-*`, `specs/002-*` |
| **Cycle 3** (Reports Cycle, software baseline frozen) | from 2026-10-17 (including the 10-18 / 10-19 commits) | `acded7f docs(cycle3): startup-grade technical report blueprint + 9 task packs`, `reports/cycle3_master_plan.md`, `specs/003-cycle3-startup-report/` |
| **004 audit (parallel to C3)** | from 2026-10-18 | `specs/004-persona-hallucination-audit/`, `scripts/audit_*.py`, `reports/audit/` |
| **Course input (not a cycle artifact)** | — | root-level `*.pdf` / `*.txt` teaching materials, `JC2001-GroupProjectDescription-and-Requirements-2026-27.*` |

## Constitution Check

*Gate: must be passed before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Check conclusion |
| :--- | :--- |
| Principle I Visual aesthetics | No UI involved, no conflict |
| Principle II Zero build | Pure Markdown, no new build step |
| Principle III Zero regression | No code changed; numbers described in the documentation must match measurements (`145 passed` has been re-run and confirmed) |
| Principle IV Dual theme / bilingual | Not involved |
| Principle V Zero root pollution | The README is an existing root file being rewritten; no new root files are added |

**Gate conclusion**: passed, no unjustified violations.

## Project Structure

### Documentation (this feature)

```text
specs/004-persona-hallucination-audit/
├── plan.md              # this file
├── spec.md              # existing audit specification
├── tasks.md             # existing task list
└── contracts/           # existing contracts
README.md                # the only rewrite target in this change (repository root)
```

## Phase 0: Research

**Decision**: cycle attribution is based on git commit times + milestone merge commits, supplemented by the creation date of each `specs/0xx/spec.md`; "last modified time" is not used.
**Rationale**: the `reports/` directory was once deleted and recreated on 2026-10-09 (`84207d9 Delete reports directory`, `d6a32ba Add files via upload`), so file mtimes are unreliable; the commit history is the verifiable fact.
**Alternatives considered**: guessing by directory name (e.g. treating everything under `reports/final_report/` as C3) - rejected because `reports/api_frontend_mapping/` is a C2 artifact yet sits at the same level.

**Decision**: make "current cycle tasks" rather than "all historical tasks" the core content of the README.
**Rationale**: the README's main readers are team members who need to act immediately; historical tasks are complete, and keeping them would dilute attention.
**Alternatives considered**: a week-by-week running log - rejected.

## Phase 1: Design and Deliverables

1. **`README.md` structure** (replacing the content between the existing §📂 Repository Structure and §🚀 Quickstart):
   - add a "cycle map" at the top, with one line stating which cycle we are currently in;
   - `## 📦 File Cycle Attribution`: a table grouped by Cycle 1 / 2 / 3 / 004 / course input, listing path + content + status;
   - `## 🎯 Current Cycle (Cycle 3 report cycle) To-Do`: taken from `reports/cycle3_master_plan.md` §4 division-of-labour matrix + §5 the two gates (G1/G2) + §7 pre-submission checklist;
   - `## 🔬 Parallel Cycle 004 Audit To-Do`: taken from `specs/004-persona-hallucination-audit/tasks.md`;
   - keep the team roster, Quickstart, and Git conventions, and change the Git conventions to a "main repository branch + PR" workflow (no longer encouraging forks).
2. **Contracts / quickstart**: no new API contracts in this change; the "run locally" steps in `quickstart.md` remain valid and need no change.
3. **Agent context update**: running `update-agent-context.ps1 -AgentType claude` is already part of repository maintenance; the manual section of `CLAUDE.md` is not changed in this pass.

## Phase 2: Stop Point

The work ends once the documentation rewrite is complete and the 145 cases have been re-run successfully; it does not proceed to task decomposition (`task.md` already exists and belongs to the 004 audit itself).
