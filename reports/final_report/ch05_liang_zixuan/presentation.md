# §9 Presentation and Video — Production Pack

**Owner:** Zixuan Liang (50106037) · **Scope:** task pack 08, §9 (15-minute video + PPTX)
**Status:** outline and script complete; recording is a team action.

This file closes the last open item of the task pack's Definition of Done
(*"the demonstration video and the slide outline are delivered; see §9"*). It is a production
document, not report prose: the deck is English, and the group's working language remains Chinese.

---

## 1. Fixed constraints (from the brief, non-negotiable)

| Constraint | Value |
| :--- | :--- |
| Length | 15 minutes; final cut 14:30–15:00 |
| Deliverables in the ZIP | `presentation.pptx` **and** `presentation.mp4` |
| Presenter visibility | every one of the 10 members on camera for **at least 30 s** |
| Opening | a group shot in the first 10 seconds |
| Recording | OBS or the system recorder, **1080p**, audio tested separately |
| Rehearsal | at least two, the second one timed |
| Slide density | ≤ 6 lines per slide, ≤ 20 words per line, no paragraphs |

> Audio quality matters more than picture quality. A clean voice track over a screen recording
> scores better than a beautiful 4K frame with room echo.

---

## 2. Running order

| Time | Segment | On camera | Condition |
| :--- | :--- | :--- | :--- |
| 0:00–1:30 | Opening and problem statement | Yuxuan Wu | open with one concrete revision scenario, not a slide definition |
| 1:30–4:00 | **Live demonstration** | Yusai Xi or Hao Jiang | answer → deliberately choose the wrong option → open the five-layer drawer |
| 4:00–6:00 | Requirements and scope | Zijian Zhang | emphasise what was cut: the four *Won't* items |
| 6:00–8:30 | Architecture and decisions | Sijian Wang | argue *why not* the alternatives |
| 8:30–10:30 | Trap engineering and diagnosis | Siqin Dong | include the row where the lookup table loses to the model |
| 10:30–12:30 | Testing and empirical results | Mingjie Yang | report the two negative results unprompted |
| **12:30–14:00** | **Deployment and reproducibility** | **Zixuan Liang (you)** | demonstrate a clean start, or play a 15 s pre-recorded clip |
| 14:00–15:00 | Conclusions, limitations, thanks | Yuxuan Wu | close on the boundary of the claims |

---

## 3. Deck outline — 14 slides

Slide text is English, written to be shown, not read aloud.

| # | Title on the slide | Content (≤6 lines) | Cue for the speaker |
| :-: | :--- | :--- | :--- |
| 1 | StudyGraph — diagnostic practice for university revision | Project name · JC2001 Group 5 · 10 names and IDs · supervisor | group shot in the first 10 s |
| 2 | Binary feedback hides the reasoning gap | 4 lines: right/wrong only · no prerequisite · no evidence · student gives up | one concrete scenario, first person |
| 3 | Existing tools solve a different problem | Quizlet marks · a general assistant spoils the answer · neither shows evidence | "we are not competing with them, we are filling the gap they leave" |
| 4 | What we built | one sentence + main console screenshot | hand over to the live demo |
| 5 | Live demonstration | ← transition slide, one line | "let me show you instead of describing it" |
| 6 | Scope: 14 requirements, 4 deliberately out | MoSCoW summary · R11–R14 marked *Won't* · one line on why | "saying no is part of the design" |
| 7 | Architecture | Figure 4.1, four layers | one sentence per layer, no more |
| 8 | Three decisions that shaped the build | ADR-01 single process · ADR-05 graph offline · ADR-06 permissive CORS for local demo | argue *why not* the alternative |
| 9 | From trap data to a five-layer drawer | `TrapDetail` fields → drawer layers | the mapping, not the screenshot |
| 10 | Lookup table versus language model | comparison table row by row | include the row we lose |
| 11 | Testing: 150 cases, all offline | test pyramid · adversarial suites · 1.79 s | **150, not 145** — see §5 |
| 12 | Empirical results | accuracy by subject · **two regressions shown** | volunteering the negative results is the credibility signal |
| 13 | Conclusions and future work | 3 lines: what works · what is partial · what is next | do not oversell |
| 14 | Q&A backup | data appendix: provenance, licences, counts | keep on screen for questions |

---

## 4. Your segment: 12:30–14:00 (90 seconds)

### 4.1 What you are proving

One sentence: *the examiner can run this on their own machine, offline, in about a minute.*
Everything else in the segment is evidence for that sentence.

### 4.2 Live demonstration (the two commands)

```bash
uvicorn backend.app.main:app --port 8000        # terminal, second window
# then open http://127.0.0.1:8000 in the browser
```

Rehearse this exact sequence. Before recording: close every other browser tab, clear the terminal,
set the font size to something readable at 1080p, and make sure port 8000 is free
(`netstat -ano | findstr :8000`).

### 4.3 Script (~200 words, ≈ 90 s at a measured pace)

> Section 5.6 is the deployment chapter, and I want to spend ninety seconds on one claim: you can run
> this on your own laptop, offline, without a database and without a key.
>
> Here is the service starting. One command — `uvicorn backend.app.main:app` on port 8000. No
> configuration file, no environment variable, no credential. And here it is in the browser: the same
> process is serving both the interface and the API, which is why there is no CORS in the demo path.
>
> The whole test suite runs offline in under two seconds — 150 cases — because the session fixture
> deletes the API keys before every test. So what we are measuring is the fallback path, not a lucky
> network call.
>
> Two honest notes. The dependency manifest is wider than the service needs: the full install takes
> about six and a half minutes, while the seven packages we actually import take forty-four seconds —
> we recommend splitting the manifest. And the benchmark evaluation is only *partially* reproducible:
> it needs a cloud graph database whose password we rotated. Every number in Chapter 6 traces to a
> snapshot that ships with the repository. We would rather say that than claim something you can
> disprove with one command.

### 4.4 Fallback

If the live start fails on the day, play the 15-second pre-recorded clip of the same two commands and
say the sentence anyway. Do not debug on camera. Record the clip during the second rehearsal.

---

## 5. Number consistency for the whole deck

| Number | Use this | Why |
| :--- | :--- | :--- |
| Test cases | **150** | measured: `150 passed in 1.79 s`; the study plan's 145 is stale, and one slide silently quoting 145 will be caught |
| Question bank | 12 items, 36 traps | from `seed_questions.py` and the assessment table |
| API surface | say *"the four documented endpoints described in Section 5.2"* **or** the number the leader settles on | the project currently has three incompatible counts in circulation: 8 (PR description), 5 (task-pack sketch), 4 (OpenAPI). Until it is fixed, the deck should defer to Section 5.2 rather than add a fourth number |
| Cold start | 1.12 s | measured, reproduce before recording |
| Full install | ~6.5 min | measured 397 s; do not repeat the "under five minutes" line on camera |

---

## 6. On-camera and recording checklist

- [ ] all 10 members appear, each for at least 30 s (Team Participation is scored)
- [ ] group shot within the first 10 seconds
- [ ] 1080p, 30 fps, one consistent layout (webcam bottom-right or full-screen when speaking)
- [ ] microphone tested separately; no fan noise, no keyboard clicks over the voice track
- [ ] terminal and browser font sizes verified at 1080p (text readable when the video is scaled down)
- [ ] no credentials, tokens or private email addresses visible on screen — check the terminal history
      and any open editor before recording
- [ ] every slide checked against the ≤6 lines / ≤20 words rule
- [ ] `presentation.pptx` and `presentation.mp4` both added to the ZIP before submission

---

## 7. Rehearsal plan

| Rehearsal | When | Gate |
| :--- | :--- | :--- |
| 1 — run-through | one week before | each speaker finishes inside their slot, no full read from the slide |
| 2 — timed | two days before | total between 14:30 and 15:00; the fallback clip is recorded in this session |
| 3 — technical | the day before | clean machine start on camera, audio levels, screen resolution |

---

## 8. Risks

| Risk | Trigger | Response |
| :--- | :--- | :--- |
| Live start fails | port busy, wrong interpreter, missing dependency | play the pre-recorded clip, say the sentence, move on |
| Segment overruns | over-rehearsed detail | the 90 s script has a hard cut after the two honest notes |
| Nobody appears on camera | people decline | assign the 30 s windows during rehearsal 1, not on the day |
| A slide contradicts a chapter | a number changes late | §5 above is the single source for deck numbers |
