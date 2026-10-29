# Chapter 6 & Appendix C Package — Testing and Evaluation

- **Author**: Yang Mingjie (杨明杰, `50106061`)
- **Role**: Testing & Evaluation Lead / PoC User Manual Author
- **Target Pages / Words**: 7–8 pages (~2,400–3,000 words; actual draft: ~2,850 words)
- **Sections Covered**: `6.1`–`6.6` + `Appendix C` (`C.1 Test Case Inventory` & `C.2 PoC Quick-Start User Manual Summary`)

## Deliverables in This Directory

- `draft.md`: Complete English prose for Chapter 6 (`6.1 Testing Strategy` through `6.6 Threats to Validity`) and `Appendix C`, including:
  - **Figure 6.1** (`figures/fig6_1_testing_pyramid.svg`): Four-tier automated testing pyramid (`9 files → 80 functions → 147 cases`, 0 external dependencies).
  - **Table 6.1**: Inventory of all 9 `pytest` modules explaining how `@pytest.mark.parametrize` expands 80 functions (`78 + 2`) into 147 executed cases (`145 + 2`).
  - **Table 6.2**: Six adversarial and robustness test groups (`A1`–`A6`) in `test_adversarial_backend.py` (25 functions, 523 LOC) and `test_empirical_stress.py`.
  - **Figure 6.2** (`figures/fig6_2_mmlu_delta.svg`) & **Table 6.3**: MMLU 12-subject empirical evaluation ($n = 4,445$ items: **7 positive gains, 3 ties, 2 negative deltas** on `HS US History -1.00 pp` and `HS Physics -1.32 pp`) with domain-mechanism and statistical-significance analysis.
  - **Table 6.4**: RAGAS evaluation framework design (`graphrag（终）/ragas_evaluator.py`) and transparent quota boundary disclosure.
  - **Table 6.5**: Requirement-by-requirement verification matrix (`R01`–`R14` and `NFR-01`–`NFR-10`), honestly marking `R10` as **Partially Met (`⚠️`)**.
  - **Section 6.6**: Six threats to validity across Internal, External (`E1`/`E2` persona provenance), Construct, and Statistical Conclusion dimensions.
  - **Appendix C**: Detailed 9-module test inventory (`Table C.1`) and 5-minute PoC Quick-Start User Manual summary.
- `evidence.md`: Exact CLI verification commands and repository file anchors.
- `viva_qa.md`: Three oral-defense Q&As covering the `80 → 147` parameterised test relationship, negative MMLU deltas (`Physics`/`US History`), and `R10` / RAGAS honesty.
