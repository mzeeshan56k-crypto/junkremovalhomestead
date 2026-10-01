import os, re, json, datetime
from lib import *
import home, svc_a, svc_b, svc_c, hubs, locations, blogs, seo
from svc_builder import build_service

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TODAY = datetime.date.today().isoformat()

def minify_html(s):
    # Drop indentation and blank lines; inline spacing between words and tags is left untouched
    return re.sub(r"\n[ \t]+", "\n", re.sub(r"\n{2,}", "\n", s))

def write(rel, content):
    if rel.endswith(".html"):
        content = minify_html(content)
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
path, html = blogs.blog_index()
write("blog.html", html); urls.append((path, "0.7"))
for p in blogs.POSTS:
    path, html = blogs.build_post(p)
    write(path.lstrip("/") + ".html", html); urls.append((path, "0.7"))
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
nf = page("/404", "Page Not Found | " + BRAND, "Page not found.", nf_body, [], [("Home", "/"), ("404", None)], noindex=True)
write("404.html", nf)

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, pr in urls:
    # lastmod reflects when page content last changed, not the build date
    sm.append(f"<url><loc>{SITE}{u}</loc><lastmod>{blogs.UPDATED if u.startswith('/blog/') else seo.UPDATED_ISO}</lastmod></url>")
sm.append("</urlset>")
write("sitemap.xml", "\n".join(sm))
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "Bingbot"]
write("robots.txt", "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS) + f"Sitemap: {SITE}/sitemap.xml\n")

# llms.txt: a plain summary that AI assistants can read when answering local questions
import seo
llms = [f"# {BRAND}", "",
        f"> Local junk removal, dumpster rental and cleanout company serving Homestead, Florida (ZIP codes 33030 to 33035) and South Miami-Dade County. Phone: {PHONE}. {HOURS}.", "",
        "## Key facts",
        "- Junk removal in Homestead, FL typically costs $95 to $650, priced by how much of a 15-cubic-yard truck your items fill.",
        "- Same-day pickup is available when you call before noon. Labor, loading, travel and disposal are included.",
        "- Dumpster rentals: 10-yard $295 to $375, 15-yard $365 to $450, 20-yard $425 to $525, including 7 days.",
        f"- Prices last updated {seo.UPDATED}. Final prices are confirmed on site before work begins.", "",
        "## Services"] + \
       [f"- [{SVC[s['slug']][2]}]({SITE}/service/{s['slug']}): {seo.SVC_QA[s['slug']]}" for s in svc_a.PAGES + svc_b.PAGES + svc_c.PAGES] + \
       ["", "## Service areas", f"- [Homestead, FL]({SITE}/): ZIP codes 33030, 33031, 33032, 33033, 33035 and 33039"] + \
       [f"- [{locations.place(l['name'])[0].upper() + locations.place(l['name'])[1:]}, FL]({SITE}{loc_url(l['name'])}): ZIP {l['zips']}" for l in locations.PAGES] + \
       ["", "## Guides"] + [f"- [{strip(p['title'])}]({SITE}/blog/{p['slug']}): {p['desc']}" for p in blogs.POSTS]
write("llms.txt", "\n".join(llms) + "\n")

vercel = {
  "cleanUrls": True,
  "trailingSlash": False,
  "redirects": [
    {"source": "/service", "destination": "/services", "permanent": True},
    {"source": "/service/junk-removal", "destination": "/", "permanent": True},
    {"source": "/service-areas/:city(florida-city|cutler-bay|leisure-city|princeton|redland)", "destination": "/fl/:city", "permanent": True},
    {"source": "/fl", "destination": "/service-areas", "permanent": True},
    {"source": "/areas", "destination": "/service-areas", "permanent": True},
    {"source": "/locations", "destination": "/service-areas", "permanent": True},
    {"source": "/index", "destination": "/", "permanent": True},
    {"source": "/:path*", "has": [{"type": "host", "value": "www.junkremovalhomesteadfl.com"}], "destination": "https://junkremovalhomesteadfl.com/:path*", "permanent": True},
    {"source": "/:path*", "has": [{"type": "host", "value": "junkremovalhomestead.com"}], "destination": "https://junkremovalhomesteadfl.com/:path*", "permanent": True},
    {"source": "/:path*", "has": [{"type": "host", "value": "www.junkremovalhomestead.com"}], "destination": "https://junkremovalhomesteadfl.com/:path*", "permanent": True}
  ],
  "headers": [
    {"source": "/assets/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/assets/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/(.*)", "headers": [
      {"key": "X-Content-Type-Options", "value": "nosniff"},
      {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
      {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}
  ]
}
write("vercel.json", json.dumps(vercel, indent=2))

# Minified script (edit main.js; main.min.js is generated). CSS is minified and inlined by lib.py
import rjsmin
write("assets/js/main.min.js", rjsmin.jsmin(open(os.path.join(OUT, "assets/js/main.js")).read()))
print("\n".join(u for u, _ in urls))
