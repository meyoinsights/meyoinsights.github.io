"""Verify the public Markdown -> PDF publishing contract, without deploying."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("editorial_pdf", ROOT / "scripts" / "build_publication_pdfs.py")
publisher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publisher)

class EditorialPdfTests(unittest.TestCase):
    def test_pdf_from_approved_public_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "src/pages/blog/sample-research.md"
            source.parent.mkdir(parents=True)
            source.write_text("""---
layout: ../../layouts/ArticleLayout.astro
title: Sample Research Report
description: Evidence and limitations reviewed for print.
pubDate: 2026-11-17
author: widdzz
category: Company research
---
## Evidence

The company reported **KES 10 billion** for the test period, with a [source](https://example.org/).

| Measure | FY2025 |
| --- | ---: |
| Revenue | KES 10bn |

## Sources
[Primary filing](https://example.org/).
""",encoding="utf-8")
            dest = root / "public/reports/sample-research.pdf"
            publisher.generate(source, dest, ROOT / "assets/editorial-print.css")
            report = PdfReader(str(dest))
            self.assertGreaterEqual(len(report.pages), 2)
            cover = report.pages[0].extract_text()
            self.assertIn("Sample Research Report", cover)
            self.assertIn("widdzz".upper(), cover)

    def test_reject_unapproved_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "private.md"
            path.write_text("""---
title: Draft Research
description: Not approved
layout: ../../layouts/ArticleLayout.astro
pubDate: 2026-11-17
author: widdzz
draft: true
---
This must not publish.
""",encoding="utf-8")
            with self.assertRaises(ValueError):
                publisher.parse_article(path)

    def test_reject_unframed_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "private.md"
            path.write_text("# Unreviewed research packet\n\nDraft text",encoding="utf-8")
            with self.assertRaises(ValueError):
                publisher.parse_article(path)


    def test_issue_001_notes_and_references_order(self):
        source = ROOT / "src/pages/blog/kenya-pipeline-is-share-price-justified.md"
        metadata, body = publisher.parse_article(source)
        self.assertEqual(metadata["issue"], "001")
        self.assertEqual(metadata["ticker"], "KPC")
        self.assertIn("## Notes\n", body)
        self.assertIn("## References\n", body)
        self.assertLess(body.index("## Notes\n"), body.index("## References\n"))
        self.assertIn("KES 124.57 billion", body)
        self.assertIn("KES 144.70 billion", body)
        self.assertIn("KES 10.70", body)
        self.assertIn("[S01]", body)
        self.assertIn("[O09]", body)
        self.assertGreater(len(body), 40000)

    def test_publication_pdf_metadata_and_reader_link(self):
        meta = {
            "title": "Example", "description": "Test", "author": "widdzz",
            "pubDate": "2026-11-18", "issue": "001", "exchange": "NSE",
            "ticker": "KPC", "researchAsOf": "14 November 2026",
            "marketReference": "KES 10.70 · 13 November 2026",
            "publicationStatus": "Independent analysis",
            "preflight": {"reviewedAt":"2026-11-18","lookbackStart":"2026-08-20",
                "reviewCategories": {k:["T01"] for k in (
                    "ownership","governance","leadership","corporate_actions",
                    "strategic_transactions","regulatory","financials")},
                "materialEvents": [], "openVerification": "Verified only for test"},
        }
        rendered = publisher.build_html(meta, "## Notes\n\nUnresolved.\n\n## References\n\n[T01] Example.")
        self.assertIn("ISSUE 001", rendered)
        self.assertIn("NSE: KPC", rendered)
        self.assertIn("14 November 2026", rendered)
        self.assertIn("https://x.com/meyo_insights", rendered)


    def test_issue_001_exhibits_are_evidence_backed(self):
        source = ROOT / "src/pages/blog/kenya-pipeline-is-share-price-justified.md"
        meta, body = publisher.parse_article(source)
        publisher.assert_evidence(meta, body)
        rendered = publisher.build_html(meta, body)
        self.assertIn('class="brief-page"', rendered)
        self.assertIn('class="cover-band"', rendered)
        self.assertIn('One financial year. Two profit figures.', rendered)
        self.assertIn('A price is a fact. A value is a model.', rendered)
        self.assertIn('https://x.com/meyo_insights', rendered)
        self.assertEqual(rendered.count('class="evidence-exhibit '), 4)
        self.assertIn('## Notes', body)
        self.assertIn('## References', body)

    def test_reject_unsupported_chart_value(self):
        metadata = {
            "editorial": {"exhibits": [
                {"kind": "bar", "title": "Unsupported", "source": "[S01]",
                 "caveat": "Draft", "beforeHeading": "Evidence",
                 "data": [{"label": "FY", "value": 999999.9}]}
            ]}
        }
        with self.assertRaises(ValueError):
            publisher.assert_evidence(metadata, "## Evidence\n\n[S01] Source.")

    def test_equity_preflight_catches_missing_ownership_review(self):
        meta, body = publisher.parse_article(
            ROOT / "src/pages/blog/kenya-pipeline-is-share-price-justified.md"
        )
        self.assertEqual(meta["preflight"]["materialEvents"][0]["id"],
                         "KPC-2026-10-19-BLOCK-TRADE")
        publisher.validate_publication_preflight(meta, body)
        broken = dict(meta)
        broken["preflight"] = dict(meta["preflight"])
        broken["preflight"]["reviewCategories"] = dict(meta["preflight"]["reviewCategories"])
        del broken["preflight"]["reviewCategories"]["ownership"]
        with self.assertRaisesRegex(ValueError, "ownership"):
            publisher.validate_publication_preflight(broken, body)

    def test_equity_preflight_catches_outdated_review(self):
        meta, body = publisher.parse_article(
            ROOT / "src/pages/blog/kenya-pipeline-is-share-price-justified.md"
        )
        expired = dict(meta)
        expired["preflight"] = dict(meta["preflight"], reviewedAt="2026-11-01")
        with self.assertRaises(ValueError):
            publisher.validate_publication_preflight(expired, body)

    def test_equity_preflight_catches_missing_event_evidence(self):
        meta, body = publisher.parse_article(
            ROOT / "src/pages/blog/kenya-pipeline-is-share-price-justified.md"
        )
        altered = dict(meta)
        altered["preflight"] = dict(meta["preflight"], materialEvents=[
            {"id":"UNSUPPORTED","eventDate":"2026-10-19","sourceIds":["M99"],
             "disposition":"Undisclosed"}
        ])
        with self.assertRaisesRegex(ValueError, "M99"):
            publisher.validate_publication_preflight(altered, body)

if __name__ == "__main__":
    unittest.main()
