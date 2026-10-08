#!/usr/bin/env python3
"""Check the rendered homepage hero's semantic structure, not its pixels."""

from html.parser import HTMLParser
from pathlib import Path


class HeroParser(HTMLParser):
    VOID_TAGS = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[tuple[str, frozenset[str]]] = []
        self.heroes = 0
        self.hero_children: list[frozenset[str]] = []
        self.content_depth: int | None = None
        self.content_has_heading = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = frozenset((dict(attrs).get("class") or "").split())
        if "veytrix-hero" in classes:
            self.heroes += 1
            self.hero_children = []
        elif self.stack and "veytrix-hero" in self.stack[-1][1]:
            self.hero_children.append(classes)
        if "veytrix-hero__content" in classes:
            self.content_depth = len(self.stack)
        if tag == "h1" and self.content_depth is not None:
            self.content_has_heading = True
        if tag not in self.VOID_TAGS:
            self.stack.append((tag, classes))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self.stack:
            return
        while self.stack:
            open_tag, classes = self.stack.pop()
            if "veytrix-hero__content" in classes:
                self.content_depth = None
            if open_tag == tag:
                break


def validate_html(html: str) -> None:
    parser = HeroParser()
    parser.feed(html)
    expected = [frozenset({"veytrix-hero__content"}), frozenset({"veytrix-hero__diagram"})]
    if parser.heroes != 1:
        raise ValueError(f"expected one rendered hero, found {parser.heroes}")
    if parser.hero_children != expected:
        raise ValueError(f"unexpected hero child structure: {parser.hero_children!r}")
    if not parser.content_has_heading:
        raise ValueError("hero content is missing its h1")


def main() -> None:
    page = Path("site/index.html")
    if not page.is_file():
        raise SystemExit("site/index.html is missing; run mkdocs build first")
    try:
        validate_html(page.read_text(encoding="utf-8"))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print("Rendered hero structure is valid (responsive layout requires browser testing).")


if __name__ == "__main__":
    main()
