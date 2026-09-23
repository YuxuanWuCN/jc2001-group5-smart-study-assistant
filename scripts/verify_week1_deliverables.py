#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 Software Engineering Week 1 - Deliverables Quality Gate & Verification Suite
Course: JC2001 Introduction to Software Engineering (2026–27)
Group:  Group 5 (BSc BMIS, 10 members, Leader: 吴宇轩 50106070)
Target: scripts/verify_week1_deliverables.py
Milestone: Milestone 5 - Automated Verification & Quality Gate

This script executes comprehensive, automated quality gate checks on all Week 1 deliverables:
  Check 1: Deliverable Files Presence & Non-Emptiness
  Check 2: Unresolved Placeholder & Bracket Scan
  Check 3: PDF Page Count & A4 Geometry Verification
  Check 4: 10-Member Team Roster & Leader Verification
  Check 5: Practical 1 Deliverables Completeness
  Check 6: Proposal Sectional & Academic Completeness
  Check 7: Exit Code & Reporting (0 on pass, 1 on fail)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Safe console encoding configuration for Windows PowerShell / CMD
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# Domain Constants & Specifications
# ==============================================================================

# Official 10-Member Team Roster (Chinese Name, English Pinyin, Student ID, Role)
ROSTER: List[Tuple[str, str, str, str]] = [
    ("吴宇轩", "Yuxuan Wu", "50106070", "Project Manager & Team Lead"),
    ("林泳桐", "Yongtong Lin", "50106038", "Principal Concept Co-Originator & Lead Domain Analyst"),
    ("王思鉴", "Sijian Wang", "50106045", "System Architect (UML & Knowledge Graph)"),
    ("江昊", "Hao Jiang", "50106065", "PoC Lead Developer (GraphRAG & Neo4j Engine)"),
    ("谢炜昕", "Weixin Xie", "50106034", "Principal Concept Co-Originator & QA Lead"),
    ("张梓健", "Zijian Zhang", "50106035", "Business Analyst (User Stories & Acceptance)"),
    ("习羽赛", "Yusai Xi", "50105989", "UI/UX Designer & Wireframe Lead"),
    ("董思钦", "Siqin Dong", "50106060", "PoC Logic Developer (Diagnostic API & Quiz)"),
    ("杨明杰", "Mingjie Yang", "50106061", "Software Testing & User Manual Lead"),
    ("梁子铉", "Zixuan Liang", "50106037", "Presentation, Media & Deployment Lead"),
]

LEADER_NAME = "吴宇轩"
LEADER_PINYIN = "Yuxuan Wu"
LEADER_ID = "50106070"

# The 5 socards.org icebreaker questions
SOCARDS_QUESTIONS: List[Tuple[str, str]] = [
    ("Q1", r"What are three things that would instantly cheer you up\?"),
    ("Q2", r"What is your favourite dish of food"),
    ("Q3", r"If you were to give a tour of your hometown"),
    ("Q4", r"If you could witness one key moment of history"),
    ("Q5", r"Where do you go and what do you do when you need to restore your energy\?"),
]

# Mandatory Proposal Sections (Sections 1–7; Section 8 removed per supervisor feedback)
PROPOSAL_SECTIONS: List[Tuple[int, str]] = [
    (1, r"## 1\.\s+Project Title"),
    (2, r"## 2\.\s+Problem"),
    (3, r"## 3\.\s+Solution"),
    (4, r"## 4\.\s+Objectives"),
    (5, r"## 5\.\s+Benefits"),
    (6, r"## 6\.\s+Timeline"),
    (7, r"## 7\.\s+Action Plan"),
]

# Standard A4 Dimensions in PostScript Points (72 pt / inch)
A4_WIDTH_PT = 595.3
A4_HEIGHT_PT = 841.9
A4_TOLERANCE_PT = 2.0


# ==============================================================================
# Data Structures for Verification Results
# ==============================================================================

@dataclass
class CheckResult:
    check_id: int
    name: str
    passed: bool
    details: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def add_detail(self, msg: str) -> None:
        self.details.append(msg)

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)
        self.passed = False

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)


# ==============================================================================
# Verification Suite Implementation
# ==============================================================================

class DeliverablesVerifier:
    """Automated Quality Gate and Verification Suite for JC2001 Week 1."""

    def __init__(self, root_dir: Path, require_review_pack: bool = False, verbose: bool = False):
        self.root_dir = root_dir.resolve()
        self.require_review_pack = require_review_pack
        self.verbose = verbose
        self.results: List[CheckResult] = []

        # Target file paths
        self.p1_md_path = self.root_dir / "practical1_deliverables.md"
        self.prop_md_path = self.root_dir / "reports" / "project_proposal.md"
        self.prop_docx_path = self.root_dir / "reports" / "project_proposal.docx"
        self.prop_pdf_path = self.root_dir / "reports" / "project_proposal.pdf"
        self.review_pack_path = self.root_dir / "reports" / "week1_team_review_pack.pdf"

    # --------------------------------------------------------------------------
    # Check 1: Deliverable Files Presence & Non-Emptiness
    # --------------------------------------------------------------------------
    def check_1_files_presence(self) -> CheckResult:
        res = CheckResult(
            check_id=1,
            name="Deliverable Files Presence & Non-Emptiness",
            passed=True,
        )

        # Primary mandatory files
        core_files = [
            ("Practical 1 Deliverables (MD)", self.p1_md_path, 1024),
            ("Proposal Document (MD)", self.prop_md_path, 1024),
            ("Proposal Document (DOCX)", self.prop_docx_path, 10240),
            ("Proposal Document (PDF)", self.prop_pdf_path, 10240),
        ]

        for label, path, min_size in core_files:
            if not path.exists():
                res.add_error(f"Missing mandatory file: {path.relative_to(self.root_dir)}")
                continue

            size = path.stat().st_size
            if size == 0:
                res.add_error(f"Empty file (0 bytes): {path.relative_to(self.root_dir)}")
            elif size < min_size:
                res.add_error(
                    f"File too small ({size} bytes < minimum {min_size} bytes): "
                    f"{path.relative_to(self.root_dir)}"
                )
            else:
                res.add_detail(
                    f"Found {label}: {path.relative_to(self.root_dir)} ({size / 1024:.1f} KB)"
                )

        # Verify DOCX zip validity
        if self.prop_docx_path.exists() and self.prop_docx_path.stat().st_size > 0:
            try:
                with zipfile.ZipFile(self.prop_docx_path, "r") as zf:
                    namelist = zf.namelist()
                    if "word/document.xml" not in namelist:
                        res.add_error(
                            f"Invalid DOCX structure (word/document.xml missing in zip): "
                            f"{self.prop_docx_path.relative_to(self.root_dir)}"
                        )
                    else:
                        res.add_detail("DOCX internal structure verified (valid OpenXML archive)")
            except zipfile.BadZipFile:
                res.add_error(
                    f"Corrupted DOCX archive (BadZipFile): {self.prop_docx_path.relative_to(self.root_dir)}"
                )

        # Verify PDF header magic
        if self.prop_pdf_path.exists() and self.prop_pdf_path.stat().st_size > 0:
            with open(self.prop_pdf_path, "rb") as f:
                header = f.read(5)
                if not header.startswith(b"%PDF-"):
                    res.add_error(
                        f"Invalid PDF binary header (expected '%PDF-', found {header!r}): "
                        f"{self.prop_pdf_path.relative_to(self.root_dir)}"
                    )
                else:
                    res.add_detail("PDF binary header verified (%PDF- magic present)")

        # Secondary / Supplementary review pack PDF
        if self.review_pack_path.exists():
            size = self.review_pack_path.stat().st_size
            if size < 1024:
                res.add_error(
                    f"Review pack PDF exists but is too small ({size} bytes): "
                    f"{self.review_pack_path.relative_to(self.root_dir)}"
                )
            else:
                # verify header
                with open(self.review_pack_path, "rb") as f:
                    if f.read(5).startswith(b"%PDF-"):
                        res.add_detail(
                            f"Supplementary Review Pack found & valid: "
                            f"{self.review_pack_path.relative_to(self.root_dir)} ({size / 1024:.1f} KB)"
                        )
                    else:
                        res.add_error(
                            f"Review pack has invalid PDF header: "
                            f"{self.review_pack_path.relative_to(self.root_dir)}"
                        )
        else:
            if self.require_review_pack:
                res.add_error(
                    f"Review pack PDF required but not found: "
                    f"{self.review_pack_path.relative_to(self.root_dir)}"
                )
            else:
                res.add_detail(
                    "Note: Supplementary review pack PDF (reports/week1_team_review_pack.pdf) "
                    "not present on disk (optional check passed gracefully)"
                )

        return res

    # --------------------------------------------------------------------------
    # Check 2: Unresolved Placeholder & Bracket Scan
    # --------------------------------------------------------------------------
    def check_2_placeholders(self) -> CheckResult:
        res = CheckResult(
            check_id=2,
            name="Unresolved Placeholder & Bracket Scan",
            passed=True,
        )

        def scan_text(source_name: str, text: str) -> None:
            # 1. Strip markdown links [label](url)
            cleaned = re.sub(r"\[([^\]\n]*)\]\([^)\n]+\)", "", text)

            # 2. Bracketed placeholder scan
            for m in re.finditer(r"\[([^\]\n]+)\]", cleaned):
                inner = m.group(1).strip()

                # Whitelist markdown checkboxes: [x], [ ], [X]
                if re.match(r"^[ xX]$", inner):
                    continue

                # Whitelist academic citations: [1], [2], [1-4], [1]–[8], [1, 2], etc.
                if re.match(
                    r"^\d+(?:\s*[\-,–]\s*\d+)*(?:\s*,\s*\d+(?:\s*[\-,–]\s*\d+)*)*$",
                    inner,
                ):
                    continue

                # Whitelist Cypher relationship definitions like [:DEPENDS_ON {type: "易错于"}]
                if inner.startswith(":") or "DEPENDS_ON" in inner:
                    continue

                # Whitelist standard lifecycle / phase tags like [PHASE 1: ...]
                if re.match(r"^PHASE\s+\d", inner, re.IGNORECASE):
                    continue

                # Detect suspicious placeholder keywords
                inner_upper = inner.upper()
                forbidden_keywords = [
                    "TBD", "TODO", "FIXME", "XXX", "INSERT",
                    "YOUR NAME", "STUDENT ID", "REPLACE", "PLACEHOLDER",
                ]
                if any(k in inner_upper for k in forbidden_keywords) or "..." in inner:
                    res.add_error(f"Unresolved bracket placeholder '[{inner}]' in {source_name}")
                elif any(inner_upper.startswith(k) for k in ["INSERT ", "ENTER ", "ADD "]):
                    res.add_error(f"Suspicious instruction placeholder '[{inner}]' in {source_name}")

            # 3. Angle bracket placeholder scan: <...>, <TBD>, etc.
            for m in re.finditer(r"<([^>\n]+)>", cleaned):
                inner = m.group(1).strip()
                # Whitelist valid HTML tags
                if re.match(
                    r"^/?(?:br|hr|p|div|span|b|i|u|strong|em|a|table|tr|td|th|ul|ol|li)\b",
                    inner,
                    re.IGNORECASE,
                ):
                    continue

                inner_upper = inner.upper()
                forbidden_keywords = [
                    "TBD", "TODO", "FIXME", "XXX", "INSERT",
                    "YOUR NAME", "REPLACE", "PLACEHOLDER",
                ]
                if any(k in inner_upper for k in forbidden_keywords) or "..." in inner:
                    res.add_error(f"Unresolved angle bracket placeholder '<{inner}>' in {source_name}")

            # 4. Naked keyword scan: TODO, FIXME, XXX, TBD outside of words
            for m in re.finditer(r"\b(TODO|FIXME|XXX|TBD)\b", cleaned):
                ctx = cleaned[max(0, m.start() - 25): min(len(cleaned), m.end() + 25)].replace("\n", " ")
                res.add_error(
                    f"Naked placeholder keyword '{m.group(1)}' found in {source_name}: '...{ctx.strip()}...'"
                )

        # Scan practical1_deliverables.md
        if self.p1_md_path.exists():
            p1_text = self.p1_md_path.read_text(encoding="utf-8")
            scan_text("practical1_deliverables.md", p1_text)
            res.add_detail(f"Scanned practical1_deliverables.md ({len(p1_text)} characters)")

        # Scan reports/project_proposal.md
        if self.prop_md_path.exists():
            prop_text = self.prop_md_path.read_text(encoding="utf-8")
            scan_text("reports/project_proposal.md", prop_text)
            res.add_detail(f"Scanned reports/project_proposal.md ({len(prop_text)} characters)")

        # Scan reports/project_proposal.docx
        if self.prop_docx_path.exists():
            try:
                import docx
                doc = docx.Document(str(self.prop_docx_path))
                p_texts = [p.text for p in doc.paragraphs]
                cell_texts = [
                    c.text
                    for t in doc.tables
                    for row in t.rows
                    for c in row.cells
                ]
                docx_text = "\n".join(p_texts + cell_texts)
                scan_text("reports/project_proposal.docx", docx_text)
                res.add_detail(
                    f"Scanned reports/project_proposal.docx ({len(doc.paragraphs)} paras, "
                    f"{len(doc.tables)} tables, {len(docx_text)} characters)"
                )
            except Exception as e:
                res.add_error(f"Failed to read reports/project_proposal.docx: {e}")

        if res.passed:
            res.add_detail("Zero unresolved placeholders detected across all scanned deliverables")

        return res

    # --------------------------------------------------------------------------
    # Check 3: PDF Page Count & A4 Geometry
    # --------------------------------------------------------------------------
    def check_3_pdf_metrics(self) -> CheckResult:
        res = CheckResult(
            check_id=3,
            name="PDF Page Count & A4 Geometry",
            passed=True,
        )

        if not self.prop_pdf_path.exists():
            res.add_error(f"PDF file does not exist: {self.prop_pdf_path.relative_to(self.root_dir)}")
            return res

        try:
            import pymupdf
            pdf = pymupdf.open(str(self.prop_pdf_path))
            total_pages = len(pdf)
            body_pages = total_pages - 1  # Page 1 is unnumbered Title Page

            res.add_detail(f"Total PDF pages: {total_pages}")
            res.add_detail(f"Body pages (total - 1 Title Page): {body_pages}")

            # Criterion 1: Body pages strictly between 4 and 8
            if not (4 <= body_pages <= 8):
                res.add_error(
                    f"PDF body page count out of bounds: got {body_pages} body pages "
                    f"(total {total_pages}), required strictly between 4 and 8 pages (4 <= body <= 8)"
                )
            else:
                res.add_detail(f"Body page count assertion met: 4 <= {body_pages} <= 8")

            # Criterion 2: Geometry verification on every page (A4 tolerance ±2 pt)
            geometry_ok = True
            for i, page in enumerate(pdf):
                rect = page.rect
                width_diff = abs(rect.width - A4_WIDTH_PT)
                height_diff = abs(rect.height - A4_HEIGHT_PT)
                if width_diff > A4_TOLERANCE_PT or height_diff > A4_TOLERANCE_PT:
                    geometry_ok = False
                    res.add_error(
                        f"Page {i + 1} dimensions ({rect.width:.2f} x {rect.height:.2f} pt) "
                        f"deviate from standard A4 ({A4_WIDTH_PT} x {A4_HEIGHT_PT} pt) "
                        f"by > {A4_TOLERANCE_PT} pt"
                    )

            if geometry_ok:
                p0_rect = pdf[0].rect
                res.add_detail(
                    f"Page geometry confirmed standard A4: "
                    f"{p0_rect.width:.2f} x {p0_rect.height:.2f} pt across all {total_pages} pages"
                )

            # Criterion 3: Unnumbered Title Page (Page 1)
            title_text = pdf[0].get_text()
            if (LEADER_NAME not in title_text and LEADER_PINYIN not in title_text) or LEADER_ID not in title_text:
                res.add_error(
                    f"Leader {LEADER_NAME} / {LEADER_PINYIN} ({LEADER_ID}) not detected on PDF Title Page (Page 1)"
                )
            else:
                res.add_detail("Title Page metadata verified (Leader name and ID present on Page 1)")

            # Check footer on Body Page 1 (PDF Page 2)
            if total_pages >= 2:
                page2_text = pdf[1].get_text()
                if "Page 1" not in page2_text:
                    res.add_warning(
                        "Body Page 1 (PDF Page 2) footer may not contain restarted numbering 'Page 1'"
                    )
                else:
                    res.add_detail("Body page numbering confirmed restarted at 'Page 1' on PDF Page 2")

        except ImportError:
            res.add_error("PyMuPDF ('pymupdf') is not installed in the current Python environment")
        except Exception as e:
            res.add_error(f"Error inspecting PDF with PyMuPDF: {e}")

        return res

    # --------------------------------------------------------------------------
    # Check 4: Team Roster & Leader Verification
    # --------------------------------------------------------------------------
    def check_4_team_roster(self) -> CheckResult:
        res = CheckResult(
            check_id=4,
            name="Team Roster & Leader Verification",
            passed=True,
        )

        p1_text = self.p1_md_path.read_text(encoding="utf-8") if self.p1_md_path.exists() else ""
        prop_md_text = self.prop_md_path.read_text(encoding="utf-8") if self.prop_md_path.exists() else ""

        # Check all 10 members in practical1_deliverables.md
        p1_missing = []
        for zh_name, en_name, sid, role in ROSTER:
            if zh_name not in p1_text and en_name not in p1_text:
                p1_missing.append(f"Name '{zh_name}/{en_name}' missing in practical1_deliverables.md")
            if sid not in p1_text:
                p1_missing.append(f"Student ID '{sid}' missing in practical1_deliverables.md")

        if p1_missing:
            for err in p1_missing:
                res.add_error(err)
        else:
            res.add_detail("All 10 members and student IDs confirmed in practical1_deliverables.md")

        # Check all 10 members in reports/project_proposal.md
        prop_missing = []
        for zh_name, en_name, sid, role in ROSTER:
            if zh_name not in prop_md_text and en_name not in prop_md_text:
                prop_missing.append(f"Name '{zh_name}/{en_name}' missing in reports/project_proposal.md")
            if sid not in prop_md_text:
                prop_missing.append(f"Student ID '{sid}' missing in reports/project_proposal.md")

        if prop_missing:
            for err in prop_missing:
                res.add_error(err)
        else:
            res.add_detail("All 10 members and student IDs confirmed in reports/project_proposal.md")

        # Cross-check in compiled DOCX and PDF if available
        if self.prop_docx_path.exists():
            try:
                import docx
                doc = docx.Document(str(self.prop_docx_path))
                docx_full = "\n".join([p.text for p in doc.paragraphs] + [c.text for t in doc.tables for r in t.rows for c in r.cells])
                for zh_name, en_name, sid, _ in ROSTER:
                    if (zh_name not in docx_full and en_name not in docx_full) or sid not in docx_full:
                        res.add_error(f"Member '{zh_name}/{en_name}' ({sid}) missing in compiled DOCX proposal!")
                res.add_detail("All 10 members and student IDs confirmed in reports/project_proposal.docx")
            except Exception as e:
                res.add_warning(f"Could not inspect DOCX for roster: {e}")

        if self.prop_pdf_path.exists():
            try:
                import pymupdf
                pdf = pymupdf.open(str(self.prop_pdf_path))
                pdf_full = "\n".join(p.get_text() for p in pdf)
                for zh_name, en_name, sid, _ in ROSTER:
                    if (zh_name not in pdf_full and en_name not in pdf_full) or sid not in pdf_full:
                        res.add_error(f"Member '{zh_name}/{en_name}' ({sid}) missing in compiled PDF proposal!")
                res.add_detail("All 10 members and student IDs confirmed in reports/project_proposal.pdf")
            except Exception as e:
                res.add_warning(f"Could not inspect PDF for roster: {e}")

        # Check Leader assignment
        leader_p1_match = re.search(r"(?:吴宇轩|Yuxuan Wu).*?(?:Leader|Project Manager|PM)", p1_text, re.IGNORECASE)
        if not leader_p1_match:
            res.add_error(f"Leader {LEADER_NAME} / {LEADER_PINYIN} ({LEADER_ID}) not explicitly designated as Team Leader / PM in practical1_deliverables.md")
        else:
            res.add_detail("Leader Yuxuan Wu (吴宇轩) verified as Project Manager & Team Lead in practical1_deliverables.md")

        leader_prop_match = re.search(r"(?:吴宇轩|Yuxuan Wu).*?(?:Leader|Project Manager|PM)", prop_md_text, re.IGNORECASE)
        if not leader_prop_match:
            res.add_error(f"Leader {LEADER_NAME} / {LEADER_PINYIN} ({LEADER_ID}) not explicitly designated as Team Leader / PM in reports/project_proposal.md")
        else:
            res.add_detail("Leader Yuxuan Wu (吴宇轩) verified as Project Manager & Team Lead in reports/project_proposal.md")

        return res

    # --------------------------------------------------------------------------
    # Check 5: Practical 1 Completeness
    # --------------------------------------------------------------------------
    def check_5_practical1_completeness(self) -> CheckResult:
        res = CheckResult(
            check_id=5,
            name="Practical 1 Deliverables Completeness",
            passed=True,
        )

        if not self.p1_md_path.exists():
            res.add_error(f"practical1_deliverables.md does not exist at {self.p1_md_path}")
            return res

        p1_text = self.p1_md_path.read_text(encoding="utf-8")

        # Sub-check 1: 5 socards.org icebreaker questions answered for all 10 members
        total_member_answers = 0
        for i, (zh_name, en_name, sid, _) in enumerate(ROSTER, 1):
            m_pattern = rf"### Member {i}:\s*(?:{zh_name}|{en_name}).*?(?=### Member|\n## |\Z)"
            block_match = re.search(m_pattern, p1_text, re.DOTALL)
            if not block_match:
                res.add_error(f"Icebreaker section missing for Member {i} ({zh_name}/{en_name}, {sid})")
                continue

            member_block = block_match.group(0)
            for q_code, q_regex in SOCARDS_QUESTIONS:
                q_match = re.search(rf"#### {q_code}:.*?\n(.*?)(?=#### Q|\Z)", member_block, re.DOTALL)
                if not q_match:
                    res.add_error(f"Member {i} ({zh_name}/{en_name}) missing answer for question {q_code}")
                else:
                    ans_text = q_match.group(1).strip()
                    if len(ans_text) < 15:
                        res.add_error(f"Member {i} ({zh_name}/{en_name}) answer for {q_code} is too brief ({len(ans_text)} chars)")
                    else:
                        total_member_answers += 1

        if total_member_answers == 50:
            res.add_detail("All 50 icebreaker answers verified across all 10 members (10 members x 5 questions)")
        else:
            res.add_error(f"Expected 50 valid icebreaker answers, found {total_member_answers}")

        # Sub-check 2: 4-phase role allocation matrix
        if "## 3. 10-Member Role Allocation Matrix Across the 4 Project Phases" not in p1_text:
            res.add_error("Section 3 'Role Allocation Matrix' header missing in practical1_deliverables.md")
        else:
            # Check 4 phases
            phases = [
                "Phase 1: Requirements Capture & Proposal",
                "Phase 2: System Architecture & UML Design",
                "Phase 3: PoC Implementation & Knowledge Graph",
                "Phase 4: System Testing, Report, Manual & Video",
            ]
            for phase in phases:
                if phase not in p1_text:
                    res.add_error(f"Phase definition '{phase}' missing in role allocation matrix")
            res.add_detail("4-Phase Role Allocation Matrix verified with all phase headers")

        # Sub-check 3: 4-element topic definition (WHAT, WHO, constraints, vision)
        topic_elements = [
            ("WHAT the System Does", r"WHAT the System Does|WHAT THE SYSTEM DOES"),
            ("WHO the System Targets", r"WHO the System Targets|WHO IT TARGETS"),
            ("Major Requirements & Constraints", r"Major Requirements & Constraints|MAJOR CONSTRAINTS"),
            ("Long-Term Vision", r"Long-Term Vision|LONG-TERM VISION"),
        ]
        for label, pat in topic_elements:
            if not re.search(pat, p1_text, re.IGNORECASE):
                res.add_error(f"Topic definition missing core element: '{label}'")
        res.add_detail("4-Element Topic Definition verified (WHAT, WHO, Constraints, Long-Term Vision)")

        # Sub-check 4: Supervisor email draft from Leader 吴宇轩
        if "## 5. Formal Academic Email Draft to Academic Supervisor" not in p1_text:
            res.add_error("Section 5 'Email Draft to Academic Supervisor' missing in practical1_deliverables.md")
        else:
            email_section = p1_text[p1_text.find("## 5."):]
            if LEADER_NAME not in email_section or LEADER_ID not in email_section:
                res.add_error(f"Leader {LEADER_NAME} ({LEADER_ID}) not found in supervisor email draft")
            if "Kick-Off Meeting" not in email_section:
                res.add_error("Kick-Off meeting request missing from supervisor email draft")
            if "Option A" not in email_section or "Option B" not in email_section:
                res.add_error("Proposed meeting time slots (Options A, B, C) missing from supervisor email")
            res.add_detail("Formal supervisor kick-off meeting email draft from Leader 吴宇轩 verified")

        return res

    # --------------------------------------------------------------------------
    # Check 6: Proposal Sectional & Academic Completeness
    # --------------------------------------------------------------------------
    def check_6_proposal_completeness(self) -> CheckResult:
        res = CheckResult(
            check_id=6,
            name="Proposal Sectional & Academic Completeness",
            passed=True,
        )

        if not self.prop_md_path.exists():
            res.add_error(f"reports/project_proposal.md does not exist at {self.prop_md_path}")
            return res

        prop_text = self.prop_md_path.read_text(encoding="utf-8")

        # Sub-check 1: Dedicated unnumbered Title Page
        if not re.search(r"#+.*Proposal Title Page", prop_text, re.IGNORECASE):
            res.add_error("Proposal Title Page header missing in reports/project_proposal.md")
        else:
            title_meta = [
                ("Course Title", r"JC2001"),
                ("Degree Programme", r"BSc\s+(?:in\s+)?(?:Business Management and Information Systems|BMIS)"),
                ("Group Designation", r"Group 5"),
                ("Project Title", r"Smart Study Assistant System"),
            ]
            for label, pat in title_meta:
                if not re.search(pat, prop_text, re.IGNORECASE):
                    res.add_error(f"Title Page missing metadata: {label}")
            res.add_detail("Dedicated Title Page structure and metadata confirmed")

        # Sub-check 2: All 7 mandatory numbered sections
        for sec_num, sec_regex in PROPOSAL_SECTIONS:
            if not re.search(sec_regex, prop_text):
                res.add_error(f"Mandatory Section {sec_num} ({sec_regex}) missing in proposal")
        res.add_detail("All 7 mandatory numbered proposal sections verified")

        # Sub-check 3: Technical entities and academic rigor
        tech_entities = [
            ("GraphRAG", r"\bGraphRAG\b"),
            ("Neo4j", r"\bNeo4j\b"),
            ("Qwen-Turbo or DashScope", r"Qwen-Turbo|DashScope"),
            ("Misconception Relation", r"PRONE_TO_MISCONCEPTION|易错于"),
            ("SMART Objectives", r"\bSMART\b"),
            ("Deadline (14 December 2026)", r"14 December 2026"),
            ("WBS Table", r"WBS\s+1\.1"),
        ]
        for label, pat in tech_entities:
            if not re.search(pat, prop_text):
                res.add_error(f"Required technical or project entity missing: {label}")
        res.add_detail("Core technical entities verified (GraphRAG, Neo4j, Qwen, PRONE_TO_MISCONCEPTION, SMART, WBS)")

        # Sub-check 4: Academic references [1] to [8]
        if "## References" not in prop_text:
            res.add_error("References section header missing in proposal")
        else:
            for ref_idx in range(1, 9):
                # Check bibliography entry [i]
                entry_pattern = rf"\[{ref_idx}\]\s+[A-Z]"
                if not re.search(entry_pattern, prop_text):
                    res.add_error(f"Bibliography entry for reference [{ref_idx}] missing in References section")

                # Check in-text citation [i]
                cite_pattern = rf"\[{ref_idx}\]"
                if not re.search(cite_pattern, prop_text[:prop_text.find("## References")]):
                    # Also check range citations like [1]–[8] or [1], [2]
                    if not re.search(r"\[1\][–\-–]\[8\]|\[[0-9,\s–\-]+\]", prop_text):
                        res.add_warning(f"Citation for [{ref_idx}] may not be explicitly referenced in narrative body")

            res.add_detail("All 8 academic references [1]–[8] verified in References section and text")

        return res

    # --------------------------------------------------------------------------
    # Check 7: Exit Code & Reporting Orchestration
    # --------------------------------------------------------------------------
    def run_all(self) -> int:
        """Runs all 6 checks, prints detailed diagnostics, and returns exit code."""
        print("=" * 78)
        print("  JC2001 INTRODUCTION TO SOFTWARE ENGINEERING (2026–27)")
        print("  WEEK 1 DELIVERABLES AUTOMATED VERIFICATION & QUALITY GATE")
        print("  Group: Group 5 (BSc BMIS) | Team Leader: 吴宇轩 (50106070)")
        print("=" * 78)
        print(f"Working Directory: {self.root_dir}\n")

        self.results = []

        # Execute Checks 1 to 6
        checks = [
            ("CHECK 1/6", self.check_1_files_presence),
            ("CHECK 2/6", self.check_2_placeholders),
            ("CHECK 3/6", self.check_3_pdf_metrics),
            ("CHECK 4/6", self.check_4_team_roster),
            ("CHECK 5/6", self.check_5_practical1_completeness),
            ("CHECK 6/6", self.check_6_proposal_completeness),
        ]

        overall_passed = True

        for step_label, check_fn in checks:
            res = check_fn()
            self.results.append(res)
            status_str = "[PASS]" if res.passed else "[FAIL]"

            print(f"[{step_label}] {res.name:<48} {status_str}")

            if self.verbose or not res.passed:
                for detail in res.details:
                    print(f"         + {detail}")
            else:
                # Print key summary details
                for detail in res.details[:2]:
                    print(f"         + {detail}")
                if len(res.details) > 2:
                    print(f"         + ... and {len(res.details) - 2} more verified conditions")

            if res.warnings:
                for warn in res.warnings:
                    print(f"         [!] WARNING: {warn}")

            if not res.passed:
                overall_passed = False
                for err in res.errors:
                    print(f"         [X] ERROR: {err}")
            print()

        # Final Summary Scorecard (Check 7)
        print("=" * 78)
        print("  VERIFICATION SCORECARD & QUALITY GATE VERDICT")
        print("=" * 78)

        total_checks = len(self.results)
        passed_checks = sum(1 for r in self.results if r.passed)
        failed_checks = total_checks - passed_checks
        total_errors = sum(len(r.errors) for r in self.results)
        total_warnings = sum(len(r.warnings) for r in self.results)

        print(f"Total Quality Checks:  {total_checks}")
        print(f"Passed Checks:         {passed_checks}")
        print(f"Failed Checks:         {failed_checks}")
        print(f"Total Errors:          {total_errors}")
        print(f"Total Warnings:        {total_warnings}")
        print("-" * 78)

        if overall_passed:
            print("  OVERALL VERDICT: [PASS] - ALL WEEK 1 DELIVERABLES FULLY COMPLIANT")
            print("  Exit Code: 0 (Quality Gate Satisfied)")
            print("=" * 78)
            return 0
        else:
            print("  OVERALL VERDICT: [FAIL] - QUALITY GATE VIOLATIONS DETECTED")
            print("  Exit Code: 1 (Deliverables Require Remediation)")
            print("=" * 78)
            return 1


# ==============================================================================
# CLI Entry Point
# ==============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="JC2001 Week 1 Deliverables Automated Verification Suite"
    )
    parser.add_argument(
        "--root-dir", "-r",
        default=".",
        help="Root repository directory containing deliverables (default: current directory)",
    )
    parser.add_argument(
        "--require-review-pack",
        action="store_true",
        help="Strictly require reports/week1_team_review_pack.pdf to exist",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print verbose output for all verification checks",
    )
    args = parser.parse_args()

    verifier = DeliverablesVerifier(
        root_dir=Path(args.root_dir),
        require_review_pack=args.require_review_pack,
        verbose=args.verbose,
    )
    return verifier.run_all()


if __name__ == "__main__":
    sys.exit(main())
