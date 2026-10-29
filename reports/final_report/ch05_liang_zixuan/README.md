# Chapter 5.6 Delivery Package

**Author:** Zixuan Liang (50106037) · Deployment and Media Lead
**Deliverable:** task pack 08 — Section 5.6 *Deployment and Reproducibility*, plus the presentation pack
**Repository snapshot used for every figure quoted:** `xin-315/my-first-github`, branch `develop`,
head `626d46707f4d3296b354b47c3fcba5d8a80ba1fc`
**Measurements taken:** 19 October 2026, Windows 11, Python 3.14.0, localhost only, no credentials present

---

## 1. Contents

| File | What it is | Length |
| :--- | :--- | :--- |
| `draft.md` | **The section**, in report form: 5.6.1–5.6.5, Figure 5.5, Table 5.7 | 1,590 words, ~3.5 pages |
| `figures/fig5_5_deployment.svg` | Figure 5.5, vector — **use this one in the report** | 578 × 756 units, self-contained |
| `figures/fig5_5_deployment.png` | Same figure at 2× for slides or chat | 1,220 × 1,576 px |
| `figures/fig5_5_deployment.mmd` | Mermaid source, if the figure has to be redrawn | — |
| `outline.md` | Step 1 outline: three-level structure, material list, boundaries with neighbouring chapters | — |
| `sources.md` | Every claim traced to a repository file, with the measurement conditions | — |
| `supervisor_summary.md` | One-page standalone summary, for sending to the supervisor on its own | — |
| `presentation.md` | §9 production pack: running order, 14-slide deck outline, the 90-second deployment script | — |
| `jc2001-group5-poc.zip` | The PoC archive. **Quarantined 2026-10-25 and again 2026-10-29:** every committed snapshot carried a nested archive with pre-remediation hardcoded credentials, so the archive is no longer a repository artefact. Build it from the submission HEAD and run the secret scan (0 hits) before distribution. | not tracked |

## 2. How to use it

1. Paste `draft.md` into Chapter 5, after Section 5.5. The headings are already numbered 5.6.1–5.6.5.
2. Insert `figures/fig5_5_deployment.svg` where the `![Figure 5.5](...)` line is. Vector output keeps
   the text sharp in Word and PDF; do not use the PNG unless the target tool rejects SVG.
3. `Table 5.7` is written as a Markdown table with the caption above it, per the group convention.
4. `sources.md` is not part of the report; it exists so that any number can be re-derived.

## 3. What is measured, and where

| Claim | Value | How |
| :--- | :--- | :--- |
| Cold start | 1.12 s | process launch → first `200` on `/api/health` |
| Application shell | 40,390 bytes in 50.9 ms | `GET /` against the running service |
| Test suite | 150 passed in 1.79 s | `python -m pytest tests/ -q` |
| Full dependency install | 397 s, 63 packages, 416 MB | fresh virtual environment, `pip install -r requirements.txt` |
| Minimal dependency install | 44 s, 32 packages, 50 MB | the seven packages the service and the suite import |
| Submission archive | 48 entries, 1.05 MB, unpacks to 1.82 MB | unpacked into an empty directory and re-tested there |

## 4. Open items this package cannot close

| Item | Owner | Why it matters |
| :--- | :--- | :--- |
| `docs/User_Manual.pdf` (8–12 pages) does not exist anywhere in the repository | Chapter 6 author | the brief requires it inside the PoC archive |
| Five credentials (DashScope, Neo4j, two Zhipu, one Gemini) were committed in 2026-09 and remain in the git history; only console-side rotation retires them | project leader + the script owner | deleting the files cannot un-publish a key; the packaging step greps for the literal prefixes before submission |
| Endpoint count circulating as 8 (PR description), 5 (task-pack sketch) and 4 (OpenAPI) | project leader | until it is fixed, the deck should defer to Section 5.2 rather than print a fourth number |

## 5. Conventions followed

British spelling; first-person plural `we`; past tense for design and implementation decisions;
no source code in the prose (the only code blocks are shell commands and a directory tree); no
internal process vocabulary (`task pack`, `PM`, `group leader`) anywhere in `draft.md`.
