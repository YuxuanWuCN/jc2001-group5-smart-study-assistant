"""
Student Authentication and Profile Management Service.
Handles student identification, demo account switching, and profile state.
"""

from datetime import datetime
from typing import Dict, List, Optional
from backend.app.models.auth import StudentProfile, AuthResponse, DemoUsersResponse


# Pre-configured team member roster (10 members of JC2001 Group 5 + Guest Demo)
DEMO_STUDENTS: List[StudentProfile] = [
    StudentProfile(
        id="50106070",
        name="吴宇轩",
        role="BSc BMIS · 组长 / 项目经理",
        avatar="吴",
        preferred_subject="law",
        subject_label="⚖️ 民商法学",
        streak_days=5
    ),
    StudentProfile(
        id="50106038",
        name="林泳桐",
        role="BSc BMIS · 需求与业务主管",
        avatar="林",
        preferred_subject="econ",
        subject_label="📈 计量经济学",
        streak_days=4
    ),
    StudentProfile(
        id="50106045",
        name="王思鉴",
        role="BSc BMIS · 系统架构师",
        avatar="王",
        preferred_subject="cs",
        subject_label="💻 计算机体系结构",
        streak_days=4
    ),
    StudentProfile(
        id="50106065",
        name="江昊",
        role="BSc BMIS · PoC 开发主管",
        avatar="江",
        preferred_subject="se",
        subject_label="⚙️ 软件工程",
        streak_days=6
    ),
    StudentProfile(
        id="50106034",
        name="谢炜昕",
        role="BSc BMIS · 技术报告与概念主管",
        avatar="谢",
        preferred_subject="law",
        subject_label="⚖️ 民商法学",
        streak_days=5
    ),
    StudentProfile(
        id="50106035",
        name="张梓健",
        role="BSc BMIS · 业务分析与用例主管",
        avatar="张",
        preferred_subject="econ",
        subject_label="📈 计量经济学",
        streak_days=3
    ),
    StudentProfile(
        id="50105989",
        name="习羽赛",
        role="BSc BMIS · UI/UX 交互设计主管",
        avatar="习",
        preferred_subject="se",
        subject_label="⚙️ 软件工程",
        streak_days=4
    ),
    StudentProfile(
        id="50106060",
        name="董思钦",
        role="BSc BMIS · 算法与逻辑开发主管",
        avatar="董",
        preferred_subject="cs",
        subject_label="💻 计算机体系结构",
        streak_days=5
    ),
    StudentProfile(
        id="50106061",
        name="杨明杰",
        role="BSc BMIS · 测试与质量主管",
        avatar="杨",
        preferred_subject="se",
        subject_label="⚙️ 软件工程",
        streak_days=3
    ),
    StudentProfile(
        id="50106037",
        name="梁子铉",
        role="BSc BMIS · 部署与媒体主管",
        avatar="梁",
        preferred_subject="cs",
        subject_label="💻 计算机体系结构",
        streak_days=4
    ),
    StudentProfile(
        id="guest",
        name="访客体验生",
        role="Guest Student · 快速体验通道",
        avatar="客",
        preferred_subject="se",
        subject_label="⚙️ 软件工程",
        streak_days=1
    )
]

SUBJECT_LABELS: Dict[str, str] = {
    "law": "⚖️ 民商法学",
    "cs": "💻 计算机体系结构",
    "econ": "📈 计量经济学",
    "se": "⚙️ 软件工程"
}


class AuthService:
    """Authentication and identity service implementation."""

    @classmethod
    def get_demo_users(cls) -> DemoUsersResponse:
        """Returns the full roster of demo student accounts."""
        return DemoUsersResponse(
            status="ok",
            total=len(DEMO_STUDENTS),
            data=DEMO_STUDENTS
        )

    @classmethod
    def login(cls, student_id: str, password: Optional[str] = None) -> AuthResponse:
        """
        Authenticate by student ID or name.
        Matches pre-configured members, or provisions a dynamic student profile for any valid name.
        """
        clean_id = student_id.strip() if student_id else ""
        if not clean_id:
            clean_id = "50106070"

        # 1. Match against pre-configured student roster
        matched = next(
            (s for s in DEMO_STUDENTS if s.id.lower() == clean_id.lower() or s.name.lower() == clean_id.lower()),
            None
        )

        if matched:
            user = matched
        else:
            # 2. Dynamic student profile fallback for new students
            avatar_char = clean_id[0] if clean_id else "学"
            user = StudentProfile(
                id=clean_id if clean_id.isdigit() else f"STU-{abs(hash(clean_id)) % 10000:04d}",
                name=clean_id,
                role="BSc BMIS · 独立研习档案",
                avatar=avatar_char,
                preferred_subject="se",
                subject_label="⚙️ 软件工程",
                streak_days=1
            )

        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        token = f"sess_{user.id}_{timestamp}"

        return AuthResponse(
            status="ok",
            message=f"Welcome back, {user.name}!",
            session_token=token,
            user=user
        )

    @classmethod
    def register(
        cls,
        student_id: str,
        name: str,
        preferred_subject: str = "se",
        password: Optional[str] = None
    ) -> AuthResponse:
        """Register a newly provisioned student profile."""
        clean_id = student_id.strip() if student_id else f"STU-{int(datetime.now().timestamp()) % 100000}"
        clean_name = name.strip() if name else "新同学"
        sub = preferred_subject.lower() if preferred_subject in SUBJECT_LABELS else "se"
        sub_label = SUBJECT_LABELS.get(sub, "⚙️ 软件工程")

        user = StudentProfile(
            id=clean_id,
            name=clean_name,
            role="BSc BMIS · 新生研习档案",
            avatar=clean_name[0] if clean_name else "学",
            preferred_subject=sub,
            subject_label=sub_label,
            streak_days=1
        )

        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        token = f"sess_{user.id}_{timestamp}"

        return AuthResponse(
            status="ok",
            message=f"Account created successfully for {user.name}.",
            session_token=token,
            user=user
        )
