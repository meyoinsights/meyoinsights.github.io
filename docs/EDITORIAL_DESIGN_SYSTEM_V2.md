# Meyo Insights — Editorial Design System v2 (proposal)

**Status:** Owner-review design direction. The six-page KPC design proof is a visual prototype, not an approved research publication. The current PDF generator in this PR remains the v1 baseline; v2 layout and metadata still require implementation and validation before this PR is merge-ready.

## Publication identity

- An original Meyo Insights **M mark + wordmark**, derived from the current MEYO / INSIGHTS text identity. The proposed mark needs brand approval before becoming permanent.
- For listed companies, put the **exchange and ticker** beside the issuer on the cover, e.g. **NSE: KPC**.
- Always display issue number, author, publication date, research-as-of date, dated market reference and research/review status.
- Palette: forest `#173D35`, warm ivory `#F8F5EE`, dark ink `#162A23`, sage `#AECAB2`, ochre `#EAB74C`, coral `#C96B4A` for meaningful warnings.
- Two-family editorial type system: expressive and readable serif headlines + body; compact sans-serif labels, chart annotations and supporting metadata. Avoid shrinking body text or tables to fit.

## Page order and visual priorities

1. **Cover:** brand mark, issuer, ticker, strong story headline, explanatory deck, author and version metadata, original or properly licensed image/diagram.
2. **The Brief:** central question and three to five **owner-reviewed key takeaways**, with the most consequential uncertainty next to the conclusion.
3. **Business economics:** short explanation, unit-economics diagram or original value-chain illustration.
4. **Financial evidence:** comparable chart and full underlying table. Every chart has units, period, company/group scope, source and caveat.
5. **Disputed figures:** give competing published numbers equal visual weight and mark the reconciliation status.
6. **Valuation:** five- and ten-year bear/base/bull scenarios, market-price reference and sensitivity assumptions, explicitly provisional where appropriate.
7. **Risks and falsifiers:** concrete evidence that could change the conclusion.
8. **Methodology, sources, corrections and disclosures:** transparent evidence register.

The KPC example demonstrates the editorial principle: a KES 7.49bn versus KES 10.24bn FY2025 profit mismatch is a prominent research finding, **not a footnote**.

## Proposed explicit publication metadata

```yaml
publication:
  type: company-research
  issue: "001"
  exchange: NSE
  ticker: KPC
  issuer: Kenya Pipeline Company PLC
  research_as_of: "2026-11-14"
  market_reference: "KES 10.70, 13 November 2026"
  review_status: "Working research — provisional valuation"
  key_takeaways:
    - title: Valuable network, uncertain investment price
      detail: Strategic infrastructure does not automatically establish shareholder value.
      sources: [S01]
    - title: Reconcile the FY2025 earnings bases
      detail: IPO compiled figures and FY2026 comparatives differ materially.
      sources: [S01, S02]
```

For a listed-company report, the agent must require a real exchange and ticker, dated price reference or explicit unavailable status, three to five takeaways and evidence references for each. **Do not invent takeaways, numerical highlights, a logo provenance or a verdict.** Human reviewers approve them.

## A professional publisher's production workflow

1. **Research editor** tests the thesis, countercase and evidence.
2. **Fact/data editor** checks tables, chart data, units, accounting scope, sources and calculations.
3. **Art director** decides which finding deserves strongest treatment and selects properly licensed visuals.
4. **Publication designer** works with grids, optical hierarchy, whitespace, typography, imagery and clear charts.
5. **Production editor** inspects every rendered page, hyperlinks, orphan lines, table continuations, mobile readability and PDF metadata.
6. **Owner** approves the exact article **and matching PDF**. PR validation is not publication. Private research never moves into a public build without explicit approval.

## Next KPC report — acceptance criteria

- [ ] Cover includes approved logo/wordmark, **NSE: KPC**, author, market reference, date and status.
- [ ] Key takeaways are individually evidence-backed and visually prominent.
- [ ] Company versus group reporting and original versus IPO-compiled data are visibly distinguished.
- [ ] The unresolved FY2025 accounting mismatch is explained close to the evidence.
- [ ] DCF scenarios use a dated market comparison and prominent provisional-model qualifications.
- [ ] Tables, figures and sources are legible on A4 and mobile; no orphaned lines or clipping.
- [ ] Full nine-section report and its PDF receive owner sign-off before public release.

Do not reproduce Harvard Business Review's masthead, photography, page compositions or other protected graphic assets. We are building a distinct Meyo Insights publication.
