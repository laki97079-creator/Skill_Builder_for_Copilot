#!/usr/bin/env python3
"""Tests for single-shot content extraction (skill_seekers.cli.extractor)."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from skill_seekers.cli import extractor


SAMPLE_HTML = """\
<html>
<head><title>Sample Docs</title></head>
<body>
<nav><a href="/nav">Nav link that should not dominate</a></nav>
<article>
<h1>Getting Started</h1>
<h2>Installation</h2>
<p>This is a longer paragraph describing how to install the package step by step.</p>
<p>Another detailed paragraph explaining configuration options and usage patterns here.</p>
<pre><code class="language-python">def hello():\n    print("hi")\n</code></pre>
<table><tr><th>Name</th><th>Value</th></tr><tr><td>foo</td><td>bar</td></tr></table>
<a href="https://example.com/docs/next">Next page</a>
</article>
</body>
</html>
"""


class TestDetectMainContent(unittest.TestCase):
    def test_auto_detect_prefers_article(self):
        soup = extractor._parse_html(SAMPLE_HTML)
        elem, selector = extractor.detect_main_content(soup)
        self.assertEqual(selector, "article")
        self.assertIn("Getting Started", elem.get_text())

    def test_preferred_selector_wins(self):
        soup = extractor._parse_html(SAMPLE_HTML)
        elem, selector = extractor.detect_main_content(soup, preferred_selector="body")
        self.assertEqual(selector, "body")

    def test_falls_back_to_document(self):
        soup = extractor._parse_html("<html><body><p>hi</p></body></html>")
        with patch.object(
            extractor, "DEFAULT_CONTENT_SELECTORS", ["article", "main"]
        ):
            elem, selector = extractor.detect_main_content(soup)
        self.assertEqual(selector, "document")


class TestExtractFromSoup(unittest.TestCase):
    def test_full_extraction(self):
        soup = extractor._parse_html(SAMPLE_HTML)
        data = extractor.extract_from_soup(soup, source="https://example.com/x")

        self.assertEqual(data["title"], "Sample Docs")
        self.assertEqual(data["selector_used"], "article")
        self.assertTrue(any(h["text"] == "Getting Started" for h in data["headings"]))
        self.assertIn("install the package", data["content"])
        self.assertEqual(data["code_blocks_count"], 1)
        self.assertEqual(data["code_samples"][0]["language"], "python")
        self.assertEqual(data["tables_count"], 1)
        self.assertEqual(data["tables"][0][0], ["Name", "Value"])
        self.assertIn("https://example.com/docs/next", data["links"])

    def test_deduplicates_code_blocks(self):
        html = (
            "<article><h1>T</h1>"
            "<p>This paragraph is long enough to be kept in the output text.</p>"
            "<pre><code>print('hello world example code')</code></pre>"
            "<pre>print('hello world example code')</pre>"
            "</article>"
        )
        data = extractor.extract_from_soup(extractor._parse_html(html), source="x")
        self.assertEqual(data["code_blocks_count"], 1)

    def test_title_falls_back_to_h1(self):
        html = "<article><h1>My Heading</h1><p>" + ("word " * 20) + "</p></article>"
        data = extractor.extract_from_soup(
            extractor._parse_html(html), source="x"
        )
        self.assertEqual(data["title"], "My Heading")


class TestLanguageDetection(unittest.TestCase):
    def test_class_based_detection(self):
        soup = extractor._parse_html(
            '<article><pre><code class="lang-javascript">const x = 1;</code></pre></article>'
        )
        elem = soup.select_one("code")
        self.assertEqual(
            extractor.detect_language_from_element(elem, "const x = 1;"), "javascript"
        )

    def test_heuristic_detection(self):
        soup = extractor._parse_html("<article><pre>some code</pre></article>")
        elem = soup.select_one("pre")
        self.assertEqual(
            extractor.detect_language_from_element(elem, "using System;\nclass A {}"),
            "csharp",
        )
        self.assertEqual(
            extractor.detect_language_from_element(elem, "just some prose here"),
            "unknown",
        )


class TestFormatting(unittest.TestCase):
    def setUp(self):
        soup = extractor._parse_html(SAMPLE_HTML)
        self.data = extractor.extract_from_soup(soup, source="https://example.com/x")

    def test_markdown(self):
        md = extractor.to_markdown(self.data)
        self.assertIn("# Sample Docs", md)
        self.assertIn("```python", md)
        self.assertIn("| Name | Value |", md)

    def test_text(self):
        text = extractor.to_text(self.data)
        self.assertIn("Sample Docs", text)
        self.assertIn("[python]", text)

    def test_json_round_trip(self):
        out = extractor.format_output(self.data, "json")
        self.assertEqual(json.loads(out)["title"], "Sample Docs")

    def test_bad_format(self):
        with self.assertRaises(ValueError):
            extractor.format_output(self.data, "yaml")


class TestSources(unittest.TestCase):
    def test_extract_from_url(self):
        fake_response = MagicMock()
        fake_response.text = SAMPLE_HTML
        fake_response.raise_for_status = MagicMock()
        with patch.object(extractor, "requests") as mock_requests:
            mock_requests.get.return_value = fake_response
            data = extractor.extract_from_url("https://example.com/docs")
        self.assertEqual(data["title"], "Sample Docs")
        self.assertEqual(data["source"], "https://example.com/docs")

    def test_extract_from_url_rejects_scheme(self):
        with self.assertRaises(ValueError):
            extractor.extract_from_url("ftp://example.com/file")

    def test_extract_from_html_file(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".html", delete=False, encoding="utf-8"
        ) as f:
            f.write(SAMPLE_HTML)
            path = f.name
        try:
            data = extractor.extract_from_html_file(path)
            self.assertEqual(data["title"], "Sample Docs")
        finally:
            os.unlink(path)

    def test_extract_from_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            extractor.extract_from_html_file("/nonexistent/page.html")

    def test_extract_from_pdf(self):
        fake_result = {
            "pages": [
                {
                    "text": "Hello PDF world",
                    "headings": [{"level": "h1", "text": "Intro"}],
                    "code_samples": [{"code": "print(1)", "language": "python"}],
                }
            ],
            "total_pages": 1,
            "total_tables": 0,
        }
        fake_extractor = MagicMock()
        fake_extractor.extract_all.return_value = fake_result
        fake_cls = MagicMock(return_value=fake_extractor)

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            path = f.name
        try:
            with patch.dict(
                sys.modules,
                {"skill_seekers.cli.pdf_extractor_poc": MagicMock(PDFExtractor=fake_cls)},
            ):
                with patch.object(Path, "exists", return_value=True):
                    data = extractor.extract_from_pdf(path)
            self.assertEqual(data["code_blocks_count"], 1)
            self.assertEqual(data["total_pages"], 1)
            self.assertIn("Hello PDF", data["content"])
        finally:
            os.unlink(path)


class TestCli(unittest.TestCase):
    def test_cli_url_to_stdout(self, capsys=None):
        fake_response = MagicMock()
        fake_response.text = SAMPLE_HTML
        fake_response.raise_for_status = MagicMock()
        with patch.object(extractor, "requests") as mock_requests:
            mock_requests.get.return_value = fake_response
            rc = extractor.main(["--url", "https://example.com/x", "--format", "text"])
        self.assertEqual(rc, 0)

    def test_cli_requires_source(self):
        with self.assertRaises(SystemExit):
            extractor.main([])

    def test_cli_writes_output_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "out.md")
            fake_response = MagicMock()
            fake_response.text = SAMPLE_HTML
            fake_response.raise_for_status = MagicMock()
            with patch.object(extractor, "requests") as mock_requests:
                mock_requests.get.return_value = fake_response
                rc = extractor.main(
                    ["--url", "https://example.com/x", "--output", out]
                )
            self.assertEqual(rc, 0)
            self.assertIn("# Sample Docs", Path(out).read_text(encoding="utf-8"))

    def test_cli_bad_url_returns_1(self):
        with patch.object(
            extractor, "fetch_url", side_effect=ValueError("bad url")
        ):
            rc = extractor.main(["--url", "ftp://x", "--format", "json"])
        self.assertEqual(rc, 1)

    def test_unified_cli_wiring(self):
        from skill_seekers.cli.main import create_parser

        args = create_parser().parse_args(
            ["extract", "--url", "https://example.com/x", "--format", "json"]
        )
        self.assertEqual(args.command, "extract")
        self.assertEqual(args.url, "https://example.com/x")

        with patch(
            "skill_seekers.cli.extractor.main", return_value=0
        ) as mock_extract:
            from skill_seekers.cli.main import main as unified_main

            rc = unified_main(
                ["extract", "--url", "https://example.com/x", "--format", "json"]
            )
            self.assertEqual(rc, 0)
            mock_extract.assert_called_once()


if __name__ == "__main__":
    unittest.main()
