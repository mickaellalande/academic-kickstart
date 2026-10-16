#!/usr/bin/env python3
"""Make Google Slides and YouTube iframes responsive in a Hugo Academic website.

Dry run:  python3 update_responsive_embeds.py --repo .
Apply:    python3 update_responsive_embeds.py --repo . --apply

Run from the academic-kickstart repository. Changes to source Markdown and
assets/scss/custom.scss can then be committed using ./update.sh "message".
No third-party embeds with dynamically determined heights are modified.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

IFRAME_RE = re.compile(r"<iframe\b[^>]*>", re.IGNORECASE | re.DOTALL)
SRC_RE = re.compile(r"\bsrc\s*=\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
WIDTH_RE = re.compile(r"\bwidth\s*=\s*(['\"])(\d+)(?:px)?\1", re.IGNORECASE)
HEIGHT_RE = re.compile(r"\bheight\s*=\s*(['\"])(\d+)(?:px)?\1", re.IGNORECASE)
CLASS_RE = re.compile(r"\bclass\s*=\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
STYLE_RE = re.compile(r"\bstyle\s*=\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
CSS_MARKER = "/* Responsive Google Slides and YouTube embeds (site-specific) */"
CSS = """
/* Responsive Google Slides and YouTube embeds (site-specific) */
.article-style iframe.responsive-embed {
  display: block;
  width: 100%;
  max-width: var(--embed-max-width, 960px);
  height: auto;
  aspect-ratio: var(--embed-ratio, 16 / 9);
  margin: 1.5rem auto;
  border: 0;
}
"""


def embed_type(url: str) -> str | None:
    url = url.lower()
    if "docs.google.com/presentation/" in url:
        return "Google Slides"
    if "youtube.com/embed/" in url or "youtube-nocookie.com/embed/" in url:
        return "YouTube"
    return None


def add_class(tag: str, classname: str) -> str:
    match = CLASS_RE.search(tag)
    if match:
        current = match.group(2)
        classes = current.split()
        if classname not in classes:
            new = current.strip() + " " + classname
            return tag[:match.start(2)] + new.strip() + tag[match.end(2):]
        return tag
    return tag[:-1] + f' class="{classname}">'


def add_style(tag: str, style: str) -> str:
    match = STYLE_RE.search(tag)
    if match:
        orig = match.group(2).strip()
        if orig and not orig.endswith(";"):
            orig += ";"
        return tag[:match.start(2)] + (orig + " " + style).strip() + tag[match.end(2):]
    return tag[:-1] + f' style="{style}">'


def make_responsive(tag: str, counts: Counter, warnings: list[str], filepath: str) -> str:
    source = SRC_RE.search(tag)
    if not source:
        return tag
    kind = embed_type(source.group(2))
    if not kind:
        return tag
    if "responsive-embed" in tag:
        counts["already responsive"] += 1
        return tag

    width = WIDTH_RE.search(tag)
    height = HEIGHT_RE.search(tag)
    if not width or not height:
        warnings.append(f"{filepath}: {kind} iframe missing pixel width/height; skipped")
        return tag
    w, h = int(width.group(2)), int(height.group(2))
    if w <= 0 or h <= 0:
        warnings.append(f"{filepath}: invalid size {w}x{h}; skipped")
        return tag

    # Keep the current desktop size for ordinary slides and YouTube videos.
    # Portrait posters would otherwise become excessively tall on desktop.
    if h > w:
        max_width = min(w, 680)
    elif w > 1400:  # Large horizontal poster
        max_width = 1000
    else:
        max_width = min(w, 960)

    updated = add_class(tag, "responsive-embed")
    updated = add_style(updated, f"--embed-ratio: {w} / {h}; --embed-max-width: {max_width}px;")
    counts[kind] += 1
    if h > w:
        counts["portrait posters"] += 1
    elif w > 1400:
        counts["wide posters"] += 1
    return updated


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Path to the Hugo source repository (default: current working directory)")
    parser.add_argument("--apply", action="store_true", help="Write changes; default is dry-run")
    args = parser.parse_args()
    root = args.repo.expanduser().resolve()
    content = root / "content"
    if not content.is_dir() or not (root / "config").exists():
        parser.error(f"{root} doesn't appear to be the academic-kickstart Hugo source repository")

    counts: Counter = Counter()
    warnings: list[str] = []
    touched: list[tuple[Path, str]] = []
    for path in sorted(content.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
            continue
        source = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        result = IFRAME_RE.sub(lambda m: make_responsive(m.group(0), counts, warnings, relative), source)
        if result != source:
            touched.append((path, result))

    cssfile = root / "assets" / "scss" / "custom.scss"
    css_source = cssfile.read_text(encoding="utf-8") if cssfile.exists() else ""
    add_css = CSS_MARKER not in css_source

    print("MODE:", "APPLY" if args.apply else "DRY RUN (nothing written)")
    print(f"Repository: {root}")
    print(f"New responsive embeds: {counts['Google Slides']} Google Slides, {counts['YouTube']} YouTube")
    print(f"Special formats: {counts['portrait posters']} portrait, {counts['wide posters']} wide")
    print(f"Previously adapted embeds: {counts['already responsive']}")
    print(f"Markdown files to change: {len(touched)}")
    for path, _ in touched:
        print("  -", path.relative_to(root).as_posix())
    print(f"CSS: {'add responsive rule' if add_css else 'responsive rule already installed'} ({cssfile.relative_to(root)})")
    for warning in warnings:
        print("WARNING:", warning)

    if args.apply:
        for path, new in touched:
            path.write_text(new, encoding="utf-8")
        if add_css:
            cssfile.parent.mkdir(parents=True, exist_ok=True)
            cssfile.write_text(css_source.rstrip() + "\n\n" + CSS.strip() + "\n", encoding="utf-8")
        print("Done. Review git diff and preview the website before running update.sh.")
    else:
        print("Review the plan and rerun with --apply to modify the source files.")


if __name__ == "__main__":
    main()
