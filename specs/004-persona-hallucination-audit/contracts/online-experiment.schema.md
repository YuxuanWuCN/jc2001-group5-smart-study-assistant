# Online Experiment Contract

**Feature ID**: `004-persona-hallucination-audit`
**Corresponding script**: `scripts/audit_online_baseline.py`
**Corresponding outputs**: `reports/audit/online_baseline.csv` (completed) or `reports/audit/online_baseline.skipped.json` (skipped)
**Upstream decisions**: `research.md` decision 1 (L4 definition), decision 4 (three groups + Wilson intervals)

---

## 1. Experiment Design

### 1.1 Three Groups

| Group | Name | Input | Constraint strength | Role when answering Q3 |
| :-: | :--- | :--- | :--- | :--- |
| **A** | `free_generation` | question stem + 4 options + "please give diagnostic feedback" | none (the model generates freely) | **baseline**: represents "the AI hallucination level without this system" |
| **B** | `offline_lookup` | question stem + 4 options + the wrong option chosen by the user → server-side table lookup | strong (no generation at all) | **lower-bound reference**: the hallucination surface is structurally eliminated |
| **C** | `graph_constrained` | question stem + 4 options + the wrong option chosen by the user + graph adjacency (prerequisite concepts / trap nodes) → table lookup + graph-constrained phrasing | medium (lookup determines the conclusion; generation is only used to organise language) | **the system's real form**: the comparison with A gives the "reduction magnitude" |

### 1.2 Groups Must Be Paired

- **A ↔ C is the real evidence for the system's "hallucination reduction"**: both have a generation surface, and the only difference is whether option-level constraints exist.
- **B does not participate in the "reduction" calculation**; it is only used to show that "the L4 generation surface of the offline path is 0" (a mechanistic fact). Putting B into "A→B reduction of x%" is **construct cheating**, because B has no generation at all.

### 1.3 Sampling

- 12 questions × at least 2 calls per question × 3 groups ⇒ N ≥ 20 per cell (`N=24`: 12 questions × 2 calls).
- Temperature fixed at `temperature=0.7`; if the provider supports `seed`, fix it, otherwise record a "non-reproducibility note" in `env_fingerprint`.
- Order: **interleaved execution** (A1,B1,C1,A2,B2,C2…), to avoid provider-side temporal drift contaminating between-group differences.

---

## 2. Output Field Contract

Columns of `reports/audit/online_baseline.csv` (fixed order):

| Column | Type | Required | Description |
| :--- | :--- | :-: | :--- |
| `sample_id` | string | ✅ | In the form `A-law_1-r1`: `<group>-<question_id>-<repeat_index>` |
| `group` | enum | ✅ | `A_free_generation` / `B_offline_lookup` / `C_graph_constrained` |
| `question_id` | string | ✅ | `law_1` … `se_3` |
| `repeat_index` | int | ✅ | starting at 1 |
| `prompt_hash` | string | ✅ | SHA-256 of the prompt actually sent (first 16 characters suffice), for later checking that it was not accidentally modified |
| `raw_output` | string | ✅ | Raw model output (for group B, the JSON text returned by the server); newlines must be escaped |
| `model_id` | string | ✅ | Identifier of the model actually called (e.g. `qwen-turbo`) |
| `latency_ms` | int | ✅ | End-to-end latency |
| `rater_1_verdict` | enum | ✅ | `HALLUCINATED` / `NOT_HALLUCINATED` / `UNSURE` |
| `rater_2_verdict` | enum | ✅ | Same as above, **independent blind rating** (cannot see rater_1's result or the source group) |
| `adjudicated_verdict` | enum | ✅ | If the two raters agree, use that value; if not, a third person adjudicates, the adjudicated value goes in this field, and `adjudication_note` explains it |
| `adjudication_note` | string | ⚠️ | Required when the raters disagree or when the verdict is `UNSURE` |
| `hallucination_span` | string | ⚠️ | Required when `HALLUCINATED`: the verbatim excerpt of the untrue statement |
| `hallucination_type` | enum | ⚠️ | `factual_error` / `unsupported_attribution` / `overclaiming` / `fabricated_citation` |

**Judgement criterion (L4 definition; must be written on the first page of the rating sheet)**
> An output is judged `HALLUCINATED` if and only if it contains a specific statement that is **falsifiable and false** - including: wrong subject-matter facts, presenting a non-existent knowledge gap as the user's gap, and fabricating textbook/article sources. **Unconfident tone, vague wording, or empty but not incorrect content** ⇒ `NOT_HALLUCINATED` (that is "useless", not "false"; the two must not be conflated).

---

## 3. Aggregation Contract

### 3.1 Wilson 95% Interval (the only permitted interval algorithm)

For group g, numerator `k` and denominator `n` (`n` = the number of samples in that group, excluding those with a missing `adjudicated_verdict`):

```
z = 1.959963984540054
p̂ = k / n
den   = 1 + z²/n
centre= (p̂ + z²/(2n)) / den
half  = z * sqrt(p̂(1-p̂)/n + z²/(4n²)) / den
ci_low, ci_high = max(0, centre-half), min(1, centre+half)
```

**Forbidden**: the normal approximation `p̂ ± 1.96·sqrt(p̂(1-p̂)/n)`: in this experiment n≈24 and p is expected to be close to 0, so the normal-approximation lower bound would become negative.

### 3.2 Rater Agreement

- Compute **Cohen's κ** for each pair of ratings (when merging `UNSURE` as a third class in a binary task, use Fleiss' κ instead and say so).
- **κ ≥ 0.6**: report the `rate` and `CI` of A and C, and report `rate_A - rate_C` together with whether the two CIs overlap.
- **κ < 0.6**: **point estimates must not be reported**. Set `l4.status` to `skipped` in `verdict.json`, write `rater_agreement_below_threshold kappa=<value>` in `note`, and state that the raters need retraining.

### 3.3 Conclusion Wording (mandatory)

- CIs **overlap** ⟹ write only "this experiment **failed to** detect a difference (N=24 per cell, insufficient power)".
- CIs **do not overlap** ⟹ may write "under this experiment's conditions, the point estimate for group A, a (CI …), is higher than that for group C, b (CI …)".
- **Under no circumstances** may "significantly reduced" be written (the sample is too small for hypothesis testing, and "significant" is already on the banned-word list).

---

## 4. Skip Path (the official behaviour when there is no API Key)

When the environment variable `QWEN_API_KEY` is missing or empty:

1. **Issue no network requests at all** (check at script start; do not make a probe call).
2. Write `reports/audit/online_baseline.skipped.json` with the structure:

```json
{
  "status": "skipped",
  "reason": "QWEN_API_KEY not set",
  "timestamp_utc": "2026-10-18T12:34:56Z",
  "env_fingerprint": { "python_version": "3.13.14", "git_commit": "…", "branch": "…" },
  "what_would_have_run": "3 groups x 12 questions x 2 repeats = 72 samples",
  "how_to_run": "set QWEN_API_KEY=<your key> && python scripts/audit_online_baseline.py",
  "report_usage": "L4 is recorded as N/A (not measured); the verdict level stays at V1"
}
```

3. **Exit code 0**. Skipping is a legitimate state, not a failure (`research.md` decision 4).
4. While this file exists, `l4.status` in `verdict.json` must be `skipped` (**not** `na_no_generation_face` - the latter refers specifically to the offline path, which has no generation surface).

---

## 5. Interfaces with Existing Artifacts

| Upstream | Usage |
| :--- | :--- |
| `backend/app/data/seed_questions.py` | question stems / options / traps / graph for the 12 questions; all three groups A, B, C share the same material |
| the `/api/diagnose` endpoint in `backend/app` | groups B and C call the real API (rather than importing directly), ensuring that what is measured is the system's actual behaviour |
| `reports/audit/verdict.json` | receives the `l4` field; V2 is only reachable when `status=measured` |

**Forbidden**: bypassing the API and calling internal functions directly inside the experiment script - that would measure "library functions", not "the system". If the server cannot be started, record groups B/C as `skipped` and explain in the note.
