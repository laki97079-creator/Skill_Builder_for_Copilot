#!/usr/bin/env python3
"""
Single-shot content extractor.

Extracts clean, structured content from a single source without crawling:
a documentation URL, a local HTML file, or a PDF file.

This fills the gap between full scraping (``scrape`` crawls whole sites)
and skill building: quickly inspect what would be extracted from one page
before committing to a full scrape, or convert a single page/document
to Markdown/JSON/text.

Usage:
    skill-seekers extract --url https://example.com/docs/intro
    skill-seekers extract --url https://example.com/docs/intro -o intro.md
    skill-seekers extract --url https://example.com/docs/intro --format json
    skill-seekers extract --file page.html --selector article
    skill-seekers extract --pdf manual.pdf -o manual.md
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:  # pragma: no cover
    BeautifulSoup = None  # type: ignore
    Tag = Any  # type: ignore


DEFAULT_TIMEOUT = 30

#: Selectors tried in order when no explicit selector is given.
#: The selector yielding the most text wins.
DEFAULT_CONTENT_SELECTORS = [
    "article",
    "main",
    "div[role='main']",
    "[role='main']",
    "div.content",
    "div.documentation",
    "div.body",
    "div.document",
    "#main-content",
    "#content",
    ".content",
    "body",
]

CODE_BLOCK_SELECTORS = ["pre code", "pre", "code[class*='language-']"]

KNOWN_LANGUAGES = [
    "javascript", "typescript", "java", "xml", "html", "python", "bash",
    "cpp", "c", "csharp", "go", "rust", "php", "ruby", "swift", "kotlin",
    "sql", "yaml", "json", "markdown", "css", "scss", "shell", "powershell",
    "r", "scala", "dart", "perl", "lua", "jsx", "tsx", "vue", "gdscript",
]


def _clean_text(text: str) -> str:
    """Collapse whitespace and strip."""
    return re.sub(r"\s+", " ", text or "").strip()


def detect_language_from_element(elem: Any, code: str) -> str:
    """Detect the programming language of a code sample.

    Checks CSS classes (``language-*``, ``lang-*``, bare names) on the
    element and its ``<pre>`` parent, then falls back to heuristics.
    """
    def from_classes(classes: List[str]) -> Optional[str]:
        for cls in classes:
            cls_clean = re.sub(r"[^\w-]", "", cls)
            if "language-" in cls_clean:
                return cls_clean.replace("language-", "")
            if "lang-" in cls_clean:
                return cls_clean.replace("lang-", "")
            if cls_clean in KNOWN_LANGUAGES:
                return cls_clean
        return None

    lang = from_classes(elem.get("class", []) or [])
    if lang:
        return lang
    parent = getattr(elem, "parent", None)
    if parent is not None and getattr(parent, "name", "") == "pre":
        lang = from_classes(parent.get("class", []) or [])
        if lang:
            return lang

    if "import " in code and "from " in code:
        return "python"
    if "const " in code or "let " in code or "=>" in code:
        return "javascript"
    if "func " in code and "var " in code:
        return "gdscript"
    if "def " in code and ":" in code:
        return "python"
    if "#include" in code or "int main" in code:
        return "cpp"
    if "using System" in code or "namespace " in code:
        return "csharp"
    return "unknown"


def detect_main_content(
    soup: Any, preferred_selector: Optional[str] = None
) -> Tuple[Any, str]:
    """Pick the best main-content element.

    Returns a ``(element, selector_used)`` tuple. When ``preferred_selector``
    matches it is used directly; otherwise every selector in
    :data:`DEFAULT_CONTENT_SELECTORS` is scored by extracted text length and
    the best one wins.
    """
    if preferred_selector:
        found = soup.select_one(preferred_selector)
        if found is not None:
            return found, preferred_selector

    best_elem = None
    best_selector = ""
    candidates: List[Tuple[Any, str, int]] = []
    for selector in DEFAULT_CONTENT_SELECTORS:
        try:
            elem = soup.select_one(selector)
        except Exception:
            continue
        if elem is None:
            continue
        length = len(_clean_text(elem.get_text(" ", strip=True)))
        if length > 0:
            candidates.append((elem, selector, length))

    if not candidates:
        return soup, "document"

    max_length = max(length for _, _, length in candidates)
    # Prefer the most specific (earliest-listed) selector whose text is
    # close to the maximum, so a focused <article> beats a <body> that
    # merely wraps it plus navigation chrome.
    threshold = max(50, int(max_length * 0.8))
    for elem, selector, length in candidates:
        if length >= threshold:
            return elem, selector

    best = max(candidates, key=lambda c: c[2])
    return best[0], best[1]


def extract_from_soup(
    soup: Any, source: str, preferred_selector: Optional[str] = None
) -> Dict[str, Any]:
    """Extract structured content from a parsed HTML document."""
    main, selector_used = detect_main_content(soup, preferred_selector)

    title = ""
    title_elem = soup.select_one("title")
    if title_elem:
        title = _clean_text(title_elem.get_text())
    if not title:
        h1 = main.find("h1") if hasattr(main, "find") else None
        if h1 is not None:
            title = _clean_text(h1.get_text())

    headings: List[Dict[str, str]] = []
    for h in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        text = _clean_text(h.get_text())
        if text:
            headings.append({
                "level": h.name,
                "text": text,
                "id": h.get("id", ""),
            })

    code_samples: List[Dict[str, str]] = []
    seen: set = set()
    for code_selector in CODE_BLOCK_SELECTORS:
        for code_elem in main.select(code_selector):
            code = code_elem.get_text()
            if len(code.strip()) <= 10:
                continue
            digest = hash(code.strip())
            if digest in seen:
                continue
            seen.add(digest)
            code_samples.append({
                "code": code.strip(),
                "language": detect_language_from_element(code_elem, code),
            })

    paragraphs: List[str] = []
    for p in main.find_all("p"):
        text = _clean_text(p.get_text())
        if text and len(text) > 20:
            paragraphs.append(text)
    content = "\n\n".join(paragraphs)

    links: List[str] = []
    for link in soup.find_all("a", href=True):
        href = link["href"].split("#")[0].strip()
        if href and href not in ("", "/") and href not in links:
            links.append(href)

    tables: List[List[List[str]]] = []
    for table in main.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [
                _clean_text(c.get_text())
                for c in tr.find_all(["th", "td"])
            ]
            if any(cells):
                rows.append(cells)
        if rows:
            tables.append(rows)

    return {
        "source": source,
        "title": title,
        "selector_used": selector_used,
        "headings": headings,
        "content": content,
        "char_count": len(content),
        "code_samples": code_samples,
        "code_blocks_count": len(code_samples),
        "tables": tables,
        "tables_count": len(tables),
        "links": links[:200],
        "links_count": len(links),
    }


def fetch_url(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Fetch a URL and return its HTML text."""
    if requests is None:
        raise RuntimeError("The 'requests' package is required for --url extraction")
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Unsupported URL scheme: {url!r} (expected http/https)")
    headers = {"User-Agent": "Mozilla/5.0 (skill-seekers-extract)"}
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text


def _parse_html(html: str) -> Any:
    if BeautifulSoup is None:
        raise RuntimeError("The 'beautifulsoup4' package is required for extraction")
    return BeautifulSoup(html, "html.parser")


def extract_from_url(
    url: str,
    selector: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:
    """Extract structured content from a single URL."""
    html = fetch_url(url, timeout=timeout)
    return extract_from_soup(_parse_html(html), source=url, preferred_selector=selector)


def extract_from_html_file(
    path: str, selector: Optional[str] = None
) -> Dict[str, Any]:
    """Extract structured content from a local HTML file."""
    html_path = Path(path)
    if not html_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    html = html_path.read_text(encoding="utf-8", errors="replace")
    return extract_from_soup(
        _parse_html(html), source=str(html_path), preferred_selector=selector
    )


def extract_from_pdf(path: str) -> Dict[str, Any]:
    """Extract structured content from a PDF file.

    Reuses :class:`PDFExtractor` when PyMuPDF is installed so PDF and HTML
    extraction share language detection and quality scoring.
    """
    pdf_path = Path(path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    try:
        from skill_seekers.cli.pdf_extractor_poc import PDFExtractor
    except ImportError as exc:
        raise RuntimeError(
            "PDF extraction requires PyMuPDF (pip install PyMuPDF)"
        ) from exc

    extractor = PDFExtractor(str(pdf_path))
    result = extractor.extract_all()
    if result is None:
        raise RuntimeError(f"Failed to extract content from PDF: {path}")

    code_samples: List[Dict[str, str]] = []
    for page in result.get("pages", []):
        for sample in page.get("code_samples", []):
            code_samples.append({
                "code": sample.get("code", ""),
                "language": sample.get("language", "unknown"),
            })

    headings: List[Dict[str, str]] = []
    for page in result.get("pages", []):
        headings.extend(page.get("headings", []))

    content_parts = [
        page.get("text", "") for page in result.get("pages", []) if page.get("text")
    ]
    content = "\n\n".join(content_parts)

    return {
        "source": str(pdf_path),
        "title": pdf_path.stem,
        "selector_used": "pdf",
        "headings": headings,
        "content": content,
        "char_count": len(content),
        "code_samples": code_samples,
        "code_blocks_count": len(code_samples),
        "tables": [],
        "tables_count": result.get("total_tables", 0),
        "links": [],
        "links_count": 0,
        "total_pages": result.get("total_pages", 0),
    }


def to_markdown(data: Dict[str, Any]) -> str:
    """Render extracted content as Markdown."""
    lines = [f"# {data.get('title') or 'Extracted content'}", ""]
    lines.append(f"> Source: `{data.get('source', '')}`")
    lines.append("")
    if data.get("content"):
        lines.append(data["content"])
        lines.append("")
    if data.get("headings"):
        lines.append("## Headings")
        lines.append("")
        for heading in data["headings"]:
            level = heading.get("level", "h2").lstrip("h")
            try:
                depth = max(3, min(6, int(level) + 1))
            except ValueError:
                depth = 3
            lines.append(f"{'#' * depth} {heading.get('text', '')}")
        lines.append("")
    if data.get("code_samples"):
        lines.append("## Code samples")
        lines.append("")
        for sample in data["code_samples"]:
            lines.append(f"```{sample.get('language', '')}")
            lines.append(sample.get("code", ""))
            lines.append("```")
            lines.append("")
    if data.get("tables"):
        lines.append("## Tables")
        lines.append("")
        for table in data["tables"]:
            for row in table:
                lines.append("| " + " | ".join(row) + " |")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def to_text(data: Dict[str, Any]) -> str:
    """Render extracted content as plain text."""
    parts = [data.get("title", ""), "", data.get("content", "")]
    for sample in data.get("code_samples", []):
        parts.extend(["", f"[{sample.get('language', 'code')}]", sample.get("code", "")])
    return "\n".join(p for p in parts if p is not None).strip() + "\n"


def format_output(data: Dict[str, Any], fmt: str) -> str:
    """Format extracted data as markdown, json, or text."""
    fmt = (fmt or "markdown").lower()
    if fmt == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)
    if fmt == "text":
        return to_text(data)
    if fmt == "markdown":
        return to_markdown(data)
    raise ValueError(f"Unsupported format: {fmt!r} (choose markdown, json, or text)")


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the extract command."""
    parser = argparse.ArgumentParser(
        prog="skill-seekers extract",
        description="Extract clean content from a single URL, HTML file, or PDF",
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--url", help="Single documentation URL to extract")
    source.add_argument("--file", help="Local HTML file to extract")
    source.add_argument("--pdf", help="Local PDF file to extract")
    parser.add_argument(
        "--selector",
        help="CSS selector for main content (default: auto-detect)",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "text"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: print to stdout)",
    )
    parser.add_argument(
        "--timeout", type=int, default=DEFAULT_TIMEOUT,
        help=f"HTTP timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point for single-shot extraction."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.url:
            data = extract_from_url(args.url, selector=args.selector, timeout=args.timeout)
        elif args.file:
            data = extract_from_html_file(args.file, selector=args.selector)
        else:
            data = extract_from_pdf(args.pdf)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 - surface fetch/parse errors cleanly
        print(f"Error extracting content: {exc}", file=sys.stderr)
        return 1

    try:
        output = format_output(data, args.format)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
        print(f"Extracted {data.get('char_count', 0):,} chars, "
              f"{data.get('code_blocks_count', 0)} code blocks "
              f"(selector: {data.get('selector_used', '')})")
        print(f"Saved to: {out_path}")
    else:
        print(output, end="" if output.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
