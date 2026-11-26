# Quickstart and Acceptance Verification Guide (Phase 1: Quickstart)

**Feature ID**: `001-landing-and-auth-portal`  
**Related Specification**: `specs/001-landing-and-auth-portal/spec.md`  
**Completed**: 2026-10-08  

---

## 1. Starting the Service Locally

Start the FastAPI local development server from the project root:

```bash
# Option A: start directly through the Python module
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload

# Option B: run the root-level launcher script
python backend/run.py
```

Once the service is running, open the following in a browser:  
👉 **`http://127.0.0.1:8000/`**

---

## 2. Acceptance Verification Checklist

### Test Point 1: Welcome and Product Introduction Home Page (Landing Hero)
1. Open `http://127.0.0.1:8000/`; the page **first presents** the polished product introduction portal (rather than the cold console).
2. Verify the top navigation bar:
   - Brand identity: SmartStudy Compass SmartStudy AI · JC2001 Group 5
   - Quick actions: the light/dark theme toggle flips correctly and the direct-to-console button works.
3. Verify the four core feature cards:
   - [01] Smart trap-detection practice
   - [02] Socratic study companion
   - [03] Exam-point graph panorama
   - [04] Holistic learning diagnosis
4. Verify that the University of Aberdeen course information and the 10-member team roster are displayed in full at the bottom.

### Test Point 2: One-Click Student Profile Switching and Login (Fast Login)
1. In the "quick trial channel" on the home page, click the **[Yuxuan Wu · Team Lead / PM]** card:
   - The system switches identity instantly and transitions elegantly into the study console!
   - The console left sidebar shows `Yuxuan Wu` / `BMIS-50106070`, with the avatar `YW`.
2. Try quick sign-in with the "Guest student" account; it should be equally smooth.

### Test Point 3: Seamless Bidirectional Switching Between Console and Home Page (Roundtrip Navigation)
1. After entering the study console, find the **`🏠 Back to product home`** button at the top of the left sidebar.
2. Click it to return smoothly to the product introduction portal, **without losing the current question and option states**.
3. Click "Enter console" again to restore the existing practice progress seamlessly.
4. Click **`🚪 Sign out of the current student account`** in the bottom-left corner; the session is reset and the page returns to the portal.

---

## 3. Automated Test Regression Verification

Run all existing quality-assurance regression tests and confirm 100% pass:

```bash
pytest tests/ -v
python scripts/verify_poc.py
```
