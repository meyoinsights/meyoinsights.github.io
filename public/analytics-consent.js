/* Optional, consent-gated analytics for Meyo Insights.
   GTM is never requested until the visitor explicitly accepts.
   Configure a GA4 Google tag inside GTM; do not also add gtag.js to Astro.
*/
(function () {
  'use strict';

  const CONTAINER_ID = 'GTM-N667W382';
  const KEY = 'meyo-insights-analytics-v1';
  const banner = document.getElementById('analytics-consent');
  const accept = document.getElementById('analytics-accept');
  const reject = document.getElementById('analytics-decline');
  const settings = document.getElementById('analytics-preferences');
  if (!banner || !accept || !reject || !settings) return;

  let loaded = false;

  function savedChoice() {
    try { return window.localStorage.getItem(KEY); } catch (_) { return null; }
  }
  function persistChoice(value) {
    try { window.localStorage.setItem(KEY, value); } catch (_) { /* Storage may be blocked. */ }
  }

  function startTagManager() {
    if (loaded) return;
    loaded = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };

    // Basic consent mode: default to denied before initializing the container.
    window.gtag('consent', 'default', {
      analytics_storage: 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    window.gtag('consent', 'update', {
      analytics_storage: 'granted'
    });
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });

    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(CONTAINER_ID);
    document.head.appendChild(script);
  }

  function select(choice) {
    const previouslyLoaded = loaded;
    persistChoice(choice);
    banner.hidden = true;

    if (choice === 'granted') {
      startTagManager();
    } else if (previouslyLoaded) {
      // Deny immediately, then reload so no GTM script remains on this page.
      if (typeof window.gtag === 'function') {
        window.gtag('consent', 'update', {
          analytics_storage: 'denied',
          ad_storage: 'denied',
          ad_user_data: 'denied',
          ad_personalization: 'denied'
        });
      }
      window.location.reload();
    }
  }

  accept.addEventListener('click', function () { select('granted'); });
  reject.addEventListener('click', function () { select('denied'); });
  settings.addEventListener('click', function () {
    banner.hidden = false;
    accept.focus();
  });

  const current = savedChoice();
  if (current === 'granted') {
    startTagManager();
  } else if (current !== 'denied') {
    banner.hidden = false;
  }
})();
