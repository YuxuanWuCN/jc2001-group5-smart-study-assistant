"""
Reports & Telemetry Endpoint Verification Suite (GET /api/reports/summary & /trend)
Covers Tier 1 (Functional & Schema), Tier 2 (Subject Aliasing, Boundaries & Zero-State),
and Tier 3 (CamelCase / SnakeCase Interoperability & Adversarial Resilience).
"""

import pytest
from starlette.testclient import TestClient


# -----------------------------------------------------------------------------
# Tier 1: Functional & Schema Tests
# -----------------------------------------------------------------------------

def test_report_summary_default(client: TestClient):
    """
    Tier 1: Verify GET /api/reports/summary with no query params returns 200 OK
    and conforms to the ReportSummaryResponse schema.
    """
    response = client.get("/api/reports/summary")
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    
    data = response.json()
    assert isinstance(data, dict)
    
    # Check core metrics exist and have valid types/ranges
    assert "attempt_count" in data or "attemptCount" in data
    assert "correct_count" in data or "correctCount" in data
    assert "accuracy_rate" in data or "accuracyRate" in data
    assert "cognitive_score" in data or "cognitiveScore" in data
    assert "data_source" in data or "dataSource" in data
    assert "generated_at" in data or "generatedAt" in data
    assert "weak_points" in data or "weakPoints" in data

    acc = data.get("accuracy_rate") if "accuracy_rate" in data else data.get("accuracyRate")
    assert 0.0 <= acc <= 100.0, f"Accuracy rate must be between 0 and 100: {acc}"

    # Weak points structure check
    weak_points = data.get("weak_points") or data.get("weakPoints") or []
    assert isinstance(weak_points, list)
    if len(weak_points) > 0:
        wp = weak_points[0]
        assert "topic" in wp
        assert "trap_name" in wp or "trapName" in wp
        assert "fail_count" in wp or "failCount" in wp


def test_report_trend_default(client: TestClient):
    """
    Tier 1: Verify GET /api/reports/trend with no query params returns 200 OK
    and includes 5 radar dimensions and scores.
    """
    response = client.get("/api/reports/trend")
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

    data = response.json()
    assert isinstance(data, dict)

    dims = data.get("dimensions", [])
    scores = data.get("scores", [])
    assert len(dims) == 5, f"Expected 5 radar dimensions, got {len(dims)}"
    assert len(scores) == 5, f"Expected 5 radar scores, got {len(scores)}"

    for s in scores:
        assert 0.0 <= s <= 100.0, f"Score out of range: {s}"

    traps = data.get("trap_distribution") or data.get("trapDistribution") or []
    assert isinstance(traps, list)
    assert len(traps) > 0


# -----------------------------------------------------------------------------
# Tier 2: Subject Filtering & Normalization
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("subject_code", ["law", "econ", "cs", "se"])
def test_report_summary_valid_subjects(client: TestClient, subject_code: str):
    """
    Tier 2: Verify GET /api/reports/summary filters appropriately by discipline.
    """
    response = client.get(f"/api/reports/summary?subject={subject_code}")
    assert response.status_code == 200
    data = response.json()
    assert data.get("subject") == subject_code
    assert data.get("attempt_count", 0) > 0
    assert len(data.get("weak_points", [])) > 0


@pytest.mark.parametrize("alias_pair", [
    ("economics", "econ"),
    ("civil_law", "law"),
    ("computer_science", "cs"),
    ("software_engineering", "se")
])
def test_report_summary_aliasing(client: TestClient, alias_pair: tuple):
    """
    Tier 2: Verify subject aliases map to the same canonical report metrics.
    """
    full_name, alias = alias_pair
    resp_full = client.get(f"/api/reports/summary?subject={full_name}")
    resp_alias = client.get(f"/api/reports/summary?subject={alias}")

    assert resp_full.status_code == 200
    assert resp_alias.status_code == 200

    data_full = resp_full.json()
    data_alias = resp_alias.json()

    assert data_full.get("subject") == data_alias.get("subject")
    assert data_full.get("cognitive_score") == data_alias.get("cognitive_score")


@pytest.mark.parametrize("subject_code", ["law", "econ", "cs", "se"])
def test_report_trend_valid_subjects(client: TestClient, subject_code: str):
    """
    Tier 2: Verify GET /api/reports/trend returns discipline-specific radar and trap distributions.
    """
    response = client.get(f"/api/reports/trend?subject={subject_code}")
    assert response.status_code == 200
    data = response.json()
    assert data.get("subject") == subject_code
    assert len(data.get("scores", [])) == 5
    assert len(data.get("trap_distribution", [])) > 0


# -----------------------------------------------------------------------------
# Tier 2 & 3: Boundary, Adversarial & Interoperability
# -----------------------------------------------------------------------------

def test_report_unknown_subject_zero_state(client: TestClient):
    """
    Tier 2 Boundary: Querying an unknown subject must return a clean zero-state report,
    never crashing with 500 Internal Server Error.
    """
    response = client.get("/api/reports/summary?subject=non_existent_astrology_domain")
    assert response.status_code == 200
    data = response.json()
    assert data.get("attempt_count") == 0
    assert data.get("accuracy_rate") == 0.0
    assert len(data.get("weak_points", [])) == 0


def test_report_trend_unknown_subject_neutral(client: TestClient):
    """
    Tier 2 Boundary: Querying an unknown subject trend returns neutral baseline radar scores (50.0).
    """
    response = client.get("/api/reports/trend?subject=non_existent_astrology_domain")
    assert response.status_code == 200
    data = response.json()
    scores = data.get("scores", [])
    assert all(s == 50.0 for s in scores)
    assert len(data.get("trap_distribution", [])) == 0


def test_report_camelcase_interoperability(client: TestClient):
    """
    Tier 3: Verify that responses contain both snake_case and camelCase attributes
    for seamless integration with both Python backend and JavaScript frontend.
    """
    response = client.get("/api/reports/summary")
    assert response.status_code == 200
    data = response.json()

    assert "attempt_count" in data and "attemptCount" in data
    assert "correct_count" in data and "correctCount" in data
    assert "accuracy_rate" in data and "accuracyRate" in data
    assert "cognitive_score" in data and "cognitiveScore" in data
    assert "data_source" in data and "dataSource" in data
    assert "generated_at" in data and "generatedAt" in data
    assert "weak_points" in data and "weakPoints" in data

    # Trend interoperability
    resp_trend = client.get("/api/reports/trend")
    assert resp_trend.status_code == 200
    t_data = resp_trend.json()
    assert "trap_distribution" in t_data and "trapDistribution" in t_data
    assert "data_source" in t_data and "dataSource" in t_data


@pytest.mark.parametrize("adversarial_input", [
    "",
    "   ",
    "<script>alert('xss')</script>",
    "' OR '1'='1",
    "../../etc/passwd",
    "x" * 200
])
def test_report_adversarial_resilience(client: TestClient, adversarial_input: str):
    """
    Tier 3 Adversarial: Hostile or malformed inputs must never cause unhandled 500 errors.
    """
    resp_sum = client.get("/api/reports/summary", params={"subject": adversarial_input})
    assert resp_sum.status_code != 500, f"Summary crashed on adversarial input: {adversarial_input}"

    resp_trend = client.get("/api/reports/trend", params={"subject": adversarial_input})
    assert resp_trend.status_code != 500, f"Trend crashed on adversarial input: {adversarial_input}"
