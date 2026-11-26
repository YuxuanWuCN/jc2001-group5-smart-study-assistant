# Feature Specification: Frontend Visual Overhaul & Modern AI UX

**Feature ID**: `002-frontend-visual-overhaul`  
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)  
**Created**: 2026-10-10  
**Status**: APPROVED / READY FOR PLANNING & IMPLEMENTATION  
**Related branch**: `002-frontend-visual-overhaul`  
**Input**: User feedback "your frontend is not impressive enough" — the interface must transform from an "ordinary course-project / flat static display" into a highly distinctive interactive interface with "world-class AI software quality (Linear/Vercel/DeepSeek level)".

---

## 1. Business Context and Pain-Point Analysis

### 1.1 Current-State Diagnosis: the Root Cause of "Not Impressive Enough"
The system's core logic and knowledge base are extremely solid, but in terms of visual presentation and frontend interaction there is a clear "visual downgrade" bottleneck:
1. **Flat, bland visuals with no spatial depth of a modern AI product**:
   - The existing Landing page is a traditional card display, lacking the signature features of modern top-tier products: **Ambient Glow / Aurora Gradients, Tech Grid & Dot Matrix Pattern, multi-layer Backdrop Glassmorphism**.
   - Headline copy and typographic rhythm are too soft; they fail to convey, within 3 seconds, the top-tier technological impact of "University of Aberdeen Honours Project + GraphRAG misconception-topology tracing".
2. **Monotonous interaction feedback, lacking the vitality of "deep thinking"**:
   - The AI study companion (Socratic tutoring) output is relatively static, missing the benchmark **Reasoning / Thinking Accordion** and breathing pulse thinking states of DeepSeek-R1 / Claude 3.7.
   - When a wrong answer is chosen in the trap-detection practice, trap hints are not striking enough; alarm micro-animations and topology spotlight effects are missing when a thinking trap triggers.
3. **Missing a killer real-time interactive showcase**:
   - Visitors or reviewer tutors must click through everything to understand the difference from conventional drill software. A **split-screen sandbox** comparing "traditional rote learning vs SmartStudy Compass misconception topology", which works without login, is missing.
4. **Missing the geek interaction of advanced tools**:
   - The **global HUD Command Palette (`Cmd+K` / `Ctrl+K`)** preferred by modern developers and student geeks is missing, so there is no global fast jump to subjects, questions, and knowledge-graph nodes.

### 1.2 Upgrade Goal (Design North Star)
With **"Academic Rigor + Linear-Grade Aesthetics + Socratic Vitality"** as the North Star, complete a full-dimensional rebuild of the frontend visual and interaction experience.

---

## 2. User Scenarios and Acceptance Specification (User Stories & Acceptance)

### US-01: Visually Striking Aurora Parallax Portal (Hero & Aurora Visuals) (Priority: P1)
- **Scenario description**: As a University of Aberdeen course reviewer tutor or new visitor, when I open the system home page, the first thing I see is dynamic aurora glow with a strong technological aesthetic, a fine engineering grid background, dynamically scrolling data telemetry cards, and a striking academic brand slogan, establishing a top-tier professional understanding of the project within 3 seconds.
- **Independent test**: Open the home page and verify that the background grid and glow rendering, telemetry data badges, and card hover micro-animations are displayed correctly.
- **Acceptance scenarios**:
  1. **Given** a user visits the root page, **when** the page finishes loading, **then** the background shows a fine technical dot-matrix grid, the main slogan has a subtle flowing-gradient shimmer, and metric cards play smooth staggered entrance animations.
  2. **Given** the mouse hovers over a feature card, **when** the pointer moves, **then** the card border and background show a flowing spotlight highlight that follows the cursor (Spotlight Border Effect).

---

### US-02: Interactive "Traditional vs Compass" Dual-Core Comparison Showcase (Interactive Comparison Sandbox) (Priority: P1)
- **Scenario description**: As a reviewer tutor or student, I want to flip a comparison toggle on the home page to directly see how the same wrong answer plays out in completely different ways under "traditional AI (only gives the standard answer, deprives thinking, lacks attribution)" and "SmartStudy Compass (trap-radar warning, prerequisite tracing, multi-round Socratic questioning)".
- **Independent test**: On the portal without logging in, click "Traditional answering mode" and "SmartStudy Compass mode" in the interactive comparison component and observe the dynamic feedback and knowledge-path evolution on the right.
- **Acceptance scenarios**:
  1. **Given** the portal comparison sandbox is displayed, **when** traditional mode is clicked, **then** cold right/wrong labels and blunt answer text are shown;
  2. **Given** switching to SmartStudy Compass mode, **when** the same distractor is clicked, **then** the thinking-trap red zone dynamically expands, prerequisite dependencies are highlighted, and a Socratic heuristic question card is generated.

---

### US-03: Full Immersive Micro-interaction Upgrade for the Learning Workspace (Workspace Micro-interactions) (Priority: P1)
- **Scenario description**: As a daily learner, when I answer questions, chat, browse the graph, and view reports in the workspace, each interface should offer high-end motion and visual depth:
  - **Smart trap-detection practice (`#view-quiz`)**: wrong options show a red warning tremor, and the trap drawer has a frosted-glass blurred background and smooth slide-in;
  - **Socratic study companion (`#view-tutor`)**: adds a "🧠 Deep thinking..." collapsible reasoning panel (DeepSeek-R1 style chain of thought), typewriter streaming animation, and staged hint bubbles;
  - **Exam-point graph (`#view-graph`)**: ECharts canvas integrated with a full-screen roaming toolbar, highlighted centre halo, prerequisite/successor dependency breathing lights, and a right-side concept deep-dive hover card;
  - **Learning radar (`#view-report`)**: five-dimension ability radar chart with a dynamic radar sweep line, five-dimension defence badges (S-tier Pioneer Scholar / A-tier Steady Mastery / B-tier Developing), and high-risk weakness breakthrough cards.
- **Independent test**: Enter each of the four tabs in turn, trigger a wrong answer, AI conversation, graph interaction, and report generation, and verify that all micro-animations are smooth and jank-free (>= 60 FPS).
- **Acceptance scenarios**:
  1. **Given** a user clicks a wrong option in the practice area, **when** diagnosis completes, **then** a flicker-free frosted-glass drawer slides out, and a radar deduction toast with dynamic particle glow appears in the bottom-right corner;
  2. **Given** a user sends a question to the companion, **when** the AI replies, **then** it first shows an expandable "Thinking Process" block and then streams the Socratic guidance.

---

### US-04: Global Geek HUD Command Palette (Command Palette `Cmd+K` / `Ctrl+K`) (Priority: P2)
- **Scenario description**: As an efficient university student or presenter who is used to keyboard operation, I want to press `Ctrl+K` or `Cmd+K` at any time (or click the top-bar quick search) to summon the global command overlay, where a quick fuzzy search can find questions, jump across subjects, and quickly switch theme or preset identity.
- **Independent test**: Press the shortcut in any view and verify that the pop-up appears centred; typing "Civil Law" or "Computer Organization" locates and jumps in one action.
- **Acceptance scenarios**:
  1. **Given** the user is on any interface, **when** `Ctrl+K` or `Cmd+K` is pressed, **then** a centred frosted-glass command palette pops up smoothly, with a depth-of-field blur applied to the background;
  2. **Given** a keyword is entered and Enter is pressed, **when** the target action is selected, **then** it executes instantly and the command palette closes automatically.

---

### US-05: Premium Dual-Theme and High-Contrast Engineering Palette (Dual-Theme Harmony) (Priority: P2)
- **Scenario description**: As a user studying for long sessions, I want high reading comfort in both light and dark modes:
  - **Dark mode (Cyber Obsidian)**: deep black-grey base + layered ambient glow + fluorescent blue/emerald/crimson state accents, with a cutting-edge AI console character;
  - **Light mode (Technical Chalk)**: premium paper-white/cloud-grey base + fine shadows + pure navy/ink-black text, matching rigorous university academic quality.
- **Independent test**: Click the theme toggle in the top bar and verify that all text, cards, ECharts charts, and drawers transition smoothly with no inverted contrast.
- **Acceptance scenarios**:
  1. **Given** the theme toggle button is clicked, **when** the `data-theme` attribute switches, **then** global variables transition smoothly, ECharts automatically redraws with the adapted palette, and all text contrast is above 4.5:1 (WCAG AA).

---

## 3. Non-Functional Requirements and Architecture Constraints

- **NFR-01 (Zero Additional Build Dependencies)**: pure native Vanilla JavaScript ES6+ and modern CSS3 (CSS Grid, Flexbox, CSS Variables, Backdrop-Filter), without introducing a Tailwind compiler, React, Vue, or any large third-party animation library, keeping local execution fast.
- **NFR-02 (Extreme Performance and Frame Rate)**: all animations prefer CSS `transform` and `opacity` hardware acceleration; regular operation transitions are kept within 150ms-250ms and a jank-free 60 FPS is maintained.
- **NFR-03 (Zero-Breakage Regression)**: all existing FastAPI APIs (`/api/health`, `/api/quiz`, `/api/diagnose`, `/api/graph`, `/api/tutor`) and the 114 pytest tests remain 100% compatible and passing.
- **NFR-04 (Zero Root Pollution)**: design and specification documents are fully archived under `specs/002-frontend-visual-overhaul/`.
