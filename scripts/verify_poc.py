#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 Smart Study Assistant System (智学罗盘) PoC MVP - Standalone Quality Gate & Verification Runner
Course: JC2001 Introduction to Software Engineering (2026–27)
Group:  Group 5 (BSc BMIS, 10 members, Leader: 吴宇轩 50106070)
Target: scripts/verify_poc.py

This script performs comprehensive end-to-end verification across:
  Check 1: Required Project Files & Assets Integrity
  Check 2: Dependency Specification & Package Imports
  Check 3: Pydantic v2 Domain Models & Dual-Mode Schemas
  Check 4: Health Probe Contract (GET /api/health)
  Check 5: Quiz Endpoint & Subject Aliasing (GET /api/quiz)
  Check 6: Diagnostic Engine & Socratic Trap Attribution (POST /api/diagnose)
  Check 7: Resilient Offline Fallback (Zero 500 Exceptions)
  Check 8: CORS Middleware Headers & Preflight Handshake
  Check 9: Frontend Static Mount & DOM Contract Integrity
  Check 10: Automated Pytest Test Suite Execution (pytest tests/)
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging

# Filter deprecation warnings
warnings.filterwarnings("ignore")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("smartstudy_api").setLevel(logging.WARNING)

# Windows console UTF-8 safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ==============================================================================
# Data Structures
# ==============================================================================

@dataclass
class CheckResult:
    check_id: int
    name: str
    passed: bool
    details: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


# ==============================================================================
# Quality Gate Checks
# ==============================================================================

def check_1_files_presence() -> CheckResult:
    """Check 1: Verify presence of all required PoC deliverables and source files."""
    required_files = [
        "requirements.txt",
        "frontend/index.html",
        "frontend/style.css",
        "frontend/app.js",
        "backend/app/__init__.py",
        "backend/app/main.py",
        "backend/app/models/quiz.py",
        "backend/app/models/diagnose.py",
        "tests/conftest.py",
        "tests/test_health.py",
        "tests/test_quiz.py",
        "tests/test_diagnose.py",
        "tests/test_cors.py",
        "tests/test_e2e_frontend.py",
        "scripts/verify_poc.py",
    ]
    details = []
    errors = []

    for rel_path in required_files:
        p = PROJECT_ROOT / rel_path
        if not p.exists():
            errors.append(f"Missing required file: {rel_path}")
        elif p.stat().st_size == 0:
            errors.append(f"File exists but is empty: {rel_path}")
        else:
            details.append(f"Verified {rel_path} ({p.stat().st_size} bytes)")

    return CheckResult(
        check_id=1,
        name="Deliverable Files & Asset Presence",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_2_dependencies_import() -> CheckResult:
    """Check 2: Verify required dependencies import cleanly."""
    required_modules = [
        ("fastapi", "FastAPI web framework"),
        ("uvicorn", "ASGI server engine"),
        ("pydantic", "Pydantic v2 data models"),
        ("pytest", "Pytest test framework"),
        ("requests", "HTTP client library"),
        ("dotenv", "python-dotenv environment loader"),
        ("starlette", "Starlette underlying toolkit"),
    ]
    details = []
    errors = []

    for mod_name, desc in required_modules:
        try:
            __import__(mod_name)
            details.append(f"Module '{mod_name}' successfully loaded ({desc})")
        except ImportError as e:
            errors.append(f"Failed to import '{mod_name}': {e}")

    return CheckResult(
        check_id=2,
        name="Dependency Specification & Package Imports",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_3_pydantic_schemas() -> CheckResult:
    """Check 3: Verify Pydantic v2 models and dual camelCase/snake_case serialization."""
    details = []
    errors = []

    try:
        from backend.app.models.common import HealthResponse
        from backend.app.models.quiz import QuizItem, OptionItem, TrapDetail
        from backend.app.models.diagnose import DiagnoseRequest, DiagnoseResponse

        # Test HealthResponse
        hr = HealthResponse(status="ok")
        assert hr.status == "ok"
        details.append("HealthResponse initialized and verified")

        # Test QuizItem bidirectional serialization
        item = QuizItem(
            id="test_1",
            subject="econ",
            stem="Sample Stem?",
            options={"A": "Alpha", "B": "Beta"},
            answer="B",
            trap_hint="Trap sample"
        )
        assert item.id == "test_1"
        assert item.question_id == "test_1"
        assert len(item.options) == 2
        details.append("QuizItem schema normalization verified")

        # Test DiagnoseRequest
        req = DiagnoseRequest(questionId="test_1", selectedKey="A")
        assert req.question_id == "test_1"
        assert req.selected_option == "A"
        details.append("DiagnoseRequest camelCase interoperability verified")

        # Test DiagnoseResponse
        resp = DiagnoseResponse(
            is_correct=False,
            question_id="test_1",
            selected_key="A",
            correct_key="B",
            trap_name="Sample Trap",
            concept_name="Sample Concept",
            socratic_guidance="Consider why...",
            fallback_mode=True
        )
        assert resp.isCorrect is False
        assert resp.trapTitle == "Sample Trap"
        assert resp.fallbackMode is True
        details.append("DiagnoseResponse bidirectional fields verified")

    except Exception as e:
        errors.append(f"Pydantic schema verification failed: {e}")

    return CheckResult(
        check_id=3,
        name="Pydantic v2 Models & Schema Contracts",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def _get_test_client():
    from starlette.testclient import TestClient
    from backend.app.main import app
    return TestClient(app, raise_server_exceptions=False)


def check_4_health_probe() -> CheckResult:
    """Check 4: Test in-memory GET /api/health endpoint."""
    details = []
    errors = []

    try:
        client = _get_test_client()
        resp = client.get("/api/health")
        if resp.status_code != 200:
            errors.append(f"GET /api/health returned HTTP {resp.status_code}: {resp.text}")
        else:
            data = resp.json()
            if data.get("status") != "ok":
                errors.append(f"Expected status='ok', got '{data.get('status')}'")
            else:
                details.append(f"GET /api/health -> 200 OK, payload: {data}")
    except Exception as e:
        errors.append(f"Health probe invocation raised exception: {e}")

    return CheckResult(
        check_id=4,
        name="Health Probe Contract (GET /api/health)",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_5_quiz_endpoint() -> CheckResult:
    """Check 5: Test GET /api/quiz and subject aliasing."""
    details = []
    errors = []

    try:
        client = _get_test_client()

        # Test subjects
        for sub in ["economics", "econ", "cs", "law", "se"]:
            resp = client.get(f"/api/quiz?subject={sub}")
            if resp.status_code != 200:
                errors.append(f"GET /api/quiz?subject={sub} returned HTTP {resp.status_code}")
            else:
                qs = resp.json()
                if not isinstance(qs, list) or len(qs) == 0:
                    errors.append(f"Subject '{sub}' returned empty or non-list questions")
                else:
                    details.append(f"Subject '{sub}': returned {len(qs)} questions conforming to schema")

        # Test aliasing consistency: economics vs econ
        r_full = client.get("/api/quiz?subject=economics").json()
        r_alias = client.get("/api/quiz?subject=econ").json()
        ids_full = [q.get("id") or q.get("question_id") for q in r_full]
        ids_alias = [q.get("id") or q.get("question_id") for q in r_alias]
        if ids_full != ids_alias:
            errors.append(f"Aliasing mismatch between 'economics' and 'econ': {ids_full} vs {ids_alias}")
        else:
            details.append(f"Aliasing verified: 'economics' <-> 'econ' returned identical IDs: {ids_full}")

    except Exception as e:
        errors.append(f"Quiz endpoint test raised exception: {e}")

    return CheckResult(
        check_id=5,
        name="Quiz Retrieval & Subject Aliasing (GET /api/quiz)",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_6_diagnose_engine() -> CheckResult:
    """Check 6: Test POST /api/diagnose option evaluation and Socratic trap attribution."""
    details = []
    errors = []

    try:
        client = _get_test_client()

        # Wrong option for econ_1
        payload_wrong = {"question_id": "econ_1", "selected_option": "A"}
        resp_wrong = client.post("/api/diagnose", json=payload_wrong)
        if resp_wrong.status_code != 200:
            errors.append(f"POST /api/diagnose (distractor) returned HTTP {resp_wrong.status_code}: {resp_wrong.text}")
        else:
            d = resp_wrong.json()
            is_correct = d.get("is_correct") if "is_correct" in d else d.get("isCorrect")
            if is_correct is not False:
                errors.append(f"Expected is_correct=False for distractor A, got {is_correct}")
            trap_title = d.get("trap_name") or d.get("trap_title") or d.get("trapTitle")
            if not trap_title:
                errors.append("Misconception trap title missing in diagnosis response")
            socratic = d.get("socratic_guidance") or d.get("socratic_hint") or d.get("socraticGuidance")
            if not socratic:
                errors.append("Socratic guidance missing in diagnosis response")
            details.append(f"Distractor diagnosis: is_correct=False, trap='{trap_title}', guidance='{str(socratic)[:50]}...'")

        # Correct option for econ_1 (C is true BLUE OLS condition)
        payload_correct = {"question_id": "econ_1", "selected_option": "C"}
        resp_correct = client.post("/api/diagnose", json=payload_correct)
        if resp_correct.status_code != 200:
            errors.append(f"POST /api/diagnose (correct) returned HTTP {resp_correct.status_code}")
        else:
            d_corr = resp_correct.json()
            is_corr = d_corr.get("is_correct") if "is_correct" in d_corr else d_corr.get("isCorrect")
            if is_corr is not True:
                errors.append(f"Expected is_correct=True for correct option C, got {is_corr}")
            else:
                details.append("Correct option diagnosis: is_correct=True verified")

    except Exception as e:
        errors.append(f"Diagnose engine check raised exception: {e}")

    return CheckResult(
        check_id=6,
        name="Socratic Diagnostic Engine (POST /api/diagnose)",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_7_resilient_fallback() -> CheckResult:
    """Check 7: Test offline fallback and zero 500 error guarantee."""
    details = []
    errors = []

    try:
        # Clear LLM API keys
        old_dashscope = os.environ.pop("DASHSCOPE_API_KEY", None)
        old_qwen = os.environ.pop("QWEN_API_KEY", None)

        client = _get_test_client()
        resp = client.post("/api/diagnose", json={"question_id": "econ_1", "selected_option": "A"})

        if resp.status_code != 200:
            errors.append(f"Offline diagnosis crashed with HTTP {resp.status_code}: {resp.text}")
        else:
            d = resp.json()
            fallback_flag = d.get("fallback_mode") if "fallback_mode" in d else d.get("fallbackMode")
            if fallback_flag is not True:
                errors.append(f"Expected fallback_mode=True when API key is missing, got {fallback_flag}")
            else:
                details.append("Offline fallback mode correctly engaged (fallback_mode=True, HTTP 200 OK)")

        # Restore env
        if old_dashscope:
            os.environ["DASHSCOPE_API_KEY"] = old_dashscope
        if old_qwen:
            os.environ["QWEN_API_KEY"] = old_qwen

    except Exception as e:
        errors.append(f"Offline fallback check raised exception: {e}")

    return CheckResult(
        check_id=7,
        name="Resilient Offline Fallback & Zero 500 Guarantee",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_8_cors_headers() -> CheckResult:
    """Check 8: Test CORS middleware headers for local development origins."""
    details = []
    errors = []

    try:
        client = _get_test_client()

        # Preflight OPTIONS
        headers = {
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type",
        }
        resp_options = client.options("/api/diagnose", headers=headers)
        if resp_options.status_code not in [200, 204]:
            errors.append(f"Preflight OPTIONS returned HTTP {resp_options.status_code}")
        else:
            allow_origin = resp_options.headers.get("access-control-allow-origin")
            if not allow_origin or allow_origin not in ["*", "http://localhost:3000"]:
                errors.append(f"Invalid Access-Control-Allow-Origin: {allow_origin}")
            else:
                details.append(f"Preflight OPTIONS passed with Access-Control-Allow-Origin='{allow_origin}'")

        # GET request with null origin (file:// simulation)
        resp_get = client.get("/api/health", headers={"Origin": "null"})
        allow_origin_get = resp_get.headers.get("access-control-allow-origin")
        if not allow_origin_get:
            errors.append("Missing Access-Control-Allow-Origin for GET request from origin 'null'")
        else:
            details.append(f"GET with Origin='null' passed (Allow-Origin: {allow_origin_get})")

    except Exception as e:
        errors.append(f"CORS verification raised exception: {e}")

    return CheckResult(
        check_id=8,
        name="CORS Middleware Headers & Preflight Handshake",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_9_frontend_mount() -> CheckResult:
    """Check 9: Test static frontend mount and DOM contract element integrity."""
    details = []
    errors = []

    try:
        client = _get_test_client()

        # Root static HTML serving
        resp_root = client.get("/")
        if resp_root.status_code != 200:
            errors.append(f"Root static route '/' returned HTTP {resp_root.status_code}")
        elif "智学罗盘" not in resp_root.text:
            errors.append("Root HTML response does not contain '智学罗盘'")
        else:
            details.append("Root route '/' successfully serves DeepSeek console HTML")

        # DOM Elements Integrity
        index_html = (PROJECT_ROOT / "frontend" / "index.html").read_text(encoding="utf-8")
        essential_ids = [
            "options-container",
            "diagnostic-drawer",
            "q-stem",
            "theme-toggle-btn",
            "next-q-btn",
            "chat-msgs-container",
            "large-graph-svg",
            "mini-radar-chart",
        ]
        missing_ids = [eid for eid in essential_ids if f'id="{eid}"' not in index_html]
        if missing_ids:
            errors.append(f"Missing essential DOM element IDs in index.html: {missing_ids}")
        else:
            details.append(f"All {len(essential_ids)} critical DOM element IDs verified in index.html")

    except Exception as e:
        errors.append(f"Frontend static mount check raised exception: {e}")

    return CheckResult(
        check_id=9,
        name="Frontend Static Mount & DOM Contract Integrity",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


def check_10_pytest_suite() -> CheckResult:
    """Check 10: Run the full automated pytest suite via subprocess."""
    details = []
    errors = []

    cmd = [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"]
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=60
        )
        if proc.returncode != 0:
            errors.append(f"pytest exited with code {proc.returncode}")
            errors.append(proc.stdout[-500:] if proc.stdout else "No stdout")
            if proc.stderr:
                errors.append(proc.stderr[-300:])
        else:
            # Parse summary line
            lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
            summary_line = lines[-1] if lines else "Tests passed"
            details.append(f"pytest executed successfully: {summary_line}")

    except Exception as e:
        errors.append(f"Failed to execute pytest suite: {e}")

    return CheckResult(
        check_id=10,
        name="Automated Pytest Test Suite (pytest tests/)",
        passed=(len(errors) == 0),
        details=details,
        errors=errors
    )


# ==============================================================================
# Main Orchestration
# ==============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="JC2001 Smart Study Assistant PoC Quality Gate")
    parser.add_argument("--skip-pytest", action="store_true", help="Skip running the subprocess pytest test suite")
    args = parser.parse_args()

    print("=" * 80)
    print("  JC2001 SMART STUDY ASSISTANT SYSTEM (智学罗盘) PoC MVP - QUALITY GATE")
    print("  Group 5 | University of Aberdeen / BMIS | Quality & Acceptance Verification")
    print("=" * 80)

    checks = [
        check_1_files_presence,
        check_2_dependencies_import,
        check_3_pydantic_schemas,
        check_4_health_probe,
        check_5_quiz_endpoint,
        check_6_diagnose_engine,
        check_7_resilient_fallback,
        check_8_cors_headers,
        check_9_frontend_mount,
    ]

    if not args.skip_pytest:
        checks.append(check_10_pytest_suite)

    results: List[CheckResult] = []
    for check_fn in checks:
        res = check_fn()
        results.append(res)
        tag = "[PASS]" if res.passed else "[FAIL]"
        print(f"\n{tag} Check {res.check_id}: {res.name}")
        for d in res.details:
            print(f"       + {d}")
        for err in res.errors:
            print(f"       x ERROR: {err}")

    # Summary
    print("\n" + "=" * 80)
    print("  QUALITY GATE SCORECARD SUMMARY")
    print("=" * 80)

    all_passed = True
    for r in results:
        status_str = "PASS" if r.passed else "FAIL"
        if not r.passed:
            all_passed = False
        print(f"  Check {r.check_id:02d} | [{status_str}] | {r.name}")

    print("-" * 80)
    if all_passed:
        print("  OVERALL VERDICT: [PASS] - ALL PoC ACCEPTANCE CRITERIA FULLY MET!")
        print("  Preview Link: http://127.0.0.1:8000/ (FastAPI single-port console)")
        print("=" * 80)
        return 0
    else:
        print("  OVERALL VERDICT: [FAIL] - ONE OR MORE ACCEPTANCE CRITERIA FAILED.")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    sys.exit(main())
