---
name: editorial-pdf-publisher
description: Typeset and QA download-ready Meyo Insights research PDFs from already approved public Astro Markdown, following original print-journal design.
---

# Meyo Insights — Editorial PDF Publishing

## Purpose

Act as a **design and preflight agent**, not a research writer or publication approver.

Make authored research attractive, legible, sourced and consistently branded in web and PDF versions. Use an original editorial system inspired by clear business magazines: strong headline hierarchy, generous margins, readable prose, restrained colours, and data-first charts and tables. Do **not** copy Harvard Business Review logos, proprietary layouts, cover art, typography files, or article content.

## Input boundary

- Input is only the already owner-approved `src/pages/blog/*.md` files of the **public** Astro repository.
- A private report, draft PR, private research merge or an AI-generated revision is **not** publication consent.
- Do not import from `meyoinsights/meyo-insights` (private) or from personal research documents.
- Every article needs title, description, author, date, sources and a human-reviewed approval/merge decision.
- Avoid exposing private research data, credentials, machine provenance notes, financial models or private PDFs without explicit approval.
- Preserve every qualification, date, amount, accounting scope and source attribution from the approved text.

## Steps

1. **Inspect:** Check article headings, tables, links and footnotes for structure and source references.
2. **Typeset:** Use `assets/editorial-print.css`; don't introduce per-article layout hacks unless justified.
3. **Build:** Run `python scripts/build_publication_pdfs.py` before `npm run build`; PDFs go to `public/reports/<slug>.pdf`.
4. **Preflight:** Confirm PDF opens and has pages, article text isn't missing, source links remain clickable, table cells aren't clipped, table headers are repeated where possible, and page numbering/cover are correct.
5. **Visual QA:** For any new layout or complex chart/table, render sample pages and inspect visually. Verify mobile browser PDF download and normal website article reading separately.
6. **PR for review:** Provide a checklist of source and visual issues. If source-derived claims need correction, request owner review; **never silently change research facts to improve layout**.
7. **Publish:** Only after the owner merges the relevant article PR to `main` does GitHub Pages host the article and its matching downloadable PDF.

## Output contract

- Website URL: `/blog/<slug>/`
- PDF URL: `/reports/<slug>.pdf`
- PDF appearance: A4 portrait, distinctive cover, author/date, numbered pages, tables, clickable references, original Meyo Insights cream/forest/ochre palette.
- All article links use the same slug for a deterministic downloadable PDF.
- A PR build may create a PDF artifact for validation, but must **not deploy it** to production.

## Failure policy

If the PDF generator, content parser or Astro build fails, CI fails. Do not publish a broken or unapproved artifact. If an article is removed, stale generated PDFs must not persist in the new deployment.

## Suggested improvements (future)

- Semantic figure components for source-attributed charts and editable Excalidraw diagrams.
- Add PDF preflight detection for overflow / extremely small table text.
- Versioned reports with corrections, revision history and source-as-of date.
- Optional downloadable summary sheet and linked data appendix once both are reviewed.

## V2 art-direction gate (not yet fully implemented)

Read [the editorial design system v2](../../../docs/EDITORIAL_DESIGN_SYSTEM_V2.md) before changing the visual template. Its six-page KPC design proof is a proposal, not a publication. The current automated v1 template must be reviewed against the v2 requirements **before** merge.

For listed companies the agent must not proceed silently with a generic Markdown cover. Collect **exchange, ticker, dated market reference, issue number, report date, research-as-of date and evidence-backed key takeaways** from the approved publication metadata. Distinguish approved identity assets from proposed design marks. Build an executive brief before detailed analysis and charts that answer specific questions, each carrying source/basis and limitations. The agent may highlight a verified claim but may not rewrite its economic meaning, supply a missing number, or infer an owner verdict. If required metadata is missing, flag the publication for human completion rather than hiding the gap in a generic layout.

Preflight the resulting **actual PDF**, not just the Astro build. Inspect cover, evidence spread, valuation visualization, tables and source pages individually at print size and on a mobile viewer. Record reviewer, date, approved research revision and a visual sign-off in the publishing PR.

## Supplied editorial production guide

Read [the adapted print guide](../../../docs/PRINT_DESIGN_GUIDE_ADAPTATION.md). Apply its typography, hierarchy, print-colour consistency, meaningful charts and preflight practices while retaining Meyo's original branding. For browser-to-PDF parity use `print-color-adjust: exact` plus the export engine's print-background setting. The current generator uses WeasyPrint, so do not claim browser flags are enabled unless its engine actually changes.
