"""ZIP code data and ZIP-targeted sections. Links stay in headings only, so tables and paragraphs carry no links."""
from lib import *

# zip, community, local detail (one or two plain sentences)
ZIPS = [
 ("33030", "Downtown Homestead",
  "Historic downtown Homestead along Krome Avenue, with older block homes and nearby farm properties. Furniture pickups, garage cleanouts and rental turnovers are the most common jobs."),
 ("33031", "The Redland",
  "Groves, plant nurseries and homes on large lots west of Homestead, near the Fruit and Spice Park. Farm cleanups, shed removal and brush piles are typical here."),
 ("33032", "Princeton, Naranja and Modello",
  "Newer subdivisions along SW 248th Street and older homes near US 1, including the Moody Drive area. We haul a lot of moving boxes, remodel debris and garage clutter here."),
 ("33033", "Leisure City and Northeast Homestead",
  "Established block homes, duplexes and rentals, plus the area around Homestead Hospital. Carport cleanouts, appliance pickups and tenant move-outs are common."),
 ("33034", "Florida City",
  "Homes, hotels and farms at the gateway to the Florida Keys and Everglades National Park. Motel turnovers, commercial pickups and yard waste keep our crews busy here."),
 ("33035", "Keys Gate and Southeast Homestead",
  "Keys Gate and the newer communities around Homestead-Miami Speedway, many with HOA rules. We load from garages and patios so nothing sits at the curb."),
 ("33039", "Homestead Air Reserve Base",
  "Base facilities and nearby housing. Base access rules apply. Call ahead, and we will confirm what your pickup requires."),
 ("33170", "Goulds and the Eastern Redland",
  "Homes, small farms and nurseries north of Princeton. Yard waste, appliance pickups and shed removal are frequent requests."),
 ("33187", "Northern Redland",
  "Rural homes, horse properties and nurseries on larger lots. Barn cleanouts, fence removal and brush piles are typical jobs."),
 ("33177", "South Miami Heights",
  "Established neighborhoods north of Cutler Bay, near Zoo Miami. Furniture removal, garage cleanouts and estate cleanouts are the most common calls."),
 ("33157", "Northern Cutler Bay",
  "The northern part of Cutler Bay, a ZIP code shared with Palmetto Bay. Remodel debris, estate cleanouts and furniture pickups are frequent here."),
 ("33189", "Central Cutler Bay",
  "Central Cutler Bay, including the Southland Mall area along US 1. We handle everything from single couches to whole-house cleanouts."),
 ("33190", "Southern Cutler Bay",
  "Southern Cutler Bay toward Black Point Marina and Biscayne Bay. After heavy storms, we often remove water-damaged carpet, drywall and furniture here."),
]
ZIP = {z: (a, d) for z, a, d in ZIPS}
HOMESTEAD_ZIPS = ["33030", "33031", "33032", "33033", "33034", "33035", "33039"]

def zip_list(zs):
    zs = list(zs)
    return zs[0] if len(zs) == 1 else ", ".join(zs[:-1]) + " and " + zs[-1]

def zip_schema(zs=None):
    """Service areas as postal-code places for structured data."""
    out = []
    for z in (zs or [z for z, _, _ in ZIPS]):
        a, _ = ZIP[z]
        out.append({"@type": "Place", "name": f"{a}, FL {z}",
                    "address": {"@type": "PostalAddress", "postalCode": z, "addressRegion": "FL", "addressCountry": "US"}})
    return out

def _table(headers, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-wrap reveal"><table class="stack"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

# ---------- Service areas hub: the full ZIP guide ----------
def hub_section():
    rows = [[f"<b>{z}</b>", a, d] for z, a, d in ZIPS]
    intro = (f"We serve every ZIP code in and around Homestead, from {ZIPS[0][0]} downtown to {ZIPS[-1][0]} in Cutler Bay. "
             "Use the table below to see what each area looks like and the jobs we handle most often there. "
             "Every ZIP code on this list gets the same crews, the same volume-based prices and no travel fee.")
    return (f'<section class="section" id="zip-codes"><div class="wrap">'
            f'{sec_head("Junk Removal by ZIP Code in South Miami-Dade", intro, "ZIP Codes")}'
            f'{_table(["ZIP Code", "Community", "What to Know"], rows)}</div></section>')

# ---------- Homepage: Homestead ZIP codes ----------
def home_section():
    rows = []
    for z in HOMESTEAD_ZIPS:
        a, _ = ZIP[z]
        pickup = "Call ahead for base access" if z == "33039" else "Same day when you call before noon"
        rows.append([f"<b>{z}</b>", a, pickup, "None"])
    intro = ("Searching for junk removal near you in Homestead, FL 33030, 33033 or 33035? We cover every Homestead ZIP code, "
             "including the Redland (33031), Princeton and Naranja (33032), Florida City (33034) and Homestead Air Reserve Base (33039).")
    body = ("<p>Prices are the same in every ZIP code, and travel is always included. "
            "Tell us your ZIP code when you call, and we will give you the earliest arrival window for your street.</p>")
    return (f'<section class="section" id="zip-codes"><div class="wrap">'
            f'{sec_head("Junk Removal in Every Homestead ZIP Code", intro, "ZIP Codes")}'
            f'{_table(["ZIP Code", "Area", "Pickup Timing", "Travel Fee"], rows)}'
            f'<div class="content reveal" style="margin-top:22px">{body}</div></div></section>')

HOME_FAQ = ("Do you offer junk removal in ZIP codes 33030, 33033 and 33035?",
            "Yes. We provide same-day junk removal in all Homestead ZIP codes, including 33030, 33031, 33032, 33033, 33034, 33035 "
            "and 33039. Prices are the same in every ZIP code, and there is no travel fee.")

# ---------- Service pages ----------
# service slug -> (what we do, how availability reads in the table, FAQ angle)
SVC_ZIP = {
 "furniture-removal": ("couch, mattress and furniture removal", "Same-day pickup",
   "Our crews remove couches, sectionals, mattresses and bedroom sets from homes and apartments in each of these ZIP codes."),
 "appliance-removal": ("appliance removal and recycling", "Same-day pickup",
   "We carry out refrigerators, washers, dryers and water heaters in each of these ZIP codes and deliver them to licensed recyclers."),
 "dumpster-rental": ("roll-off dumpster delivery", "Next-day delivery",
   "We deliver 10-, 15- and 20-yard dumpsters to driveways and job sites in each of these ZIP codes, usually the next day."),
 "construction-debris-removal": ("construction and remodel debris removal", "Same-day pickup",
   "We haul drywall, lumber, tile and job site waste for homeowners and contractors in each of these ZIP codes."),
 "yard-waste-removal": ("yard waste and brush removal", "Same-day pickup",
   "We clear palm fronds, branches and brush piles from yards, groves and rental lots in each of these ZIP codes."),
 "garage-cleanout": ("garage cleanouts", "Same-day or next-day",
   "We sort, haul and sweep out garages, sheds and carports in each of these ZIP codes."),
 "estate-cleanout": ("estate and whole-house cleanouts", "Scheduled within days",
   "We handle estate cleanouts for families, executors and realtors in each of these ZIP codes, including homes with sheds and outbuildings."),
 "commercial-junk-removal": ("commercial junk removal", "Within 24 to 48 hours",
   "We serve offices, stores, restaurants and rental properties in each of these ZIP codes, with after-hours scheduling available."),
 "hurricane-debris-removal": ("hurricane and storm debris removal", "Priority after storms",
   "After storms, we send crews to each of these ZIP codes as soon as roads are safe, starting with water-damaged homes."),
}
SVC_ZIPS = ["33030", "33031", "33032", "33033", "33034", "33035", "33170", "33177", "33189", "33190"]

def service_section(slug, name):
    what, avail, _ = SVC_ZIP[slug]
    rows = [[f"<b>{z}</b>", ZIP[z][0], avail] for z in SVC_ZIPS]
    intro = (f"Looking for {what} near me in Homestead? We provide {what} in every ZIP code below, from downtown Homestead (33030) to Cutler Bay (33190). "
             "Prices are the same in each one, and travel is always included.")
    return (f'<section class="section alt" id="zip-codes"><div class="wrap">'
            f'{sec_head(f"{name} by ZIP Code", intro, "ZIP Codes")}'
            f'{_table(["ZIP Code", "Area", "Availability"], rows)}</div></section>')

def service_faq(slug, name):
    _, _, angle = SVC_ZIP[slug]
    q = f"Do you offer {name.lower()} in Homestead ZIP codes 33030, 33032 and 33033?"
    a = (f"Yes. {angle} That covers every Homestead ZIP code from 33030 to 33035, plus nearby Goulds, South Miami Heights "
         "and Cutler Bay. Pricing is the same in every ZIP code.")
    return (q, a)

# ---------- Location pages ----------
# Location pages describe each ZIP only in terms of that community
LOC_ZIP = {
 "33031": ("Western Redland", "Groves, plant nurseries and homes on large lots near the Fruit and Spice Park. Farm cleanups, shed removal and brush piles are typical here."),
 "33032": ("Princeton", "Newer subdivisions along SW 248th Street and older homes near US 1. We haul a lot of moving boxes, remodel debris and garage clutter here."),
 "33033": ("Leisure City", "Established block homes, duplexes and rentals across Leisure City. Carport cleanouts, appliance pickups and tenant move-outs are common."),
 "33157": ("Northern Cutler Bay", "The northern neighborhoods of Cutler Bay. Remodel debris, estate cleanouts and furniture pickups are frequent here."),
 "33170": ("Eastern Redland", "Homes, small farms and nurseries on the eastern edge of the Redland. Yard waste, appliance pickups and shed removal are frequent requests."),
}

def location_section(l, place):
    zs = [z.strip() for z in l["zips"].split(",")]
    rows = [[f"<b>{z}</b>", *LOC_ZIP.get(z, ZIP[z])] for z in zs]
    cap = place[0].upper() + place[1:]
    if len(zs) == 1:
        h2 = f"Junk Removal in {place}, FL {zs[0]}"
        intro = (f"{cap} is covered by ZIP code {zs[0]}. We offer same-day junk removal, furniture and appliance pickup, "
                 f"cleanouts and dumpster rental everywhere in {zs[0]}, with no travel fee.")
    else:
        h2 = f"Junk Removal in {place} ZIP Codes {zip_list(zs)}"
        intro = (f"{cap} spans ZIP codes {zip_list(zs)}. We offer the same fast junk removal, cleanouts and dumpster rental "
                 "in each one, with no travel fee.")
    return (f'<section class="section" id="zip-codes"><div class="wrap">'
            f'{sec_head(h2, intro, "ZIP Codes")}'
            f'{_table(["ZIP Code", "Area", "What to Know"], rows)}'
            f'{map_facade(l["map_q"], place + ", Florida", "margin-top:30px")}</div></section>')
