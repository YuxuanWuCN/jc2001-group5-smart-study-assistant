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
    assert lead["name"] == "Wu Yuxuan"
    assert "PM" in lead["role"] or "Project Manager" in lead["role"] or "Team Lead" in lead["role"]


def test_login_known_student_by_id():
    """Login with a valid student matriculation ID."""
    res = client.post("/api/auth/login", json={"student_id": "50106070", "password": "any"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["id"] == "50106070"
    assert data["user"]["name"] == "Wu Yuxuan"
    assert "session_token" in data
    assert data["session_token"].startswith("sess_50106070_")


def test_login_known_student_by_name():
    """Login with student full name."""
    res = client.post("/api/auth/login", json={"student_id": "Lin Yongtong"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["id"] == "50106038"
    assert data["user"]["name"] == "Lin Yongtong"


def test_login_guest_student():
    """Login as guest student."""
    res = client.post("/api/auth/login", json={"student_id": "guest"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["id"] == "guest"
    assert "Guest" in data["user"]["name"]


def test_login_new_student_dynamic_provisioning():
    """Login with an unlisted custom student name provisions a new profile."""
    res = client.post("/api/auth/login", json={"student_id": "Zhang Xiaofan"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["name"] == "Zhang Xiaofan"
    assert data["user"]["avatar"] == "Z"
    assert "session_token" in data


def test_register_new_student():
    """Register a new student with custom discipline."""
    payload = {
        "student_id": "50109999",
        "name": "Li",
        "preferred_subject": "law",
        "password": "mypassword"
    }
    res = client.post("/api/auth/register", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["id"] == "50109999"
    assert data["user"]["name"] == "Li"
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


def test_login_accepts_camel_case_alias():
    """Dual-naming contract (CamelModel): camelCase payloads map onto snake_case fields."""
    res = client.post("/api/auth/login", json={"studentId": "50106070"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["id"] == "50106070"


def test_register_accepts_camel_case_alias():
    """Registration accepts camelCase studentId/preferredSubject and still serializes snake_case."""
    res = client.post(
        "/api/auth/register",
        json={"studentId": "50999991", "name": "Alias Test", "preferredSubject": "law"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["user"]["id"] == "50999991"
    assert "preferred_subject" in data["user"]


def test_register_with_password_and_login_success():
    """Registered user with a password can authenticate with matching credentials."""
    reg_res = client.post(
        "/api/auth/register",
        json={
            "student_id": "50888001",
            "name": "Password Check Student",
            "preferred_subject": "econ",
            "password": "secret-pass-42"
        },
    )
    assert reg_res.status_code == 200

    login_res = client.post(
        "/api/auth/login",
        json={"student_id": "50888001", "password": "secret-pass-42"},
    )
    assert login_res.status_code == 200
    data = login_res.json()
    assert data["user"]["id"] == "50888001"
    assert data["user"]["name"] == "Password Check Student"
    assert data["user"]["preferred_subject"] == "econ"


def test_login_registered_user_wrong_password_returns_401():
    """Registered password-protected user fails with HTTP 401 when password is wrong or missing."""
    reg_res = client.post(
        "/api/auth/register",
        json={
            "student_id": "50888002",
            "name": "Password Reject Student",
            "preferred_subject": "law",
            "password": "correct-password"
        },
    )
    assert reg_res.status_code == 200

    wrong_res = client.post(
        "/api/auth/login",
        json={"student_id": "50888002", "password": "wrong-password"},
    )
    assert wrong_res.status_code == 401

    missing_res = client.post(
        "/api/auth/login",
        json={"student_id": "50888002"},
    )
    assert missing_res.status_code == 401
