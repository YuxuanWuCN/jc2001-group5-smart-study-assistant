# Ch 5.3-5.4 Writing Skeleton (G1 Deliverable)

| Item | Content |
| :--- | :--- |
| Owner | Dong Siqin (50106060 · PoC logic) |
| Chapters | 5.3 Question Bank and Trap Engineering + 5.4 Diagnostic Algorithm |
| Target length | 5-6 pages / 1,800-2,400 English words |
| Required graphics | Table 5.4, Table 5.5, Table 5.6, Figure 5.2 (numbering locked by the whole group, must not change) |
| Delivery path | `reports/final_report/ch05_dong_siqin/` (outline.md -> draft.md) |
| Status of this file | G1 skeleton (submitted before Sunday 23:59 of Week A) |
| Body language | English (this skeleton's explanatory notes were drafted in Chinese; the final draft is in English) |

> **Every number in this skeleton has been checked back against the code** (2026-10-19). The original task package 06 contains 4 statements that do not match the code; this file has corrected them to the measured values, see "Differences from task package 06" at the end.

---

## 1. Report Body Heading Structure (the draft can follow it directly)

```text
5.  Implementation
    5.3  Question Bank and Trap Engineering
        5.3.1  Scale and Composition of the Question Bank
        5.3.2  The Three-Part Anatomy of a Trap
        5.3.3  Trap Design Methodology and Its Limits
        5.3.4  Automated Data-Integrity Assurance
    5.4  Diagnostic Algorithm
        5.4.1  Diagnosis Is a Lookup, Not an Inference
        5.4.2  Why the Diagnostician Is Not an LLM
        5.4.3  Aggregating the Five-Dimension Radar
```

(The report body has 9 headings; together with the Tables / Figures / Sources sections of this skeleton this satisfies G1's ">= 12 lines of third-level headings plus a material list".)

---

## 2. Section-by-Section Writing Notes

### 5.3 Question Bank and Trap Engineering (budget 900-1,200 words + Table 5.4 / 5.5 + Figure 5.2)

#### 5.3.1 Scale and Composition of the Question Bank
- **What to write**: start by laying out the whole picture to prove that "the 12 questions were genuinely produced, not padding"; give the subject distribution and the difficulty distribution; explain that "each question has exactly 3 distractors" is a design constraint rather than a coincidence.
- **Material**: `backend/app/data/seed_questions.py` (657 lines; 12 entries in `SEED_QUESTIONS`)
- **Measured numbers (copy as-is)**:
  - 12 questions; subjects law 3 / cs 3 / econ 3 / se 3
  - 36 distractor traps, **exactly 3 per question** (mean 3.00)
  - Difficulty: ★★★☆☆ 2 questions, ★★★★☆ 8, ★★★★★ 2
- **Table 5.4**: 12-question distribution table (Subject / Question ID / Difficulty / Trap count / Knowledge point), data in section 4 of this file
- **Avoid**: do not say "the question bank is substantial" -- 12 questions is a feasibility prototype, so say so plainly

#### 5.3.2 The Three-Part Anatomy of a Trap
- **What to write**: the four `TrapDetail` fields each serve a distinct pedagogical role; the core argument -- **an ordinary question bank gives only a binary right/wrong, whereas we give three-part feedback: which concept went wrong + which prerequisite is missing + which dimension it is recorded against**.
- **Material**: `backend/app/models/quiz.py` (`TrapDetail` definition); use `law_1 / trap_law_1` as the real sample
- **Table 5.5**: four-field pedagogical function table (field / pedagogical function / real value)
- **Figure 5.2**: the causal chain wrong option -> `trap_id` -> `TrapDetail(title/desc/prereq/radar_hit)` -> displayed in the diagnosis drawer (does not duplicate Jiang Hao's class diagram in 5.2: he draws structure, you draw data flow)
- **⚠️ Citation convention**: the trap `title` text carries a 🚨 prefix and is colloquial (e.g. "🚨 Typical confusion trap: misapplying the 'preclusive period of a formative right' as the '3-year ordinary limitation period'"), **the body text must rewrite it as a declarative sentence**; do not quote the emoji text directly

#### 5.3.3 Trap Design Methodology and Its Limits
- **What to write**: summarise four trap-generation rules, **each paired with a real question**; end with "honest limitations" -- 12 questions / 36 traps cannot claim statistical significance; this is feasibility evidence rather than a benchmark.
- **Material**: choose from the 36 traps (real pairings in section 5 of this file)
- **Key point**: this section is the core of "removing the AI feel"; it must describe the manual review process clearly (who reviewed, against which textbook/syllabus), otherwise there is an academic-integrity risk
- **⚠️ Deadline reminder**: in the code, 4 trap descriptions contain **percentages with no source** ("64% of the whole school", "58%", "71%", "60% of the class"). **The body must never cite these numbers**, otherwise it violates the hard rule that "every number must be traceable". Rewrite as "high-frequency error-prone points annotated from textbooks and syllabi" and put "no large-scale empirical validation" in Limitations.

#### 5.3.4 Automated Data-Integrity Assurance
- **What to write**: how the data rules are enforced (describe the rules only and reference the test files, **do not paste code**), and align with the Chapter 6 wording.
- **Measured (assertable)**: 12/12 questions have 4 options; each question has exactly 1 `is_correct`; no dangling `trap_id`; none of the four fields is empty; the `explanation` of 12/12 questions carries an authoritative-source annotation of the form `[Authoritative exam-point analysis · ...]`
- **Material**: `tests/test_quiz.py` (6 cases), `tests/test_adversarial_backend.py` (25 adversarial test functions across 6 test classes)
- **Honesty bonus point**: the frontend `frontend/app.js` embeds a **mirror of the question bank** (19 question blocks, 57 `radarHit` annotations) that is not the same data source as the backend `seed_questions.py`. Writing this up as "a known engineering simplification / dual-data-source risk" is more credible than pretending there is a single data source.

### 5.4 Diagnostic Algorithm (budget 700-900 words + pseudocode + Table 5.6)

#### 5.4.1 Diagnosis Is a Lookup, Not an Inference
- **What to write**: open the paragraph with the line **"Diagnosis is a lookup, not an inference."**; give <=20 lines of pseudocode (**not Python**).
- **The pseudocode must follow the real implementation** (the task package's original 404/422 do not match the code): question not found -> **200 + graceful fallback** (return "question lookup miss", `fallback_mode=true`), not 404; option mismatch -> the same fallback; 422 appears only when request-body schema validation fails.
- **Material**: `backend/app/services/diagnostic_service.py` (274 lines), `backend/app/routers/diagnose.py`

#### 5.4.2 Why the Diagnostician Is Not an LLM
- **What to write**: Table 5.6 compares "deterministic table lookup vs live LLM generation" dimension by dimension (latency / offline / reproducibility / testability / pedagogical correctness / coverage).
- **Must write**: **the last row must admit the one item we lose** -- table lookup fails in open-ended question-answering scenarios, which is exactly the fundamental reason for choosing a closed multiple-choice interface (echoing the R01/R02 scope cut in Ch2).
- **You may quote one measured point**: live LLM generation can produce teaching-accident-level errors such as "2 years / 3 years" on legal articles and formulas; table lookup guarantees correctness through manually reviewed authoritative sources.

#### 5.4.3 Aggregating the Five-Dimension Radar
- **The data source was ruled by the team lead to be `frontend/app.js`** (option B: lightweight frontend aggregation, no complex temporal decay); do not reference the non-existent `report_service.py` / `/api/reports/trend` any more.
- **Measured specification (must be written exactly like this; do not invent formulas)**:

| Situation | Dimension change | Clamp |
| :--- | :--- | :--- |
| Correct | `recall +4`, `trapDefense +5`, `synthesis +3`, `predictedScore +0.5` | per-dimension cap 100; predictedScore cap 99 |
| Wrong | `trapDefense -6`, `boundary -4` | floor 30 |

- **Two key facts that must be stated honestly**:
  1. The frontend **does not consume** the backend's `radar_dimension` / `score_delta` at all (0 references in `app.js`) -- the increments are a heuristic issued on a fixed "right/wrong" basis and **do not vary with the specific trap's `radar_hit`**.
  2. The initial radar (0 answers) is not all zeros but a preset baseline: `recall 76 / boundary 62 / trapDefense 65 / synthesis 72 / precision 81`.
- **Known copy bug (recommend fixing before writing, or put it in Limitations)**: the UI hint says "Defense Index **+6**" while the code actually adds **+5**. Recommend asking Liang Zixuan / Xi Yusai to change it to +5, or note in the report that the code is authoritative.
- **Qualitative conclusion**: write it as "session-scoped, rule-based aggregation without temporal decay", and list it under Ch7 Limitations (hence R04 is "partially satisfied").

---

## 3. Graphics List (numbering locked, must not change)

| Number | Content | Data source | Status |
| :--- | :--- | :--- | :--- |
| Table 5.4 | 12-question distribution table | `seed_questions.py` (see section 4) | Data ready |
| Table 5.5 | Pedagogical function of the four `TrapDetail` fields | `law_1 / trap_law_1` | Data ready |
| Table 5.6 | Lookup vs LLM comparison (**including the disadvantage row**) | discussion in this section | To be written |
| Figure 5.2 | Trap causal chain (wrong option -> trap -> diagnostic feedback) | self-drawn (Mermaid or draw.io) | To be drawn |

---

## 4. Table 5.4 Data (verified, ready to use)

| ID | Subject | Difficulty | Traps | Knowledge point |
| :--- | :--- | :-: | :-: | :--- |
| law_1 | Law | ★★★☆☆ | 3 | Revocable juristic acts · limitation period for the right of revocation |
| law_2 | Law | ★★★★☆ | 3 | Property law · requirements and defences of bona fide acquisition |
| law_3 | Law | ★★★★☆ | 3 | General provisions · apparent authority and appearance-based liability |
| cs_1 | CS | ★★★★☆ | 3 | RISC pipeline · hazard handling and forwarding/bypassing |
| cs_2 | CS | ★★★★☆ | 3 | Memory hierarchy · set-associative cache mapping and miss analysis |
| cs_3 | CS | ★★★★★ | 3 | Virtual memory · TLB and page-fault handling sequence |
| econ_1 | Econ | ★★★★☆ | 3 | Violations of classical assumptions · multicollinearity and omitted-variable bias |
| econ_2 | Econ | ★★★★★ | 3 | Causal inference · instrumental variables (IV/2SLS) and weak instruments |
| econ_3 | Econ | ★★★★☆ | 3 | Violations of classical assumptions · heteroskedasticity, White test, robust SEs |
| se_1 | SE | ★★★☆☆ | 3 | Process models · Scrum versus waterfall trade-off |
| se_2 | SE | ★★★★☆ | 3 | OO architecture · SOLID and the dependency-inversion principle |
| se_3 | SE | ★★★★☆ | 3 | Quality assurance · boundary-value analysis and mutation testing |

Real radar-dimension distribution (for use when writing 5.3.1 or 5.4.3): `boundary` 12, `recall` 8, `trapDefense` 7, `synthesis` 7, `precision` 2.

---

## 5. Real Pairings for the Four Trap Types (replacing the fabricated examples in the task package)

| Trap type | Use this question | Trap ID | `radar_hit` | One-line misconception |
| :--- | :--- | :--- | :--- | :--- |
| Conceptual neighbour | `law_1` | `trap_law_1` | **`trapDefense`** | Misapplying the preclusive period of a formative right as the 3-year ordinary limitation period |
| Boundary condition | `cs_2` | `trap_cs_2_2` | `boundary` | Blindly increasing block size -> fewer sets and worse conflict misses |
| Causal inversion | `econ_3` | `trap_econ_3_1` | `recall` | Mistaking "impaired efficiency" for "the estimator losing unbiasedness" |
| Terminology contamination | `se_3` | `trap_se_3_3` | `recall` | Mistaking "mutation testing" for "performance stress testing" |

(Alternatives: `cs_3 / trap_cs_3_2` (Fault retry vs. Interrupt returning PC+4, boundary), `cs_3 / trap_cs_3_1` (TLB Miss != Page Fault, trapDefense), `econ_1 / trap_econ_1` (insufficient precision != biased, recall).)

---

## 6. References (Crossref-checked)

1. VanLehn, K. (2011) 'The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems', *Educational Psychologist*, 46(4), pp. 197-221. doi:10.1080/00461520.2011.611369.
2. Corbett, A.T. and Anderson, J.R. (1994) 'Knowledge tracing: Modeling the acquisition of procedural knowledge', *User Modeling and User-Adapted Interaction*, 4(4), pp. 253-278. doi:10.1007/BF01099821.
   ⚠️ Crossref records the publication year as **1995**, while the literature most often cites 1994; before submission, follow the publisher page and be consistent throughout.
3. Koedinger, K.R., Corbett, A.T. and Perfetti, C. (2012) 'The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning', *Cognitive Science*, 36(5), pp. 757-798. doi:10.1111/j.1551-6709.2012.01245.x.

---

## 7. DoD Self-Check (tick each item at the draft stage)

- [ ] 1,800-2,400 words, 5-6 pages
- [ ] Table 5.4 / 5.5 / 5.6 + Figure 5.2 complete, numbering consistent with the group-locked table
- [ ] Each of the four trap types is illustrated with a **real question** (see section 5)
- [ ] 5.4.1 pseudocode <=20 lines and not Python, semantics consistent with the implementation (200 + fallback)
- [ ] 5.3.3 ends with an honest limitations paragraph
- [ ] 5.4.3 specification fully consistent with `app.js` (+4/+5/+3, -6/-4, floor 30, baseline values)
- [ ] Radar dimension names character-for-character consistent: `recall` / `boundary` / `trapDefense` / `synthesis` / `precision`
- [ ] Body contains **no source code** (search for `def ` / `import ` / ```python)
- [ ] Harvard references >= 4, volume/issue/pages checked
- [ ] `sources.md` attached (see same directory)
- [ ] Able to present for 4 minutes without notes; able to answer Q1-Q3

---

## 8. Differences from Task Package 06 (corrected to the measured values; recommend informing Wu Yuxuan as well)

| Task package 06 original text | Measured | Adopted in this skeleton |
| :--- | :--- | :--- |
| `seed_questions.py` 932 lines | 657 lines | 657 |
| 5.3.2 table: `law_1`'s `radar_hit` = `boundary` | `trapDefense` | `trapDefense` |
| 5.3.3 example: subnetting `2^n-2` | no such question type in the bank | replaced with `cs_2 / trap_cs_2_2` |
| 5.3.3 example: supply-demand elasticity causal inversion | all three econ questions are econometrics | replaced with `econ_3 / trap_econ_3_1` |
| 5.3.3 example: unit test vs. integration test | no such question type | replaced with `se_3 / trap_se_3_3` |
| 5.4.3 reads `report_service.py` / `/api/reports/trend` | neither exists | changed to read `frontend/app.js` (ruled by the team lead) |
| Pseudocode 404 / 422 | implemented as 200 + fallback | written per the actual behaviour |
| 8 endpoints (overall index README) | 4 | omit the endpoint count or write 4 |

---

## 9. Known Risks (must be handled before writing)

1. **Credential leak (security incident, highest priority)**: line 1207 of `frontend/app.js` hardcodes an API key starting with `sk-` (variable `GEMINI_DEFAULT_KEY`, length 67) and pre-fills it into the UI input box as the default value. The repository is public, so **anyone can read it and abuse the quota**. Must: revoke the key in the console -> remove it from the code and git history -> whole-team self-check. This is unrelated to 5.3/5.4 directly but must be handled before submission (corresponds to the "credential leak handled" item in the overall checklist).
2. **Percentages without a source** (4 places): must not enter the body; see the reminder in 5.3.3.
3. **Emoji trap titles**: the body must rewrite them and must not quote them verbatim.
4. **Duplicate frontend/backend question banks**: state honestly in 5.3.4, or have Liang Zixuan unify the data source later.
5. **+6 / +5 copy inconsistency**: recommend fixing the UI copy to +5.
