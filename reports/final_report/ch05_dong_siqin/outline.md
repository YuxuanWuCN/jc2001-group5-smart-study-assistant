# 5.3 & 5.4 Question Bank, Trap Engineering, and Diagnostic Algorithm — Section Outline

**Author:** Siqin Dong (50106060) · PoC Logic Developer  
**Chapter:** Sections 5.3 and 5.4, inside Chapter 5 (*Implementation*)  
**Target:** 5–6 pages, 1,800–2,400 words of prose, Figure 5.2, Table 5.4, Table 5.5, Table 5.6, and diagnostic pseudocode  
**Status:** Outline (Step 1 Deliverable). Pre-submission compliance verified against JC2001 Specification & Task Pack 06.

---

## 1. Section Spine & Core Thesis

> **Core Axiom:** *Diagnosis in safety-critical educational scaffolding is a deterministic topological lookup, not an unconstrained generative inference.*

This package establishes two fundamental engineering claims:
1. **Curated Cognitive Distractor Traps (Section 5.3):** The 36 misconception traps embedded in the question bank are not random distractor text; they are pedagogical artefacts engineered according to four formal misconception typologies, mapping student mistakes to verified statutory provisions, mathematical boundary conditions, and prerequisite conceptual gaps.
2. **Deterministic Diagnostic Engine (Section 5.4):** Evaluating student errors via an $O(1)$ dictionary lookup against pre-audited misconception metadata eliminates the existential hazards of generative AI (answer spoiling, probabilistic drift, and hallucinated legal statutes/theorems), ensuring sub-5ms latency and 100% offline reproducibility.

---

## 2. Section Breakdown & Word Budget

| Section | Title | Target Length | Tables & Figures | Core Academic / Engineering Question Addressed |
| :---: | :--- | :---: | :---: | :--- |
| **5.3.1** | Question Bank Scale, Multidisciplinary Scope, and Taxonomy | 250 words | **Table 5.4** | What is the empirical scale and subject distribution of the seed corpus? |
| **5.3.2** | The Tripartite Architecture of Cognitive Traps | 350 words | **Figure 5.2**, **Table 5.5** | How do the four `TrapDetail` fields convert a wrong answer into actionable metacognition? |
| **5.3.3** | Trap Engineering Typology and Feasibility Limitations | 450 words | — | What formal rules governed trap design, and what are the honest empirical boundaries? |
| **5.3.4** | Automated Data Integrity and Invariant Testing | 250 words | — | How do unit and adversarial test suites guarantee zero dangling traps? |
| **5.4.1** | Deterministic Lookup Algorithm vs. Generative Inference | 300 words | **Algorithm 5.1** (Pseudocode) | How does the $O(1)$ lookup algorithm execute without executing unconstrained inference? |
| **5.4.2** | Comparative Trade-Off Analysis: Lookup vs. Generative LLMs | 350 words | **Table 5.6** | Why was live LLM reasoning rejected on the primary evaluation path, and what was conceded? |
| **5.4.3** | Real-Time Competency Radar Telemetry and Startup Trade-offs | 300 words | — | How are five competency dimensions aggregated in-session without backend bloat? |

---

## 3. Three-Level Structural Outline

### 5.3 Question Bank and Trap Engineering

#### 5.3.1 Question Bank Composition and Multi-Disciplinary Scope
- **5.3.1.1 Empirical Dataset Geometry:**
  - Audit of `backend/app/data/seed_questions.py` (932 lines): 12 primary benchmark assessment items spanning four distinct academic disciplines (Civil & Commercial Law, Computer Architecture & Systems, Micro/Macroeconomics, and Software Engineering).
  - Uniform structural geometry: Each item contains exactly 4 options ($N=48$ total options), featuring exactly 1 verified correct answer ($P_{correct}=0.25$) and 3 distractors ($P_{distractor}=0.75$).
  - Granular trap enumeration: Exactly 36 unique distractor traps ($12 \times 3 = 36$), with 100% bijective mapping between distractor options and `trap_id` keys in `traps` dictionaries.
- **5.3.1.2 Presentation of Table 5.4 (Question Distribution Matrix):**
  - Tabulation of Subject, Question ID, Bloom's Cognitive Level, Difficulty Rating, Core Knowledge Point, and Prerequisite Anchor.
  - Verification that every entry corresponds to an existing, executable Python object in the repository baseline.

#### 5.3.2 The Tripartite Architecture of Cognitive Traps
- **5.3.2.1 From Binary Feedback to Diagnostic Scaffolding:**
  - Critique of conventional Computer-Based Testing (CBT): Traditional systems yield only binary indicators ($is\_correct \in \{0, 1\}$), leaving the underlying reasoning fallacy uninspected.
  - Contrast with tripartite pedagogical decomposition: Our system provides (1) fallacy identification, (2) cognitive conflict explanation, and (3) remedial prerequisite navigation.
- **5.3.2.2 Pedagogical Specification of Table 5.5 (`TrapDetail` Fields):**
  - `title`: Conceptual labeling providing mnemonic anchor (e.g., *"Confusing Extinction of Rescission Right with Extinctive Prescription"*).
  - `desc`: Articulation of cognitive dissonance citing specific statutory/theoretical misalignments (e.g., Article 152 vs. Article 188 of the Civil Code).
  - `prereq`: Forward-directed remediation targeting formative antecedent theorems (e.g., formative rights vs. claim rights).
  - `radar_hit`: Telemetry routing key directing penalty vectors into the 5-dimensional mastery model (`recall`, `boundary`, `trapDefense`, `synthesis`, `precision`).
- **5.3.2.3 Exposition of Figure 5.2 (Trap Causal Flow):**
  - Diagrammatic trace: Student Selection $\to$ Option Extraction $\to$ `trap_id` Matching $\to$ `TrapDetail` Payload $\to$ Socratic Prompt Assembly $\to$ Radar Telemetry Mutation.

#### 5.3.3 Trap Engineering Methodology and Formal Typology
- **5.3.3.1 Four Formal Distractor Construction Patterns:**
  1. *Conceptual Neighbour Inversion:* Swapping adjacent doctrinal concepts (e.g., Law: rescission period vs. limitation of actions).
  2. *Boundary Condition Neglect:* Applying valid formula to invalid boundary intervals (e.g., CS: assigning $2^n$ instead of $2^n - 2$ available host addresses in subnet masking).
  3. *Causal Direction Inversion:* Reversing dependent and independent variables (e.g., Economics: asserting demand contraction causes price inflation).
  4. *Terminology Contamination / Jargon Masking:* Using valid software engineering buzzwords in inverted semantic scopes (e.g., SE: conflating mutation survival with statement coverage).
- **5.3.3.2 Peer-Reviewed Academic Grounding:**
  - Grounding in VanLehn's (2011) findings on fine-grained diagnostic effectiveness and Koedinger et al.'s (2012) Knowledge-Learning-Instruction (KLI) framework.
- **5.3.3.3 Honest Feasibility Scoping (Anti-Overclaim Clause):**
  - Explicit statement that 12 questions and 36 traps demonstrate *proof-of-mechanism feasibility*, not statistical saturation across entire degree curricula.

#### 5.3.4 Automated Structural Integrity and Validation Guarantees
- **5.3.4.1 Test-Driven Knowledge Invariants:**
  - Enforcing zero dangling trap references: Every option `trap_id` must resolve in `traps`.
  - Cardinality invariant: Exactly one `is_correct == True` per question item.
  - Statutory provenance invariant: Every `explanation` must cite formal textbook/statutory origins.
- **5.3.4.2 Cross-Validation against Testing Suite:**
  - Aligning data integrity with `tests/test_quiz.py` (6 unit cases) and `tests/test_adversarial_backend.py` (25 adversarial functions).

---

### 5.4 Diagnostic Algorithm

#### 5.4.1 Deterministic Lookup vs. Generative Inference
- **5.4.1.1 The Lookup Philosophy:**
  - Stating the core architectural decision: Runtime diagnosis is executed via static in-memory index traversal.
- **5.4.1.2 Presentation of Algorithm 5.1 (Pseudocode):**
  - Formal $\le 20$-line algorithmic specification demonstrating $O(1)$ retrieval, boundary condition checks, and payload assembly.
  - Explicit avoidance of raw Python code to adhere strictly to Course Brief Page 5 prohibitions.
- **5.4.1.3 Complexity and Latency Guarantees:**
  - Time complexity: $O(1)$ dictionary lookup.
  - Space complexity: $O(N)$ bounded memory footprint (~60 KB heap footprint).
  - Measured local round-trip execution time: $< 2.5 \text{ ms}$.

#### 5.4.2 Comparative Trade-Off Analysis: Lookup vs. Generative LLMs
- **5.4.2.1 Presentation of Table 5.6 (Comparative Decision Matrix):**
  - Six evaluation vectors: Latency, Offline Availability, Output Determinism, Automated Testability, Academic Soundness, and Question Surface Coverage.
- **5.4.2.2 The "Conceded Vector" (Honest Limitation):**
  - Conceding that generative LLMs naturally surpass lookup tables in open-ended essay scenarios.
  - Defending why closed-form multiple-choice items were deliberately chosen in Chapter 2 (R01/R02) to guarantee academic integrity and zero hallucination risk.
- **5.4.2.3 Dual-Mode Safety Architecture:**
  - Role of Qwen-Turbo LLM in `diagnostic_service.py`: Used exclusively for tone-polishing Socratic questions under a strict 4.0-second timeout; if offline or unconfigured, falls back immediately to verified local prompts with zero unhandled exceptions.

#### 5.4.3 Real-Time Competency Radar Telemetry and Startup Trade-offs
- **5.4.3.1 Client-Side Instant Vector Adjustment:**
  - Five targeted dimensions: Basic Concepts (`recall`), Boundary Conditions (`boundary`), Trap Defense (`trapDefense`), Cross-Chapter Synthesis (`synthesis`), Computational Precision (`precision`).
  - Mechanics: Client-side event aggregation (`frontend/app.js:updateRadarCharts`) achieving immediate UI responsiveness without database write transactions.
- **5.4.3.2 Startup Architecture Trade-Offs (Option B Scoping):**
  - Justification of lean in-session aggregation over complex persistent Bayesian Knowledge Tracing (BKT) or Free Spaced Repetition Scheduling (FSRS).
  - Explicit demarcation for Chapter 7 (*Future Work*): Temporal retention decay and longitudinal student tracking deferred to post-MVP roadmap.

---

## 4. Required Tables, Figures, and Pseudocode

### 4.1 Table 5.4: Question Bank and Misconception Trap Distribution Matrix
*To be populated directly from `backend/app/data/seed_questions.py`:*
- 12 rows corresponding to questions `law_1`, `law_2`, `law_3`, `cs_1`, `cs_2`, `cs_3`, `econ_1`, `econ_2`, `econ_3`, `se_1`, `se_2`, `se_3`.
- Columns: Subject, Question ID, Difficulty, Core Academic Concept, Distractor Trap IDs, Target Radar Dimensions.

### 4.2 Table 5.5: `TrapDetail` Schema and Pedagogical Role Mapping
- Mapping of the 4 data model fields (`title`, `desc`, `prereq`, `radar_hit`) to their metacognitive and tutoring functions.

### 4.3 Table 5.6: Architectural Decision Matrix: Static Lookup vs. Generative LLM
- Comparative trade-off table contrasting deterministic table lookup with on-the-fly generative LLM prompts, concluding with the acknowledged open-domain limitation.

### 4.4 Figure 5.2: Diagnostic Traversal and Feedback Causal Chain
- Vector diagram (Mermaid/SVG) detailing the flow from distractor selection to radar delta and Socratic prompt.

### 4.5 Algorithm 5.1: Deterministic Misconception Diagnosis Algorithm
- Formal algorithmic pseudocode ($\le 20$ lines) specifying input validation, $O(1)$ dictionary indexing, and output payload assembly.

---

## 5. Harvard Reference Corpus

1. **Corbett, A.T. and Anderson, J.R. (1994)** 'Knowledge tracing: Modeling the acquisition of procedural knowledge', *User Modeling and User-Adapted Interaction*, 4(4), pp. 253–278.
2. **Koedinger, K.R., Corbett, A.T. and Perfetti, C. (2012)** 'The Knowledge-Learning-Instruction framework: Bridging the science-practice chasm to enhance robust student learning', *Cognitive Science*, 36(5), pp. 757–798.
3. **VanLehn, K. (2011)** 'The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems', *Educational Psychologist*, 46(4), pp. 197–221.
4. **Sommerville, I. (2020)** *Software Engineering*. 10th edn. Harlow: Pearson Education.

---

## 6. Oral Defense Preparation (30-Second Strategy)

- **Q1 ("Only 12 questions? Is this just a toy demo?"):**  
  *Strategy:* Concede scale, defend mechanism. The 12 questions establish proof-of-concept feasibility for fine-grained distractor attribution. Scaling question volume is an editorial asset ingestion task, whereas establishing deterministic trap routing and zero-hallucination guarantees is the core architectural innovation.
- **Q2 ("How do you know these traps reflect real student mistakes?"):**  
  *Strategy:* Triangulate sources. Cite statutory contrasts (Civil Code Articles 152 vs. 188), textbook boundary traps ($2^n - 2$ host addresses), and team cross-review audits. Concede lack of large-scale longitudinal empirical validation in the Limitations subsection.
- **Q3 ("Why not let modern generative LLMs diagnose students directly?"):**  
  *Strategy:* Highlight safety and reliability. LLMs exhibit prompt drift and legal/mathematical hallucinations (e.g., misquoting statutory limitation periods). In educational assessment, deterministic correctness and offline reproducibility strictly supersede conversational novelty.
