# Interaction and Interface Contracts (Phase 1: Contracts)

**Feature ID**: `001-landing-and-auth-portal`  
**Related Specification**: `specs/001-landing-and-auth-portal/spec.md`  
**Completed**: 2026-10-08  

---

## 1. Frontend View Lifecycle Contract

### 1.1 Root Container Switching: `switchRootView(targetView, options)`
Responsible for seamless switching between the "product introduction portal (`#portal-landing`)" and the "regular study console (`#app-shell`)".

```typescript
type RootView = 'portal' | 'workspace';

interface SwitchViewOptions {
  /** Target sub-view to activate when switching to the console (defaults to 'quiz') */
  targetTab?: 'quiz' | 'tutor' | 'graph' | 'report';
  
  /** Student login profile that accompanies the switch (when triggered directly by a card) */
  userProfile?: StudentProfile;
  
  /** Whether to update the URL hash (e.g. #portal, #workspace) */
  updateHash?: boolean;
}

function switchRootView(targetView: RootView, options?: SwitchViewOptions): void;
```

**Behaviour specification and constraints**:
1. If `targetView === 'workspace'`:
   - Add the `.view-hidden` class to the `#portal-landing` node (150ms fade-out animation), then set `display: none`.
   - Remove the `hidden` attribute from the `#app-shell` node and set `display: flex`.
   - Trigger an ECharts chart resize (`window.dispatchEvent(new Event('resize'))`) so the console radar chart renders at the exact size.
2. If `targetView === 'portal'`:
   - Set `display: none` on the `#app-shell` node.
   - Set `display: block` on the `#portal-landing` node and fade it in smoothly.

---

### 1.2 Student Identity Authentication Contract: `loginStudent(identifier, password, options)`

```typescript
interface LoginResult {
  success: boolean;
  message: string;
  user?: StudentProfile;
  sessionToken?: string;
}

function loginStudent(
  identifier: string, 
  password?: string, 
  remember: boolean = true
): LoginResult;
```

**Response codes and logic rules**:
- If the input matches a preset member ID (e.g. `50106070`, `Yuxuan Wu`): automatically load the team-lead profile and its 5-day check-in streak, and return `success: true`.
- If the input is any other name/student ID (e.g. a new student): automatically create a temporary student profile (using the first character as the avatar) and return `success: true`.
- If login succeeds: automatically sync the left sidebar entries `#current-user-name`, `#current-user-role`, `#current-user-avatar`.

---

## 2. Draft Backend OpenAPI Contract (Optional Backend Endpoints)

When student records need to be persisted to the backend service, the FastAPI backend will expose the following compatible endpoints:

### 2.1 `GET /api/auth/demo-users`
Return the list of preset team members for the frontend cards to render.

```json
{
  "status": "ok",
  "data": [
    {
      "id": "50106070",
      "name": "Yuxuan Wu",
      "role": "Project Manager & Team Lead",
      "preferred_subject": "law",
      "avatar": "YW"
    },
    {
      "id": "50106038",
      "name": "Yongtong Lin",
      "role": "Lead Business Analyst",
      "preferred_subject": "econ",
      "avatar": "YL"
    }
  ]
}
```

### 2.2 `POST /api/auth/login`
Validate the student ID and issue a session identifier.

**Request Body**:
```json
{
  "student_id": "50106070",
  "password": "optional_password"
}
```

**Response 200 OK**:
```json
{
  "status": "ok",
  "session_token": "sess_50106070_20261008",
  "user": {
    "id": "50106070",
    "name": "Yuxuan Wu",
    "role": "Project Manager & Team Lead",
    "preferred_subject": "law",
    "avatar": "YW",
    "streak_days": 5
  }
}
```
