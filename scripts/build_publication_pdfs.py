#!/usr/bin/env python3
"""Generate print PDFs from approved, already-public Astro blog Markdown.

Does not read private repositories or decide editorial approval.
Run before Astro builds so public/reports/*.pdf is copied into dist/reports.
"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import yaml
from markdown_it import MarkdownIt
from weasyprint import CSS, HTML

MD = MarkdownIt("commonmark", {"html": False}).enable("table").enable("strikethrough")

def parse_article(path: Path):
    source = path.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", source, flags=re.S)
    if not frontmatter:
        raise ValueError(f"Not a published Astro article: {path}")
    metadata = yaml.safe_load(frontmatter.group(1)) or {}
    body = source[frontmatter.end():]
    for required in ("layout", "title", "description", "pubDate", "author"):
        if not metadata.get(required):
            raise ValueError(f"Missing {required} in {path}")
    if metadata.get("draft") is True or metadata.get("publish") is False:
        raise ValueError(f"Draft/not-approved content must not be placed in public blog: {path}")
    return metadata, body

def build_html(meta: dict, body: str):
    safe = lambda value: html.escape(str(value), quote=True)
    title = safe(meta["title"])
    description = safe(meta["description"])
    category = safe(meta.get("category", "COMPANY RESEARCH"))
    author = safe(meta["author"]).upper()
    date = safe(meta["pubDate"])
    text = MD.render(body)
    # Links are real embedded annotations; WeasyPrint resolves them from base_url.
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title></head>
<body>
<section class="cover">
<div class="cover-content">
<div class="masthead">
<div class="brand">MEYO <span>/</span> INSIGHTS</div>
<div class="strapline">INDEPENDENT<br>INVESTMENT RESEARCH</div>
</div>
<div class="category">{category}</div>
<h1>{title}</h1>
<p class="deck">{description}</p>
<div class="accent-rule"></div>
<div class="status">RESEARCH &amp; EDUCATION · READ SOURCES AND LIMITATIONS</div>
</div>
<div class="monogram">MI</div>
<div class="cover-foot">
<div class="author">BY {author}</div>
<div class="date">{date}<br>Meyo Insights · Research journal</div>
</div>
</section>
<main class="report"><div class="kicker">MEYO INSIGHTS / RESEARCH REPORT</div>{text}</main>
</body></html>'''

def generate(src: Path, target: Path, css: Path):
    metadata, body = parse_article(src)
    target.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=build_html(metadata, body), base_url=src.resolve().parent.as_uri() + "/").write_pdf(
        str(target), stylesheets=[CSS(filename=str(css))])
    if target.stat().st_size < 3000:
        raise RuntimeError(f"PDF too small: {target}")
    # Check PDF structure and actual page count.
    from pypdf import PdfReader
    reader = PdfReader(str(target))
    if not reader.pages:
        raise RuntimeError(f"PDF has no pages: {target}")
    print(f"{target}: {len(reader.pages)} pages")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("."))
    args = parser.parse_args()
    site = args.site.resolve()
    css = site / "assets" / "editorial-print.css"
    source_dir = site / "src" / "pages" / "blog"
    out_dir = site / "public" / "reports"
    if not css.exists() or not source_dir.is_dir():
        raise RuntimeError("Missing site print stylesheet or blog directory")
    published = sorted(source_dir.glob("*.md"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Generated PDFs must reflect ONLY the current public articles. Do not carry
    # stale PDFs after a post is removed.
    for stale in out_dir.glob("*.pdf"):
        stale.unlink()
    for source in published:
        generate(source, out_dir / f"{source.stem}.pdf", css)
    print(f"Generated {len(published)} public research PDFs")

if __name__ == "__main__":
    main()
