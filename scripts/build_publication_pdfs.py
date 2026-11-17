#!/usr/bin/env python3
"""Meyo Insights — evidence-led editorial PDF publisher.

Renders only owner-approved, public Astro Markdown sources. Editorial metadata
controls artwork and evidence exhibits; the body and citations are unchanged.
"""
from __future__ import annotations

import argparse
from datetime import date
import html
from pathlib import Path
import re

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
    for field in ("layout", "title", "description", "pubDate", "author"):
        if not metadata.get(field):
            raise ValueError(f"Missing {field} in {path}")
    if metadata.get("draft") is True or metadata.get("publish") is False:
        raise ValueError(f"Draft/not-approved content must not be placed in public blog: {path}")
    return metadata, body


def safe(value):
    return html.escape(str(value), quote=True)


def assert_evidence(meta: dict, body: str):
    """Reject unlabeled/unsupported visual numbers instead of inventing evidence."""
    ed = meta.get("editorial") or {}
    if not ed:
        return
    if not isinstance(ed, dict):
        raise ValueError("editorial must be an object")
    for item in ed.get("takeaways", []):
        if not (item.get("title") and item.get("detail") and item.get("sources")):
            raise ValueError("Every editorial takeaway requires a title, detail and evidence IDs")
        for source_id in re.findall(r"\[(?:S|O)\d{2}\]", str(item["sources"])):
            if source_id not in body:
                raise ValueError(f"Unresolved takeaway citation: {source_id}")
    for exhibit in ed.get("exhibits", []):
        if not (exhibit.get("kind") and exhibit.get("title") and exhibit.get("source") and exhibit.get("caveat")):
            raise ValueError("Each exhibit requires kind, title, source and caveat")
        for cited in re.findall(r"\[(?:S|O)\d{2}\]", str(exhibit['source'])):
            if cited not in body:
                raise ValueError(f"Missing exhibit source {cited}")
        for row in exhibit.get("data", []):
            number = row.get("value")
            if not isinstance(number, (int, float)) or isinstance(number, bool):
                raise ValueError("Every chart value must be numeric")
            # Exact printed values must be traceable to the publication, preventing
            # visual figures silently drifting from the corresponding report table.
            formatted = f"{number:.2f}" if float(number) != int(number) else str(number)
            if formatted not in body and str(number) not in body:
                raise ValueError(f"Exhibit value {number} is absent from the research body")


def pipeline_art():
    """Original, self-contained vector illustration of the route model."""
    return '''<svg class="pipeline-art" viewBox="0 0 410 205" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Simplified fuel pipeline route from coastal source through pump and depot to market">
<path d="M25 152 H140 V112 H245 V70 H360" fill="none" stroke="#173d35" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M25 152 H140 V112 H245 V70 H360" fill="none" stroke="#d9df4a" stroke-width="3.4" stroke-dasharray="11 13" stroke-linecap="round"/>
<g fill="#f7f6f2" stroke="#173d35" stroke-width="5"><circle cx="25" cy="152" r="13"/><circle cx="140" cy="112" r="13"/><circle cx="245" cy="70" r="13"/><circle cx="360" cy="70" r="13"/></g>
<g fill="#173d35" font-size="12" font-family="Inter,DejaVu Sans,sans-serif" font-weight="700"><text x="5" y="190">SOURCE</text><text x="117" y="84">PUMP</text><text x="221" y="110">DEPOT</text><text x="328" y="42">MARKET</text></g></svg>'''


def cover(meta: dict):
    ed = meta.get("editorial") or {}
    title = safe(ed.get("displayTitle") or meta["title"])
    official = safe(meta["title"])
    deck = safe(ed.get("coverDeck") or meta["description"])
    issue = safe(meta.get("issue", "—"))
    ticker = safe(meta.get("ticker", ""))
    exchange = safe(meta.get("exchange", ""))
    issuer = safe(ed.get("issuer") or meta.get("issuer") or "COMPANY RESEARCH")
    author = safe(meta["author"]).upper()
    pub = meta["pubDate"]
    published = safe(pub.strftime("%d %b %Y").upper() if isinstance(pub, date) else str(pub))
    asof = safe(meta.get("researchAsOf", "Not specified"))
    market = safe(meta.get("marketReference", "Not specified"))
    return f'''<section class="publication-cover">
 <div class="cover-band"><div class="cover-brand">MEYO<br>INSIGHTS<span>.</span></div><p>THE RESEARCH JOURNAL<br>ISSUE {issue} / COMPANY RESEARCH</p></div>
 <div class="cover-issuer"><small>{issuer}</small><strong>{exchange}: {ticker}</strong><small>PUBLISHED {published}<br>ISSUE {issue}</small></div>
 <div class="cover-story"><p class="cover-label">MEYO INSIGHTS / ORIGINAL RESEARCH</p><h1>{title}</h1><h2>{official}</h2><p class="cover-deck">{deck}</p></div>
 <div class="cover-art">{pipeline_art()}</div>
 <div class="cover-meta"><div><strong>BY {author}</strong><br>RESEARCH CUT-OFF: {asof}</div><div><strong>MARKET REFERENCE</strong><br>{market}</div><div><strong>INDEPENDENT ANALYSIS</strong><br>VALUATIONS ARE PROVISIONAL</div></div>
 <div class="cover-base">PUBLISHED RESEARCH · NOTES &amp; REFERENCES INCLUDED</div>
 </section>'''


def brief(meta: dict):
    ed=meta.get("editorial") or {}
    info=ed.get("brief") or {}
    if not info:
        return ""
    ts=[]
    for i, item in enumerate(ed.get("takeaways", []), 1):
        ts.append(f'<div class="takeaway"><div class="takeaway-number">{i:02d}<span>.</span></div><h3>{safe(item["title"])}</h3><p>{safe(item["detail"])} <small>{safe(item["sources"])}</small></p></div>')
    mv=safe(meta.get("marketReference", ""))
    return f'''<section class="brief-page">
    <p class="brief-overline">01 / THE EXECUTIVE BRIEF</p>
    <h2>{safe(info.get('headline','The investment question'))}</h2>
    <div class="brief-intro"><p>{safe(info.get('intro',''))}</p><div class="brief-market"><span>DATED MARKET REFERENCE</span><strong>{mv.split('·')[0].strip()}</strong><small>{mv.split('·')[-1].strip()}</small></div></div>
    <div class="takeaway-grid">{''.join(ts)}</div>
    <div class="brief-bottom"><span>EDITORIAL BOTTOM LINE</span><strong>{safe(info.get('verdict','Provisional analysis — consult Notes and References'))}</strong></div>
    <p class="brief-disclosure">This is an independent research publication. Financial comparisons and valuation assumptions remain qualified where indicated; see Notes before References.</p>
    </section>'''


def svg_bars(values, maxv=None, color_mode="bars", width=650, height=250):
    if not values: return ""
    maximum=maxv or max(float(r["value"]) for r in values)*1.10
    n=len(values); lm=54; rm=18; tm=25; bm=65; chart_h=height-tm-bm
    bw=(width-lm-rm)/max(n,1)*.57
    step=(width-lm-rm)/max(n,1)
    parts=[]
    for i,r in enumerate(values):
        value=float(r["value"]); x=lm+step*i+step*.20; h=chart_h*value/maximum; y=tm+chart_h-h
        fill="#d9df4a" if (i==n-1 and color_mode=="bars") else ("#173d35" if i==n-2 else "#afc2b2")
        label=safe(r["label"])
        parts += [f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{fill}"/>',
                  f'<text x="{x+bw/2:.1f}" y="{y-10:.1f}" text-anchor="middle" class="chart-number">{value:g}</text>',
                  f'<text x="{x+bw/2:.1f}" y="{tm+chart_h+22:.1f}" text-anchor="middle" class="chart-axis">{label}</text>']
    parts.append(f'<line x1="{lm}" y1="{tm+chart_h}" x2="{width-rm}" y2="{tm+chart_h}" stroke="#8b9b8f"/>')
    return f'<svg class="evidence-svg" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'


def exhibit(ex: dict):
    kind=ex["kind"]
    title=safe(ex["title"]); subtitle=safe(ex.get("subtitle", ""))
    provenance=f'<p class="exhibit-source"><strong>SOURCE &amp; BASIS</strong> {safe(ex["source"])}</p><p class="exhibit-caveat">{safe(ex["caveat"])}</p>'
    if kind=="bar":
        content=svg_bars(ex.get("data", []))
    elif kind=="compare":
        data=ex.get("data",[])
        boxes=''.join(f'<div class="compare-box {"compare-highlight" if i==1 else ""}"><span>{safe(x["label"])}</span><strong>{float(x["value"]):.2f}</strong><small>{safe(x.get("unit",""))}</small></div>' for i,x in enumerate(data))
        content=f'<div class="compare-grid">{boxes}</div>'
    elif kind=="valuation":
        data=ex.get("data",[])
        maxv=max([float(x["value"]) for x in data] or [1])
        rows=''.join(f'<div class="valuation-row"><span>{safe(x["label"])}</span><div class="valuation-track"><div class="valuation-fill {"market" if x.get("market") else ""}" style="width:{max(2,100*float(x["value"])/maxv):.2f}%"></div></div><strong>{float(x["value"]):.2f}</strong></div>' for x in data)
        content=f'<div class="valuation-bars">{rows}</div>'
    elif kind=="pipeline":
        content=pipeline_art()
    else:
        raise ValueError(f"Unsupported editorial exhibit kind: {kind}")
    return f'<figure class="evidence-exhibit kind-{safe(kind)}"><figcaption><div class="exhibit-eyebrow">THE EVIDENCE / {safe(kind).upper()}</div><h3>{title}</h3><p>{subtitle}</p></figcaption>{content}{provenance}</figure>'


def add_exhibits(meta: dict, rendered: str):
    ed=meta.get("editorial") or {}
    for ex in ed.get("exhibits",[]):
        anchor=ex.get("beforeHeading")
        if not anchor:
            raise ValueError("Every editorial exhibit requires a beforeHeading anchor")
        matcher = re.compile(r'(?=<h[23]>'+re.escape(anchor)+r'</h[23]>)')
        if not matcher.search(rendered):
            raise ValueError(f"Evidence exhibit placement heading is absent: {anchor}")
        rendered = matcher.sub(lambda _: exhibit(ex), rendered, count=1)
    return rendered


def build_html(meta: dict, body: str):
    assert_evidence(meta,body)
    title=safe(meta['title']); issue=safe(meta.get('issue', '—'))
    rendered=MD.render(body)
    # Auto-link bare primary-source URLs in the References list while retaining
    # the already-linked Markdown text and its original visible source details.
    if "<h2>References</h2>" in rendered:
        before, tail = rendered.split("<h2>References</h2>", 1)
        def make_link(match):
            url = match.group(0).rstrip('.,;')
            suffix = match.group(0)[len(url):]
            return f'<a href="{safe(url)}">{safe(url)}</a>{suffix}'
        tail = re.sub(r'(?<!["\'])https?://[^\s<>]+', make_link, tail)
        rendered = before + "<h2>References</h2>" + tail
    rendered=add_exhibits(meta,rendered)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><title>{title} | Meyo Insights</title></head><body>
{cover(meta)}{brief(meta)}
<main class="research-report"><div class="body-kicker">MEYO INSIGHTS / FULL COMPANY RESEARCH / ISSUE {issue}</div>{rendered}
<div class="publication-outro"><strong>THE PURSUIT OF BETTER INVESTMENT JUDGMENT.</strong><p>Follow the ongoing research at <a href="https://x.com/meyo_insights">x.com/meyo_insights</a></p><small>Published by Meyo Insights. Independent research and education; not personalized investment advice.</small></div>
</main></body></html>'''


def generate(src: Path, target: Path, css: Path):
    metadata,body=parse_article(src)
    target.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=build_html(metadata,body),base_url=src.resolve().parent.as_uri()+"/").write_pdf(str(target),stylesheets=[CSS(filename=str(css))],presentational_hints=True)
    if target.stat().st_size < 3000:
        raise RuntimeError(f"PDF too small: {target}")
    from pypdf import PdfReader
    pdf=PdfReader(str(target))
    if len(pdf.pages)<2:
        raise RuntimeError(f"Publication is unexpectedly short: {target}")
    all_text='\n'.join((p.extract_text() or '') for p in pdf.pages)
    for required in (str(metadata['title']), 'MEYO', 'INSIGHTS'):
        if not required in all_text:
            raise RuntimeError(f"Missing publication text in PDF: {required}")
    if metadata.get('issue')=='001' and 'References' in all_text:
        assert all_text.find('Notes') < all_text.rfind('References'), 'Notes must precede references'
    print(f"{target}: {len(pdf.pages)} pages / {target.stat().st_size:,} bytes")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--site',type=Path,default=Path('.'))
    args=parser.parse_args(); site=args.site.resolve()
    css=site/'assets'/'editorial-print.css'
    src=site/'src'/'pages'/'blog'
    out=site/'public'/'reports'
    if not css.exists() or not src.is_dir():raise RuntimeError('Missing PDF CSS or public blog')
    out.mkdir(parents=True,exist_ok=True)
    for stale in out.glob('*.pdf'):stale.unlink()
    for post in sorted(src.glob('*.md')):
        generate(post,out/f'{post.stem}.pdf',css)
    print('Generated',len(list(src.glob('*.md'))),'publication PDFs')

if __name__=='__main__':main()