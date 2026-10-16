"""
FastAPI Router for Student Authentication & Identity Endpoints.
Endpoints:
  GET  /api/auth/demo-users -> List pre-configured demo student accounts
  POST /api/auth/login      -> Authenticate student by ID or name
  POST /api/auth/register   -> Provision new student profile
"""

from fastapi import APIRouter, status
from backend.app.models.auth import (
    LoginRequest,
    RegisterRequest,
    AuthResponse,
    DemoUsersResponse
)
from backend.app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get(
    "/demo-users",
    response_model=DemoUsersResponse,
    status_code=status.HTTP_200_OK,
    summary="Get demo student accounts",
    description="Returns list of pre-configured 10-person JC2001 Group 5 members plus guest account."
)
async def get_demo_users():
    """Retrieve all available demo student accounts."""
    return AuthService.get_demo_users()


@router.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Student Login / Identification",
    description="Authenticates student by student ID or name, loading personal mastery profile."
)
async def login(req: LoginRequest):
    """Log in as a student using student ID or name."""
    return AuthService.login(
        student_id=req.student_id,
        password=req.password
    )


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Student Profile Registration",
    description="Registers a new student learner profile with designated major discipline."
)
async def register(req: RegisterRequest):
    """Register a new student profile."""
    return AuthService.register(
        student_id=req.student_id,
        name=req.name,
        preferred_subject=req.preferred_subject,
        password=req.password
    )
