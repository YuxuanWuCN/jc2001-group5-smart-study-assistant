# StudyGraph High-Fidelity Design Specification

**Owner:** 50105989 (UI/UX Designer)
**Document status:** v1.0
**Aligned documents:** 02-design-system.md, RTM NFR-03, NFR-07, NFR-08

## 1. Overview
This document defines the visual implementation rules for all core pages based on the UI design system. It replaces graphical design drafts and provides front-end development with clear visual standards, fully aligned with light/dark dual theme requirements.

## 2. General Visual Rules
- Follow 8px grid system for all padding, margin and component dimensions
- Apply design system color variables uniformly, no custom color values
- Console-style aesthetic: minimal decoration, content-first, clear information hierarchy
- All status indicators use icon + text dual presentation, not colour alone (aligned with NFR-03)

## 3. Page-by-Page High-Fidelity Specification

### 3.1 Diagnostic Practice Page
1. **Question header bar**
   - Use small tag components for knowledge point, review status and source
   - Review status: "Pending" uses warning color tag; "Reviewed" uses success color tag
2. **Question content area**
   - Question stem uses body font weight regular
   - Options use card-style containers, hover state shows light primary background border highlight
3. **Operation bar**
   - "View Hint" uses secondary button style; "Submit Answer" uses primary button style
   - Buttons are right-aligned
4. **Result & explanation area**
   - Result feedback uses large icon + bold title + description, correct = success color, wrong = danger color
   - Explanation content uses secondary text color
   - Evidence source uses mono font and tertiary background block

### 3.2 Wrong Answer History Page
1. **Filter bar**
   - Search box and dropdown filters use standard input component style
   - "Clear Records" uses text button with danger color
2. **List cards**
   - Standard card component, 8px radius, 16px padding
   - Question summary uses primary text; time and tags use secondary text
   - Hover state shows subtle shadow lift
3. **Detail area**
   - Expanded below the corresponding list card, with left border indicator

### 3.3 Socratic AI Tutor Page
1. **Left context panel**
   - Standard card container, question title uses H2 style
   - Hint and evidence use folded block style
2. **Chat panel**
   - User message: right-aligned, primary color background bubble, white text
   - AI message: left-aligned, secondary background bubble, primary text
   - Mode label at bottom of AI bubble: "Local Mode" / "AI Mode", caption text size
   - Input box: standard textarea component, send button aligned right, character count at bottom right

### 3.4 Learning Analytics Page
1. **Overview cards**
   - 3 equal-width cards in one row, standard card component
   - Large bold number on top, caption label below
2. **Radar area**
   - Centered layout, dimension labels around the chart
   - Dimensions with fewer than 2 attempts show "Insufficient evidence" caption tag instead of percentage (aligned with NFR-07)

## 4. Theme Adaptation Rules
- All pages support both light and dark themes, switched via CSS variables
- Text contrast meets WCAG AA standard in both themes
- Border and background colors are replaced synchronously during theme switching, no visual breakage
