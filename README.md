# Junk Removal Homestead (junkremovalhomesteadfl.com)

Static, fast loading rank and rent site for junk removal in Homestead, FL. Plain HTML, CSS and JS with no build step.

## Deploy on Vercel
1. Create a new GitHub repo and upload the contents of this folder (index.html must be at the repo root).
2. In Vercel: Add New Project > Import the repo > Framework Preset: **Other** > leave Build Command and Output Directory empty > Deploy.
3. Add the domain `junkremovalhomesteadfl.com` under Project Settings > Domains.
4. Submit `https://junkremovalhomesteadfl.com/sitemap.xml` in Google Search Console.

`vercel.json` enables clean URLs, so `/service/junk-removal.html` is served at `/service/junk-removal`.

## Pages
- `/` homepage
- `/service/junk-removal`, `/service/furniture-removal`, `/service/appliance-removal`, `/service/dumpster-rental`,
  `/service/construction-debris-removal`, `/service/yard-waste-removal`, `/service/garage-cleanout`,
  `/service/estate-cleanout`, `/service/commercial-junk-removal`, `/service/hurricane-debris-removal`

## Site structure
- `/` homepage (targets "junk removal Homestead"), `/services` hub, `/service/<slug>` service pages
- `/service-areas` hub, `/fl/<city>` location pages (content in `_generator/locations.py`)
- `/blog` and `/blog/<slug>` guides (content in `_generator/blogs.py`)
- Internal links sit only in headings (H2/H3 and card titles), never inside paragraphs.

## SEO and lead features
- Quick Answer blocks (question H2, a 40 to 60 word answer and a key facts panel) near the top of the homepage, service and location pages, written to be quoted by Google AI Overviews and featured snippets.
- Price estimator on the homepage, the services hub and every location page (`assets/js/main.js`). Tiers match the published price tables.
- Item price guide on `/services` for long-tail searches such as "hot tub removal cost".
- Structured data: LocalBusiness with GeoCircle service area, contact point and ZIP-level areaServed; Service nodes with AggregateOffer and an OfferCatalog built from each price table; BlogPosting with key takeaways and entity links.
- `llms.txt` and an AI-crawler-friendly `robots.txt`.
- Phone clicks push a `phone_call_click` event to `dataLayer` and `gtag`, ready for GA4 or Google Tag Manager.
- Prices and content dates live in `_generator/seo.py` (`UPDATED`). Update them whenever prices change.

## Calls only
There is no contact form. Every call to action dials 877-745-9845 (set in `_generator/lib.py`).

## Editing content
All pages are generated from `_generator/` (Python 3 + Pillow):
```
pip install pillow
python _generator/build.py
```
Phone, hours, service areas and the service list live at the top of `_generator/lib.py`. Page copy lives in
`home.py`, `svc_a.py`, `svc_b.py`, `svc_c.py`, `hubs.py`, `locations.py` and `blogs.py`. The `_generator` folder is excluded from deploys by `.vercelignore`.

## Before renting the site
Prices, truck size, hours and service promises are typical placeholders for the Homestead market. Confirm them with the business
that rents the site and update them so everything on the page is accurate.
