
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
