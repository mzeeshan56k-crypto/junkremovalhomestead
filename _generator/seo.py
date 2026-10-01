"""Answer-first blocks, the price estimator, the item price guide and richer structured data.

These pieces target AI Overviews and local commercial searches: each page opens with a short,
quotable answer and a fact panel, and the structured data spells out prices, areas and entities.
Links stay in headings only.
"""
import re
from lib import *

UPDATED = "October 2026"
UPDATED_ISO = "2026-10-01"

# ---------- Price helpers ----------
def price_range(rows, floor):
    """Lowest and highest dollar amounts in a price table's last column."""
    nums = [int(n.replace(",", "")) for r in rows for n in re.findall(r"\$([\d,]+)", r[-1])]
    nums = [n for n in nums if n >= floor]
    return floor, max(nums) if nums else floor

def money(n):
    return f"${n:,}"

# ---------- Quick answer + key facts ----------
def quick_answer(question, answer, facts, alt_bg=False):
    """A short, self-contained answer that AI Overviews and featured snippets can quote, beside a fact panel."""
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    return (f'<section class="section answer{" alt" if alt_bg else ""}" id="quick-answer"><div class="wrap answer-grid">'
            f'<div class="answer-text reveal"><span class="eyebrow dark">Quick Answer</span><h2>{question}</h2><p>{answer}</p>'
            f'<p class="answer-cta">{call_btn("btn btn-primary", f"Call {PHONE} for an Exact Price")}</p></div>'
            f'<dl class="facts reveal">{dl}</dl></div></section>')

def facts(price, timing, area):
    return [("Typical price", price), ("Availability", timing), ("Service area", area),
            ("Hours", HOURS), ("Phone", f'<a href="tel:{TEL}">{PHONE}</a>'), ("Prices updated", UPDATED)]

HOME_QA = ("How much does junk removal cost in Homestead, FL?",
           "Junk removal in Homestead, FL typically costs $95 to $650. A single item starts at $95, a half truckload runs "
           "$300 to $425 and a full 15-cubic-yard truck costs $560 to $650. Labor, loading and disposal are included, and "
           "same-day pickup is available when you call before noon.")

SVC_QA = {
 "furniture-removal": "Furniture removal in Homestead, FL typically costs $95 to $650. A recliner starts at about $95, a standard sofa runs $120 to $160 and a full bedroom set costs $220 to $300. The price includes carrying items from any room, hauling and donation, and same-day pickup is often available.",
 "appliance-removal": "Appliance removal in Homestead, FL typically costs $95 to $175 per unit. A washer or dryer runs $95 to $125, a refrigerator costs $110 to $160 and an AC condenser costs $120 to $175. Every price includes carry-out, hauling and recycling, including refrigerant recovery for fridges and freezers.",
 "dumpster-rental": "Dumpster rental in Homestead, FL typically costs $295 to $525. A 10-yard dumpster runs $295 to $375, a 15-yard dumpster costs $365 to $450 and a 20-yard dumpster costs $425 to $525. Prices include delivery, pickup, a 7-day rental and a weight allowance, and next-day delivery is standard.",
 "construction-debris-removal": "Construction debris removal in Homestead, FL typically costs $150 to $700. A bathroom remodel runs $200 to $300, a kitchen remodel costs $280 to $425 and a full 15-cubic-yard truck of mixed debris costs $560 to $700. Concrete, tile and dirt are priced by weight.",
 "yard-waste-removal": "Yard waste removal in Homestead, FL typically costs $95 to $650. A small pile of 10 to 15 bags starts around $95, a palm frond pile runs $175 to $260 and an overgrown lot cleanup costs $520 to $650. Stumps, sod and soil are priced by weight.",
 "garage-cleanout": "A garage cleanout in Homestead, FL typically costs $150 to $650. A partial cleanout starts around $150, a full one-car garage runs $400 to $520 and a full two-car garage costs $520 to $650. Sorting, donation drop-offs and a final sweep are included.",
 "estate-cleanout": "An estate cleanout in Homestead, FL typically costs $450 to $2,600, depending on home size. An apartment runs $450 to $650, a three-bedroom home costs $1,100 to $1,750 and a four-bedroom home with a garage costs $1,750 to $2,600. Sorting and donation are included.",
 "commercial-junk-removal": "Commercial junk removal in Homestead, FL typically costs $250 to $650 per job. A small office cleanout runs $250 to $450, an apartment turnover costs $300 to $560 and a retail fixture removal costs $400 to $650. Larger and recurring jobs are quoted individually.",
 "hurricane-debris-removal": "Hurricane debris removal in Homestead, FL typically costs $150 to $700. A small limb pile runs $150 to $280, water-damaged room contents cost $350 to $520 and a full truck of mixed storm debris costs $560 to $700. Our storm pricing never goes up after a hurricane.",
}
SVC_TIMING = {"dumpster-rental": "Next-day delivery", "estate-cleanout": "Scheduled within days",
              "commercial-junk-removal": "Within 24 to 48 hours", "hurricane-debris-removal": "Priority after storms"}

def service_qa(s, lo, hi):
    q = f"How much does {s['name'].lower()} cost in Homestead, FL?"
    return quick_answer(q, SVC_QA[s["slug"]],
                        facts(f"{money(lo)} to {money(hi)}", SVC_TIMING.get(s["slug"], "Same day when you call before noon"),
                              "Homestead, FL 33030 to 33035 and South Miami-Dade"), alt_bg=False)

def location_qa(place, zip_text):
    cap = place[0].upper() + place[1:]
    q = f"How much does junk removal cost in {place}, FL?"
    a = (f"Junk removal in {place}, FL typically costs $95 to $650. A single item starts at $95, a half truckload runs "
         f"$300 to $425 and a full 15-cubic-yard truck costs $560 to $650. {cap} jobs in {zip_text} include labor, "
         "loading and disposal, with no travel fee and same-day pickup when you call before noon.")
    return quick_answer(q, a, facts("$95 to $650", "Same day when you call before noon", f"{cap}, {zip_text}"))

# ---------- Price estimator (lead tool) ----------
EST_ITEMS = [  # key, label, cubic yards
 ("sofa", "Sofa or loveseat", 2), ("sectional", "Sectional sofa", 3.5), ("recliner", "Recliner or armchair", 1),
 ("mattress", "Mattress and box spring", 2), ("dresser", "Dresser or armoire", 1), ("table", "Dining table and chairs", 2),
 ("fridge", "Refrigerator or freezer", 1.5), ("washer", "Washer or dryer", 1), ("tv", "TV or electronics", 0.5),
 ("treadmill", "Treadmill or gym equipment", 1.5), ("bags", "Bags of trash (per 5 bags)", 0.75), ("boxes", "Boxes (per 10 boxes)", 1),
]

def estimator(place="Homestead"):
    rows = "".join(
        f'<div class="est-row"><label for="est-{k}">{label}</label>'
        f'<div class="stepper"><button type="button" class="est-step" data-step="-1" aria-label="Remove one {label.lower()}">&minus;</button>'
        f'<input id="est-{k}" type="number" min="0" max="20" value="0" inputmode="numeric" data-yards="{yd}">'
        f'<button type="button" class="est-step" data-step="1" aria-label="Add one {label.lower()}">+</button></div></div>'
        for k, label, yd in EST_ITEMS)
    intro = (f"Add the items you want removed to see a typical price range for junk removal in {place}. "
             "Your exact price is confirmed on site before any work begins.")
    return (f'<section class="section alt" id="estimate"><div class="wrap">{sec_head("Estimate Your Junk Removal Price", intro, "Free Estimate")}'
            f'<div class="estimator reveal" data-estimator>'
            f'<div class="est-items">{rows}</div>'
            f'<div class="est-result" aria-live="polite"><span class="est-label">Estimated price</span>'
            f'<b class="est-price" data-est-price>Add items to start</b>'
            f'<span class="est-load" data-est-load>Prices include labor, loading and disposal.</span>'
            f'{call_btn("btn btn-primary pulse call-wide", "Call to Lock In Your Price")}'
            f'<small>Estimates use typical {UPDATED} prices. Heavy items such as concrete, pianos and hot tubs are quoted separately.</small>'
            f'</div></div></div></section>')

# ---------- Item price guide (long-tail commercial keywords) ----------
ITEM_PRICES = [
 ("Couch or sofa removal", "$120 to $160", "Sleeper sofas cost more because of weight"),
 ("Sectional sofa removal", "$175 to $250", "Priced by the number of pieces"),
 ("Mattress and box spring disposal", "$110 to $150", "Wrapped before carrying out"),
 ("Recliner or armchair removal", "$95 to $120", "Minimum charge usually applies"),
 ("Refrigerator or freezer removal", "$110 to $160", "Refrigerant recovered by a licensed recycler"),
 ("Washer or dryer removal", "$95 to $125", "A pair on the same visit costs $160 to $220"),
 ("Water heater removal", "$110 to $150", "Must be drained and disconnected first"),
 ("Hot tub removal", "$350 to $550", "Includes cutting and hauling"),
 ("Piano removal", "Quoted per job", "Depends on weight, stairs and access"),
 ("Shed demolition and removal", "$300 to $650", "Size and material drive the price"),
 ("TV and electronics disposal", "$95 and up", "Delivered to electronics recyclers"),
 ("Treadmill and gym equipment removal", "$95 to $150", "Metal is recycled"),
 ("Carpet and padding removal", "$95 to $280", "Priced by volume"),
 ("Construction debris pickup", "$150 to $700", "Concrete and tile priced by weight"),
 ("Yard waste and brush hauling", "$95 to $650", "Palm fronds, limbs and brush"),
 ("Tire disposal", "Small fee per tire", "Up to four tires on a standard pickup"),
]

def item_guide(alt_bg=False):
    tr = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in ITEM_PRICES)
    intro = (f"Typical prices for single items and common jobs in Homestead, FL, updated {UPDATED}. "
             "Grouping several items in one visit usually costs less than booking them separately.")
    return (f'<section class="section{" alt" if alt_bg else ""}" id="item-prices"><div class="wrap">'
            f'{sec_head("What We Haul and What It Costs", intro, "Item Prices")}'
            f'<div class="table-wrap reveal"><table class="stack"><thead><tr><th scope="col">Item or Job</th>'
            f'<th scope="col">Typical Price</th><th scope="col">Notes</th></tr></thead><tbody>{tr}</tbody></table></div></div></section>')

# ---------- Lead CTA band (mid-page) ----------
def cta_band(text):
    return (f'<section class="cta-band"><div class="wrap cta-band-in reveal"><p>{text}</p>'
            f'{call_btn("btn btn-light", f"Call {PHONE}")}</div></section>')

# ---------- Structured data ----------
ENTITIES = {
 "Homestead": ("City", "https://en.wikipedia.org/wiki/Homestead,_Florida"),
 "Florida City": ("City", "https://en.wikipedia.org/wiki/Florida_City,_Florida"),
 "Cutler Bay": ("City", "https://en.wikipedia.org/wiki/Cutler_Bay,_Florida"),
 "Leisure City": ("Place", "https://en.wikipedia.org/wiki/Leisure_City,_Florida"),
 "Princeton": ("Place", "https://en.wikipedia.org/wiki/Princeton,_Florida"),
 "Redland": ("Place", "https://en.wikipedia.org/wiki/Redland,_Florida"),
 "Miami-Dade County": ("AdministrativeArea", "https://en.wikipedia.org/wiki/Miami-Dade_County,_Florida"),
}

def entity(name):
    t, url = ENTITIES[name]
    return {"@type": t, "name": f"{name}, FL" if t != "AdministrativeArea" else f"{name}, Florida", "sameAs": url}

def offer_catalog(name, url, rows):
    """Each price-table row becomes an Offer with a price range, which AI answers can quote directly."""
    items = []
    for r in rows:
        nums = [int(n.replace(",", "")) for n in re.findall(r"\$([\d,]+)", r[-1])]
        if not nums:
            continue
        spec = {"@type": "PriceSpecification", "priceCurrency": "USD", "minPrice": min(nums)}
        if len(nums) > 1:
            spec["maxPrice"] = max(nums)
        items.append({"@type": "Offer", "name": strip(r[0]), "description": strip(r[1]) if len(r) > 2 else None,
                      "priceSpecification": spec, "url": url, "areaServed": entity("Homestead")})
    for i in items:
        if i["description"] is None:
            del i["description"]
    return {"@type": "OfferCatalog", "name": f"{name} prices", "itemListElement": items}

def aggregate_offer(lo, hi):
    return {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": lo, "highPrice": hi,
            "availability": "https://schema.org/InStock", "priceValidUntil": "2027-03-31"}

def business_extras():
    """Fields merged into the LocalBusiness node on every page."""
    return {
        "slogan": "Same-day junk removal with upfront pricing",
        "paymentAccepted": "Cash, Credit Card, Debit Card",
        "currenciesAccepted": "USD",
        "areaServed_geo": {"@type": "GeoCircle",
                           "geoMidpoint": {"@type": "GeoCoordinates", "latitude": 25.4687, "longitude": -80.4776},
                           "geoRadius": "32000"},
        "contactPoint": {"@type": "ContactPoint", "telephone": "+1-877-745-9845", "contactType": "customer service",
                         "areaServed": "US-FL", "availableLanguage": "English"},
        "knowsAbout": ["Junk removal", "Furniture removal", "Appliance recycling", "Roll-off dumpster rental",
                       "Construction debris removal", "Yard waste removal", "Estate cleanouts", "Hurricane debris cleanup",
                       "Miami-Dade bulky waste rules"],
    }
