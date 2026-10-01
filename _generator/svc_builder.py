from lib import *
import zips, seo

def build_service(s):
    faqs = s["faqs"] + [zips.service_faq(s["slug"], s["name"])]
    lo, hi = seo.price_range(s["rows"], s["min"])
    path = f"/service/{s['slug']}"
    crumbs = [("Home", "/"), ("Services", "/services"), (SVC[s['slug']][1], None)]
    b = [
        hero(s["h1"], s["lead"], s["points"], s["hero_img"], s["hero_alt"], crumbs=crumbs, eyebrow=s.get("eyebrow", "Homestead, FL 33030"), selected=SVC[s["slug"]][1]),
        trust(),
        seo.service_qa(s, lo, hi),
        split(s["intro_h2"], s["intro_html"], s["intro_img"], s["intro_alt"], badge=s.get("badge"), eyebrow=s["name"]),
        prose(s["body_html"], alt_bg=True),
        steps(s["steps_h2"], s["steps_p"], s["steps"], alt_bg=False),
        pricing(s["price_h2"], s["price_intro"], s["headers"], s["rows"], s["note"] + f" Prices updated {seo.UPDATED}.", alt_bg=True),
        seo.cta_band(f"Want an exact price for {s['name'].lower()}? Call now for a free quote and same-day scheduling."),
        split(s["local_h2"], s["local_html"], s["local_img"], s["local_alt"], rev=True, eyebrow="Local Know How"),
        related(s["related_h2"], s["related_p"], s["related"]),
        zips.service_section(s["slug"], s["name"]),
        areas(s["areas_h2"], s["areas_p"]),
        faq(s["faq_h2"], s["faq_p"], faqs),
        cta(s["cta_h2"], s["cta_p"]),
    ]
    svc = {"name": s["schema_name"], "type": s["name"], "min": lo, "max": hi,
           "catalog": seo.offer_catalog(s["name"], SITE + path, s["rows"])}
    return path, page(path, s["title"], s["desc"], "\n".join(b), faqs, crumbs, service=svc)
