#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
snapshot_corpus - capture a dated, hash-pinned text snapshot of the public corpus (R6).

Reads the cloned site source (default: ../canon-corpus-src relative to this repo)
and writes one clean text file per page under canon13/corpus/snapshot-<date>/,
plus a manifest (snapshot-<date>.tsv) with raw-HTML SHA-256, text SHA-256, and
word counts. Re-run for every edition; the snapshot directory is the corpus of
record for extract/contradictions and for audit.

Stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

SKIP_TAGS = {"script", "style", "svg", "nav", "button", "noscript", "template", "iframe", "form"}
BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "blockquote", "div", "section", "article", "main", "table", "thead", "tbody", "pre"}
CELL_TAGS = {"td", "th"}
HEADING_TAGS = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = 0
        self.skip_depth = 0
        self.in_cell = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main += 1
            return
        if self.in_main == 0:
            return
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in CELL_TAGS:
            if self.in_cell:
                self.parts.append(" | ")
            self.in_cell = True
        elif tag in BLOCK_TAGS:
            prefix = HEADING_TAGS.get(tag, "")
            self.parts.append("\n" + prefix)
            if tag in ("ul", "ol"):
                self.parts.append("")

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = max(0, self.in_main - 1)
            return
        if self.in_main == 0:
            return
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag in CELL_TAGS:
            self.in_cell = False
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.in_main and not self.skip_depth:
            self.parts.append(data)

    def text(self):
        out = "".join(self.parts)
        lines = []
        for line in out.splitlines():
            line = " ".join(line.split())
            if line:
                lines.append(line)
        return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="capture dated text snapshot of the public corpus")
    ap.add_argument("--src", default="../canon-corpus-src", help="path to the cloned site source")
    ap.add_argument("--out", default=None, help="snapshot dir (default canon13/corpus/snapshot-<today>)")
    args = ap.parse_args()

    src = Path(args.src)
    if not src.is_dir():
        print(f"source not found: {src.resolve()}", file=sys.stderr)
        sys.exit(2)
    today = date.today().isoformat()
    out = Path(args.out) if args.out else Path(__file__).resolve().parent.parent / "corpus" / f"snapshot-{today}"
    out.mkdir(parents=True, exist_ok=True)

    pages = []
    canon = src / "investors-canon"
    if (canon / "index.html").exists():
        pages.append(("index", canon / "index.html", "https://santoshkumaradhikari.com.np/investors-canon/"))
    if (canon / "framework.html").exists():
        pages.append(("framework", canon / "framework.html", "https://santoshkumaradhikari.com.np/investors-canon/framework.html"))
    for p in sorted((canon / "chapters").glob("*.html")) if (canon / "chapters").is_dir() else []:
        pages.append((p.stem, p, f"https://santoshkumaradhikari.com.np/investors-canon/chapters/{p.name}"))
    for stem in ("nabil-bank", "chilime-hydropower"):
        p = src / "research" / stem / "index.html"
        if p.exists():
            pages.append((f"research-{stem}", p, f"https://santoshkumaradhikari.com.np/research/{stem}/"))
    home = src / "index.html"
    if home.exists():
        pages.append(("home", home, "https://santoshkumaradhikari.com.np/"))

    manifest = []
    total_words = 0
    for slug, path, url in pages:
        raw = path.read_bytes()
        raw_sha = hashlib.sha256(raw).hexdigest()
        try:
            html = raw.decode("utf-8", errors="replace")
        except Exception as e:
            print(f"WARN {slug}: {e}", file=sys.stderr)
            continue
        ex = TextExtractor()
        ex.feed(html)
        text = ex.text()
        text_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        words = len(text.split())
        total_words += words
        body = (
            f"# SNAPSHOT {today}\n"
            f"# url: {url}\n"
            f"# raw_html_sha256: {raw_sha}\n"
            f"# text_sha256: {text_sha}\n"
            f"# words: {words}\n\n"
            + text
        )
        (out / f"{slug}.txt").write_text(body, encoding="utf-8")
        manifest.append((slug, url, raw_sha, text_sha, words, path))
        print(f"  {words:6d} words  {slug}")

    man = out / f"snapshot-{today}.tsv"
    with man.open("w", encoding="utf-8", newline="") as f:
        f.write("slug\turl\traw_html_sha256\ttext_sha256\twords\tsrc_path\n")
        for slug, url, raw_sha, text_sha, words, path in manifest:
            f.write(f"{slug}\t{url}\t{raw_sha}\t{text_sha}\t{words}\t{path}\n")
    print(f"\nSNAPSHOT: {len(manifest)} pages, {total_words} total words -> {out}")
    print(f"manifest -> {man}")


if __name__ == "__main__":
    main()
