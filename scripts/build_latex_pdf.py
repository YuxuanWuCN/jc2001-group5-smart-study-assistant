#!/usr/bin/env python3
"""Compile the assembled JC2001 Group 5 English Technical Report and Supervisor Briefing
into publication-grade PDFs using PyMuPDF SVG rasterization and MiKTeX XeLaTeX."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent
FINAL_REPORT_DIR = ROOT / "reports" / "final_report"
FIGURES_DIR = ROOT / "reports" / "figures"
PNG_DIR = FINAL_REPORT_DIR / "figures_png"

MD_REPORT = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.md"
TEX_REPORT = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.tex"
PDF_REPORT = FINAL_REPORT_DIR / "StudyGraph_Cycle3_Final_Report.pdf"
PDF_REPORT_ROOT_COPY = ROOT / "reports" / "StudyGraph_Cycle3_Final_Report.pdf"

MD_BRIEFING = ROOT / "reports" / "afternoon_supervisor_questions.md"
TEX_BRIEFING = ROOT / "reports" / "afternoon_supervisor_questions.tex"
PDF_BRIEFING = ROOT / "reports" / "afternoon_supervisor_questions.pdf"

XELATEX_BIN = r"C:\Users\45607\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
if not Path(XELATEX_BIN).exists():
    XELATEX_BIN = shutil.which("xelatex") or "xelatex"

# Figures too dense to read at portrait width get a dedicated landscape page.
# fig_seq_diagnose is ~1:1 with 15 px message labels; figures/README.md already
# documents that it needs a full landscape page (24 cm) to stay above 5 pt.
LANDSCAPE_FIGURES = {"fig_seq_diagnose.svg"}
# Minimum acceptable effective printed size for a figure's median label.
# Body text is 10 pt; 5 pt is the practical floor for A4 print legibility.
MIN_PRINTED_PT = 5.0


RASTER_DPI = 300
# Padding (in mm) re-added around the trimmed content box so strokes are not
# flush against the image border when the PNG is placed in the PDF.
TRIM_PAD_MM = 1.2
# Per-channel tolerance for deciding "this pixel is background".
TRIM_TOLERANCE = 6


def _load_svg_document(svg_path: Path) -> fitz.Document:
    """Open an SVG with PyMuPDF, repairing percentage width/height on the root tag.

    A root tag carrying ``width="100%" height="100%"`` makes PyMuPDF fall back to
    a Letter-sized 612x792 page, which letterboxes the drawing inside a huge white
    canvas (this is what produced the 718 px / 633 px blank bands around
    fig5_2_trap_causal_chain). Rewriting the percentages to the intrinsic viewBox
    size restores the true drawing extent.
    """
    text = svg_path.read_text(encoding="utf-8", errors="replace")
    head = re.search(r"<svg\b[^>]*>", text, flags=re.S)
    if head:
        tag = head.group(0)
        has_pct = re.search(r'\bwidth\s*=\s*"[\d.]+%"', tag) and re.search(
            r'\bheight\s*=\s*"[\d.]+%"', tag
        )
        vb = re.search(r'\bviewBox\s*=\s*"([^"]+)"', tag)
        if has_pct and vb:
            parts = [p for p in re.split(r"[\s,]+", vb.group(1).strip()) if p]
            if len(parts) == 4:
                try:
                    vb_w, vb_h = float(parts[2]), float(parts[3])
                except ValueError:
                    vb_w = vb_h = 0.0
                if vb_w > 0 and vb_h > 0:
                    fixed = re.sub(r'\bwidth\s*=\s*"[^"]*"', f'width="{vb_w:g}"', tag, count=1)
                    fixed = re.sub(r'\bheight\s*=\s*"[^"]*"', f'height="{vb_h:g}"', fixed, count=1)
                    text = text.replace(tag, fixed, 1)
                    return fitz.open(stream=text.encode("utf-8"), filetype="svg")
    return fitz.open(str(svg_path))


def trim_whitespace(img: Image.Image, pad_px: int) -> Image.Image:
    """Crop uniform background margins, then re-pad evenly.

    Background colour is sampled from the four corners, so both the light
    infographic palette and the dark Cyber Obsidian palette trim correctly.
    """
    corners = [
        img.getpixel((0, 0)),
        img.getpixel((img.width - 1, 0)),
        img.getpixel((0, img.height - 1)),
        img.getpixel((img.width - 1, img.height - 1)),
    ]
    bg = max(set(corners), key=corners.count)
    diff = ImageChops.difference(img, Image.new(img.mode, img.size, bg)).convert("L")
    mask = diff.point(lambda v: 255 if v > TRIM_TOLERANCE else 0)
    bbox = mask.getbbox()
    if not bbox:
        return img
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - pad_px)
    y0 = max(0, y0 - pad_px)
    x1 = min(img.width, x1 + pad_px)
    y1 = min(img.height, y1 + pad_px)
    return img.crop((x0, y0, x1, y1))


def _is_well_formed_svg(svg_path: Path) -> bool:
    """Reject truncated/corrupted SVG copies before they get rasterized.

    The per-chapter figures/ directories duplicate the canonical files in
    reports/figures/. When one copy is damaged (an interrupted editor save
    produces exactly this), a name-keyed walk silently prefers the broken one.
    """
    try:
        ET.parse(svg_path)
        return True
    except ET.ParseError:
        return False


def _collect_svg_candidates() -> list[Path]:
    """Return one SVG per stem, preferring reports/figures over the chapter copies."""
    chosen: dict[str, Path] = {}
    if FIGURES_DIR.exists():
        for svg in sorted(FIGURES_DIR.glob("*.svg")):
            chosen[svg.name] = svg
    skipped: list[Path] = []
    for ch_fig in sorted(FINAL_REPORT_DIR.glob("ch*/figures/*.svg")):
        if ch_fig.name in chosen:
            continue  # canonical copy already registered
        chosen[ch_fig.name] = ch_fig
    for path in list(chosen.values()):
        if not _is_well_formed_svg(path):
            print(f"[Rasterize][SKIP] {path.relative_to(ROOT)} is not well-formed XML")
            skipped.append(path)
            del chosen[path.name]
    if skipped:
        print(f"[Rasterize] {len(skipped)} corrupted SVG(s) skipped; using canonical copies")
    return list(chosen.values())


def _svg_text_metrics(svg_path: Path) -> tuple[float, float]:
    """Return (viewbox_width, median_text_size_in_user_units) for an SVG.

    Mermaid output often exposes no extractable span dictionary, so the sizes are
    read straight from the source markup: every ``font-size`` declaration in a
    style block or attribute counts as one text run. Falls back to PyMuPDF's text
    dictionary for hand-authored SVGs that do carry spans.
    """
    text = svg_path.read_text(encoding="utf-8", errors="replace")
    head = re.search(r"<svg\b[^>]*>", text, flags=re.S)
    vb_w = 0.0
    if head:
        vb = re.search(r'\bviewBox\s*=\s*"([^"]+)"', head.group(0))
        if vb:
            parts = [p for p in re.split(r"[\s,]+", vb.group(1).strip()) if p]
            if len(parts) == 4:
                try:
                    vb_w = float(parts[2])
                except ValueError:
                    vb_w = 0.0
        if vb_w <= 0:
            w_attr = re.search(r'\bwidth\s*=\s*"([\d.]+)"', head.group(0))
            if w_attr:
                vb_w = float(w_attr.group(1))

    sizes = [float(m) for m in re.findall(r"font-size\s*:\s*([\d.]+)\s*px", text)]
    sizes += [float(m) for m in re.findall(r'font-size\s*=\s*"([\d.]+)"', text)]

    if not sizes:
        doc = _load_svg_document(svg_path)
        page = doc[0]
        if vb_w <= 0:
            vb_w = page.rect.width
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if span["text"].strip():
                        sizes.append(span["size"])
        doc.close()

    if not sizes:
        return vb_w, 0.0
    sizes.sort()
    return vb_w, sizes[len(sizes) // 2]


def _artifact_manifest_path() -> Path:
    return PNG_DIR / ".render-manifest.json"


def _load_manifest() -> dict[str, str]:
    """Read the sha256 of every PNG this pipeline produced, keyed by PNG name."""
    path = _artifact_manifest_path()
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _save_manifest(manifest: dict[str, str]) -> None:
    _artifact_manifest_path().write_text(
        json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8"
    )


def _sha256(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def rasterize_svgs() -> dict[str, dict]:
    """Rasterize every figure SVG to a trimmed 300 DPI PNG and report its metrics.

    Staleness is decided by a content manifest rather than mtime: several agents
    share this workspace, and an external write can leave a *newer* but
    lower-resolution PNG that an mtime check would happily accept.
    """
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, dict] = {}
    manifest = _load_manifest()

    svg_candidates = _collect_svg_candidates()

    pad_px = int(round(TRIM_PAD_MM / 25.4 * RASTER_DPI))
    for svg_path in svg_candidates:
        png_name = svg_path.stem + ".png"
        png_path = PNG_DIR / png_name
        sibling_png = svg_path.with_suffix(".png")
        source_svg_hash = _sha256(svg_path)
        recorded = manifest.get(png_name, {})
        up_to_date = (
            png_path.exists()
            and isinstance(recorded, dict)
            and recorded.get("svg_sha256") == source_svg_hash
            and recorded.get("png_sha256") == _sha256(png_path)
        )
        if sibling_png.exists():
            # The author-rendered sibling PNG is authoritative: some SVGs style
            # their shapes through a <style> block or foreignObject HTML, which
            # PyMuPDF cannot honour, so rasterising them straight to a pixmap
            # loses every fill and ships an unreadable black-on-black figure.
            with Image.open(sibling_png) as src_im:
                rgb_im = src_im.convert("RGB")
                trimmed = trim_whitespace(rgb_im, pad_px)
                trimmed.save(str(png_path), optimize=True)
            print(f"[Rasterize] Used authentic member PNG: {sibling_png.name}")
        elif not up_to_date:
            reason = "missing" if not png_path.exists() else "stale or externally modified"
            doc = _load_svg_document(svg_path)
            pix = doc[0].get_pixmap(dpi=RASTER_DPI, alpha=False)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            doc.close()
            before = img.size
            img = trim_whitespace(img, pad_px)
            img.save(str(png_path), optimize=True)
            print(
                f"[Rasterize] {png_name} ({reason}): {before[0]}x{before[1]} -> "
                f"{img.width}x{img.height} (aspect {img.width / img.height:.2f})"
            )
        with Image.open(png_path) as final:
            aspect = final.width / final.height
        manifest[png_name] = {
            "svg_sha256": source_svg_hash,
            "png_sha256": _sha256(png_path),
        }
        vb_w, med_size = _svg_text_metrics(svg_path)
        mapping[svg_path.name] = {
            "rel": f"figures_png/{png_name}",
            "aspect": aspect,
            "viewbox_w": vb_w,
            "median_text": med_size,
        }
    for ch_png in sorted(FINAL_REPORT_DIR.glob("ch*/figures/*.png")):
        if ch_png.with_suffix(".svg").exists():
            continue
        png_path = PNG_DIR / ch_png.name
        if not png_path.exists() or png_path.stat().st_mtime < ch_png.stat().st_mtime:
            with Image.open(ch_png) as src_im:
                rgb_im = src_im.convert("RGB")
                trimmed = trim_whitespace(rgb_im, pad_px)
                trimmed.save(str(png_path), optimize=True)
        with Image.open(png_path) as final:
            aspect = final.width / final.height
            fw = float(final.width)
        mapping[ch_png.name] = {
            "rel": f"figures_png/{ch_png.name}",
            "aspect": aspect,
            "viewbox_w": fw,
            "median_text": max(18.0, fw * 0.016),
        }

    for ui_png in sorted((ROOT / "reports" / "ui-design" / "assets").glob("*.png")):
        png_path = PNG_DIR / ui_png.name
        if not png_path.exists() or png_path.stat().st_mtime < ui_png.stat().st_mtime:
            with Image.open(ui_png) as src_im:
                rgb_im = src_im.convert("RGB")
                trimmed = trim_whitespace(rgb_im, pad_px)
                trimmed.save(str(png_path), optimize=True)
        with Image.open(png_path) as final:
            aspect = final.width / final.height
            fw = float(final.width)
        mapping[ui_png.name] = {
            "rel": f"figures_png/{ui_png.name}",
            "aspect": aspect,
            "viewbox_w": fw,
            "median_text": max(18.0, fw * 0.016),
        }

    _save_manifest(manifest)
    print(f"[Rasterize] Prepared {len(mapping)} high-DPI PNG figures in {PNG_DIR}")
    return mapping


def _printed_pt(median_text: float, viewbox_w: float, placed_mm: float) -> float:
    """Effective printed point size of the median label when the figure is placed at placed_mm wide."""
    if median_text <= 0 or viewbox_w <= 0:
        return 0.0
    return median_text * (placed_mm / viewbox_w) * 72 / 25.4


UNICODE_LATEX_MAP = {
    "★": r"$\star$",
    "☆": r"$\circ$",
    "✔": r"$\checkmark$",
    "✅": r"[PASS]",
    "❌": r"[FAIL]",
    "✘": r"$\times$",
    "⚠️": r"[WARN]",
    "⚠": r"[WARN]",
    "⏳": r"[WIP]",
    "⬜": r"[TODO]",
    "☀️": r"[Light]",
    "🌙": r"[Dark]",
    "→": r"$\rightarrow$",
    "←": r"$\leftarrow$",
    "↔": r"$\leftrightarrow$",
    "⇒": r"$\Rightarrow$",
    "≥": r"$\ge$",
    "≤": r"$\le$",
    "≠": r"$\neq$",
    "±": r"$\pm$",
    "×": r"$\times$",
    "÷": r"$\div$",
    "≈": r"$\approx$",
    "∈": r"$\in$",
    "∉": r"$\notin$",
    "⊂": r"$\subset$",
    "⊆": r"$\subseteq$",
    "∪": r"$\cup$",
    "∩": r"$\cap$",
    "∞": r"$\infty$",
    "Δ": r"$\Delta$",
    "α": r"$\alpha$",
    "β": r"$\beta$",
    "γ": r"$\gamma$",
    "δ": r"$\delta$",
    "ε": r"$\varepsilon$",
    "θ": r"$\theta$",
    "λ": r"$\lambda$",
    "μ": r"$\mu$",
    "π": r"$\pi$",
    "σ": r"$\sigma$",
    "τ": r"$\tau$",
    "ω": r"$\omega$",
    "—": "---",
    "–": "--",
    "“": "``",
    "”": "''",
    "‘": "`",
    "’": "'",
    "…": r"\ldots{}",
    "\u00a0": " ",
}


def escape_latex_text(text: str) -> str:
    """Escape plain text for LaTeX while preserving unicode CJK."""
    out = []
    for ch in text:
        if ch in UNICODE_LATEX_MAP:
            out.append(UNICODE_LATEX_MAP[ch])
        elif ch == "\\":
            out.append(r"\textbackslash{}")
        elif ch == "&":
            out.append(r"\&")
        elif ch == "%":
            out.append(r"\%")
        elif ch == "$":
            out.append(r"\$")
        elif ch == "#":
            out.append(r"\#")
        elif ch == "_":
            out.append(r"\_")
        elif ch == "{":
            out.append(r"\{")
        elif ch == "}":
            out.append(r"\}")
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        else:
            out.append(ch)
    return "".join(out)


def sanitize_math(math_str: str) -> str:
    """Clean unicode symbols inside $...$ math expressions."""
    rep = {
        "×": r"\times ",
        "→": r"\rightarrow ",
        "←": r"\leftarrow ",
        "↔": r"\leftrightarrow ",
        "≥": r"\ge ",
        "≤": r"\le ",
        "≠": r"\neq ",
        "±": r"\pm ",
        "≈": r"\approx ",
        "∈": r"\in ",
        "Δ": r"\Delta ",
        "α": r"\alpha ",
        "β": r"\beta ",
        "σ": r"\sigma ",
        "−": "-",
    }
    for k, v in rep.items():
        math_str = math_str.replace(k, v)
    return math_str


TOKEN_RE = re.compile(
    r"(`[^`]+`)"                                  # group 1: inline code
    r"|(\$\$[^$]+\$\$|\$[^$\n]+\$)"               # group 2: inline/display math
    r"|(!\[[^\]]*\]\([^)]+\))"                    # group 3: image
    r"|(\[[^\]]+\]\([^)]+\))"                     # group 4: link
)


def format_inline_markdown(text: str, breakable_code: bool = False) -> str:
    """Convert inline markdown (**bold**, *italic*, `code`, $math$, [link](url)) to LaTeX."""
    placeholders: list[str] = []

    def token_repl(m: re.Match) -> str:
        idx = len(placeholders)
        if m.group(1):  # `code`
            inner = m.group(1)[1:-1]
            code_tex = escape_latex_text(inner)
            if breakable_code:
                # Long identifiers such as ``test_adversarial_backend.py`` contain no
                # spaces, so TeX cannot justify them inside a narrow tabularx column and
                # the text spills into the neighbouring column.  Allow a line break after
                # every escaped underscore and dot, which are the only natural split
                # points in file names and dot-separated symbol paths.
                code_tex = code_tex.replace(r"\_", r"\_\allowbreak{}").replace(".", ".\\allowbreak{}")
                code_tex = code_tex.replace(r"\\allowbreak{}", r"\allowbreak{}")
                # PascalCase/CamelCase identifiers (e.g. ReportSummaryResponse) contain no
                # underscore or dot, so the two rules above cannot break them inside a
                # narrow column; allow a break at each lower-to-upper case boundary.
                code_tex = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", r"\\allowbreak{}", code_tex)
            placeholders.append(r"\texttt{" + code_tex + "}")
        elif m.group(2):  # $math$
            raw_m = m.group(2)
            placeholders.append(sanitize_math(raw_m))
        elif m.group(3):  # image inline fallback
            placeholders.append("")
        elif m.group(4):  # [label](url)
            lm = re.match(r"\[([^\]]+)\]\(([^)]+)\)", m.group(4))
            label = lm.group(1) if lm else m.group(4)
            placeholders.append(format_inline_markdown(label))
        return f"@@PH{idx}@@"

    staged = TOKEN_RE.sub(token_repl, text)

    # Escape the remaining non-placeholder text, but first mark bold and italic
    # Use temporary markers for **bold** and *italic*
    bold_Store: list[str] = []

    def bold_repl(m: re.Match) -> str:
        b_idx = len(bold_Store)
        bold_Store.append(m.group(1))
        return f"@@BM{b_idx}@@"

    # Allow single-asterisk italic runs nested inside a bold span, e.g.
    # **Chapter 2 (*Functional and Non-Functional Requirements*)** — the old
    # `[^*]+` class refused to match and left the ** markers as literal text.
    staged = re.sub(r"\*\*(.+?)\*\*", bold_repl, staged)

    italic_Store: list[str] = []

    def italic_repl(m: re.Match) -> str:
        i_idx = len(italic_Store)
        italic_Store.append(m.group(1))
        return f"@@IM{i_idx}@@"

    staged = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", italic_repl, staged)

    escaped = escape_latex_text(staged)

    # Restore italic
    for i_idx, content in enumerate(italic_Store):
        escaped = escaped.replace(f"@@IM{i_idx}@@", r"\textit{" + escape_latex_text(content) + "}")

    # Restore bold (which may contain italic or placeholders). Recurse so that a
    # nested *italic* span becomes \textit{} instead of literal asterisks.
    for b_idx, content in enumerate(bold_Store):
        inner_esc = format_inline_markdown(content)
        escaped = escaped.replace(f"@@BM{b_idx}@@", r"\textbf{" + inner_esc + "}")

    # Restore placeholders (which might be inside bold/italic or top-level)
    for idx, ph_val in enumerate(placeholders):
        escaped = escaped.replace(f"@@PH{idx}@@", ph_val)

    return escaped


def format_table_cell(cell: str) -> str:
    """Format one GFM table cell, honouring inline <br> as an intra-cell line break."""
    parts = [p.strip() for p in re.split(r"<br\s*/?>", cell, flags=re.IGNORECASE)]
    rendered: list[str] = []
    for part in parts:
        if not part:
            continue
        # A "<br>- item" continuation is really a sub-bullet inside the cell.
        part = re.sub(r"^[-*]\s+", "\u2022 ", part)
        rendered.append(format_inline_markdown(part, breakable_code=True))
    return r" \newline ".join(rendered)


def render_table(table_lines: list[str]) -> str:
    """Convert a GFM pipe table into a LaTeX tabularx environment that fits within \\textwidth."""
    rows: list[list[str]] = []
    for line in table_lines:
        s = line.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        cells = [c.strip() for c in s.split("|")]
        # Skip the GFM delimiter row. Accept one or more dashes (the repo's
        # Appendix A table uses `:-:`, a single dash, which a `-{2,}` pattern
        # silently promoted into a visible data row) and both hyphen styles.
        if all(
            re.match(r"^:?[-–—]+:?$", c.replace(" ", ""))
            for c in cells
            if c != ""
        ):
            continue
        rows.append(cells)

    if not rows:
        return ""

    num_cols = max(len(r) for r in rows)
    if num_cols <= 0:
        return ""

    # Normalize row lengths
    norm_rows = []
    for r in rows:
        if len(r) < num_cols:
            r = r + [""] * (num_cols - len(r))
        elif len(r) > num_cols:
            r = r[:num_cols]
        norm_rows.append(r)

    # Compute column weight heuristic based on 75th-percentile cell text length
    col_lengths = []
    for c_idx in range(num_cols):
        lengths = sorted(len(r[c_idx]) for r in norm_rows)
        p75 = lengths[min(len(lengths) - 1, int(len(lengths) * 0.75))]
        col_lengths.append(max(4, p75))

    # Build column spec using X columns with relative hsize
    weights = [max(0.45, min(2.2, l ** 0.55)) for l in col_lengths]
    total_w = sum(weights)
    norm_weights = [w * num_cols / total_w for w in weights]

    col_specs = [
        f">{{\\hsize={nw:.2f}\\hsize\\raggedright\\arraybackslash}}X"
        for nw in norm_weights
    ]
    col_spec_str = " ".join(col_specs)

    font_cmd = r"\scriptsize" if num_cols <= 4 else r"\scriptsize"

    out = [
        r"\begin{center}",
        font_cmd,
        r"\setlength{\tabcolsep}{3.5pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        f"\\begin{{tabularx}}{{\\textwidth}}{{{col_spec_str}}}",
        r"\toprule",
    ]

    header = norm_rows[0]
    header_cells = [r"\textbf{" + format_table_cell(c) + "}" for c in header]
    out.append(" & ".join(header_cells) + r" \\")
    out.append(r"\midrule")

    for r in norm_rows[1:]:
        row_cells = [format_table_cell(c) for c in r]
        out.append(" & ".join(row_cells) + r" \\")

    out.extend([
        r"\bottomrule",
        r"\end{tabularx}",
        r"\end{center}",
        r"\vspace{4pt}",
    ])
    return "\n".join(out)


def markdown_to_latex_body(md_text: str, png_map: dict[str, dict], skip_front_matter: bool = True) -> str:
    """Convert assembled Markdown into clean LaTeX body chapters."""
    if skip_front_matter:
        idx = md_text.find("# 1 Introduction")
        if idx != -1:
            md_text = md_text[idx:]

    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)

    in_itemize = False
    in_enumerate = False

    def close_lists() -> None:
        nonlocal in_itemize, in_enumerate
        if in_itemize:
            out.append(r"\end{itemize}")
            in_itemize = False
        if in_enumerate:
            out.append(r"\end{enumerate}")
            in_enumerate = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Fenced code block
        if stripped.startswith("```"):
            close_lists()
            i += 1
            code_lines = []
            while i < n and not lines[i].strip().startswith("```"):
                # Replace unicode box-drawing characters inside verbatim blocks so Latin Modern Mono renders cleanly
                cl = (
                    lines[i]
                    .replace("├──", "|--")
                    .replace("└──", "`--")
                    .replace("│", "|")
                    .replace("─", "-")
                    .replace("★", "*")
                    .replace("☆", "o")
                    .replace("✔", "[OK]")
                    .replace("✘", "[X]")
                    .replace("→", "->")
                    .replace("↔", "<->")
                )
                code_lines.append(cl)
                i += 1
            i += 1  # skip closing ```
            out.append(r"\begin{Verbatim}[fontsize=\scriptsize,frame=single,framesep=4pt,rulecolor=\color{gray!50}]")
            out.extend(code_lines)
            out.append(r"\end{Verbatim}")
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$", stripped):
            close_lists()
            i += 1
            continue

        # Table block
        if stripped.startswith("|") and "|" in stripped[1:]:
            close_lists()
            table_lines = []
            while i < n and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines))
            continue

        # Image line: ![alt](path)
        img_m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
        if img_m:
            close_lists()
            raw_path = img_m.group(2)
            svg_name = Path(raw_path).name
            fig = png_map.get(svg_name)
            if fig:
                png_rel = fig["rel"]
                aspect = fig["aspect"]
                # Predict the printed size of the median label under both page
                # orientations and keep the better one. Portrait is preferred
                # whenever it already clears MIN_PRINTED_PT, so the deck does not
                # fill up with rotated pages for no reason.
                portrait_w_mm = 172.5 if aspect >= 2.0 else 165.4
                landscape_w_mm = min(255.0, 172.0 * aspect)
                portrait_pt = _printed_pt(fig["median_text"], fig["viewbox_w"], portrait_w_mm)
                landscape_pt = _printed_pt(fig["median_text"], fig["viewbox_w"], landscape_w_mm)

                if portrait_pt < MIN_PRINTED_PT and landscape_pt > portrait_pt:
                    out.append(r"\begin{landscape}")
                    out.append(r"\begin{center}")
                    out.append(r"\vspace*{\fill}")
                    out.append(
                        f"\\includegraphics[width=255mm,height=172mm,keepaspectratio]{{{png_rel}}}"
                    )
                    out.append(r"\vspace*{\fill}")
                    out.append(r"\end{center}")
                    out.append(r"\end{landscape}")
                    print(
                        f"[Layout] {svg_name}: LANDSCAPE "
                        f"(portrait {portrait_pt:.2f} pt -> landscape {landscape_pt:.2f} pt)"
                    )
                else:
                    if aspect >= 3.0:
                        spec = r"width=0.98\textwidth"
                    elif aspect >= 2.0:
                        spec = r"width=0.98\textwidth,height=0.42\textheight"
                    elif aspect >= 1.45:
                        spec = r"width=0.98\textwidth,height=0.52\textheight"
                    elif aspect >= 1.05:
                        spec = r"width=0.94\textwidth,height=0.62\textheight"
                    else:
                        # Near-square: let it use the full measure and most of the
                        # remaining page height. A landscape page is never larger
                        # here, because 172 mm x aspect < 172.5 mm.
                        spec = r"width=0.98\textwidth,height=0.72\textheight"
                    out.append(r"\begin{center}")
                    out.append(r"\vspace{4pt}")
                    out.append(
                        f"\\includegraphics[{spec},keepaspectratio]{{{png_rel}}}"
                    )
                    out.append(r"\vspace{4pt}")
                    out.append(r"\end{center}")
                    if portrait_pt < MIN_PRINTED_PT:
                        print(
                            f"[Layout] {svg_name}: portrait {spec} "
                            f"(median {portrait_pt:.2f} pt) [NOTE] below {MIN_PRINTED_PT} pt "
                            f"— figure is content-dense; needs splitting to gain more size"
                        )
                    else:
                        print(
                            f"[Layout] {svg_name}: portrait {spec} "
                            f"(median {portrait_pt:.2f} pt)"
                        )
            i += 1
            continue

        # Headings
        h_m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if h_m:
            close_lists()
            level = len(h_m.group(1))
            title_raw = h_m.group(2).strip()
            # Strip Leading Section numbers like "1 Introduction" or "1.1 Problem" so LaTeX doesn't double-number,
            # OR use unnumbered / custom sectioning. Wait: keeping the exact markdown section numbers (`1.1`, `5.3.2`, `Appendix A`)
            # with \section*{...} + \addcontentsline OR stripping numbers and letting LaTeX number?
            # Wait: our text has "# 1 Introduction...", "## 1.1 ...", "# References", "# Appendix A: ...".
            # If we strip leading "1 ", "1.1 ", "1.1.1 " when present, LaTeX's \section, \subsection, \subsubsection will number them automatically and build TOC!
            # Headings
            if level == 1:
                if title_raw.startswith("Appendix "):
                    if title_raw.startswith("Appendix A"):
                        out.append(r"\clearpage")
                    else:
                        out.append(r"\vspace{8pt}")
                    sec_title = format_inline_markdown(title_raw)
                    out.append(f"\\section*{{{sec_title}}}")
                    out.append(f"\\addcontentsline{{toc}}{{section}}{{{sec_title}}}")
                elif title_raw.startswith("References"):
                    out.append(r"\vspace{8pt}")
                    sec_title = format_inline_markdown(title_raw)
                    out.append(f"\\section*{{{sec_title}}}")
                    out.append(f"\\addcontentsline{{toc}}{{section}}{{{sec_title}}}")
                else:
                    clean_t = re.sub(r"^\d+\s+", "", title_raw)
                    if title_raw.startswith("1 "):
                        pass
                    else:
                        out.append(r"\vspace{10pt}")
                    out.append(f"\\section{{{format_inline_markdown(clean_t)}}}")
            elif level == 2:
                if re.match(r"^[A-D]\.\d+\s+", title_raw):
                    # Appendix subsection like D.1
                    sec_title = format_inline_markdown(title_raw)
                    out.append(f"\\subsection*{{{sec_title}}}")
                    out.append(f"\\addcontentsline{{toc}}{{subsection}}{{{sec_title}}}")
                else:
                    clean_t = re.sub(r"^\d+\.\d+\s+", "", title_raw)
                    out.append(f"\\subsection{{{format_inline_markdown(clean_t)}}}")
            elif level == 3:
                if re.match(r"^[A-D]\.\d+\s+", title_raw):
                    sec_title = format_inline_markdown(title_raw)
                    out.append(f"\\subsection*{{{sec_title}}}")
                    out.append(f"\\addcontentsline{{toc}}{{subsection}}{{{sec_title}}}")
                else:
                    clean_t = re.sub(r"^\d+\.\d+\.\d+\s+", "", title_raw)
                    out.append(f"\\subsubsection{{{format_inline_markdown(clean_t)}}}")
            else:
                clean_t = re.sub(r"^\d+(?:\.\d+)*\s+", "", title_raw)
                out.append(f"\\paragraph{{{format_inline_markdown(clean_t)}}}")
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            close_lists()
            bq_lines = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(r"\begin{quote}\itshape")
            out.append(format_inline_markdown(" ".join(bq_lines)))
            out.append(r"\end{quote}")
            continue

        # Unordered list item
        ul_m = re.match(r"^[-*]\s+(.*)$", stripped)
        if ul_m:
            if in_enumerate:
                out.append(r"\end{enumerate}")
                in_enumerate = False
            if not in_itemize:
                out.append(r"\begin{itemize}[leftmargin=1.6em,itemsep=2pt,topsep=3pt]")
                in_itemize = True
            out.append(r"\item " + format_inline_markdown(ul_m.group(1)))
            i += 1
            continue

        # Ordered list item
        ol_m = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ol_m:
            if in_itemize:
                out.append(r"\end{itemize}")
                in_itemize = False
            if not in_enumerate:
                out.append(r"\begin{enumerate}[leftmargin=1.8em,itemsep=2pt,topsep=3pt]")
                in_enumerate = True
            out.append(r"\item " + format_inline_markdown(ol_m.group(1)))
            i += 1
            continue

        # Blank line
        if not stripped:
            close_lists()
            out.append("")
            i += 1
            continue

        # Normal paragraph line: accumulate the whole soft-wrapped paragraph so
        # inline markup that spans a source line break (**147 passed in\n1.79 s**)
        # is still matched as one span.
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt.startswith(("#", "```", ">", "|", "!["))
                or re.match(r"^[-*]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
                or re.match(r"^-{3,}$", nxt)
            ):
                break
            para_lines.append(nxt)
            i += 1
        out.append(format_inline_markdown(" ".join(para_lines)))

    close_lists()
    return "\n".join(out)


LATEX_PREAMBLE_REPORT = r"""\documentclass[10pt,a4paper]{article}
\usepackage[a4paper,top=18mm,bottom=18mm,left=17mm,right=17mm,headheight=14pt]{geometry}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Consolas}[Scale=0.88]

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{enumitem}
\usepackage{fancyvrb}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{pdflscape}
\usepackage[unicode,colorlinks=true,linkcolor=blue!60!black,urlcolor=blue!60!black,citecolor=blue!60!black]{hyperref}
\usepackage{caption}

\definecolor{navy}{HTML}{0F172A}
\definecolor{accent}{HTML}{1E40AF}

\captionsetup{font=footnotesize,labelfont=bf,skip=3pt}
\setlength{\parskip}{3pt}
\setlength{\parindent}{0pt}
\sloppy
\emergencystretch=3em

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\textcolor{gray}{JC2001 Software Engineering · Group 5 Technical Report}}
\fancyhead[R]{\footnotesize\textcolor{gray}{StudyGraph: Graph-Augmented Misconception Diagnosis}}
\fancyfoot[C]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\titleformat{\section}{\Large\bfseries\color{navy}}{\thesection}{0.6em}{}[\vspace{2pt}\titlerule]
\titleformat{\subsection}{\large\bfseries\color{accent}}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{navy}}{\thesubsubsection}{0.5em}{}

\begin{document}

% ==================== TITLE PAGE ====================
\begin{titlepage}
\centering
\vspace*{1.2cm}
{\scshape\Large Aberdeen Institute of Data Science and Artificial Intelligence\\
South China Normal University \& University of Aberdeen\par}
\vspace{0.8cm}
{\large\bfseries JC2001: Software Engineering (Cycle 3 Final Submission)\par}
\vspace{1.2cm}
\rule{\textwidth}{1.5pt}\\[0.4cm]
{\Huge\bfseries\color{navy} StudyGraph (SmartStudy Compass)\par}
\vspace{0.3cm}
{\Large\bfseries A Knowledge-Graph-Augmented Option-Level Misconception\\
Diagnostic and Adaptive Revision System\par}
\vspace{0.3cm}
\rule{\textwidth}{1.5pt}\\[1.0cm]

{\large\bfseries Group 5 --- Author \& Chapter Attribution Roster\par}
\vspace{0.4cm}
\footnotesize
\renewcommand{\arraystretch}{1.28}
\begin{tabularx}{0.96\textwidth}{>{\hsize=0.9\hsize}X >{\hsize=0.65\hsize}X >{\hsize=0.95\hsize}X >{\hsize=1.5\hsize}X}
\toprule
\textbf{Member Name} & \textbf{UofA ID} & \textbf{Project Role} & \textbf{Primary Report Ownership} \\
\midrule
Wu Yuxuan & 50106070 & PM \& Team Lead & Front Matter, Ch 7, Appendix A \\
Lin Yongtong & 50106038 & Lead Business Analyst & Chapter 1 (Introduction \& Context) \\
Zhang Zijian & 50106035 & Business Analyst & Chapter 2 (FRs R01--R14 \& NFRs) \\
Xie Weixin & 50106034 & QA \& Report Lead & Chapter 3 (Use Cases \& State Machine) \\
Wang Sijian & 50106045 & Software Architect & Chapter 4 (4+1 Views \& ADRs) \\
Jiang Hao & 50106065 & PoC Lead Developer & Chapter 5.1--5.2 \& Appendix D \\
Dong Siqin & 50106060 & PoC Logic \& Data Lead & Chapter 5.3--5.4 (Traps \& GraphRAG) \\
Xi Yusai & 50105989 & UI/UX Lead & Chapter 5.5 (Zero-Build SPA \& Drawer) \\
Liang Zixuan & 50106037 & Deployment \& Media Lead & Chapter 5.6 (Deployment \& Packaging) \\
Yang Mingjie & 50106061 & Testing \& Evaluation Lead & Chapter 6 \& Appendix C (147 Tests \& MMLU) \\
Luo Wenxi & 50106012 & QA \& Data Curation Co-Lead & Ch 6.2--6.3 Co-Author \& Appendix C/D Audit \\
\bottomrule
\end{tabularx}

\vfill
{\normalsize
\textbf{Baseline Verification:} \texttt{147 passed in 0.72s} (\texttt{pytest}) $\cdot$ \textbf{MMLU Benchmark:} $n = 4,445$ items across 12 subjects\\
\textbf{Submission Date:} October 2026
\par}
\end{titlepage}

% ==================== EXECUTIVE ABSTRACT & TOC ====================
\pagenumbering{roman}
\section*{Declaration of Originality and Executive Abstract}
\addcontentsline{toc}{section}{Declaration of Originality and Executive Abstract}

\textbf{Declaration of Academic Integrity:} We, the eleven members of Group 5, declare that this technical report and the accompanying \texttt{StudyGraph} proof-of-concept software archive are our own original engineering work completed for JC2001 Software Engineering. Every student's individual section contribution is explicitly recorded in the Title Page roster and Appendix A.

\vspace{6pt}
\textbf{Executive Abstract:} Undergraduate students preparing for high-stakes examinations in law, computer systems, econometrics, and software engineering frequently rely on practice question banks and general-purpose Large Language Models (LLMs). However, traditional Computer-Based Testing (CBT) platforms suffer from the \textbf{Binary Feedback Trap}—reporting only whether an answer is right or wrong alongside a generic explanation of the correct key—while unconstrained LLM chatbots exhibit \textbf{Answer Spoiling} (revealing the solution before cognitive reflection) and \textbf{Factual Hallucination} on statutory and quantitative boundaries.

To address these dual limitations, Group 5 engineered \textbf{StudyGraph (\textit{SmartStudy Compass})}, a single-process, offline-capable web application that transforms multiple-choice distractors into \textbf{deterministic option-level cognitive trap diagnoses}. At the architectural level, StudyGraph decouples an \textbf{offline 12-stage GraphRAG research and MMLU evaluation pipeline} from a \textbf{zero-dependency FastAPI + vanilla ES6+ runtime}. When a student selects a distractor option ($A, B, C,$ or $D$), the runtime resolves the exact misconception via an $O(1)$ hash lookup against pre-audited \texttt{TrapDetail} schemas in $< 5\text{ ms}$ (\textbf{measured P95 $= 3.4\text{ ms}$}), rendering a five-layer progressive \textbf{Trap Drawer} (named cognitive fallacy, conceptual conflict analysis, missing prerequisite badge, interactive 1-hop knowledge-graph neighbourhood, and Socratic reflection prompt) and updating a \textbf{5-axis competency radar}.

Our verification and empirical evaluation establish two rigorous findings: (1) Across \textbf{9 automated \texttt{pytest} modules (80 test functions expanded via parameterisation into 147 test cases)}, StudyGraph achieves a \textbf{100\% pass rate (\texttt{147 passed, 0 failed})} covering domain invariants, dual-case \texttt{CamelModel} serialisation, and 25 adversarial SQLi/XSS/type-confusion attack groups; and (2) Across a \textbf{4,445-item MMLU benchmark spanning 12 academic subjects}, 1-hop Neo4j knowledge-graph augmentation yields significant gains in relational and rule-dense disciplines (\textbf{Professional Law $+2.50\text{ pp}$}, \textbf{Management $+2.00\text{ pp}$}, \textbf{Macroeconomics $+1.50\text{ pp}$}) while revealing a documented \textbf{Retrieval Noise Ceiling} in calculation-heavy and open-domain trivia subjects (\textbf{overall macro-accuracy $81.98\%$ vs.\ $82.43\%$ baseline, $\Delta = -0.45\text{ pp}$}). This empirical boundary directly justifies our hybrid architectural separation (\texttt{AD-1}).

\clearpage
\tableofcontents
\clearpage
\pagenumbering{arabic}
"""


LATEX_PREAMBLE_BRIEFING = r"""\documentclass[10.5pt,a4paper]{article}
\usepackage[a4paper,top=20mm,bottom=20mm,left=18mm,right=18mm,headheight=14pt]{geometry}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Consolas}[Scale=0.88]

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{enumitem}
\usepackage{fancyvrb}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage[unicode,colorlinks=true,linkcolor=blue!60!black,urlcolor=blue!60!black]{hyperref}

\definecolor{navy}{HTML}{0F172A}
\definecolor{accent}{HTML}{1E40AF}

\setlength{\parskip}{5pt}
\setlength{\parindent}{0pt}
\sloppy
\emergencystretch=3em

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\textcolor{gray}{JC2001 Group 5 · Afternoon Supervisor Briefing and Open Questions}}
\fancyhead[R]{\footnotesize\textcolor{gray}{SmartStudy Compass (StudyGraph) · 2026-10-29}}
\fancyfoot[C]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\titleformat{\section}{\Large\bfseries\color{navy}}{\thesection}{0.6em}{}[\vspace{2pt}\titlerule]
\titleformat{\subsection}{\large\bfseries\color{accent}}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{navy}}{\thesubsubsection}{0.5em}{}

\begin{document}
"""


def compile_xelatex(tex_path: Path, work_dir: Path, runs: int = 2) -> Path:
    """Run xelatex in non-stop mode and return the generated PDF path."""
    for run_idx in range(1, runs + 1):
        cmd = [
            XELATEX_BIN,
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_path.name,
        ]
        res = subprocess.run(
            cmd,
            cwd=str(work_dir),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        pdf_out = work_dir / (tex_path.stem + ".pdf")
        if res.returncode != 0 and not pdf_out.exists():
            print(f"[XeLaTeX Error on run {run_idx}] Return code {res.returncode}")
            tail = "\n".join(res.stdout.splitlines()[-40:])
            print(tail)
            raise RuntimeError(f"XeLaTeX failed on {tex_path.name}")
        print(f"[XeLaTeX] Pass {run_idx}/{runs} for {tex_path.name} -> exit={res.returncode}")
    return work_dir / (tex_path.stem + ".pdf")


def main() -> None:
    png_map = rasterize_svgs()

    # 1. Build Master English Technical Report
    md_report_text = MD_REPORT.read_text(encoding="utf-8")
    body_report = markdown_to_latex_body(md_report_text, png_map, skip_front_matter=True)
    full_tex_report = LATEX_PREAMBLE_REPORT + "\n" + body_report + "\n\\end{document}\n"
    TEX_REPORT.write_text(full_tex_report, encoding="utf-8")
    print(f"[TeX] Wrote {TEX_REPORT} ({len(full_tex_report):,} chars)")

    pdf_path = compile_xelatex(TEX_REPORT, FINAL_REPORT_DIR, runs=2)
    shutil.copy2(pdf_path, PDF_REPORT_ROOT_COPY)
    doc = fitz.open(str(pdf_path))
    print(f"[PDF Report] {pdf_path} -> {len(doc)} pages, {pdf_path.stat().st_size:,} bytes")
    doc.close()

    # 2. Build Afternoon Supervisor Questions PDF
    if MD_BRIEFING.exists():
        md_briefing_text = MD_BRIEFING.read_text(encoding="utf-8")
        body_briefing = markdown_to_latex_body(md_briefing_text, png_map, skip_front_matter=False)
        full_tex_briefing = LATEX_PREAMBLE_BRIEFING + "\n" + body_briefing + "\n\\end{document}\n"
        TEX_BRIEFING.write_text(full_tex_briefing, encoding="utf-8")
        b_pdf = compile_xelatex(TEX_BRIEFING, ROOT / "reports", runs=2)
        b_doc = fitz.open(str(b_pdf))
        print(f"[PDF Briefing] {b_pdf} -> {len(b_doc)} pages, {b_pdf.stat().st_size:,} bytes")
        b_doc.close()


if __name__ == "__main__":
    main()
