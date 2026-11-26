# Feature Specification: Smart Study Assistant Landing & Auth Portal

**Feature ID**: `001-landing-and-auth-portal`  
**Project**: JC2001 Group 5 — SmartStudy Compass (SmartStudy Assistant System)  
**Created**: 2026-10-08  
**Status**: APPROVED / READY FOR IMPLEMENTATION  

---

## 1. Business Context and Pain Points

### 1.1 Current State and Pain Points
The system currently drops users straight into the dense dark "DeepSeek Eval Harness evaluation console". This creates the following serious UX and software-engineering defects:
1. **Missing product positioning**: new users / reviewer-tutors have no context when they open the system and cannot quickly understand what the system does or what its core innovation is (misconception topology vs. conventional drill-and-practice).
2. **No identity awareness or student-record integration**: the system lacks a proper student login entry, so users cannot sign in under their real identity (e.g., team lead Yuxuan Wu, member Yongtong Lin, guest) with personalised learning-state isolation.
3. **Visual fragmentation and abruptness**: exposing cold evaluation metrics directly (such as NEO4J ONLINE, HALLUCINATION DROP) feels impersonal and unguided for an undergraduate study-assistant application.

### 1.2 Construction Goals
Build an attractive **Landing & Auth Portal** with the modern academic and technical quality of a university product, delivering:
1. **Academic-grade product landing page (Landing Hero & Highlights)**: present the project background (University of Aberdeen JC2001 Group 5 course practice), the core pain-point comparison, and four core capability modules (smart trap detection, Socratic study companion, exam-point graph, learning radar).
2. **Lightweight student-profile login and quick trial (Student Login & Fast Switch)**: support login by student ID / name, with 10 preset one-click trial accounts for core team members, plus guest access.
3. **Smooth portal-to-workspace flow**: clicking "Enter the Smart Console" transitions smoothly into the daily practice and trap-detection interface (the "everyday UI"), with the console permanently offering "Back to product intro" and "Sign out" channels.

---

## 2. User Stories and Roles

- **US-01 (as a reviewer tutor / guest)**: I want the system home page to open with a clear, elegant product positioning intro and an overview of the four modules, so I can grasp the project's core academic and engineering value within 30 seconds.
- **US-02 (as a team member / student)**: I want to one-click select my own student identity (e.g., student Wu, BMIS-50106070) or type my student ID to enter the system, so that my independent cognitive radar and learning state load.
- **US-03 (as a daily learner)**: I want to go straight from login into the console practice and trap-detection interface I am familiar with, and during practice be able to click "Back to product home" in the top navigation at any time to revisit the system introduction or demo it to others.

---

## 3. Functional Requirements

### FR-01: Welcome Home Page and Product Showcase (Hero & Showcase)
- **FR-01.1 Navbar**: shows the "SmartStudy Compass SmartStudy AI" brand logo, the JC2001 Group 5 course marker, a light/dark theme toggle, and a quick login / enter-workspace button.
- **FR-01.2 Hero Section**:
  - Main title: `An intelligent STEM study-assistant system for university students based on cognitive graphs and question-trap topology`
  - Core tags: `GraphRAG cognitive graph` · `Misconception-topology tracing` · `Socratic heuristic tutoring` · `Five-dimension ability profile`
  - Visual comparison: conventional question bank (gives only dead answers) vs. SmartStudy Compass (targets thinking blind spots and reverse-looks-up prerequisite knowledge).
- **FR-01.3 Four Core Feature Cards (Feature Showcase)**:
  1. **Smart trap-detection practice**: AI labels the traps in questions; clicking a wrong option immediately opens a deep root-cause drawer.
  2. **Socratic study companion**: guided questioning that prompts self-derivation of core theorems.
  3. **Exam-point graph panorama**: prerequisite/successor dependency topology visualisation that traces weak knowledge nodes.
  4. **Holistic learning diagnosis**: a five-dimension ability radar and defence index that precisely quantify knowledge mastery.
- **FR-01.4 Team Roster & Compliance Section**:
  - Shows University of Aberdeen JC2001 Group 5 (BSc BMIS, ten members with roles and student IDs) and supervising-tutor information.

### FR-02: Student Profile Login and Quick Identity Switching (Authentication & Identity)
- **FR-02.1 One-Click Preset Role Cards (Fast Identity Switcher)**:
  - Preset account 1: Yuxuan Wu (50106070 · PM / team lead · all-subject access)
  - Preset account 2: Yongtong Lin (50106038 · Requirements lead · Law/Economics study)
  - Preset account 3: Sijian Wang (50106045 · System architecture · CS/Software Engineering study)
  - Preset account 4: Guest student (Guest · password-free quick entry)
- **FR-02.2 Form Login & Register**:
  - Accept any student ID or name, with the password optional (defaults to 123456 in demo mode); clicking "Sign in now" creates a new student context.
- **FR-02.3 State Persistence**:
  - Login state and current user information are stored in `localStorage` (`smartstudy_user`) and survive a refresh.

### FR-03: View Transitions and Bidirectional Seamless Switching (Navigation & State Flow)
- **FR-03.1 Home Page to Workspace**:
  - Clicking "Enter the study console" or a preset identity card fades the home page out elegantly and smoothly reveals the full-screen workspace (`#app-shell`).
  - The workspace sidebar/top bar immediately syncs the logged-in student's name, student ID, and avatar.
- **FR-03.2 Workspace Back to Home**:
  - The top of the workspace sidebar permanently shows a prominent `🏠 Back to product intro` navigation item and a `🚪 Sign out` shortcut.
  - Clicking either returns smoothly to the landing page without reloading the page and without losing question data already loaded from the backend.

---

## 4. Non-Functional Requirements

- **NFR-01 (Zero External Heavy Dependencies)**: implemented in pure native HTML5/CSS3/ES6 JavaScript, without pulling in a large React/Vue framework, guaranteeing instant local opening even without a network (load time < 100ms).
- **NFR-02 (Adaptive Dual-Mode Colour)**: fully supports the existing Light and Dark modes, with typography and contrast meeting WCAG AA.
- **NFR-03 (Zero-Breakage Integration)**: the existing FastAPI backend endpoints (`/api/health`, `/api/quiz`, `/api/diagnose`) and the 114 automated tests already passing are unaffected.
- **NFR-04 (Code Conventions and Workspace Discipline)**: all new views are cohesively organised under `frontend/`; no scattered scripts in the project root.
