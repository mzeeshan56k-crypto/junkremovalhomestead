"""Shared templates and helpers for the static site generator."""
import json, os, html as H
from PIL import Image

SITE = "https://junkremovalhomestead.com"
BRAND = "Junk Removal Homestead"
PHONE = "877-745-9845"
TEL = "+18777459845"
CITY = "Homestead"
STATE = "FL"
HOURS = "Open 7 days, 7 AM to 7 PM"
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img")

SERVICES = [
    # slug, nav name, card title, card blurb, image
    ("furniture-removal", "Furniture Removal", "Furniture Removal Homestead",
     "Couches, sectionals, mattresses, dressers and patio sets hauled from any room, any floor, the same day you call.",
     "furniture-junk-pickup-homestead"),
    ("appliance-removal", "Appliance Removal", "Appliance Removal and Disposal",
     "Old refrigerators, washers, dryers, stoves and water heaters removed and recycled the right way.",
     "junk-hauling-truck-homestead"),
    ("dumpster-rental", "Dumpster Rental", "Dumpster Rental Homestead, FL",
     "Driveway friendly roll off dumpsters for cleanouts, roofing and remodels with flat rate pricing.",
     "roll-off-dumpster-rental-homestead"),
    ("construction-debris-removal", "Construction Debris Removal", "Construction Debris Removal",
     "Drywall, lumber, tile, cabinets and renovation waste cleared from job sites and garages.",
     "construction-dumpster-homestead-fl"),
    ("yard-waste-removal", "Yard Waste Removal", "Yard Waste Removal Homestead",
     "Palm fronds, branches, brush piles and storm limbs bagged and hauled so your lawn looks clean again.",
     "dumpster-trailer-loaded-homestead"),
    ("garage-cleanout", "Garage Cleanout", "Garage Cleanout Services",
     "Reclaim your garage. We sort, haul and donate so you can park inside again.",
     "garage-junk-pickup-carport-homestead"),
    ("estate-cleanout", "Estate Cleanout", "Estate Cleanout Homestead, FL",
     "Respectful whole house cleanouts for families, executors and realtors on a tight timeline.",
     "estate-cleanout-home-homestead"),
    ("commercial-junk-removal", "Commercial Junk Removal", "Commercial Junk Removal",
     "Office furniture, retail fixtures, warehouse pallets and property turnovers handled after hours if needed.",
     "commercial-debris-dumpster-homestead"),
    ("hurricane-debris-removal", "Hurricane Debris Removal", "Hurricane Debris Removal",
     "Fast storm cleanup for downed limbs, fencing, soaked drywall and damaged contents across South Dade.",
     "storm-debris-lumber-pile-homestead"),
]
SVC = {s[0]: s for s in SERVICES}
# The core "junk removal" keyword is targeted by the homepage, so links to it point to "/".
HOME_SVC = ("junk-removal", "Junk Removal", "Junk Removal in Homestead, FL")

def svc_url(slug):
    return "/" if slug == HOME_SVC[0] else f"/service/{slug}"

def svc_title(slug):
    return HOME_SVC[2] if slug == HOME_SVC[0] else SVC[slug][2]

# Areas that have their own location page, in menu order: name -> slug
LOC_PAGES = {"Florida City": "florida-city", "Cutler Bay": "cutler-bay", "Leisure City": "leisure-city",
             "Princeton": "princeton", "Redland": "redland"}

def loc_url(name):
    return f"/service-areas/{LOC_PAGES[name]}"

AREAS = [
    ("Homestead", "33030, 33033, 33035"),
    ("Florida City", "33034"),
    ("Leisure City", "33033"),
    ("Naranja", "33032"),
    ("Princeton", "33032"),
    ("Redland", "33031, 33170, 33187"),
    ("Homestead Base", "33039"),
    ("Modello", "33032"),
    ("Goulds", "33170"),
    ("Cutler Bay", "33189, 33190"),
    ("South Miami Heights", "33177"),
    ("Keys Gateway", "33034, 33035"),
]

ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "truck": '<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "dollar": '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "recycle": '<path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7L7.1 9.6M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7L19.3 14M14 16l-3 3 3 3M8.3 13.6 7.1 9.6 3.1 10.7M9.3 5.6a1.8 1.8 0 0 1 3.1 0l3.3 5.7M13.4 10.3l3.3-.1-.1-3.9"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "broom": '<path d="M19.4 2.6 13 9M8 11l5 5M3 21c3 0 7.6-1.3 9.8-5.2L8.2 11.2C4.3 13.4 3 18 3 21z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
}

def icon(name, cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

_dims = {}
def dims(fn):
    if fn not in _dims:
        _dims[fn] = Image.open(os.path.join(IMG_DIR, fn)).size
    return _dims[fn]

def img(base, alt, sizes="(max-width: 960px) 100vw, 50vw", eager=False, cls=""):
    """Responsive webp image. Uses the 1200 and 640 variants when present."""
    srcs = []
    for w in (640, 1200):
        fn = f"{base}-{w}.webp"
        if os.path.exists(os.path.join(IMG_DIR, fn)):
            srcs.append((fn, dims(fn)[0]))
    main = srcs[-1][0]
    w, h = dims(main)
    srcset = ", ".join(f"/assets/img/{f} {wd}w" for f, wd in srcs)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="/assets/img/{main}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{H.escape(alt)}" {load}{c}>')

def call_btn(cls="btn btn-primary", label=None):
    label = label or f"Call {PHONE}"
    return f'<a class="{cls}" href="tel:{TEL}">{icon("phone")}<span>{label}</span></a>'

def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

# ---------- Section builders ----------
def split(h2, body, image, alt, rev=False, badge=None, alt_bg=False, eyebrow=None, sid=None):
    b = f'<div class="badge">{badge}</div>' if badge else ""
    e = f'<span class="eyebrow dark">{eyebrow}</span>' if eyebrow else ""
    i = f' id="{sid}"' if sid else ""
    return f'''<section class="section{' alt' if alt_bg else ''}"{i}>
<div class="wrap split{' rev' if rev else ''}">
<div class="media reveal {'from-right' if rev else 'from-left'}">{img(image, alt)}{b}</div>
<div class="prose reveal {'from-left' if rev else 'from-right'}">{e}<h2>{h2}</h2>{body}</div>
</div></section>'''

def prose(body, alt_bg=False, sid=None):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="section{" alt" if alt_bg else ""}"{i}><div class="wrap"><div class="content reveal">{body}</div></div></section>'

def sec_head(h2, p="", eyebrow=None):
    e = f'<span class="eyebrow dark">{eyebrow}</span>' if eyebrow else ""
    pp = f"<p>{p}</p>" if p else ""
    return f'<div class="sec-head reveal">{e}<h2>{h2}</h2>{pp}</div>'

def service_cards(h2, p, exclude=None, alt_bg=False, sid="services", include_home=False):
    cards = []
    if include_home:
        cards.append(f'''<article class="card">
<figure>{img("junk-removal-truck-homestead-fl", f"Junk removal in Homestead, FL by {BRAND}", sizes="(max-width: 640px) 100vw, (max-width: 1080px) 50vw, 33vw")}</figure>
<div class="body"><h3><a href="/">Junk Removal in Homestead, FL</a></h3><p>Full service junk pickup for homes, condos and rentals. We lift, load, haul and sweep up so you never touch a thing.</p></div></article>''')
    for slug, nav, title, blurb, image in SERVICES:
        if slug == exclude:
            continue
        cards.append(f'''<article class="card">
<figure>{img(image, f"{title} by {BRAND}", sizes="(max-width: 640px) 100vw, (max-width: 1080px) 50vw, 33vw")}</figure>
<div class="body"><h3><a href="/service/{slug}">{title}</a></h3><p>{blurb}</p></div></article>''')
    return f'<section class="section{" alt" if alt_bg else ""}" id="{sid}"><div class="wrap">{sec_head(h2, p, "Our Services")}<div class="cards stagger">{"".join(cards)}</div></div></section>'

def steps(h2, p, items, alt_bg=True):
    out = []
    for title, text, ic in items:
        out.append(f'<div class="step"><div class="ic">{icon(ic)}</div><h3>{title}</h3><p>{text}</p></div>')
    return f'<section class="section{" alt" if alt_bg else ""}"><div class="wrap">{sec_head(h2, p, "How It Works")}<div class="steps stagger">{"".join(out)}</div></div></section>'

def pricing(h2, intro, headers, rows, note, alt_bg=False, sid="pricing"):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'''<section class="section{" alt" if alt_bg else ""}" id="{sid}"><div class="wrap">{sec_head(h2, intro, "Pricing")}
<div class="table-wrap reveal zoom"><table><caption class="sr-only">{h2}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>
<p class="table-note reveal">{note}</p></div></section>'''

GALLERY = [
    ("construction-debris-removal-before-after", "Garage Construction Debris Removal, Homestead",
     "Drywall, insulation and a broken tub cleared from a gutted garage in one truckload, about 12 cubic yards."),
    ("garage-cleanout-before-after-homestead", "Full Garage Cleanout, South Miami-Dade",
     "Lumber, an old fridge and years of clutter removed, then swept so the owner could use the workshop again."),
    ("yard-waste-removal-before-after-homestead", "Backyard Brush Pile Removal, Homestead",
     "Palm fronds, branches and a compost heap hauled away, leaving a clean bed ready for replanting."),
]
def gallery(h2, p, alt_bg=True):
    figs = []
    for i, (b, t, c) in enumerate(GALLERY):
        sizes = "(max-width: 960px) 100vw, 60vw" if i == 0 else "(max-width: 960px) 100vw, 40vw"
        figs.append(f'<figure class="ba ba-{i+1}">{img(b, t + " before and after", sizes=sizes)}<figcaption><h3>{t}</h3><p>{c}</p></figcaption></figure>')
    return (f'<section class="section{" alt" if alt_bg else ""}" id="before-after"><div class="wrap">{sec_head(h2, p, "Before and After")}'
            f'<div class="ba-grid stagger">{"".join(figs)}</div>'
            f'<div class="ba-cta reveal"><p>Want results like these at your property?</p>{call_btn("btn btn-primary pulse")}</div></div></section>')

def areas(h2, p, alt_bg=False, map_q="Homestead,+FL+33030", map_title="Homestead, Florida", sid="service-areas", show_all=True):
    lis = []
    for n, z in AREAS:
        name = f'<a href="{loc_url(n)}">{n}</a>' if n in LOC_PAGES else n
        lis.append(f'<li>{icon("pin")}<div><b>{name}</b><span>ZIP {z}</span></div></li>')
    mp = (f'<div class="map reveal"><iframe title="Junk removal service area map for {map_title}" '
          f'src="https://www.google.com/maps?q={map_q}&z=12&output=embed" loading="lazy" '
          'referrerpolicy="no-referrer-when-downgrade"></iframe></div>')
    more = '<p class="areas-more reveal"><a class="btn btn-outline-dark" href="/service-areas">View All Service Areas</a></p>' if show_all else ""
    return f'<section class="section{" alt" if alt_bg else ""}" id="{sid}"><div class="wrap">{sec_head(h2, p, "Service Areas")}<ul class="areas stagger">{"".join(lis)}</ul>{more}{mp}</div></section>'

def faq(h2, p, faqs, alt_bg=True):
    items = "".join(f'<details><summary><h3>{q}</h3></summary><div class="ans"><p>{a}</p></div></details>' for q, a in faqs)
    return f'<section class="section{" alt" if alt_bg else ""}" id="faq"><div class="wrap">{sec_head(h2, p, "FAQs")}<div class="faq stagger">{items}</div></div></section>'

def cta(h2, p):
    return f'''<section class="section"><div class="wrap"><div class="cta reveal zoom">
<div><h2>{h2}</h2><p>{p}</p></div>
<div class="actions"><a class="big-phone" href="tel:{TEL}">{PHONE}</a>{call_btn("btn btn-light pulse", "Call for a Free Quote")}</div>
</div></div></section>'''

def related(h2, p, items, alt_bg=True):
    arts = "".join(f'<article><h3><a href="{svc_url(s)}">{svc_title(s)}</a></h3><p>{t}</p></article>' for s, t in items)
    return f'<section class="section{" alt" if alt_bg else ""}"><div class="wrap">{sec_head(h2, p, "Related Services")}<div class="related stagger">{arts}</div></div></section>'

def call_card(selected=None):
    svc = selected or "Junk Removal"
    return f'''<div class="quote-card call-card" id="call">
<span class="eyebrow dark">{icon("clock")} {HOURS}</span>
<h2>Call for a Free {svc} Quote</h2>
<p>Talk to a local Homestead team and get an upfront price in minutes. No forms, no waiting.</p>
<a class="call-number" href="tel:{TEL}" aria-label="Call {PHONE}">{icon("phone")}<span>{PHONE}</span></a>
{call_btn("btn btn-primary pulse call-wide", "Tap to Call Now")}
<ul class="call-points">
<li>{icon("check")}Same day pickup when you call before noon</li>
<li>{icon("check")}Free, no obligation price over the phone</li>
<li>{icon("check")}Serving Homestead and all of South Dade</li>
</ul></div>'''

def hero(h1, lead, points, image, alt, crumbs=None, eyebrow="Homestead, FL Junk Removal", selected=None):
    pts = "".join(f'<li><span class="tick">{icon("check")}</span>{p}</li>' for p in points)
    cr = ""
    if crumbs:
        lis = "".join((f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>') for n, u in crumbs)
        cr = f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'
    return f'''<section class="hero">
<div class="hero-bg">{img(image, alt, sizes="100vw", eager=True)}</div>
<div class="wrap">
<div class="hero-anim">{cr}<span class="eyebrow">{icon("pin")} {eyebrow}</span><h1>{h1}</h1><p class="hero-lead">{lead}</p>
<ul class="hero-points">{pts}</ul>
<div class="hero-ctas">{call_btn("btn btn-primary pulse")}<a class="btn btn-outline" href="#pricing">See Prices</a></div></div>
{call_card(selected=selected)}
</div></section>'''

def trust():
    items = [("clock", "Same Day Pickup", "Book by noon, gone today"),
             ("dollar", "Upfront Pricing", "Priced by volume, no surprises"),
             ("recycle", "Donate and Recycle", "Less goes to the landfill"),
             ("broom", "We Sweep Up", "Space left broom clean")]
    out = "".join(f'<div class="trust-item"><span class="ic">{icon(i)}</span><div><b>{t}</b><span>{s}</span></div></div>' for i, t, s in items)
    return f'<section class="trust" aria-label="Why homeowners choose us"><div class="wrap stagger">{out}</div></section>'

# ---------- Page shell ----------
def business_schema():
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": f"{SITE}/#business",
        "name": BRAND,
        "url": SITE + "/",
        "telephone": "+1-877-745-9845",
        "logo": f"{SITE}/assets/img/junk-removal-homestead-logo.png",
        "image": f"{SITE}/assets/img/og-junk-removal-homestead.jpg",
        "priceRange": "$$",
        "description": "Local junk removal, dumpster rental and cleanout company serving Homestead, Florida and South Miami-Dade County.",
        "address": {"@type": "PostalAddress", "addressLocality": "Homestead", "addressRegion": "FL", "postalCode": "33030", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": 25.4687, "longitude": -80.4776},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "07:00", "closes": "19:00"}],
        "areaServed": [{"@type": "City", "name": f"{n}, FL"} for n, _ in AREAS] +
                      [{"@type": "AdministrativeArea", "name": "Miami-Dade County, FL"}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Junk Removal Services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": HOME_SVC[2], "url": SITE + "/"}}] +
                [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[2], "url": f"{SITE}/service/{s[0]}"}} for s in SERVICES]},
    }

def page(path, title, desc, body, faqs, crumbs, service=None, og_image="og-junk-removal-homestead.jpg"):
    url = SITE + path
    graph = [
        business_schema(),
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/", "name": BRAND, "publisher": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US"},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc,
         "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#business"}, "inLanguage": "en-US",
         "breadcrumb": {"@id": url + "#breadcrumb"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (u if u else path)} for i, (n, u) in enumerate(crumbs)]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]},
    ]
    if service:
        graph.append({"@type": "Service", "@id": url + "#service", "name": service["name"], "serviceType": service["type"],
                      "description": desc, "url": url, "provider": {"@id": f"{SITE}/#business"},
                      "areaServed": service.get("area") or [{"@type": "City", "name": f"{n}, FL"} for n, _ in AREAS],
                      "offers": {"@type": "Offer", "priceCurrency": "USD", "availability": "https://schema.org/InStock",
                                 "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "USD", "minPrice": service["min"]}}})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))

    CUR = ' aria-current="page"'
    cur = lambda u: CUR if path == u else ""
    nav_svcs = (f'<li><a href="/services"{cur("/services")}><b>All Services</b></a></li>' +
                "".join(f'<li><a href="/service/{s[0]}"{cur("/service/" + s[0])}>{s[1]}</a></li>' for s in SERVICES))
    nav_areas = (f'<li><a href="/service-areas"{cur("/service-areas")}><b>All Service Areas</b></a></li>' +
                 f'<li><a href="/">Homestead</a></li>' +
                 "".join(f'<li><a href="{loc_url(n)}"{cur(loc_url(n))}>{n}</a></li>' for n in LOC_PAGES))
    foot_svcs = ('<li><a href="/">Junk Removal Homestead</a></li>' +
                 "".join(f'<li><a href="/service/{s[0]}">{s[1]} Homestead</a></li>' for s in SERVICES))
    foot_areas = ('<li><a href="/">Homestead, FL</a></li>' +
                  "".join(f'<li><a href="{loc_url(n)}">{n}, FL</a></li>' for n in LOC_PAGES) +
                  '<li><a href="/service-areas">All Service Areas</a></li>')
    home_cur = ' aria-current="page"' if path == "/" else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="Homestead, Florida">
<meta name="geo.position" content="25.4687;-80.4776">
<meta name="ICBM" content="25.4687, -80.4776">
<meta name="theme-color" content="#1e6b34">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/{og_image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>{icon("pin", "sr-only")}Serving Homestead, Florida City and all of South Miami-Dade</span><span class="hide-sm">{HOURS} &middot; <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<header class="site-header">
<div class="wrap nav">
<a class="brand" href="/" aria-label="{BRAND} home"><img src="/assets/img/junk-removal-homestead-logo-160.webp" width="160" height="160" alt="{BRAND} logo"><span>Junk Removal<br>Homestead<small>PROFESSIONAL &amp; RELIABLE</small></span></a>
<nav aria-label="Main">
<ul class="menu">
<li><a href="/"{home_cur}>Home</a></li>
<li class="has-dd"><button class="dd-toggle" aria-expanded="false">Services</button><ul class="dropdown">{nav_svcs}</ul></li>
<li class="has-dd"><button class="dd-toggle" aria-expanded="false">Service Areas</button><ul class="dropdown">{nav_areas}</ul></li>
<li><a href="/#pricing">Pricing</a></li>
<li><a href="#faq">FAQs</a></li>
<li>{call_btn("btn btn-primary")}</li>
</ul>
</nav>
<button class="burger" aria-label="Open menu" aria-expanded="false"><span></span></button>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="wrap fgrid">
<div><div class="flogo"><img src="/assets/img/junk-removal-homestead-logo-160.webp" width="160" height="160" alt="" loading="lazy"><span>Junk Removal<br>Homestead</span></div>
<p>Locally focused junk removal, dumpster rental and property cleanouts for Homestead, Florida City, Redland, Leisure City and the rest of South Miami-Dade County.</p>
<a class="fphone" href="tel:{TEL}">{PHONE}</a><p>{HOURS}</p></div>
<div><h2>Services</h2><ul>{foot_svcs}</ul></div>
<div><h2>Service Areas</h2><ul>{foot_areas}</ul></div>
<div><h2>Quick Links</h2><ul><li><a href="/">Home</a></li><li><a href="/#pricing">Junk Removal Prices</a></li><li><a href="/services">All Services</a></li><li><a href="/service-areas">Areas We Serve</a></li><li><a href="/#faq">Homestead Junk Removal FAQs</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>
</div>
<div class="wrap fbottom"><span>&copy; <span data-year>2026</span> {BRAND}. All rights reserved.</span><span>Junk removal and hauling in Homestead, FL 33030</span></div>
</footer>
<div class="callbar">{call_btn("btn btn-primary", f"Call Now {PHONE}")}</div>
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''

def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)
