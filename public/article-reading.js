/* Native accessible article navigation for all long-form publications. */
(function () {
  'use strict';
  const article = document.querySelector('[data-research-article]');
  if (!article) return;
  const sections = Array.from(article.querySelectorAll('details[data-article-section]'));
  if (!sections.length) return;

  const expand = article.querySelector('[data-expand-sections]');
  const collapse = article.querySelector('[data-collapse-sections]');
  if (expand) expand.addEventListener('click', function () {
    sections.forEach(function (section) { section.open = true; });
  });
  if (collapse) collapse.addEventListener('click', function () {
    sections.forEach(function (section) { section.open = false; });
  });

  function revealHash() {
    if (!window.location.hash) return;
    let id;
    try { id = decodeURIComponent(window.location.hash.slice(1)); }
    catch (_) { return; }
    const target = document.getElementById(id);
    if (!target || !article.contains(target)) return;
    const section = target.closest('details[data-article-section]');
    if (section) section.open = true;
    window.requestAnimationFrame(function () { target.scrollIntoView({block:'start'}); });
  }

  article.addEventListener('click', function (event) {
    const link = event.target.closest && event.target.closest('a[href^="#"]');
    if (!link) return;
    let hash;
    try { hash = decodeURIComponent(link.getAttribute('href').slice(1)); }
    catch (_) { return; }
    const target = document.getElementById(hash);
    if (!target || !article.contains(target)) return;
    const section = target.closest('details[data-article-section]');
    if (section) section.open = true;
  });
  window.addEventListener('hashchange', revealHash);
  revealHash();
})();
