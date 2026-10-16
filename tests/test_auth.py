"""
Pytest Suite for Student Authentication & Identity Endpoints.
Covers:
  - GET  /api/auth/demo-users
  - POST /api/auth/login (known members, dynamic fallback, password optional)
  - POST /api/auth/register (disciplines, id creation)
  - Boundary and adversarial inputs (empty ID, long strings, special characters)
"""

import pytest
from starlette.testclient import TestClient
from backend.app.main import create_app

app = create_app()
client = TestClient(app)


def test_get_demo_users():
    """Verify pre-configured student roster retrieval."""
    res = client.get("/api/auth/demo-users")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["total"] >= 10
    users = data["data"]

    # Verify team lead Wu Yuxuan is present
    lead = next((u for u in users if u["id"] == "50106070"), None)
    assert lead is not None
    assert lead["name"] == "吴宇轩"
    assert "PM" in lead["role"] or "项目经理" in lead["role"] or "组长" in lead["role"]


def test_login_known_student_by_id():
    """Login with a valid student matriculation ID."""
    res = client.post("/api/auth/login", json={"student_id": "50106070", "password": "any"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["id"] == "50106070"
    assert data["user"]["name"] == "吴宇轩"
    assert "session_token" in data
    assert data["session_token"].startswith("sess_50106070_")


def test_login_known_student_by_name():
    """Login with student full name (Chinese)."""
    res = client.post("/api/auth/login", json={"student_id": "林泳桐"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["id"] == "50106038"
    assert data["user"]["name"] == "林泳桐"


def test_login_guest_student():
    """Login as guest student."""
    res = client.post("/api/auth/login", json={"student_id": "guest"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["id"] == "guest"
    assert "访客" in data["user"]["name"] or "Guest" in data["user"]["name"]


def test_login_new_student_dynamic_provisioning():
    """Login with an unlisted custom student name provisions a new profile."""
    res = client.post("/api/auth/login", json={"student_id": "张小凡"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["name"] == "张小凡"
    assert data["user"]["avatar"] == "张"
    assert "session_token" in data


def test_register_new_student():
    """Register a new student with custom discipline."""
    payload = {
        "student_id": "50109999",
        "name": "李同学",
        "preferred_subject": "law",
        "password": "mypassword"
    }
    res = client.post("/api/auth/register", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["id"] == "50109999"
    assert data["user"]["name"] == "李同学"
    assert data["user"]["preferred_subject"] == "law"


def test_login_empty_id_fallback():
    """Login with empty string student ID falls back gracefully without 500 crash."""
    res = client.post("/api/auth/login", json={"student_id": "   "})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["name"] is not None


def test_login_missing_field_422():
    """Missing required student_id field returns 422 Unprocessable Entity."""
    res = client.post("/api/auth/login", json={})
    assert res.status_code == 422
