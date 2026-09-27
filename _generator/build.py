import os, json, datetime
from lib import *
import home, svc_a, svc_b, svc_c, hubs, locations
from svc_builder import build_service

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TODAY = datetime.date.today().isoformat()

def write(rel, content):
    fp = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)

urls = []
write("index.html", home.build()); urls.append(("/", "1.0"))
for build_fn in (hubs.services_page, hubs.areas_page):
    path, html = build_fn()
    write(path.lstrip("/") + ".html", html); urls.append((path, "0.9"))
for s in svc_a.PAGES + svc_b.PAGES + svc_c.PAGES:
    path, html = build_service(s)
    write(path.lstrip("/") + ".html", html); urls.append((path, "0.8"))
for l in locations.PAGES:
    path, html = locations.build_location(l)
    write(path.lstrip("/") + ".html", html); urls.append((path, "0.8"))

# Location pages moved from /service-areas/<slug> to /fl/<slug>
import shutil
shutil.rmtree(os.path.join(OUT, "service-areas"), ignore_errors=True)

# The junk removal service page was folded into the homepage
old = os.path.join(OUT, "service", "junk-removal.html")
if os.path.exists(old):
    os.remove(old)

# 404
nf_body = f'''<section class="section"><div class="wrap"><div class="content" style="text-align:center">
<h1>Page Not Found</h1><p>The page you are looking for has moved. Try one of our Homestead junk removal services below or call {PHONE}.</p>
<p>{call_btn()}</p></div></div></section>''' + service_cards("Popular Junk Removal Services in Homestead", "", alt_bg=True)
nf = page("/404", "Page Not Found | " + BRAND, "Page not found.", nf_body, [], [("Home", "/"), ("404", None)])
nf = nf.replace('content="index, follow, max-image-preview:large"', 'content="noindex, follow"')
write("404.html", nf)

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, pr in urls:
    sm.append(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
sm.append("</urlset>")
write("sitemap.xml", "\n".join(sm))
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

vercel = {
  "cleanUrls": True,
  "trailingSlash": False,
  "redirects": [
    {"source": "/service", "destination": "/services", "permanent": True},
    {"source": "/service/junk-removal", "destination": "/", "permanent": True},
    {"source": "/service-areas/:city", "destination": "/fl/:city", "permanent": True},
    {"source": "/fl", "destination": "/service-areas", "permanent": False},
    {"source": "/areas", "destination": "/service-areas", "permanent": True},
    {"source": "/locations", "destination": "/service-areas", "permanent": True},
    {"source": "/index", "destination": "/", "permanent": True}
  ],
  "headers": [
    {"source": "/assets/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/assets/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"}]},
    {"source": "/(.*)", "headers": [
      {"key": "X-Content-Type-Options", "value": "nosniff"},
      {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
      {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}
  ]
}
write("vercel.json", json.dumps(vercel, indent=2))
print("\n".join(u for u, _ in urls))
