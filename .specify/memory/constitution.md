# JC2001 Group 5 SmartStudy Compass Project Constitution

**Project name**: An intelligent STEM study-assistant system for university students based on cognitive graphs and question-trap topology (SmartStudy Assistant)  
**Course**: University of Aberdeen JC2001 Software Engineering (2026–27) · Group 5 (BSc BMIS)  
**Version**: 2.0.0 | **Last revised**: 2026-10-10  

---

## Core Development and Design Principles

### Principle I: Top-Tier Academic & AI Aesthetics
- The interface must never look cheap or rough; it must match the refined quality of modern high-end technical products (Linear / Vercel / Raycast / DeepSeek).
- Incorporate ambient glow, a technical grid texture, layered backdrop-filter glassmorphism, and precise typographic hierarchy contrasts.
- Ensure information presentation meets the rigorous academic standards of an Aberdeen University Honours Project while carrying the modern tech-interaction impact that impresses judges and users.

### Principle II: Native Instant Loading & Zero Build Friction
- Stick with a native HTML5 / CSS3 / ES6+ architecture, with no complex Webpack/Vite build black box, so the app runs as soon as it is opened in a local browser (first contentful paint FCP < 100ms).
- Keep components modular and highly cohesive; use CSS Variables as semantic design tokens in CSS, and an event bus plus clear state machines in JS.

### Principle III: Zero Regression & Test Preservation
- The existing 147 backend pytest automated tests (145 measured on 2026-10-25, plus 2 dual-naming regression cases; the earlier figure of 114 was the Cycle 2 count — this revision awaits PM confirmation) and the FastAPI endpoints (`/api/health`, `/api/quiz`, `/api/diagnose`, `/api/graph`, `/api/tutor`) must keep passing 100% with protocol compatibility.
- The existing functional logic, student-ID login state, local cache (`localStorage`), and the core reasoning chain of the misconception topology must not be broken.

### Principle IV: Fluid Dual-Theme & Responsive Ergonomics
- Natively support both "Deep Space Aurora (Dark Mode)" and "Academic Tech White (Light Mode)", with contrast ratios strictly meeting WCAG AA.
- Adapt responsively to mobile, tablet, and 4K ultra-wide desktops; keep transition animations smooth at 60 FPS with hardware acceleration.
- Fully preserve seamless ZH/EN bilingual internationalization switching.

### Principle V: Zero Root Pollution & Space Hygiene
- Never create temporary scripts, intermediate test files, or clutter in the project root.
- All planning documents, data models, and API contracts are consolidated under the corresponding structure in `specs/002-frontend-visual-overhaul/`.

---

## Quality Gates and Governance Rules

1. **Visual and interaction gate**: any new UI must pass colour-contrast, viewport-adaptation, micro-animation smoothness, and bilingual-match tests.
2. **Regression gate**: the test suite must be run before and after any code commit, keeping `pytest tests/` at a 100% pass rate.
3. **Architectural justification**: do not introduce heavy, bloated third-party libraries just to show off; strictly preserve the explainability expected of undergraduate software engineering and the defensibility required at an academic viva.
