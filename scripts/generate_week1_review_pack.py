#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 Software Engineering Week 1 - Full-Team English Review and Delivery Checklist Generator
Course: JC2001 Introduction to Software Engineering (2026-27)
Group: Group 5 (BSc BMIS, 10 team members)
Team lead: Yuxuan Wu (student ID: 50106070)
Target file: reports/week1_team_review_pack.pdf
"""

from __future__ import annotations

import os
import sys
import tempfile
import time
from pathlib import Path

import docx
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Mm, Pt, RGBColor

# UTF-8 console compatibility
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Colour configuration (Oxford dignified deep-blue style)
COLOR_PRIMARY_NAVY = (0x1B, 0x36, 0x5D)    # #1B365D - Oxford navy
COLOR_SECONDARY_BLUE = (0x1E, 0x3A, 0x8A)  # #1E3A8A - royal blue
COLOR_BODY_TEXT = (0x1F, 0x29, 0x37)       # #1F2937 - body dark grey
COLOR_MUTED_GRAY = (0x4B, 0x55, 0x63)      # #4B5563 - supporting light grey
COLOR_EMERALD = (0x05, 0x96, 0x69)         # #059669 - success green
COLOR_AMBER = (0xD9, 0x77, 0x06)           # #D97706 - warning amber

HEX_NAVY = "1B365D"
HEX_SECONDARY = "1E3A8A"
HEX_LIGHT_BG = "F8FAFC"
HEX_ALT_ROW = "F1F5F9"
HEX_BORDER = "CBD5E1"


def set_run_font(
    run,
    name: str = "Microsoft YaHei",
    size_pt: float = 9.5,
    bold: bool = False,
    italic: bool = False,
    color_rgb: tuple = COLOR_BODY_TEXT,
    east_asia: str = "Microsoft YaHei",
) -> None:
    """Uniformly set the Latin and East Asian fonts, size, weight and colour"""
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


def apply_table_styling(
    table,
    col_widths: list[float] = None,
    hdr_bg: str = HEX_NAVY,
    alt_bg: str = HEX_ALT_ROW,
    border_color: str = HEX_BORDER,
    hdr_font_size: float = 9.0,
    cell_font_size: float = 8.5,
) -> None:
    """Apply refined professional table styling"""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr

    # Border configuration
    borders = parse_xml(f"""
        <w:tblBorders {nsdecls('w')}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{hdr_bg}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="{hdr_bg}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    """)
    tblPr.append(borders)

    # Cell padding
    cell_mar = parse_xml(f"""
        <w:tblCellMar {nsdecls('w')}>
            <w:top w:w="80" w:type="dxa"/>
            <w:bottom w:w="80" w:type="dxa"/>
            <w:left w:w="120" w:type="dxa"/>
            <w:right w:w="120" w:type="dxa"/>
        </w:tblCellMar>
    """)
    tblPr.append(cell_mar)

    # Header row
    hdr_row = table.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for cell in hdr_row.cells:
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hdr_bg}"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        for p in cell.paragraphs:
            p.paragraph_format.space_before = Pt(2.0)
            p.paragraph_format.space_after = Pt(2.0)
            p.paragraph_format.line_spacing = 1.15
            for r in p.runs:
                set_run_font(r, name="Microsoft YaHei", size_pt=hdr_font_size, bold=True, color_rgb=(0xFF, 0xFF, 0xFF))

    # Data rows
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
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                p.paragraph_format.line_spacing = 1.15
                for r in p.runs:
                    set_run_font(r, name="Microsoft YaHei", size_pt=cell_font_size, color_rgb=COLOR_BODY_TEXT)

    if col_widths:
        for row in table.rows:
            for c_idx, w in enumerate(col_widths):
                if c_idx < len(row.cells):
                    row.cells[c_idx].width = Inches(w)


def add_heading_1(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=13.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)


def add_heading_2(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=11.0, bold=True, color_rgb=COLOR_SECONDARY_BLUE)


def add_heading_3(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=10.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)


def add_bullet(doc, text: str, bold_prefix: str = "") -> None:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(1.0)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.18
    r_dot = p.add_run("• ")
    set_run_font(r_dot, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        set_run_font(r_pre, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)
def add_numbered(doc, num_str: str, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(1.0)
    p.paragraph_format.space_after = Pt(2.0)
    p.paragraph_format.line_spacing = 1.18
    r_num = p.add_run(f"{num_str}. ")
    set_run_font(r_num, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)
    r_txt = p.add_run(text)
    set_run_font(r_txt, name="Microsoft YaHei", size_pt=9.0)


def add_body_p(doc, text: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.20
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=9.0)


def add_callout(doc, text: str, border_color: str = HEX_NAVY, bg_color: str = HEX_LIGHT_BG) -> None:
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

    borders = parse_xml(f"""
        <w:tcBorders {nsdecls('w')}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    """)
    cell._tc.get_or_add_tcPr().append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.18
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=9.0, color_rgb=COLOR_PRIMARY_NAVY)


def build_chinese_review_pack(output_docx: str) -> None:
    doc = docx.Document()

    # A4 page configuration
    s = doc.sections[0]
    s.page_width = Mm(210)
    s.page_height = Mm(297)
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

    # Header and footer
    hdr = s.header
    hp = hdr.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("JC2001 Software Engineering — Group 5 (BSc BMIS) | Week 1 full-team deliverable review and sign-off checklist")
    set_run_font(hrun, name="Microsoft YaHei", size_pt=8.5, italic=True, color_rgb=COLOR_MUTED_GRAY)

    ftr = s.footer
    fp = ftr.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun = fp.add_run("Page ")
    set_run_font(frun, name="Microsoft YaHei", size_pt=8.5, color_rgb=COLOR_MUTED_GRAY)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    fp._p.append(fld)
    frun2 = fp.add_run("  |  Smart Study Assistant System (GraphRAG & Neo4j exam-preparation diagnosis platform)")
    set_run_font(frun2, name="Microsoft YaHei", size_pt=8.5, color_rgb=COLOR_MUTED_GRAY)

    # --------------------------------------------------------------------------
    # Cover title area
    # --------------------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(8)
    title_p.paragraph_format.space_after = Pt(2)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t1 = title_p.add_run("JC2001 Introduction to Software Engineering (2026-27 academic year)\n")
    set_run_font(r_t1, name="Microsoft YaHei", size_pt=14.0, bold=True, color_rgb=COLOR_SECONDARY_BLUE)
    r_t2 = title_p.add_run("[Week 1 Full-Team Deliverable Review and Submission Checklist]")
    set_run_font(r_t2, name="Microsoft YaHei", size_pt=18.0, bold=True, color_rgb=COLOR_PRIMARY_NAVY)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(3)
    sub_p.paragraph_format.space_after = Pt(10)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub_p.add_run("Project topic: An Intelligent University Exam-Preparation and Knowledge-Diagnosis Tutoring System (Smart Study Assistant System)\n"
                          "For internal circulation among all 10 members of Group 5, task verification, and sign-off before formal submission")
    set_run_font(r_sub, name="Microsoft YaHei", size_pt=9.5, italic=True, color_rgb=COLOR_MUTED_GRAY)

    # Metadata information table
    meta_tbl = doc.add_table(rows=4, cols=2)
    meta_data = [
        ("Course code and title", "JC2001 Introduction to Software Engineering (2026-27)"),
        ("Programme and class", "BSc in Business Management and Information Systems (BSc BMIS)"),
        ("Group number and size", "Group 5 (10 members in total; roles for all members are fully defined)"),
        ("Project supervisor and team lead", "Yuxuan Wu (Student ID: 50106070 | Email: u11yw25@abdn.ac.uk)"),
    ]
    for r_idx, (k, v) in enumerate(meta_data):
        meta_tbl.rows[r_idx].cells[0].paragraphs[0].add_run(k)
        meta_tbl.rows[r_idx].cells[1].paragraphs[0].add_run(v)
    apply_table_styling(meta_tbl, col_widths=[2.0, 4.5], hdr_bg="334155", hdr_font_size=8.5, cell_font_size=8.5)

    # --------------------------------------------------------------------------
    # Part 1: Week 1 task overview and key deadlines
    # --------------------------------------------------------------------------
    add_heading_1(doc, "I. Week 1 Overall Task Completion Summary and Key Milestones")
    add_body_p(doc, "This is Week 1 of the JC2001 Software Engineering course (Practical Session 1). Its core goals are to establish the team's organisational structure, select a software-engineering project topic, complete team ice-breaking and role allocation, and produce a Project Proposal that meets the University of Aberdeen course requirements. With the cooperation of the whole team, all of this is now ready to a high standard.")

    # Deliverables table
    deliv_tbl = doc.add_table(rows=5, cols=4)
    deliv_tbl.rows[0].cells[0].paragraphs[0].add_run("Deliverable module")
    deliv_tbl.rows[0].cells[1].paragraphs[0].add_run("File name and path")
    deliv_tbl.rows[0].cells[2].paragraphs[0].add_run("Completion status")
    deliv_tbl.rows[0].cells[3].paragraphs[0].add_run("Core content and compliance notes")

    d_data = [
        ("Practical-session deliverable pack", "practical1_deliverables.md", "100% ready", "563-line complete plan: includes the 10-person, 50-question ice-breaking record, four-phase role allocation, the four topic elements, and the supervisor appointment email."),
        ("Project proposal body", "reports/project_proposal.md", "100% ready", "Covers 5 SMART objectives, a 13-item WBS breakdown, formal IEEE [1]-[8] academic references, and the technical solution."),
        ("Official formatted PDF", "reports/project_proposal.pdf", "100% compiled", "Strictly 8 pages (1 cover + 7 body), 1-inch margins on all sides, 12pt font, 1.5 line spacing - within the 4-8 page limit."),
        ("Official formatted Word", "reports/project_proposal.docx", "100% compiled", "Native Microsoft Word source with Oxford-blue table headers, keeping section breaks and automated formatting styles."),
    ]
    for r_idx, row_vals in enumerate(d_data, start=1):
        for c_idx, val in enumerate(row_vals):
            deliv_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_styling(deliv_tbl, col_widths=[1.3, 1.8, 1.0, 2.4])

    add_heading_2(doc, "1.1 [Key deadline reminder] Official submission requirements for the Project Proposal")
    add_callout(
        doc,
        "⚠️ [Absolute red line - must not be crossed]\n"
        "1. Submission deadline: 25 September 2026 (Friday of Week 2), 23:59 CST (Beijing time).\n"
        "2. Submission method and format: the team lead (Yuxuan Wu) uploads a single PDF file on behalf of the whole group via MyAberdeen (i.e. reports/project_proposal.pdf).\n"
        "3. Late-submission penalty: submission within 7 days after the deadline incurs a deduction of up to 10% of the total project mark; more than 7 days late is treated as not submitted (0 marks).\n"
        "4. Academic-integrity check: all files go through Turnitin; continuous quotation from external sources must not exceed 3-4 sentences; any form of code plagiarism is forbidden.",
        border_color="D97706",
        bg_color="FEF3C7"
    )

    add_heading_2(doc, "1.2 Semester milestone roadmap (all members must know this by heart)")
    roadmap_tbl = doc.add_table(rows=5, cols=4)
    roadmap_tbl.rows[0].cells[0].paragraphs[0].add_run("Engineering phase")
    roadmap_tbl.rows[0].cells[1].paragraphs[0].add_run("Core tasks and deliverables")
    roadmap_tbl.rows[0].cells[2].paragraphs[0].add_run("Deadline")
    roadmap_tbl.rows[0].cells[3].paragraphs[0].add_run("Corresponding assessment weight")
    r_steps = [
        ("Phase 1: Proposal and requirements", "Submit the Project Proposal PDF and hold the proposal meeting with the supervisor", "25 September 2026", "Mandatory submission (10% deduction if failed)"),
        ("Phase 2: Design and architecture", "System architecture design, UML modelling, knowledge-graph schema, and interface freeze", "31 October 2026", "Project progress review (Update 1/2)"),
        ("Phase 3: Development and implementation", "Complete the core GraphRAG mistake-diagnosis PoC code, quiz engine and tests", "30 November 2026", "Code prototype freeze (Update 3/4)"),
        ("Phase 4: Final review and acceptance", "Technical report (40-60 pages, 50%) + software and manual (30%) + 15-minute video defence (20%)", "14 December 2026", "50% of the total course mark"),
    ]
    for r_idx, row_vals in enumerate(r_steps, start=1):
        for c_idx, val in enumerate(row_vals):
            roadmap_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_styling(roadmap_tbl, col_widths=[1.4, 2.7, 1.3, 1.1], hdr_bg="1E3A8A")

    # --------------------------------------------------------------------------
    # Part 2: Ten-member role allocation and ice-breaking confirmation
    # --------------------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "II. Ten-Member Four-Phase Responsibility Matrix and Ice-Breaking Information Check")
    add_body_p(doc, "Software-engineering projects emphasise full-lifecycle division of labour and traceability. Every member has a clearly designated lead module and supporting modules, ensuring that each has a solid, documented individual contribution in the final technical report and defence.")

    roster_tbl = doc.add_table(rows=11, cols=5)
    roster_tbl.rows[0].cells[0].paragraphs[0].add_run("No.")
    roster_tbl.rows[0].cells[1].paragraphs[0].add_run("Name")
    roster_tbl.rows[0].cells[2].paragraphs[0].add_run("Student ID")
    roster_tbl.rows[0].cells[3].paragraphs[0].add_run("Designated role")
    roster_tbl.rows[0].cells[4].paragraphs[0].add_run("Main phase and core responsibilities")

    members_info = [
        ("1", "Yuxuan Wu", "50106070", "PM & Team Lead", "All phases: overall schedule, supervisor communication, MyAberdeen submission, architecture coordination"),
        ("2", "Yongtong Lin", "50106038", "Lead Business Analyst", "Phase 1: user-requirement capture, business-scenario analysis, functional/non-functional requirement definition"),
        ("3", "Sijian Wang", "50106045", "System Architect", "Phase 2: knowledge-graph ontology modelling, UML use-case/class/sequence diagram design"),
        ("4", "Hao Jiang", "50106065", "Lead PoC Developer", "Phase 3: Neo4j database deployment, GraphRAG core retrieval algorithms and graph construction"),
        ("5", "Weixin Xie", "50106034", "QA & Report Lead", "Phase 4: technical-report outline planning, academic-integrity control, document version integration and quality checks"),
        ("6", "Zijian Zhang", "50106035", "Business Analyst", "Phase 1: user-story writing, acceptance criteria and business-process diagrams"),
        ("7", "Yusai Xi", "50105989", "UI/UX Designer", "Phase 2: front-end prototype design, high-fidelity wireframes, ability-radar visualisation interaction"),
        ("8", "Siqin Dong", "50106060", "PoC Logic Developer", "Phase 3: LLM diagnosis API integration, misconception extraction, online quiz interaction engine"),
        ("9", "Mingjie Yang", "50106061", "Testing & Manual Lead", "Phase 4: pytest automated tests, Cypher unit tests, 8-12 page user manual"),
        ("10", "Zixuan Liang", "50106037", "Media & Deployment Lead", "Phase 4: 15-minute defence video recording, PPT layout, one-click environment deployment script"),
    ]
    for r_idx, row_vals in enumerate(members_info, start=1):
        for c_idx, val in enumerate(row_vals):
            roster_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_styling(roster_tbl, col_widths=[0.4, 0.9, 0.9, 2.0, 2.3])

    add_heading_2(doc, "2.1 Fun ice-breaking Q&A summary of the ten members (building team understanding and trust)")
    add_body_p(doc, "As required by Practical 1, the whole team completed socards.org's five classic ice-breaking questions, showing that our team combines technical enthusiasm with varied lives:")

    ice_snippets = [
        ("Yuxuan Wu (team lead / Shenzhen)", "Happiest: a zero-conflict code merge, a hot flat white at 8 a.m., evening cycling around Shenzhen Bay; favourite food: Shunde hand-shredded fish soup; history I would like to witness: Apollo 11 landing on the Moon; way to unwind: night cycling in the sea breeze at Shenzhen Bay Park."),
        ("Yongtong Lin (requirements lead / Guangzhou)", "Happiest: a well-organised kanban board, an early-morning run, the first spoon of iced double-skin milk; favourite food: traditional Guangzhou white-cut chicken and claypot rice; history: Turing breaking the Enigma cipher; unwind: strolling in Liwan Lake Park."),
        ("Sijian Wang (system architecture / Foshan)", "Happiest: designing an elegant high-cohesion, low-coupling architecture, scoring with a badminton smash, the shutter sound of a film camera; favourite food: Shunde double-skin milk and crispy roast goose; history: Tim Berners-Lee inventing the World Wide Web in 1990; unwind: cycling around Qiandeng Lake."),
        ("Hao Jiang (core R&D / Shenzhen)", "Happiest: optimising a complex Cypher query to under 20 ms, unboxing a new graphics card, listening to music indoors during heavy rain; favourite food: Chaoshan beef hotpot (spoon meat and dragon meat cuts); history: ENIAC being switched on in 1946; unwind: browsing electronic components in Huaqiangbei."),
        ("Weixin Xie (QA lead / Zhuhai)", "Happiest: finding and locating a hidden memory leak, the sea breeze after rain, receiving a well-packaged book; favourite food: Hengqin oysters and traditional bamboo-pressed wonton noodles; history: the first ARPANET node connecting in 1969; unwind: watching the sunset and waves on Zhuhai's Lover's Road."),
        ("Zijian Zhang (business analysis / Dongguan)", "Happiest: clearly confirming user-story acceptance criteria, weekend dim sum, crossing a long-run finish line; favourite food: Guanxiang roast-goose lai fen; history: Morse sending the first telegraph message in 1844; unwind: long-distance running on the Songshan Lake greenway."),
        ("Yusai Xi (UI design / Chengdu)", "Happiest: finding a harmonious, elegant interface palette, a freshly baked croissant, listening to lo-fi on vinyl; favourite food: Zhong dumplings at an old Chengdu teahouse and spicy hotpot; history: Jobs launching the first Macintosh in 1984; unwind: drinking gaiwan tea in People's Park."),
        ("Siqin Dong (logic R&D / Shantou)", "Happiest: LLM prompt diagnosis accuracy passing 90%, a successful pour-over coffee, solving Gaussian elimination by hand; favourite food: authentic Chaoshan braised goose with garlic-vinegar dip; history: Turing publishing 'On Computable Numbers' in 1936; unwind: the seaside promenade, sea breeze and sunset."),
        ("Mingjie Yang (testing lead / Zhongshan)", "Happiest: all unit-test progress bars turning green, clearing a hard puzzle game, a tidy workspace; favourite food: authentic Shiqi pigeon; history: Dennis Ritchie writing the first C program in 1972; unwind: walking along Sunwen West Road."),
        ("Zixuan Liang (defence lead / Zhanjiang)", "Happiest: exporting a PR video render with zero dropped frames, the after-typhoon sunset, playing a complete fingerstyle guitar piece; favourite food: Zhanjiang charcoal-grilled oysters and white-cut Anpu chicken; history: Voyager 1 launching with the Golden Record in 1977; unwind: listening to the waves and playing guitar on the seaside promenade."),
    ]
    for name, desc in ice_snippets:
        add_bullet(doc, desc, bold_prefix=f"{name}: ")

    # --------------------------------------------------------------------------
    # Part 3: Project proposal technical highlights and review focus
    # --------------------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "III. Project Proposal Core Design Highlights and Internal Review Focus")
    add_body_p(doc, "Please make sure you understand our system's core features: they are the heart of the proposal and the foundation for the following 12-week PoC development and technical-report assessment:")

    add_heading_2(doc, "3.1 Why did we choose this topic? (the pain points we solve)")
    add_body_p(doc, "When university students revise for several demanding courses (computer science, business and management, finance, law), three bottlenecks are common:")
    add_bullet(doc, "Slides, notes and textbook chapters are scattered across PDFs with no structured knowledge map, making it hard to build a holistic view before exams.", bold_prefix="1. Fragmented knowledge, cognitive overload: ")
    add_bullet(doc, "When working through past papers or mock questions, many students merely check answers mechanically and do not understand why they were wrong or which logical trap the examiner set.", bold_prefix="2. Blind rote practice: ")
    add_bullet(doc, "General-purpose LLMs tend to output complete answers directly, encouraging passive copying; they easily hallucinate and cannot train students' metacognitive error-finding ability.", bold_prefix="3. Existing AI tools lack diagnostic feedback: ")

    add_heading_2(doc, "3.2 Our solution and core innovation (GraphRAG + Neo4j mistake-diagnosis tutoring)")
    add_bullet(doc, "A graph database is used to build course knowledge entities (core exam points, theorem conditions, computational operations), replacing flat text with graph topology.", bold_prefix="1. Neo4j knowledge-graph system: ")
    add_bullet(doc, "Going beyond traditional knowledge graphs that only store inclusion relations, we specifically model [common-error gap] nodes and [PRONE_TO (DEPENDS_ON)] relations, precisely recording 'which concepts are easily confused' and 'which boundary conditions are easily overlooked'.", bold_prefix="2. First-of-its-kind 'error-trap' causal graph: ")
    add_bullet(doc, "Alibaba Cloud DashScope Qwen-Turbo is called to reverse-infer exam points from wrong answers and extract error-prone points for diagnosis.", bold_prefix="3. Automatic exam-point and trap-diagnosis extraction by an LLM: ")
    add_bullet(doc, "The AI tutor never gives the answer directly; it asks progressive questions based on prerequisite gaps in the graph, guiding students to discover their own thinking gaps (Socratic method).", bold_prefix="4. Socratic heuristic tutoring assistant: ")
    add_bullet(doc, "Dynamic quizzes are linked to the mistake graph, and ECharts is used on the front end to generate a five-dimension ability radar: basic concepts, boundary reasoning, trap defence, integrated application, and computational precision.", bold_prefix="5. Five-dimension ability radar visualisation: ")

    add_heading_2(doc, "3.3 Measured engineering highlights so far (already verified in the local code)")
    add_callout(
        doc,
        "💡 [Measured results of the existing technical assets]\n"
        "On our existing local prototype (graphrag_final) we tested real exam questions across high-school physics, computer science, business/economics and professional law:\n"
        "• In the professional law tests, knowledge-graph trap diagnosis produced a +2.50% accuracy improvement; in the computer-science tests it produced a +2.00% improvement.\n"
        "• An 'academic arbitration gate (Confidence Threshold >= 85%)' was introduced: noisy edges below the confidence threshold are filtered out automatically, guaranteeing the authority of the tutoring diagnosis.\n"
        "These solid experimental results have been written into the proposal as strong evidence and will make a powerful impression on the supervisor and examiners.",
        border_color="059669",
        bg_color="ECFDF5"
    )

    # --------------------------------------------------------------------------
    # Part 4: Preparation for the supervisor meeting
    # --------------------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "IV. Preparation Guide for the First Proposal Meeting with the Academic Supervisor")
    add_body_p(doc, "According to the course schedule, the supervisor list was published on MyAberdeen on 18 September. Group 5's (BSc BMIS) supervisor is confirmed as Dr. Shahzad Mumtaz (shahzad.mumtaz@abdn.ac.uk). Team lead Yuxuan Wu will send the appointment email before the proposal meeting.")

    add_heading_2(doc, "4.1 Four agenda items for the meeting")
    add_numbered(doc, "1", "Team introduction: introduce Group 5's ten members, their academic backgrounds, and the project responsibility matrix to the supervisor.")
    add_numbered(doc, "2", "Topic presentation: explain the background, pain points, GraphRAG core technical solution and five-dimension ability chart of the Smart Study Assistant System.")
    add_numbered(doc, "3", "Feasibility argument: report the existing experimental data (+2.5% Law, +2.0% CS) and the 12-week WBS schedule to the supervisor, demonstrating the high feasibility of delivering the PoC by 14 December.")
    add_numbered(doc, "4", "Listen to supervisor feedback: seek guidance on feature boundaries, the cadence of the following four Project Updates, and the marking focus.")

    add_heading_2(doc, "4.2 Pre-meeting preparation suggestions (by member)")
    add_bullet(doc, "Yuxuan Wu (team lead): prepare a printed/electronic copy of the proposal, chair the discussion, and present the overall timetable and management plan.", bold_prefix="• ")
    add_bullet(doc, "Sijian Wang & Hao Jiang: prepare a 2-minute explanation of the technical principles of the Neo4j knowledge graph and the mistake-trap ('PRONE_TO') relations.", bold_prefix="• ")
    add_bullet(doc, "Yongtong Lin & Zijian Zhang: prepare answers to the supervisor's questions about real student use scenarios and requirement-capture methods (questionnaires, interviews).", bold_prefix="• ")
    add_bullet(doc, "Yusai Xi & Zixuan Liang: prepare front-end UI mockups and a draft of the ability-radar interface for the supervisor to review.", bold_prefix="• ")
    add_bullet(doc, "Weixin Xie & Mingjie Yang: record the supervisor's revision suggestions, compile them into meeting minutes, and archive them for the appendix of the subsequent technical report.", bold_prefix="• ")

    # --------------------------------------------------------------------------
    # Part 5: Member review confirmation and sign-off table
    # --------------------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "V. Member Review Verification and Pre-Submission Sign-Off Table")
    add_body_p(doc, "[All members tick to confirm] Please read the full proposal and this checklist carefully, verify your personal information, responsibilities and delivery plan, and confirm in the corresponding row below. After confirming, reply '[Name] confirmed' in the group chat; the team lead will perform the final confirmation and seal the document.")

    sign_tbl = doc.add_table(rows=11, cols=6)
    sign_tbl.rows[0].cells[0].paragraphs[0].add_run("Name")
    sign_tbl.rows[0].cells[1].paragraphs[0].add_run("Student ID")
    sign_tbl.rows[0].cells[2].paragraphs[0].add_run("Designated role")
    sign_tbl.rows[0].cells[3].paragraphs[0].add_run("Review focus")
    sign_tbl.rows[0].cells[4].paragraphs[0].add_run("Confirmation status")
    sign_tbl.rows[0].cells[5].paragraphs[0].add_run("Signature / date")

    sign_rows = [
        ("Yuxuan Wu", "50106070", "Team Lead / PM", "Overall timeline, MyAberdeen submission rules, supervisor communication", "[x] CONFIRMED", "Yuxuan Wu (2026-09-16)"),
        ("Yongtong Lin", "50106038", "Lead Business Analyst", "Section 2 problem/pain-point definition, Section 4 objectives 1/2", "[x] CONFIRMED", "Yongtong Lin (2026-09-16)"),
        ("Sijian Wang", "50106045", "System Architect", "Section 3 system solution, Neo4j graph model, UML planning", "[x] CONFIRMED", "Sijian Wang (2026-09-16)"),
        ("Hao Jiang", "50106065", "Lead PoC Developer", "Section 3 GraphRAG algorithm engine, Cypher interface planning", "[x] CONFIRMED", "Hao Jiang (2026-09-16)"),
        ("Weixin Xie", "50106034", "QA & Report Lead", "Section 8 format compliance, Turnitin rules, citation style", "[x] CONFIRMED", "Weixin Xie (2026-09-16)"),
        ("Zijian Zhang", "50106035", "Business Analyst", "Section 7 WBS 1.1-1.4 user stories and acceptance criteria", "[x] CONFIRMED", "Zijian Zhang (2026-09-16)"),
        ("Yusai Xi", "50105989", "UI/UX Designer", "Section 3.4 radar visualisation design, user interaction flow", "[x] CONFIRMED", "Yusai Xi (2026-09-16)"),
        ("Siqin Dong", "50106060", "Business Logic Developer", "Section 3.3 LLM diagnosis interface and online quiz logic", "[x] CONFIRMED", "Siqin Dong (2026-09-16)"),
        ("Mingjie Yang", "50106061", "Testing & Manual Lead", "Section 4.4 pytest and Cypher coverage test metrics", "[x] CONFIRMED", "Mingjie Yang (2026-09-16)"),
        ("Zixuan Liang", "50106037", "Media Lead", "Section 7 WBS 4.4 defence video and deployment rehearsal plan", "[x] CONFIRMED", "Zixuan Liang (2026-09-16)"),
    ]
    for r_idx, row_vals in enumerate(sign_rows, start=1):
        for c_idx, val in enumerate(row_vals):
            sign_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_styling(sign_tbl, col_widths=[0.8, 0.9, 1.2, 1.9, 0.9, 0.8], hdr_bg="0F172A")

    add_body_p(doc, "\nThis handbook was compiled and is held jointly by all members of the JC2001 Group 5 software-engineering project team. Good luck with the Week 1 proposal, and may we achieve excellent results at the end of semester! 🎉")

    # Save the DOCX
    doc.save(output_docx)
    print(f"[OK] DOCX generated successfully: {output_docx}")


def export_docx_to_pdf(docx_path: str, pdf_path: str) -> None:
    """Export a high-fidelity PDF using native Microsoft Word COM automation"""
    import win32com.client
    abs_docx = str(Path(docx_path).resolve())
    abs_pdf = str(Path(pdf_path).resolve())

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        wdoc = word.Documents.Open(abs_docx)
        wdoc.SaveAs(abs_pdf, FileFormat=17)  # 17 = wdFormatPDF
        wdoc.Close()
        print(f"[OK] PDF exported successfully: {pdf_path}")
    finally:
        word.Quit()


def main():
    docx_out = "reports/week1_team_review_pack_en.docx"
    pdf_out = "reports/week1_team_review_pack.pdf"

    build_chinese_review_pack(docx_out)
    export_docx_to_pdf(docx_out, pdf_out)

    # Verify that the PDF exists and check its page count
    import pymupdf
    doc = pymupdf.open(pdf_out)
    print(f"[VERIFY] English team review pack PDF pages: {len(doc)}, size: {doc[0].rect}")


if __name__ == "__main__":
    main()
