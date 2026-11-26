#!/usr/bin/env python3
"""Build and compile the Cycle 3 Interim Technical Report (50% Milestone Draft)
100% grounded in authentic team-member PR submissions from xin-315/my-first-github:
- Completed Full Prose Chapters (authored directly by Group 5 members):
  * Ch 1: Lin Yongtong (50106038) — PR #18 (Chapter1_Introduction.docx + 2 embedded figures)
  * Ch 3 + Appendix B RTM: Xie Weixin (50106034) — PR #17 (ch03_xie_weixin/draft.md + 2 figures)
  * Ch 4 + Table 4.1 ADRs: Wang Sijian (50106045) — PR #14 (ch04_wang_sijian/draft.md + 4 figures)
  * Ch 5.3–5.4: Dong Siqin (50106060) — PR #16 (ch05_dong_siqin/draft.md + Fig 5.2)
  * Ch 5.6: Liang Zixuan (50106037) — PR #15 (ch05_liang_zixuan/draft.md + Fig 5.5)
- Week B In-Progress Chapters (backed by member-submitted engineering & design PRs):
  * Ch 2: Zhang Zijian (50106035) — PR #5 / #8 (personal & consolidated MoSCoW RTM tables)
  * Ch 5.1–5.2: Jiang Hao (50106065) — PR #9 (FastAPI bootstrap & API schema outline)
  * Ch 5.5: Xi Yusai (50105989) — PR #1 / #20 (UI/UX design specifications, API mapping & page prototypes)
  * Ch 6: Yang Mingjie (50106061) & Luo Wenxi (50106012) — PR #12 (black-box test_plan.md TC-01..TC-08)
  * Ch 7: Wu Yuxuan (50106070) — Week B final synthesis & 11-member workload sign-off
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path
import fitz  # PyMuPDF

import build_latex_pdf

ROOT = Path(__file__).resolve().parent.parent
FINAL_REPORT_DIR = ROOT / "reports" / "final_report"
REPORTS_DIR = ROOT / "reports"
INTERIM_DIR = REPORTS_DIR / "interim_50pct"
INTERIM_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_MD = INTERIM_DIR / "StudyGraph_Cycle3_Interim_Report_50pct.md"
OUTPUT_TEX = INTERIM_DIR / "StudyGraph_Cycle3_Interim_Report_50pct.tex"
OUTPUT_PDF = INTERIM_DIR / "StudyGraph_Cycle3_Interim_Report_50pct.pdf"
OUTPUT_PDF_REPORTS = REPORTS_DIR / "StudyGraph_Cycle3_Interim_Report_50pct.pdf"
HANDOVER_PDF = REPORTS_DIR / "handover_2026-10-29" / "01_supervisor_files" / "StudyGraph_Cycle3_Interim_Report_50pct.pdf"


def get_front_matter_50pct() -> str:
    return """# Front Matter: Title Page, Declaration, and Interim Progress Summary

**UNIVERSITY OF ABERDEEN — JOINT INSTITUTE OF SCNU & UoA**  
**JC2001: Introduction to Software Engineering (2026–2027)**  
**Project Title**: *StudyGraph (SmartStudy Compass): Graph-Grounded Option-Level Misconception Diagnostic Study Assistant*  
**Document Type**: **Cycle 3 Interim Technical Report (50% Milestone Draft · Week A Checkpoint)**  
**Group 5 (11 Members)**: Wu Yuxuan (`50106070`, Group Lead), Lin Yongtong (`50106038`, Requirements Lead), Zhang Zijian (`50106035`, Business Analysis), Xie Weixin (`50106034`, Report Lead & QA), Wang Sijian (`50106045`, System Architect), Jiang Hao (`50106065`, Backend Implementation), Dong Siqin (`50106060`, Diagnostic API & Quiz Logic), Xi Yusai (`50105989`, UI/UX Design), Liang Zixuan (`50106037`, Deployment & Media Lead), Yang Mingjie (`50106061`, Software Testing Lead), Luo Wenxi (`50106012`, QA & Data Verification).

### Milestone Progress Matrix (Week A Checkpoint — ~50% Completed via Team PRs)
- [PASS] **Chapter 1 · Introduction and Project Context** (Yongtong Lin, PR `#18`): Complete member-authored draft with Tables 1.1–1.3 and Figures 1.1–1.2.
- [WIP] **Chapter 2 · Functional and Non-Functional Requirements** (Zijian Zhang, PR `#5` / `#8`): Consolidated MoSCoW requirement tables (`reports/rtm.md`) submitted; narrative prose scheduled for Week B after canonical ID sign-off.
- [PASS] **Chapter 3 · Use Cases, Behavioural Modelling & Appendix B RTM** (Weixin Xie, PR `#17`): Complete member-authored draft covering UC-01–UC-08, Figure 3.1, Figure 3.2, and the 25-row Appendix B traceability matrix.
- [PASS] **Chapter 4 · System Design and Architecture** (Sijian Wang, PR `#14`): Complete member-authored draft with Figures 4.1–4.4, Table 4.1 (AD-1 to AD-7), and Table 4.2.
- [WIP] **Chapter 5.1–5.2 · Backend Packaging & API Contracts** (Hao Jiang, PR `#9`): FastAPI bootstrap remediation merged; prose and schema tables scheduled for Week B.
- [PASS] **Chapter 5.3–5.4 · Question Bank, Trap Engineering & Diagnostic Algorithm** (Siqin Dong, PR `#16`): Complete member-authored draft with Tables 5.4–5.6, Figure 5.2, and deterministic lookup pseudocode.
- [WIP] **Chapter 5.5 · Graphical User Interface Design** (Yusai Xi, PR `#1` / `#20`): Full 5-part UI/UX specification (`reports/ui-design/`) and high-fidelity wireframes submitted; prose consolidation scheduled for Week B.
- [PASS] **Chapter 5.6 · Deployment and Reproducibility** (Zixuan Liang, PR `#15`): Complete member-authored draft with Figure 5.5, Table 5.7, and clean-machine deployment timings.
- [WIP] **Chapter 6 · Testing and Empirical Evaluation** (Mingjie Yang & Wenxi Luo, PR `#12`): Black-box test matrix (`TC-01`–`TC-08`) and automated `pytest` suite (`147–150 passed`) delivered; MMLU ablation narrative scheduled for Week B.
- [WIP] **Chapter 7 · Critical Evaluation and Future Work** (Yuxuan Wu): Scheduled for Week B following full chapter integration.

---
"""


def get_authentic_wip_sections() -> dict[str, str]:
    """Build Week B in-progress sections strictly from actual member PR artifacts in reports/."""
    test_plan_lines = [
        ln for ln in (REPORTS_DIR / "test_plan.md").read_text(encoding="utf-8").splitlines()
        if ln.strip().startswith("|")
    ]
    test_plan_table = "\n".join(test_plan_lines)

    return {
        "ch02_wip": """# 2 Functional and Non-Functional Requirements

*Author: Zijian Zhang (50106035) & Yongtong Lin (50106038) | Status: Week B Prose in Progress — Consolidated MoSCoW Tables Submitted via PR #5 and PR #8*

> **Interim Checkpoint Note:** Both Business Analysts have submitted their requirement inventories and acceptance mappings in `reports/rtm.md` and `reports/use_cases.md` (PR `#5` and PR `#8`). Before finalising the prose narrative of Chapter 2 in Week B, the team is resolving one documented governance item: aligning the legacy repository numbering (`FR-01`–`FR-08`) with Zhang Zijian's extended personal RTM numbering (`FR-04`–`FR-10`) into a single canonical scheme. Both author-verified requirement tables are presented below in their submitted form.

## 2.1 Core Scope Functional & Non-Functional Requirements (UC-01–UC-04 Scope)

| ID | Requirement | Objective | Use Case | MoSCoW | Acceptance Criterion | Current Check |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** | Select a study domain | Obj 1 | UC-02 | Must Have | Choose discipline filter and display matching items | Browser filtering present; full UI check scheduled |
| **FR-02** | Submit one answer per on-screen attempt | Obj 1, 4 | UC-01, UC-02 | Must Have | Valid selection invokes diagnosis endpoint and locks controls | API handler and frontend state present |
| **FR-03** | Identify misconception and missing prerequisite | Obj 1, 2 | UC-01 | Must Have | Every curated distractor maps structurally to a named misconception and prerequisite | Structural `pytest` checks passing |
| **FR-05** | Inspect evidence, source and review status | Obj 1, 2 | UC-03 | Must Have | Display item evidence and review status without overstating unreviewed items | Partial; provenance status workflow in refinement |
| **FR-06** | Inspect question-specific knowledge subgraph | Obj 1 | UC-04 | Should Have | Render typed concept/prerequisite/trap nodes and edges per question | Local SVG graph view implemented |
| **NFR-01** | Secure API and credential handling | Obj 4 | UC-01, UC-02 | Must Have | No secret keys in browser bundles or tracked source files | Verified via packaging secret scan |
| **NFR-02** | Local reliability / no cloud dependency | Obj 1, 4 | UC-01, UC-02 | Must Have | Core demonstration runs offline via local Python and curated data | Verified offline (`has_api_key: false`) |
| **NFR-05** | Responsive layout | Obj 4 | UC-02, UC-04 | Should Have | Readable controls without horizontal overflow across desktop and mobile widths | Responsive CSS implemented |
| **NFR-07** | Local API performance | Obj 4 | UC-01, UC-02 | Should Have | Local API median latency below 200 ms (measured ~1.5 ms median) | Measured and verified locally |

## 2.2 Extended Learning Analytics & Tutoring Requirements (UC-05–UC-08 Scope, PR #5)

| ID | Requirement Name | Objective | Use Case | MoSCoW | Short Acceptance Criterion |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **FR-04** | Five-dimension learning radar and mastery analysis | Obj 1 | UC-05 | Should Have | Refresh five-axis radar from attempt outcomes; flag insufficient evidence below threshold |
| **FR-05** | Socratic guided follow-up | Obj 1, 2 | UC-08 | Should Have | Return 2–3 sentence contextual counter-question without spoiling the direct answer |
| **FR-06** | Supplementary question recommendation | Obj 1 | UC-07 | Could Have | Recommend an isomorphic item on the same concept when available (planned scope) |
| **FR-07** | Search, filter and retry historical wrong answers | Obj 1 | UC-06 | Should Have | Filter wrong attempts by subject/concept and retry without overwriting original error |
| **FR-08** | Traceable question evidence and review status | Obj 1, 2 | UC-05, UC-07, UC-08 | Must Have | Show source provenance and keep pending items clearly marked |
| **FR-09** | Hints and student-requested explanations | Obj 1 | UC-05, UC-08 | Must Have | Viewing a hint does not record an attempt; full explanation appears upon student action |
| **FR-10** | Save, read and clear learning records | Obj 1 | UC-05, UC-06, UC-07 | Must Have | Persist attempts across refreshes and require confirmation before clearing |
""",
        "ch05_51_52_wip": """## 5.1 Software Structure and Packaging Discipline

*Author: Hao Jiang (50106065) | Status: Week B Prose in Progress — FastAPI Bootstrap Fix Merged in PR #9*

> **Interim Checkpoint Note:** Engineering remediation for standalone FastAPI module execution (`backend/app/main.py` and `backend/run.py` path resolution, PR `#9`) and frontend-to-backend route mapping (`reports/api_frontend_mapping.md`) have been merged into `xin/master`. Full narrative documentation of the package hierarchy (`routers/`, `services/`, `models/`, `data/`) and Pydantic v2 `CamelModel` schema tables (`5.1`–`5.2`) is scheduled for Week B completion.

## 5.2 API Endpoint Inventory and Serialization Contract

*(Section in active drafting by Hao Jiang, 50106065, for Week B integration — cross-referenced with Chapter 4.1.3 and `backend/app/routers/`.)*
""",
        "ch05_55_wip": """## 5.5 Graphical User Interface Design and Console Workflow

*Author: Yusai Xi (50105989) | Status: Week B Prose in Progress — 5-Part UI Design Package & High-Fidelity Prototypes Submitted in PR #1 & PR #20*

> **Interim Checkpoint Note:** Complete UI/UX design specifications (`reports/ui-design/01-wireframes.md` through `05-checklist.md`), frontend-backend field mappings (`reports/api_frontend_mapping.md`), and high-fidelity page renders have been delivered in PR `#1` and PR `#20`. The interface adopts an **8px-grid console-style developer-tool aesthetic** supporting both light and dark themes (`NFR-03`), dual icon-plus-text status indicators, and five explicit view states (`default`, `loading`, `empty`, `error`, `fallback`). Narrative synthesis into Section 5.5 prose is underway for Week B.

![Practice Page High-Fidelity Prototype](page-practice.png)

**Figure 5.4 (Preview): High-fidelity console layout for the question practice and option-level diagnosis view (submitted by Yusai Xi, 50105989, PR #20).**
""",
        "ch06_wip": f"""# 6 Software Testing and Empirical Evaluation

*Authors: Mingjie Yang (50106061) & Wenxi Luo (50106012) | Status: Week B Prose in Progress — Black-Box Test Matrix (PR #12) and Automated Pytest Suite Active*

> **Interim Checkpoint Note:** Two verification artefacts are already established in the repository: (1) the automated `pytest` regression suite across nine test files (`147` passing cases on the frozen PoC baseline; `183` passing cases on `xin/master` including the `GET /api/health/llm` diagnostic tests from PR `#10`), and (2) the manual black-box functional acceptance matrix (`reports/test_plan.md`, PR `#12`) reproduced below, which honestly distinguishes passing core flows (`TC-01`, `TC-02`, `TC-05`, `TC-08`) from partial or unimplemented scope (`TC-03`, `TC-04`, `TC-06`, `TC-07`). In Week B, Chapter 6 will integrate the full 12-discipline MMLU empirical evaluation ($n = 4,445$ items from `graphrag/final_systematic_report.csv`) and RAGAS faithfulness discussion.

## 6.1 Black-Box Functional Verification Matrix (`TC-01`–`TC-08`, PR #12)

{test_plan_table}
""",
        "ch07_wip": """# 7 Critical Evaluation, Reflections and Future Work

*Author: Yuxuan Wu (50106070) | Status: Scheduled for Week B Final Integration*

> **Interim Checkpoint Note:** Chapter 7 is intentionally held open until all Week B empirical sections (Chapters 2, 5.1–5.2, 5.5, and 6) are frozen, ensuring that the critical evaluation against Objectives 1–5 reflects verified final measurements rather than premature claims. Key topics queued for Week B drafting include:
> 1. **Audit against Project Objectives 1–5**: Reconciling the 12-question / 36-trap curated bank against Objective 2's 15-item target, and documenting the offline vs. live Neo4j architectural boundary (`AD-5`).
> 2. **Known Engineering Trade-offs**: Unifying the frontend offline presentation cache with `seed_questions.py`, tightening permissive local CORS (`AD-6`), and completing credential rotation across legacy prototype scripts (Section 5.6.5).
> 3. **11-Member Group Workload & Reflection**: Consolidating individual contribution sign-offs across all eleven team members (`50106070`, `50106038`, `50106035`, `50106034`, `50106045`, `50106065`, `50106060`, `50105989`, `50106037`, `50106061`, `50106012`) in Appendix A.
""",
    }


def assemble_50pct_markdown() -> str:
    wip = get_authentic_wip_sections()

    # Read authentic member-authored chapters
    ch01 = (FINAL_REPORT_DIR / "ch01_lin_yongtong" / "draft.md").read_text(encoding="utf-8").strip()

    ch03_full = (FINAL_REPORT_DIR / "ch03_xie_weixin" / "draft.md").read_text(encoding="utf-8").strip()
    # Split Xie Weixin's Appendix B so it sits cleanly at the back of the report as Appendix B!
    if "# Appendix B: Requirements Traceability Matrix" in ch03_full:
        ch03_main, appendix_b_part = ch03_full.split("# Appendix B: Requirements Traceability Matrix", 1)
        ch03_main = ch03_main.strip()
        appendix_b = "# Appendix B: Requirements Traceability Matrix (Weixin Xie, PR #17)\n\n" + appendix_b_part.strip()
    else:
        ch03_main = ch03_full
        appendix_b = ""

    ch04 = (FINAL_REPORT_DIR / "ch04_wang_sijian" / "draft.md").read_text(encoding="utf-8").strip()
    ch05_dong = (FINAL_REPORT_DIR / "ch05_dong_siqin" / "draft.md").read_text(encoding="utf-8").strip()
    ch05_liang = (FINAL_REPORT_DIR / "ch05_liang_zixuan" / "draft.md").read_text(encoding="utf-8").strip()

    parts: list[str] = [
        get_front_matter_50pct(),
        ch01,
        wip["ch02_wip"],
        ch03_main,
        ch04,
        "# 5 Implementation\n\n" + wip["ch05_51_52_wip"].strip(),
        ch05_dong,
        wip["ch05_55_wip"],
        ch05_liang,
        wip["ch06_wip"],
        wip["ch07_wip"],
    ]
    if appendix_b:
        parts.append(appendix_b)

    merged = "\n\n---\n\n".join(p.strip().strip("-").strip() for p in parts if p.strip()) + "\n"
    OUTPUT_MD.write_text(merged, encoding="utf-8")
    words = len(merged.split())
    print(f"[Interim 50% Authentic] Wrote {OUTPUT_MD} ({words:,} words, {len(merged):,} chars)")
    return merged


INTERIM_FRONT_MATTER_TEX = r"""
% ==================== INTERIM DECLARATION & PROGRESS SUMMARY ====================
\pagenumbering{roman}
\section*{Interim Declaration and Week A Milestone Status}
\addcontentsline{toc}{section}{Interim Declaration and Week A Milestone Status}

\textbf{Document status.} This document is the \textbf{Cycle 3 Interim Technical Report (50\% Milestone Draft)} of JC2001 Group 5, compiled directly from member-authored pull requests in the team collaboration repository (\texttt{xin-315/my-first-github}, PRs \texttt{\#1}--\texttt{\#22}). At this Week A checkpoint, five substantial sections have reached full first-pass prose completion by their respective owners: \textbf{Chapter 1} (Yongtong Lin, PR \texttt{\#18}), \textbf{Chapter 3 \& Appendix B} (Weixin Xie, PR \texttt{\#17}), \textbf{Chapter 4} (Sijian Wang, PR \texttt{\#14}), \textbf{Sections 5.3--5.4} (Siqin Dong, PR \texttt{\#16}), and \textbf{Section 5.6} (Zixuan Liang, PR \texttt{\#15}). The remaining Week B sections (\textbf{Chapter 2}, \textbf{Sections 5.1--5.2}, \textbf{Section 5.5}, \textbf{Chapter 6}, and \textbf{Chapter 7}) are represented here by their already-merged engineering tables, UI prototypes, and black-box verification matrices (\texttt{rtm.md}, \texttt{ui-design/}, \texttt{test\_plan.md}), with narrative synthesis scheduled for Week B.

\textbf{Declaration of academic integrity.} We, the eleven members of JC2001 Group 5, declare that the engineering artefacts and chapter drafts assembled in this interim submission are our own original group work. Differences in terminology or requirement numbering across parallel member drafts (such as the legacy repository IDs vs.\ extended RTM IDs noted in Chapter 2 and Appendix B, and the 12-item backend seed bank vs.\ 19-item client cache noted in Section 5.3.4) are transparently preserved at this midpoint for supervisor review prior to Week B harmonisation.

\vspace{6pt}
\textbf{Interim overview.} \textbf{StudyGraph} addresses the binary-feedback limitation of conventional multiple-choice revision tools and the answer-spoiling / statutory-hallucination risks of unconstrained language models. Architecturally, it runs as a single-process FastAPI + zero-build ES6 modular monolith (\texttt{AD-1}, \texttt{AD-2}) backed by a static curated question bank (\texttt{AD-3}, 12 questions across Law, Computer Science, Econometrics, and Software Engineering encoding 36 option-level misconception traps). Diagnosis is executed as a deterministic $O(1)$ table lookup (\texttt{AD-4}, sub-millisecond core lookup; $\sim 1.5$\,ms local HTTP median) with Neo4j AuraDB isolated strictly to offline MMLU benchmarking (\texttt{AD-5}).

\clearpage
\tableofcontents
\clearpage
\pagenumbering{arabic}
"""


def build_interim_preamble() -> str:
    marker = "% ==================== EXECUTIVE ABSTRACT & TOC ===================="
    head = build_latex_pdf.LATEX_PREAMBLE_REPORT.split(marker)[0]

    head = head.replace(
        r"JC2001: Software Engineering (Cycle 3 Final Submission)",
        r"JC2001: Introduction to Software Engineering --- Cycle 3 Interim Report (50\% Milestone Draft)",
    )
    head = head.replace(
        r"JC2001 Software Engineering · Group 5 Technical Report",
        r"JC2001 Software Engineering · Group 5 Interim Report (50\% Team PR Baseline)",
    )
    head = head.replace(
        r"\textbf{Submission Date:} October 2026",
        r"\textbf{Checkpoint:} Cycle 3 Week A (Authentic Team PR Snapshot, 23 PRs) $\cdot$ October 2026",
    )
    return head + INTERIM_FRONT_MATTER_TEX


def main() -> None:
    merged_md = assemble_50pct_markdown()
    png_map = build_latex_pdf.rasterize_svgs()

    interim_png_dir = INTERIM_DIR / "figures_png"
    interim_png_dir.mkdir(parents=True, exist_ok=True)
    for f in build_latex_pdf.PNG_DIR.glob("*.png"):
        target = interim_png_dir / f.name
        if not target.exists() or target.stat().st_mtime < f.stat().st_mtime:
            shutil.copy2(f, target)

    body_latex = build_latex_pdf.markdown_to_latex_body(merged_md, png_map, skip_front_matter=True)
    full_tex = build_interim_preamble() + "\n" + body_latex + "\n\\end{document}\n"
    OUTPUT_TEX.write_text(full_tex, encoding="utf-8")
    print(f"[Interim 50%] Wrote {OUTPUT_TEX} ({len(full_tex):,} chars)")

    pdf_path = build_latex_pdf.compile_xelatex(OUTPUT_TEX, INTERIM_DIR, runs=2)
    shutil.copy2(pdf_path, OUTPUT_PDF_REPORTS)
    if HANDOVER_PDF.parent.exists():
        shutil.copy2(pdf_path, HANDOVER_PDF)

    doc = fitz.open(str(pdf_path))
    page_count = len(doc)
    doc.close()
    print(
        f"[Interim 50% PDF] SUCCESS -> {OUTPUT_PDF_REPORTS} "
        f"({page_count} pages, {OUTPUT_PDF_REPORTS.stat().st_size:,} bytes)"
    )


if __name__ == "__main__":
    main()
