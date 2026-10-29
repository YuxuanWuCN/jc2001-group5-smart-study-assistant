# Section 5.6 in one page — for supervisor review

**Project:** StudyGraph, JC2001 Group 5 · **Section author:** Zixuan Liang (50106037)
**Section:** 5.6 Deployment and Reproducibility, inside Chapter 5 (Implementation)

**What the section argues.** The proof of concept is deployed as a single operating-system process.
One `uvicorn` server loads the FastAPI application, which mounts the JSON API below `/api` and the
browser application at `/` from the same process and the same port. Because both are served from one
origin, the demonstration path needs no reverse proxy, no container, no build step and no second web
server — and, more importantly, no database and no language-model endpoint. The question bank is a
Python source module that is imported at startup.

**Why that is a decision and not a shortfall.** The assessed artefact is run by the examiner on their
own machine. A hosted deployment would introduce a dependency that fails precisely when the network
is unavailable. Chapter 4 records this as ADR-01, and the section is written as its direct
consequence.

**What was verified, and how.** Every figure in the section was measured on a Windows 11 machine with
Python 3.14.0 on 19 October 2026, with no credential present:

- cold start from process launch to the first successful health response: **1.12 s**;
- the application shell served at `/`: **40,390 bytes in 50.9 ms**, identical in size to
  `frontend/index.html`, which demonstrates the single-process claim rather than asserting it;
- test suite: **150 passed in 1.79 s** with no external service contact;
- the full dependency installation from a clean environment, and the resulting environment size.

**What the section does not claim.** Re-running the benchmark evaluation requires a Neo4j Aura
instance whose credential has since been rotated, and the RAGAS metrics depend on the same instance.
The section therefore describes the evaluation as *partially* reproducible and names the result
snapshot (`final_systematic_report.csv`) as the artefact to which every reported number is traceable.
We preferred a defensible boundary to a claim that the first inspection of the evaluation scripts
would contradict.

**Two defects the section reports rather than hides.** The start command written in `backend/run.py`
(`python backend/run.py`) fails with `ModuleNotFoundError`; the working alternatives are documented
and were each executed. And three exploratory scripts inside the evaluation archive still carry
literal credentials inherited from the prototype phase; their remediation and the rotation of both
credentials are scheduled before the archive is built.

The section supports the *Documentation and Reproducibility* and *Reliability* criteria of the proof
of concept, and it is deliberately written so that any number in it can be re-derived from the
repository in under five minutes.
