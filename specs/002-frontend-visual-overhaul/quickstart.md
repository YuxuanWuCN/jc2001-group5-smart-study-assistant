# Quickstart and Verification Guide: Frontend Visual Overhaul (Quickstart & Verification Guide)

**Feature ID**: `002-frontend-visual-overhaul`  
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)  
**Date**: 2026-10-10  
**Status**: APPROVED  

---

## 1. Quick Startup and Local Preview

The system is a native lightweight pure-frontend plus FastAPI architecture with zero build configuration - open and test immediately:

### Option A: Start the full-featured FastAPI local backend (recommended)
Run in a command line:
```powershell
python -m uvicorn backend.app.main:app --reload --port 8000
```
Or run the convenience launcher script directly:
```powershell
python backend/run.py
```
Then visit the following in a modern browser: `http://localhost:8000/`

---

## 2. Core Visual and Interaction Acceptance Checklist

| No. | Acceptance Scenario | Steps | Expected Result (tick when satisfied) | Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **Aurora glow and grid background** | Open the home page `http://localhost:8000/` | The background shows a fine technical dot-matrix grid, the main title has a subtle glowing shimmer, and metric cards fade in smoothly in staggered order | [ ] |
| **02** | **Mouse spotlight highlight effect** | Move the mouse over feature cards and identity cards | The card border lights up with a dynamic aurora glow highlight that follows the cursor position (Spotlight Effect) | [ ] |
| **03** | **Traditional vs Compass comparison showcase** | Toggle between "Traditional mode" and "SmartStudy Compass" in the portal comparison sandbox | Traditional mode shows cold mechanical right/wrong verdicts; Compass mode dynamically expands the thinking-trap red zone and prerequisite tracing | [ ] |
| **04** | **Global HUD command palette (Cmd+K)** | Press `Ctrl+K` or `Cmd+K` on the keyboard | A frosted-glass command menu pops up, supporting fuzzy search, up/down keyboard navigation, and one-key subject jumps | [ ] |
| **05** | **DeepSeek-style reasoning chain expansion** | Enter the "Socratic study companion" and trigger a question reply | A breathing "🧠 Expand deep thinking process" micro-badge appears; expanding it reveals the 4-step cognitive-graph arbitration evidence | [ ] |
| **06** | **Five-dimension defence badges and radar sweep** | Enter the "Holistic learning diagnosis" view | A dynamic five-dimension radar chart and S/A/B/C defence badges appear, with high-risk blind spots showing alarming micro-pulses | [ ] |
| **07** | **Seamless geek dual-theme switching** | Click the theme toggle in the top-right corner | Dark (Cyber Obsidian) and light (Technical Chalk) modes transition smoothly with no contrast inversion whatsoever | [ ] |
| **08** | **Automated quality gate and regression** | Run `pytest tests/` | All 114 existing test cases keep passing 100%, with zero breaking changes | [ ] |
