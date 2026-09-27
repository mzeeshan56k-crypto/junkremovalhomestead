from lib import *

def build_service(s):
    path = f"/service/{s['slug']}"
    crumbs = [("Home", "/"), ("Services", "/#services"), (SVC[s['slug']][1], None)]
    b = [
        hero(s["h1"], s["lead"], s["points"], s["hero_img"], s["hero_alt"], crumbs=crumbs, eyebrow=s.get("eyebrow", "Homestead, FL"), selected=SVC[s["slug"]][1]),
        trust(),
        split(s["intro_h2"], s["intro_html"], s["intro_img"], s["intro_alt"], badge=s.get("badge"), eyebrow=s["name"]),
        prose(s["body_html"], alt_bg=True),
        steps(s["steps_h2"], s["steps_p"], s["steps"], alt_bg=False),
        pricing(s["price_h2"], s["price_intro"], s["headers"], s["rows"], s["note"], alt_bg=True),
        split(s["local_h2"], s["local_html"], s["local_img"], s["local_alt"], rev=True, eyebrow="Local Know How"),
        related(s["related_h2"], s["related_p"], s["related"]),
        areas(s["areas_h2"], s["areas_p"]),
        faq(s["faq_h2"], s["faq_p"], s["faqs"]),
        cta(s["cta_h2"], s["cta_p"]),
    ]
    svc = {"name": s["schema_name"], "type": s["name"], "min": s["min"]}
    return path, page(path, s["title"], s["desc"], "\n".join(b), s["faqs"], crumbs, service=svc)
