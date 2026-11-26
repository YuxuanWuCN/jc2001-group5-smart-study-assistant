#!/usr/bin/env python3
"""
Persona Claims Provenance & Requirement Mapping Audit Harness
Part of Speckit 004: Persona-Hallucination-Audit
"""

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO_ROOT / "reports" / "audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)


PERSONA_CLAIMS = [
    {
        "claim_id": "PA-01",
        "persona": "A_EXAM_CRAMMER",
        "claim_text": "Second or third-year undergraduate with four exams concentrated in two weeks",
        "claim_kind": "identity",
        "source_type": "literature",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:78",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Described as common for this group based on public literature/teaching scenarios",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PA-02",
        "persona": "A_EXAM_CRAMMER",
        "claim_text": "Quizlet cards, classmates' mistake notebooks, answer summaries shared in group chats",
        "claim_kind": "current_tools",
        "source_type": "competitor_behaviour",
        "source_locator": "reports/competitor_analysis.md:32",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "A competitor offers this feature, which implies the need exists",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PA-03",
        "persona": "A_EXAM_CRAMMER",
        "claim_text": "Gets an answer wrong without knowing why, and has no time to dig deeper (binary-feedback trap)",
        "claim_kind": "pain_point",
        "source_type": "literature",
        "source_locator": "VanLehn 2011; Hattie & Timperley 2007",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "Based on fine-grained feedback literature, this pain point is widespread during exam preparation",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PA-04",
        "persona": "A_EXAM_CRAMMER",
        "claim_text": "Wants to know within five minutes which area to catch up on",
        "claim_kind": "expectation",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md:37",
        "evidence_level": "E2",
        "is_core": True,
        "allowed_usage": "Members expressed this expectation for rapid diagnosis during an internal n=10 discussion (non-representative sample)",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PA-05",
        "persona": "A_EXAM_CRAMMER",
        "claim_text": "Primary target user",
        "claim_kind": "is_target_user",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_master_plan.md:100",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Established as the primary target user by the Lean Scoping decision",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PB-01",
        "persona": "B_SYSTEMATIC_REVIEWER",
        "claim_text": "Postgraduate student doing long-term systematic revision",
        "claim_kind": "identity",
        "source_type": "literature",
        "source_locator": "Corbett & Anderson 1994 (BKT)",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Based on academic literature and postgraduate exam-preparation patterns",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PB-02",
        "persona": "B_SYSTEMATIC_REVIEWER",
        "claim_text": "Anki, note-taking software, academic papers",
        "claim_kind": "current_tools",
        "source_type": "competitor_behaviour",
        "source_locator": "reports/competitor_analysis.md:45",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Competitor observation shows that systematic learners prefer spaced-repetition tools",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PB-03",
        "persona": "B_SYSTEMATIC_REVIEWER",
        "claim_text": "Knows they are weak but cannot see which ability dimension is weak",
        "claim_kind": "pain_point",
        "source_type": "literature",
        "source_locator": "Koedinger et al. 2012 (prerequisite knowledge framework)",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "Based on multi-dimensional ability assessment models in cognitive science",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PB-04",
        "persona": "B_SYSTEMATIC_REVIEWER",
        "claim_text": "Wants to see long-term trends across ability dimensions",
        "claim_kind": "expectation",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md:37",
        "evidence_level": "E2",
        "is_core": True,
        "allowed_usage": "Expectation for learning-progress tracking formed through internal discussion",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PB-05",
        "persona": "B_SYSTEMATIC_REVIEWER",
        "claim_text": "Primary target user",
        "claim_kind": "is_target_user",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_master_plan.md:100",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Positioned as a target user for long-term exam preparation",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PC-01",
        "persona": "C_COURSE_TEACHER",
        "claim_text": "Lecturer / teaching assistant for this course",
        "claim_kind": "identity",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:78",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Stakeholder within the course context",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PC-02",
        "persona": "C_COURSE_TEACHER",
        "claim_text": "Learning-platform back office, Excel",
        "claim_kind": "current_tools",
        "source_type": "competitor_behaviour",
        "source_locator": "reports/competitor_analysis.md:60",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Common administration tools for university teachers",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PC-03",
        "persona": "C_COURSE_TEACHER",
        "claim_text": "Cannot see the specific distribution of student misconceptions beyond marking",
        "claim_kind": "pain_point",
        "source_type": "literature",
        "source_locator": "Hattie & Timperley 2007",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "Class-level diagnostic blind spot identified in the literature",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PC-04",
        "persona": "C_COURSE_TEACHER",
        "claim_text": "(Not used directly)",
        "claim_kind": "expectation",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:81",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "Does not operate the system directly",
        "auditor": "Audit Team"
    },
    {
        "claim_id": "PC-05",
        "persona": "C_COURSE_TEACHER",
        "claim_text": "Explicitly designated as a non-target user",
        "claim_kind": "is_target_user",
        "source_type": "team_discussion",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:84",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "Explicitly excluded from the MVP target-user scope (Lean Scoping)",
        "auditor": "Audit Team"
    }
]


REQUIREMENT_MAPPINGS = [
    {
        "requirement_id": "R01",
        "requirement_text": "Browse question lists by subject and load the corresponding options and trap labels",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-01, PB-01",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R02",
        "requirement_text": "Submit answers and record correct/incorrect status",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-03, PB-03",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R03",
        "requirement_text": "Option-level trap-diagnosis drawer (misconception naming / error-cause explanation / prerequisite blind spots / radar attribution)",
        "moscow": "Must",
        "served_personas": "A",
        "served_pain_points": "PA-03",
        "assumption_driven": True,
        "hallucination_layers": "L1, L2, L3",
        "external_falsifiable_claim": "If students receive only binary right/wrong feedback, their probability of repeating the same conceptual error is significantly higher than that of students who receive option-level attribution",
        "gap_reason": ""
    },
    {
        "requirement_id": "R04",
        "requirement_text": "Five-dimension radar ability-trend display (ability scores updated in real time from quiz results)",
        "moscow": "Must",
        "served_personas": "B",
        "served_pain_points": "PB-03, PB-04",
        "assumption_driven": True,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "A multi-dimensional radar chart can effectively reveal local theorem-related cognitive weaknesses hidden by a single aggregate score",
        "gap_reason": ""
    },
    {
        "requirement_id": "R05",
        "requirement_text": "Learning-status card and weak exam-point summary (attempt count / mastery rate / core error-prone prerequisite points)",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-04, PB-04",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R06",
        "requirement_text": "Student-ID password-free / password login with session isolation (including quick switching between preset demo accounts)",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-01, PB-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R07",
        "requirement_text": "Bilingual English/Chinese interface internationalisation toggle",
        "moscow": "Should",
        "served_personas": "A, B",
        "served_pain_points": "PA-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R08",
        "requirement_text": "Dark console and light academic dual themes (meeting WCAG AA contrast)",
        "moscow": "Should",
        "served_personas": "A, B",
        "served_pain_points": "PA-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R09",
        "requirement_text": "Fully offline, zero external cloud dependency, single-port operation (StaticFiles mount and local dictionary)",
        "moscow": "Must",
        "served_personas": "A",
        "served_pain_points": "PA-01",
        "assumption_driven": True,
        "hallucination_layers": "L4",
        "external_falsifiable_claim": "Under offline deterministic lookup, while eliminating network fluctuation the system also indirectly eliminates reasoning hallucination on the free-generation surface",
        "gap_reason": ""
    },
    {
        "requirement_id": "R10",
        "requirement_text": "GraphRAG offline accuracy enhancement and baseline validation",
        "moscow": "Should",
        "served_personas": "B",
        "served_pain_points": "PB-03",
        "assumption_driven": True,
        "hallucination_layers": "L4",
        "external_falsifiable_claim": "In concept- and statute-dense subjects, a prior knowledge graph can provide structural constraints that improve retrieval accuracy",
        "gap_reason": ""
    },
    {
        "requirement_id": "R11",
        "requirement_text": "Multi-tenant and teacher-side class-monitoring dashboard",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "Not part of the core student loop; beyond the capacity of a zero-budget team in 12 weeks, so it was proactively pruned"
    },
    {
        "requirement_id": "R12",
        "requirement_text": "Native mobile App development (iOS / Android)",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "The web client already supports responsive mobile viewports, and a native App has high maintenance cost"
    },
    {
        "requirement_id": "R13",
        "requirement_text": "Social mistake-sharing and discussion community",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "Easily introduces content-moderation and privacy risks, and conflicts with the independent immersive revision scenario"
    },
    {
        "requirement_id": "R14",
        "requirement_text": "AI automatic real-time unlimited question generation and paper assembly",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "Without expert review mechanisms it easily triggers high-frequency hallucination, threatening the seriousness of exam preparation"
    }
]


def main():
    provenance_file = AUDIT_DIR / "persona_provenance.csv"
    with open(provenance_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(PERSONA_CLAIMS[0].keys()))
        writer.writeheader()
        writer.writerows(PERSONA_CLAIMS)

    req_map_file = AUDIT_DIR / "requirement_persona_map.csv"
    with open(req_map_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(REQUIREMENT_MAPPINGS[0].keys()))
        writer.writeheader()
        writer.writerows(REQUIREMENT_MAPPINGS)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"[OK] Persona Provenance: {len(PERSONA_CLAIMS)} claims -> {provenance_file}")
    print(f"[OK] Requirement-Persona Mapping: {len(REQUIREMENT_MAPPINGS)} items -> {req_map_file}")


if __name__ == "__main__":
    main()
