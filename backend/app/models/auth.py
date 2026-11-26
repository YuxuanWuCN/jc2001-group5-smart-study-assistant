"""
Pydantic data models for Student Authentication & Identity Management.
Conforms to specs/001-landing-and-auth-portal/contracts/portal-auth-contracts.md
"""

from typing import List, Optional
from pydantic import Field

from backend.app.models.common import CamelModel


class StudentProfile(CamelModel):
    """Represents a student learner profile with academic metadata."""
    id: str = Field(..., description="Student matriculation ID or identifier", json_schema_extra={"example": "50106070"})
    name: str = Field(..., description="Student full name", json_schema_extra={"example": "Wu Yuxuan"})
    role: str = Field(..., description="Academic role or program description", json_schema_extra={"example": "BSc BMIS · Project Manager"})
    avatar: str = Field(..., description="Avatar character or icon", json_schema_extra={"example": "W"})
    preferred_subject: str = Field("law", description="Initial enrolled discipline", json_schema_extra={"example": "law"})
    subject_label: Optional[str] = Field("⚖️ Civil and Commercial Law", description="Human-readable subject name")
    streak_days: int = Field(3, description="Continuous study streak in days", ge=0)


class LoginRequest(CamelModel):
    """Request payload for student login."""
    student_id: str = Field(..., description="Student ID or name", json_schema_extra={"example": "50106070"})
    password: Optional[str] = Field(None, description="Access credential (optional in PoC demo)", json_schema_extra={"example": "123456"})


class RegisterRequest(CamelModel):
    """Request payload for creating a new student profile."""
    student_id: str = Field(..., description="Student ID", json_schema_extra={"example": "50106099"})
    name: str = Field(..., description="Full student name", json_schema_extra={"example": "Chen"})
    preferred_subject: str = Field("se", description="Major discipline code", json_schema_extra={"example": "se"})
    password: Optional[str] = Field(None, description="Password credential", json_schema_extra={"example": "123456"})


class AuthResponse(CamelModel):
    """Standard authentication response."""
    status: str = Field("ok", json_schema_extra={"example": "ok"})
    message: str = Field("Login successful", json_schema_extra={"example": "Login successful"})
    session_token: str = Field(..., json_schema_extra={"example": "sess_50106070_20261017"})
    user: StudentProfile


class DemoUsersResponse(CamelModel):
    """List of pre-configured group demo student accounts."""
    status: str = Field("ok", json_schema_extra={"example": "ok"})
    total: int = Field(..., json_schema_extra={"example": 11})
    data: List[StudentProfile]
