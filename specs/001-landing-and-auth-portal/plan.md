# Implementation Plan: Landing & Auth Portal

**Branch**: `001-landing-and-auth-portal` | **Date**: 2026-10-08 | **Spec**: [spec.md](spec.md)  
**Input**: Feature specification from `specs/001-landing-and-auth-portal/spec.md`

---

## Summary

In response to user feedback that "the current interface is awkward, and going straight into the cold, dense Eval Harness makes the experience abrupt", design and deliver a polished **Landing & Auth Portal for an undergraduate STEM intelligent study-assistant product**.
As the system's first reception point, the portal clearly communicates the University of Aberdeen JC2001 Group 5 project positioning, the core innovative value of the misconception graph, and the four feature modules; it embeds a quick-login channel for the ten core team members' student profiles; it supports a one-click smooth transition into the daily practice and trap-detection workspace (the "everyday interface"), and it offers a bidirectional channel in the workspace to return to the product introduction page at any time.

---

## Technical Context

- **Language/runtime**: native ES6+ JavaScript, HTML5, CSS3 (zero-friction integration with the existing frontend code)
- **Backend service**: FastAPI (Python 3.11/3.13), Uvicorn asynchronous service, static-mount mode
- **Dependency management**: zero new external frontend build dependencies (no Webpack/Vite compilation burden, instant open and instant test), reusing the already installed ECharts 5.5.1 CDN
- **State storage**: browser local persistent cache (`localStorage`: `smartstudy_auth_session`, `smartstudy_theme`)
- **Target platforms**: modern Chromium browsers / Firefox / Edge / Safari, responsive on mobile and desktop
- **Performance targets**: home-page load time < 100ms, portal-to-workspace view switch latency < 150ms (60fps hardware-accelerated transition)
- **Core constraints**:
  1. Strictly follow JC2001 undergraduate software-engineering conventions, without commercial-grade over-engineering;
  2. Maintain 100% non-breaking compatibility with the existing 114 automated backend tests and the deployed `/api/diagnose` logic;
  3. Comply with the zero-root-pollution, surgical-precision modification, and workspace-tidiness principles.

---

## Constitution Checks

| Check Item | Status | Assessment and Justification |
| :--- | :--- | :--- |
| **Undergraduate capability boundary** | ✅ Pass | Uses the classic lightweight dual-container SPA switching pattern; the logic is clear and explainable, and easy to present to tutors during the defence. |
| **Test and quality regression** | ✅ Pass | Does not break any existing route or data model, guaranteeing the existing `pytest tests/` keeps a 100% pass rate. |
| **File operation discipline** | ✅ Pass | All new documents are collected under `specs/001-landing-and-auth-portal/`; root-directory pollution is prohibited. |
| **Existing code integrity** | ✅ Pass | All original `#app-shell` console logic is treated as a protected controlled sub-container, with incremental wrapping and bridging only. |

---

## Project Structure

### Specification artifacts (this feature)

```text
specs/001-landing-and-auth-portal/
├── spec.md              # Requirements engineering and user-story specification
├── plan.md              # This implementation plan file
├── research.md          # Phase 0: architectural choices and state-machine transitions
├── data-model.md        # Phase 1: student identity and session data model
├── contracts/           # Phase 1: view lifecycle and interface contracts
│   └── portal-auth-contracts.md
└── quickstart.md        # Phase 1: one-click startup and acceptance checklist
```

### Source code change areas (Repository Layout)

```text
frontend/
├── index.html           # Incrementally embed the #portal-landing portal structure, coordinating with #app-shell
├── style.css            # Incrementally add responsive styles for the product introduction portal and role cards
└── app.js               # Incrementally inject switchRootView, initAuthPortal and preset-account wiring
```

**Structure decision**: use a cohesive extension pattern, making the introduction portal the first-level router at the frontend root level. When the user is not signed in or actively views the introduction, `#portal-landing` is shown; after entry, the original `#app-shell` workspace is activated.

---

## Complexity Tracking

*No entries required (no architectural gate violations triggered, no over-engineering introduced).*

---

## Work Breakdown

### Phase 0: Architecture and technical research (complete)
- [x] Produced `research.md`: resolved the SPA container switching, localStorage persistence, and dual-mode theme adaptation approach.

### Phase 1: Model and contract design (complete)
- [x] Produced `spec.md`: clarified the three major requirements - product introduction, role selection, and return to home page.
- [x] Produced `data-model.md`: standardised `StudentProfile`, `AuthSession`, and the preset accounts.
- [x] Produced `contracts/portal-auth-contracts.md`: defined `switchRootView` and `loginStudent`.
- [x] Produced `quickstart.md`: defined the quick-start and three-step acceptance checklist.

### Phase 2: Precise implementation coding (ready to execute)
1. **HTML skeleton injection** (`frontend/index.html`): inject the contemporary `#portal-landing` portal node before `#app-shell`; inject a "Back to product home" channel inside `#app-sidebar`.
2. **CSS styling additions** (`frontend/style.css`): write the Hero banner, the four-feature card grid, the preset-identity quick-switch panel, and fluid transition animations.
3. **JS logic wiring** (`frontend/app.js`): implement `initAuthPortal()`, `switchRootView()`, quick loading of preset roles, and bidirectional smooth switching.
4. **Verification and regression**: start the service and verify the interactions, run the pytest test suite, and capture acceptance screenshots.
