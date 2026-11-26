"""
Student Authentication and Profile Management Service.
Handles student identification, demo account switching, and profile state.
"""

import hashlib
import hmac
import secrets
import threading
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from fastapi import HTTPException, status
from backend.app.models.auth import StudentProfile, AuthResponse, DemoUsersResponse


# Pre-configured team member roster (11 members of JC2001 Group 5 + Guest Demo)
DEMO_STUDENTS: List[StudentProfile] = [
    StudentProfile(
        id="50106070",
        name="Wu Yuxuan",
        role="BSc BMIS · Team Lead / Project Manager",
        avatar="W",
        preferred_subject="law",
        subject_label="⚖️ Civil and Commercial Law",
        streak_days=5
    ),
    StudentProfile(
        id="50106038",
        name="Lin Yongtong",
        role="BSc BMIS · Requirements and Business Lead",
        avatar="L",
        preferred_subject="econ",
        subject_label="📈 Econometrics",
        streak_days=4
    ),
    StudentProfile(
        id="50106045",
        name="Wang Sijian",
        role="BSc BMIS · System Architect",
        avatar="W",
        preferred_subject="cs",
        subject_label="💻 Computer Architecture",
        streak_days=4
    ),
    StudentProfile(
        id="50106065",
        name="Jiang Hao",
        role="BSc BMIS · PoC Development Lead",
        avatar="J",
        preferred_subject="se",
        subject_label="⚙️ Software Engineering",
        streak_days=6
    ),
    StudentProfile(
        id="50106034",
        name="Xie Weixin",
        role="BSc BMIS · Technical Report and Concepts Lead",
        avatar="X",
        preferred_subject="law",
        subject_label="⚖️ Civil and Commercial Law",
        streak_days=5
    ),
    StudentProfile(
        id="50106035",
        name="Zhang Zijian",
        role="BSc BMIS · Business Analysis and Use Cases Lead",
        avatar="Z",
        preferred_subject="econ",
        subject_label="📈 Econometrics",
        streak_days=3
    ),
    StudentProfile(
        id="50105989",
        name="Xi Yusai",
        role="BSc BMIS · UI/UX Interaction Design Lead",
        avatar="X",
        preferred_subject="se",
        subject_label="⚙️ Software Engineering",
        streak_days=4
    ),
    StudentProfile(
        id="50106060",
        name="Dong Siqin",
        role="BSc BMIS · Algorithms and Logic Development Lead",
        avatar="D",
        preferred_subject="cs",
        subject_label="💻 Computer Architecture",
        streak_days=5
    ),
    StudentProfile(
        id="50106061",
        name="Yang Mingjie",
        role="BSc BMIS · Testing and Quality Lead",
        avatar="Y",
        preferred_subject="se",
        subject_label="⚙️ Software Engineering",
        streak_days=3
    ),
    StudentProfile(
        id="50106037",
        name="Liang Zixuan",
        role="BSc BMIS · Deployment and Media Lead",
        avatar="L",
        preferred_subject="cs",
        subject_label="💻 Computer Architecture",
        streak_days=4
    ),
    StudentProfile(
        id="50106012",
        name="Luo Wenxi",
        role="BSc BMIS · Quality Assurance and Data Validation",
        avatar="L",
        preferred_subject="econ",
        subject_label="📈 Econometrics",
        streak_days=4
    ),
    StudentProfile(
        id="guest",
        name="Guest Student",
        role="Guest Student · Quick experience channel",
        avatar="G",
        preferred_subject="se",
        subject_label="⚙️ Software Engineering",
        streak_days=1
    )
]

SUBJECT_LABELS: Dict[str, str] = {
    "law": "⚖️ Civil and Commercial Law",
    "cs": "💻 Computer Architecture",
    "econ": "📈 Econometrics",
    "se": "⚙️ Software Engineering",
    "or": "📐 Operations Research",
    "mis": "🌐 Management Information Systems",
    "prob_stat": "🎲 Probability and Mathematical Statistics",
    "mkt": "🎯 Marketing Principles",
    "eng": "✍️ Academic English",
    "ds": "🧩 Data Structures and Algorithms",
}


def _hash_password(password: str, salt: Optional[str] = None) -> Tuple[str, str]:
    """Derive a salted PBKDF2-HMAC-SHA256 credential digest."""
    salt_hex = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt_hex.encode("utf-8"),
        100_000,
    ).hex()
    return salt_hex, digest


def _verify_password(password: str, salt: str, expected_hash: str) -> bool:
    """Constant-time verification against a stored salted PBKDF2 digest."""
    _, actual_hash = _hash_password(password, salt=salt)
    return hmac.compare_digest(actual_hash, expected_hash)


class AuthService:
    """Authentication and identity service implementation."""

    _lock = threading.Lock()
    _registered_users: Dict[str, StudentProfile] = {}
    _password_hashes: Dict[str, Tuple[str, str]] = {}

    @classmethod
    def reset(cls) -> None:
        """Clear dynamically registered users and credential hashes (used for test isolation)."""
        with cls._lock:
            cls._registered_users.clear()
            cls._password_hashes.clear()

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
        Matches pre-configured demo members (zero-barrier), verifies registered passwords,
        or provisions a deterministic student profile for an unlisted name.
        """
        clean_id = student_id.strip() if student_id else ""
        if not clean_id:
            clean_id = "50106070"

        # 1. Match against pre-configured zero-barrier demo roster
        matched = next(
            (s for s in DEMO_STUDENTS if s.id.lower() == clean_id.lower() or s.name.lower() == clean_id.lower()),
            None
        )

        if matched:
            user = matched
        else:
            # 2. Match against registered in-session users (with password verification when set)
            with cls._lock:
                matched_reg = next(
                    (
                        u for u in cls._registered_users.values()
                        if u.id.lower() == clean_id.lower() or u.name.lower() == clean_id.lower()
                    ),
                    None
                )
                cred = cls._password_hashes.get(matched_reg.id.lower()) if matched_reg else None

            if matched_reg is not None:
                if cred is not None:
                    salt_hex, expected_hash = cred
                    if not password or not _verify_password(password, salt_hex, expected_hash):
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid student credentials"
                        )
                user = matched_reg
            else:
                # 3. Deterministic student profile fallback for new unlisted students
                avatar_char = clean_id[0] if clean_id else "S"
                digest = hashlib.sha256(clean_id.encode("utf-8")).hexdigest()[:6]
                user = StudentProfile(
                    id=clean_id if clean_id.isdigit() else f"STU-{digest}",
                    name=clean_id,
                    role="BSc BMIS · Independent study profile",
                    avatar=avatar_char,
                    preferred_subject="se",
                    subject_label="⚙️ Software Engineering",
                    streak_days=1
                )

        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        token = f"sess_{user.id}_{timestamp}_{secrets.token_hex(6)}"

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
        """Register and store a newly provisioned student profile with optional salted password."""
        clean_id = student_id.strip() if student_id else f"STU-{int(datetime.now().timestamp()) % 100000}"
        clean_name = name.strip() if name else "New Student"
        raw_sub = (preferred_subject or "se").strip().lower()
        sub = raw_sub if raw_sub in SUBJECT_LABELS else "se"
        sub_label = SUBJECT_LABELS.get(sub, "⚙️ Software Engineering")

        user = StudentProfile(
            id=clean_id,
            name=clean_name,
            role="BSc BMIS · New student study profile",
            avatar=clean_name[0] if clean_name else "S",
            preferred_subject=sub,
            subject_label=sub_label,
            streak_days=1
        )

        key = clean_id.lower()
        with cls._lock:
            cls._registered_users[key] = user
            if password:
                cls._password_hashes[key] = _hash_password(password)
            else:
                cls._password_hashes.pop(key, None)

        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        token = f"sess_{user.id}_{timestamp}_{secrets.token_hex(6)}"

        return AuthResponse(
            status="ok",
            message=f"Account created successfully for {user.name}.",
            session_token=token,
            user=user
        )
