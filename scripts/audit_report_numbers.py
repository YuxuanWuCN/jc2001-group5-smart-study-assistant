#!/usr/bin/env python3
"""Audit numeric claims in the report against the actual code.

Motivation: the Cycle 3 supervisor review found that the report stated
"twelve questions, thirty-six traps, 657 lines" while the running system
served seventeen questions and fifty-one traps from a 932-line module.
The text had been written against an earlier state of the file and nobody
re-checked it before integration.

This script makes that class of error impossible to ship silently: it reads
ground truth out of the repository, then scans the report markdown for
number claims about the *shipped seed bank* that contradict it.

Deliberately narrow. A claim is only checked when the sentence is talking
about the curated bank itself. Lines about the MMLU benchmark, the roadmap,
or future targets are excluded, because "12 subjects" is a true statement
about the MMLU evaluation set and not about our question bank.

Exit code 0 = report agrees with code, 1 = contradictions found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "backend" / "app" / "data" / "seed_questions.py"

REPORT_CANDIDATES = [
    ROOT / "reports" / "interim_50pct" / "StudyGraph_Cycle3_Interim_Report_50pct.md",
    ROOT / "reports" / "final_report" / "StudyGraph_Cycle3_Final_Report.md",
    ROOT / "reports" / "final_report" / "FULL_TECHNICAL_REPORT_EN.md",
]

NUMBER_WORDS = {
    "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-four": 24, "thirty": 30, "thirty-six": 36, "forty": 40,
    "forty-eight": 48, "fifty": 50, "fifty-one": 51, "sixty": 60,
}

# Any line carrying one of these markers is not making a claim about the
# shipped bank, so it is out of scope for this audit.
EXCLUDE_MARKERS = (
    "mmlu", "benchmark", "ragas", "future", "roadmap", "planned", "week b",
    "target", "aim", "aspire", "scale to", "scale up", "phase 2", "phase two",
    "would hold", "could hold", "should hold", "evaluation set", "held-out",
    "in total across", "projection", "estimate", "if we", "by the end",
    # Rhetorical "two questions" ("what the student got wrong, and how we
    # tell them") is not a claim about the size of the shipped bank.
    "easy to confuse",
    # The business-model table states authoring *scenarios*, not the current
    # bank; its provenance column says so explicitly.
    "scenario", "assumes", "provenance",
)

# The token before the noun must not be the tail of a hyphenated word
# ("thirty-six traps" must not be read as "six traps").
BOUNDARY = r"(?<![\w-])"


def ground_truth() -> dict[str, int]:
    text = SEED.read_text(encoding="utf-8")
    qids = re.findall(r'QuizItem\(\s*\n\s*id="([^"]+)"', text)
    subjects = re.findall(
        r'QuizItem\(\s*\n\s*id="[^"]+",\s*\n\s*subject="([^"]+)"', text
    )
    traps = re.findall(r'"(trap_[A-Za-z0-9_]+)"\s*:\s*TrapDetail\(', text)
    options = re.findall(r"OptionItem\(", text)
    return {
        "questions": len(qids),
        "subjects": len(set(subjects)),
        "traps": len(set(traps)),
        "options": len(options),
        "seed_lines": len(text.splitlines()),
    }


# label, regex (group 1 = the claimed number), ground-truth key, extra condition
CLAIM_PATTERNS: list[tuple[str, str, str]] = [
    ("questions in the bank",
     BOUNDARY + r"(\w+|\d+)\s+(?:curated\s+)?questions\b", "questions"),
    ("traps in the bank",
     BOUNDARY + r"(\w+|\d+)\s+traps\b", "traps"),
    ("subjects in the bank",
     BOUNDARY + r"(\w+|\d+)\s+(?:subjects|disciplines)\b", "subjects"),
    ("seed module line count",
     BOUNDARY + r"(\d+)\s+lines\b", "seed_lines"),
]

# Phrases that make a "N questions/traps" claim a per-item statement rather
# than a total, e.g. "each question carries four options".
PER_ITEM_MARKERS = ("each", "per question", "per item", "every question", "a question")


def to_number(token: str) -> int | None:
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return NUMBER_WORDS.get(token)


def scan(path: Path, truth: dict[str, int]):
    findings = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        low = line.lower()
        if any(marker in low for marker in EXCLUDE_MARKERS):
            continue
        for label, pattern, key in CLAIM_PATTERNS:
            for match in re.finditer(pattern, line, flags=re.IGNORECASE):
                claimed = to_number(match.group(1))
                actual = truth[key]
                if claimed is None or claimed == actual:
                    continue
                if key == "seed_lines" and "seed" not in low:
                    continue
                if key in ("questions", "traps") and any(
                    marker in low for marker in PER_ITEM_MARKERS
                ):
                    continue
                findings.append((line_no, label, match.group(0), claimed, actual))
    return findings


def main() -> int:
    truth = ground_truth()
    print("=== GROUND TRUTH (backend/app/data/seed_questions.py) ===")
    for k, v in truth.items():
        print(f"  {k:12s}: {v}")
    print()

    total = 0
    for report in REPORT_CANDIDATES:
        if not report.exists():
            continue
        findings = scan(report, truth)
        rel = report.relative_to(ROOT)
        if not findings:
            print(f"[OK]   {rel}: numbers agree with the code")
            continue
        print(f"[FAIL] {rel}: {len(findings)} contradiction(s)")
        for line_no, label, snippet, claimed, actual in findings:
            print(f"   line {line_no:5d} | {label:22s} | {snippet!r} -> says {claimed}, actual {actual}")
        total += len(findings)

    print()
    if total:
        print(f"RESULT: {total} stale numeric claim(s). The report does not match the code.")
        return 1
    print("RESULT: report numbers agree with the code.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
