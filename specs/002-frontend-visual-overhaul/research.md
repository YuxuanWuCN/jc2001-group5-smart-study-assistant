# Technical Research and Architecture Decisions: Frontend Visual Overhaul (Research & Architecture Decisions)

**Feature ID**: `002-frontend-visual-overhaul`  
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)  
**Date**: 2026-10-10  
**Status**: COMPLETED / APPROVED  

---

## 1. Research Questions and Architecture Choices

### Decision 1: Visual aesthetics system and material technology selection
- **Decision**: adopt the **Cyber Obsidian (deep-space aurora dark)** and **Technical Chalk (academic-tech light)** dual-mode modern industrial aesthetics. The foundation uses a modern native CSS-variable design system, multi-layer acrylic frosted glass (`backdrop-filter: blur(16px)`), aurora glow gradients, and engineering grid/dot-matrix textures.
- **Rationale**:
  1. The reason modern top-tier AI tools (Linear, Raycast, Vercel, DeepSeek) look so stunning is the "sense of spatial depth" and "subtle glowing materiality", not merely different colours;
  2. Pure native CSS Variables and modern CSS3 features natively support hardware acceleration, require no bulky third-party framework, and open instantly offline (first contentful paint FCP < 80ms);
  3. Strictly complies with Constitution Principles I and II, with zero external build black boxes.
- **Alternatives considered**:
  - *Tailwind CSS CDN*: large runtime payload, adding extra CDN dependency and style-override conflicts; rejected.
  - *Bootstrap / Ant Design*: highly homogenised, strongly reminiscent of traditional enterprise back-office systems from a decade ago, which directly caused the "not impressive enough" verdict; firmly rejected.
  - *Three.js 3D background*: excessive CPU/GPU usage, likely to cause jank or loud fans on low-spec demo laptops, violating NFR-02.

---

### Decision 2: Interactive Comparison Sandbox architecture design
- **Decision**: seamlessly embed a dual-core split-screen comparison sandbox on the Landing page and in the workspace. Users can click a distractor directly; the left side dynamically shows the mechanical, cold feedback of "traditional AI / ordinary question bank" (reports the answer directly, no knowledge reverse-lookup), while the right side simultaneously activates SmartStudy Compass's misconception-topology highlights, prerequisite-weakness warnings, and heuristic hints.
- **Rationale**:
  1. In undergraduate software-engineering coursework and pitch defences, the judges' biggest pain point is "how is your system different from just asking ChatGPT or using a question-search app";
  2. The interactive sandbox lets judges flip the switch themselves within 5 seconds without entering a deep practice flow, directly seeing the difference in information density and tutoring value between the two systems - highly persuasive;
  3. Data-driven pure DOM state-machine switching renders extremely lightly.
- **Alternatives considered**:
  - *Static image/text comparison table*: dull and lifeless, lacking interactivity and persuasiveness.
  - *Pre-recorded video*: not interactive; judges cannot click and test as they wish.

---

### Decision 3: DeepSeek-R1-style reasoning accordion
- **Decision**: in the Socratic companion and trap-detection diagnosis views, introduce a "🧠 Thinking Process" collapsible interaction block. It defaults to a micro-badge with pulsing glow, and when expanded reveals a structured 4-step cognitive-graph arbitration process:
  - `[01 Knowledge-graph recall]`: hits the prerequisite theorems and associated exam points;
  - `[02 Misconception-topology arbitration]`: identifies the high-frequency thinking trap the current option belongs to;
  - `[03 Anti-spoiler safety filtering]`: blocks direct dumping of the final answer;
  - `[04 Staged hint generation]`: outputs Socratic heuristic questions.
- **Rationale**:
  1. Aligns with the mainstream cutting-edge interaction standard of 2026 Reasoning Models (such as DeepSeek-R1, o3, Claude 3.7 Sonnet);
  2. Concretises the otherwise invisible backend GraphRAG reasoning logic for users and tutors with a high-tech feel, maximising academic explainability.
- **Alternatives considered**:
  - *Printing plain text directly in the chat box*: visually unstructured and lacking technological ceremony.

---

### Decision 4: Global geek HUD command palette (`Cmd+K` / `Ctrl+K`)
- **Decision**: implement a pure-native lightweight Command Palette overlay. It is summoned by a keyboard listener on `keydown (Meta+K / Ctrl+K / Escape)` and supports up/down selection and Enter confirmation. Preset commands include:
  - quick subject switching (Civil & Commercial Law / Computer Organization / Econometrics / Software Engineering);
  - quick question-number navigation;
  - jump to the exam-point graph panorama;
  - instant light/dark theme switching;
  - one-click preset identity switching.
- **Rationale**:
  1. A keyboard-first geek interaction experience that greatly improves operating efficiency;
  2. Significantly raises the professionalism and industrial-software quality of the entire interface.
- **Alternatives considered**:
  - *Relying only on top navigation clicks*: operation chains become too long for a complex multi-function system.

---

### Decision 5: Spotlight glow and micro-animation implementation mechanism
- **Decision**: use a lightweight CSS-variable injection mechanism: listen for `pointermove` events on card containers, compute `e.clientX - rect.left`, dynamically write `--mouse-x` and `--mouse-y` onto the card, and combine with CSS `radial-gradient(circle at var(--mouse-x) var(--mouse-y), rgba(99,102,241,0.18), transparent 70%)` to achieve a dynamic flowing highlight border like the Linear website.
- **Rationale**:
  1. Requires no Canvas or complex WebGL; performance overhead is extremely low (handled by the browser's native compositor);
  2. The visual quality is extremely refined, completely eliminating any "plain and crude" feel.
- **Alternatives considered**:
  - *Fixed static gradient shadows*: stiff, with no cursor-following interaction feedback.
