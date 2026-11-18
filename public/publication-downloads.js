/* Track opted-in PDF link clicks via GTM without overriding GA4 file_download.
   Direct PDF requests, actual download success and declined analytics cannot be
   measured from a static client-side site. */
(function () {
  'use strict';
  document.addEventListener('click', function (event) {
    const link = event.target.closest && event.target.closest('a[href]');
    if (!link || !window.meyoInsightsAnalyticsAllowed || !window.meyoInsightsAnalyticsAllowed()) return;
    let url;
    try { url = new URL(link.href, window.location.href); }
    catch (_) { return; }
    if (url.origin !== window.location.origin || !/^\/reports\/.*\.pdf$/i.test(url.pathname)) return;

    const article = link.closest('[data-research-article]');
    const filename = url.pathname.split('/').pop();
    const historical = filename.match(/-v(\d+)-(\d+)\.pdf$/i);
    const version = historical ? historical[1] + '.' + historical[2] : (article?.dataset.publicationVersion || 'unversioned');
    const documentId = article?.dataset.publicationId || filename.replace(/(?:-v\d+-\d+)?\.pdf$/i, '');
    const location = link.closest('[data-section-id="change-log"]') ? 'change_log'
      : link.closest('.download-publication') ? 'article_download'
      : link.closest('.prior-editions') ? 'previous_editions'
      : 'article_body';

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'publication_download',
      publication_id: documentId,
      publication_version: version,
      publication_title: article?.dataset.publicationTitle || documentId,
      download_location: location,
      file_name: filename,
      file_extension: 'pdf',
      link_url: url.href
    });
  });

  // Open historical PDFs in a separate tab; the reporting page stays available
  // and in-flight consented events are less likely to be interrupted.
  document.querySelectorAll('a[href*="/reports/"][href$=".pdf"]:not([download])').forEach(function (link) {
    if (!link.target) {
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
    }
  });
})();
