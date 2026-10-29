# StudyGraph Interaction Specification

**Owner:** 50105989 (UI/UX Designer)
**Document status:** v1.0
**Aligned documents:** Use Cases UC-05 ~ UC-08, RTM FR-09, FR-10, NFR-02, NFR-04

## 1. Overview
This document defines the interaction rules, state transitions and exception handling logic for all core pages, strictly corresponding to the main success scenarios and exception branches in the use case specifications.

## 2. Global Interaction Rules
1. **Sidebar navigation**: click to switch pages; current page item stays highlighted active state
2. **Theme toggle**: click the button in top bar to switch between light/dark themes; preference takes effect immediately and applies globally
3. **General button states**: all buttons have default / hover / disabled three states
4. **Delete / clear action**: all destructive operations require a secondary confirmation dialog; cancel retains data, confirm executes operation (aligned with NFR-04)

## 3. Page Interaction Details

### 3.1 Diagnostic Practice Page (UC-05)
**Main flow:**
1. Page loads with question content, explanation area hidden by default
2. User clicks "View Hint": hint content expands, **no attempt record is created** (aligned with FR-09)
3. User selects option and clicks "Submit Answer":
   - Show loading state briefly
   - Display result feedback and full explanation
   - Save attempt record automatically (aligned with FR-10)
   - Evidence source and review status are displayed synchronously

**Exception branches:**
- Question loading failure: show error prompt + "Retry" button
- Insufficient attempts for dimension: label "Insufficient evidence" in analytics section

### 3.2 Wrong Answer History Page (UC-06)
**Main flow:**
1. Page loads and displays records sorted by time (newest first)
2. User enters keyword or selects filters: list updates in real time, shows matching count
3. User clicks a record: detail area expands below
4. User clicks "Retry Question": hides original answer, enters practice flow; new record is created without overwriting original (aligned with FR-07)
5. User clicks "Clear Records": pops up confirmation dialog; confirm clears all records, cancel closes dialog (aligned with FR-10)

**Exception branches:**
- No records exist: show empty state illustration + shortcut button to practice page
- No matching records after filter: show "No matching records" prompt + reset filter button
- Original question unavailable: mark record as unavailable, disable retry button

### 3.3 Socratic AI Tutor Page (UC-08)
**Main flow:**
1. Left panel loads current question context
2. User enters question (within 1200 characters) and clicks send:
   - User message appears in chat flow
   - Show loading state for AI response
   - AI returns 2-3 sentence guided response with thinking prompt, no direct answer (aligned with FR-05)
   - Response mode label is displayed

**Exception branches:**
- Input empty or over 1200 characters: prompt user to edit, do not submit
- External model unavailable: automatically fall back to local prompt response, mark as "Local Mode" (aligned with NFR-02)
- Local service also unavailable: show error message + retry button
- User asks for answer directly: AI returns guiding question or counterexample instead of direct answer

### 3.4 Learning Analytics Page (UC-05)
**Main flow:**
1. Page reads local attempt records
2. Calculates accuracy per dimension and renders radar chart
3. Dimensions with < 2 attempts show "Insufficient evidence" label instead of percentage (aligned with FR-04)

**Exception branches:**
- No attempt records: show empty state + guide to practice
- Record reading failure: show error message, do not display 0% result

## 4. State Transition Rules
- All loading states use skeleton screen or spinner, no unresponsive blank interface
- All error states provide clear text description and operable retry / fallback entry
- All empty states provide clear guidance and shortcut operation entry
