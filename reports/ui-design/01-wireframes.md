# StudyGraph Low-Fidelity Wireframes Specification

**Owner:** 50105989 (UI/UX Designer)
**Document status:** v1.0
**Aligned documents:** RTM (FR-04 ~ FR-10, NFR-02 ~ NFR-08), Use Cases UC-05 ~ UC-08

## 1. Overview
This document defines the low-fidelity wireframe structure of all core pages. Wireframes focus on information architecture, module distribution and navigation logic, without visual styling details. All modules strictly correspond to functional requirements, no out-of-scope features are included.

## 2. Global Layout Framework
All pages follow a unified console-style layout with three fixed areas:

| Area | Position | Core Function |
| :--- | :--- | :--- |
| Sidebar | Left, 240px fixed width | Project logo, 4 primary navigation entries, bottom status info |
| Top Status Bar | Top, 56px fixed height | Current page title, theme toggle button |
| Main Content Area | Right, adaptive width | All page business modules |

Navigation entries in sidebar:
1. Diagnostic Practice (corresponds to UC-05)
2. Wrong Answer History (corresponds to UC-06)
3. Socratic AI Tutor (corresponds to UC-08)
4. Learning Analytics (corresponds to UC-05)

## 3. Page-by-Page Wireframe Breakdown

### 3.1 Diagnostic Practice Page (UC-05)
**Aligned requirements:** FR-08, FR-09, FR-10, NFR-04, NFR-07

Modules arranged from top to bottom:
1. Question header bar: knowledge point tag, review status tag, evidence source label
2. Question content area: question stem, option list
3. Operation bar: "View Hint" secondary button, "Submit Answer" primary button
4. Collapsible explanation area (shown after submission): result feedback, diagnosis explanation, evidence basis, operation entry for retry and similar practice

### 3.2 Wrong Answer History Page (UC-06)
**Aligned requirements:** FR-07, FR-10, NFR-04

Modules arranged from top to bottom:
1. Filter bar: keyword search box, multi-dimensional filters (subject, topic, misconception, result, date range), "Clear Records" button
2. Wrong answer list: list cards sorted by time in reverse order, each card contains question summary, attempt time, subject tag, misconception tag
3. Record detail area (expanded on click): original question, user's answer, diagnosis result, "Retry Question" button

### 3.3 Socratic AI Tutor Page (UC-08)
**Aligned requirements:** FR-05, FR-08, NFR-02

Left-right two-column layout:
1. Left context panel (30% width): current question content, hint, evidence source info
2. Right chat panel (70% width): message flow area, bottom input box with send button, character count prompt

### 3.4 Learning Analytics Page (UC-05)
**Aligned requirements:** FR-04, NFR-07

Modules arranged from top to bottom:
1. Data overview card row: 3 side-by-side cards for total attempts, overall accuracy, mastered dimensions
2. Five-dimension radar area: radar chart visualization, each dimension marked with accuracy and attempt count
3. Quick action area: "Practice Weak Points" button, "View Wrong Answers" button

## 4. Page Navigation Flow
- Sidebar navigation allows direct switching between all four primary pages
- Clicking "Retry" on practice page enters practice flow without leaving current page
- Clicking "View Wrong Answers" on analytics page jumps to Wrong Answer History page
- Clicking "Practice Similar" on result area enters recommended question practice flow
