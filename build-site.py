#!/usr/bin/env python3
"""Build the static documentation site in docs/ into site/, ready for GitHub Pages.

No dependencies. The markdown subset here is exactly what docs/ uses — headings,
paragraphs, lists, tables, fenced code, blockquotes and inline emphasis — so a small
converter is safer than pulling in a parser that has to be installed first.

    python3 build-site.py

Output goes to site/. Nothing else is touched.
"""

import html
import json
import pathlib
import re
import shutil

DOCS = pathlib.Path("docs")
OUT = pathlib.Path("site")
REPO = "https://github.com/asarayja/asaraya-cloth-creator"
TITLE = "Asarayja Cloth Creator"


# --------------------------------------------------------------------------- inline

def out_url(path):
    """docs/-relative markdown path -> site-relative html path."""
    if path.endswith("README.md"):
        return path[:-len("README.md")] + "index.html"
    return path[:-3] + ".html"


def _slug(text):
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def _inline(text, base):
    """Emphasis, code and links. Code is pulled out first so its contents survive."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1)))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)

    def link(m):
        label, href = m.group(1), m.group(2)
        if href.endswith(".md"):
            href = out_url(href)
        external = href.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if external else ""
        return f'<a href="{href}"{attrs}>{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{spans[int(m.group(1))]}</code>", text)
    return text


# ---------------------------------------------------------------------------- blocks

def _table(rows, base):
    head, body = rows[0], rows[2:]
    cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
    out = ['<div class="scroll"><table>', "<thead><tr>"]
    out += [f"<th>{_inline(c, base)}</th>" for c in cells(head)]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{_inline(c, base)}</td>" for c in cells(r)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def _list(items, ordered, base):
    tag = "ol" if ordered else "ul"
    out = [f"<{tag}>"]
    for item, sub in items:
        out.append(f"<li>{_inline(item, base)}")
        if sub:
            out.append(_list([(s, []) for s in sub], False, base))
        out.append("</li>")
    out.append(f"</{tag}>")
    return "".join(out)


def convert(md, base):
    lines = md.split("\n")
    out, headings = [], []
    i = 0
    para = []

    def flush():
        if para:
            out.append(f"<p>{_inline(' '.join(para), base)}</p>")
            para.clear()

    while i < len(lines):
        ln = lines[i]

        if ln.startswith("```"):
            flush()
            i += 1
            code = []
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            continue

        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows, base))
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush()
            lvl, txt = len(m.group(1)), m.group(2)
            sid = _slug(txt)
            if lvl >= 2:
                headings.append({"text": re.sub(r"[*`]", "", txt), "id": sid})
            out.append(f'<h{lvl} id="{sid}">{_inline(txt, base)}</h{lvl}>')
            i += 1
            continue

        if ln.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip(">").strip())
                i += 1
            body = " ".join(x for x in quote if x)
            out.append(f'<blockquote>{_inline(body, base)}</blockquote>')
            continue

        if re.match(r"^\s*(?:[*-]|\d+\.)\s+", ln):
            flush()
            ordered = bool(re.match(r"^\s*\d+\.\s+", ln))
            items = []
            while i < len(lines):
                cur = lines[i]
                top = re.match(r"^(?:[*-]|\d+\.)\s+(.*)$", cur)
                nested = re.match(r"^\s{2,}(?:[*-])\s+(.*)$", cur)
                cont = re.match(r"^\s{2,}(?!\s*(?:[*-]|\d+\.)\s)(\S.*)$", cur)
                if top:
                    items.append([top.group(1), []])
                elif nested and items:
                    items[-1][1].append(nested.group(1))
                elif cont and items:
                    if items[-1][1]:
                        items[-1][1][-1] += " " + cont.group(1)
                    else:
                        items[-1][0] += " " + cont.group(1)
                elif cur.strip() == "" and i + 1 < len(lines) and re.match(
                        r"^\s*(?:[*-]|\d+\.)\s+", lines[i + 1]):
                    pass
                else:
                    break
                i += 1
            out.append(_list([(a, b) for a, b in items], ordered, base))
            continue

        if ln.strip() == "":
            flush()
            i += 1
            continue

        if ln.strip() == "---":
            flush()
            out.append("<hr>")
            i += 1
            continue

        para.append(ln.strip())
        i += 1

    flush()
    return "".join(out), headings


# ------------------------------------------------------------------------------- nav

def parse_summary():
    groups, current = [], None
    for ln in (DOCS / "SUMMARY.md").read_text(encoding="utf-8").split("\n"):
        g = re.match(r"^##\s+(.*)$", ln)
        if g:
            current = {"title": g.group(1), "pages": []}
            groups.append(current)
            continue
        p = re.match(r"^\*\s+\[([^\]]+)\]\(([^)]+)\)", ln)
        if p:
            entry = {"title": p.group(1), "path": p.group(2)}
            if current is None:
                current = {"title": None, "pages": []}
                groups.append(current)
            current["pages"].append(entry)
    return groups


def render_nav(groups, active, base):
    out = ['<nav class="nav">']
    for g in groups:
        if g["title"]:
            out.append(f'<div class="nav-group">{html.escape(g["title"])}</div>')
        out.append("<ul>")
        for p in g["pages"]:
            href = base + out_url(p["path"])
            cls = ' class="active"' if p["path"] == active else ""
            out.append(f'<li><a href="{href}"{cls}>{html.escape(p["title"])}</a></li>')
        out.append("</ul>")
    out.append("</nav>")
    return "".join(out)


PAGE = """<!doctype html>
<html lang="en" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{base}style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#129507;</text></svg>">
<script>(function(){{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}})();</script>
</head>
<body>
<header class="top">
  <button class="burger" aria-label="Menu" onclick="document.body.classList.toggle('open')">
    <svg viewBox="0 0 24 24" width="20" height="20"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>
  </button>
  <a class="brand" href="{base}index.html"><span class="brand-mark"></span>{brand}</a>
  <div class="top-right">
    <input id="q" class="search" type="search" placeholder="Search" autocomplete="off" spellcheck="false">
    <a class="ghost" href="{repo}" target="_blank" rel="noopener" aria-label="GitHub">
      <svg viewBox="0 0 16 16" width="17" height="17" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.4 7.4 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
    </a>
    <button class="ghost" id="theme" aria-label="Toggle theme">
      <svg class="i-sun" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="i-moon" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>
    </button>
  </div>
</header>
<div class="shell">
  <aside class="side">{nav}</aside>
  <main>
    <article class="prose">{body}</article>
    {pager}
    <footer class="foot">
      <a href="{repo}/edit/main/docs/{path}">Edit this page on GitHub</a>
      <span>{brand} &middot; GPL-3.0-or-later</span>
    </footer>
  </main>
  <div class="toc-wrap">{toc}</div>
</div>
<div class="scrim" onclick="document.body.classList.remove('open')"></div>
<div id="results" class="results" hidden></div>
<script>window.SEARCH_BASE="{base}";</script>
<script src="{base}search-index.js"></script>
<script src="{base}site.js"></script>
</body>
</html>"""


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    groups = parse_summary()
    flat = [p for g in groups for p in g["pages"]]
    index = []

    for n, page in enumerate(flat):
        src = DOCS / page["path"]
        md = src.read_text(encoding="utf-8")
        depth = page["path"].count("/")
        base = "../" * depth
        body, headings = convert(md, base)

        first = re.search(r"^#\s+(.*)$", md, re.M)
        h1 = first.group(1) if first else page["title"]
        desc = ""
        m = re.search(r"^#\s+.*?\n+([^\n#|>*\-`].*?)$", md, re.M | re.S)
        if m:
            desc = re.sub(r"\s+", " ", re.sub(r"[*`\[\]]|\(.*?\)", "", m.group(1)))[:155].strip()

        toc = ""
        if len(headings) > 1:
            links = "".join(
                f'<a href="#{h["id"]}">{html.escape(h["text"])}</a>' for h in headings)
            toc = f'<nav class="toc"><div class="toc-title">On this page</div>{links}</nav>'

        prev_p = flat[n - 1] if n else None
        next_p = flat[n + 1] if n + 1 < len(flat) else None
        pl = pr = ""
        if prev_p:
            pl = (f'<a class="pg prev" href="{base}{out_url(prev_p["path"])}">'
                  f'<span>Previous</span>{html.escape(prev_p["title"])}</a>')
        if next_p:
            pr = (f'<a class="pg next" href="{base}{out_url(next_p["path"])}">'
                  f'<span>Next</span>{html.escape(next_p["title"])}</a>')
        pager = f'<div class="pager">{pl}{pr}</div>' if (pl or pr) else ""

        out_rel = out_url(page["path"])
        dest = OUT / out_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(PAGE.format(
            title=f"{h1} · {TITLE}" if out_rel != "index.html" else TITLE,
            desc=html.escape(desc), base=base, brand=TITLE, repo=REPO,
            nav=render_nav(groups, page["path"], base), body=body, toc=toc,
            pager=pager, path=page["path"]), encoding="utf-8")

        index.append({"t": h1, "u": out_rel, "g": next(
            (g["title"] for g in groups if page in g["pages"]), ""),
            "h": [h["text"] for h in headings],
            "b": re.sub(r"\s+", " ", re.sub(r"[#*`|>\[\]()-]", " ", md))[:1200]})

    (OUT / "search-index.js").write_text(
        "window.SEARCH_INDEX=" + json.dumps(index, ensure_ascii=False) + ";",
        encoding="utf-8")
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    (OUT / "site.js").write_text(JS, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"{len(flat)} pages -> {OUT}/")


CSS = ""   # filled in by style.py
JS = ""

if __name__ == "__main__":
    from site_assets import CSS, JS  # noqa: F811
    build()
