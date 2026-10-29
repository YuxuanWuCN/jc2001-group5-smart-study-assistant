# StudyGraph UI Restoration Acceptance Checklist

**Owner:** 50105989 (UI/UX Designer)
**Document status:** v1.0
**Aligned documents:** 02-design-system.md, 03-high-fidelity.md, 04-interaction-spec.md

## 1. Overview
This checklist is used for front-end development acceptance to verify whether the implementation conforms to design specifications and requirement standards. All items are checked one by one, and passed items are marked as ✓.

## 2. Acceptance Checklist

### 2.1 Global Design System
| Item | Status | Note |
| :--- | :---: | :--- |
| All color values use CSS variables defined in design system | ☐ | |
| Light and dark themes switch normally without style breakage | ☐ | Aligned with NFR-03 |
| All spacing follows 8px grid rule | ☐ | |
| Font hierarchy matches design specification | ☐ | |
| All statuses use icon + text dual indication, not colour only | ☐ | Aligned with NFR-03 |

### 2.2 Layout & Navigation
| Item | Status | Note |
| :--- | :---: | :--- |
| Global console layout: left sidebar + top bar + main content | ☐ | |
| Sidebar width 240px fixed, top bar height 56px fixed | ☐ | |
| Sidebar navigation switches pages correctly, active state highlighted | ☐ | |
| Theme toggle button works normally | ☐ | |

### 2.3 Diagnostic Practice Page
| Item | Status | Note |
| :--- | :---: | :--- |
| Question header shows knowledge point, review status, evidence source | ☐ | Aligned with FR-08 |
| Viewing hint does not create an attempt record | ☐ | Aligned with FR-09 |
| Full explanation only shown after user submission | ☐ | Aligned with FR-09 |
| Submission saves record correctly | ☐ | Aligned with FR-10 |
| Answer hidden by default before submission | ☐ | Aligned with NFR-04 |

### 2.4 Wrong Answer History Page
| Item | Status | Note |
| :--- | :---: | :--- |
| Keyword search and multi-dimensional filters work normally | ☐ | Aligned with FR-07 |
| Records sorted by time in reverse order | ☐ | |
| Retry creates new record, does not overwrite original | ☐ | Aligned with FR-07 |
| Clearing records requires secondary confirmation | ☐ | Aligned with NFR-04 |
| Empty state and no-match state display correctly | ☐ | |

### 2.5 Socratic AI Tutor Page
| Item | Status | Note |
| :--- | :---: | :--- |
| Left panel shows question context and evidence | ☐ | |
| AI response is guided, no direct answer | ☐ | Aligned with FR-05 |
| Response mode label is displayed | ☐ | |
| Input length limit (1200 chars) works | ☐ | |
| External model failure falls back to local mode | ☐ | Aligned with NFR-02 |

### 2.6 Learning Analytics Page
| Item | Status | Note |
| :--- | :---: | :--- |
| Five-dimension radar renders correctly | ☐ | Aligned with FR-04 |
| Dimensions with < 2 attempts show "Insufficient evidence" | ☐ | Aligned with FR-04, NFR-07 |
| Attempt count is displayed for each dimension | ☐ | Aligned with NFR-07 |
| Empty state displays correctly when no records | ☐ | |

### 2.7 Exception & States
| Item | Status | Note |
| :--- | :---: | :--- |
| Loading state is displayed during data request | ☐ | |
| Error state shows clear message and retry button | ☐ | |
| All destructive operations have secondary confirmation | ☐ | |
