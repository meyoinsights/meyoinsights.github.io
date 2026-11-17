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

if __name__ == "__main__":
    unittest.main()
