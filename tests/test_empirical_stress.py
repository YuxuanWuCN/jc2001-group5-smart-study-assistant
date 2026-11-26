"""
Empirical Stress and Resilience Test Harness
Challenger 2 Verification Suite
"""

import re
from pathlib import Path
import pytest
from starlette.testclient import TestClient

from backend.app.main import app
from backend.app.data.seed_questions import SEED_QUESTIONS
from backend.app.models.diagnose import DiagnoseRequest, DiagnoseResponse
from backend.app.services.diagnostic_service import diagnostic_service

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


# ==============================================================================
# 1. Exhaustive DOM Element Audit & Null Guard Verification
# ==============================================================================

def test_exhaustive_dom_audit_and_null_guards():
    """
    Empirical check: Verify every document.getElementById call in app.js
    either maps to an element in index.html, is dynamically created in app.js,
    or is guarded by an `if (elem)` check so it never crashes with null pointer.
    """
    app_js_text = (FRONTEND_DIR / "app.js").read_text(encoding="utf-8")
    index_html_text = (FRONTEND_DIR / "index.html").read_text(encoding="utf-8")

    # Find all getElementById calls
    pattern = r'document\.getElementById\(["\']([^"\']+)["\']\)'
    queried_ids = set(re.findall(pattern, app_js_text))
    assert len(queried_ids) > 0, "Should have extracted DOM IDs from app.js"

    static_html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', index_html_text))
    dynamic_js_ids = set(re.findall(r'id=["\']([^"\']+)["\']', app_js_text))
    all_known_ids = static_html_ids | dynamic_js_ids

    unguarded_missing_ids = []
    for elem_id in queried_ids:
        if elem_id not in all_known_ids:
            # Check if this ID is guarded by a null check in app.js
            # E.g. const el = document.getElementById("..."); if (el) ...
            guard_pattern = rf'(?:const|let|var)\s+(\w+)\s*=\s*document\.getElementById\(["\']{re.escape(elem_id)}["\']\);'
            match = re.search(guard_pattern, app_js_text)
            if match:
                var_name = match.group(1)
                # Check if there is an `if (var_name)` guard
                if not re.search(rf'if\s*\(\s*{var_name}\s*\)', app_js_text):
                    unguarded_missing_ids.append(elem_id)
            else:
                unguarded_missing_ids.append(elem_id)

    assert not unguarded_missing_ids, (
        f"Found DOM IDs queried without null guards and missing in HTML: {unguarded_missing_ids}"
    )


# ==============================================================================
# 2. Exhaustive Option Click Simulation Across All Seed Questions
# ==============================================================================

def test_exhaustive_option_click_simulation(client: TestClient):
    """
    Simulate student selecting every single option (A, B, C, D) for all questions
    across all subjects (law, econ, cs, se). Verify that:
    1. Every option returns HTTP 200 OK
    2. Response strictly conforms to DiagnoseResponse schema
    3. The correct option is marked is_correct=True
    4. Distractor options return is_correct=False with valid trap_name and guidance
    """
    total_checks = 0
    for q in SEED_QUESTIONS:
        get_field = (lambda name, default=None, item=q: item.get(name, default)) if isinstance(q, dict) else (lambda name, default=None, item=q: getattr(item, name, default))
        qid = get_field("question_id") or get_field("id")
        qtype = get_field("question_type") or "single_choice"
        correct_answer = get_field("answer")
        options = get_field("options")

        if qtype == "fill_blank":
            blank_answers = get_field("blank_answers") or ([correct_answer] if correct_answer else [])
            assert blank_answers, f"Fill-blank question {qid} must declare at least one accepted answer"

            # Verify accepted answer passes
            total_checks += 1
            ok_res = client.post("/api/diagnose", json={"question_id": qid, "user_answer_text": blank_answers[0]})
            assert ok_res.status_code == 200, f"Failed fill-blank correct check for {qid}: {ok_res.text}"
            ok_validated = DiagnoseResponse.model_validate(ok_res.json())
            assert ok_validated.is_correct is True, f"Expected is_correct=True for fill-blank {qid}"
            assert ok_validated.socratic_guidance

            # Verify wrong answer produces structured diagnostic feedback
            total_checks += 1
            err_res = client.post(
                "/api/diagnose",
                json={"question_id": qid, "user_answer_text": "__intentionally_wrong_answer__"}
            )
            assert err_res.status_code == 200, f"Failed fill-blank wrong check for {qid}: {err_res.text}"
            err_validated = DiagnoseResponse.model_validate(err_res.json())
            assert err_validated.is_correct is False, f"Expected is_correct=False for fill-blank {qid}"
            assert err_validated.trap_name and len(err_validated.trap_name) > 0
            assert err_validated.concept_name and len(err_validated.concept_name) > 0
            assert err_validated.socratic_guidance and len(err_validated.socratic_guidance) > 0
            continue

        if hasattr(options, "keys"):
            opt_keys = options.keys()
        elif isinstance(options, list) and options:
            opt_keys = [o.key if hasattr(o, "key") else o["key"] for o in options]
        else:
            opt_keys = ["A", "B", "C", "D"]

        for opt_key in opt_keys:
            total_checks += 1
            payload = {
                "question_id": qid,
                "selected_option": opt_key
            }
            res = client.post("/api/diagnose", json=payload)
            assert res.status_code == 200, (
                f"Failed for question {qid}, option {opt_key}: {res.status_code} {res.text}"
            )
            data = res.json()

            # Pydantic validation
            validated = DiagnoseResponse.model_validate(data)

            if opt_key == correct_answer:
                assert validated.is_correct is True, f"Question {qid} option {opt_key} should be correct"
                assert validated.socratic_guidance, "Correct answer should provide positive explanation"
            else:
                assert validated.is_correct is False, f"Question {qid} option {opt_key} should be incorrect"
                assert validated.trap_name is not None and len(validated.trap_name) > 0, (
                    f"Distractor {opt_key} in {qid} must have trap_name"
                )
                assert validated.concept_name is not None and len(validated.concept_name) > 0, (
                    f"Distractor {opt_key} in {qid} must have concept_name"
                )
                assert validated.socratic_guidance is not None and len(validated.socratic_guidance) > 0, (
                    f"Distractor {opt_key} in {qid} must have Socratic guidance"
                )

    assert total_checks >= 40, f"Expected at least 40 option checks, executed {total_checks}"


# ==============================================================================
# 3. CamelCase and snake_case Interoperability for Option Click
# ==============================================================================

@pytest.mark.parametrize("payload", [
    {"question_id": "econ_1", "selected_option": "A"},
    {"questionId": "econ_1", "selectedOption": "A"},
    {"question_id": "cs_1", "selected_option": "B"},
    {"questionId": "cs_1", "selectedOption": "B"},
    {"question_id": "law_1", "selected_option": "B"},
    {"questionId": "law_1", "selectedOption": "B"},
])
def test_option_click_dual_naming_convention(client: TestClient, payload: dict):
    """Verify both camelCase and snake_case request formats work seamlessly."""
    res = client.post("/api/diagnose", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "is_correct" in data or "isCorrect" in data
    assert "fallback_mode" in data or "fallbackMode" in data


# ==============================================================================
# 4. Offline / Disconnected State Resilience
# ==============================================================================

def test_offline_fallback_zero_500_guarantee(client: TestClient):
    """
    Verify that in offline / no-API-key environment, POST /api/diagnose
    always returns HTTP 200 with fallback_mode=True and never crashes with 500.
    """
    res = client.post("/api/diagnose", json={
        "question_id": "econ_1",
        "selected_option": "A"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["fallback_mode"] is True
    assert data["is_correct"] is False
    concept_name = data["concept_name"].lower()
    assert "omitted" in concept_name or "endogen" in concept_name


def test_offline_graceful_handling_unknown_question(client: TestClient):
    """
    Verify requesting diagnosis on an unknown question ID returns a clean 404 or graceful fallback,
    never an unhandled 500 crash.
    """
    res = client.post("/api/diagnose", json={
        "question_id": "nonexistent_999",
        "selected_option": "A"
    })
    # Must not be 500 Internal Server Error
    assert res.status_code in [404, 422, 200], f"Expected graceful status code, got {res.status_code}"


def test_offline_graceful_handling_invalid_option_key(client: TestClient):
    """
    Verify requesting diagnosis on an invalid option key (e.g. 'Z') returns clean response.
    """
    res = client.post("/api/diagnose", json={
        "question_id": "econ_1",
        "selected_option": "Z"
    })
    # Should not raise 500
    assert res.status_code in [200, 400, 404, 422], f"Expected graceful status, got {res.status_code}"


# ==============================================================================
# 5. Single-Port Static Serving Integrity
# ==============================================================================

def test_single_port_static_serving(client: TestClient):
    """
    Empirically verify that single-port serving at http://127.0.0.1:8000/
    serves index.html, style.css, and app.js with exact content types and contents.
    """
    # 1. Root /
    root_res = client.get("/")
    assert root_res.status_code == 200
    assert "text/html" in root_res.headers.get("content-type", "")
    assert "<!DOCTYPE html>" in root_res.text
    # English is the shipped default; the Chinese title lives in the i18n dictionary.
    assert "SmartStudy Compass" in root_res.text
    assert 'data-i18n="portalDocumentTitle"' in root_res.text
    assert 'data-theme="dark"' in root_res.text

    # 2. /style.css
    css_res = client.get("/style.css")
    assert css_res.status_code == 200
    assert "text/css" in css_res.headers.get("content-type", "")
    assert "--bg-base" in css_res.text or "sidebar" in css_res.text

    # 3. /app.js
    js_res = client.get("/app.js")
    assert js_res.status_code == 200
    content_type = js_res.headers.get("content-type", "")
    assert ("javascript" in content_type or "text/plain" in content_type)
    assert "handleSelectOption" in js_res.text
    assert "API_BASE" in js_res.text
