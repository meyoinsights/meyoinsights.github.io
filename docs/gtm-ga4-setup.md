# Meyo Insights — GA4 and Google Tag Manager setup

Last updated: 18 November 2026.

Use this runbook to recreate website analytics and publication PDF tracking after a migration or configuration loss, or to onboard another maintainer. The website implementation is deployed (PRs [#5](https://github.com/meyoinsights/meyoinsights.github.io/pull/5) and [#14](https://github.com/meyoinsights/meyoinsights.github.io/pull/14)). The owner reported completing the GTM/GA4 configuration on 18 November 2026; this repository does not independently verify the live Google account settings or received analytics data.

## 1. Configuration inventory

| Item | Value |
| --- | --- |
| Website | https://meyoinsights.github.io/ |
| GTM container | GTM-N667W382 |
| GA4 web stream measurement ID | G-7JFK77TPEN |
| Custom event | publication_download |
| Consent script | public/analytics-consent.js |
| Download event script | public/publication-downloads.js |
| Shared publication template | src/layouts/ArticleLayout.astro |
| Owner access | Google Tag Manager and Google Analytics |

Verify the container and measurement IDs in the destination account before recreating the setup. They are public configuration identifiers, not secrets.

The site loads GTM only after explicit optional analytics consent. Do not install a second gtag.js snippet directly in Astro. It can duplicate page views and circumvent the intended consent boundary. Do not add marketing or advertising tags as part of this setup.

## 2. Set up the base Google tag (one time)

1. Open [Google Tag Manager](https://tagmanager.google.com/) and select container GTM-N667W382.
2. Under Workspace → Tags → New → Tag Configuration, select **Google tag**.
3. Enter G-7JFK77TPEN as the Tag ID.
4. Use Initialization — All Pages (or the equivalent site-wide initialization trigger); the website itself loads the container only after consent.
5. Check Consent Settings and ensure analytics_storage is respected. Leave advertising consent denied.
6. Save. Use Preview and connect to the website; accept analytics and confirm the Google tag fires once. Check that GA4 receives one page_view per page load.

If the existing base Google tag is already correct, reuse it rather than creating another.

## 3. Create the publication download trigger

In GTM, select Workspace → Triggers → New.

| Field | Value |
| --- | --- |
| Name | Publication Download |
| Trigger type | Custom Event |
| Event name | publication_download |
| Use regex matching | Off |
| Fires on | All Custom Events |

Save the trigger.

The website pushes the custom event only for consented clicks on same-origin PDFs within /reports/. It includes historic editions under /reports/versions/. Do not use a page_view matching rule to count downloads.

## 4. Create Data Layer Variables

Go to Workspace → Variables → User-Defined Variables → New → Data Layer Variable. Create the following six variables. For each, choose Data Layer Version 2, leave Set Default Value unchecked and save.

| GTM variable name | Data Layer Variable Name |
| --- | --- |
| DLV - Publication ID | publication_id |
| DLV - Publication Version | publication_version |
| DLV - Publication Title | publication_title |
| DLV - Download Location | download_location |
| DLV - File Name | file_name |
| DLV - Link URL | link_url |

The site additionally sends file_extension=pdf; it can be mapped to an optional seventh variable if required. It is not necessary for this publication-only report.

## 5. Create the GA4 event tag

Go to Workspace → Tags → New → Tag Configuration → Google Analytics: GA4 Event.

- Tag name: GA4 - Publication Download
- Measurement ID: G-7JFK77TPEN (use the existing Google tag configuration)
- Event name: publication_download

Under Event Parameters, add these rows. Select the matching GTM variable with the variable picker rather than entering the variable name as literal text.

| Event parameter | Value |
| --- | --- |
| publication_id | `{{DLV - Publication ID}}` |
| publication_version | `{{DLV - Publication Version}}` |
| publication_title | `{{DLV - Publication Title}}` |
| download_location | `{{DLV - Download Location}}` |
| file_name | `{{DLV - File Name}}` |
| link_url | `{{DLV - Link URL}}` |

Select the **Publication Download** custom event trigger under Triggering. Confirm consent settings respect analytics_storage. Save.

## 6. Test and publish the GTM container

1. Click Preview in GTM and connect Tag Assistant to https://meyoinsights.github.io/.
2. Accept analytics on the site. Navigate to the [KPC article](https://meyoinsights.github.io/blog/kenya-pipeline-is-share-price-justified/).
3. Click the main PDF download link once.
4. In Tag Assistant, select publication_download and verify GA4 - Publication Download fired once. Check the Data Layer/Variables values:
   - publication_id: kenya-pipeline-is-share-price-justified
   - publication_version: current displayed edition (1.2 at the time of this guide)
   - publication_title: the full article title
   - download_location: article_download
   - file_name: kenya-pipeline-is-share-price-justified.pdf
   - link_url: full same-origin PDF URL.
5. Repeat with an archived PDF: the version should match the archived edition (for example 1.1); the placement should match previous_editions or change_log on the current article.
6. Start a fresh private browser session: verify no GTM network request before consent; decline analytics and confirm no custom download event is sent. Verify the PDF still opens. Test changing consent using Analytics settings in the footer.
7. In GA4, check Admin → DebugView (when debug traffic is enabled), and Reports → Realtime for the custom event. Test traffic may not appear in normal reports if developer/internal traffic filters exclude it.
8. Once the tests pass, click Submit → Publish in GTM. Record the container version and description, such as “Publication download tracking — event and dimensions”.
9. Test once again on the live site outside Preview using consented traffic.

### Avoid duplicate counts

GA4's Enhanced Measurement can also emit file_download when a PDF link is clicked. It is a separate standard event: do not add the two event counts together.

If GA4 contains a rule that creates publication_download from page_view or file_download, remove that rule once the GTM-based event is active. GTM must be the sole source of the custom event. Do not delete the standard file_download event itself just to remove a duplicate derived rule. Check Admin → Data display → Events and the Create events/custom-event configuration.

## 7. Register GA4 custom dimensions

In [Google Analytics](https://analytics.google.com/), select the correct property. Go to Admin → Data display → Custom definitions → Create custom dimension.

| Dimension name | Scope | Event parameter |
| --- | --- | --- |
| Publication ID | Event | publication_id |
| Publication Version | Event | publication_version |
| Publication Title | Event | publication_title |
| Download Location | Event | download_location |

Create each once. Use the exact lowercase event parameter names. Standard GA4 dimensions for file name or link URL can be used if populated; create additional event-scoped dimensions only if needed. Allow 24–48 hours for normal reporting after collection begins. Custom definitions do not retroactively populate historical reporting dimensions.

If downloads are a key business outcome, optionally mark publication_download as a key event in GA4. This is not required for collection.

## 8. Publication performance report

In GA4 → Explore → Free form, create a report with Event count as the metric, Publication ID / Publication Title as rows, and Publication Version or Download Location as breakdowns. Filter Event name to exactly publication_download. Add Session source / medium if appropriate to investigate acquisition sources.

To assess article-to-download conversion, use a funnel with article page_view followed by publication_download (or another explicitly defined session/user conversion). Event count divided by page view count is a click-per-view ratio, not necessarily the fraction of unique readers who downloaded.

Interpretation: the custom event measures observed, consented PDF link clicks, not proven successful transfers or unique downloads. Direct PDF requests from external sites, blocked analytics, declined consent, and some interrupted browser sessions are unobserved. Do not report these counts as total PDF downloads across the internet.

## 9. Future publications and maintenance

All articles using the shared ArticleLayout automatically expose the article identifier, version and title, and PDF links are detected by the shared download script. Use the existing /reports/ and /reports/versions/ routing conventions. No new custom event or GTM trigger is needed for each report. Test a new article and its archived PDF links during release checks.

If data stops arriving, check in this order: correct property/container → consent choice → GTM network request → dataLayer event in Tag Assistant → trigger/tag firing → published GTM version → GA4 DebugView/Realtime → custom definitions and report filters. Keep account credentials out of repository documentation. Save an export of the GTM container in approved private storage when its configuration changes, not in the public site repository.

Official Google documentation: [Google tag in GTM](https://support.google.com/tagmanager/answer/9442095), [GA4 event tags](https://support.google.com/tagmanager/answer/13034206), [Custom definitions](https://support.google.com/analytics/answer/10075209).

