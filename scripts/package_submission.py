"""Build and verify the submission archive for JC2001 Group 5.

The archive holds exactly the tree described in Section 5.6.5 of the report:
backend/, frontend/, tests/, graphrag_final/, requirements.txt, README.md,
.env.example and docs/User_Manual.pdf.  It is written as a single top-level
directory (jc2001-group5-poc/) so that the documented ``unzip ... && cd ...``
sequence works.

The script refuses to write the archive when the credential scan finds a
high-confidence secret.  After writing, it unpacks the archive into an empty
temporary directory, runs the test suite from the unpacked copy and starts the
service once to confirm that /api/health answers.  The numbers it prints are
the ones to quote in the viva.

Usage:
    python scripts/package_submission.py [--out PATH] [--skip-verify]
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
TOP_DIR = "jc2001-group5-poc"

INCLUDE_TREES = ["backend", "frontend", "tests", "graphrag_final"]
INCLUDE_FILES = [
    "requirements.txt",
    "README.md",
    ".env.example",
    "docs/User_Manual.pdf",
    "docs/User_Manual.tex",
]

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    ".idea",
    ".vscode",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".log", ".aux", ".out", ".toc"}
EXCLUDED_NAMES = {".env", ".DS_Store", "Thumbs.db"}

TEXT_SUFFIXES = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".csv",
    ".js",
    ".css",
    ".html",
    ".yml",
    ".yaml",
    ".example",
    ".tex",
    ".cfg",
    ".ini",
    ".toml",
}

# (pattern, description, blocking).  Blocking patterns must never appear in the
# archive; the advisory ones are recorded for the submission checklist.
SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{16,}", "DashScope-style literal API key", True),
    (r"neo4j\+ssc://[^\s\"'`]*", "hardcoded neo4j+s connection URI", True),
    (r"neo4j://[^\s\"'`]*:[^\s\"'`]*@", "neo4j URI carrying credentials", True),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id", True),
    (
        r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*[\"'][^\"'\s]{8,}[\"']",
        "literal credential assignment",
        True,
    ),
    (r"BEGIN [A-Z ]*PRIVATE KEY", "embedded private key", True),
    (r"(?i)\bpassword\b", "the word 'password' (prose mentions are expected)", False),
]

REPORT_PATH = ROOT / "reports" / "submission" / "credential_scan.txt"

# Tokens that look like credentials but are documentation placeholders or
# synthetic values used by the masking tests.  Each entry is quoted verbatim so
# that the allowlist stays auditable; a real key must never be added here.
ALLOWED_LITERALS = {
    "sk-xxxxxxxxxxxxxxxx",  # placeholder shown in the API-key input of the console
    "sk-0123456789abcdefghijklmnop",  # synthetic value used by the key-masking test
}

PLACEHOLDER_MARKERS = ("your-", "your_", "example", "placeholder", "changeme", "xxxx")


def is_allowlisted(token: str, line: str) -> bool:
    """Return True for documentation placeholders and synthetic test values."""
    if any(token in allowed for allowed in ALLOWED_LITERALS if token in allowed):
        return True
    lowered = token.lower()
    if any(marker in lowered for marker in PLACEHOLDER_MARKERS):
        return True
    body = token[3:] if token.lower().startswith("sk-") else token
    # A single repeated character carries no entropy and cannot be a real key.
    if len(set(body)) <= 2:
        return True
    return False


def iter_payload() -> list[Path]:
    """Return every regular file that belongs in the archive."""
    files: list[Path] = []
    for rel in INCLUDE_TREES:
        base = ROOT / rel
        if not base.is_dir():
            raise SystemExit(f"missing payload directory: {rel}")
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDED_DIRS)
            for name in sorted(filenames):
                path = Path(dirpath) / name
                if name in EXCLUDED_NAMES or path.suffix.lower() in EXCLUDED_SUFFIXES:
                    continue
                files.append(path)
    for rel in INCLUDE_FILES:
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"missing payload file: {rel}")
        files.append(path)
    return files


def scan_secrets(files: list[Path]) -> tuple[list[tuple[str, int, str, str]], list[str]]:
    """Scan text payload for credentials.  Returns (blocking hits, advisory lines)."""
    blocking: list[tuple[str, int, str, str]] = []
    advisory: list[str] = []
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(text.split("\n"), start=1):
            for pattern, desc, is_blocking in SECRET_PATTERNS:
                match = re.search(pattern, line)
                if not match:
                    continue
                token = match.group(0)
                if is_allowlisted(token, line):
                    advisory.append(f"{rel}:{lineno}: allowlisted placeholder ({token[:40]})")
                    continue
                if is_blocking:
                    blocking.append((rel, lineno, desc, line.strip()[:160]))
                else:
                    advisory.append(f"{rel}:{lineno}: {desc}")
    return blocking, advisory


def build_archive(files: list[Path], out_path: Path) -> tuple[int, int]:
    """Write the archive; returns (entry count, byte size)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        out_path.unlink()
    entries = 0
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            arcname = f"{TOP_DIR}/{path.relative_to(ROOT).as_posix()}"
            zf.write(path, arcname)
            entries += 1
    return entries, out_path.stat().st_size


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def verify_archive(zip_path: Path) -> dict[str, object]:
    """Unpack into an empty directory and exercise the documented start path."""
    result: dict[str, object] = {}
    with tempfile.TemporaryDirectory(prefix="jc2001-pkg-") as tmp:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp)
        roots = [p for p in Path(tmp).iterdir() if p.is_dir()]
        if len(roots) != 1 or roots[0].name != TOP_DIR:
            raise SystemExit(f"archive must unpack into one directory named {TOP_DIR}")
        tree = roots[0]
        result["tree"] = str(tree)

        pytest_run = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "-q"],
            cwd=tree,
            capture_output=True,
            text=True,
        )
        tail = [line for line in pytest_run.stdout.strip().split("\n") if line.strip()][-1]
        result["pytest_exit"] = pytest_run.returncode
        result["pytest_tail"] = tail

        port = free_port()
        env = dict(os.environ)
        env["STUDYGRAPH_PORT"] = str(port)
        server = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "backend.app.main:app", "--port", str(port)],
            cwd=tree,
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            health = ""
            shell = b""
            for _ in range(80):
                try:
                    with urlopen(f"http://127.0.0.1:{port}/api/health", timeout=1) as resp:
                        health = f"{resp.status} {resp.read().decode('utf-8')[:120]}"
                    with urlopen(f"http://127.0.0.1:{port}/", timeout=2) as resp:
                        shell = resp.read()
                    break
                except Exception:  # noqa: BLE001 - server needs a moment to boot
                    time.sleep(0.25)
            result["health"] = health
            result["shell_bytes"] = len(shell)
        finally:
            server.terminate()
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server.kill()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=str(ROOT / "reports" / "submission" / "jc2001-group5-poc.zip"),
    )
    parser.add_argument("--skip-verify", action="store_true")
    args = parser.parse_args()
    out_path = Path(args.out)

    files = iter_payload()
    blocking, advisory = scan_secrets(files)

    lines = [
        "Credential scan of the submission payload",
        f"Scanned files: {len(files)}",
        f"Blocking findings: {len(blocking)}",
        f"Advisory findings: {len(advisory)}",
        "",
    ]
    for rel, lineno, desc, snippet in blocking:
        lines.append(f"BLOCKING {rel}:{lineno} [{desc}] {snippet}")
    lines.extend(advisory)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if blocking:
        print(f"refusing to package: {len(blocking)} blocking secret finding(s)")
        for rel, lineno, desc, _ in blocking:
            print(f"  {rel}:{lineno}  {desc}")
        return 1

    entries, size = build_archive(files, out_path)
    print(f"archive: {out_path}")
    print(f"entries: {entries}")
    print(f"size: {size} bytes ({size / 1024 / 1024:.2f} MB)")
    print(f"credential scan: 0 blocking, {len(advisory)} advisory (see {REPORT_PATH})")

    if args.skip_verify:
        return 0

    result = verify_archive(out_path)
    print(f"pytest: exit={result['pytest_exit']}  {result['pytest_tail']}")
    print(f"health: {result['health']}")
    print(f"shell bytes: {result['shell_bytes']}")
    if result["pytest_exit"] != 0 or not str(result["health"]).startswith("200"):
        print("verification failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
