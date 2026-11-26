# Data Model Design (Phase 1: Data Model)

**Feature ID**: `001-landing-and-auth-portal`  
**Related Specification**: `specs/001-landing-and-auth-portal/spec.md`  
**Completed**: 2026-10-08  

---

## 1. Core Entities

### 1.1 Student Profile and Identity Entity (StudentProfile)
Describes the identity information of an enrolled student or team member using SmartStudy Compass.

```typescript
interface StudentProfile {
  /** Unique student ID or virtual identifier (e.g. "50106070", "50106038", "guest_01") */
  id: string;
  
  /** Student's real name or nickname (e.g. "Yuxuan Wu", "Yongtong Lin", "Guest student") */
  name: string;
  
  /** Role within the course or professional identity (e.g. "Team Lead & PM", "Lead BA", "BSc BMIS") */
  role: string;
  
  /** Avatar shorthand text (e.g. "YW", "YL", "G") */
  avatarText: string;
  
  /** Major or preferred study subject ("law" | "cs" | "econ" | "se") */
  preferredSubject: 'law' | 'cs' | 'econ' | 'se';
  
  /** Consecutive study check-in days (used for the console Streak incentive) */
  streakDays: number;
  
  /** Whether this is a preset demo account */
  isDemoAccount: boolean;
}
```

### 1.2 Session State Entity (AuthSession)
The current login session stored in the client-side `localStorage` (`smartstudy_auth_session`).

```typescript
interface AuthSession {
  /** Temporary session authentication token */
  sessionToken: string;
  
  /** Associated student profile subject */
  user: StudentProfile;
  
  /** Login timestamp (ISO 8601) */
  loginTime: string;
  
  /** Flag for remembering the login state */
  rememberMe: boolean;
}
```

### 1.3 Portal Navigation and View State (PortalViewState)
Controls the transitions and memory between the home-page product landing page and the core console.

```typescript
interface PortalViewState {
  /** Currently active root view: 'portal' (product introduction page) | 'workspace' (practice console) */
  activeRootView: 'portal' | 'workspace';
  
  /** Target tab for jumping straight to the console: 'quiz' | 'tutor' | 'graph' | 'report' */
  targetWorkspaceTab: 'quiz' | 'tutor' | 'graph' | 'report';
  
  /** Whether to skip the introduction page automatically (per user settings) */
  skipPortalOnLaunch: boolean;
}
```

---

## 2. Pre-seeded Team Demo Accounts

The system pre-seeds the following demo users with real student records from University of Aberdeen JC2001 Group 5:

| Student ID | Name | Team Role and Professional Identity | Preferred Subject | Avatar | Demo Password |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **50106070** | **Yuxuan Wu** | **Project Manager & Team Lead** | ⚖️ Civil & Commercial Law (`law`) | YW | `123456` |
| **50106038** | **Yongtong Lin** | **Lead Business Analyst (Requirements team)** | 📈 Econometrics (`econ`) | YL | `123456` |
| **50106045** | **Sijian Wang** | **System Architect (Architecture team)** | 💻 Computer Systems (`cs`) | SW | `123456` |
| **50106065** | **Jiang Hao** | **PoC Lead Developer (Development team)** | ⚙️ Software Engineering (`se`) | JH | `123456` |
| **50106034** | **Xie Weixin** | **QA & Technical Report Lead (Quality Assurance team)** | ⚖️ Civil & Commercial Law (`law`) | XW | `123456` |
| **guest** | **Guest student** | **Guest Learner (full-access quick trial)** | ⚙️ Software Engineering (`se`) | G | *(no password)* |

---

## 3. Validation and Boundary Rules

1. **Student ID format rule**: accepts an 8-digit Aberdeen standard student ID (starting with `501`) or a 2–10 character English/display name.
2. **Password compatibility**: preset accounts all use `123456`; the guest account signs in with one click and no password; self-created test accounts are not subject to strong-password validation.
3. **Sign-out and data hygiene**: signing out clears `smartstudy_auth_session` but keeps the user's practice radar progress in the local snapshot.
