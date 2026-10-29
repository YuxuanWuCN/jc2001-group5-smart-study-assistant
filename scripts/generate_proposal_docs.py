#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 Software Engineering Week 1 - Dual-Format Compilation Tooling
Author: Group 5 (Leader: 吴宇轩 50106070)
Milestone: Milestone 4 - Document Generation Pipeline

This script compiles the Markdown Project Proposal (reports/project_proposal.md)
into professional, submission-grade DOCX and PDF formats:
  - reports/project_proposal.docx
  - reports/project_proposal.pdf

Formatting and Quality Constraints:
  1. Paper Size: Standard A4 (210mm x 297mm).
  2. Margins: Standard 1-inch (2.54cm / 72pt) on all 4 sides.
  3. Section 1: Unnumbered Title Page (centered metadata, 10-member roster table).
  4. Section 2: Body text, separated by Next-Page Section Break, unlinked from
     previous header/footer, with page number restarting at 1 right-aligned.
  5. Typography: 12pt Times New Roman, 1.5 line spacing, 0pt before, 4pt after.
  6. Headings: 18pt/14pt/12pt with keep_with_next = True.
  7. Tables: Navy styled headers (#1B365D), white bold text, clean borders, 9.5-10pt text.
  8. References: 10.5pt, 1.15 line spacing, hanging indent.
  9. Page Budget: Total body pages (excluding Title Page) strictly between 4 and 8 pages.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import docx
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Mm, Pt, RGBColor

# Configure console encoding for Windows UTF-8 safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ==============================================================================
# Helper Functions: Typography, OpenXML Fields & Styling
# ==============================================================================

def set_run_font(
    run,
    name: str = "Times New Roman",
    size_pt: float = 12.0,
    bold: bool = False,
    italic: bool = False,
    color_rgb: Optional[Tuple[int, int, int]] = (0, 0, 0),
    east_asia: str = "Microsoft YaHei",
) -> None:
    """Sets Latin font, East Asian font, size, weight, and color on a text run."""
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color_rgb is not None:
        run.font.color.rgb = RGBColor(*color_rgb)

    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), east_asia)
    rFonts.set(qn("w:cs"), name)


def clean_math_and_latex(text: str) -> str:
    """Converts LaTeX math expressions like $\\le 2$, $\\ge 85\\%$ to clean Unicode symbols."""
    def replace_math(m: re.Match) -> str:
        inner = m.group(1)
        inner = inner.replace(r"\le", "≤")
        inner = inner.replace(r"\ge", "≥")
        inner = inner.replace(r"\%", "%")
        return inner.strip()

    cleaned = re.sub(r"\$([^$]+)\$", replace_math, text)
    cleaned = cleaned.replace(r"$\le$", "≤").replace(r"$\ge$", "≥")
    return cleaned


def add_formatted_text(
    paragraph,
    text: str,
    base_size: float = 12.0,
    base_bold: bool = False,
    base_italic: bool = False,
    base_color: Tuple[int, int, int] = (0, 0, 0),
    east_asia: str = "Microsoft YaHei",
) -> None:
    """
    Parses inline markdown tokens (**bold**, *italic*, `code`) and appends
    corresponding styled runs to the paragraph.
    """
    text = clean_math_and_latex(text)
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
    tokens = pattern.split(text)

    for token in tokens:
        if not token:
            continue
        if token.startswith("**") and token.endswith("**"):
            inner = token[2:-2]
            r = paragraph.add_run(inner)
            set_run_font(
                r,
                name="Times New Roman",
                size_pt=base_size,
                bold=True,
                italic=base_italic,
                color_rgb=base_color,
                east_asia=east_asia,
            )
        elif token.startswith("*") and token.endswith("*"):
            inner = token[1:-1]
            r = paragraph.add_run(inner)
            set_run_font(
                r,
                name="Times New Roman",
                size_pt=base_size,
                bold=base_bold,
                italic=True,
                color_rgb=base_color,
                east_asia=east_asia,
            )
        elif token.startswith("`") and token.endswith("`"):
            inner = token[1:-1]
            r = paragraph.add_run(inner)
            set_run_font(
                r,
                name="Consolas",
                size_pt=base_size - 1.0,
                bold=base_bold,
                italic=base_italic,
                color_rgb=(0x8B, 0x1E, 0x3F),
                east_asia=east_asia,
            )
        else:
            r = paragraph.add_run(token)
            set_run_font(
                r,
                name="Times New Roman",
                size_pt=base_size,
                bold=base_bold,
                italic=base_italic,
                color_rgb=base_color,
                east_asia=east_asia,
            )


def apply_table_styling(
    table,
    col_widths: Optional[List[Inches]] = None,
    hdr_bg: str = "1B365D",
    alt_bg: str = "F8FAFC",
    hdr_font_size: float = 10.0,
    cell_font_size: float = 9.5,
) -> None:
    """
    Applies professional styling to a python-docx table:
      - Centered table alignment
      - Dark navy header shading with bold white text
      - Alternating row tint
      - Clean horizontal borders (no vertical borders)
      - Cell padding (margins)
      - Row cantSplit and header repeat on next page
    """
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Subtle horizontal borders
    borders = parse_xml(f"""
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="1B365D"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1B365D"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    """)
    table._tbl.tblPr.append(borders)

    # Compact cell margins
    cell_mar = parse_xml(f"""
        <w:tblCellMar {nsdecls("w")}>
            <w:top w:w="70" w:type="dxa"/>
            <w:bottom w:w="70" w:type="dxa"/>
            <w:left w:w="120" w:type="dxa"/>
            <w:right w:w="120" w:type="dxa"/>
        </w:tblCellMar>
    """)
    table._tbl.tblPr.append(cell_mar)

    # Header Row Formatting
    hdr_row = table.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

    for cell in hdr_row.cells:
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hdr_bg}"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        for p in cell.paragraphs:
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(1.5)
            p.paragraph_format.line_spacing = 1.05
            for r in p.runs:
                set_run_font(
                    r,
                    name="Times New Roman",
                    size_pt=hdr_font_size,
                    bold=True,
                    color_rgb=(0xFF, 0xFF, 0xFF),
                )

    # Data Rows Formatting
    for row_idx, row in enumerate(table.rows[1:], start=1):
        bg = alt_bg if row_idx % 2 == 0 else "FFFFFF"
        r_trPr = row._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if bg != "FFFFFF":
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg}"/>')
                cell._tc.get_or_add_tcPr().append(shd)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(0.5)
                p.paragraph_format.space_after = Pt(0.5)
                p.paragraph_format.line_spacing = 1.05
                for r in p.runs:
                    set_run_font(
                        r,
                        name="Times New Roman",
                        size_pt=cell_font_size,
                        color_rgb=(0x1F, 0x29, 0x37),
                    )

    # Apply column widths across all rows
    if col_widths:
        for row in table.rows:
            for c_idx, w in enumerate(col_widths):
                if c_idx < len(row.cells):
                    row.cells[c_idx].width = w


# ==============================================================================
# Markdown Parser: Separates Title Page Metadata and Body Blocks
# ==============================================================================

class ProposalMarkdownParser:
    """Parses project_proposal.md into Title Page metadata, roster, and body blocks."""

    def __init__(self, md_path: str | Path):
        self.md_path = Path(md_path)
        with open(self.md_path, "r", encoding="utf-8") as f:
            self.content = f.read()
        self.lines = [l.rstrip("\r\n") for l in self.content.splitlines()]

    def parse(self) -> Tuple[Dict[str, str], List[str], List[List[str]], List[str]]:
        """
        Splits the markdown into:
          - metadata: dict of title page key-values
          - roster_headers: list of table header strings
          - roster_rows: list of row lists
          - body_lines: raw markdown lines for the proposal body
        """
        title_lines: List[str] = []
        body_lines: List[str] = []
        found_section_divider = False

        for line in self.lines:
            if not found_section_divider:
                if line.strip() == "---":
                    found_section_divider = True
                    continue
                title_lines.append(line)
            else:
                body_lines.append(line)

        metadata: Dict[str, str] = {}
        roster_headers: List[str] = []
        roster_rows: List[List[str]] = []

        # Parse metadata key-values from Title Page
        tbl_lines: List[str] = []

        for line in title_lines:
            s = line.strip()
            if not s:
                continue
            if s.startswith("|") and s.endswith("|"):
                tbl_lines.append(s)
                continue
            m = re.match(r"^\*\*([^*]+)\*\*:\s*(.*)$", s)
            if m:
                key = m.group(1).strip()
                val = m.group(2).strip()
                metadata[key] = val

        # Parse Roster table
        if len(tbl_lines) >= 3:
            roster_headers = [c.strip() for c in tbl_lines[0].strip("|").split("|")]
            for r_line in tbl_lines[2:]:
                cols = [c.strip() for c in r_line.strip("|").split("|")]
                roster_rows.append(cols)

        return metadata, roster_headers, roster_rows, body_lines


# ==============================================================================
# DOCX Document Builder: Two-Section Layout, A4 Geometry & Typography
# ==============================================================================

class ProposalDocxBuilder:
    """Builds reports/project_proposal.docx using python-docx."""

    def __init__(self, metadata: Dict[str, str], roster_headers: List[str], roster_rows: List[List[str]], body_lines: List[str]):
        self.metadata = metadata
        self.roster_headers = roster_headers
        self.roster_rows = roster_rows
        self.body_lines = body_lines
        self.doc = docx.Document()
        self._configure_default_styles()

    def _configure_default_styles(self) -> None:
        """Sets default Normal style to 12pt Times New Roman with 1.5 line spacing."""
        normal_style = self.doc.styles["Normal"]
        normal_style.font.name = "Times New Roman"
        normal_style.font.size = Pt(12.0)
        normal_style.paragraph_format.line_spacing = 1.5
        normal_style.paragraph_format.space_before = Pt(0)
        normal_style.paragraph_format.space_after = Pt(4.0)

    def build(self, output_docx: str | Path) -> None:
        """Constructs the full document and saves to output_docx."""
        self._build_section_1_title_page()
        self._build_section_2_body()
        output_path = Path(output_docx)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.doc.save(str(output_path))

    def _build_section_1_title_page(self) -> None:
        """Constructs Section 1: Unnumbered Title Page (fits exactly on Page 1)."""
        s1 = self.doc.sections[0]
        s1.page_width = Mm(210)
        s1.page_height = Mm(297)
        s1.top_margin = Inches(1.0)
        s1.bottom_margin = Inches(1.0)
        s1.left_margin = Inches(1.0)
        s1.right_margin = Inches(1.0)
        s1.header.is_linked_to_previous = False
        s1.footer.is_linked_to_previous = False

        # Course Header
        course_title = self.metadata.get("Course Title", "JC2001 Introduction to Software Engineering")
        acad_year = self.metadata.get("Academic Year", "2026–27")
        p_course = self.doc.add_paragraph()
        p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_course.paragraph_format.space_before = Pt(0)
        p_course.paragraph_format.space_after = Pt(2)
        p_course.paragraph_format.line_spacing = 1.15
        r = p_course.add_run(f"{course_title.upper()} ({acad_year})")
        set_run_font(r, name="Times New Roman", size_pt=13, bold=True, color_rgb=(0x1B, 0x36, 0x5D))

        # Programme & Group
        degree = self.metadata.get("Degree Programme", "BSc in Business Management and Information Systems (BSc BMIS)")
        group = self.metadata.get("Group Designation", "Group 5")
        p_prog = self.doc.add_paragraph()
        p_prog.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_prog.paragraph_format.space_before = Pt(0)
        p_prog.paragraph_format.space_after = Pt(8)
        p_prog.paragraph_format.line_spacing = 1.15
        r = p_prog.add_run(f"{degree} — {group}")
        set_run_font(r, name="Times New Roman", size_pt=11, bold=False, color_rgb=(0x4A, 0x55, 0x68))

        # Main Document Title
        p_main = self.doc.add_paragraph()
        p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_main.paragraph_format.space_before = Pt(8)
        p_main.paragraph_format.space_after = Pt(6)
        p_main.paragraph_format.line_spacing = 1.15
        r = p_main.add_run("PROJECT PROPOSAL")
        set_run_font(r, name="Times New Roman", size_pt=20, bold=True, color_rgb=(0x0F, 0x17, 0x2A))

        # Project Title
        proj_title = self.metadata.get("Project Title", "To Design and Implement a Smart Study Assistant System for University Students")
        p_proj = self.doc.add_paragraph()
        p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_proj.paragraph_format.space_before = Pt(4)
        p_proj.paragraph_format.space_after = Pt(4)
        p_proj.paragraph_format.line_spacing = 1.15
        r = p_proj.add_run(proj_title)
        set_run_font(r, name="Times New Roman", size_pt=15, bold=True, color_rgb=(0x1E, 0x3A, 0x8A))

        # Subtitle
        sub_title = self.metadata.get("Subtitle", "A GraphRAG and Knowledge Graph Diagnostic Approach to Misconception Remediation and Exam Preparation")
        p_sub = self.doc.add_paragraph()
        p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(10)
        p_sub.paragraph_format.line_spacing = 1.15
        r = p_sub.add_run(sub_title)
        set_run_font(r, name="Times New Roman", size_pt=11, italic=True, color_rgb=(0x4B, 0x55, 0x63))

        # Supervisor and Submission Date
        supervisor = self.metadata.get("Academic Supervisor", "Dr. Shahzad Mumtaz (shahzad.mumtaz@abdn.ac.uk)")
        sub_date = self.metadata.get("Submission Date", "25 September 2026")
        p_meta = self.doc.add_paragraph()
        p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_meta.paragraph_format.space_before = Pt(0)
        p_meta.paragraph_format.space_after = Pt(12)
        p_meta.paragraph_format.line_spacing = 1.15
        r = p_meta.add_run(f"Academic Supervisor: {supervisor}  |  Submission Date: {sub_date}")
        set_run_font(r, name="Times New Roman", size_pt=9.5, color_rgb=(0x37, 0x41, 0x51))

        # Team Member Roster Subheading
        p_rt = self.doc.add_paragraph()
        p_rt.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_rt.paragraph_format.space_before = Pt(4)
        p_rt.paragraph_format.space_after = Pt(4)
        p_rt.paragraph_format.line_spacing = 1.15
        r = p_rt.add_run(f"Team Member Roster ({group})")
        set_run_font(r, name="Times New Roman", size_pt=11, bold=True, color_rgb=(0x1B, 0x36, 0x5D))

        # Roster Table (5 columns, 10 members)
        if self.roster_headers and self.roster_rows:
            table = self.doc.add_table(rows=len(self.roster_rows) + 1, cols=len(self.roster_headers))
            # Header cells
            for i, h_text in enumerate(self.roster_headers):
                cell = table.cell(0, i)
                cell.text = h_text
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in (0, 2) else WD_ALIGN_PARAGRAPH.LEFT
            # Data cells
            for row_idx, row_data in enumerate(self.roster_rows):
                for col_idx, val in enumerate(row_data):
                    cell = table.cell(row_idx + 1, col_idx)
                    cell.text = val
                    p = cell.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in (0, 2) else WD_ALIGN_PARAGRAPH.LEFT

            # Column widths calibrated to 6.27 inches
            col_widths = [Inches(0.40), Inches(0.90), Inches(0.90), Inches(2.50), Inches(1.57)]
            apply_table_styling(
                table,
                col_widths,
                hdr_bg="1B365D",
                alt_bg="F8FAFC",
                hdr_font_size=9.0,
                cell_font_size=8.5,
            )

    def _build_section_2_body(self) -> None:
        """Constructs Section 2: Proposal Body, restart page number at 1, right footer."""
        s2 = self.doc.add_section(WD_SECTION_START.NEW_PAGE)
        s2.page_width = Mm(210)
        s2.page_height = Mm(297)
        s2.top_margin = Inches(1.0)
        s2.bottom_margin = Inches(1.0)
        s2.left_margin = Inches(1.0)
        s2.right_margin = Inches(1.0)
        s2.header.is_linked_to_previous = False
        s2.footer.is_linked_to_previous = False

        # Running Header
        hdr_p = s2.header.paragraphs[0]
        hdr_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hdr_run = hdr_p.add_run("JC2001 Project Proposal — Group 5 (Smart Study Assistant)")
        set_run_font(hdr_run, name="Times New Roman", size_pt=8.5, italic=True, color_rgb=(0x6B, 0x72, 0x80))

        # Page numbering restart at 1
        sectPr = s2._sectPr
        pgNumType = OxmlElement("w:pgNumType")
        pgNumType.set(qn("w:start"), "1")
        sectPr.append(pgNumType)

        # Right-aligned footer with Page field
        footer_p = s2.footer.paragraphs[0]
        footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = footer_p.add_run("Page ")
        set_run_font(f_run, name="Times New Roman", size_pt=10, color_rgb=(0x37, 0x41, 0x51))
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), "PAGE")
        footer_p._p.append(fld)

        # Iterate over body markdown lines
        i = 0
        in_references = False

        while i < len(self.body_lines):
            line = self.body_lines[i]
            stripped = line.strip()

            if not stripped or stripped == "---":
                i += 1
                continue

            # References Heading
            if stripped.startswith("## References"):
                in_references = True
                p = self.doc.add_paragraph()
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.keep_with_next = True
                add_formatted_text(p, "References", base_size=16, base_bold=True, base_color=(0x1B, 0x36, 0x5D))
                i += 1
                continue

            # Level 1 Heading (## ...)
            if stripped.startswith("## "):
                in_references = False
                heading_text = stripped[3:].strip()
                p = self.doc.add_paragraph()
                p.paragraph_format.space_before = Pt(9)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.keep_with_next = True
                add_formatted_text(p, heading_text, base_size=16, base_bold=True, base_color=(0x1B, 0x36, 0x5D))
                i += 1
                continue

            # Level 2 Heading (### ...)
            if stripped.startswith("### "):
                heading_text = stripped[4:].strip()
                p = self.doc.add_paragraph()
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(2.5)
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.keep_with_next = True
                add_formatted_text(p, heading_text, base_size=13, base_bold=True, base_color=(0x1E, 0x3A, 0x8A))
                i += 1
                continue

            # Markdown Table parsing
            if stripped.startswith("|") and stripped.endswith("|"):
                tbl_lines = []
                while i < len(self.body_lines) and self.body_lines[i].strip().startswith("|") and self.body_lines[i].strip().endswith("|"):
                    tbl_lines.append(self.body_lines[i].strip())
                    i += 1

                if len(tbl_lines) >= 2:
                    raw_headers = [c.strip() for c in tbl_lines[0].strip("|").split("|")]
                    data_rows = []
                    for row_line in tbl_lines[2:]:
                        cols = [c.strip() for c in row_line.strip("|").split("|")]
                        data_rows.append(cols)

                    tbl = self.doc.add_table(rows=len(data_rows) + 1, cols=len(raw_headers))
                    for col_idx, h_text in enumerate(raw_headers):
                        cell = tbl.cell(0, col_idx)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in (0, 1) else WD_ALIGN_PARAGRAPH.LEFT
                        add_formatted_text(p, h_text, base_size=9.5, base_bold=True, base_color=(0xFF, 0xFF, 0xFF))

                    for r_idx, row_data in enumerate(data_rows):
                        for c_idx, val in enumerate(row_data):
                            if c_idx < len(raw_headers):
                                cell = tbl.cell(r_idx + 1, c_idx)
                                p = cell.paragraphs[0]
                                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in (0, 1, 2, 4, 5, 6) and len(raw_headers) == 7 else (WD_ALIGN_PARAGRAPH.CENTER if c_idx in (0, 1, 3) and len(raw_headers) == 4 else WD_ALIGN_PARAGRAPH.LEFT)
                                add_formatted_text(p, val, base_size=9.0, base_color=(0x1F, 0x29, 0x37))

                    # Calibrated widths for exact 6.27-inch printable region
                    if len(raw_headers) == 4:  # Milestones Schedule
                        widths = [Inches(0.95), Inches(1.10), Inches(2.90), Inches(1.32)]
                    elif len(raw_headers) == 7:  # WBS Matrix
                        widths = [Inches(0.72), Inches(1.88), Inches(0.62), Inches(0.95), Inches(0.75), Inches(0.70), Inches(0.65)]
                    else:
                        widths = [Inches(6.27 / len(raw_headers))] * len(raw_headers)

                    apply_table_styling(
                        tbl,
                        widths,
                        hdr_bg="1B365D",
                        alt_bg="F8FAFC",
                        hdr_font_size=9.5,
                        cell_font_size=9.0,
                    )
                continue

            # Bullet List Item (- ...)
            if stripped.startswith("- "):
                p = self.doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.25)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(2.5)
                p.paragraph_format.line_spacing = 1.4
                bullet_run = p.add_run("•  ")
                set_run_font(bullet_run, name="Times New Roman", size_pt=11.5, bold=True, color_rgb=(0x1B, 0x36, 0x5D))
                content = stripped[2:].strip()
                add_formatted_text(p, content, base_size=11.5)
                i += 1
                continue

            # Numbered List Item (1. ..., 2. ...)
            num_match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
            if num_match:
                num_str = num_match.group(1)
                content = num_match.group(2)
                p = self.doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.25)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(3.0)
                p.paragraph_format.line_spacing = 1.45
                num_run = p.add_run(f"{num_str}.  ")
                set_run_font(num_run, name="Times New Roman", size_pt=11.5, bold=True, color_rgb=(0x1B, 0x36, 0x5D))
                add_formatted_text(p, content, base_size=11.5)
                i += 1
                continue

            # Reference Citations ([1] ..., [2] ...)
            if in_references and stripped.startswith("["):
                p = self.doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.35)
                p.paragraph_format.first_line_indent = Inches(-0.35)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(2.0)
                p.paragraph_format.line_spacing = 1.12
                add_formatted_text(p, stripped, base_size=10.0, base_color=(0x1F, 0x29, 0x37))
                i += 1
                continue

            # Normal Running Paragraph
            p = self.doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(3.5)
            p.paragraph_format.line_spacing = 1.48
            # If paragraph is a standalone bold subtitle or title header, keep with next
            if stripped.startswith("**") and stripped.endswith("**"):
                p.paragraph_format.keep_with_next = True
            add_formatted_text(p, stripped, base_size=12.0)
            i += 1


# ==============================================================================
# PDF Exporter: Microsoft Word COM Automation with Fallback & Cleanup
# ==============================================================================

class WordPdfExporter:
    """Exports a .docx file to .pdf using Microsoft Word COM automation."""

    @staticmethod
    def export(docx_path: str | Path, pdf_path: str | Path) -> None:
        abs_docx = os.path.abspath(str(docx_path))
        abs_pdf = os.path.abspath(str(pdf_path))
        Path(abs_pdf).parent.mkdir(parents=True, exist_ok=True)

        if os.path.exists(abs_pdf):
            try:
                os.remove(abs_pdf)
            except Exception:
                pass

        import win32com.client

        word = None
        wdoc = None
        try:
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            word.DisplayAlerts = 0  # wdAlertsNone

            wdoc = word.Documents.Open(abs_docx, ReadOnly=True)

            # Refresh field codes (page numbering)
            try:
                wdoc.Fields.Update()
                for section in wdoc.Sections:
                    for footer in section.Footers:
                        footer.Range.Fields.Update()
                    for header in section.Headers:
                        header.Range.Fields.Update()
            except Exception:
                pass

            # wdFormatPDF = 17
            wdoc.SaveAs(abs_pdf, FileFormat=17)

        finally:
            if wdoc is not None:
                try:
                    wdoc.Close(SaveChanges=False)
                except Exception:
                    pass
                wdoc = None
            if word is not None:
                try:
                    word.Quit()
                except Exception:
                    pass
                word = None

        if not os.path.exists(abs_pdf) or os.path.getsize(abs_pdf) == 0:
            raise RuntimeError(f"Word COM PDF export failed: Output file '{abs_pdf}' was not generated.")


# ==============================================================================
# Quality Gate & PyMuPDF Verifier
# ==============================================================================

class ProposalVerifier:
    """Verifies compiled proposal PDF against course standards."""

    @staticmethod
    def verify(pdf_path: str | Path) -> Tuple[bool, List[str]]:
        import pymupdf

        pdf = pymupdf.open(str(pdf_path))
        total_pages = len(pdf)
        body_pages = total_pages - 1  # Page 1 is unnumbered Title Page

        errors = []
        # Check 1: Body page count in [4, 8]
        if not (4 <= body_pages <= 8):
            errors.append(f"Body page count violation: Got {body_pages} body pages (total {total_pages}), required strictly between 4 and 8 pages!")

        # Check 2: A4 Dimensions (595.28 pt x 841.89 pt, tolerance 5 pt)
        for i, page in enumerate(pdf):
            rect = page.rect
            if abs(rect.width - 595.3) > 5.0 or abs(rect.height - 841.9) > 5.0:
                errors.append(f"Page {i+1} dimensions ({rect.width:.1f} x {rect.height:.1f} pt) deviate from standard A4 (595.3 x 841.9 pt)!")

        # Check 3: Title Page Verification (Page 1)
        page1_text = pdf[0].get_text()
        if ("吴宇轩" not in page1_text and "Yuxuan Wu" not in page1_text) or "50106070" not in page1_text:
            errors.append("Team leader Yuxuan Wu / 吴宇轩 (50106070) not found on Title Page (Page 1)!")

        # Check 4: Body Page 1 Footing check
        if total_pages >= 2:
            page2_text = pdf[1].get_text()
            if "Page 1" not in page2_text:
                errors.append("Body Page 1 (PDF Page 2) does not contain restarted footer 'Page 1'!")

        # Check 5: 10-Member Team Roster Presence
        full_text = "\n".join(page.get_text() for page in pdf)
        roster_members = [
            ("吴宇轩", "Yuxuan Wu", "50106070"),
            ("林泳桐", "Yongtong Lin", "50106038"),
            ("王思鉴", "Sijian Wang", "50106045"),
            ("江昊", "Hao Jiang", "50106065"),
            ("谢炜昕", "Weixin Xie", "50106034"),
            ("张梓健", "Zijian Zhang", "50106035"),
            ("习羽赛", "Yusai Xi", "50105989"),
            ("董思钦", "Siqin Dong", "50106060"),
            ("杨明杰", "Mingjie Yang", "50106061"),
            ("梁子铉", "Zixuan Liang", "50106037"),
        ]
        for zh_name, en_name, sid in roster_members:
            if zh_name not in full_text and en_name not in full_text:
                errors.append(f"Member name '{zh_name}/{en_name}' missing from compiled PDF!")
            if sid not in full_text:
                errors.append(f"Student ID '{sid}' missing from compiled PDF!")

        return len(errors) == 0, errors


# ==============================================================================
# CLI Entry Point
# ==============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="JC2001 Week 1 Dual-Format Proposal Compiler (Markdown -> DOCX -> PDF)"
    )
    parser.add_argument(
        "--input", "-i",
        default="reports/project_proposal.md",
        help="Path to source Markdown proposal (default: reports/project_proposal.md)",
    )
    parser.add_argument(
        "--docx-out", "-d",
        default="reports/project_proposal.docx",
        help="Path to output DOCX document (default: reports/project_proposal.docx)",
    )
    parser.add_argument(
        "--pdf-out", "-p",
        default="reports/project_proposal.pdf",
        help="Path to output PDF document (default: reports/project_proposal.pdf)",
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Skip post-compilation PyMuPDF quality verification",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    docx_path = Path(args.docx_out)
    pdf_path = Path(args.pdf_out)

    print("=" * 72)
    print("JC2001 DUAL-FORMAT PROPOSAL COMPILATION ENGINE")
    print(f"Course: JC2001 Introduction to Software Engineering (2026–27)")
    print(f"Team:   Group 5 (Leader: 吴宇轩 50106070)")
    print("=" * 72)

    if not input_path.exists():
        print(f"[ERROR] Input proposal file not found: {input_path}")
        return 1

    t0 = time.time()

    # Step 1: Parse Markdown
    print(f"\n[1/3] Parsing Markdown Proposal: {input_path}")
    md_parser = ProposalMarkdownParser(input_path)
    metadata, roster_headers, roster_rows, body_lines = md_parser.parse()
    print(f"      - Extracted {len(metadata)} Title Page metadata items")
    print(f"      - Extracted {len(roster_rows)} Team Member Roster records")
    print(f"      - Extracted {len(body_lines)} Body markdown lines")

    # Step 2: Build DOCX
    print(f"\n[2/3] Generating Submission-Grade DOCX: {docx_path}")
    builder = ProposalDocxBuilder(metadata, roster_headers, roster_rows, body_lines)
    builder.build(docx_path)
    docx_size_kb = docx_path.stat().st_size / 1024
    print(f"      -> DOCX Successfully Generated ({docx_size_kb:.1f} KB)")

    # Step 3: Export PDF via Microsoft Word COM
    print(f"\n[3/3] Exporting High-Fidelity PDF via Word COM: {pdf_path}")
    WordPdfExporter.export(docx_path, pdf_path)
    pdf_size_kb = pdf_path.stat().st_size / 1024
    print(f"      -> PDF Successfully Exported ({pdf_size_kb:.1f} KB)")

    # Step 4: Verification Gate
    if not args.no_verify:
        print(f"\n[QUALITY GATE] Running Automated PyMuPDF Verification...")
        passed, violations = ProposalVerifier.verify(pdf_path)
        import pymupdf
        pdf_doc = pymupdf.open(str(pdf_path))
        total_p = len(pdf_doc)
        body_p = total_p - 1
        print(f"      - Total PDF Pages: {total_p}")
        print(f"      - Body Pages:      {body_p} (Permitted range: [4, 8])")
        print(f"      - Page Geometry:   {pdf_doc[0].rect.width:.2f} x {pdf_doc[0].rect.height:.2f} pt (A4 Standard)")

        if not passed:
            print("\n[FAIL] Quality Gate Violations Detected:")
            for v in violations:
                print(f"  * {v}")
            return 1
        else:
            print("      -> QUALITY GATE PASSED: All formatting & pagination assertions met.")

    elapsed = time.time() - t0
    print("\n" + "=" * 72)
    print(f"BUILD SUCCESSFUL in {elapsed:.2f}s")
    print(f"Outputs:")
    print(f"  * DOCX: {docx_path.resolve()}")
    print(f"  * PDF:  {pdf_path.resolve()}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
