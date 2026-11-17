# Meyo Insights — print publication principles (adapted from the supplied production guide)

**Status:** Proposed editorial standard for the PDF publishing agent; not yet a claim that every page blueprint is implemented.

## What we borrow

The supplied `Editorial Publication Design System & Production Style Guide` is an excellent *production discipline* reference. Its implementation sample uses a magazine-sized HTML sheet with print CSS. Meyo Insights will keep its **own brand**, copy and art direction, and apply the useful general principles:

| Source principle | Meyo Insights adaptation |
| --- | --- |
| Twelve-column page grid; measured margins | Logical 12-column design grid for editorial spreads, with simple two-column pages as the default for long investment research. A4 print remains the standard for convenient Kenyan office printing; revisit magazine trim separately, not as a silent breaking change. |
| Two primary font families | Open-source **Inter** (display, labels, tables) plus **Source Serif 4** (body and expressive editorial headlines), or equivalent locally installed fallbacks verified during PDF build. A condensed font is optional *only if* it does not become a third competing family. |
| 80/15/5 colour hierarchy | Warm neutral paper and deep ink dominate. Meyo forest `#173D35` stays the flagship spot accent, with warm ochre reserved for data emphasis. Prefer **one accent per spread** and don't use low-contrast accent colours for small text. |
| 9.75pt / 13.5pt body baseline | Target comfortable print reading, about 10–11 pt serif body; don't force excessive 3–4-column text into A4 when accounting tables or source notes need room. |
| Editorial blueprints | Separate cover, executive brief, investigative feature, evidence spread, valuation spread, glossary/sources. Avoid arbitrary repetitions of the same title and generic stacked cards. |
| Direct-annotated Tufte-style charts | Clear sources, units, reporting scope, periods and data labels; no 3D, unnecessary legends, heavy gridlines or ambiguous comparisons. Use chart emphasis to explain evidence rather than dramatize it. |
| Structured framework layouts | For investment philosophy or methodology posts, use numbered insight modules and fine dividers rather than generic icon cards. |
| Preflight checks | Check page boundaries, colour, font fallbacks, table splits, footers, orphan lines, chart references, links, PDF metadata, mobile legibility and underlying calculation equivalence. |

## What we specifically do not borrow

- The HBR masthead or cover compositions, proprietary imagery, copyrighted layouts, brand marks, fake magazine price/barcode or reproduction of their actual article content.
- Mandatory full-bleed executive portraits in company research reports. Prefer a licensed, credited image of the issuer's operations or an original technical illustration that advances the argument.
- The full colour palette of the reference. **Only one controlled accent on each editorial spread**.
- Rules that reduce accessibility or introduce unreadably narrow body columns or financial tables.
- Claims that aesthetic polish implies an audited valuation or resolved financial statements.

## Meyo Insights publication components

1. **Cover:** approved masthead and logo, report title, short deck, `EXCHANGE: TICKER` for listed equities, issue number, author, reporting scope, dated price, research cut-off, publication/revision status.
2. **The Brief:** 3–5 *owner-approved*, evidence-linked key takeaways. The key uncertainty sits beside the most important conclusion, never buried in endnotes.
3. **Business model:** original diagram of the economic mechanism, e.g., volume × tariff − operating and maintenance costs.
4. **Evidence pages:** revenue, cash, margins and capital structure, dated, labelled, and supporting complete tables. Company/group and original/adjusted series are never silently combined.
5. **Valuation spread:** dated market price, verified shares, 5-/10-year bear/base/bull valuation bands, assumption and sensitivity labels. Provisional valuations are visibly marked **Provisional**.
6. **Risks and countercase:** reasons the thesis may fail and observable events that could change it.
7. **Sources and change log:** working links and source IDs, notes, scope limitations, correction history, evidence and author approval.

## Why the HTML sample lost colour in print

The supplied sample defines coloured surfaces such as `#F7F6F2` and `#E83E28`. It has `@media print` layout rules but **no explicit `print-color-adjust: exact`**. Chrome's default print options often omit backgrounds, and disabling those backgrounds visually strips accent blocks and tinted sheets.

For browser-generated PDFs:
```css
@media print {
  html, body, .sheet, .sheet *,
  .masthead, .cover, .chart, .callout {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}
```

The export must still specify **print backgrounds**, e.g. Playwright Chromium `page.pdf(print_background=True, prefer_css_page_size=True)`. For manual Chrome export turn on **More settings → Background graphics**. `print-color-adjust` is a request to retain colour, not a guarantee that printer drivers, colour profiles or PDF viewers will display identical colours.

Fonts in the uploaded example load via Google Fonts. Production build must **bundle or install licensed open-source fonts** and validate them; don't depend on the export environment having web access.

The Meyo current automated pipeline uses **WeasyPrint**, not Chromium. The proposed browser export flags above describe a possible browser renderer; they are **not** currently active in the production script. The CSS colour preservation declarations are harmless additional guidance for browser parity, but exporting from WeasyPrint must be visually validated on its own.

## Mandatory publish-time preflight

- [ ] Approved branded masthead and verified issuer/exchange/ticker; no placeholder company logo.
- [ ] Key takeaways supported by citations; any unresolved disagreement is visible near corresponding data.
- [ ] Page geometry and 12-column design logic are consistent, but no clipped content or forced microprint.
- [ ] Maximum two deliberate font families. Actual renderer fonts confirmed available and embedded/substituted appropriately.
- [ ] Text contrast and a single controlled accent colour checked visually.
- [ ] PDF background colours and vector graphics survive the selected export engine.
- [ ] Every data visualization can be reproduced from approved source values, has a dated basis and footnotes.
- [ ] Tables do not clip or obscure scope; row and column headings are clear.
- [ ] No widows/orphans, footer collisions, accidental blank pages or broken links.
- [ ] PDF text extractable, references clickable, PDF opens in mobile viewers.
- [ ] **Research approval and exact public publication approval** recorded separately.

Source reference: user's supplied `Editorial Publication Design System & Production Style Guide.md` and `HBR-Style Editorial Publication Report (Print-to-PDF Ready).html`, consulted for general design practices. Do not copy the demonstration's HBR-like branding or content into the website.
