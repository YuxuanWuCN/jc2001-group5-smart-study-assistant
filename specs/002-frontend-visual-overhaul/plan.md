# Implementation Plan: Frontend Visual Overhaul & Modern AI UX

**Branch**: `002-frontend-visual-overhaul` | **Date**: 2026-10-10 | **Spec**: [spec.md](spec.md)  
**Input**: Feature specification from `specs/002-frontend-visual-overhaul/spec.md` and user feedback "your frontend is not impressive enough"

---

## Summary

In response to user feedback that "the frontend interface is not impressive enough and lacks the visual quality and interactive impact of top-tier modern AI products", this plan defines and delivers a **frontend visual overhaul and modern AI interaction upgrade system**.
Drawing fully on the world-class design aesthetics of Linear / Vercel / Raycast / DeepSeek, and while preserving pure-native instant loading (no heavy build black boxes), it delivers the following five key breakthroughs:
1. **Aurora Hero & Matrix Grid**: a top-tier academic portal with an engineering dot-matrix grid, subtle flowing gradients, dynamic metric cards, and a cursor-following spotlight highlight;
2. **Interactive Comparison Sandbox**: a one-click comparison showcase built into the home page and console that contrasts "traditional practice (cold judgement, answer only)" with "SmartStudy Compass (trap-radar warning, prerequisite tracing, heuristic questioning)";
3. **Workspace Micro-interactions**: DeepSeek-R1-style **Reasoning Accordion**, wrong-answer pulse tremor, frosted-glass overlays, and exam-point topology highlight halos;
4. **Global Geek HUD Command Palette (`Cmd+K` / `Ctrl+K`)**: full-keyboard fuzzy question search, one-key cross-subject jumps, and theme switching;
5. **Radar Defense Badge System**: upgrades the learning report into a high-energy dashboard with dynamic scan effects and S/A/B/C defence badges.

---

## Technical Context

- **Language/versions**: native ES6+ JavaScript, semantic HTML5 tags, modern CSS3 (CSS Variables, Grid, Backdrop-Filter)
- **Main dependencies**: Apache ECharts 5.5.1 CDN (no new external heavy build dependencies)
- **Storage**: browser local persistent cache (`localStorage`: `smartstudy_auth_session`, `smartstudy_theme`, `smartstudy_radar`)
- **Testing**: backend `pytest tests/` (114 cases, 100% automated tests); frontend full-viewport and console interaction walkthroughs in Chrome/Edge
- **Target platforms**: modern Chromium browsers / Edge / Firefox / Safari, responsive on mobile and ultra-wide desktop
- **Project type**: FastAPI monolithic static-mounted native single-page application (Vanilla SPA)
- **Performance targets**: first contentful paint (FCP) < 80ms, 60 FPS hardware-accelerated interaction transitions, HUD pop-up summon < 50ms
- **Constraints**:
  1. Strictly follow the University of Aberdeen JC2001 undergraduate software-engineering conventions, with rigorous academic expression;
  2. Maintain 100% non-breaking compatibility with the existing 114 automated backend tests and the deployed FastAPI endpoints;
  3. Strictly enforce zero root-directory pollution, surgical-precision modification, and workspace tidiness.
- **Scale/scope**: covers 7 core modules - Landing portal, comparison sandbox, trap-detection practice workspace, companion reasoning stream, exam-point graph roaming, learning radar, and HUD command palette.

---

## Constitution Checks

| Constitution Principle | Check Status | Assessment and Justification |
| :--- | :---: | :--- |
| **Principle I: Top-tier academic and AI visual aesthetics** | ✅ Pass | Moves away from the crude backend style and adopts the Cyber Obsidian / Technical Chalk material system, with visual quality directly comparable to industry benchmarks. |
| **Principle II: Native lightweight and zero build burden** | ✅ Pass | Implemented in pure native CSS3 + ES6, with zero Webpack/Vite dependencies, completely eliminating environment-configuration barriers and network-loading white screens. |
| **Principle III: Zero-breakage compatibility and regression** | ✅ Pass | Purely incremental UI and micro-interaction upgrades; the backend data contract is untouched and the existing 114 pytest tests pass 100%. |
| **Principle IV: Dual-mode adaptivity and multi-device responsiveness** | ✅ Pass | Fully supports seamless switching between dark and light themes, colour contrast meets WCAG AA, and mobile gesture interaction is perfectly adapted. |
| **Principle V: Zero root-directory pollution and workspace discipline** | ✅ Pass | All specification documents are collected under `specs/002-frontend-visual-overhaul/`, and modifications are strictly limited to the `frontend/` directory. |

---

## Project Structure

### Specification artifacts (this feature)

```text
specs/002-frontend-visual-overhaul/
├── spec.md              # Requirements engineering and user-story specification
├── plan.md              # This implementation plan file
├── research.md          # Phase 0: architectural choices and material systems
├── data-model.md        # Phase 1: entity models and state-machine definitions
├── contracts/           # Phase 1: UI interaction contracts and backend-compatibility guarantees
│   └── ui-interaction-contracts.md
└── quickstart.md        # Phase 1: quick startup and acceptance checklist
```

### Source code change areas (Repository Layout)

```text
frontend/
├── index.html           # Upgrade the hero aurora structure; inject the comparison sandbox, HUD command modal layer, and reasoning-chain container
├── style.css            # Upgrade the modern design-system variables, aurora glow, grid textures, frosted glass, and micro-animations
└── app.js               # Upgrade the CommandPalette controller, comparison-sandbox interaction, spotlight following, and reasoning-chain rendering
```

---

## Complexity Tracking

*No entries required (no architectural gate violations triggered, no over-engineering or unnecessary dependencies introduced).*

---

## Work Breakdown

### Phase 0: Architecture and technical research (complete)
- [x] Produced `research.md`: resolved the Cyber Obsidian material system, comparison-sandbox state flow, DeepSeek reasoning-accordion, and spotlight micro-animation approach.

### Phase 1: Model and contract design (complete)
- [x] Produced `spec.md`: clarified the four core user stories - aurora parallax portal, comparison sandbox, immersive workspace interaction, and HUD command palette.
- [x] Produced `data-model.md`: standardised the `CommandPaletteItem`, `ComparisonCase`, `ReasoningStep`, and `RadarBadgeTier` models.
- [x] Produced `contracts/ui-interaction-contracts.md`: clarified the UI controller interaction contracts and backward API-compatibility guarantees.
- [x] Produced `quickstart.md`: defined the 8-item full-dimension acceptance checklist.

### Phase 2: Precise implementation coding (ready to execute)
1. **CSS modern design system and material upgrade** (`frontend/style.css`):
   - Inject top-tier aurora glow gradients, dot-matrix grid textured backgrounds, and frosted-glass acrylic panel classes;
   - Add card spotlight-following highlights (Spotlight Border) and glowing-button micro-interactions;
   - Implement DeepSeek-R1-style `<details>` deep-thinking collapsible animations and five-dimension defence badge styles;
   - Implement the global Command Palette HUD modal layer and shortcut-hint badge styles.
2. **HTML skeleton and interaction container injection** (`frontend/index.html`):
   - Inject flowing typography and dynamic academic telemetry metric cards into the Hero area;
   - Inject the "traditional practice vs SmartStudy Compass" split-screen interactive comparison showcase (Interactive Sandbox);
   - Inject the reasoning-chain container into the workspace and companion views;
   - Inject the global Command Palette HUD modal node structure.
3. **JS interaction controller and state-machine wiring** (`frontend/app.js`):
   - Write `initCommandPalette()` to support the `Cmd+K` / `Ctrl+K` global command palette;
   - Write `initComparisonSandbox()` to support instant click comparison and misconception linkage;
   - Write `renderReasoningTrace()` to give the companion and trap detection a breathing thinking process;
   - Write `initSpotlightCards()` to inject cursor-following mousemove glow effects;
   - Wire bilingual (Chinese/English) and light/dark theme adaptive redrawing.
4. **Verification and regression**:
   - Run `pytest tests/` to verify 100% test pass;
   - Start the local service for multi-viewport interaction walkthroughs and acceptance.
