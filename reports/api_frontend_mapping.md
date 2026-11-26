# Frontend-Backend API Field Mapping Reference

## Notes
Cross-check the request parameters initiated by the frontend and the response fields it expects to receive against the existing `frontend/app.js` and `frontend/index.html`, to prevent errors during subsequent integration testing.

## Implemented API List
| View/Module | Frontend Trigger Action | Backend URL Called | Request Method | Key Request Fields (Request Body) | Expected Response Fields |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **Global Initialization** | Preload the full question bank at application startup | `/api/questions` | `GET` | None | `[{id, stem, options, subject}]` array of question objects |
| **Global Initialization** | Preload knowledge-point dataset resources at application startup | `/api/datasets` | `GET` | None | `[{id, name, concept_list, subject}]` array of knowledge points/datasets |
| **Global Initialization** | Probe service health and run mode at application startup | `/api/health` | `GET` | None | `{ mode: "online" \| "local" }` service run-mode identifier |
| **Targeted Practice** | Submit the selected answer and obtain grading and explanation | `/api/answer` | `POST` | `{question_id, selected}` | `{correct_key, correct, dimensions, misconception, explanation}` answer result and explanation |
| **Tutor Dialogue** | Send a question to the tutor and obtain a reply | `/api/tutor` | `POST` | `{question_id, message}` | `{reply, mode}` tutor reply content and source mode |
