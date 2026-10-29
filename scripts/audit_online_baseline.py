#!/usr/bin/env python3
"""
Online Baseline & Hallucination Experiment Harness
Part of Speckit 004: Persona-Hallucination-Audit
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO_ROOT / "reports" / "audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)


def get_git_info():
    branch = "unknown"
    commit = "unknown"
    try:
        b_res = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
        if b_res.returncode == 0:
            branch = b_res.stdout.strip()
        c_res = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
        if c_res.returncode == 0:
            commit = c_res.stdout.strip()
    except Exception:
        pass
    return branch, commit


def main():
    api_key = os.getenv("QWEN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")

    if not api_key:
        branch, commit = get_git_info()
        skip_payload = {
            "status": "skipped",
            "reason": "QWEN_API_KEY not set",
            "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "env_fingerprint": {
                "python_version": sys.version.split()[0],
                "git_commit": commit,
                "branch": branch
            },
            "what_would_have_run": "3 groups x 12 questions x 2 repeats = 72 samples",
            "how_to_run": "set QWEN_API_KEY=<your key> && python scripts/audit_online_baseline.py",
            "report_usage": "L4 记为 N/A（未测量），结论等级停在 V1"
        }
        skip_file = AUDIT_DIR / "online_baseline.skipped.json"
        with open(skip_file, "w", encoding="utf-8") as f:
            json.dump(skip_payload, f, ensure_ascii=False, indent=2)

        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        print(f"[INFO] QWEN_API_KEY not configured. Generated skip record -> {skip_file}")
        print("[OK] Exit 0 (graceful skip as defined in Online Experiment Contract)")
        sys.exit(0)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print("[INFO] Live API key detected. Running baseline experiment...")
    # In live mode, execute sample calls or generate online_baseline.csv


if __name__ == "__main__":
    main()
