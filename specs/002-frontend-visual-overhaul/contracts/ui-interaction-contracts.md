# Interaction and API Contracts: Visual and UX Overhaul (Interaction & API Contracts)

**Feature ID**: `002-frontend-visual-overhaul`  
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)  
**Date**: 2026-10-10  
**Status**: APPROVED  

---

## 1. Client-Side JS Contracts

### 1.1 Global HUD Command Controller (`CommandPaletteController`)
Provides the geek-grade `Cmd+K` global search and quick-action channel:

```javascript
/**
 * Open the global HUD command overlay
 * @param {string} [initialQuery=""] - Initial search keyword to prefill
 */
function openCommandPalette(initialQuery = ""): void;

/**
 * Close the global HUD command overlay and release focus
 */
function closeCommandPalette(): void;

/**
 * Register or extend quick commands
 * @param {Array<CommandPaletteItem>} items - Command list
 */
function registerCommands(items): void;
```

### 1.2 Interactive Comparison Showcase Controller (`SandboxComparatorController`)
Used to switch in real time between traditional practice and SmartStudy Compass in the portal and demo scenarios:

```javascript
/**
 * Switch the sandbox display mode
 * @param {'smartstudy' | 'traditional'} mode - Target mode
 */
function setSandboxMode(mode): void;

/**
 * Trigger misconception linkage for a sandbox distractor
 * @param {string} optionKey - Option key ('A' | 'B' | 'C' | 'D')
 */
function inspectSandboxOption(optionKey): void;
```

### 1.3 Deep Reasoning-Chain Dynamic Renderer (`ReasoningRenderer`)
Used to generate the DeepSeek-R1-style reasoning accordion panel:

```javascript
/**
 * Render or collapse the AI thinking-process path
 * @param {HTMLElement} mountTarget - Mount container
 * @param {Array<ReasoningStep>} steps - Reasoning step list
 * @param {boolean} [defaultOpen=false] - Whether to expand by default
 */
function renderReasoningAccordion(mountTarget, steps, defaultOpen = false): HTMLElement;
```

### 1.4 Card Spotlight-Following Effect (`SpotlightGlowEffect`)
Dynamically injects coordinate-driven glow flow on mouse movement:

```javascript
/**
 * Bind mouse-following glow listeners to a container element
 * @param {HTMLElement} containerElement - Parent container holding .spotlight-card elements
 */
function initSpotlightCards(containerElement): void;
```

---

## 2. Backend API Compatibility Contract

This feature is a pure frontend visual overhaul and **keeps 100% backward compatibility with the existing FastAPI interfaces**; the following existing contracts must not be broken:

| Endpoint | Method | Response Data Model | Compatibility Guarantee Requirement |
| :--- | :--- | :--- | :--- |
| `/api/health` | `GET` | `{ status: "ok", version: "1.0.0" }` | Keep the health probe as-is |
| `/api/quiz` | `GET` | `Array<QuestionEntity>` | Keep the question stem, options, trap ID, and topology data model unchanged |
| `/api/diagnose` | `POST` | `DiagnosticResult` | Keep the misconception attribution, prerequisite weakness, and radar-deduction fields unchanged |
| `/api/tutor` | `POST` | `SocraticResponse` | Keep the heuristic follow-up text and guidance level unchanged |
| `/api/graph` | `GET` | `{ nodes: [], edges: [] }` | Keep node coordinates, categories, and relationship-edge topology unchanged |
