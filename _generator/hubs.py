from lib import *
import svc_a, svc_b, svc_c, locations, zips, seo

# ---------- /services ----------
SVC_FAQS = [
 ("What junk removal services do you offer in Homestead?",
  "We offer full-service junk removal across Homestead and South Miami-Dade. Our services include furniture and appliance removal, dumpster rental, and construction debris and yard waste removal. We also handle garage and estate cleanouts, commercial junk removal and hurricane debris removal."),
 ("Can I combine more than one service in a single visit?",
  "Yes. Most jobs mix services, such as a garage cleanout with appliance removal, or yard waste with old patio furniture. "
  "You pay one volume-based price for everything that goes on the truck."),
 ("How is pricing calculated for your services?",
  "Pickup services are priced by how much space your items take in our 15-cubic-yard truck, with labor, travel and disposal included. "
  "Dumpster rentals have a flat rate based on container size and rental period. Very heavy materials such as concrete may be priced by weight."),
 ("Should I rent a dumpster or book junk removal?",
  "If you have a multi-day project and people to load, a dumpster usually costs less. If you want the work done in one visit with no lifting, full-service junk removal is often cheaper. Labor is included, and nothing sits in your driveway."),
 ("Do you serve businesses as well as homes?",
  "Yes. We work with property managers, realtors, contractors, offices, retailers and hotels, with early-morning, after-hours and recurring pickups available."),
 ("What items can you not take?",
  "We cannot haul hazardous materials such as paint, solvents, fuel, pool chemicals, propane tanks, asbestos or medical waste. "
  "Miami-Dade County accepts many of these at its Home Chemical Collection events."),
]

def services_page():
    path = "/services"
    crumbs = [("Home", "/"), ("Services", None)]
    all_pages = svc_a.PAGES + svc_b.PAGES + svc_c.PAGES
    best = {"furniture-removal": "Couches, mattresses and bedroom sets", "appliance-removal": "Fridges, washers, dryers and water heaters",
            "dumpster-rental": "Roofing, remodels and multi-day cleanouts", "construction-debris-removal": "Drywall, lumber, tile and job site waste",
            "yard-waste-removal": "Palm fronds, limbs and brush piles", "garage-cleanout": "Packed garages, sheds and carports",
            "estate-cleanout": "Whole-house cleanouts for families and executors", "commercial-junk-removal": "Offices, retail, hotels and rentals",
            "hurricane-debris-removal": "Storm-damaged trees, fencing and contents"}
    rows = [["Junk Removal", "Household junk and clutter pickup", "$95"]]
    for s in all_pages:
        rows.append([s["name"], best[s["slug"]], f'${s["min"]}'])
    b = [
        hero("Junk Removal <em>Services</em> in Homestead, FL",
             "Our junk removal services cover every kind of cleanup, from a single couch to a full estate, job site or storm mess. One local crew lifts, loads, hauls and sweeps across South Miami-Dade with upfront pricing.",
             ["10 services, one phone call", "Same-day pickup available", "Upfront volume pricing", "Donation and recycling first"],
             "junk-hauling-truck-homestead", "Junk hauling truck for Homestead junk removal services",
             crumbs=crumbs, eyebrow="All Services"),
        trust(),
        split("Every Junk Removal Service Homestead Needs, Under One Roof",
              "<p>Most cleanups are not just one thing. A garage cleanout turns up an old fridge. A remodel leaves a pile of drywall and a broken vanity. A storm drops limbs on top of the patio furniture. Instead of calling three companies, you call one crew that handles it all in a single visit.</p>"
              "<p>We serve homes, rentals, farms and businesses in Homestead, Florida City, Leisure City, Princeton, Cutler Bay, the Redland and the rest of South Dade. Every job is done by two trained movers with a 15-cubic-yard truck, and every price is confirmed on site before work starts.</p>"
              "<p>Not sure which service fits? Call us, describe the job, and we will point you to the fastest and most affordable option.</p>",
              "dumpster-delivery-driveway-homestead", "Dumpster delivered to a Homestead driveway for a cleanout",
              badge="<b>10 services</b>one local team", eyebrow="Our Services"),
        service_cards("Choose Your Junk Removal Service",
                      "Tap any service to see what is included, typical prices and answers to common questions.",
                      alt_bg=True, sid="all-services", include_home=True),
        pricing("Starting Prices by Service",
                "Here is where each service starts. Most jobs are quoted by truck volume, and your exact price is confirmed on site before any lifting begins.",
                ["Service", "Best For", "Starting At"], rows,
                "Starting prices are typical minimums for Homestead and nearby ZIP codes. Heavy materials may be priced by weight. "
                f"Call for an exact quote. Prices updated {seo.UPDATED}."),
        seo.item_guide(),
        seo.estimator(),
        steps("How Booking Works for Any Service",
              "Whatever the job, the process follows the same four simple steps.",
              [("Call for a Price", f"Call {PHONE}, describe the job and get a fast price range.", "phone"),
               ("Pick a Time", "Choose a same-day slot or a scheduled two-hour arrival window.", "calendar"),
               ("We Do the Work", "The crew confirms the price, then lifts, loads or delivers.", "truck"),
               ("Sweep and Sort", "We sweep up and donate or recycle everything we can.", "recycle")], alt_bg=True),
        areas("Services Available Across South Miami-Dade",
              "Every service is available throughout our service area, with no extra travel fee inside it."),
        faq("Junk Removal Services FAQs", "Common questions about choosing and combining our services.", SVC_FAQS),
        cta("Not Sure Which Service You Need?", "Call and describe the job. We will recommend the fastest, most affordable option and give you an upfront price."),
    ]
    return path, page(path, "Junk Removal Services in Homestead, FL | All Services",
                      "All junk removal services in Homestead, FL: furniture and appliance removal, dumpster rental, cleanouts, debris and yard waste removal. Call 877-745-9845.",
                      "\n".join(b), SVC_FAQS, crumbs)

# ---------- /service-areas ----------
AREA_FAQS = [
 ("What areas do you serve for junk removal?",
  "We serve Homestead and all of South Miami-Dade. That includes Florida City, Leisure City, Princeton, Naranja, Modello, the Redland, Goulds, Cutler Bay, South Miami Heights, Homestead Base and Keys Gate."),
 ("Do you charge a travel fee outside Homestead?",
  "No. Our core service radius is about 20 miles from downtown Homestead, and travel is included in your price anywhere inside it. "
  "For jobs farther out, such as the upper Keys, call, and we will let you know if a small travel charge applies."),
 ("Is same-day junk removal available in every service area?",
  "Same-day service is available across our service area when you call before noon, subject to crew availability. Homestead, Florida City and "
  "Leisure City are closest to our base and usually have the earliest openings."),
 ("Do bulk trash rules differ between Homestead and nearby areas?",
  "Yes. The City of Homestead and Florida City run their own trash collection. Unincorporated areas like Leisure City, Princeton and the Redland follow Miami-Dade County rules instead. Those rules allow two bulky pickups per year and no single items over 150 pounds. We are not bound by those limits."),
 ("Do you serve businesses in all of these areas?",
  "Yes. Commercial junk removal, construction debris removal and dumpster rental are available to businesses, contractors and property managers "
  "anywhere in our service area."),
 ("Which ZIP codes do you serve for junk removal?",
  "We serve 33030, 33031, 33032, 33033, 33034, 33035 and 33039 in and around Homestead. We also cover 33170 in Goulds, "
  "33177 in South Miami Heights, 33187 in the northern Redland and 33157, 33189 and 33190 in Cutler Bay."),
 ("My neighborhood is not listed. Can you still help?",
  "Probably. If you are in South Miami-Dade between Cutler Bay and the gateway to the Keys, we almost certainly serve you. Call, and we will confirm."),
]

def area_cards():
    cards = [f'''<article class="card">
<figure>{img("junk-removal-truck-homestead-fl", "Junk removal in Homestead, FL", sizes="(max-width: 640px) 100vw, (max-width: 1080px) 50vw, 33vw")}</figure>
<div class="body"><h3><a href="/">Junk Removal in Homestead</a></h3><p>Homestead is our home base. We offer same-day junk pickup across ZIP codes 33030, 33033 and 33035, from downtown Krome Avenue to Keys Gate.</p></div></article>''']
    for l in locations.PAGES:
        blurb = strip(l["lead"])
        cards.append(f'''<article class="card">
<figure>{img(l["hero_img"], f"Junk removal in {l['name']}, FL", sizes="(max-width: 640px) 100vw, (max-width: 1080px) 50vw, 33vw")}</figure>
<div class="body"><h3><a href="{loc_url(l["name"])}">Junk Removal in {locations.place(l["name"])}</a></h3><p>{blurb}</p><p><b>ZIP {l["zips"]}</b></p></div></article>''')
    return (f'<section class="section alt" id="locations"><div class="wrap">'
            f'{sec_head("Junk Removal by Location", "Choose your community for local details, pricing and answers to common questions.", "Locations")}'
            f'<div class="cards stagger">{"".join(cards)}</div></div></section>')

def areas_page():
    path = "/service-areas"
    crumbs = [("Home", "/"), ("Service Areas", None)]
    b = [
        hero("Junk Removal <em>Service Areas</em> in South Miami-Dade",
             "Based in Homestead and serving every community from Cutler Bay to the gateway to the Florida Keys. Same crews, same upfront pricing "
             "and no travel fee anywhere inside our service area.",
             ["Homestead and all of South Dade", "Same-day pickup in most areas", "No travel fee in our core area", "Homes, farms and businesses"],
             "dumpster-trailer-loaded-homestead", "Junk removal trailer serving South Miami-Dade communities",
             crumbs=crumbs, eyebrow="Service Areas"),
        trust(),
        split("Local Junk Removal From Cutler Bay to Florida City",
              "<p>Our trucks start every day in Homestead. That puts us minutes from Florida City, Leisure City, Naranja and Princeton, and a short drive from the Redland, Goulds and Cutler Bay. Being close means shorter arrival windows, more same-day openings and lower prices than companies "
              "dispatching from farther north in Miami.</p>"
              "<p>Each community has its own mix of homes, rentals, farms and businesses, and its own trash rules. The City of Homestead and Florida City run "
              "their own collection, while unincorporated areas follow Miami-Dade County bulky waste limits. We know the differences and the disposal sites, "
              "so every load goes to the right place.</p>",
              "junk-hauling-truck-homestead", "Junk hauling truck heading out from Homestead",
              badge="<b>20 miles</b>core service radius", eyebrow="Where We Work"),
        area_cards(),
        zips.hub_section(),
        prose("<h2>Every Service, in Every Area</h2>"
              "<p>Every service we offer is available across South Miami-Dade. That includes furniture and appliance removal, "
              "dumpster rental, debris and yard waste removal, garage and estate cleanouts, commercial junk removal and storm cleanup. "
              "Every area gets the same trained crews, the same trucks and the same upfront pricing.</p>"
              "<h2>Pricing Is the Same Across Our Service Area</h2>"
              "<p>You pay the same volume-based rates whether you are in Homestead, Florida City or Cutler Bay. Labor, loading, travel and disposal "
              "are included, and your final price is confirmed on site before any work starts.</p>"),
        pricing("Junk Removal Prices Across South Dade",
                "Typical prices by truck volume, the same in every community we serve.",
                locations.PRICE_HEADERS, locations.PRICE_ROWS,
                "Typical price ranges. Very heavy loads such as concrete, dirt or roofing may be priced by weight. Your final price is confirmed on site.",
                alt_bg=True),
        areas("All Communities and ZIP Codes We Serve",
              "Linked communities have their own local page. Every area listed gets the same crews, prices and same-day scheduling.",
              map_q="Homestead,+FL", show_all=False),
        faq("Service Area FAQs", "Questions about where we work, travel fees and local rules.", AREA_FAQS),
        cta("Junk Removal Wherever You Are in South Dade", "Call for a free, upfront quote. Same-day pickup is available across our service area."),
    ]
    return path, page(path, "Junk Removal Service Areas | Homestead and South Dade",
                      "Junk removal service areas across South Miami-Dade: Homestead, Florida City, Cutler Bay, Leisure City, Princeton, Redland and more. Call 877-745-9845.",
                      "\n".join(b), AREA_FAQS, crumbs)
