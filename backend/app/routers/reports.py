"""
Reports & Learning Telemetry Router
Provides GET /api/reports/summary and GET /api/reports/trend.
"""

from typing import Optional
from fastapi import APIRouter, Query
from backend.app.models.report import ReportSummaryResponse, ReportTrendResponse
from backend.app.services.report_service import report_service

router = APIRouter(tags=["Reports & Analytics"])


@router.get("/reports/summary", response_model=ReportSummaryResponse)
def get_report_summary(
    subject: Optional[str] = Query(
        None,
        description="Optional discipline code (law, econ, cs, se) or 'all'"
    )
) -> ReportSummaryResponse:
    """
    Retrieve comprehensive learning summary metrics for the active session.
    Provides total attempts, accuracy rate, distractor traps identified,
    overall cognitive defense score, and top fragile topics.
    """
    return report_service.get_summary(subject=subject)


@router.get("/reports/trend", response_model=ReportTrendResponse)
def get_report_trend(
    subject: Optional[str] = Query(
        None,
        description="Optional discipline code (law, econ, cs, se) or 'all'"
    )
) -> ReportTrendResponse:
    """
    Retrieve multi-dimensional radar telemetry and misconception frequency distribution.
    Powers ECharts 5.5.1 cognitive radar profile and misconception breakdown charts.
    """
    return report_service.get_trend(subject=subject)
