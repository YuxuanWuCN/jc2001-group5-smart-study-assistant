#!/usr/bin/env python3
"""Assemble the 10 member chapter drafts into the master JC2001 Technical Report."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINAL_REPORT_DIR = ROOT / "reports" / "final_report"
OUTPUT_PATH = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.md"

# Official 10-member chapter order (from reports/cycle3_task_packs/README.md)
SECTIONS = [
    ("ch07_wu_yuxuan", "front_matter"),
    ("ch01_lin_yongtong", "full"),
    ("ch02_zhang_zijian", "full"),
    ("ch03_xie_weixin", "full"),
    ("ch04_wang_sijian", "full"),
    ("ch05_jiang_hao", "main"),
    ("ch05_dong_siqin", "full"),
    ("ch05_xi_yusai", "full"),
    ("ch05_liang_zixuan", "full"),
    ("ch06_yang_mingjie", "main"),
    ("ch07_wu_yuxuan", "ch07_and_app_a"),
    ("ch03_xie_weixin", "app_b"),
    ("ch06_yang_mingjie", "app_c"),
    ("ch05_jiang_hao", "app_d"),
]


def split_by_marker(text: str, marker: str) -> tuple[str, str]:
    idx = text.find(marker)
    if idx == -1:
        return text, ""
    return text[:idx].strip(), text[idx:].strip()


def assemble() -> Path:
    parts: list[str] = []

    ch07_path = FINAL_REPORT_DIR / "ch07_wu_yuxuan" / "draft.md"
    ch07_text = ch07_path.read_text(encoding="utf-8") if ch07_path.exists() else ""
    front_matter, ch07_body = split_by_marker(ch07_text, "# 7 Conclusions and Future Work")
    if not ch07_body:
        front_matter, ch07_body = split_by_marker(ch07_text, "## 7.1")

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

    appendices: list[str] = []

    for folder in ordered_dirs:
        draft_path = FINAL_REPORT_DIR / folder / "draft.md"
        if not draft_path.exists():
            continue
        raw = draft_path.read_text(encoding="utf-8").strip()
        if folder == "ch05_jiang_hao" and "# Appendix D" in raw:
            main_part, app_d = split_by_marker(raw, "# Appendix D")
            parts.append(main_part)
            appendices.append(app_d)
        elif folder == "ch06_yang_mingjie" and "# Appendix C" in raw:
            main_part, app_c = split_by_marker(raw, "# Appendix C")
            parts.append(main_part)
            appendices.append(app_c)
        else:
            parts.append(raw)

    if ch07_body:
        parts.append(ch07_body)
    elif ch07_text and not front_matter:
        parts.append(ch07_text.strip())

    for app in appendices:
        if app:
            parts.append(app)

    merged = "\n\n---\n\n".join(p for p in parts if p) + "\n"
    OUTPUT_PATH.write_text(merged, encoding="utf-8")
    word_count = len(merged.split())
    print(f"Assembled {OUTPUT_PATH} ({word_count:,} words, {len(merged):,} chars)")
    return OUTPUT_PATH


if __name__ == "__main__":
    assemble()
