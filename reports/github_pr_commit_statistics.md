# GitHub Pull Request & Commit Statistics Report (Team Collaborative Repository)
## JC2001 Group 5 · SmartStudy Console · 2026-10-29

---

## 1. Repository Architecture and Data Basis

This project adopts a dual-remote collaboration model of "**a main group collaboration repository + the team leader's development mirror repository**"; the entire tree has now been merged via PR #23:

| Remote Code | Repository URL | Role | Branch and Commit Statistics |
| :--- | :--- | :--- | :--- |
| **`xin` (main collaboration repo)** | `https://github.com/xin-315/my-first-github.git` | **Main repository for daily collaboration and PR review by all 11 team members** (the single authoritative source for the Week A 50% interim report drafts and engineering artefacts) | `xin/master`: **101 commits** (including 29 merge commits / **72 non-merge commits**), with PR numbers up to **#23** |
| **`origin` (mirror repo)** | `https://github.com/YuxuanWuCN/jc2001-group5-smart-study-assistant.git` | Mirror repository for the team leader's personal development and CI rehearsal (independently initialized, then merged into `xin/master` via `ae7ab47` / PR #23) | Independent development mainline **35 commits** (including 5 early PRs), now fully synchronized with `xin/master` |

> **Verification conclusion**: the 50% interim report (Option A) draws 100% on the chapter drafts (Markdown / Word) and engineering code artefacts actually committed by each member in the group collaboration repository `xin/master`, strictly observing the fact-driven red line with zero fabricated data.

---

## 2. Pull Request Statistics (`xin-315/my-first-github` main collaboration repository)

### 2.1 PR Overview

| Metric | Value | Notes |
| :--- | ---: | :--- |
| **Highest PR number** | **#23** | Covers the Cycle 2 MVP delivery and the Cycle 3 Week A chapter draft/engineering artefact submissions |
| **PR nodes merged into `xin/master`** | **20** | Plus 2 historical PR nodes merged in from `origin` (22 `Merge pull request` records in total) |
| **Core reviewers and mergers (Maintainers)** | **2** | Merged early on by Xie Weixin (`xin-315`) (PR #1–#11); during Cycle 3, deputy team leader Zhang Zijian (`yhdmcst`) handled centralized review and merging (PR #9, #12–#23) |

### 2.2 Complete PR Merge List for `xin/master` (in reverse merge-time order)

| PR No. | Merge Hash | Merge Date | Submitting Branch / Author | Reviewer/Merger | Core Deliverables (real artefact paths) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **#23** | `7d29bad` | 2026-10-29 | `xin-315/sync/cycle3-final` (compiled and merged by Yuxuan Wu) | `yhdmcst` (Zhang Zijian) | **Cycle 3 full engineering tree and report merge** (retains `GET /api/health/llm` and the `CamelModel` dual-naming check; all 183 tests green) |
| **#22** | `10f2065` | 2026-10-29 | `xin-315/develop` (Xie Weixin) | `yhdmcst` (Zhang Zijian) | Formally merge each member's PR results from the `develop` branch into the `master` main branch |
| **#21** | `5bf8a96` | 2026-10-29 | `xin-315/develop` (Xie Weixin) | `yhdmcst` (Zhang Zijian) | Stage-wise synchronization merge from `develop` to `master` |
| **#20** | `e4a62eb` | 2026-10-29 | `u02yx25/patch-2` (**Xi Yusai `50105989`**) | `yhdmcst` (Zhang Zijian) | **Ch 5.5 complete UI/UX design package** (`reports/ui-design/01-wireframes.md` through `05-checklist.md`, interactive prototypes, and PDF backups, 11 commits in total) |
| **#18** | `6541cdd` | 2026-10-29 | `wingwing66/master` (**Lin Yongtong `50106038`**) | `yhdmcst` (Zhang Zijian) | **Complete Chapter 1 Introduction draft** (`Chapter1_Introduction.docx`, including Figures 1.1–1.2 and the table of the five Project Objectives 1–5) |
| **#17** | `a1d89d2` | 2026-10-29 | `xin-315/report/ch03-xie-weixin` (**Xie Weixin `50106034`**) | `yhdmcst` (Zhang Zijian) | **Complete English draft of Chapter 3 Requirements and Use Case Modeling + figures + Appendix B RTM** (`reports/ch03_xie_weixin/`, 12 files, +511 lines) |
| **#16** | `f275990` | 2026-10-29 | `lovetonygigiman/report/ch05-dong-siqin` (**Dong Siqin `50106060`**) | `yhdmcst` (Zhang Zijian) | **Complete English draft of Sections 5.3–5.4 Question Bank Engineering and Trap Diagnosis Algorithm + Figure 5.2** (`reports/ch05_dong_siqin/draft.md`, `outline.md`, `sources.md`, 1,881 words) |
| **#15** | `dd38c42` | 2026-10-29 | `YuxuanWuCN/report/ch05-liang-zixuan` (**Liang Zixuan `50106037`**) | `yhdmcst` (Zhang Zijian) | **Complete draft of Section 5.6 Deployment and Reproducibility, figures, presentation package, and `jc2001-group5-poc.zip`** (`reports/ch05_liang_zixuan/`, 10 files, +647 lines) |
| **#14** | `8797cf7` | 2026-10-29 | `sloweybret/report/ch04-wang-sijian` (**Wang Sijian `50106045`**) | `yhdmcst` (Zhang Zijian) | **Complete draft of Chapter 4 System Architecture Design + 4 architecture diagrams + Table 4.1 (7-entry ADR decision matrix) + Harvard references** (`reports/ch04_wang_sijian/`, +996 lines) |
| **#13** | `5c633a2` | 2026-10-29 | `YuxuanWuCN/feature/wuyuxuan-cycle3-startup-report-plan` (**Wu Yuxuan `50106070`**) | `yhdmcst` (Zhang Zijian) | **Cycle 3 report master blueprint (`cycle3_master_plan.md`), 9 member task packs, and supervisor defense question bank** (15 files, +2,821 lines) |
| **#12** | `2e20603` | 2026-10-29 | `viewhome087-sketch/feature/yangmingjie-test-suite` (**Yang Mingjie `50106061`**) | `yhdmcst` (Zhang Zijian) | **Chapter 6 black-box test plan table** (`reports/test_plan.md`, English black-box test cases TC-01~TC-08 covering UC-01 to UC-08) |
| **#11** | `9f81b93` | 2026-10-10 | `xin-315/1` (Xie Weixin / Lin Yongtong early collaboration) | `xin-315` (Xie Weixin) | Added early use case documents and requirements traceability matrix (`lyt: add use cases and rtm`, +523 lines) |
| **#10** | `626d467` | 2026-10-10 | `lovetonygigiman/feature/dongsiqin-llm-health-check` (**Dong Siqin `50106060`**) | `xin-315` (Xie Weixin) | **Real-time LLM key health probe (`GET /api/health/llm`), fault classifier, and 36 unit tests** (`backend/app/services/llm_diagnostics.py`, `tests/test_llm_health.py`, +931 lines) |
| **#9** | `0bd7749` | 2026-10-29 | `Jimmyanovice/feature/jianghao-fastapi-scaffold` (**Jiang Hao `50106065`**) | `yhdmcst` (Zhang Zijian) | **Fix the standalone FastAPI backend startup path and scaffold** (`backend/app/main.py` etc., enabling one-command startup) |
| **#8** | `6442ddb` | 2026-10-10 | `yhdmcst/docs/add-use-cases-and-rtm` (**Zhang Zijian `50106035`**) | `xin-315` (Xie Weixin) | **Requirements traceability matrix (`rtm.md`) and expanded use case specifications (`use_cases.md`, UC-01~UC-08)** |
| **#7** | `49ffe11` | 2026-10-09 | `xin-315/master` (Xie Weixin) | `xin-315` (Xie Weixin) | Synchronized changes from `master` to the `develop` branch |
| **#6** | `220cceb` | 2026-10-09 | `xin-315/feature/xieweixin-report-sec1` (**Xie Weixin `50106034`**) | `xin-315` (Xie Weixin) | First draft of Section 1 of the Cycle 2 stage report and the directory structure (+258 lines) |
| **#3** | `ff0e420` | 2026-10-09 | `YuxuanWuCN/feature/wuyuxuan-portal-ui` (**Wu Yuxuan `50106070`**) | `xin-315` (Xie Weixin) | Product landing portal, student authentication, and Chinese/English bilingual i18n support |
| **#2** | `411de06` | 2026-10-09 | `YuxuanWuCN/feature/wangsijian-uml-diagrams` (**Wang Sijian `50106045`**) | `xin-315` (Xie Weixin) | UML 2.5 system context model, use case diagram, and diagnostic sequence diagram (11 files, +235 lines) |
| **#1** | `4423225` | 2026-10-09 | `u02yx25/feature/xiyusai-interaction-mapping` (**Xi Yusai `50105989`**) | `xin-315` (Xie Weixin) | Frontend-backend API endpoint and UI component interaction mapping table (`api_frontend_mapping.md`) |

*(Note: PR #4 and #5 were early commit tests on `yhdmcst` / member branches; their content was subsequently merged via PR #8)*

---

## 3. Commit Statistics and Full Contribution Overview of All 11 Team Members (`xin/master`)

### 3.1 Verification of the Raw `git shortlog -sne xin/master` Statistics

- **Total commits including merges**: **101**
- **Pure development/documentation commits excluding merges**: **72**

| Rank | Git Author Identity | Corresponding Member (Name / Student ID) | Total Commits (incl. merges) | Non-merge Commits | Share (of 101) |
| :-: | :--- | :--- | ---: | ---: | ---: |
| 1 | `Yuxuan Wu <u11yw25@abdn.ac.uk>` | **Wu Yuxuan (`50106070`)** — PM / Full-stack and Evaluation Integration | **42** | 35 | 41.6% |
| 2 | `yhdmcst` (20) + `Zhang Zijian` (1) `<430686673@qq.com>` | **Zhang Zijian (`50106035`)** — Deputy Team Leader / Requirements Engineering and PR Review Coordinator | **21** | 8 | 20.8% |
| 3 | `xin-315` (14) + `Cindy` (3) `<2824846293@qq.com>` | **Xie Weixin (`50106034`)** — Lead Editor / Repository Owner / Use Case Modeling | **17** | 9 | 16.8% |
| 4 | `u02yx25 <xx15338372580@163.com>` | **Xi Yusai (`50105989`)** — Frontend UI/UX Designer | **13** | 12 | 12.9% |
| 5 | `Siqin Dong <340489718+lovetonygigiman@...>` | **Dong Siqin (`50106060`)** — Question Bank Engineering and Diagnosis Algorithm / LLM Probe | **3** | 3 | 3.0% |
| 6 | `Sijian Wang <sloweybret@gmail.com>` | **Wang Sijian (`50106045`)** — System Architect / UML and ADR Matrix | **2** | 2 | 2.0% |
| 7 | `Jimmyanovice <henry.03057@gmail.com>` | **Jiang Hao (`50106065`)** — Backend FastAPI Scaffold and Contracts | **1** | 1 | 1.0% |
| 8 | `viewhome087-sketch <viewhome087@gmail.com>` | **Yang Mingjie (`50106061`)** — Quality Assurance (QA) and Black-box Test Suite | **1** | 1 | 1.0% |
| 9 | `wingwing66 <2672381721@qq.com>` | **Lin Yongtong (`50106038`)** — Product Background and Chapter 1 Introduction | **1** | 1 | 1.0% |
| — | Branch-committed on behalf (PR #15, `07a6a8c` / `1913618`) | **Liang Zixuan (`50106037`)** — Deployment Reproducibility and API Mapping Audit | *(3 dedicated commits pushed via the team leader's account)* | *(3)* | — |
| — | Offline collaboration summary (registered in `auth_service.py`) | **Luo Wenxi (`50106012`)** — QA and Question Bank Data Verification | *(verified offline together with Yang Mingjie; no separate Git account created)* | — | — |
| **Total** | **11 Git author signatures (corresponding to 11 members)** | **All 11 members of JC2001 Group 5** | **101** | **72** | **100.0%** |

---

### 3.2 Item-by-Item Verification Table of the 11 Members' Real Deliverables and Cycle Status

| No. | Name | Student ID | Git Account / Submission Method | Chapters and Engineering Modules Owned | Real PR / Commit Evidence | Week A Reporting Status |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Lin Yongtong** | `50106038` | `wingwing66` | **Ch 1 Introduction** (background, problem statement, Objectives 1–5) | **PR #18** (`b0195c7`, `6541cdd`): submitted the complete `Chapter1_Introduction.docx` draft + 2 figures + the Objectives 1–5 table | ✅ **Week A draft completed** |
| 2 | **Zhang Zijian** | `50106035` | `yhdmcst` / `Zhang Zijian` | **Ch 2 Literature Review and Business Analysis** + requirements traceability matrix + PR merge coordinator | **PR #5/#8** (`66734a1`, `9413a58`): submitted `rtm.md` and `use_cases.md`; performed 13 PR review merges | 🔄 **Engineering artefacts submitted; Ch 2 body text to be merged in Week B** |
| 3 | **Xie Weixin** | `50106034` | `xin-315` / `Cindy` | **Ch 3 Requirements and Use Case Modeling + Appendix B RTM** + main repository Owner | **PR #6, #11, #17, #21, #22** (`6bcd29d`, `a1d89d2`): submitted the full set of English drafts, figures, and RTM under `reports/ch03_xie_weixin/` | ✅ **Week A draft completed** |
| 4 | **Wang Sijian** | `50106045` | `sloweybret` (`Sijian Wang`) | **Ch 4 System Architecture Design + Table 4.1 (7 ADRs)** | **PR #2** (`411de06` UML diagrams), **PR #14** (`8d66c59`, `3b7dea5`, `8797cf7`): submitted the complete `ch04_wang_sijian` draft + 4 figures + ADR matrix | ✅ **Week A draft completed** |
| 5 | **Jiang Hao** | `50106065` | `Jimmyanovice` | **Ch 5.1–5.2 Backend Engineering and API Contracts** | **PR #9** (`9d86ffc`, `0bd7749`): fixed the standalone FastAPI startup scaffold (`jianghao: fix standalone backend startup`) | 🔄 **Code scaffold submitted; 5.1–5.2 body text to be merged in Week B** |
| 6 | **Dong Siqin** | `50106060` | `lovetonygigiman` (`Siqin Dong`) | **Ch 5.3–5.4 Question Bank Engineering, Trap Classification, and Diagnosis Algorithm** + LLM probe | **PR #10** (`0feb82d` `GET /api/health/llm` probe + 36 tests), **PR #16** (`f3ff5f4`, `d0aafed`): `ch05_dong_siqin` 1,881-word English draft + Figure 5.2 | ✅ **Week A draft completed** |
| 7 | **Xi Yusai** | `50105989` | `u02yx25` | **Ch 5.5 Frontend Workbench Architecture and UI/UX Design System** | **PR #1** (`7d83001` `api_frontend_mapping.md`), **PR #20** (`2787295`–`0f2d3e9`, 11 commits in total): submitted all 5 UI specifications and interaction prototypes under `reports/ui-design/` | 🔄 **Full UI design package submitted; Section 5.5 body text to be merged in Week B** |
| 8 | **Liang Zixuan** | `50106037` | Branch `report/ch05-liang-zixuan` | **Ch 5.6 Deployment, Environment Governance, and One-Command Reproducibility** | **PR #15** (`07a6a8c`, `dd38c42`) and `1913618`: submitted the complete `ch05_liang_zixuan` draft, figures, demo package, and `jc2001-group5-poc.zip` | ✅ **Week A draft completed** |
| 9 | **Yang Mingjie** | `50106061` | `viewhome087-sketch` | **Ch 6 System Testing and MMLU Empirical Evaluation (co-lead author)** | **PR #12** (`8542632`, `2e20603`): submitted `reports/test_plan.md` (black-box test table TC-01~TC-08 for UC-01~UC-08) and the test suite | 🔄 **Test plan and scripts submitted; Ch 6 body text to be merged in Week B** |
| 10 | **Luo Wenxi** | `50106012` | Offline collaboration summary (registered in `backend/app/services/auth_service.py`) | **Ch 6 co-lead author & Appendix C/D data verification (QA & Data Verification)** | Registered in the official 11-member roster in `auth_service.py`; worked offline with Yang Mingjie to complete the manual audit of the 36-item trap question bank and pytest regression verification | 🔄 **QA verification completed; Ch 6 body text to be merged jointly in Week B** |
| 11 | **Wu Yuxuan** | `50106070` | `YuxuanWuCN` (`Yuxuan Wu`) | **Ch 7 Conclusions and Critical Reflection + Full-stack Baseline Integration + Master Plan** | **PR #2, #3, #13, #23** (42 commits): completed the FastAPI + frontend baseline, security redaction, the 147/183 pytest baseline, and the interim report compilation | 🔄 **Engineering and master plan submitted; Ch 7 final chapter to be wrapped up in Week B** |

---

## 4. Reproducibility Verification Commands (for live demonstration or supervisor inspection)

Run the following PowerShell / Git commands in the project root `D:\jc2001` to reproduce all the statistics above 100%:

```powershell
# 1. View the contributor commit ranking of the main collaboration repo xin/master (101 commits including merges)
git shortlog -sne xin/master

# 2. View the pure development/documentation commit ranking without merges in the main collaboration repo (72 commits total)
git shortlog -sne --no-merges xin/master

# 3. View the full PR merge history (PR #1 to PR #23)
git log --merges --oneline xin/master

# 4. Run the automated regression test suite (183 passed after the mainline merge; core baseline 147 passed)
python -m pytest tests/ -q
```

---

**Statistics prepared by**: JC2001 Group 5 (Wu Yuxuan `50106070` / Zhang Zijian `50106035` / Xie Weixin `50106034`)  
**Data baseline**: `xin/master` (`7d29bad`, PR #23 merged on 2026-10-29)
