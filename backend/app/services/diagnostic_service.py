"""
Dual-Mode Diagnostic Engine Service
Supports DashScope Qwen-Turbo LLM inference with 4s timeout and robust offline local knowledge fallback.
Never returns unhandled 500 exceptions.
"""

import logging
import re
from typing import Optional, List, Tuple
import httpx

from backend.app.config import settings
from backend.app.models.quiz import QuizItem, TrapDetail, OptionItem
from backend.app.models.diagnose import DiagnoseRequest, DiagnoseResponse
from backend.app.services.quiz_service import quiz_service
from backend.app.services.report_service import report_service

logger = logging.getLogger("diagnostic_engine")


def _normalize_blank_answer(value: Optional[str]) -> str:
    """Normalize fill-in-the-blank answers for case- and delimiter-tolerant matching."""
    text = str(value or "").strip().lower()
    text = re.sub(r"[,;:/]", ",", text)
    text = text.replace("−", "-")
    text = re.sub(r"\s+", " ", text)
    return text


class DiagnosticService:
    """Diagnostic Service implementing dual-mode cognitive evaluation."""

    def __init__(self, timeout: float = 4.0):
        self.timeout = timeout

    async def _call_dashscope_qwen(
        self,
        question: QuizItem,
        selected_key: str,
        trap_title: str,
        prerequisite: str
    ) -> Optional[str]:
        """
        Call DashScope Qwen-Turbo API with strict timeout.
        Returns generated Socratic guidance or None on failure.
        """
        if not settings.has_api_key:
            return None

        headers = {
            "Authorization": f"Bearer {settings.QWEN_API_KEY.strip()}",
            "Content-Type": "application/json"
        }

        system_prompt = (
            "You are a rigorous and incisive Socratic tutor for university subjects. "
            "Your task is to ask probing, guiding questions about the cognitive traps and prerequisite blind spots "
            "that students hit while answering questions. "
            "Absolute commands: 1. Never state the correct option letter directly; 2. Stay anchored to the prerequisite "
            "theorems and common-error blind spots of the examination point; 3. Use follow-up questioning to prompt "
            "students to reflect, in an approachable yet academically rigorous tone, strictly within 120 words."
        )

        user_content = (
            f"[Question stem]: {question.stem}\n"
            f"[Student's wrong choice]: option {selected_key}\n"
            f"[Trap set by the examiner]: {trap_title}\n"
            f"[Knowledge blind spot / prerequisite]: {prerequisite}\n"
            "Now give a Socratic follow-up and hint that does not reveal the answer:"
        )

        payload = {
            "model": settings.QWEN_MODEL,
            "input": {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ]
            },
            "parameters": {
                "result_format": "message",
                "max_tokens": 200,
                "temperature": 0.7
            }
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(settings.DASHSCOPE_URL, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                output = data.get("output", {})
                choices = output.get("choices", [])
                if choices and "message" in choices[0]:
                    return choices[0]["message"].get("content", "").strip()
                elif "text" in output:
                    return output.get("text", "").strip()
            else:
                logger.warning(f"DashScope API returned HTTP {resp.status_code}: {resp.text}")
        return None

    async def _resolve_socratic_guidance(
        self,
        question: QuizItem,
        selected_key: str,
        trap_title: str,
        prerequisite: str,
        fallback_socratic: str,
        include_socratic: bool
    ) -> Tuple[str, bool, str]:
        """Attempt live Qwen Socratic rephrasing when enabled, falling back safely offline."""
        socratic_text: Optional[str] = None
        model_used = "local-knowledge-seed"
        fallback_mode = True

        if settings.has_api_key and include_socratic:
            try:
                socratic_text = await self._call_dashscope_qwen(
                    question=question,
                    selected_key=selected_key,
                    trap_title=trap_title,
                    prerequisite=prerequisite
                )
                if socratic_text and socratic_text.strip():
                    fallback_mode = False
                    model_used = settings.QWEN_MODEL
            except Exception as e:
                logger.warning(f"Live Qwen LLM call exception ({e}), engaging local seed fallback.")
                socratic_text = None

        if not socratic_text:
            socratic_text = fallback_socratic
            fallback_mode = True
            model_used = "local-knowledge-seed"

        return socratic_text, fallback_mode, model_used

    async def diagnose_answer(self, req: DiagnoseRequest) -> DiagnoseResponse:
        """
        Main asynchronous diagnostic entrypoint.
        Guaranteed to return HTTP 200 DiagnoseResponse with zero 500 exceptions.
        """
        try:
            # 1. Resolve question from repository
            q_id = req.question_id
            question = quiz_service.get_question_by_id(q_id)
            
            # If not found by given ID, return graceful safe fallback without polluting telemetry
            if not question:
                logger.warning(f"Question id '{q_id}' not found in database, using graceful safe fallback.")
                return DiagnoseResponse(
                    is_correct=False,
                    question_id=q_id or "unknown",
                    selected_key=req.selected_key or "A",
                    correct_key="B",
                    explanation="Could not locate the specified question id, so the system has engaged the knowledge-ontology emergency fallback mode.",
                    trap_id="trap_fallback",
                    trap_title="🚨 Question lookup miss",
                    trap_name="Question lookup miss",
                    concept_name="Concept boundary retrieval and matching",
                    misconception="No matching question id was found in the question-bank index",
                    prerequisite="System question-ontology integrity",
                    radar_dimension="boundary",
                    score_delta=-2,
                    socratic_guidance="Please check that the question index is valid, and try deriving from the foundational conceptual theorems of this subject.",
                    socratic_hint="Please check that the question index is valid, and try deriving from the foundational conceptual theorems of this subject.",
                    knowledge_nodes=["Concept retrieval", "Basic assumptions"],
                    fallback_mode=True,
                    model_used="local-safe-fallback"
                )

            # Extract graph concept nodes if available
            knowledge_nodes: List[str] = []
            if question.graph and question.graph.nodes:
                knowledge_nodes = [node.label for node in question.graph.nodes]
            elif question.tag:
                knowledge_nodes = [question.tag]

            # 2a. Handle fill-in-the-blank items
            if question.question_type == "fill_blank":
                raw_text = (
                    req.user_answer_text
                    if req.user_answer_text is not None
                    else (req.selected_key or req.selected_option or "")
                )
                accepted_raw = list(question.blank_answers or [])
                if not accepted_raw and question.answer:
                    accepted_raw = [question.answer]

                norm_input = _normalize_blank_answer(raw_text)
                is_correct = bool(norm_input) and any(
                    _normalize_blank_answer(ans) == norm_input for ans in accepted_raw
                )
                canonical_answer = question.answer or (accepted_raw[0] if accepted_raw else "")

                if is_correct:
                    report_service.record_attempt(
                        subject=question.subject,
                        question_id=question.id,
                        is_correct=True,
                        trap_name=None,
                        concept_name=question.tag or "Core concept",
                        recommendation="",
                        radar_dimension="recall",
                        score_delta=5
                    )
                    guidance = question.explanation or "The blank answer matched the core concept exactly!"
                    return DiagnoseResponse(
                        is_correct=True,
                        question_id=question.id,
                        selected_key=raw_text.strip(),
                        correct_key=canonical_answer,
                        explanation=question.explanation,
                        trap_id=None,
                        trap_title=None,
                        trap_name=None,
                        concept_name=question.tag or "Examination concept matched exactly",
                        misconception=None,
                        prerequisite="Mastered the definition of this core concept",
                        radar_dimension="recall",
                        score_delta=5,
                        socratic_guidance=guidance,
                        socratic_hint=guidance,
                        knowledge_nodes=knowledge_nodes,
                        fallback_mode=False,
                        model_used="rule-evaluation"
                    )

                trap_title = "🚨 Concept blank-answer wording deviation"
                prerequisite = question.tag or "Course foundational concept"
                misconception = f"The submitted answer deviates from the standard formulation (reference answer: {canonical_answer})."
                fallback_socratic = (
                    question.socratic_prompt
                    or question.explanation
                    or "Please review the core definition and standard terminology of this examination point."
                )
                socratic_text, fallback_mode, model_used = await self._resolve_socratic_guidance(
                    question=question,
                    selected_key=raw_text.strip() or "(empty)",
                    trap_title=trap_title,
                    prerequisite=prerequisite,
                    fallback_socratic=fallback_socratic,
                    include_socratic=req.include_socratic
                )
                report_service.record_attempt(
                    subject=question.subject,
                    question_id=question.id,
                    is_correct=False,
                    trap_name=trap_title,
                    concept_name=prerequisite,
                    recommendation=question.explanation or prerequisite,
                    radar_dimension="precision",
                    score_delta=-5
                )
                return DiagnoseResponse(
                    is_correct=False,
                    question_id=question.id,
                    selected_key=raw_text.strip(),
                    correct_key=canonical_answer,
                    explanation=question.explanation,
                    trap_id=f"trap_blank_{question.id}",
                    trap_title=trap_title,
                    trap_name=trap_title,
                    concept_name=prerequisite,
                    misconception=misconception,
                    prerequisite=prerequisite,
                    radar_dimension="precision",
                    score_delta=-5,
                    socratic_guidance=socratic_text,
                    socratic_hint=socratic_text,
                    knowledge_nodes=knowledge_nodes,
                    fallback_mode=fallback_mode,
                    model_used=model_used
                )

            # 2b. Determine selected option key for multiple-choice items
            selected_key = (req.selected_key or req.selected_option or "A").strip().upper()
            
            # 3. Locate correct option and student option
            correct_opt: Optional[OptionItem] = None
            student_opt: Optional[OptionItem] = None
            
            if isinstance(question.options, list):
                for opt in question.options:
                    if isinstance(opt, OptionItem):
                        if opt.is_correct or (question.answer and opt.key.upper() == question.answer.upper()):
                            correct_opt = opt
                        if opt.key.upper() == selected_key:
                            student_opt = opt
                    elif isinstance(opt, dict):
                        if opt.get("is_correct") or opt.get("isCorrect") or (question.answer and opt.get("key", "").upper() == question.answer.upper()):
                            correct_opt = OptionItem(**opt)
                        if opt.get("key", "").upper() == selected_key:
                            student_opt = OptionItem(**opt)

            correct_key = correct_opt.key.upper() if correct_opt else (question.answer or "A").upper()
            is_correct = (selected_key == correct_key)

            # 4. Handle correct option
            if is_correct:
                report_service.record_attempt(
                    subject=question.subject,
                    question_id=question.id,
                    is_correct=True,
                    trap_name=None,
                    concept_name=question.tag or "Core concept",
                    recommendation="",
                    radar_dimension="trapDefense",
                    score_delta=5
                )
                return DiagnoseResponse(
                    is_correct=True,
                    question_id=question.id,
                    selected_key=selected_key,
                    correct_key=correct_key,
                    explanation=question.explanation,
                    trap_id=None,
                    trap_title=None,
                    trap_name=None,
                    concept_name="Examination concept matched exactly",
                    misconception=None,
                    prerequisite="Fully mastered the core theorem and boundary conditions of this knowledge point",
                    radar_dimension="trapDefense",
                    score_delta=5,
                    socratic_guidance="Excellent! The examination point was hit precisely and the trap was successfully avoided! Both the solidity of your foundational concepts and your trap-defence index have improved.",
                    socratic_hint="Excellent! The examination point was hit precisely and the trap was successfully avoided! Both the solidity of your foundational concepts and your trap-defence index have improved.",
                    knowledge_nodes=knowledge_nodes,
                    fallback_mode=False,
                    model_used="rule-evaluation"
                )

            # 5. Handle incorrect option (distractor trap hit)
            trap_id = student_opt.trap_id if student_opt and student_opt.trap_id else None
            trap: Optional[TrapDetail] = None
            if trap_id and question.traps and trap_id in question.traps:
                trap = question.traps[trap_id]
            elif question.traps:
                trap_id = next(iter(question.traps.keys()))
                trap = question.traps[trap_id]

            trap_title = trap.title if trap else "🚨 Core-concept comprehension deviation trap"
            misconception = trap.desc if trap else "This option touches a typical cognitive blind spot of this subject's examination point."
            prerequisite = trap.prereq if trap else (question.tag or "Prerequisite theorems and conceptual boundaries")
            radar_dim = trap.radar_hit if trap else "trapDefense"
            fallback_socratic = (
                question.socratic_prompt 
                or (trap.desc if trap else "Recall the strict mathematical or legal boundary conditions of the relevant prerequisite theorem.")
            )

            # 6. Dual-Mode Evaluation: Attempt Live LLM with timeout, else Graceful Fallback
            socratic_text, fallback_mode, model_used = await self._resolve_socratic_guidance(
                question=question,
                selected_key=selected_key,
                trap_title=trap_title,
                prerequisite=prerequisite,
                fallback_socratic=fallback_socratic,
                include_socratic=req.include_socratic
            )

            report_service.record_attempt(
                subject=question.subject,
                question_id=question.id,
                is_correct=False,
                trap_name=trap_title,
                concept_name=prerequisite,
                recommendation=misconception,
                radar_dimension=radar_dim,
                score_delta=-5
            )

            return DiagnoseResponse(
                is_correct=False,
                question_id=question.id,
                selected_key=selected_key,
                correct_key=correct_key,
                explanation=question.explanation,
                trap_id=trap_id,
                trap_title=trap_title,
                trap_name=trap_title,
                concept_name=prerequisite,
                misconception=misconception,
                prerequisite=prerequisite,
                radar_dimension=radar_dim,
                score_delta=-5,
                socratic_guidance=socratic_text,
                socratic_hint=socratic_text,
                knowledge_nodes=knowledge_nodes,
                fallback_mode=fallback_mode,
                model_used=model_used
            )

        except Exception as unhandled:
            # Absolute failsafe shield: NEVER raise 500
            logger.error(f"Unexpected error in diagnostic engine: {unhandled}", exc_info=True)
            return DiagnoseResponse(
                is_correct=False,
                question_id=getattr(req, "question_id", "unknown"),
                selected_key=getattr(req, "selected_key", "A") or "A",
                correct_key="B",
                explanation="The diagnostic service is in high-availability emergency fallback mode; parsing continues to work normally.",
                trap_id="trap_failsafe",
                trap_title="🚨 High-availability safety net",
                trap_name="High-availability safety net",
                concept_name="System disaster-recovery high availability",
                misconception="The service encountered an occasional unknown perturbation and completed millisecond-level lossless degradation",
                prerequisite="System robustness and exception-isolation principles",
                radar_dimension="trapDefense",
                score_delta=0,
                socratic_guidance="Think about the core definition this question tests, and use elimination to analyse the internal logical plausibility of each option.",
                socratic_hint="Think about the core definition this question tests, and use elimination to analyse the internal logical plausibility of each option.",
                knowledge_nodes=["High-availability safety net"],
                fallback_mode=True,
                model_used="local-failsafe-shield"
            )


# Global singleton instance
diagnostic_service = DiagnosticService(timeout=settings.LLM_TIMEOUT)
