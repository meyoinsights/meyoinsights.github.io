---
layout: ../../layouts/ArticleLayout.astro
title: "Kenya Pipeline Company: Is the Share Price Justified?"
description: "An independent assessment of the business, accounts, cash flows and price of Kenya Pipeline Company."
author: widdzz
pubDate: 2026-11-18
issue: '001'
exchange: NSE
ticker: KPC
researchAsOf: "14 November 2026"
marketReference: "KES 10.70 · 13 November 2026"
publicationStatus: "Independent analysis · provisional valuation"
editorial:
  issuer: Kenya Pipeline Company PLC
  displayTitle: "KPC: Testing the investment case."
  coverDeck: "KPC's pipelines matter to regional trade. But reported profits, accounting changes and a demanding capital plan complicate the investment case."
  brief:
    headline: "A valuable network does not automatically make a cheap share."
    intro: "Kenya Pipeline Company transports and stores refined fuel across a network that is expensive to reproduce. The harder investment question is how much cash will reach ordinary shareholders after upkeep, new projects and other obligations."
    verdict: "WATCH — NOT A PROVEN BARGAIN. Valuation scenarios are provisional."
  takeaways:
    - title: "The network is difficult to replicate"
      detail: "Physical scale is an advantage, but regulated tariffs limit how much shareholders can capture."
      sources: "[S01][S06]"
    - title: "The FY2025 profit bases disagree"
      detail: "The IPO compilation and the newer comparative report different group profits; a reconciliation is still required."
      sources: "[S01][S03]"
    - title: "Cash flow is not yet distributable cash"
      detail: "Planned capital expenditure and debt financing may absorb future cash; a strong year is not a dividend forecast."
      sources: "[S01]"
    - title: "The base scenarios are below the price"
      detail: "The five- and ten-year estimates are conditional, not verified fair values or a trading recommendation."
      sources: "[S01][S03][S05]"
  exhibits:
    - kind: pipeline
      beforeHeading: "What KPC does and how it makes money"
      title: "A pipeline is a toll road for fuel."
      subtitle: "Throughput and regulated route charges drive revenue; power, maintenance and capital investment determine the economics."
      source: "KPC IPO information memorandum [S01]; EPRA tariff disclosures [S06]"
      caveat: "An explanatory illustration, not an as-built engineering map or accounting identity."
    - kind: bar
      beforeHeading: "Five-year historical results (FY2021–FY2025)"
      title: "Revenue rose. Comparability takes work."
      subtitle: "Reported revenue, KES billions, FY2021–FY2025. Do not treat the series as like-for-like organic growth."
      source: "KPC IPO selected historical financial information [S01]"
      caveat: "KPRL entered the group during the period. Reporting basis and adjustment notes must be read with the chart."
      data:
        - {label: FY21, value: 27.99}
        - {label: FY22, value: 26.21}
        - {label: FY23, value: 30.86}
        - {label: FY24, value: 35.37}
        - {label: FY25, value: 38.59}
    - kind: compare
      beforeHeading: "The FY2025 comparison problem"
      title: "One financial year. Two profit figures."
      subtitle: "KES billions, FY2025 group net profit, as presented in different reporting compilations."
      source: "IPO reporting accountant compilation [S01]; FY2026 published comparative [S03]"
      caveat: "Approximately KES 2.75bn difference remains unreconciled. These are not a like-for-like growth base."
      data:
        - {label: "IPO compiled group / FY2025", value: 7.49, unit: "KES BILLION"}
        - {label: "FY2026 release / FY2025 comparative", value: 10.24, unit: "KES BILLION"}
    - kind: valuation
      beforeHeading: "Five-year and ten-year discounted valuations"
      title: "A price is a fact. A value is a model."
      subtitle: "Market capitalisation versus provisional base present-value estimates. KES billions."
      source: "Dated market reference and model assumptions [S03][S05]"
      caveat: "Five- and ten-year scenario outputs depend on unverified capex, financing and cash-flow assumptions; they are not firm price targets."
      data:
        - {label: "5Y BASE", value: 124.57}
        - {label: "10Y BASE", value: 144.70}
        - {label: "MARKET", value: 194.45, market: true}
---

**Issue 001 · Independent company research · Research cut-off: 14 November 2026**

**Reader's note:** I am publishing this analysis with open questions, not claiming it is perfect or presenting a definitive price target. Figures and assumptions that still need independent verification are collected in **Notes**, immediately before **References**.

## Abstract

KPC owns infrastructure that Kenya and its neighbours use to move and store fuel. It earns money from transport and storage, mainly under regulated tariffs. Its pipelines would be costly to replace. But owning essential assets does not guarantee good returns for shareholders. [S01][S06][S07]

KPC reported **KES 42.98 billion in revenue** and **KES 11.58 billion in net profit** for the year ended June 2026. It also reported **KES 119.33 billion in shareholders' equity**. At the **13 November 2026 closing price of KES 10.70**, the market valued all shares at about **KES 194.45 billion**. Investors therefore paid **1.63 times accounting book value**. [S01][S03][S04][S05]

Our base cash-flow scenarios value KPC at **KES 124.57 billion over five years** and **KES 144.70 billion over ten years**. Both are below the market value. These are tests of assumptions, not established fair values. We lack a full bridge between two sets of FY2025 accounts and a current, project-by-project spending plan. [S01][S03]

Two risks deserve close attention. First, the IPO forecast envisaged **KES 110.32 billion of spending on fixed assets and intangibles from FY2026 to FY2030**. That was a forecast, not audited actual spending. Second, a proposed refinery in Lamu could either send more fuel through KPC's network or draw volume away through other routes. We have no verified KPC transport agreement for the refinery. [S01][O03][O04][O05]

**Current verdict:** KPC appears to own valuable assets and generate cash, but **the shares do not look underpriced under our base assumptions**. We cannot make a firm call until we check the accounts and capital plan.

## Introduction

**Question.** At the 13 November 2026 share price, does KPC offer enough value for its assets, cash generation and long-term business risks?

This report examines the business, its last five reported financial years, the latest FY2026 results, its assets and cash flows, two discounted valuations, and threats to the transport routes on which its revenue depends. We use the IPO memorandum, company disclosures, regulator data, signed accounts where available, and attributed reporting. References appear as bracketed source IDs that resolve in **Sources**.

**How to read it.** We mark company figures as reported, calculations as derived, and forecasts as assumptions. Five-year history is not always comparable because KPRL entered the group in FY2024. The 11% valuation rate is an investor assumption; the five- and ten-year values are scenarios, not established fair values. The FY2025 profit discrepancy and FY2026 capital-spending detail are still open. This published analysis does not replace an independent verification of the underlying sources.


## Company Review

### What KPC does and how it makes money

KPC moves refined fuel from coastal storage to inland markets. Oil marketers pay it to move and store fuel. The tariffs can affect the eventual cost of fuel. KPC's revenue depends mainly on how much fuel it handles, which routes it uses and the prices allowed for each service.

> **Revenue = transport volume × route charges, summed across routes, plus storage and other fees.**

This is a guide, not an accounting formula. The fee changes with distance, service and route. The IPO memorandum says transport and storage account for about **95% of revenue**. Fibre, LPG-related services, training, conference services and rent make up most of the rest. [S01]

### Infrastructure and reporting scope

KPC's main assets include pipelines, pumps, tanks and inland facilities. The FY2024 company-only fixed-asset note reports KES 58.24 billion for pipelines, pumps and tanks, within KES 83.33 billion of net property, plant and equipment. These are accounting values, not an independent estimate of what the assets could be sold for. [S14]

KPC acquired Kenya Petroleum Refineries Limited (KPRL) in October 2023. The acquisition affects which operations appear in the group accounts, so we must separate acquired activity from underlying growth. We have not reconstructed current ownership percentages from a verified shareholder register. [S01]


## Financial Review (Fundamental Analysis)

### Five-year historical results (FY2021–FY2025)

The IPO memorandum gives us a five-year record. But **FY2021–FY2023 show KPC alone**, while **FY2024–FY2025 include KPRL**, which KPC acquired in October 2023. Part of the apparent growth therefore comes from adding another business. Figures below are in **KES billions**. [S01]

| Indicator | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Revenue | 27.99 | 26.21 | 30.86 | 35.37 | 38.59 |
| Gross profit | 14.42 | 12.67 | 17.64 | 20.85 | 23.86 |
| Operating profit (selected summary) | 3.48 | 6.64 | 5.51 | 10.13 | 11.93 |
| Net profit/(loss) | (1.74) | 4.24 | 3.30 | 7.41 | 7.49 |
| Operating cash flow | 8.96 | 12.86 | 11.81 | 11.30 | 14.26 |
| Reported PP&E + intangible capex | 0.42 | 0.71 | 2.69 | 4.35 | 1.47 |
| CFO − reported capex (proxy) | 8.53 | 12.14 | 9.12 | 6.95 | 12.79 |
| Year-end equity | 87.79 | 79.98 | 80.98 | 91.99 | 98.39 |

**Source detail:** the IPO's selected summary pp. 83–86 and Reporting Accountant's historical cash-flow tables in Appendix V. CFO−capex is **our calculation**, not a reported distributable-equity-cash number. The smaller FY2025 capex could reflect project timing rather than a permanent reduction in sustaining needs. [S01]

### What changed?

- **Revenue rose 9.1% in FY2025**, and about **8.36% a year from FY2021 to FY2025** on the reported basis. Some growth reflects the addition of KPRL.
- **Gross margin rose to 61.8% in FY2025** from about 51.5% in FY2021. We need to know whether lower costs, longer routes, service mix or accounting changes drove the increase.
- **Operating margin reached 30.9% in FY2025** on the IPO basis. Profit has not risen smoothly: KPC lost money in FY2021 and recorded major asset write-downs in FY2023.
- **Cash from operations was KES 14.26 billion in FY2025.** Recorded asset spending was only KES 1.47 billion. We should not assume it will stay that low.
- **Liquidity improved.** The current ratio rose from **1.22 to 1.46** between FY2024 and FY2025. Interest-bearing debt fell from **6.37% to 3.36% of equity**. [S01]

### Why old EPS cannot be compared with new EPS

The IPO summary gives FY2025 earnings per share (EPS) of **KES 412** under the old share structure. Appendix V gives **KES 467** on a company-only basis. FY2026 EPS is **KES 0.64** under the post-IPO structure. These are **not comparable measures of earnings growth**. The same warning applies to old state dividends and later per-share payouts. [S01]

### Latest reported results (FY2026)

KPC released results for the year ended **30 June 2026** in October. We found the official results listing but could not inspect the linked one-page summary in full when preparing this version. The figures below come from reports published near the announcement date. **We still need to compare every line with the full signed annual report.** [S02][S03][S04][S12]

| Measure | FY2026 | Interpretation |
|---|---:|---|
| Revenue | **KES 42.98bn** | Reported ~8.8% increase vs its FY2025 comparable (about 39.5bn) |
| Profit after tax | **KES 11.58bn** | Reported ~13.1% increase vs FY2025 10.24bn comparable |
| EPS | **KES 0.64** | Comparable current post-IPO share basis |
| Recommended DPS | **KES 0.32** | Board-recommended; payable status/approval should be checked |
| Equity | **KES 119.33bn** | Accounting book equity; includes revaluations/other reserve effects |
| Interest-bearing borrowings | **KES 0.443bn** | Borrowings/equity approximately **0.37%** |
| Current assets / liabilities | **KES 30.03bn / 6.10bn** | Current ratio approximately **4.92x** using rounded amounts |
| Reported cash generated from operations | **KES 17.39bn** | Secondary summary wording; classification should be checked against full audit |
| Cash and equivalents | **KES 20.54bn** | Reported year end |
| Net cash used in investing activities | **KES 4.48bn** | Do **not** substitute for individual capex line items |

Using the reported numbers, we calculate a **26.9% net profit margin**, a **16.7× price-to-earnings ratio**, a **3.0% indicative dividend yield**, **KES 6.57 of book value per share** and a **1.63× price-to-book ratio**. Return on average equity is about **10.2%**, using the later FY2025 comparison. These are our calculations from rounded figures, **not separately reported company ratios**. [S03][S04][S05]

### The FY2025 comparison problem

| FY2025 line (KES bn) | Jan 2026 IPO consolidated | FY2025 comparator in FY2026 release | Difference |
|---|---:|---:|---:|
| Revenue | 38.59 | ~39.51 | +0.92 |
| Profit after tax | **7.49** | **10.24** | **+2.75** |
| Shareholders' equity | **98.39** | **107.92** | **+9.53** |
| Total assets | **139.01** | **140.63** | **+1.62** |

**We have not proved why these numbers changed.** It might relate to which businesses were included or to corrections in the accounts, but that remains unverified. Until we get the full bridge, use the FY2025 comparison presented alongside FY2026 when calculating FY2026 growth. [S01][S03][S12]

### Free cash flow: cash after capital spending

Free cash flow (FCF) starts with cash from operations and deducts cash spent on long-lived assets. It helps show whether reported profit turns into cash. But these figures do **not** show how much KPC can safely pay in dividends. They do not cover all future projects or funding needs. FY2024 and FY2025 include KPRL; earlier years cover KPC alone. [S01]

| KES bn | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Cash flow from operating activities | 8.96 | 12.86 | 11.81 | 11.30 | 14.26 |
| PP&E + intangible cash capex | 0.42 | 0.71 | 2.69 | 4.35 | 1.47 |
| **Historical FCF proxy** | **8.53** | **12.14** | **9.12** | **6.95** | **12.79** |

The FY2025 figure of **KES 12.79 billion** equals **6.6% of the current market value**. That looks attractive at first. But annual spending can vary sharply. KPC's FY2024 standalone accounts record about **KES 4.81 billion of depreciation** and **KES 4.26 billion of additions to fixed assets**. We need the full FY2026 cash-flow notes and a realistic long-term maintenance budget before we call 6.6% a lasting cash yield. [S14]

### Accounting policies, auditor notes and asset quality

### Accounting notes and the unresolved FY2025 bridge

The FY2025 comparison table above shows a KES 2.75 billion difference in reported profit between the IPO history and the FY2026 comparator. The financial statements have not yet been reconciled line by line. [S01][S02][S03][S15]

Note 44 describes corrections related to environmental claims, the closure of Pipeline 1, asset values, taxes and balances without enough support. These matters may affect asset quality and earnings. **We have not found an audited note that ties the two FY2025 profit figures together, line by line.** We should not guess the cause. [S01][S14]

We also have not checked the exact wording of the signed audit opinion for FY2025 or FY2026. The FY2024 report contains an Auditor-General section, and a Parliamentary archive lists the FY2025 report, but we must read the signed opinions before calling them clean or qualified. [S14][S16]

### Notes that could change KPC's value

| Note / issue | What the source actually shows | Valuation consequence | Status |
|---|---|---|---|
| **Historical accounting adjustments** (IPO Appendix V, Note 44) | Compiled financials adjusted past audited balances; includes unsupported balances, fair-value and tax treatments | Earnings comparability and asset quality require a reconciliation | **Verified category; FY2025 comparator bridge unresolved** |
| **Environmental damage claims** (Note 44) | FY2025 adjustments explicitly include a provision for environmental damage claims | Review likely cash settlement, policy coverage and any unprovided exposure | **Accounting treatment evidenced; adequacy unverified** |
| **Pipeline 1 decommissioning** (Note 44) | Decommissioning costs and related Pipeline 1 valuation issues are explicitly disclosed | Maintenance/replacement cash and liabilities could be higher than recent cash capex | **Disclosed; final cost and schedule not established** |
| **Property valuations / land title** | Prior-year adjustments and annual-report policies include non-cost measurement and issues with property without title | Accounting book value is not a realizable floor; verify titles and valuation assumptions | **Disclosure verified; adjusted NAV not calculated** |
| **Contingent claims** (IPO historical notes) | Directors describe legal/tax claims with uncertain outcomes | Underwrite expected losses, avoid treating uncertain contingencies as zero | **Disclosed, not fully valued** |
| **Customer-owned fuel** (IPO Note 42) | Fuel held for oil marketers is excluded from KPC-owned assets | Do not add third-party petroleum inventory to KPC NAV | **Verified** |
| **Capital commitments** (IPO Note 43) | FY2025 group commitments net of work-in-progress total **KES 4.689bn** | Distinguish binding/authorized commitments from much larger management forecasts | **Historical amount verified; latest plan needed** |
| **KPRL acquisition / common control** | KPRL came under the group in 2023/24; predecessor and group years are not like-for-like | Segment organic growth; do not paste together unrelated earnings bases | **Verified structure** |
| **2024 fixed-asset schedule (FY2024 full annual report, Note 17)** | Company-only net PP&E **KES 83.33bn**, including pipelines/pumps/tanks **KES 58.24bn**, and work in progress **KES 4.31bn**; annual depreciation charge approx **KES 4.81bn** | Network value is capital-intensive; recent spending below annual depreciation may not reflect long-run replacement need | **Full note reviewed; do not compare company-only fixed assets directly with group NAV** |

**Next audit check:** Read the full signed report and its notes. Record the auditor's actual findings. Check revenue, receivables, asset write-downs, provisions, asset valuations, possible legal claims, related-party deals, taxes, borrowing conditions and spending commitments. Explain what changed year to year and how it might affect cash or value. Resolve material restatements before relying on growth rates.

### Glossary of financial and valuation terms

- **CAGR:** Compound annual growth rate, `(ending / beginning)^(1/number of year intervals) − 1`. Five observations have four intervals.
- **Current ratio:** Current assets ÷ current liabilities. Liquidity indicator, not a guarantee of cash availability.
- **Debt/equity:** Interest-bearing debt ÷ total equity. Other liabilities and contingencies are separate.
- **EPS/DPS:** Net profit per weighted-average ordinary share / dividends per ordinary share. Verify post-IPO share basis and declaration date.
- **ROE/ROIC:** Net profit ÷ average equity / post-tax operating profit ÷ average invested capital. ROIC is particularly useful for capital-heavy expansion.
- **CFO:** Cash flow from operating activities. Check whether secondary sources mean gross cash generated or net CFO after interest and tax.
- **Capex:** Capital spending on property, plant, equipment and relevant intangibles. Split *sustaining* from *growth*.
- **FCFE:** Cash available to shareholders after operating cash, capex, financing flows and required reinvestment. Here only a **proxy** is modeled.
- **Discount rate:** Required return applied to future equity cash flows. Investor base case here is 11%.
- **Terminal value:** Present value of cash flows beyond forecast year 5 or 10; extremely sensitive to persistent growth and capex assumptions.
- **Intrinsic value:** Model-implied value of future cash flows, **not an observable market fact**.
- **Margin of safety:** `(intrinsic value − quoted price) / intrinsic value`; depends on robust underlying value estimate.
- **Pricing power:** Ability to retain higher real prices without excessive demand loss; regulation limits this.
- **Unit economics:** Net cash/profit attributable to an additional unit (here preferably a route/service-specific m³), not merely blended revenue/m³.

*A larger glossary and full scenario formulas remain in the accompanying workbook.*

### Further definitions

- **Market capitalisation:** Current share price × total ordinary shares outstanding; not enterprise value or free-float value.
- **Book value / accounting NAV:** Consolidated shareholders' equity; per-share book value divides by ordinary shares. These are *not separate independent valuation methods*.
- **Adjusted NAV:** Fair value of identifiable assets less all economic liabilities, costs and adjustments; requires defendable independent valuations.
- **P/B (price to book):** Market cap / book equity, or price / book value per share. Beware of historic-cost and revaluation accounting.
- **P/E (price to earnings):** Price / comparable EPS, or market cap / attributable earnings. Use the same earnings/share basis and avoid mixing historic pre-recapitalisation EPS with current shares.
- **Free cash flow (FCF):** Net operating cash flow minus cash expenditure on capital assets (including relevant intangibles), carefully distinguished from **net investing cash flow** or financing-adjusted FCFE.
- **FCF yield:** Normalized recurring FCF / market cap (for equity cash flow) or FCFF / enterprise value, with consistent definitions.
- **Audit qualification / key audit matter / emphasis:** Different auditor-report concepts; never assume any is present unless the signed report has been checked.

## Valuation

### Market price, market capitalisation and accounting value

The table uses the FY2026 results, the **18.173299 billion shares** shown in KPC's IPO memorandum and the **KES 10.70** closing price. Market value means the price of *all* issued shares, not only the shares traded by the public. [S01][S03][S05][S13]

| Metric | Result | Interpretation / basis |
|---|---:|---|
| Market price (13 Nov 2026) | **KES 10.70** | Last available close, not a live quote |
| Total ordinary shares | **18.173299bn** | Total issued post-offer ordinary shares |
| **Current market capitalisation** | **KES 194.45bn** | Share price × all issued ordinary shares |
| FY2026 revenue | KES 42.98bn | Published FY2026 group figure |
| FY2026 profit after tax | KES 11.58bn | Published FY2026 group figure |
| FY2026 EPS | **KES 0.64** | Published rounded post-IPO EPS |
| FY2026 recommended DPS | KES 0.32 | Proposed distribution, not yet assumed paid |
| **Trailing P/E** | **16.72×** | KES 10.70 / reported EPS KES 0.64 |
| **Reported book equity (NAV)** | **KES 119.33bn** | Consolidated shareholders' equity; NOT appraised liquidation value |
| Total assets | KES 149.27bn | Published FY2026 consolidated assets |
| Total liabilities (implied) | KES 29.94bn | Assets less equity; calculated |
| **Book value per share** | **KES 6.57** | Reported equity / issued shares |
| **P/B ratio** | **1.63×** | Market cap / accounting equity |
| Market premium to accounting NAV | **63.0%** | Market cap / book equity − 1 |
| FY2026 cash from operations (reported summary) | ~KES 17.39bn | Classification requires validation against full statement |
| FY2026 net cash used in investing | ~KES 4.48bn | **Not a capex number** |
| FY2026 FCF: CFO − cash capex | **Not verified** | Full capex cash-payment breakout unavailable in material reviewed |
| FY2025 FCF proxy: CFO − capex | **KES 12.79bn** | IPO 14.26 less PP&E/intangible capex 1.47; historical, not normalized |
| FY2026 cash after net investing (non-FCF proxy) | ~KES 12.91bn | 17.39 − 4.48; includes all investing activity, not pure FCF |

**Book value is not a sale price.** The accounts show net assets of KES 119.33 billion: assets less liabilities. That is the same figure as shareholders' equity. We have **not** produced a separate market-based value for KPC's land, pipelines or other assets. To do so, we would need current valuations, proof of ownership, estimates of clean-up costs, tax and other liabilities. [S01][S14]

### Capital expenditure and financing assumptions

The IPO forecast included large spending on existing assets, new facilities and software or other intangible assets. **These were plans prepared in January 2026, not amounts spent.** [S01]

| Projected year | Sustaining capex | New PP&E | Intangibles | Total planned |
|---|---:|---:|---:|---:|
| FY2026 | 1.83 | 7.43 | 0.00 | **9.26** |
| FY2027 | 1.90 | 9.06 | 1.38 | **12.34** |
| FY2028 | 2.00 | 20.69 | 1.22 | **23.91** |
| FY2029 | 2.33 | 47.39 | 0.00 | **49.72** |
| FY2030 | 3.23 | 11.86 | 0.00 | **15.09** |
| **Total** | **11.28** | **96.43** | **2.60** | **110.32** |

The same forecast included about **KES 13 billion of new borrowing in FY2028** and **KES 32.2 billion in FY2029**, followed by repayments. KPC currently reports little debt, but that could change if it builds the planned projects. We need the latest approved plan, not only this older forecast. [S01]

For each new project, the key question is simple: **How much extra after-tax operating profit will each shilling of investment produce?** We need forecast volume, tariffs, running costs, life of the asset and financing terms before we can answer it.

### Five-year and ten-year discounted valuations

We use **two valuation methods** and show both a five-year and a ten-year forecast.

**Cash-flow model.** We start from the reported FY2026 operating cash figure of **KES 17.39 billion**. For each future year, the model estimates cash generated, deducts spending on existing and new assets, and adds new borrowing less repayments. It discounts those cash flows at **11%**, the investor's required return on equity. The five-year model runs to FY2031; the ten-year model runs to FY2036. Both include a value for cash flows after the forecast period. **This is a scenario model, not a fully verified free-cash-flow-to-equity (FCFE) valuation.** [S01][S03]

**Dividend check.** A separate model starts with a **KES 0.32 proposed annual dividend** and assumes dividend growth of 6% a year for five years, 5% for years 6–10 and 4% thereafter. It also uses 11%. It values that *assumed dividend path*, not all cash the business might earn.

The cash-flow model draws on KPC's January 2026 plan for FY2027–FY2030, then changes spending and borrowing under each scenario. All forecasts after FY2030 are **our assumptions**, not promises made by KPC.

### What each scenario assumes

| Model input | Bear | Base | Bull |
|---|---:|---:|---:|
| Required return | 11% | **11%** | 11% |
| Operating-cash growth years 1–5 | 2% | **6%** | 10% |
| Operating-cash growth years 6–10 | 1% | **4%** | 7% |
| FY2027 sustaining capex | KES 3.0bn | **2.5bn** | 2.2bn |
| FY2027–FY2030 expansion-cost factor vs plan | 120% | **100%** | 85% |
| FY2027–FY2030 net-borrowing factor vs plan | 75% | **100%** | 110% |
| FY2031 new-project capex | KES 6bn | **3bn** | 1bn |
| FY2032 onward annual expansion capex | KES 4bn | **2bn** | 1bn |
| Annual debt repayment FY2032 onward | KES 4bn | **3bn** | 2bn |
| Terminal perpetual equity cash-flow growth | 1.5% | **2.5%** | 3.5% |

We do not assign odds to these cases. The bull case assumes better growth and cheaper projects. The bear case assumes higher costs, slower growth and less borrowing than KPC planned.

### Estimated share values

| Scenario | Five-year explicit discounting | Ten-year explicit discounting | Comparison with KES 10.70 |
|---|---:|---:|---|
| Bear | **1.23** | **1.69** | Considerably below market |
| Base | **6.85** | **7.96** | Below market; conditional estimates |
| Bull | **12.75** | **14.94** | Above market, but assumes favorable project outcomes |
| Dividend-only cross-check | **5.17** | **5.33** | Values modeled dividends, **not a floor/ceiling** |

On the usual **margin-of-safety** measure—(estimated value − price) ÷ estimated value—the base cases give about **−56%** over five years and **−34%** over ten years. Negative figures mean the quoted price is above the estimated value. These are not trading signals. [S01][S03][S05]

**How to read the model:** We discount equity cash flows at the required return on equity, not at the firm's blended cost of capital. Each horizon has its own value for cash beyond the forecast; we do not add the two together. Borrowed money supplies cash now but must later be repaid. We do not add all cash on the balance sheet to the valuation without first proving that it is excess cash. Nor do we treat total investing cash flow as capital spending. The model does not separately value non-operating assets.

### Intrinsic equity value versus market capitalisation

The model discounts estimated cash available to shareholders at an **11% required return**. Each case assumes different growth, spending and borrowing. No case is a confirmed fair value, and we have not assigned probabilities. [S01]

| Scenario | 5-year value/share | 5-year equity value | 10-year value/share | 10-year equity value | Versus KES 194.45bn market cap |
|---|---:|---:|---:|---:|---|
| Bear | KES 1.23 | KES 22.27bn | KES 1.69 | KES 30.66bn | Both substantially lower |
| **Base** | **KES 6.85** | **KES 124.57bn** | **KES 7.96** | **KES 144.70bn** | **KES 69.9bn and 49.8bn below market**, respectively |
| Bull | KES 12.75 | KES 231.65bn | KES 14.94 | KES 271.57bn | Above market, favorable assumptions required |

The price of KES 10.70 is **56% above** our five-year base value of KES 6.85 per share and **34% above** our ten-year base value of KES 7.96. If the market moved to those estimates, the fall from today's price would be about **36%** and **26%**, respectively. We use different denominators for the price premium and the potential fall.

### Are the assets or cash flow underpriced?

**Assets:** We have not shown that KPC is cheap. The market price is **63% above reported book value**. Its pipelines may earn much more than their accounting value suggests, but we have no separate, verified appraisal to prove it.

**Cash flow:** The business generated cash in recent years. Yet our five- and ten-year base cases both sit below the market price. The bull cases exceed it, but they depend on better growth, project costs and future cash returns than the base assumptions.

**Verdict:** **Watch, not a proven bargain.** This judgment may change when KPC publishes enough evidence on project returns, full audited cash flow and the FY2025 accounting changes.

## Industry and Market Review

### The economics of pipeline transport

| Driver | Economic mechanism | Key investor test |
|---|---|---|
| Throughput | More cubic metres across existing lines spread fixed capital and staff costs. | Is incremental demand on an uncongested line? |
| Approved tariffs and service mix | Regulated price sets capture; longer routes and depot mix alter realizations. | Can realized price rise beyond inflation without losing volume? |
| Power and pump operation | Electricity and pumping efficiency influence cost per m³. | How does the cost base respond to fuel/energy price changes? |
| Capital replacement | Pipeline, tanks and safety systems require periodic renewal. | How much sustaining spend is economically unavoidable? |
| Expansion projects | New depots, LPG terminals, corridors and storage may raise long-run earnings. | Does incremental ROIC exceed the appropriate cost of capital? |
| Transit geography | Uganda and regional trade are important to volumes. | What happens if alternative ports/corridors gain market share? |
| Regulator and public policy | Strategic infrastructure may serve security-of-supply objectives. | Are returns to shareholders protected when public needs conflict? |
| Contingencies | Environmental remediation, claims and litigation may absorb cash. | Which liabilities are reserved, insured or contingent? |

KPC reports that fuel volume rose from about **8.11 million cubic metres in FY2021 to 9.88 million in FY2025**. That is growth of about **5.07% a year**. Revenue grew faster. Dividing revenue by volume gives about **KES 3,450 per cubic metre** in FY2021 and **KES 3,904** in FY2025. **That is not the regulated transport tariff.** It mixes routes and services and includes changes in group reporting. We also need to resolve a volume mismatch: the IPO narrative cites a 52% export share for FY2025, while the cited figures suggest 48.8%. [S01]

KPC cannot freely set its main tariffs. EPRA oversees them. An October 2025 EPRA document sought public views; it was **not** an approval. A May 2026 news report says approved rates rise from **KES 5.44 per cubic metre per kilometre in FY2025/26**, to **KES 5.53** and then **KES 5.83**. We need the official tariff notice before relying on the schedule in a final valuation. [S06][S07]

A rival would face high costs to build a similar network. Yet EPRA and KPC's customers may retain much of the benefit. A strong network does not, by itself, mean high shareholder returns.

### Demand and competing uses of energy

| Observation | Verified source result | Meaning for KPC | Limits |
|---|---|---|---|
| Petroleum import volumes, FY2025/26 | **10.881 million m³**, **+11.52%** year on year through Mombasa | Indicates positive near-term domestic and regional product flows | Imports are **not identical** to KPC billed throughput; other storage and road routes exist |
| Electric-mobility electricity consumption, FY2025/26 | **12.25 GWh**, **+143.01%** year on year | Signals a growing substitute to petrol/diesel in some road-transport segments | Small category; can't directly translate GWh to petrol/diesel displaced without fleet and usage information |
| Registered electric vehicles, as of 2025 | Government reports **39,324 cumulative EVs**, up from **1,378 in 2022** | Adoption is accelerating, particularly in motorcycles | Registration counts are **not** total fuel displacement or KPC volume |
| EPRA 2025–2029 baseline domestic forecast | Petrol **2.044bn litres (2024)** to **2.427bn (2029)**; diesel **2.608bn** to **3.099bn** | Official medium-term baseline still assumes fuel-volume growth | Earlier projection; not a realized 2029 outcome and may become outdated by transition or supply shocks |

Sources: EPRA FY2026 statistics and its 2025–2029 petroleum plan; Kenya's transport ministry. [O01][O02][O06]

In the next five years, KPC's returns may depend more on fuel routes, tariffs and project costs than on a complete shift away from petrol and diesel. Over ten years, changes in vehicle fleets and competing routes could matter much more. **This is a judgment to test, not a forecast.** We need Kenyan fuel and transport data, not a global oil headline applied to KPC.

### Related research

This company study should be read alongside the research record on **Kenya's refined-petroleum supply and transport chain**. The industry evidence provides context for fuel demand, port competition, tariff regulation and competing transport corridors. An unrelated investment-philosophy memo is not evidence about KPC's assets, earnings or future throughput.


## Future

### Ten-year business viability

The answer depends on **how much fuel East Africa needs**, **where it comes from**, and **which routes carry it**. We should not confuse a change in fuel supplier with a change in transport route.

EPRA says petroleum imports through Mombasa rose **11.52% to 10.881 million cubic metres in FY2025/26**. Electricity used under Kenya's e-mobility tariff also rose sharply—**143.01% to 12.25 GWh**—but from a low base. Both can rise at the same time. More electric vehicles do not yet prove that KPC transports less fuel. [O01][O02]

On **30 September 2026**, officials held a groundbreaking for a proposed **700,000-barrel-per-day Dangote refinery in Lamu**. This is a major planned development, not a working refinery. We have not verified its funding, opening date, transport contracts or a link to KPC's current network. [O03][O04][O05]

**What this means for value:** A refinery in Lamu could feed KPC through a new connection. It could also use a separate route and take traffic from KPC's Mombasa network. Neither outcome is proven. Our core five- and ten-year valuations do not yet assign either outcome a cash figure.

### The Dangote refinery and changes in supply routes

**Fuel made in Nigeria and shipped to Mombasa.** If oil marketers buy refined fuel from Dangote's Nigerian plant, land it in Mombasa and then use KPC, KPC may still earn the same transport fees. Who refined the fuel matters less to KPC than where it lands and how it travels inland. [O05][O07]

**Fuel refined in Lamu.** Lamu lies outside KPC's existing Mombasa-centred network. A refinery there would need a way to reach Nairobi, inland Kenya and neighbouring countries. That could be a link to KPC, a separate pipeline, road, rail or sea routes. The value to KPC depends on which routes are built and who owns them. We need signed, funded plans—not ceremony photographs or proposed capacity. [O03][O04][O05][O07]

**Scale, not a demand forecast:** Running a **700,000-barrel-per-day** crude refinery every day at full capacity would require about **40.6 million cubic metres of crude oil a year**. That is about **3.7 times** FY2026 refined-product imports through Mombasa. We are comparing different products and markets. The point is only that such a refinery would need a much wider sales and transport network. It says nothing about future output through KPC. [O01][O03]

Officials have mentioned a goal around **2030**, but commissioning dates, utilization, yields, customers and routes remain unknown. [O03][O04]

### How KPC could gain or lose traffic

| Potential structural change | Mechanism | Possible KPC upside | Possible KPC downside | Verification required |
|---|---|---|---|---|
| Nigeria-sourced refined fuel into **Mombasa** | Source of imported fuel changes | Stable or higher KPC throughput if fuel remains on same corridors | Little direct benefit if regional demand stagnates | Import port, landing volumes and actual KPC billings |
| **Lamu** refinery with KPC interconnection | Kenyan/refined supply enters existing KPC distribution | New route billings, storage, better capacity use | Large link capex, financing and tariff-regulatory risk | Signed interconnect design, capex, ownership and tariffs |
| **Lamu** refinery with separate inland corridor | Fuel moves independently of Mombasa route | Possible cross-network partnerships | Lower volume/capacity utilization on KPC's legacy network | Permits, maps, competitive tariffs, contracts and off-take |
| **Uganda/Tanzania** refining and other corridors | Landlocked markets source product closer to home | KPC could compete on quality or price | Transit volumes may be diverted from Kenyan western depots | Refinery commissioning and country-by-country market shares |
| Accelerated **electrification** | Road-fuel intensity per passenger-/tonne-km falls | KPC may diversify into LPG/other logistics **only if technically feasible** | Long-run fuel throughput and terminal value weaken | Vehicle fleet, mileage, fuel mix, product-level demand |
| Delayed transition / regional volume growth | Population, freight and aviation grow | Better utilization of existing network | Need for greater capex and resilience | Demand by grade, route, terminal, tariff and capex |

For shareholders, the key measure is not East Africa's total fuel demand. It is **the fuel that moves through KPC's pipes, at the tariffs KPC earns, after the costs of maintaining and expanding those pipes**.

### Measures to track each year

Five disclosed metrics are the minimum research dataset:

1. **Throughput by route and customer destination**: m³ on Mombasa–Nairobi and the western network; domestic versus transit, with source definitions reconciled.
2. **Effective realised tariff / unit economics**: transport/storage revenue by route divided by corresponding billable units, explicitly distinct from an approved headline tariff.
3. **Competitive route evidence**: new refineries, port facilities, rail and pipeline links; approved projects versus funded construction versus commissioned assets.
4. **Fuel demand by grade and electrification**: petrol, diesel, jet fuel, LPG, kerosene, and the vehicle/freight mix; use volumes, not anecdotes.
5. **Capital efficiency**: maintenance capex, incremental project capex, financing, associated incremental cash flows, ROIC versus cost of capital, and asset impairment/decommissioning indicators.

The notes may reveal changes before they show up in profit. Check events after the reporting date, revenue by service, future spending, asset write-downs, useful lives, closure costs and major fuel transport contracts.

### How structural risks affect the valuation

The workbook uses a rough measure of cash available to shareholders and discounts it at **11%**. It does not yet model each pipeline route on its own.

A stronger model would forecast **volume by route**, multiply it by the **fees actually earned**, then deduct running costs, taxes, maintenance, new projects and net debt repayments. We would discount the resulting equity cash flows over five and ten years.

Until those records are available, we use a simple stress test. A permanent **KES 1 billion drop in annual equity cash flow starting in FY2032** would cut present value by about **KES 5.40 billion**, or **KES 0.30 per share**, if the cash loss continued indefinitely and we used 11%. This is **not a forecast** of Dangote's effect. The five-year model captures it in the value after year five; the ten-year model captures it in years 6–10 and thereafter. We must not count it twice. A new KPC link to Lamu would need its own cost and return forecast.

**Scenario design:**

| Scenario | Years 1–5 (FY2027–2031) | Years 6–10 (FY2032–2036) | Key valuation changes |
|---|---|---|---|
| Integrated regional supply | Continue tracking existing demand; no Lamu benefit assumed until contracted | Lamu supplies connected KPC routes if commissioned | Incremental route cash receipts less link capex and operating cost |
| Separate-corridor competition | No automatic 2026 volume loss from groundbreaking | Transit or domestic volumes migrate to alternate coastal routes | Lower throughput, possible legacy asset impairment and fixed-cost deleveraging |
| Faster electrification | Monitor conversion in motorcycles/buses and retail fuel | Greater exposure as fleet replacement accumulates | Slower petrol/diesel route volumes; lower terminal growth |
| Demand resilience | Continued transport/freight, aviation and regional energy use | Stable or rising throughput where network is competitive | Stable utilization, but test required reinvestment |

We have not assigned odds or prices to these cases. There is no verified KPC–Lamu contract, rival-route market-share forecast or detailed fuel-demand study to support one.

### What this means for shareholders

**The energy shift is a real long-term risk, not proof of an imminent collapse.** Kenya's fuel flows are still growing, and electric vehicles are gaining ground. We need to track how many litres of fuel EVs actually replace on KPC's routes.

**Lamu can help or harm KPC.** A profitable link to the proposed refinery could bring new business. A separate route could take away volume. Neither case is supported by a signed agreement in our reviewed evidence. The refinery itself still faces funding, construction and customer risks.

**Valuation verdict:** We do **not** have proof that the market price is cheap once we allow for these risks. The five- and ten-year base values remain provisional. We should not change the price target by guessing one broad “transition discount.” First, we need a route-by-route cash forecast.

### What evidence we still need

| Priority | Needed evidence | Why it changes the valuation |
|---|---|---|
| High | KPC signed FY2026 annual report and latest corporate investment plan | Asset useful-life/impairment, capex, debt and exposure updates |
| High | Dangote Lamu project financing/FID, engineering works, product off-take agreements, corridor strategy | Whether a real output source enters KPC or a rival system |
| High | Kenya/EPRA route and destination-specific pipeline data; updated regulated tariff schedule | Price × volume cash earnings by route |
| High | Uganda and Tanzania refinery construction status and transit demand allocation | Western transit competition and potential KPC volume loss |
| Medium | Monthly product demand, EV fleet usage, road freight and aviation statistics | Real fuel-displacement sensitivity by segment |
| Medium | Lamu interconnection feasibility, project IRR, ownership and tariff framework | Incremental KPC value creation versus capital dilution |

## Conclusion

### Strengths, risks and ways the thesis could fail

**Strengths:** KPC's pipes, tanks and depots would be costly to copy. They help keep fuel moving across Kenya and into neighbouring markets. KPC reports little interest-bearing debt today, and added storage or handling services could bring in revenue. [S01][S09]

**Risks:** EPRA limits tariffs. Projects cost money and can run late. KPC may borrow more to build them. Other ports and routes may take traffic. Power costs, outages, environmental claims and contract decisions can also cut cash flow. In the longer run, new transport technology may reduce fuel demand. [S01][S06][S07]

**What would weaken this thesis?** Profit that repeatedly fails to turn into cash; new projects that earn less than they cost; unexplained account changes; environmental costs above provisions; borrowing KPC cannot service; or lost transit business to other routes.

### Current investment verdict

| Question | Current assessment |
|---|---|
| Is it an understandable business? | **Yes**, primarily regulated pipeline transport/storage, with identifiable economic drivers. |
| Is its network strategically useful? | **Yes**, though strategic importance does not guarantee investor returns. |
| Are recent accounts profitable and liquid? | **Yes on disclosed FY2026 summary**, with low present borrowings and strong current ratio. |
| Is the historical five-year growth fully organic/comparable? | **No**: 2024 KPRL consolidation and FY2025 accounting conflict must be handled. |
| Are distributable equity cash flows reliably forecast? | **Not yet**: capex, financing, statement classification and project return information are insufficient. |
| Is KPC definitively undervalued at 10.70? | **Not established**. The provisional base scenarios are lower than price, but highly uncertain. |
| Publishable as a final price target? | **No**. Needs audit reconciliation and capital-spending underwriting. |

**Next research task:** Obtain the full FY2026 signed statements, the notes explaining the FY2025 changes and the latest approved spending and loan plans. Then rebuild the cash-flow model and test whether each new project earns enough to cover the capital it uses.

## Notes

The following items remain **unverified, incomplete or assumption-dependent** at publication. They are disclosed deliberately rather than presented as settled facts. This is an independently published analysis, not an audit opinion or a definitive fair-value estimate.

1. **FY2025 accounts do not yet reconcile.** The IPO reporting accountant's compiled FY2025 group profit of approximately **KES 7.49bn** differs from the **KES 10.24bn** FY2025 group comparative published with FY2026 results. The parent-company figures also differ between the original FY2025 audit and IPO compilation. We have not completed the line-by-line adjustment and restatement bridge. Do not combine these profit series to calculate growth. [S01][S02][S16]
2. **Some FY2026 numbers rely on secondary reporting.** The official results listing was identified, but the signed full FY2026 statements, their notes, and every line of the condensed announcement could not be independently examined in this research pass. **KES 42.98bn** revenue, **KES 11.58bn** profit, **KES 17.39bn** operating cash flow, **KES 119.33bn** equity and related metrics should be rechecked against the issuer's full audited report. [S02][S03][S04][S12][S15]
3. **Historical growth is not wholly comparable.** KPRL entered the group in FY2024 and the IPO compilation adjusts previously issued financials. The five-year financial presentation should not be mistaken for an audited, organic like-for-like growth series. Environmental provisions, tax adjustments and asset valuation disclosures also require continued review. [S01][S14][S16]
4. **Market price and share count are dated inputs.** The **KES 10.70** market reference is for **13 November 2026**, not the publication-date or current trading price. The derived approximately **KES 194.45bn** equity market value, price-to-book ratio and per-share estimates depend on the price and issued-share assumptions used in the report. Recheck against current NSE disclosures before taking a decision. [S05][S13]
5. **Valuation outputs are scenarios, not verified intrinsic value.** The **11% discount rate**, five- and ten-year base values of **KES 124.57bn** and **KES 144.70bn**, growth, reinvestment, borrowing and terminal assumptions are analyst estimates. They depend particularly on spending, financing and cash-flow data that remain incomplete. The sensitivity cases do not represent probabilities or price targets.
6. **Capital spending forecasts are not actual expenditure.** The IPO's approximately **KES 110.32bn** FY2026–FY2030 fixed-asset/intangible spending plan was prospective. We have not independently verified the latest approved project-by-project capital budget, full FY2026 capex cash payments, financing terms or expected returns. [S01]
7. **Lamu refinery and regional-route impacts are uncertain.** Reported groundbreaking and proposals do not prove financing close, construction completion, KPC interconnections, signed transport commitments or future diversion of volumes. The report's upside/downside route analysis is conditional, not a forecast of an operating refinery. [O03][O04][O05][O08][O09]
8. **Audit findings, ownership and asset claims need follow-up.** The complete FY2025 Auditor-General opinion and subsequent FY2026 audit notes have not been independently reviewed in full. Current beneficial ownership, environmental liabilities, contingencies, title issues and the realizable value of infrastructure assets require direct primary-document confirmation. [S01][S14][S16]

**Interpretation:** Where a figure is described as *reported*, that means it appears in an identified disclosure or attributed coverage—not that Meyo Insights has audited it. *Derived* indicates our arithmetic from stated inputs; *forecast*, *scenario* and *provisional* indicate judgment rather than independently verified facts. We may revise conclusions as stronger evidence arrives.

## References

### Financial, company and market sources

[S01] **KPC IPO Information Memorandum**, 17 Jan 2026, selected financials pp. 83–86, operating review pp. 87–94, Appendix V reporting accountants historical statements and prospective FY2026–FY2030 cash-flow plan: https://www.kpc.co.ke/wp-content/uploads/2026/01/Kenya_Pipeline_Company_IPO-4.pdf  
[S02] **KPC official FY2026 audited results listing**, 14 Oct 2026 (the linked file was not fully retrievable in this review): https://www.kpc.co.ke/wpfd_file/consolidated-audited-financial-results-fy-2025-26-2/  
[S03] **Cytonn weekly analysis of FY2026 KPC results**, Oct 2026: https://cytonnreport.com/research/kenyas-balance-of-1  
[S04] **Business Daily**, 14 Oct 2026, profit and dividend reporting: https://www.businessdailyafrica.com/bd/corporate/companies/how-kpc-owners-will-share-sh5-8bn-as-profits-rise-13pc-5631744  
[S05] **KenyaStocks**, market close 13 Nov 2026: https://kenyastocks.co.ke/stocks/kpc  
[S06] **EPRA**, public consultation on *proposed* pipeline tariffs, 10 Oct 2025: https://www.epra.go.ke/public-consultation-proposed-kenya-pipeline-transportation-and-secondary-storage-tariffs  
[S07] **The Standard**, report of EPRA approved rate schedule, May 2026: https://standardmedia.co.ke/business/business/article/2001548308/epra-makes-marginal-hike-on-pipeline-tariff-piles-pressure-on-consumers  
[S08] **Privatization Authority**, official IPO record: https://privatization.go.ke/success-stories/kenya-pipeline-company-ipo/  
[S09] **EPRA**, biannual petroleum statistics FY2025/26: https://epra.go.ke/sites/default/files/2026-03/Biannual%20Statistics%20Report%202025-2026.pdf  
[S10] **KPC** annual reports archive: https://www.kpc.co.ke/annual-reports/  
[S12] **Pulse Kenya**, FY2026 financial summary Oct 2026: https://www.pulse.co.ke/story/kenya-pipeline-posts-sh116-b-net-profit-as-revenue-rises-9percent-2026101408412743025


[S13] **StockAnalysis / AfricanFinancials**, market capitalisation at 13 Nov 2026 (cross-check): https://stockanalysis.com/quote/nase/KPC/market-cap/ ; https://africanfinancials.com/company/ke-kpc/  
[S14] **KPC FY2024 full annual report**, accounting policies and Auditor-General section (the signed opinion is not readable in the web extraction reviewed): https://www.kpc.co.ke/download/72/annual-reports/13301/fy2024-annual-report-financial-statements.pdf  
[S15] **Investreet Financial**, 14 October 2026 report of FY2026 cash flows, assets, equity and FY2025 comparator: https://investreetfinancial.com/kenya-pipeline-company-financial-results-2026/  
[S16] **Kenya Parliament repository**, full FY2025 Auditor-General report, issued March 2026 (identified, but full opinion text has not been independently inspected): https://libraryir.parliament.go.ke/items/3db9fb13-5f4b-4ab2-9e00-413e3353c34e

### Industry and long-term outlook sources

- **[O01] EPRA, Energy & Petroleum Statistics Report FY2025/26** (published September 2026): petroleum import volumes, annual change, e-mobility electricity consumption, physical coastal petroleum infrastructure. https://epra.go.ke/sites/default/files/2026-09/Energy%20%26%20Petroleum%20Statistics%20Report%202026.pdf
- **[O02] EPRA, Petroleum Development Plan 2025–2029** (June 2025, publicly posted October 2025): baseline demand forecasts by product and regulatory transition discussion. https://epra.go.ke/sites/default/files/2025-10/Petroleum%20Development%20Plan%20for%20the%20Medium%20Term%20Period%202025%20to2029.pdf
- **[O03] Kenya Ministry of Foreign Affairs** (1 October 2026): Lamu petroleum and petrochemicals zone groundbreaking and proposed 700,000 bpd capacity. https://mfa.go.ke/president-ruto-dangote-launch-east-africa-petroleum-and-petrochemicals-zone-lamu
- **[O04] Kenya State Department for Transport** (30 September 2026): construction-launch details, equipment on site and intended transport/logistics role. https://www.transport.go.ke/index.php/dangote-refinery-groundbreaking-marks-new-chapter-lamus-economic-development
- **[O05] Kenya Pipeline Company**, IPO Information Memorandum (17 January 2026), network map and demand drivers. https://www.kpc.co.ke/wp-content/uploads/2026/01/Kenya_Pipeline_Company_IPO-4.pdf
- **[O06] Ministry of Roads & Transport, e-Mobility Policy launch** (3 February 2026): 39,324 cumulative EV registrations at end-2025. https://www.transport.go.ke/node/730
- **[O07] Ministry of Petroleum**, published pipeline network and depot infrastructure. https://petroleum.go.ke/index.php/petroleum-information
- **[O08] Reuters**, 7 July 2026: Dangote's announced Lamu refinery financing intention; investment/funding details not a verified financed budget. https://www.reuters.com/business/energy/dangote-fund-proposed-kenya-refinery-with-cash-bonds-an-ipo-2026-07-07/
- **[O09] Government of Uganda**, 5 October 2026: proposed complementarity of regional refinery projects and Uganda's own refining intentions. https://www.op.go.ug/news-updates/news-and-updates/general/news-and-updates/president-museveni-backs-regional-oil-0

### Editorial record and corrections

This is Meyo Insights Issue 001, first published 18 November 2026. It develops the v6.0 analysis from evidence available at the research cut-off of 14 November 2026; it is **not** a new audit of the financial statements. Material corrections will be dated and explained in future revisions rather than silently changing the investment conclusion. Readers can submit corrections through [@meyo_insights](https://x.com/meyo_insights).