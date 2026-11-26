"""
Report Service - Learning Telemetry, Mastery Analytics, and Diagnostic Aggregation
Provides domain metrics and cognitive radar evaluations with strict zero-crash guarantees.
"""

import threading
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime, timezone

from backend.app.models.report import (
    ReportSummaryResponse,
    ReportTrendResponse,
    WeakPointItem,
    TrapDistributionItem
)
from backend.app.services.quiz_service import quiz_service, SUBJECT_ALIASES
from backend.app.data.seed_questions import SEED_QUESTIONS


# Subject specific curriculum baselines (Domain Topics & Curated Diagnostic Recommendations)
DISCIPLINE_METADATA: Dict[str, Dict[str, Any]] = {
    "law": {
        "title": "Civil and Commercial Law",
        "radar": [88.0, 75.0, 82.0, 70.0, 80.0],
        "weak_points": [
            WeakPointItem(
                topic="Civil Code Art. 152 · preclusive period of the right of revocation",
                trap_name="Rescission period vs. limitation period",
                fail_count=3,
                severity="high",
                recommendation="Study in depth the fixed-period character of the preclusive period, and note that a court may examine the expiry of a preclusive period of its own motion."
            ),
            WeakPointItem(
                topic="Change of real rights · elements of bona fide acquisition",
                trap_name="Misclassification of entrusted versus escaped articles",
                fail_count=2,
                severity="medium",
                recommendation="Distinguish the legal remedies available for lost property from those available for articles delivered under a lease and entrusted to another's possession."
            )
        ]
    },
    "econ": {
        "title": "Econometrics and Intermediate Microeconomics",
        "radar": [85.0, 78.0, 90.0, 68.0, 84.0],
        "weak_points": [
            WeakPointItem(
                topic="Endogeneity · omitted-variable bias (OVB)",
                trap_name="Conflating omitted-variable bias with multicollinearity",
                fail_count=3,
                severity="high",
                recommendation="Review the OLS assumptions and identify the exogeneity conditions required when control variables and instruments are introduced."
            ),
            WeakPointItem(
                topic="Price elasticity of demand and total revenue",
                trap_name="Reversed judgement of elasticity magnitude and revenue after a price cut",
                fail_count=2,
                severity="medium",
                recommendation="Master the relation between marginal revenue and elasticity: MR = P(1 - 1/|Ed|)."
            )
        ]
    },
    "cs": {
        "title": "Computer Architecture",
        "radar": [92.0, 80.0, 85.0, 75.0, 88.0],
        "weak_points": [
            WeakPointItem(
                topic="Instruction-level parallelism · Tomasulo dynamic scheduling",
                trap_name="Conflating reservation-station renaming with the role of the reorder buffer (ROB)",
                fail_count=2,
                severity="high",
                recommendation="Remember that register renaming eliminates WAW/WAR hazards in the reservation stations, while in-order commit is guaranteed by the ROB."
            ),
            WeakPointItem(
                topic="Multi-level cache coherence · MESI protocol",
                trap_name="Missing invalidate broadcasts and Shared-state transitions",
                fail_count=1,
                severity="low",
                recommendation="Review the bus-snooping state-transition diagram."
            )
        ]
    },
    "se": {
        "title": "Software Engineering & UML 2.5",
        "radar": [86.0, 82.0, 84.0, 78.0, 90.0],
        "weak_points": [
            WeakPointItem(
                topic="UML 2.5 use-case modelling · include and extend relationships",
                trap_name="Confusing <<include>> base behaviour with <<extend>> optional extensions",
                fail_count=3,
                severity="high",
                recommendation="Remember: <<include>> denotes a subflow indispensable to executing the base use case; <<extend>> denotes an incremental flow inserted only when a specific extension point is met."
            ),
            WeakPointItem(
                topic="Agile estimation and the MoSCoW requirements traceability matrix",
                trap_name="Unclear boundary between Must-Have and Should-Have scope creep",
                fail_count=1,
                severity="low",
                recommendation="Against Ian Sommerville's 10th-edition requirements-engineering standard, lock down the runnable boundary of the PoC MVP."
            )
        ]
    },
    "or": {
        "title": "Operational Research",
        "radar": [82.0, 74.0, 80.0, 72.0, 78.0],
        "weak_points": [
            WeakPointItem(
                topic="Linear programming · feasible-region boundaries and non-negativity constraints",
                trap_name="Ignoring the non-negativity boundary conditions of decision variables",
                fail_count=1,
                severity="low",
                recommendation="Check the variable-sign constraints in the standard form and the range of validity of shadow prices."
            )
        ]
    },
    "mis": {
        "title": "Management Information Systems",
        "radar": [80.0, 76.0, 79.0, 74.0, 81.0],
        "weak_points": [
            WeakPointItem(
                topic="Information-system levels · the TPS/DSS boundary",
                trap_name="Conflating the data granularity of transaction processing and decision support",
                fail_count=1,
                severity="low",
                recommendation="Distinguish routine atomic transaction records from multi-dimensional aggregated analytical views."
            )
        ]
    },
    "prob_stat": {
        "title": "Probability Theory and Mathematical Statistics",
        "radar": [84.0, 73.0, 81.0, 70.0, 79.0],
        "weak_points": [
            WeakPointItem(
                topic="Bayes' theorem · prior base rates and conditional probability",
                trap_name="Base rate fallacy: confusing sensitivity with posterior probability",
                fail_count=2,
                severity="medium",
                recommendation="Expand the denominator with the law of total probability and avoid ignoring a low prior probability."
            )
        ]
    },
    "mkt": {
        "title": "Marketing Principles",
        "radar": [83.0, 77.0, 82.0, 75.0, 84.0],
        "weak_points": [
            WeakPointItem(
                topic="STP strategic positioning and Porter's competitive strategies",
                trap_name="Over-generalised positioning trap without a cost barrier",
                fail_count=1,
                severity="low",
                recommendation="Define the target segment and the differentiated value proposition clearly, and avoid being stuck in the middle."
            )
        ]
    },
    "eng": {
        "title": "Academic English",
        "radar": [85.0, 79.0, 80.0, 76.0, 82.0],
        "weak_points": [
            WeakPointItem(
                topic="IMRaD paper structure and academic hedges",
                trap_name="Absolutist causal claims replacing cautious qualified statements",
                fail_count=1,
                severity="low",
                recommendation="Distinguish the boundary of empirical observation from over-generalised statements."
            )
        ]
    },
    "ds": {
        "title": "Data Structures and Algorithms",
        "radar": [86.0, 78.0, 84.0, 74.0, 83.0],
        "weak_points": [
            WeakPointItem(
                topic="Complexity analysis and boundary conditions",
                trap_name="Mixing worst-case and amortised time complexity",
                fail_count=1,
                severity="low",
                recommendation="State clearly the upper bound on complexity for the given input size and the degenerate boundary cases."
            )
        ]
    },
}


class ReportService:
    """Service generating student telemetry summaries and trend analysis."""

    _MAX_ATTEMPTS = 2000
    _DIM_LABELS = [
        "Basic Recall",
        "Trap Defense",
        "Deductive Synthesis",
        "Boundary Migration",
        "Domain Breadth"
    ]
    _DIM_INDEX = {
        "recall": 0,
        "trapdefense": 1,
        "synthesis": 2,
        "boundary": 3,
        "precision": 4,
    }

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._attempts: List[Dict[str, Any]] = []

    def reset(self) -> None:
        """Clear in-memory session attempts (used for test isolation)."""
        with self._lock:
            self._attempts.clear()

    def record_attempt(
        self,
        *,
        subject: str,
        question_id: str,
        is_correct: bool,
        trap_name: Optional[str] = None,
        concept_name: Optional[str] = None,
        recommendation: str = "",
        radar_dimension: str = "trapDefense",
        score_delta: int = 0
    ) -> None:
        """Record a diagnosed student attempt into bounded thread-safe session memory."""
        canonical_sub = quiz_service.normalize_subject(subject) or (subject or "unknown").strip().lower()
        entry: Dict[str, Any] = {
            "subject": canonical_sub,
            "question_id": question_id,
            "is_correct": bool(is_correct),
            "trap_name": trap_name,
            "concept_name": concept_name or "Core concept",
            "recommendation": recommendation or "",
            "radar_dimension": radar_dimension or "trapDefense",
            "score_delta": int(score_delta),
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        with self._lock:
            self._attempts.append(entry)
            if len(self._attempts) > self._MAX_ATTEMPTS:
                del self._attempts[: len(self._attempts) - self._MAX_ATTEMPTS]

    def _resolve_scope(self, subject: Optional[str]) -> Tuple[bool, Optional[str], List[Dict[str, Any]]]:
        """Resolve subject filter and return matching attempt snapshot."""
        is_all = not subject or subject.strip().lower() in ["all", "global", "total", "overall"]
        canonical = None if is_all else quiz_service.normalize_subject(subject)
        with self._lock:
            snapshot = list(self._attempts)
        if is_all:
            return True, "all", snapshot
        filtered = [a for a in snapshot if a["subject"] == canonical]
        return False, canonical, filtered

    def get_summary(self, subject: Optional[str] = None) -> ReportSummaryResponse:
        """
        Generate aggregate learning summary report.
        Returns real session telemetry once attempts exist, otherwise honest demo baselines.
        """
        now_iso = datetime.now(timezone.utc).isoformat()
        is_all, canonical, filtered = self._resolve_scope(subject)

        if filtered:
            attempt_count = len(filtered)
            correct_count = sum(1 for a in filtered if a["is_correct"])
            accuracy_rate = round((correct_count / attempt_count) * 100.0, 1)
            diagnostic_count = attempt_count - correct_count

            grouped_traps: Dict[Tuple[str, str], Dict[str, Any]] = {}
            for a in filtered:
                if not a["is_correct"]:
                    topic = str(a["concept_name"] or "Core concept")
                    trap_label = str(a["trap_name"] or "Typical cognitive trap")
                    key = (topic, trap_label)
                    if key not in grouped_traps:
                        grouped_traps[key] = {
                            "count": 0,
                            "recommendation": str(a["recommendation"] or "")
                        }
                    grouped_traps[key]["count"] += 1

            sorted_traps = sorted(
                grouped_traps.items(),
                key=lambda item: item[1]["count"],
                reverse=True
            )
            weak_points: List[WeakPointItem] = []
            for (topic, trap_label), info in sorted_traps[:4]:
                cnt = info["count"]
                severity = "high" if cnt >= 3 else ("medium" if cnt == 2 else "low")
                weak_points.append(
                    WeakPointItem(
                        topic=topic,
                        trap_name=trap_label,
                        fail_count=cnt,
                        severity=severity,
                        recommendation=info["recommendation"]
                    )
                )

            cognitive_score = round(
                max(0.0, min(100.0, 50.0 + (accuracy_rate - 50.0) * 0.8 + min(10.0, correct_count * 1.0))),
                1
            )

            return ReportSummaryResponse(
                subject="all" if is_all else (canonical or str(subject)),
                attempt_count=attempt_count,
                correct_count=correct_count,
                accuracy_rate=accuracy_rate,
                diagnostic_count=diagnostic_count,
                traps_identified=len(grouped_traps),
                cognitive_score=cognitive_score,
                streak_days=1,
                data_source="live_session_telemetry",
                generated_at=now_iso,
                weak_points=weak_points
            )

        # Cold-start baseline (no recorded live attempts for requested scope yet)
        if is_all:
            all_weak_points: List[WeakPointItem] = []
            for code in ("law", "econ", "cs", "se"):
                all_weak_points.extend(DISCIPLINE_METADATA[code]["weak_points"])

            return ReportSummaryResponse(
                subject="all",
                attempt_count=18,
                correct_count=14,
                accuracy_rate=77.8,
                diagnostic_count=4,
                traps_identified=9,
                cognitive_score=86.5,
                streak_days=5,
                data_source="demo_baseline",
                generated_at=now_iso,
                weak_points=all_weak_points[:4]
            )

        if canonical in DISCIPLINE_METADATA:
            meta = DISCIPLINE_METADATA[canonical]
            return ReportSummaryResponse(
                subject=canonical,
                attempt_count=5,
                correct_count=4,
                accuracy_rate=80.0,
                diagnostic_count=1,
                traps_identified=len(meta["weak_points"]),
                cognitive_score=85.0,
                streak_days=5,
                data_source="demo_baseline",
                generated_at=now_iso,
                weak_points=meta["weak_points"]
            )

        # Unknown/adversarial subject graceful zero-state fallback (Never throw 500)
        return ReportSummaryResponse(
            subject=canonical or str(subject),
            attempt_count=0,
            correct_count=0,
            accuracy_rate=0.0,
            diagnostic_count=0,
            traps_identified=0,
            cognitive_score=50.0,
            streak_days=0,
            data_source="demo_baseline (empty)",
            generated_at=now_iso,
            weak_points=[]
        )

    def get_trend(self, subject: Optional[str] = None) -> ReportTrendResponse:
        """
        Generate multi-dimensional radar scores and misconception distribution.
        Computes real radar deltas when live attempts exist; otherwise returns honest demo baselines.
        """
        now_iso = datetime.now(timezone.utc).isoformat()
        dim_labels = list(self._DIM_LABELS)
        is_all, canonical, filtered = self._resolve_scope(subject)

        if filtered:
            scores = [75.0, 68.0, 72.0, 65.0, 78.0]
            trap_counts: Dict[Tuple[str, str], int] = {}

            for a in filtered:
                if a["is_correct"]:
                    scores[0] += 4.0
                    scores[1] += 5.0
                    scores[2] += 3.0
                    scores[4] += 2.0
                else:
                    dim_key = str(a.get("radar_dimension") or "trapDefense").strip().lower()
                    idx = self._DIM_INDEX.get(dim_key, 1)
                    scores[idx] -= 6.0
                    secondary_idx = 1 if idx == 3 else 3
                    scores[secondary_idx] -= 4.0

                    trap_label = str(a["trap_name"] or "Typical cognitive trap")
                    sub_code = str(a["subject"] or "unknown")
                    trap_counts[(trap_label, sub_code)] = trap_counts.get((trap_label, sub_code), 0) + 1

            clamped_scores = [round(max(30.0, min(100.0, s)), 1) for s in scores]
            trap_dist = [
                TrapDistributionItem(trap_name=t_name, subject=sub_code, count=cnt)
                for (t_name, sub_code), cnt in sorted(
                    trap_counts.items(),
                    key=lambda item: item[1],
                    reverse=True
                )
            ]

            return ReportTrendResponse(
                subject="all" if is_all else (canonical or str(subject)),
                dimensions=dim_labels,
                scores=clamped_scores,
                trap_distribution=trap_dist,
                data_source="live_session_telemetry",
                generated_at=now_iso
            )

        # Case 1: Overall global baseline
        if is_all:
            return ReportTrendResponse(
                subject="all",
                dimensions=dim_labels,
                scores=[86.0, 77.8, 85.5, 72.0, 85.0],
                trap_distribution=[
                    TrapDistributionItem(trap_name="Rescission period vs. limitation period", subject="law", count=3),
                    TrapDistributionItem(trap_name="Conflating omitted variables with collinearity", subject="econ", count=3),
                    TrapDistributionItem(trap_name="UML use-case Include/Extend confusion", subject="se", count=3),
                    TrapDistributionItem(trap_name="Reservation-station vs. ROB role confusion", subject="cs", count=2),
                    TrapDistributionItem(trap_name="Bona fide acquisition of escaped articles", subject="law", count=2),
                ],
                data_source="demo_baseline",
                generated_at=now_iso
            )

        # Case 2: Specific subject baseline
        if canonical in DISCIPLINE_METADATA:
            meta = DISCIPLINE_METADATA[canonical]
            traps = [
                TrapDistributionItem(trap_name=wp.trap_name, subject=canonical, count=wp.fail_count)
                for wp in meta["weak_points"]
            ]
            return ReportTrendResponse(
                subject=canonical,
                dimensions=dim_labels,
                scores=list(meta["radar"]),
                trap_distribution=traps,
                data_source="demo_baseline",
                generated_at=now_iso
            )

        # Case 3: Unknown subject boundary handling (Neutral baseline 50.0 across all dimensions)
        return ReportTrendResponse(
            subject=canonical or str(subject),
            dimensions=dim_labels,
            scores=[50.0, 50.0, 50.0, 50.0, 50.0],
            trap_distribution=[],
            data_source="demo_baseline (empty)",
            generated_at=now_iso
        )


# Global singleton instance
report_service = ReportService()
