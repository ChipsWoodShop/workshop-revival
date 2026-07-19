#!/usr/bin/env python3
"""Validate required site files and local links using only the standard library."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "index.html",
    "about.html",
    "projects/index.html",
    "assets/css/styles.css",
    "assets/js/site.js",
    "assets/images/README.md",
    "assets/images/brand/workshop-revival-logo.svg",
    "assets/images/projects/grey-water-filter.jpg",
    "assets/images/projects/weed-puller.png",
    "README.md",
    "PROJECT.md",
    "TODO.md",
    "CHANGELOG.md",
    "DECISIONS.md",
    "AGENTS.md",
    "docs/brand/BRAND_GUIDE.md",
    "docs/brand/brand-tokens.css",
    "docs/brand/VISUAL_ASSETS.md",
    "docs/brand/VOICE_AND_TONE.md",
    "docs/brand/SOURCE.md",
    "docs/README.md",
    "tests/README.md",
    "scripts/validate_site.py",
)


class ReferenceParser(HTMLParser):
    """Collect attributes that can point to local resources."""

    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, int]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        attribute_name = "href" if tag in {"a", "link"} else "src" if tag in {"script", "img"} else None
        if attribute_name and attributes.get(attribute_name):
            self.references.append((attributes[attribute_name], self.getpos()[0]))


def local_target(source: Path, reference: str) -> tuple[Path, str] | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("mailto:", "tel:")):
        return None
    path_text = unquote(parsed.path)
    target = source if not path_text else (source.parent / path_text)
    if path_text.endswith("/"):
        target = target / "index.html"
    return target.resolve(), unquote(parsed.fragment)


def main() -> int:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    html_files = sorted(ROOT.rglob("*.html"))
    parsed_pages: dict[Path, ReferenceParser] = {}
    for html_file in html_files:
        parser = ReferenceParser()
        try:
            parser.feed(html_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            errors.append(f"Could not read {html_file.relative_to(ROOT)}: {exc}")
            continue
        parsed_pages[html_file.resolve()] = parser

    for source, parser in parsed_pages.items():
        for reference, line in parser.references:
            resolved = local_target(source, reference)
            if resolved is None:
                continue
            target, fragment = resolved
            source_label = source.relative_to(ROOT)
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source_label}:{line}: local reference leaves repository: {reference}")
                continue
            if not target.is_file():
                errors.append(f"{source_label}:{line}: broken local reference: {reference}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed_pages.get(target)
                if target_parser is None or fragment not in target_parser.ids:
                    errors.append(f"{source_label}:{line}: missing fragment #{fragment} in {target.relative_to(ROOT)}")

    print(f"Checked {len(REQUIRED_FILES)} required files and {len(html_files)} HTML pages.")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Validation passed: required files exist and local references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
