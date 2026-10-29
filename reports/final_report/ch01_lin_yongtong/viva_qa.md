# Oral Defense (Viva) Q&A — Chapter 1 (Lin Yongtong, `50106038`)

## Q1: In Section 1.3, you compare StudyGraph against Quizlet, Anki, Khanmigo, ChatGPT, and Chegg. Could a student simply paste a missed question into ChatGPT and ask "Why is my chosen option wrong?" Why build a dedicated system?

**Answer:**
A student can indeed paste a question into ChatGPT, and we explicitly evaluated that workflow in Table 1.1 and Figure 1.2. However, unconstrained LLM chat suffers from three structural flaws during exam revision:
1. **Answer Spoiling & Cognitive Bypass**: ChatGPT immediately outputs the full derivation of the correct answer rather than isolating the specific antecedent rule violated by the student's chosen distractor (`TrapDetail.prereq`), short-circuiting active retrieval.
2. **Statutory and Formula Hallucination**: In specialized domains such as Civil Law (`law_1`–`law_3`) or Econometrics (`econ_1`–`econ_3`), general LLMs frequently fabricate statutory article numbers or conflate prescription periods with preclusive periods.
3. **Cloud Dependency and Marginal Cost**: ChatGPT requires active internet connectivity and incurs per-token API costs. StudyGraph pre-verifies all 36 distractor traps offline and serves them via an $O(1)$ in-memory lookup (`POST /api/diagnose`, P95 $< 5\text{ ms}$) with £0.00 marginal inference cost and 100% offline determinism.

## Q2: In Table 1.3, you list Persona C (Course Instructor / Marker) as an "Explicitly Non-Target User for MVP UI". Why include a non-target persona in your requirements and stakeholder analysis?

**Answer:**
Including Persona C as an explicit **non-target operator** is a deliberate scoping safeguard aligned with Requirement `R11` (*No Multi-Tenant Teacher Administration*, marked `Won't Have` in Chapter 2). In student software engineering projects, teams frequently claim to serve both students and instructors, resulting in half-finished admin dashboards with non-functional buttons. By distinguishing between **direct system operators** (Personas A and B, who use the diagnostic loop) and **indirect institutional stakeholders** (Persona C, who evaluates the offline ZIP deliverable and benefits from future cohort telemetry), we keep 100% of our 10-week engineering budget focused on making the student-facing misconception loop end-to-end verifiable.

## Q3: Did you conduct an external user survey to establish the pain points of Personas A and B?

**Answer:**
No—and we explicitly document that boundary in Section 1.4.1 and `reports/audit/persona_provenance.csv`. In compliance with our project's anti-hallucination audit (`004-persona-hallucination-audit`), we never fabricate user survey sample sizes. Every attribute in Table 1.3 is tagged with its actual provenance level: **E1** (grounded in peer-reviewed educational literature such as Hattie & Timperley 2007 and competitor audits) or **E2** (structured internal workshops across our 10 BSc BMIS undergraduate team members, who are themselves active exam candidates). We list the lack of an $N \ge 30$ external student trial as an explicit threat to external validity in Section 6.6 and a Phase 2 priority in Section 7.3.
