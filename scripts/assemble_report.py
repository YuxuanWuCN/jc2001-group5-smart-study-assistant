#!/usr/bin/env python3
"""Assemble the 10 member chapter drafts into the master JC2001 Technical Report,
and compile the publication-grade LaTeX PDF via XeLaTeX."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINAL_REPORT_DIR = ROOT / "reports" / "final_report"
FIGURES_DIR = ROOT / "reports" / "figures"
OUTPUT_MD_1 = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.md"
OUTPUT_MD_2 = FINAL_REPORT_DIR / "FULL_TECHNICAL_REPORT_EN.md"
OUTPUT_TEX = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.tex"
OUTPUT_PDF = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.pdf"
OUTPUT_PDF_COPY = ROOT / "reports" / "StudyGraph_Cycle3_Final_Report.pdf"


def split_by_marker(text: str, marker: str) -> tuple[str, str]:
    idx = text.find(marker)
    if idx == -1:
        return text.strip(), ""
    return text[:idx].strip(), text[idx:].strip()


def normalize_subchapter_headings(folder: str, text: str) -> str:
    """Normalize top-level headings in Chapter 5 sub-packages so Chapter 5 is a single chapter."""
    if folder == "ch05_dong_siqin":
        # Remove the redundant top-level # 5.3 ... line since ## 5.3 follows immediately
        lines = text.splitlines()
        if lines and lines[0].startswith("# 5.3"):
            lines = lines[1:]
        return "\n".join(lines).strip()
    if folder == "ch05_liang_zixuan":
        # Demote '# 5.6 Deployment and Reproducibility' to '## 5.6 Deployment and Reproducibility'
        return re.sub(r"^#\s+5\.6\b", "## 5.6", text, count=1, flags=re.MULTILINE).strip()
    return text.strip()


def assemble_markdown() -> str:
    parts: list[str] = []

    ch07_path = FINAL_REPORT_DIR / "ch07_wu_yuxuan" / "draft.md"
    ch07_text = ch07_path.read_text(encoding="utf-8") if ch07_path.exists() else ""

    front_matter, ch07_rest = split_by_marker(ch07_text, "# 7 Conclusions")
    ch07_body, ch07_tail = split_by_marker(ch07_rest, "# Appendix A")
    app_a_and_b, ch07_after_b = split_by_marker(ch07_tail, "# Appendix C")
    _, refs_block = split_by_marker(ch07_after_b, "# References")

    if front_matter:
        parts.append(front_matter)

    ordered_dirs = [
        "ch01_lin_yongtong",
        "ch02_zhang_zijian",
        "ch03_xie_weixin",
        "ch04_wang_sijian",
        "ch05_jiang_hao",
        "ch05_dong_siqin",
        "ch05_xi_yusai",
        "ch05_liang_zixuan",
        "ch06_yang_mingjie",
    ]

    app_c_detailed = ""
    app_d_detailed = ""

    for folder in ordered_dirs:
        draft_path = FINAL_REPORT_DIR / folder / "draft.md"
        if not draft_path.exists():
            continue
        raw = draft_path.read_text(encoding="utf-8").strip()
        raw = normalize_subchapter_headings(folder, raw)

        if folder == "ch05_jiang_hao" and "# Appendix D" in raw:
            main_part, app_d_detailed = split_by_marker(raw, "# Appendix D")
            parts.append(main_part)
        elif folder == "ch06_yang_mingjie" and "## Appendix C" in raw:
            main_part, app_c_raw = split_by_marker(raw, "## Appendix C")
            app_c_detailed = re.sub(r"^##\s+Appendix C", "# Appendix C", app_c_raw, count=1)
            parts.append(main_part)
        else:
            parts.append(raw)

    if ch07_body:
        parts.append(ch07_body)

    if refs_block:
        parts.append(refs_block)

    if app_a_and_b:
        parts.append(app_a_and_b)
    if app_c_detailed:
        parts.append(app_c_detailed)
    if app_d_detailed:
        parts.append(app_d_detailed)

    merged = "\n\n---\n\n".join(p.strip().strip("-").strip() for p in parts if p.strip()) + "\n"
    OUTPUT_MD_1.write_text(merged, encoding="utf-8")
    OUTPUT_MD_2.write_text(merged, encoding="utf-8")
    word_count = len(merged.split())
    print(f"[Assemble] Wrote {OUTPUT_MD_1.name} & {OUTPUT_MD_2.name} ({word_count:,} words, {len(merged):,} chars)")
    return merged


if __name__ == "__main__":
    assemble_markdown()

