# StudyGraph UI/UX Design Documents

**Course & Group:** JC2001 / Group 5  
**Project:** Smart Study Assistant System (智学罗盘)  
**Owner:** 50105989 (UI/UX Designer)  
**Document status:** Initial version, design framework in progress  
**Aligned documents:** Personal RTM (50106035), Use Case Specifications UC-05 ~ UC-08

---

## 1. Design Overview

This directory contains all UI/UX design deliverables for the StudyGraph system. The design follows a **console-style developer-tool aesthetic** for university STEM students and exam learners, prioritising efficiency, clarity and traceability of learning evidence.

Core design objectives:
- Deliver a consistent left-sidebar console layout across all pages
- Support both light and dark themes (aligned with NFR-03)
- Implement full state design: default, loading, empty, error and fallback states
- Ensure all functional requirements are mapped to visible UI modules
- Follow 8px grid system for spacing and layout standardisation

---

## 2. Requirements Alignment

All interface designs are strictly derived from the group requirements traceability matrix and use case specifications. No out-of-scope features are added without requirement approval.

### Aligned Use Cases
| Use Case ID | Use Case Name | Corresponding Page | Priority |
| :---: | :--- | :--- | :---: |
| UC-05 | Five-dimension learning radar analysis | Practice page + Learning analytics page | Must Have (core flow) / Should Have (radar) |
| UC-06 | Wrong-answer history & retry | History page | Must Have |
| UC-07 | Adaptive supplementary question recommendation | Result section (embedded) | Could Have |
| UC-08 | Socratic AI tutor follow-up | AI Tutor page | Must Have |

### Aligned Non-Functional Requirements
- **NFR-02**: External service failure fallback states (error prompt + retry button)
- **NFR-03**: Light/dark theme support; status indicated by icon + text, not colour alone
- **NFR-04**: Delete confirmation dialog; answers hidden by default
- **NFR-07**: Clear "Insufficient evidence" label; recommendation reason visible; attempt count shown
- **NFR-08**: Desktop-first layout with basic responsive adaption

---

## 3. Document Structure

> Files will be added sequentially as design phases progress.

---

## 4. Core Design Principles

1.  **Requirement-Driven**
    Every UI module corresponds to at least one functional requirement. No decorative elements that affect functional clarity are added.

2.  **8px Grid System**
    All padding, margin and component dimensions follow the 8px grid rule to ensure layout consistency and front-end implementability.

3.  **Accessibility First**
    All status feedback uses icon + text dual expression; text contrast meets WCAG standard; interactive controls have clear hover and active states.

4.  **Console-Style Aesthetic**
    Left fixed navigation + top status bar + main content area; monospaced fonts are used for data and code content to maintain a professional tool-style atmosphere.

5.  **State Completeness**
    Each page covers five states: default, loading, empty, error and success, to guide front-end exception handling implementation.

---

## 5. Design Assets

- **Figma source file (editable):** *Link to be added after phase 1 completion*
- **Component library:** Built-in Figma design system aligned with CSS variables

---

## 6. Version History

| Version | Date | Description | Owner |
| :---: | :--- | :--- | :---: |
| v0.1 | 2026-10-28 | Initial document structure & requirements alignment | 50105989 |
