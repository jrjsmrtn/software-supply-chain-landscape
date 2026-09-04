#!/usr/bin/env python3
"""Render the OKF bundle in `knowledge/` as a browseable static site.

WHY THIS EXISTS RATHER THAN JEKYLL
----------------------------------
OKF writes cross-concept links bundle-absolute -- `/formats/sbom-types.md`, where the
leading `/` means the BUNDLE root. A browser reads it as the SITE root, so on a project
Pages site (`<user>.github.io/<repo>/`) all 190 of them drop the repo segment and 404.
Every internal link also ends in `.md`, which no HTML-rendering generator preserves.

The corpus cannot be changed to suit the website: the convention is the OKF spec's, `okf`
enforces it, and rewriting it would corrupt the product to serve one of its consumers.
So the rewrite happens HERE, at build time, and `knowledge/` is read and never written.

WHY THE REWRITE IS DONE ON RENDERED HTML, NOT ON MARKDOWN
---------------------------------------------------------
A link inside a fenced block or an inline code span is DOCUMENTATION of a link, not a
link, and must not be rewritten. Editing markdown means re-implementing the fence and
code-span rules by hand, which is exactly the parsing this project deleted elsewhere in
favour of `mq`. Rendering first makes the distinction free: a code-block link comes out
as text, and only real links become `<a href>`.

That leaves one way to be wrong -- an `href=` string appearing literally in prose or in a
code sample would be matched by the attribute rewrite. `assert_no_literal_href()` fails
the build if one ever appears, so the assumption is checked on every run rather than
being true on the day it was written.
"""

from __future__ import annotations

import html
import os
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "knowledge"
OUT = ROOT / "_site"
TEMPLATE = Path(__file__).resolve().parent / "template.html"
STYLE = Path(__file__).resolve().parent / "style.css"

# Empty for a custom domain or a user page; "/<repo>" for a project page.
BASEURL = os.environ.get("SITE_BASEURL", "/software-supply-chain-landscape").rstrip("/")

EXTERNAL = ("http://", "https://", "mailto:", "//", "data:")

# A bundle link may deliberately point OUTSIDE the bundle: `knowledge/log.md` cites
# `../CHANGELOG.md`, and says in place that a copied tree loses it by design. Only
# `knowledge/` is published, so on the site that target does not exist -- but the file
# does exist in the repository, so the honest rendering is a link to it there rather
# than a dead relative path or a silently dropped link.
REPO_BLOB = "https://github.com/jrjsmrtn/software-supply-chain-landscape/blob/main/"

# `footnotes` is not optional: OKF 5.1 makes footnotes the attribution mechanism, so
# without it every `[^id]` reference renders as literal text and the sources vanish.
MD_EXTENSIONS = ["extra", "footnotes", "tables", "sane_lists", "toc", "attr_list"]


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter, body). A concept without frontmatter is a fault, not a page."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def assert_no_literal_href(md_files: list[Path]) -> None:
    """The attribute rewrite below assumes `href=` never occurs as content. Check it."""
    offenders = [p for p in md_files if "href=" in p.read_text(encoding="utf-8")]
    if offenders:
        names = ", ".join(str(p.relative_to(ROOT)) for p in offenders[:5])
        sys.exit(
            f"build: {len(offenders)} file(s) contain a literal `href=` ({names}).\n"
            "  The HTML attribute rewrite cannot distinguish those from real links.\n"
            "  Rewrite them, or teach this script to mask <pre>/<code> before matching."
        )


def rewrite_target(url: str, page: Path) -> str:
    """Map one bundle link onto its published URL, as seen from `page`.

    Anchors and externals survive intact. A relative link that escapes the bundle is sent
    to the repository, because only `knowledge/` is published.
    """
    if not url or url.startswith(EXTERNAL) or url.startswith("#"):
        return url
    path, sep, anchor = url.partition("#")

    if not path.startswith("/"):
        # Resolve against the page to see whether it leaves the bundle at all.
        resolved = os.path.normpath((page.parent / path).as_posix())
        if resolved.startswith(".."):
            return REPO_BLOB + resolved.lstrip("./").replace("../", "") + sep + anchor

    if path.endswith(".md"):
        path = path[:-3] + ".html"
    if path.startswith("/"):                      # bundle-absolute -> site-absolute
        path = BASEURL + path
    return path + sep + anchor


def rewrite_links(html_text: str, page: Path) -> str:
    return re.sub(
        r'(href=")([^"]*)(")',
        lambda m: m.group(1) + rewrite_target(m.group(2), page) + m.group(3),
        html_text,
    )


FIRST_H1 = re.compile(r'<h1[^>]*>(.*?)</h1>', re.S)


def page_title(fm: dict, rendered: str, rel: Path) -> tuple[str, str]:
    """Return (title, body) — and take the title OUT of the body when it came from there.

    Two shapes exist in this bundle and they need opposite handling. A concept carries
    `title` in frontmatter and uses `#` for SECTION headings, so its first h1 is not a
    title. The eleven category indexes and `log.md` carry no frontmatter at all (checked:
    12 of 86 files), so their first h1 IS the title -- and rendering it as well as the
    template's own produced `<h1>index</h1>` above `<h1>The xBOM family</h1>`, with the
    nav falling back to directory slugs.
    """
    if fm.get("title"):
        return str(fm["title"]), rendered
    m = FIRST_H1.search(rendered)
    if not m:
        return rel.stem, rendered
    return re.sub(r"<[^>]+>", "", m.group(1)).strip(), rendered[: m.start()] + rendered[m.end() :]


def demote_headings(rendered: str) -> str:
    """Shift every body heading down one level so the page has exactly one h1: its title.

    Ids are generated from the heading TEXT, not its level, so `#anchor` links survive.
    """
    for level in range(5, 0, -1):
        rendered = re.sub(rf"<h{level}([^>]*)>", rf"<h{level + 1}\1>", rendered)
        rendered = rendered.replace(f"</h{level}>", f"</h{level + 1}>")
    return rendered


def meta_block(fm: dict) -> str:
    """Surface the metadata that makes this corpus worth trusting, or not trusting.

    A concept's `verified` state and `stale_after` are the difference between a sourced
    claim and an assertion, and they are invisible in the prose. They belong on the page.
    """
    rows = []
    if fm.get("type"):
        rows.append(("Type", html.escape(str(fm["type"]))))
    if fm.get("status"):
        rows.append(("Status", html.escape(str(fm["status"]))))
    verified = fm.get("verified")
    rows.append(("Verified", html.escape(str(verified[0].get("at", "—"))[:10])
                 if isinstance(verified, list) and verified else "not verified"))
    if fm.get("stale_after"):
        rows.append(("Review by", html.escape(str(fm["stale_after"]))))
    if isinstance(fm.get("sources"), list):
        rows.append(("Sources", str(len(fm["sources"]))))
    cells = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    return f'<dl class="meta">{cells}</dl>'


def nav_html(pages: list[tuple[Path, dict, str]]) -> str:
    """One entry per category, titled from that category's own index.md."""
    cats: dict[str, str] = {}
    for rel, fm, heading in pages:
        if len(rel.parts) == 2 and rel.name == "index.md":
            cats[rel.parts[0]] = str(fm.get("title") or heading or rel.parts[0])
    items = "".join(
        f'<li><a href="{BASEURL}/{slug}/index.html">{html.escape(title)}</a></li>'
        for slug, title in sorted(cats.items())
    )
    return f'<ul class="nav">{items}</ul>'


def main() -> int:
    md_files = sorted(BUNDLE.rglob("*.md"))
    if not md_files:
        sys.exit(f"build: no markdown under {BUNDLE}")
    assert_no_literal_href(md_files)

    template = TEMPLATE.read_text(encoding="utf-8")
    parsed = [(p.relative_to(BUNDLE), split_frontmatter(p.read_text(encoding="utf-8"))) for p in md_files]
    # Titles must be known before the nav is built, and a heading-derived title requires
    # the rendered body -- so render once, up front, and reuse it.
    prepared = []
    for rel, (fm, body) in parsed:
        rendered = markdown.Markdown(extensions=MD_EXTENSIONS).convert(body)
        title, rendered = page_title(fm, rendered, rel)
        prepared.append((rel, fm, title, demote_headings(rendered)))
    nav = nav_html([(rel, fm, title) for rel, fm, title, _ in prepared])

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    written = 0
    for rel, fm, title, rendered in prepared:
        rendered = rewrite_links(rendered, rel)
        is_home = rel.as_posix() == "index.md"
        page = (
            template.replace("{{ title }}", html.escape(title))
            .replace("{{ description }}", html.escape(str(fm.get("description") or "")))
            .replace("{{ baseurl }}", BASEURL)
            .replace("{{ nav }}", nav)
            .replace("{{ meta }}", "" if is_home else meta_block(fm))
            .replace("{{ content }}", rendered)
        )
        dest = OUT / rel.with_suffix(".html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        written += 1

    shutil.copy2(STYLE, OUT / "style.css")
    # Tell Pages not to run Jekyll over output that is already final.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    if written != len(md_files):
        sys.exit(f"build: wrote {written} page(s) from {len(md_files)} source file(s)")

    # ONLY `knowledge/` is published. `CLAUDE.md` is developer guidance, `CHANGELOG.md`
    # is release history, and neither is part of the product -- the bundle is. The
    # generator reads nothing else, and this asserts that rather than trusting it: the
    # emitted pages must correspond one-to-one to the bundle's own files.
    emitted = {q.relative_to(OUT).with_suffix(".md") for q in OUT.rglob("*.html")}
    expected = {p.relative_to(BUNDLE) for p in md_files}
    if emitted != expected:
        stray = sorted(str(x) for x in emitted - expected)
        sys.exit(f"build: output does not match the bundle; unexpected page(s): {stray[:5]}")
    print(f"built {written} page(s) -> {OUT.relative_to(ROOT)}  (baseurl: {BASEURL or '/'})")
    return verify()


def verify() -> int:
    """Resolve every internal link in the OUTPUT. A build that emits 404s has failed.

    This is the check the repository lacked for the bundle itself until 2026-09-04, when
    `okf validate` was found reporting `valid: true` on a planted missing target. The
    same mistake is cheaper to make here, because the rewrite is what can break it.
    """
    broken, checked = [], 0
    for page in sorted(OUT.rglob("*.html")):
        for url in re.findall(r'href="([^"]*)"', page.read_text(encoding="utf-8")):
            if not url or url.startswith(EXTERNAL) or url.startswith("#"):
                continue
            path = url.partition("#")[0]
            if not path:
                continue
            if path.endswith(".md"):
                broken.append(f"{page.relative_to(OUT)}: still points at markdown -> {url}")
                continue
            target = (OUT / path[len(BASEURL) + 1 :]) if BASEURL and path.startswith(BASEURL + "/") \
                else (OUT / path.lstrip("/")) if path.startswith("/") \
                else (page.parent / path)
            checked += 1
            if not target.resolve().exists():
                broken.append(f"{page.relative_to(OUT)}: dead link -> {url}")
    if broken:
        print(f"\nbuild: {len(broken)} broken link(s) in the generated site:", file=sys.stderr)
        for b in broken[:20]:
            print(f"  {b}", file=sys.stderr)
        return 1
    print(f"links OK ({checked} internal link(s) resolved in the built site)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
