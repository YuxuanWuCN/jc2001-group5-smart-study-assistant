# Oral Defense (Viva) Q&A — Chapter 5.3–5.4 (Dong Siqin, `50106060`)

## Q1: In Section 5.3, you describe a "bijective 1:1 distractor-to-trap mapping" across 12 questions (36 traps). How did you construct those 36 traps, and how is that invariant enforced in code?

**Answer:**
For each of the 12 questions across Law, Computer Architecture, Econometrics, and Software Engineering, we engineered every incorrect option (`3 distractors × 12 questions = 36 traps`) to represent a specific, documented student fallacy rather than a random wrong value. For example, in `law_1` (Civil Code Art. 152 rescission), Option A tests conflating a formative right's 1-year preclusive period with a claim right's 3-year limitation period (`radar_hit: "boundary"`), Option C tests confusing the inception rule of fraud with duress (`radar_hit: "precision"`), and Option D tests invoking a repealed 2-year statutory rule (`radar_hit: "recall"`). In code, `tests/test_quiz.py` (`test_each_question_has_three_traps` and `test_trap_keys_exclude_correct_answer`) and `tests/test_diagnose.py` (36 parametrized test cases) enforce that every non-answer option maps 1:1 to a complete `TrapDetail` record.

## Q2: Walk us through the algorithmic complexity of `diagnose_answer()` in `backend/app/services/diagnostic_service.py`. Why is it $O(1)$?

**Answer:**
At module import time (`backend/app/data/seed_questions.py:1257`), the 12 `QuizItem` objects are pre-indexed into a Python hash dictionary: `QUESTIONS_BY_ID = {q.id: q for q in SEED_QUESTIONS}`. When `diagnose_answer(question_id, selected_option)` executes, it performs:
1. One dictionary lookup `QUESTIONS_BY_ID.get(question_id)` ($O(1)$ average time);
2. One string equality check `is_correct = (selected_option == item.answer)` ($O(1)$);
3. If incorrect, one nested dictionary lookup `trap = item.traps.get(selected_option)` ($O(1)$);
4. Instantiation of `DiagnoseResponse` referencing the pre-loaded `item.graph` and `item.socratic_prompt` ($O(1)$).
Because there are no database queries, file reads, or loops over the question bank at request time, in-process execution averages $1.8\text{ ms}$ (P95 $3.4\text{ ms}$).

## Q3: How does the 12-stage offline GraphRAG pipeline in `graphrag（终）/graphrag_pipeline.py` relate to the runtime `seed_questions.py` data?

**Answer:**
As shown in Table 5.3, the 12-stage GraphRAG pipeline (`graphrag_pipeline.py`) operates as our **offline research and evaluation engine** over 4,445 MMLU items (`AD-1`). Stages 1–8 extract domain entities, build semantic/prerequisite triples in Neo4j, and retrieve multi-hop subgraphs (`1-hop` core concepts, prerequisite rules, and confusable neighbour nodes), while Stages 9–12 perform noise pruning and prompt synthesis. Insights from this offline graph structure—specifically how confusable neighbour nodes trigger wrong answers—informed the design of our 12 embedded `GraphData` subgraphs (`nodes` and `edges`) and 36 `TrapDetail` records in `seed_questions.py`, giving the runtime app instantaneous offline speed without losing structural graph context.
