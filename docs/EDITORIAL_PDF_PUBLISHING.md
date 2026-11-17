# Website and PDF editorial publishing

Meyo Insights uses **one public Markdown source** for each article and its printable A4 PDF. The article and PDF should match in research content, sources and limitations.

## Editorial control

- The private research repository remains private. A research PR merge is not publication approval.
- Owner approves **exact public wording** in a public website pull request.
- Merging that PR to `main` permits publication of **that** article and its PDF via GitHub Pages. PR CI generates only local build artifacts, never a production deployment.
- The PDF generator never fetches or publishes unpublished research, and must not alter factual content.
- The current v6.0 KPC report is an **unapproved research draft**. The design preview of that report is for editorial review only. It must not be added to `src/pages/blog` or `public/reports` until approved.

## Publisher automation

A deploy (or PR check) runs:

```bash
python -m pip install -r requirements-pdf.txt
python scripts/build_publication_pdfs.py
npm ci
npm run build
```

1. Reads `src/pages/blog/*.md` (no private directory).
2. Validates Astro frontmatter: title, description, author, pubDate, layout; fails if a public post is marked draft.
3. Typesets PDF using the original `assets/editorial-print.css` print design.
4. Writes `public/reports/<article-slug>.pdf` and checks pages with pypdf.
5. Astro copies PDFs into `dist/reports/`; every blog article offers a PDF download link.
6. GitHub Pages serves `https://meyoinsights.github.io/reports/<article-slug>.pdf` after deployment.

The generator regenerates the PDF set for the current public articles on every build. Generated PDFs are gitignored to prevent stale binary sources in version control.

## Visual rules

- Expressive serif headline, measured sans-serif labels and headings, readable serif body.
- Cream paper, forest green, moss accents and occasional warm ochre for emphasis.
- Numbers and financial tables remain readable in print and on phones when zoomed.
- Put evidence first; a beautiful layout cannot hide contradictory figures or create false confidence.
- Inline clickable sources wherever available, and a clearly labeled Sources section for full reports.
- Do not reproduce any HBR images, trademarked masthead, stock photography or magazine page compositions.

## Manual QA checklist

- [ ] Cover title, author, report/as-of date and status are accurate.
- [ ] No clipped tables, blank pages, unexpected widows or illegible footnotes.
- [ ] Source URLs remain clickable and present in both web and PDF versions.
- [ ] The PDF contains the same material caveats and figures as approved Markdown.
- [ ] The PDF renders on Android and desktop PDF viewers.
- [ ] No private file or research draft entered the public build.
- [ ] Build passes; owner explicitly approves the release.

See [the Codex skill](../.agents/skills/editorial-pdf-publisher/SKILL.md).
