# JC2001 SmartStudy: Learning-Progress and Troubleshooting Report Data Contract Specification (Report Data Contract)
## Milestone M2.2 Deliverable · Supporting the closed loop of the 50% Reports module

- **Prepared by**: JC2001 Group 5 (BSc BMIS)
- **Responsible Developers**: Jiang Hao (50106065, Backend Architecture), Dong Siqin (50106060, Data Model), Xi Yusai (50105989, Frontend Interaction)
- **Document Version**: v1.0 (Phase 2 Baseline)
- **Status**: **Implemented and verified by 23 Pytest automated tests (100% Pass)**

---

## 1. Contract Design Principles

To thoroughly address the problems of "looking too AI-generated" and "lacking reproducible evidence", this data contract follows three engineering principles:
1. **Honestly label data provenance (`data_source`)**: no empty boasts of "99.9% zero hallucination"; explicitly mark whether the data comes from `session_telemetry` (aggregation of local self-test practice sessions) or `seed_baseline` (baseline samples), together with an ISO 8601 generation timestamp (`generated_at`).
2. **Seamless dual serialization between frontend and backend (`CamelModel`)**: all models support both `snake_case` (Python convention) and `camelCase` (JavaScript frontend convention), preventing `KeyError` or `undefined` from being thrown due to inconsistent casing.
3. **Defensive zero-crash fallback (Zero-Crash Fallback)**: when an invalid subject is supplied or there are no practice records, the system returns a standard empty state (`attempt_count=0, accuracy_rate=0.0`) and under no circumstances throws a 500 Internal Server Error at the examiner.

---

## 2. API Contract Overview

| Endpoint | Request Method | Key Query Params | Response Model (Pydantic Schema) | Core Responsibility |
| :--- | :---: | :--- | :--- | :--- |
| `/api/reports/summary` | `GET` | `subject` (optional: `law`, `econ`, `cs`, `se`, `all`) | `ReportSummaryResponse` | Retrieve the cumulative attempt count, accuracy rate, troubleshooting trigger count, cognitive mastery score, and list of high-risk weak points |
| `/api/reports/trend` | `GET` | `subject` (optional: `law`, `econ`, `cs`, `se`, `all`) | `ReportTrendResponse` | Retrieve five-dimensional cognitive ability radar scores (Recall, Trap Defense, Synthesis, etc.) and the distribution of common traps |

---

## 3. Detailed Model Field Specifications

### 3.1 `ReportSummaryResponse` (Learning-Progress Assessment Summary)

```json
{
  "subject": "law",
  "attempt_count": 5,
  "attemptCount": 5,
  "correct_count": 4,
  "correctCount": 4,
  "accuracy_rate": 80.0,
  "accuracyRate": 80.0,
  "diagnostic_count": 1,
  "diagnosticCount": 1,
  "traps_identified": 2,
  "trapsIdentified": 2,
  "cognitive_score": 85.0,
  "cognitiveScore": 85.0,
  "streak_days": 5,
  "streakDays": 5,
  "data_source": "session_telemetry",
  "dataSource": "session_telemetry",
  "generated_at": "2026-10-16T19:44:23.000570+00:00",
  "generatedAt": "2026-10-16T19:44:23.000570+00:00",
  "weak_points": [
    {
      "topic": "Civil Code Article 152 · Exclusion period of the right of rescission",
      "trap_name": "Trap: confusing the exclusion period with interruption of the limitation period",
      "trapName": "Trap: confusing the exclusion period with interruption of the limitation period",
      "fail_count": 3,
      "failCount": 3,
      "severity": "high",
      "recommendation": "Thoroughly review the fixed-period nature of the exclusion period, and note that courts may examine the expiry of the exclusion period on their own initiative."
    }
  ]
}
```

### 3.2 `ReportTrendResponse` (Five-Dimensional Ability Radar and Error-Cause Distribution)

```json
{
  "subject": "law",
  "dimensions": [
    "Basic Recall",
    "Trap Defense",
    "Deductive Synthesis",
    "Boundary Migration",
    "Domain Breadth"
  ],
  "scores": [88.0, 75.0, 82.0, 70.0, 80.0],
  "trap_distribution": [
    {
      "trap_name": "Confusing the exclusion period with the limitation period",
      "trapName": "Confusing the exclusion period with the limitation period",
      "subject": "law",
      "count": 3
    }
  ],
  "data_source": "session_telemetry",
  "dataSource": "session_telemetry",
  "generated_at": "2026-10-16T19:44:23.009340+00:00",
  "generatedAt": "2026-10-16T19:44:23.009340+00:00"
}
```

---

## 4. Automated Testing and Engineering Verification Matrix

This contract is directly covered by the `tests/test_reports.py` automated test suite (23 tests in total, all included in the regression test network):
- `test_report_summary_default`: Verify the 200 status and basic data structure of the default summary endpoint;
- `test_report_trend_default`: Verify the integrity of the five-dimensional radar array and the score range ($0 \le score \le 100$);
- `test_report_summary_valid_subjects`: Verify multi-subject filtering (law, economics and management, computer organization, software engineering);
- `test_report_summary_aliasing`: Verify Chinese/English alias compatibility (e.g., `civil_law` is automatically mapped to `law`);
- `test_report_unknown_subject_zero_state`: Verify the friendly zero-state response for unknown parameters;
- `test_report_camelcase_interoperability`: Verify camelCase and snake_case interoperability between frontend and backend;
- `test_report_adversarial_resilience`: Verify resilience against XSS, SQLi, and long-string attacks, ensuring zero 500 crashes.

---

*JC2001 Group 5 · Software Engineering Specification and Architecture Baseline Document*
