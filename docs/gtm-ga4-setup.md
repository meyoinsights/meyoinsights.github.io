# Meyo Insights — Google Analytics through Google Tag Manager

**Website:** https://meyoinsights.github.io/  
**Google Tag Manager container:** `GTM-N667W382`  
**Google Analytics 4 web-stream Measurement ID:** `G-7JFK77TPEN`  
**Status:** Website container implementation is staged in PR #5. Creating/publishing the GA4 tag inside GTM is an **owner-controlled action** not performed by this repository.

## One-time setup in Google Tag Manager

1. Go to https://tagmanager.google.com/ and open the website container **GTM-N667W382**.
2. Under **Workspace → Tags → New → Tag Configuration**, select **Google tag**.
3. Enter **G-7JFK77TPEN** in the **Tag ID** field.
4. Set a single **Initialization — All Pages** trigger (or the equivalent site-wide initialization trigger in the active GTM interface). This container itself is loaded only after the visitor has accepted optional analytics on the website.
5. In the tag's **Consent Settings**, confirm that `analytics_storage` consent is respected. Do not add marketing/advertising tags as part of this change.
6. Click **Preview**, connect to `https://meyoinsights.github.io/`, choose **Accept analytics** and confirm the Google tag fires once; without acceptance no Google Tag Manager script should be requested.
7. **Submit / Publish** the GTM container changes. A draft tag in GTM does not send production traffic.
8. Check **Google Analytics → Reports → Realtime** for a consented visit and verify a single `page_view` event per page load. You may need to allow time for reports to populate.

**Important:** Do **not** also add the `G-7JFK77TPEN` `gtag.js` snippet directly to Astro. The public website hosts the consent-gated GTM container. GA4 is configured **inside GTM** to avoid duplicate tracking.

## Website rollout

- Review and merge [PR #5](https://github.com/meyoinsights/meyoinsights.github.io/pull/5) after checks pass.
- Confirm GitHub Pages redeploys successfully.
- With a new/private browser session, inspect Network requests: before any choice, there should be **no request** to `googletagmanager.com/gtm.js`; after **Accept analytics**, it should load.
- Reload after choosing **Decline** and verify no GTM script loads.
- Use **Analytics settings** in the footer to change consent. Existing GA4 data is not erased by resetting browser consent.
- Follow up separately on Google Search Console verification and sitemap submission.

The GTM and GA4 identifiers are public configuration values, not credentials. Never commit Google-account access tokens or GTM API secrets.

Official instructions: https://support.google.com/tagmanager/answer/9442095 and https://support.google.com/tagmanager/answer/6107056
