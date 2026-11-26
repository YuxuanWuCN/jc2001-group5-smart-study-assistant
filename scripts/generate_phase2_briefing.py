from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = r"D:\jc2001\reports\phase2_supervisor_briefing_bilingual.docx"

def set_font(run, name="Calibri", size=10.5, color=None, bold=False, italic=False):
    run.font.name = name
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Microsoft YaHei" if name == "Calibri" else name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def set_cell_text(cell, text, bold=False, color=None):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text)
    set_font(r, size=9, bold=bold, color=color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


doc = Document()
sec = doc.sections[0]
sec.top_margin = Cm(1.7)
sec.bottom_margin = Cm(1.7)
sec.left_margin = Cm(1.9)
sec.right_margin = Cm(1.9)

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Microsoft YaHei")
for style_name, size, color in [("Title", 22, (31, 78, 121)), ("Heading 1", 15, (31, 78, 121)), ("Heading 2", 12, (55, 96, 146))]:
    st = doc.styles[style_name]
    st.font.name = "Calibri"
    st.font.size = Pt(size)
    st.font.color.rgb = RGBColor(*color)
    st._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Microsoft YaHei")

def heading(text, level=1):
    p = doc.add_paragraph(style=f"Heading {level}")
    r = p.add_run(text)
    set_font(r, size=15 if level == 1 else 12, color=(31,78,121) if level == 1 else (55,96,146), bold=True)
    return p

def para(text="", style=None, color=None, italic=False, bold=False, space_after=5):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    set_font(r, size=10.5, color=color, italic=italic, bold=bold)
    return p

def bullet(text, color=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    set_font(r, size=10, color=color)
    return p

# Title
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Phase 2 / Cycle 2\nSupervisor Progress Briefing")
set_font(r, size=22, color=(31,78,121), bold=True)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Spoken Script for the Supervisor Meeting")
set_font(r, size=16, color=(80,80,80), bold=True)

meta = doc.add_table(rows=6, cols=2)
meta.alignment = WD_TABLE_ALIGNMENT.CENTER
meta.style = "Table Grid"
rows = [
    ("Course", "JC2001 Introduction to Software Engineering"),
    ("Project", "Smart Study Assistant System (SmartStudy Console)"),
    ("Group", "Group 5"),
    ("Supervisor", "Dr. Shahzad Mumtaz"),
    ("Presenter", "Yuxuan Wu (50106070)"),
    ("Period", "Phase 2 / Cycle 2: 28 September–15 October 2026"),
]
for i, (a,b) in enumerate(rows):
    set_cell_text(meta.cell(i,0), a, bold=True, color=(31,78,121)); shade(meta.cell(i,0), "EAF2F8")
    set_cell_text(meta.cell(i,1), b)

doc.add_paragraph()
para("Usage note: the text below is the suggested spoken script. It runs for approximately 8 minutes, with an additional 2 minutes for the live demonstration.", color=(90,90,90), italic=True)

heading("1. Opening | approx. 30 seconds", 1)
para(
    "Good afternoon, Dr. Mumtaz. Thank you for meeting with me. I am Yuxuan Wu, the project manager of Group 5. Today I would like to report our Phase Two progress on the Smart Study Assistant System, or SmartStudy Console. I will briefly cover our requirements work, system modelling, working proof of concept, quality evidence, and the next risks we need to manage."
)

heading("2. Phase Positioning | approx. 45 seconds", 1)
para(
    "Phase One focused on team formation, problem definition and the project proposal. Phase Two was the transition from a written proposal to an engineered and testable system. Our central design principle was that the system should diagnose why a student selected a distractor, rather than simply reveal the correct answer."
)
para(
    "This addresses two weaknesses of existing tools: conventional quizzes often provide only right-or-wrong feedback, while unrestricted large language models may reveal answers too early or produce unsupported explanations. Our solution combines option-level misconception diagnosis, knowledge-graph-style grounding, and Socratic guidance."
)

heading("3. Four Main Deliverables Completed in Phase 2 | approx. 4 minutes", 1)
heading("1. Requirements Engineering", 2)
para(
    "First, we established a formal requirements baseline. We decomposed the system into eight Cockburn-style use cases, from student login and quiz participation to distractor diagnosis, Socratic tutoring and competency tracking. We also created a MoSCoW traceability structure covering functional requirements FR-01 to FR-08 and non-functional requirements NFR-01 to NFR-06."
)
para(
    "The important point is that we did not treat every feature as a must-have. We explicitly prioritised the reliable single-turn diagnostic experience for this cycle, while multi-turn tutoring, adaptive variants and cloud graph persistence remain planned extensions."
)

heading("2. UML and Architecture", 2)
para(
    "Second, we produced a UML 2.5 architecture package: a system context model, a global use-case model, a core sequence diagram for the diagnosis flow, and a domain class model. These diagrams helped us make the system boundary, actors, services and data contracts explicit before further implementation."
)
para(
    "In the Week Six modelling exercise, we also practised the semantics of include and extend relationships using a university library example. This was useful because it reinforced the difference between mandatory shared behaviour and conditional extension behaviour, which we then applied when reviewing our own diagrams."
)

heading("3. Working PoC", 2)
para(
    "Third, we delivered an end-to-end proof of concept. The backend uses a modular FastAPI structure with routers, services and Pydantic data models. The current live routes are health, quiz and diagnosis. The frontend is an interactive console with a dark visual language, a command palette, a comparison sandbox, and a five-dimension competency radar."
)
para(
    "The seed dataset contains twelve questions across four disciplines: law, computer science, economics and software engineering. Each discipline has three questions. The questions contain thirty-six option-level distractor traps. All twelve questions also have a small graph structure: sixty concept nodes and forty-eight directed edges in total."
)
para(
    "For resilience, the diagnosis service has two modes. When the external Qwen service is available, it can use the live path with a four-second timeout. When credentials are missing or the network fails, it falls back to the curated local seed data instead of returning an unhandled server error. This makes the prototype demonstrable in an offline classroom environment."
)

heading("4. Verification and QA", 2)
para(
    "Fourth, we built an automated quality gate. The current mainline collects and passes 114 pytest cases with zero failures. The suites cover adversarial backend inputs, quiz contracts, CORS behaviour, full-stack stress scenarios, diagnosis logic, health checks and frontend asset delivery."
)
para(
    "The security-oriented cases include SQL injection strings, XSS payloads, path traversal probes, malformed JSON and extreme input lengths. We also tested concurrent diagnosis and quiz requests. The key result for this phase is not only that the happy path works, but that common failure paths are handled without an unhandled HTTP 500 response."
)

heading("4. Engineering Governance and Cycle Wrap-up | approx. 45 seconds", 1)
para(
    "We also improved the engineering process. Work was organised through feature branches and reviewable commits. Before integration, we ran the full test suite. This week, we landed the Cycle Two progress report and the Week Six UML lab artefacts, merged the visual overhaul into develop, and then merged develop into main locally. The final main branch still passes all 114 tests."
)

# Metrics table
heading("5. Key Evidence", 1)
t = doc.add_table(rows=1, cols=3)
t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
for c, txt in enumerate(["Metric", "Verified result", "Evidence"]):
    set_cell_text(t.cell(0,c), txt, bold=True, color=(255,255,255)); shade(t.cell(0,c), "1F4E79")
metrics = [
    ("Automated QA", "114 passed, 0 failures", "python -m pytest -q"),
    ("Seed questions", "12 questions; 4 subjects", "backend/app/data/seed_questions.py"),
    ("Distractor traps", "36 option-level traps", "seed question data"),
    ("Graph seed", "12 graphs; 60 nodes; 48 edges", "Question model graph field"),
    ("API surface", "health / quiz / diagnose", "backend/app/routers/"),
    ("UML package", "Context, Use Case, Sequence, Class", "reports/figures/"),
    ("Repository history", "47 commits across refs", "git log --all"),
]
for row in metrics:
    cells = t.add_row().cells
    for i, val in enumerate(row): set_cell_text(cells[i], val)

doc.add_paragraph()

heading("6. Live Demo Cue | approx. 2 minutes", 1)
para(
    "For a short demonstration, I would first show the diagnosis interface and select a plausible wrong option. The system should identify the distractor trap, show the related prerequisite concept, and provide a guiding question without exposing the answer letter. I would then show the offline fallback by running the same flow without depending on an external API key."
)
para("Demo commands", bold=True, color=(31,78,121))
for cmd in ["python -m pytest -q", "python backend/run.py", "Open frontend/index.html (or use the http://127.0.0.1:8000 address printed by the backend)"]:
    bullet(cmd)

heading("7. Current Risks and Points for the Supervisor", 1)
para(
    "There are three points I want to state transparently. First, the local main branch is complete and tested, but the final push to GitHub is currently blocked by a local network and proxy problem. Second, some team artefacts exist on member fork branches and need path consolidation before they can be treated as part of the mainline evidence package. Third, the current graph is a validated in-memory seed graph; live Neo4j or AuraDB integration is a next-stage task, not something I want to overclaim for this cycle."
)
para(
    "My main question for you is: for the upcoming architecture baseline, would you prefer us to demonstrate a live Neo4j instance now, or is a validated ontology, deterministic local graph and clear integration plan sufficient for the current milestone?"
)

heading("8. Next Steps | approx. 45 seconds", 1)
para(
    "Our immediate priorities are to complete the UML and Neo4j ontology baseline, consolidate the outstanding fork artefacts, and prepare Project Update One. After that, Phase Three will focus on live Neo4j or AuraDB integration, a multi-turn Socratic state machine, adaptive question variants, and broader user evaluation."
)
para(
    "Thank you. To summarise in one sentence: Phase Two transformed our proposal into a testable, resilient and demonstrable MVP, while also showing us exactly which architecture and integration tasks must be completed next."
)

heading("9. Q&A Preparation", 1)
qa = [
    ("Why is this better than a normal quiz?", "Because the system models the reason behind a wrong option and gives a Socratic prompt instead of only displaying correct or incorrect."),
    ("Is the graph already Neo4j?", "Not yet in the mainline MVP. The current graph is a validated local graph structure. Neo4j or AuraDB integration is the next architecture milestone."),
    ("How do you know it is robust?", "The current mainline collects 114 pytest cases and all pass, including adversarial, CORS, stress and fallback scenarios."),
    ("What is the biggest current limitation?", "The MVP is still primarily single-turn and seed-data driven. Multi-turn state, cloud graph persistence and broader user evaluation remain open."),
    ("What will you deliver next?", "The UML and ontology baseline, consolidated repository evidence, Project Update One, and then the live graph integration plan."),
]
for q, a in qa:
    para(q, bold=True, color=(31,78,121), space_after=2)
    para(a, color=(70,70,70), space_after=7)

heading("10. Three Accuracy Rules for the Meeting", 1)
for item in [
    "You may state clearly: all 114 tests pass on the local main branch; the 12 questions, 4 subjects, 36 traps, 60 nodes and 48 edges have all been verified from the code.",
    "Do not say: Neo4j/AuraDB integration is complete; the current graph is a local seed graph, and real cloud graph integration is a next-stage task.",
    "Do not avoid: the final GitHub push is blocked by the network; if the supervisor views the remote repository, explain that the local main branch is complete but remote synchronisation will be performed once the network recovers.",
]: bullet(item)

heading("Appendix: Evidence References", 1)
refs = [
    ("Phase 2 progress report", "reports/phase2_cycle2_progress_report.md"),
    ("Backend routes and models", "backend/app/routers/ and backend/app/models/"),
    ("Seed questions and graph data", "backend/app/data/seed_questions.py"),
    ("Automated tests", "tests/"),
    ("UML figures", "reports/figures/"),
    ("Week 6 modelling guide", "reports/week6_lab_submission_guide.md"),
    ("Runtime entry point", "backend/run.py"),
]
t = doc.add_table(rows=1, cols=2); t.style="Table Grid"; t.alignment=WD_TABLE_ALIGNMENT.CENTER
for i, txt in enumerate(["Evidence", "Path"]):
    set_cell_text(t.cell(0,i), txt, bold=True, color=(255,255,255)); shade(t.cell(0,i), "1F4E79")
for a,b in refs:
    cells=t.add_row().cells; set_cell_text(cells[0],a); set_cell_text(cells[1],b)

# Footer
for section in doc.sections:
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = footer.add_run("JC2001 Group 5 | Phase 2 / Cycle 2 Supervisor Briefing")
    set_font(r, size=8, color=(120,120,120))

doc.save(OUT)
print(OUT)
