"""
Report & Learning Telemetry Models
Defines Pydantic schemas for GET /api/reports/summary and GET /api/reports/trend.
Full camelCase / snake_case interoperability via CamelModel.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from pydantic import Field, model_validator
from backend.app.models.common import CamelModel


class WeakPointItem(CamelModel):
    """Represents a diagnosed fragile concept or frequent misconception trap."""
    topic: str = Field(..., description="Core concept or theorem name")
    trap_name: str = Field(..., description="Cognitive distractor trap title")
    trapName: Optional[str] = Field(None, description="CamelCase alias for trap_name")
    fail_count: int = Field(default=1, description="Number of times student fell into this trap")
    failCount: Optional[int] = Field(1, description="CamelCase alias for fail_count")
    severity: str = Field(default="medium", description="Severity level: low, medium, high")
    recommendation: str = Field(default="", description="Targeted revision guidance")

    @model_validator(mode="before")
    @classmethod
    def normalize_aliases(cls, data: Any) -> Any:
        if isinstance(data, dict):
            tn = data.get("trap_name") or data.get("trapName") or ""
            data["trap_name"] = tn
            data["trapName"] = tn

            fc = data.get("fail_count") if "fail_count" in data else data.get("failCount", 1)
            data["fail_count"] = fc
            data["failCount"] = fc
        return data

    @model_validator(mode="after")
    def sync_aliases(self) -> "WeakPointItem":
        self.trapName = self.trap_name
        self.failCount = self.fail_count
        return self


class ReportSummaryResponse(CamelModel):
    """
    Response payload for GET /api/reports/summary.
    Aggregates overall diagnostic metrics and mastery scores.
    """
    subject: Optional[str] = Field(default="all", description="Discipline filter applied (all, econ, cs, law, se)")
    attempt_count: int = Field(default=0, description="Total questions attempted in session")
    attemptCount: Optional[int] = Field(0, description="CamelCase alias for attempt_count")
    correct_count: int = Field(default=0, description="Total correctly answered questions")
    correctCount: Optional[int] = Field(0, description="CamelCase alias for correct_count")
    accuracy_rate: float = Field(default=0.0, description="Accuracy percentage: 0.0 - 100.0")
    accuracyRate: Optional[float] = Field(0.0, description="CamelCase alias for accuracy_rate")
    diagnostic_count: int = Field(default=0, description="Total times misconception diagnosis was triggered")
    diagnosticCount: Optional[int] = Field(0, description="CamelCase alias for diagnostic_count")
    traps_identified: int = Field(default=0, description="Unique distinct distractor traps recognized")
    trapsIdentified: Optional[int] = Field(0, description="CamelCase alias for traps_identified")
    cognitive_score: float = Field(default=50.0, description="Overall evaluated cognitive defense score: 0 - 100")
    cognitiveScore: Optional[float] = Field(50.0, description="CamelCase alias for cognitive_score")
    streak_days: int = Field(default=1, description="Active study streak in days")
    streakDays: Optional[int] = Field(1, description="CamelCase alias for streak_days")
    data_source: str = Field(default="session_telemetry", description="Provenance marker: session_telemetry, seed_baseline, or mock")
    dataSource: Optional[str] = Field("session_telemetry", description="CamelCase alias for data_source")
    generated_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat(), description="ISO 8601 generation timestamp")
    generatedAt: Optional[str] = Field(None, description="CamelCase alias for generated_at")
    weak_points: List[WeakPointItem] = Field(default_factory=list, description="Top diagnosed misconception bottlenecks")
    weakPoints: Optional[List[WeakPointItem]] = Field(default_factory=list, description="CamelCase alias for weak_points")

    @model_validator(mode="before")
    @classmethod
    def normalize_summary(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # Sync snake_case & camelCase aliases
            for snake, camel in [
                ("attempt_count", "attemptCount"),
                ("correct_count", "correctCount"),
                ("accuracy_rate", "accuracyRate"),
                ("diagnostic_count", "diagnosticCount"),
                ("traps_identified", "trapsIdentified"),
                ("cognitive_score", "cognitiveScore"),
                ("streak_days", "streakDays"),
                ("data_source", "dataSource"),
                ("generated_at", "generatedAt"),
                ("weak_points", "weakPoints")
            ]:
                val = data.get(snake) if snake in data else data.get(camel)
                if val is not None:
                    data[snake] = val
                    data[camel] = val
        return data

    @model_validator(mode="after")
    def sync_all(self) -> "ReportSummaryResponse":
        self.attemptCount = self.attempt_count
        self.correctCount = self.correct_count
        self.accuracyRate = self.accuracy_rate
        self.diagnosticCount = self.diagnostic_count
        self.trapsIdentified = self.traps_identified
        self.cognitiveScore = self.cognitive_score
        self.streakDays = self.streak_days
        self.dataSource = self.data_source
        self.generatedAt = self.generated_at or datetime.now(timezone.utc).isoformat()
        self.weakPoints = self.weak_points
        return self


class TrapDistributionItem(CamelModel):
    """Distribution of errors across misconception categories."""
    trap_name: str = Field(..., description="Trap name")
    trapName: Optional[str] = Field(None, description="CamelCase alias for trap_name")
    subject: str = Field(..., description="Subject code")
    count: int = Field(default=1, description="Trigger count")

    @model_validator(mode="before")
    @classmethod
    def normalize_aliases(cls, data: Any) -> Any:
        if isinstance(data, dict):
            tn = data.get("trap_name") or data.get("trapName") or ""
            data["trap_name"] = tn
            data["trapName"] = tn
        return data

    @model_validator(mode="after")
    def sync_aliases(self) -> "TrapDistributionItem":
        self.trapName = self.trap_name
        return self


class ReportTrendResponse(CamelModel):
    """
    Response payload for GET /api/reports/trend.
    Provides multi-dimensional radar scores and misconception frequency distribution.
    """
    subject: Optional[str] = Field(default="all", description="Discipline filter applied")
    dimensions: List[str] = Field(
        default_factory=lambda: [
            "Basic Recall",
            "Trap Defense",
            "Deductive Synthesis",
            "Boundary Migration",
            "Domain Breadth"
        ],
        description="Radar dimension labels"
    )
    scores: List[float] = Field(
        default_factory=lambda: [75.0, 68.0, 82.0, 70.0, 85.0],
        description="Radar scores corresponding to each dimension (0 - 100)"
    )
    trap_distribution: List[TrapDistributionItem] = Field(
        default_factory=list,
        description="Frequency breakdown across cognitive traps"
    )
    trapDistribution: Optional[List[TrapDistributionItem]] = Field(
        default_factory=list,
        description="CamelCase alias for trap_distribution"
    )
    data_source: str = Field(default="session_telemetry", description="Data provenance marker")
    dataSource: Optional[str] = Field("session_telemetry", description="CamelCase alias for data_source")
    generated_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
        description="ISO 8601 generation timestamp"
    )
    generatedAt: Optional[str] = Field(None, description="CamelCase alias for generated_at")

    @model_validator(mode="before")
    @classmethod
    def normalize_trend(cls, data: Any) -> Any:
        if isinstance(data, dict):
            td = data.get("trap_distribution") if "trap_distribution" in data else data.get("trapDistribution", [])
            data["trap_distribution"] = td
            data["trapDistribution"] = td

            ds = data.get("data_source") if "data_source" in data else data.get("dataSource", "session_telemetry")
            data["data_source"] = ds
            data["dataSource"] = ds

            ga = data.get("generated_at") or data.get("generatedAt") or datetime.now(timezone.utc).isoformat()
            data["generated_at"] = ga
            data["generatedAt"] = ga
        return data

    @model_validator(mode="after")
    def sync_trend(self) -> "ReportTrendResponse":
        self.trapDistribution = self.trap_distribution
        self.dataSource = self.data_source
        self.generatedAt = self.generated_at
        return self
