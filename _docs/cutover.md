# Moving datainsightonline.com from Wix to GitHub Pages

A checklist for switching the domain to the new site. Plan about an hour of work, then up to a day of waiting for DNS changes to spread.

## How the domain is set up today

The domain is registered with an outside registrar, but its **nameservers point to Wix** (`ns8.wixdns.net` and `ns9.wixdns.net`). That means Wix, not the registrar, currently answers every DNS question for the domain. The switch therefore has two parts: point the nameservers back to the registrar, and create the GitHub Pages records there.

The domain has no email (MX) records, so no email can break.

The new site will be served at **www.datainsightonline.com**, the same address Wix used, so every existing link and search ranking carries over. The bare domain (datainsightonline.com) will redirect to it.

## Before the switch (a few days ahead)

1. **Merge every pending site change** and check the preview at https://aai-services.github.io/datainsightonline/.
2. **Record the current DNS setup** for rollback: in the Wix dashboard, open Domains, then the domain's DNS records, and take a screenshot.
3. **Verify the domain for the GitHub organization.** This stops anyone else from ever claiming it on GitHub.
   - GitHub, `aai-services` organization, Settings, Pages, **Add a domain**: enter `datainsightonline.com`.
   - GitHub shows a TXT record (name starting with `_github-pages-challenge-aai-services`, and a value). Keep that page open; you add the record in step 6.
4. **Find the registrar's DNS settings.** Log in to the registrar and find where to change nameservers and where to edit DNS records. Most registrars include DNS hosting for free.

## Switch day

5. **Set the custom domain on the repository first.** GitHub asks for this before DNS changes, so no one else can claim the address in between.
   - `aai-services/datainsightonline`, Settings, Pages, Custom domain: enter `www.datainsightonline.com` and save. It will show a DNS warning until step 7 is done; that is expected.
6. **At the registrar, create these records** in its own DNS zone:

   | Type | Name | Value |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | AAAA | @ | 2606:50c0:8000::153 |
   | AAAA | @ | 2606:50c0:8001::153 |
   | AAAA | @ | 2606:50c0:8002::153 |
   | AAAA | @ | 2606:50c0:8003::153 |
   | CNAME | www | aai-services.github.io |
   | TXT | the name GitHub gave in step 3 | the value GitHub gave in step 3 |

   Some registrars only let you edit records after the nameservers point to them. If so, do step 7 first and add the records straight after.
7. **Change the nameservers** from the Wix ones back to the registrar's default nameservers.
8. **Wait.** Changes usually spread within a few hours, and at most about 48 hours. During that time some visitors still see the Wix site; both work.
9. **Finish in GitHub:**
   - Organization Settings, Pages: click **Verify** next to the domain.
   - Repository Settings, Pages: once the DNS check shows as successful, tick **Enforce HTTPS**. The certificate can take up to an hour to be issued.

## Checks after the switch

Open each of these; all should load the new site:

- https://www.datainsightonline.com
- https://datainsightonline.com (should redirect to www)
- https://www.datainsightonline.com/post/programming-for-data-science
- https://www.datainsightonline.com/data-scientist-program (should redirect to the Program page)
- https://www.datainsightonline.com/product-page/python-for-data-science (should redirect to Resources)
- https://www.datainsightonline.com/ads.txt (should show the single AdSense line)

## Search and ads

- **Google Search Console:** the site's verification tags were carried over to the new site, so the property should stay verified. Open the property, then Sitemaps, and submit `sitemap.xml`.
- **AdSense:**
  - Sites: confirm datainsightonline.com shows as ready and ads.txt as authorized. After a platform change, AdSense can take a few days to re-check the site; ads may pause briefly.
  - Privacy & messaging: create and publish a **European regulations** message (Google's consent notice for the EEA, the UK, and Switzerland). The privacy page already describes it.

## After the switch

- In the Wix dashboard, **disconnect the domain** from the Wix site.
- Keep the Wix plan for 2 to 4 weeks in case anything needs to be recovered, then cancel it.

## Rolling back

If something goes badly wrong, set the nameservers back to `ns8.wixdns.net` and `ns9.wixdns.net`. The Wix site returns as the changes spread.
