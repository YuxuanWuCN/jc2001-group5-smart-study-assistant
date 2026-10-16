"""
Pydantic data models for Student Authentication & Identity Management.
Conforms to specs/001-landing-and-auth-portal/contracts/portal-auth-contracts.md
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class StudentProfile(BaseModel):
    """Represents a student learner profile with academic metadata."""
    id: str = Field(..., description="Student matriculation ID or identifier", example="50106070")
    name: str = Field(..., description="Student full name", example="吴宇轩")
    role: str = Field(..., description="Academic role or program description", example="BSc BMIS · Project Manager")
    avatar: str = Field(..., description="Avatar character or icon", example="吴")
    preferred_subject: str = Field("law", description="Initial enrolled discipline", example="law")
    subject_label: Optional[str] = Field("⚖️ 民商法学", description="Human-readable subject name")
    streak_days: int = Field(3, description="Continuous study streak in days", ge=0)


class LoginRequest(BaseModel):
    """Request payload for student login."""
    student_id: str = Field(..., description="Student ID or name", example="50106070")
    password: Optional[str] = Field(None, description="Access credential (optional in PoC demo)", example="123456")


class RegisterRequest(BaseModel):
    """Request payload for creating a new student profile."""
    student_id: str = Field(..., description="Student ID", example="50106099")
    name: str = Field(..., description="Full student name", example="陈同学")
    preferred_subject: str = Field("se", description="Major discipline code", example="se")
    password: Optional[str] = Field(None, description="Password credential", example="123456")


class AuthResponse(BaseModel):
    """Standard authentication response."""
    status: str = Field("ok", example="ok")
    message: str = Field("Login successful", example="Login successful")
    session_token: str = Field(..., example="sess_50106070_20261017")
    user: StudentProfile


class DemoUsersResponse(BaseModel):
    """List of pre-configured group demo student accounts."""
    status: str = Field("ok", example="ok")
    total: int = Field(..., example=11)
    data: List[StudentProfile]
