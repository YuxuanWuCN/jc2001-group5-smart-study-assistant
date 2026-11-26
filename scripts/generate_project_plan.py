#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 Software Engineering - Group 5 Project Plan (Project Proposal) official English generator
For team lead Yuxuan Wu to distribute to the ten members for review and engineering alignment
"""

import os
import sys
from pathlib import Path

import docx
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Mm, Pt, RGBColor

# Console UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Classic deep-blue business/academic colour scheme
COLOR_NAVY = (0x1B, 0x36, 0x5D)        # #1B365D -  oxford navy
COLOR_BLUE = (0x1E, 0x3A, 0x8A)        # #1E3A8A - primary blue
COLOR_TEXT = (0x1F, 0x29, 0x37)        # #1F2937 - dark body
COLOR_MUTED = (0x4B, 0x55, 0x63)       # #4B5563 - gray
COLOR_EMERALD = (0x05, 0x96, 0x69)     # #059669 - success green
COLOR_AMBER = (0xD9, 0x77, 0x06)       # #D97706 - warning amber

HEX_NAVY = "1B365D"
HEX_ALT = "F8FAFC"
HEX_BORDER = "CBD5E1"


def set_run_font(run, name="Microsoft YaHei", size_pt=10.0, bold=False, italic=False, color_rgb=COLOR_TEXT):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color_rgb:
        run.font.color.rgb = RGBColor(*color_rgb)
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), name)
    rFonts.set(qn("w:cs"), name)


def apply_table_style(table, col_widths=None, hdr_bg=HEX_NAVY, alt_bg=HEX_ALT):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr

    borders = parse_xml(f"""
        <w:tblBorders {nsdecls('w')}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="{hdr_bg}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="{hdr_bg}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    """)
    tblPr.append(borders)

    cell_mar = parse_xml(f"""
        <w:tblCellMar {nsdecls('w')}>
            <w:top w:w="90" w:type="dxa"/>
            <w:bottom w:w="90" w:type="dxa"/>
            <w:left w:w="120" w:type="dxa"/>
            <w:right w:w="120" w:type="dxa"/>
        </w:tblCellMar>
    """)
    tblPr.append(cell_mar)

    hdr_row = table.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for cell in hdr_row.cells:
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hdr_bg}"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        for p in cell.paragraphs:
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            for r in p.runs:
                set_run_font(r, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=(0xFF, 0xFF, 0xFF))

    for idx, row in enumerate(table.rows[1:], start=1):
        bg = alt_bg if idx % 2 == 0 else "FFFFFF"
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
                    set_run_font(r, name="Microsoft YaHei", size_pt=8.5, color_rgb=COLOR_TEXT)

    if col_widths:
        for row in table.rows:
            for c_idx, w in enumerate(col_widths):
                if c_idx < len(row.cells):
                    row.cells[c_idx].width = Inches(w)


def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=13.0, bold=True, color_rgb=COLOR_NAVY)


def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=11.0, bold=True, color_rgb=COLOR_BLUE)


def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.2
    r_dot = p.add_run("• ")
    set_run_font(r_dot, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=COLOR_NAVY)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        set_run_font(r_pre, name="Microsoft YaHei", size_pt=9.0, bold=True, color_rgb=COLOR_NAVY)
    r_txt = p.add_run(text)
    set_run_font(r_txt, name="Microsoft YaHei", size_pt=9.0)


def add_p(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.22
    r = p.add_run(text)
    set_run_font(r, name="Microsoft YaHei", size_pt=9.0)


def add_callout(doc, text, border_color=HEX_NAVY, bg_color="F8FAFC"):
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
    set_run_font(r, name="Microsoft YaHei", size_pt=9.0, color_rgb=COLOR_NAVY)


def generate_project_plan_docx(docx_path: str):
    doc = docx.Document()

    # A4 page and margins
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
    hrun = hp.add_run("JC2001 Software Engineering — Group 5 (BSc BMIS) | Project Proposal")
    set_run_font(hrun, name="Microsoft YaHei", size_pt=8.5, italic=True, color_rgb=COLOR_MUTED)

    ftr = s.footer
    fp = ftr.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun1 = fp.add_run("Page ")
    set_run_font(frun1, name="Microsoft YaHei", size_pt=8.5, color_rgb=COLOR_MUTED)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    fp._p.append(fld)
    frun2 = fp.add_run("  |  An Intelligent University Exam-Preparation and Knowledge-Diagnosis Tutoring System (Smart Study Assistant)")
    set_run_font(frun2, name="Microsoft YaHei", size_pt=8.5, color_rgb=COLOR_MUTED)

    # Cover title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(3)
    r_sub = p_title.add_run("JC2001 Introduction to Software Engineering (2026-27 academic year)\n")
    set_run_font(r_sub, name="Microsoft YaHei", size_pt=14.0, bold=True, color_rgb=COLOR_BLUE)
    r_main = p_title.add_run("[Software Engineering Project Proposal]")
    set_run_font(r_main, name="Microsoft YaHei", size_pt=18.0, bold=True, color_rgb=COLOR_NAVY)

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_before = Pt(4)
    p_proj.paragraph_format.space_after = Pt(12)
    r_proj = p_proj.add_run("Project name: An Intelligent Exam-Preparation and Knowledge-Diagnosis Tutoring System Based on Knowledge Graphs and Large Language Models\n"
                            "Smart Study Assistant System: A GraphRAG & Knowledge Graph Diagnostic Approach")
    set_run_font(r_proj, name="Microsoft YaHei", size_pt=10.0, italic=True, color_rgb=COLOR_MUTED)

    # Team information table
    team_tbl = doc.add_table(rows=11, cols=4)
    team_tbl.rows[0].cells[0].paragraphs[0].add_run("No.")
    team_tbl.rows[0].cells[1].paragraphs[0].add_run("Name")
    team_tbl.rows[0].cells[2].paragraphs[0].add_run("Student ID")
    team_tbl.rows[0].cells[3].paragraphs[0].add_run("Programme and project role")

    members = [
        ("1", "Yuxuan Wu", "50106070", "BSc (BMIS) | Team Leader and Project Contact (Team Leader)"),
        ("2", "Yongtong Lin", "50106038", "BSc (BMIS) | Principal Concept Co-Originator (Principal Concept Co-Originator)"),
        ("3", "Sijian Wang", "50106045", "BSc (BMIS) | Team Member (Team Member)"),
        ("4", "Hao Jiang", "50106065", "BSc (BMIS) | Team Member (Team Member)"),
        ("5", "Weixin Xie", "50106034", "BSc (BMIS) | Principal Concept Co-Originator (Principal Concept Co-Originator)"),
        ("6", "Zijian Zhang", "50106035", "BSc (BMIS) | Team Member (Team Member)"),
        ("7", "Yusai Xi", "50105989", "BSc (BMIS) | Team Member (Team Member)"),
        ("8", "Siqin Dong", "50106060", "BSc (BMIS) | Team Member (Team Member)"),
        ("9", "Mingjie Yang", "50106061", "BSc (BMIS) | Team Member (Team Member)"),
        ("10", "Zixuan Liang", "50106037", "BSc (BMIS) | Team Member (Team Member)"),
    ]
    for r_idx, row in enumerate(members, start=1):
        for c_idx, val in enumerate(row):
            team_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(team_tbl, col_widths=[0.6, 1.2, 1.2, 3.5])

    # 1. Project background and problem definition
    add_h1(doc, "1. Project Background and Problem Definition (Problem Statement)")
    add_p(doc, "During undergraduate study, students commonly face several demanding, wide-ranging courses (computer science, business and management, finance, law, etc.). When revising for final exams and consolidating knowledge day to day, they hit serious efficiency bottlenecks and cognitive overload:")
    add_bullet(doc, "Slides, textbook chapters and exercise books exist as separate blocks with no clear knowledge-dependency graph, easily leaving students in a confused 'blind men describing an elephant' revision state.", bold_prefix="1. Fragmented knowledge and cognitive overload: ")
    add_bullet(doc, "When working through past papers or exercises, students can often see only 'right' or 'wrong'; they cannot tell which logical trap the examiner set, and lack a way to trace root weaknesses.", bold_prefix="2. Blind practice without a clear view of error-prone points: ")
    add_bullet(doc, "Existing commercial LLMs tend to give the final complete answer directly in Q&A. Passively copying answers not only removes the process of independent thought but also fails to build deeper problem-solving thinking.", bold_prefix="3. Existing AI tutoring lacks diagnosis and heuristic guidance: ")
    add_bullet(doc, "General-purpose LLMs suffer from serious 'knowledge hallucination' and random-answer behaviour in professional academic fields. Faced with advanced university mathematical derivations, theorem prerequisites and technical terminology, they readily produce answers that look plausible but are in fact fabricated and wrong. Students who trust wrong derivations not only fail to improve their marks but reinforce misconceptions, causing serious academic misdirection.", bold_prefix="4. The severe pain point of knowledge hallucination and nonsense answers in academic fields: ")

    # 2. Technical solution
    add_h1(doc, "2. Solution and Core Technical Architecture (Proposed Solution)")
    add_p(doc, "This project proposes and implements the [An Intelligent University Exam-Preparation and Knowledge-Diagnosis Tutoring System (Smart Study Assistant System)]. Centred on an existing knowledge graph and Retrieval-Augmented Generation (GraphRAG), it upgrades conventional flat, passive question-answering into structured intelligent diagnostic tutoring.")
    add_bullet(doc, "Build a subject ontology in Neo4j defining four core node types: [core exam point], [theorem condition], [common-error gap] and [computational operation]. It introduces a first-of-its-kind [PRONE_TO (DEPENDS_ON)] relation edge to precisely record easily confused concepts and easily overlooked boundary conditions.", bold_prefix="1. Neo4j mistake-graph modelling: ")
    add_bullet(doc, "Integrate Alibaba Cloud's Tongyi Qianwen model (DashScope Qwen-Turbo) to reverse-infer exam points from past papers, automatically extract error-prone logical traps, and achieve automated graph construction and exam-point knowledge capture.", bold_prefix="2. Automatic exam-paper diagnosis and extraction: ")
    add_bullet(doc, "The AI tutor is strictly forbidden from outputting the complete answer directly during tutoring; instead it poses heuristic questions step by step based on error-prone nodes in the graph, guiding students to discover their own thinking gaps (Socratic tutoring mechanism).", bold_prefix="3. Socratic heuristic tutoring: ")
    add_bullet(doc, "The quiz system automatically links weak graph nodes, and on the front end uses ECharts 5.5.1 to generate the student's five-dimension ability radar (basic concepts, boundary reasoning, trap defence, integrated application, computational precision), intuitively showing revision weaknesses.", bold_prefix="4. Adaptive quizzes and five-dimension ability radar: ")
    add_bullet(doc, "Generative question-answering is strictly grounded in the verified Neo4j knowledge topology and combined with a high-confidence arbitration gate (>=85%), effectively filtering generated noise and spurious edges and, by mechanism, substantially reducing the AI's knowledge-hallucination rate in professional academic fields.", bold_prefix="5. Graph fact grounding and significant reduction of the knowledge-hallucination rate: ")

    add_callout(
        doc,
        "💡 [Existing technical validation basis and supporting data]\n"
        "This project already has a solid technical prototype (the local graphrag codebase already runs Neo4j connectivity and Qwen diagnostic extraction):\n"
        "• On a multi-subject real test set, graph-based trap diagnosis compared with the general-LLM baseline improved accuracy by +2.50% in professional law tests and +2.00% in computer-science tests.\n"
        "• Addressing the industry pain point of 'serious nonsense answers and knowledge hallucination in academic LLMs', the system uses authoritative Neo4j subject-ontology fact grounding and a high-confidence arbitration gate (Confidence Threshold >= 85%) to intercept noise effectively and significantly reduce the knowledge-hallucination rate.",
        border_color="059669",
        bg_color="ECFDF5"
    )

    # 3. SMART objectives
    add_h1(doc, "3. Project Objectives (SMART Principles)")
    add_p(doc, "Strictly aligned with the JC2001 course standard, this project sets five SMART objectives to be achieved by 14 December 2026:")
    add_bullet(doc, "By 14 December 2026, design, develop and deliver a fully functional PoC software package comprising a Neo4j cloud database, the Qwen diagnosis API, Socratic tutoring, and a front-end visualisation interface.", bold_prefix="Objective 1 (functional delivery): ")
    add_bullet(doc, "Build a knowledge graph covering at least 250 core exam points, 500 multi-subject real exam questions and 300 error-prone dependency relationships, with bidirectional Cypher graph-traversal query response latency strictly under 2.0 seconds.", bold_prefix="Objective 2 (graph scale and performance): ")
    add_bullet(doc, "Reach over 85% accuracy in extracting exam points and traps from real papers; filter over 85% of noisy edges through graph fact grounding and the high-confidence arbitration gate (>=85%), significantly suppressing academic nonsense answers and effectively reducing the knowledge-hallucination rate.", bold_prefix="Objective 3 (diagnostic accuracy and hallucination reduction): ")
    add_bullet(doc, "Follow modular object-oriented software-engineering standards, reach 100% unit-test coverage of core Cypher query interfaces, >= 80% pytest branch coverage of key business logic, and PEP 8 compliance.", bold_prefix="Objective 4 (engineering quality and testing): ")
    add_bullet(doc, "By 23:59 CST on 14 December, submit in full the 40-60 page formal technical report, the 8-12 page user manual, the 15-minute MP4 defence video, and the individual workload table signed by every member.", bold_prefix="Objective 5 (documentation and course acceptance): ")

    # 4. Project benefits
    add_h1(doc, "4. Project Value and Expected Benefits (Expected Benefits)")
    add_bullet(doc, "Help students build a three-dimensional exam-point topology network and escape blind rote memorisation, with an estimated 30-40% saving in revision time; radar visualisation exposes weak points clearly.", bold_prefix="For students (primary users): ")
    add_bullet(doc, "Through aggregated mistake-graph heat data, lecturers and teaching assistants can directly see on which prerequisite exam points the class has collective cognitive blind spots, enabling targeted support.", bold_prefix="For teachers and teaching assistants: ")
    add_bullet(doc, "Accumulate a reusable cross-year digital course knowledge asset that supports the digitalisation and intelligent teaching of university courses.", bold_prefix="For the school and discipline: ")

    # 5. Timeline
    add_h1(doc, "5. Project Timeline and Milestone Roadmap (Timeline & Roadmaps)")
    add_p(doc, "The project cycle exactly matches the 12-week full lifecycle of the first semester of 2026-27 (14 September 2026 to 14 December 2026), divided into four consecutive engineering phases:")

    time_tbl = doc.add_table(rows=5, cols=4)
    time_tbl.rows[0].cells[0].paragraphs[0].add_run("Engineering phase")
    time_tbl.rows[0].cells[1].paragraphs[0].add_run("Core task content")
    time_tbl.rows[0].cells[2].paragraphs[0].add_run("Key deliverables")
    time_tbl.rows[0].cells[3].paragraphs[0].add_run("Deadline")

    time_data = [
        ("Phase 1: Requirements capture and proposal", "Team formation, pain-point research, user-story definition, first meeting with the supervisor", "Project Proposal PDF", "25 September 2026"),
        ("Phase 2: Architecture design and modelling", "Neo4j schema definition, UML class/sequence/use-case diagram modelling, prototype wireframes", "Architecture design baseline and Project Update 1", "31 October 2026"),
        ("Phase 3: PoC development and validation", "Graph API development, Qwen API diagnosis integration, quiz engine implementation, unit tests", "Software code freeze and Project Update 2/3", "30 November 2026"),
        ("Phase 4: Final review, delivery and defence", "Technical report writing, 8-12 page user manual, 15-minute video recording and final assembly packaging", "Technical report + software package + video defence", "14 December 2026"),
    ]
    for r_idx, row in enumerate(time_data, start=1):
        for c_idx, val in enumerate(row):
            time_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(time_tbl, col_widths=[1.5, 2.2, 1.8, 1.0])

    add_callout(
        doc,
        "📌 [Quick reminder of key submission milestones]\n"
        "• 25 September (Friday of Week 2): submit the formal Project Proposal PDF on MyAberdeen (submitted by team lead Yuxuan Wu).\n"
        "• 23 October: submit Project Update 1 (architecture design).\n"
        "• 06 November: submit Project Update 2 (interim progress).\n"
        "• 25 November: submit Project Update 3 (prototype code and tests).\n"
        "• 14 December (Monday of Week 12): submit the final technical report (50%) + software code and manual (30%) + defence video (20%).",
        border_color="1E3A8A",
        bg_color="F1F5F9"
    )

    # 6. Work breakdown structure
    doc.add_page_break()
    add_h1(doc, "6. Project Engineering Modules and R&D Task List (Work Breakdown Structure)")
    add_p(doc, "Around system implementation and course acceptance standards, the whole project is divided into 13 concrete engineering R&D and documentation-delivery tasks, to be taken forward by the group according to engineering module:")

    wbs_tbl = doc.add_table(rows=14, cols=4)
    wbs_tbl.rows[0].cells[0].paragraphs[0].add_run("Task ID")
    wbs_tbl.rows[0].cells[1].paragraphs[0].add_run("Concrete engineering task and core output")
    wbs_tbl.rows[0].cells[2].paragraphs[0].add_run("System module")
    wbs_tbl.rows[0].cells[3].paragraphs[0].add_run("Delivery cycle and status")

    wbs_data = [
        ("WBS 1.1", "User-requirement research, revision pain-point capture and SRS compilation", "Requirements analysis module", "Phase 1 (completed)"),
        ("WBS 1.2", "Overall proposal coordination, format and layout validation, and MyAberdeen submission", "Proposal management module", "Phase 1 (in progress)"),
        ("WBS 2.1", "Neo4j graph-database knowledge-graph schema and 'PRONE_TO' relation ontology design", "Data graph module", "Phase 2 (in progress)"),
        ("WBS 2.2", "System UML architecture modelling (class, sequence, use-case and package diagrams)", "System architecture module", "Phase 2 (not started)"),
        ("WBS 3.1", "Qwen-Turbo LLM exam-point and mistake-trap automatic extraction engine development", "Back-end algorithm module", "Phase 3 (not started)"),
        ("WBS 3.2", "GraphRAG retrieval pipeline and heuristic Socratic tutoring assistant kernel development", "Tutoring assistant module", "Phase 3 (not started)"),
        ("WBS 3.3", "Adaptive diagnostic quiz front end and ECharts 5.5.1 five-dimension ability radar development", "Front-end interaction module", "Phase 3 (not started)"),
        ("WBS 3.4", "pytest unit-test suite construction, Cypher mock testing and exception-backoff handling", "Test and QA module", "Phase 3 (not started)"),
        ("WBS 4.1", "Multi-subject real-paper testing and academic-arbitration noise-filtering gate tuning", "Algorithm evaluation module", "Phase 4 (not started)"),
        ("WBS 4.2", "Formal technical report writing (40-60 pages), UML model integration and plagiarism control", "Core documentation module", "Phase 4 (not started)"),
        ("WBS 4.3", "User manual compilation (8-12 pages) and one-click deployment script for the runnable PoC package", "Deployment and manual module", "Phase 4 (not started)"),
        ("WBS 4.4", "15-minute HD defence video recording and editing, and full presentation slide deck layout", "Defence showcase module", "Phase 4 (not started)"),
        ("WBS 4.5", "Final quality-gate review of the full three-part deliverable set and final MyAberdeen upload", "Final assembly and acceptance module", "Phase 4 (not started)"),
    ]
    for r_idx, row in enumerate(wbs_data, start=1):
        for c_idx, val in enumerate(row):
            wbs_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(wbs_tbl, col_widths=[0.9, 3.2, 1.2, 1.2])

    # 7. Risk management
    doc.add_page_break()
    add_h1(doc, "7. Project Risk Management and Contingency Plans (Risk Management)")
    add_bullet(doc, "The free Neo4j AuraDB tier has a 200,000-node limit and memory constraints. Countermeasure: enforce rigorous normalisation and deduplication of knowledge nodes, set up caching and indexes carefully, and keep a lightweight local backup deployment during testing.", bold_prefix="1. Database quota risk: ")
    add_bullet(doc, "Alibaba Cloud DashScope imposes concurrency throttling (HTTP 429). Countermeasure: implement an exponential backoff with jitter retry algorithm at the code layer and maintain a local cache pool of real exam questions.", bold_prefix="2. LLM API rate-limit risk: ")
    add_bullet(doc, "Subject mid-term exams in Weeks 7-8 may spread effort thin. Countermeasure: freeze the Phase 2 architecture baseline by 20 October, leaving a 10-day flexible sprint buffer.", bold_prefix="3. Team member availability conflict risk: ")
    add_bullet(doc, "The technical report must not paste code and must pass Turnitin. Countermeasure: a designated member strictly controls this; the main text only shows algorithmic topology, UML models and architecture diagrams, and continuous text quotation must not exceed 3 sentences.", bold_prefix="4. Academic integrity and plagiarism risk: ")

    # 8. Member review checklist
    add_h1(doc, "8. Member Review Focus and Checklist (Review Checklist)")
    add_p(doc, "When reviewing this plan, please focus on and confirm the following key items:")
    add_bullet(doc, "Confirm that the names and student IDs on the cover page of this plan are correct.", bold_prefix="1. Check your name and student ID: ")
    add_bullet(doc, "Fully understand the core features of our system (Neo4j mistake graph + Qwen exam-point reverse inference + Socratic tutoring assistant + five-dimension ability radar).", bold_prefix="2. Project solution consensus: ")
    add_bullet(doc, "Know the five JC2001 delivery components (proposal, milestone reports, 40-60 page technical report, PoC software package + 8-12 page user manual, 15-minute defence video) and the marking red lines.", bold_prefix="3. Awareness of course requirements: ")
    add_bullet(doc, "After the whole group has reviewed and confirmed, the team lead will formally upload the English Proposal to MyAberdeen by 25 September; individual R&D modules will then be discussed and claimed by the group at team meetings.", bold_prefix="4. Collaboration mechanism: ")

    add_p(doc, "\n----------------------------------------------------------------------\n"
               "Held by all members of the JC2001 Group 5 project team (Aberdeen Institute, South China Normal University, September 2026).")

    doc.save(docx_path)
    print(f"[OK] Project plan DOCX generated successfully: {docx_path}")


def export_pdf(docx_path: str, pdf_path: str):
    import win32com.client
    abs_docx = str(Path(docx_path).resolve())
    abs_pdf = str(Path(pdf_path).resolve())
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        wdoc = word.Documents.Open(abs_docx)
        wdoc.SaveAs(abs_pdf, FileFormat=17)
        wdoc.Close()
        print(f"[OK] Project plan PDF exported successfully: {pdf_path}")
    finally:
        word.Quit()


def main():
    docx_out = "reports/JC2001_Group5_Project_Plan.docx"
    pdf_out = "reports/JC2001_Group5_Project_Plan.pdf"

    generate_project_plan_docx(docx_out)
    export_pdf(docx_out, pdf_out)

    import pymupdf
    doc = pymupdf.open(pdf_out)
    print(f"[VERIFY] Project plan PDF pages: {len(doc)}, size: {doc[0].rect}")


if __name__ == "__main__":
    main()
