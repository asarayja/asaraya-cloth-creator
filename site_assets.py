"""Stylesheet and script for the generated documentation site."""

CSS = r"""
:root{
  --bg:#ffffff; --surface:#f6f7f9; --surface-2:#eceef2;
  --text:#14161a; --muted:#5f6672; --border:#e3e6eb;
  --accent:#bf2532; --accent-soft:#fdeced; --accent-line:#eda9ae;
  --shadow:0 1px 2px rgba(16,20,28,.06),0 8px 24px rgba(16,20,28,.08);
  --radius:10px; --side:252px; --toc:196px; --head:56px;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0e1014; --surface:#15181e; --surface-2:#1c2027;
    --text:#e7e9ee; --muted:#9aa1ae; --border:#252932;
    --accent:#ff7a7a; --accent-soft:#2a1315; --accent-line:#5e262b;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.45);
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#0e1014; --surface:#15181e; --surface-2:#1c2027;
  --text:#e7e9ee; --muted:#9aa1ae; --border:#252932;
  --accent:#ff7a7a; --accent-soft:#2a1315; --accent-line:#5e262b;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.45);
  color-scheme:dark;
}

*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);
  font-size:16px;line-height:1.68;-webkit-font-smoothing:antialiased;
}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:3px}

/* ---------------------------------------------------------------- header */
.top{
  position:sticky;top:0;z-index:40;height:var(--head);display:flex;align-items:center;
  gap:12px;padding:0 18px;background:color-mix(in srgb,var(--bg) 88%,transparent);
  backdrop-filter:saturate(180%) blur(12px);border-bottom:1px solid var(--border);
}
.brand{display:flex;align-items:center;gap:9px;font-weight:650;color:var(--text);
  letter-spacing:-.01em;font-size:15px;white-space:nowrap}
.brand:hover{text-decoration:none}
.brand-mark{
  width:20px;height:20px;border-radius:6px;flex:none;
  background:linear-gradient(140deg,#e04350,#bf2532 55%,#7a121b);
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);
}
.top-right{margin-left:auto;display:flex;align-items:center;gap:8px}
.search{
  width:200px;height:34px;padding:0 12px;border-radius:8px;font:inherit;font-size:14px;
  background:var(--surface);border:1px solid var(--border);color:var(--text);
}
.search::placeholder{color:var(--muted)}
.search:focus{outline:2px solid var(--accent-line);outline-offset:-1px;background:var(--bg)}
.ghost{
  display:grid;place-items:center;width:34px;height:34px;border-radius:8px;flex:none;
  background:transparent;border:1px solid transparent;color:var(--muted);cursor:pointer;
}
.ghost:hover{background:var(--surface);color:var(--text)}
.i-sun{display:none}
:root[data-theme="dark"] .i-sun{display:block}
:root[data-theme="dark"] .i-moon{display:none}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]) .i-sun{display:block}
  :root:not([data-theme="light"]) .i-moon{display:none}
}
.burger{display:none;background:none;border:0;color:var(--text);cursor:pointer;padding:6px}

/* ----------------------------------------------------------------- shell */
.shell{
  display:grid;grid-template-columns:var(--side) minmax(0,1fr) var(--toc);
  gap:36px;max-width:1400px;margin:0 auto;padding:0 24px;align-items:start;
}
.side{
  position:sticky;top:var(--head);max-height:calc(100vh - var(--head));
  overflow-y:auto;padding:26px 4px 60px;
}
.nav-group{
  font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin:22px 0 7px 10px;
}
.nav-group:first-child{margin-top:0}
.nav ul{list-style:none;margin:0;padding:0}
.nav a{
  display:block;padding:5px 10px;border-radius:7px;color:var(--muted);
  font-size:14.5px;line-height:1.45;border-left:2px solid transparent;
}
.nav a:hover{background:var(--surface);color:var(--text);text-decoration:none}
.nav a.active{
  color:var(--accent);background:var(--accent-soft);font-weight:600;
  border-left-color:var(--accent);
}
main{min-width:0;padding:34px 0 72px}

/* ----------------------------------------------------------------- prose */
.prose{max-width:75ch}
.prose h1{font-size:2.05rem;line-height:1.2;letter-spacing:-.022em;margin:0 0 .55em;font-weight:700}
.prose h2{
  font-size:1.36rem;line-height:1.3;letter-spacing:-.014em;font-weight:660;
  margin:2.3em 0 .7em;padding-top:1.1em;border-top:1px solid var(--border);
}
.prose h3{font-size:1.08rem;font-weight:650;margin:1.9em 0 .5em;letter-spacing:-.008em}
.prose h4{font-size:.98rem;font-weight:650;margin:1.6em 0 .4em;color:var(--muted)}
.prose h2:first-child,.prose h3:first-child{margin-top:0;border-top:0;padding-top:0}
.prose p{margin:0 0 1.15em}
.prose ul,.prose ol{margin:0 0 1.25em;padding-left:1.35em}
.prose li{margin:.34em 0}
.prose li>ul,.prose li>ol{margin:.35em 0 .1em}
.prose strong{font-weight:650;color:var(--text)}
.prose hr{border:0;border-top:1px solid var(--border);margin:2.4em 0}

code{
  font-family:var(--mono);font-size:.875em;background:var(--surface-2);
  padding:.14em .38em;border-radius:5px;border:1px solid var(--border);
  overflow-wrap:break-word;
}
/* identifiers in tables must never be split mid-word — the table scrolls instead */
th code,td code{overflow-wrap:normal;word-break:normal;white-space:nowrap}
pre{
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:15px 17px;overflow-x:auto;margin:0 0 1.35em;line-height:1.6;
}
pre code{background:none;border:0;padding:0;font-size:.855em;color:var(--text)}

blockquote{
  margin:0 0 1.35em;padding:13px 17px;background:var(--accent-soft);
  border:1px solid var(--accent-line);border-left-width:3px;border-radius:var(--radius);
  color:var(--text);
}
blockquote strong:first-child{color:var(--accent)}

.scroll{overflow-x:auto;margin:0 0 1.45em;border:1px solid var(--border);
  border-radius:var(--radius);background:var(--bg)}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:9px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--border)}
th{background:var(--surface);font-weight:640;font-size:13px;letter-spacing:.01em;
  white-space:nowrap;color:var(--text)}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover td{background:var(--surface)}
td:first-child{white-space:nowrap}
/* below this width a three-column table cannot fit; let it scroll rather than squeeze */
@media (max-width:680px){table{min-width:540px}}

/* ----------------------------------------------------------------- pager */
.pager{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:48px 0 0;max-width:75ch}
.pg{
  display:flex;flex-direction:column;gap:2px;padding:13px 16px;border:1px solid var(--border);
  border-radius:var(--radius);color:var(--text);font-weight:600;font-size:14.5px;
  background:var(--bg);transition:border-color .15s,background .15s;
}
.pg:hover{border-color:var(--accent-line);background:var(--surface);text-decoration:none}
.pg span{font-size:11.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.pg.next{grid-column:2;text-align:right}
.pg.prev:only-child{grid-column:1}

.foot{
  display:flex;flex-wrap:wrap;gap:10px 20px;justify-content:space-between;
  margin-top:44px;padding-top:20px;border-top:1px solid var(--border);
  font-size:13.5px;color:var(--muted);max-width:75ch;
}

/* ------------------------------------------------------------------- toc */
.toc-wrap{position:sticky;top:var(--head);padding:34px 0 40px;max-height:calc(100vh - var(--head));overflow-y:auto}
.toc{display:flex;flex-direction:column;gap:1px;border-left:1px solid var(--border);padding-left:14px}
.toc-title{font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin-bottom:8px}
.toc a{color:var(--muted);font-size:13.5px;line-height:1.45;padding:3.5px 0}
.toc a:hover{color:var(--text);text-decoration:none}
.toc a.here{color:var(--accent);font-weight:600}

/* ---------------------------------------------------------------- search */
.results{
  position:fixed;top:calc(var(--head) + 8px);left:50%;transform:translateX(-50%);
  width:min(640px,calc(100vw - 32px));max-height:min(64vh,520px);overflow-y:auto;z-index:60;
  background:var(--bg);border:1px solid var(--border);border-radius:14px;box-shadow:var(--shadow);
  padding:6px;
}
.results a{display:block;padding:9px 12px;border-radius:8px;color:var(--text)}
.results a:hover,.results a.sel{background:var(--surface);text-decoration:none}
.results .r-t{font-weight:620;font-size:14.5px}
.results .r-g{font-size:12px;color:var(--muted);margin-top:1px}
.results .r-none{padding:16px 12px;color:var(--muted);font-size:14px}

.scrim{
  position:fixed;inset:0;background:rgba(8,10,14,.5);z-index:45;opacity:0;
  pointer-events:none;transition:opacity .18s;
}

/* ------------------------------------------------------------ responsive */
@media (max-width:1180px){
  .shell{grid-template-columns:var(--side) minmax(0,1fr)}
  .toc-wrap{display:none}
}
@media (max-width:900px){
  .burger{display:block}
  .shell{grid-template-columns:minmax(0,1fr);padding:0 20px}
  .side{
    position:fixed;top:var(--head);left:0;bottom:0;width:282px;z-index:50;
    background:var(--bg);border-right:1px solid var(--border);padding:20px 12px 40px;
    transform:translateX(-102%);transition:transform .2s ease;
  }
  body.open .side{transform:none}
  body.open .scrim{opacity:1;pointer-events:auto}
  .search{width:130px}
  main{padding:26px 0 56px}
  .prose h1{font-size:1.72rem}
  .pager{grid-template-columns:1fr}
  .pg.next{grid-column:1;text-align:left}
}
@media (max-width:560px){
  /* collapse to a magnifier; expand on focus so the field is still usable */
  .search{
    width:34px;padding:0;color:transparent;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235f6672' stroke-width='2' stroke-linecap='round'><circle cx='11' cy='11' r='7'/><path d='M20 20l-3.6-3.6'/></svg>");
    background-repeat:no-repeat;background-position:center;background-size:16px;
  }
  .search::placeholder{color:transparent}
  .search:focus{width:190px;padding:0 12px;color:var(--text);background-image:none}
  .search:focus::placeholder{color:var(--muted)}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--head) + 16px)}
"""


JS = r"""
(function () {
  var root = document.documentElement;

  /* theme -------------------------------------------------------------- */
  var btn = document.getElementById('theme');
  if (btn) btn.addEventListener('click', function () {
    var dark = getComputedStyle(root).getPropertyValue('color-scheme').trim() === 'dark';
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  /* search ------------------------------------------------------------- */
  var q = document.getElementById('q');
  var box = document.getElementById('results');
  var idx = window.SEARCH_INDEX || [];
  var base = window.SEARCH_BASE || '';
  var hits = [], sel = -1;

  function score(page, term) {
    var t = page.t.toLowerCase(), s = 0;
    if (t === term) s += 100;
    if (t.indexOf(term) === 0) s += 60;
    else if (t.indexOf(term) > -1) s += 40;
    for (var i = 0; i < page.h.length; i++) {
      if (page.h[i].toLowerCase().indexOf(term) > -1) { s += 14; break; }
    }
    if (page.b.toLowerCase().indexOf(term) > -1) s += 5;
    return s;
  }

  function render() {
    if (!hits.length) {
      box.innerHTML = '<div class="r-none">No matches</div>';
    } else {
      box.innerHTML = hits.map(function (h, i) {
        return '<a class="' + (i === sel ? 'sel' : '') + '" href="' + base + h.u + '">' +
               '<div class="r-t">' + h.t + '</div>' +
               (h.g ? '<div class="r-g">' + h.g + '</div>' : '') + '</a>';
      }).join('');
    }
    box.hidden = false;
  }

  function close() { box.hidden = true; sel = -1; }

  if (q) {
    q.addEventListener('input', function () {
      var term = q.value.trim().toLowerCase();
      if (term.length < 2) return close();
      hits = idx.map(function (p) { return { p: p, s: score(p, term) }; })
                .filter(function (r) { return r.s > 0; })
                .sort(function (a, b) { return b.s - a.s; })
                .slice(0, 8)
                .map(function (r) { return r.p; });
      sel = -1;
      render();
    });

    q.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { q.blur(); return close(); }
      if (box.hidden || !hits.length) return;
      if (e.key === 'ArrowDown') { e.preventDefault(); sel = (sel + 1) % hits.length; render(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = (sel - 1 + hits.length) % hits.length; render(); }
      else if (e.key === 'Enter' && sel > -1) { e.preventDefault(); location.href = base + hits[sel].u; }
    });

    document.addEventListener('click', function (e) {
      if (!box.contains(e.target) && e.target !== q) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== q) { e.preventDefault(); q.focus(); }
    });
  }

  /* table of contents highlight ---------------------------------------- */
  var links = [].slice.call(document.querySelectorAll('.toc a'));
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var seen = [];
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var id = en.target.id;
        var i = seen.indexOf(id);
        if (en.isIntersecting && i < 0) seen.push(id);
        if (!en.isIntersecting && i > -1) seen.splice(i, 1);
      });
      links.forEach(function (a) { a.classList.remove('here'); });
      if (seen.length) {
        var first = links.filter(function (a) {
          return seen.indexOf(a.getAttribute('href').slice(1)) > -1;
        })[0];
        if (first) first.classList.add('here');
      }
    }, { rootMargin: '-70px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }

  /* close the mobile drawer when a link is followed --------------------- */
  document.querySelectorAll('.side a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('open'); });
  });
})();
"""
