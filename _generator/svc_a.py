from lib import *

STD_STEPS = None

FURN = dict(
 slug="furniture-removal", name="Furniture Removal", schema_name="Furniture Removal in Homestead, FL", min=95,
 title="Furniture Removal in Homestead, FL | Couch and Mattress Pickup",
 desc="Furniture removal in Homestead, FL 33030. Couch, sectional, mattress and dresser pickup from any room, often the same day. From $95. Call 877-745-9845.",
 h1="Furniture Removal and <em>Couch Pickup</em> in Homestead, FL",
 lead="Old sofa, broken bed frame or a whole room of furniture? We carry it out of any room in your Homestead home, load it and haul it away the same day, donating whatever still has life left in it.",
 points=["Couches, beds and dressers", "Removed from any floor", "Donation drop-offs included", "Same-day pickup available"],
 hero_img="junk-hauling-truck-homestead", hero_alt="Furniture removal truck at a Homestead home",
 intro_h2="Furniture Removal That Homestead Families Trust",
 intro_html="<p>Furniture is the single most common item we haul in Homestead. It is bulky, awkward and hard to fit into a car. Many pieces are also too heavy for the county bulky waste program, which refuses single items over 150 pounds. Our two-person crews bring moving blankets, dollies and straps to get sofas, sleeper sofas and armoires out without scratching walls or door frames.</p>"
  "<p>We regularly remove furniture from new builds in Keys Gate, apartments near Homestead Hospital, and vacation rentals turning over between seasons. If you are replacing furniture, we can schedule the pickup the same day the new pieces arrive so you never have two sets in the room.</p>",
 intro_img="furniture-junk-pickup-homestead", intro_alt="Furniture and boxes loaded for removal in Homestead",
 badge="<b>80%</b>of discarded US furniture is landfilled. We donate first.",
 body_html="<h2>Furniture We Remove in Homestead and Florida City</h2>"
  + checks(["Sofas, sectionals and sleeper sofas", "Recliners and lift chairs", "Mattresses and box springs", "Bed frames and headboards",
            "Dressers, armoires and wardrobes", "Dining tables and chairs", "Entertainment centers", "Office desks and cubicles",
            "Patio and outdoor furniture", "Cribs, bunk beds and kids' furniture"])
  + "<h2>Old Couch Removal Near Me: Why Donation Matters</h2>"
  "<p>The EPA reports that Americans discarded about 12.1 million tons of furniture and furnishings in 2018, and roughly 80 percent of it went to landfills. We sort each load so that clean, sturdy pieces go to local charities and resale shops in South Miami-Dade. Items that cannot be reused are broken down so wood and metal can be recycled where possible.</p>"
  "<p>Mattresses are a special case. More than 15 million mattresses are thrown away in the United States each year, and they take up enormous landfill space. When recycling is available, we separate the steel springs, foam and fabric instead of dumping the whole mattress.</p>"
  "<h2>Mattress Disposal and Bed Removal in Homestead</h2>"
  "<p>Bed bug concerns, water damage after summer storms and simple upgrades all lead to mattress removal calls. We wrap damaged mattresses before carrying them through your home and haul them out the same day. Pair it with our junk removal service to clear the rest of the bedroom during the same visit.</p>"
  "<h2>Office Furniture Removal for Homestead Businesses</h2>"
  "<p>Relocating or downsizing? We remove desks, filing cabinets, conference tables and cubicle panels from offices along Krome Avenue, Campbell Drive and the Homestead business parks. Larger jobs are covered under our commercial junk removal service with after-hours scheduling.</p>",
 steps_h2="How Furniture Pickup Works",
 steps_p="From quote to empty room in four easy steps.",
 steps=[("Snap a Photo", "Send pictures of the furniture for a fast, accurate price.", "phone"),
        ("Book a Slot", "Same-day or scheduled pickup with a two-hour window.", "calendar"),
        ("We Carry It Out", "Pads and dollies protect floors, walls and door frames.", "truck"),
        ("Donate or Recycle", "Usable pieces are donated, and the rest is recycled or disposed of properly.", "recycle")],
 price_h2="Furniture Removal Cost in Homestead",
 price_intro="Typical Homestead prices for furniture pickup. Multiple items are priced together by truck volume, so bundling saves money.",
 headers=["Item", "Typical Space", "Typical Price"],
 rows=[["Recliner or armchair", "About 1 cubic yard", "$95 to $120"], ["Standard sofa", "About 2 cubic yards", "$120 to $160"],
       ["Sectional sofa", "3 to 4 cubic yards", "$175 to $250"], ["Mattress and box spring", "About 2 cubic yards", "$110 to $150"],
       ["Full bedroom set", "About 4 cubic yards", "$220 to $300"], ["Whole house of furniture", "12 to 15 cubic yards", "$480 to $650"]],
 note="Sleeper sofas, marble tables and solid wood armoires may cost more because of weight. Final price is confirmed on site.",
 local_h2="Why Homestead Residents Skip the Curb",
 local_html="<p>Leaving a couch on the swale in Homestead is risky. Afternoon storms soak upholstery within minutes, making it heavier and harder to collect, and code enforcement can issue notices for piles placed too early. We pick up from inside the home instead, which keeps your yard clean and your HOA happy.</p>"
  "<p>Our crews know the gated communities off SW 328th Street and Palm Drive, including their gate procedures and truck parking rules. That keeps pickups quick without neighbors noticing.</p>",
 local_img="junk-removal-truck-homestead-fl", local_alt="Junk removal truck at a gated Homestead community",
 related_h2="Related Furniture and Home Services",
 related_p="Clearing more than furniture? These services pair well with a furniture pickup.",
 related=[("appliance-removal", "Remove the old fridge or washer during the same visit."),
          ("estate-cleanout", "Clear an entire home of furniture and belongings respectfully."),
          ("junk-removal", "Haul away boxes, clutter and anything else left behind.")],
 areas_h2="Furniture Pickup Across South Dade",
 areas_p="Furniture removal is available in all of these communities around Homestead.",
 faq_h2="Furniture Removal FAQs for Homestead",
 faq_p="Answers about couch removal, mattress disposal and furniture donation in Homestead.",
 faqs=[
  ("How much does couch removal cost in Homestead?", "A standard three-seat sofa typically costs $120 to $160 to remove, and a large sectional runs $175 to $250. The price covers carrying it out, loading, hauling and donation or disposal."),
  ("Can you take a sofa out of an upstairs apartment?", "Yes. Our two-person crews carry furniture down stairways and through narrow halls every day. If a piece does not fit through a doorway, we can disassemble it with your permission."),
  ("Do you donate furniture you pick up?", "Yes. Clean, structurally sound furniture goes to charities and resale partners in South Miami-Dade. Items with stains, tears, pet damage or bed bugs cannot be donated and are recycled or disposed of properly."),
  ("Will Miami-Dade bulky pickup take my furniture for free?", "Unincorporated Miami-Dade residents get two free bulky pickups per year, up to 25 cubic yards each. However, single items over 150 pounds are refused, and you must drag everything to the curb yourself. We carry items from inside the same day."),
  ("How do you dispose of mattresses?", "When recycling capacity is available, mattresses are separated into steel, foam and fabric for recycling. Otherwise, they go to a licensed disposal facility. Nationally, more than 15 million mattresses are discarded each year."),
  ("Can you remove furniture the day my new furniture is delivered?", "Yes. Tell us your delivery window, and we will schedule the removal right after it. The old pieces leave the same day, so you never have two sets in the room."),
  ("Do you remove heavy items like pianos or pool tables?", "We remove upright pianos, pool tables and gun safes with advance notice. These carry an extra fee based on weight and access, which we quote before scheduling."),
  ("Do I have to be home for furniture pickup?", "If the furniture is in a garage, in a carport or on a patio, you do not need to be home. For pickups inside the home, an adult or property manager should be present to give access."),
  ("How much furniture fits in one truck?", "Our 15-cubic-yard truck holds about the furniture from a three-bedroom home, roughly two sofas, three bedroom sets, a dining set and a few accent pieces."),
  ("Do you remove office furniture in Homestead?", "Yes. We remove desks, chairs, filing cabinets and cubicles from offices and medical suites around Homestead. Evening and weekend times are available, so your business hours are not disrupted."),
 ],
 cta_h2="Get Rid of That Old Couch Today",
 cta_p="Furniture removal from any room in your Homestead home. Call for an upfront quote.",
)

APPL = dict(
 slug="appliance-removal", name="Appliance Removal", schema_name="Appliance Removal and Disposal in Homestead, FL", min=95,
 title="Appliance Removal in Homestead, FL | Fridge and Washer Pickup",
 desc="Appliance removal in Homestead, FL 33030. Refrigerator, washer, dryer, stove, AC and water heater pickup and recycling from $95. Call 877-745-9845.",
 h1="Appliance Removal and <em>Disposal</em> in Homestead, FL",
 lead="Old refrigerator, dead washer or rusted water heater? We disconnect where safe, carry it out, and recycle it responsibly so you do not have to rent a truck or wrestle it to the curb.",
 points=["Fridges, freezers and AC units", "Washers, dryers and stoves", "Recycled at licensed facilities", "Same-day appliance pickup"],
 hero_img="junk-hauling-truck-homestead", hero_alt="Appliance removal truck in Homestead, FL",
 intro_h2="Old Appliance Removal That Homestead Homeowners Can Count On",
 intro_html="<p>Appliances are heavy, bulky and full of materials that should not go to a landfill. A typical refrigerator weighs 200 to 300 pounds, which is more than double the 150-pound single-item limit on Miami-Dade County bulky waste pickups. That is why so many Homestead residents call a professional <strong>appliance removal service</strong>.</p>"
  "<p>Our crew uses appliance dollies and straps to move units safely down steps and across tile floors. We remove appliances from kitchens, laundry rooms, garages and utility closets throughout Homestead, Florida City, Naranja and Leisure City. We handle every step, from the moment we arrive to the drop-off at the recycling yard.</p>",
 intro_img="junk-removal-truck-homestead-fl", intro_alt="Crew ready to remove appliances from a Homestead home",
 badge="<b>200+ lbs</b>typical fridge weight we carry for you",
 body_html="<h2>Appliances We Pick Up and Recycle</h2>"
  + checks(["Refrigerators and freezers", "Washing machines and dryers", "Stoves, ranges and ovens", "Dishwashers and microwaves",
            "Water heaters", "Window and central AC units", "Chest freezers and ice makers", "Pool pumps and pressure washers",
            "Grills and outdoor kitchens", "Dehumidifiers and wine coolers"])
  + "<h2>Refrigerator Disposal Done the Right Way</h2>"
  "<p>Refrigerators, freezers, dehumidifiers and air conditioners contain refrigerants. Under Section 608 of the federal Clean Air Act, those refrigerants must be recovered by certified technicians before the unit is scrapped. We deliver cooling appliances to recyclers who perform that recovery, then the steel, copper and aluminum are recycled. Most major appliances are about 60 to 75 percent steel by weight, so very little needs to be landfilled.</p>"
  "<h2>Washer, Dryer and Water Heater Removal in Homestead</h2>"
  "<p>Upgrading your laundry room? We can remove the old washer and dryer the day your new set arrives. For water heaters, we ask that the unit be drained and the power or gas shut off by a licensed plumber or the homeowner. Once disconnected, we carry it out through the garage or side yard and recycle the tank.</p>"
  "<h2>AC Unit Removal After Replacements and Storms</h2>"
  "<p>Homestead summers are brutal on air conditioners, and many homes replace condensers every 10 to 15 years. We haul old condensers, air handlers and window units, often alongside debris from storm cleanups. Remodel crews can bundle appliance hauling with construction debris removal for one easy invoice.</p>",
 steps_h2="How Appliance Pickup Works",
 steps_p="Quick, safe and fully handled from start to finish.",
 steps=[("Tell Us What It Is", "Share the appliance type, location and any stairs involved.", "phone"),
        ("Disconnect Check", "Make sure water, gas or hardwired power is shut off before we arrive.", "shield"),
        ("We Haul It Out", "Dollies and straps move the unit safely out of your home.", "truck"),
        ("Certified Recycling", "Refrigerant recovered and metals recycled by licensed facilities.", "recycle")],
 price_h2="Appliance Removal Cost in Homestead",
 price_intro="Typical Homestead prices for appliance pickup and recycling. Multiple appliances in one visit are discounted.",
 headers=["Appliance", "Notes", "Typical Price"],
 rows=[["Refrigerator or freezer", "Includes refrigerant handling", "$110 to $160"], ["Washer or dryer", "Each unit", "$95 to $125"],
       ["Washer and dryer pair", "Same visit", "$160 to $220"], ["Stove, range or dishwasher", "Each unit", "$95 to $125"],
       ["Water heater", "Must be drained", "$110 to $150"], ["AC condenser or air handler", "Disconnected by HVAC tech", "$120 to $175"]],
 note="Prices include labor, hauling and recycling fees inside our Homestead service area. Commercial units and walk-in coolers are quoted individually.",
 local_h2="Why Not Take It to the Moody Drive Center Yourself?",
 local_html="<p>Miami-Dade County does accept white goods such as stoves, refrigerators, water heaters, washers and dryers. Eligible residents can drop them off at the Moody Drive Trash and Recycling Center, 12970 SW 268th Street. The catch is that you need a truck or trailer, at least one strong helper and a way to safely tie down a 250-pound fridge on US 1.</p>"
  "<p>For most Homestead homeowners, a single appliance pickup costs less than a pickup truck rental plus fuel and time. We also take the appliance from inside the kitchen, which the county centers and curbside programs never do.</p>",
 local_img="dumpster-trailer-loaded-homestead", local_alt="Loaded hauling trailer at a Homestead property",
 related_h2="Services to Pair With Appliance Removal",
 related_p="Other services often booked together with appliance pickup in Homestead.",
 related=[("furniture-removal", "Clear out old couches and beds during the same trip."),
          ("garage-cleanout", "Remove that spare garage fridge and everything around it."),
          ("junk-removal", "Haul away boxes, packaging and household clutter too.")],
 areas_h2="Appliance Pickup Near You",
 areas_p="Appliance removal and recycling are available in these Homestead-area neighborhoods.",
 faq_h2="Appliance Removal FAQs",
 faq_p="What Homestead residents ask before scheduling appliance disposal.",
 faqs=[
  ("How much does refrigerator removal cost in Homestead?", "Refrigerator removal in Homestead typically costs $110 to $160. That price covers carrying it out, hauling it and delivering it to a recycler that recovers the refrigerant, as the Clean Air Act requires."),
  ("Do you disconnect appliances?", "We unplug standard appliances and disconnect washer hoses. Gas lines, hardwired units and water heater plumbing should be disconnected by a licensed professional before we arrive for safety and code reasons."),
  ("Will the City of Homestead pick up my old appliance?", "No. City of Homestead bulk pickup does not accept stoves, refrigerators, freezers, washers, dryers or water heaters. In unincorporated Miami-Dade, the county bulky program takes appliances only twice a year and refuses single items over 150 pounds. Most refrigerators weigh more than 200 pounds, so a private pickup is usually the fastest option."),
  ("Where do old appliances go?", "Appliances go to licensed scrap and appliance recyclers in Miami-Dade. Refrigerant is recovered, then steel, copper and aluminum are recycled. Working units in good condition may be donated."),
  ("Can you remove a fridge full of spoiled food after a power outage?", "Yes. After storms, we remove refrigerators with spoiled contents. We tape doors shut and wrap the unit to contain odors while carrying it through your home."),
  ("Do you take commercial appliances?", "Yes. We remove commercial refrigerators, ice machines and kitchen equipment from restaurants and businesses in Homestead. These are quoted individually based on size and weight."),
  ("How quickly can you pick up an appliance?", "Most appliance pickups in Homestead are completed the same day or next day. Calls before noon usually qualify for same-day service."),
  ("Do you remove old water heaters?", "Yes. Once the water heater is drained and disconnected, we remove it for $110 to $150. Tank water heaters usually weigh 100 to 150 pounds empty."),
  ("Can I get a discount for several appliances?", "Yes. Because we price by truck volume, bundling a washer, dryer and refrigerator in one visit costs less than booking three separate pickups."),
  ("Do you remove AC units and pool equipment?", "Yes. We haul old AC condensers, air handlers, window units, pool pumps and heaters. HVAC units should be disconnected by a licensed technician before pickup."),
 ],
 cta_h2="Schedule Appliance Removal Today",
 cta_p="Safe removal and certified recycling for any home appliance in Homestead. Call for a quick quote.",
)

DUMP = dict(
 slug="dumpster-rental", name="Dumpster Rental", schema_name="Dumpster Rental in Homestead, FL", min=295,
 title="Dumpster Rental in Homestead, FL | Roll-Off Dumpsters",
 desc="Dumpster rental in Homestead, FL 33030. 10-, 15- and 20-yard roll-off dumpsters for cleanouts, roofing and remodels, with 7 days included. Call 877-745-9845.",
 h1="Roll-Off <em>Dumpster Rental</em> in Homestead, FL",
 lead="Load at your own pace with a driveway-friendly roll-off dumpster. Flat-rate pricing includes delivery, pickup, disposal and a full week on site for Homestead homeowners and contractors.",
 points=["10-, 15- and 20-yard sizes", "7-day standard rental", "Driveway-safe placement", "Next-day delivery"],
 hero_img="roll-off-dumpster-rental-homestead", hero_alt="Roll-off dumpsters available for rent in Homestead, FL",
 eyebrow="Homestead, FL Dumpster Rental",
 intro_h2="Affordable Dumpster Rental for Homestead Contractors and Homeowners",
 intro_html="<p>When a project runs several days or produces a lot of debris, a dumpster is usually the most cost-effective option. Our trailer-mounted roll-off dumpsters are smaller and lighter than typical commercial units. They fit in residential driveways, slide under carports and cause less wear on pavers.</p>"
  "<p>We deliver throughout Homestead, Florida City, the Redland and Leisure City, from new builds in Keys Gate to farm properties along Krome Avenue. Every rental comes with a clear weight allowance, a flat price and a scheduled pickup, so there are no surprises when the job wraps up.</p>",
 intro_img="dumpster-delivery-driveway-homestead", intro_alt="Dumpster delivered under a carport in a Homestead driveway",
 badge="<b>7 days</b>included with every standard rental",
 body_html="<h2>Which Dumpster Size Do I Need?</h2>"
  "<p>Choosing the right size saves money. A cubic yard is about the size of a washing machine. Here is a quick guide:</p>"
  + checks(["10 yard: bathroom remodel or small garage cleanout", "10 yard: about 4 pickup truck loads", "15 yard: kitchen remodel or 1,500 sq ft flooring",
            "15 yard: about 6 pickup truck loads", "20 yard: whole-house cleanout or roof tear-off", "20 yard: about 8 pickup truck loads"])
  + "<h2>Roofing Dumpster Rental in Homestead</h2>"
  "<p>Roofing shingles are heavy. One square of asphalt shingles, which covers 100 square feet, weighs roughly 200 to 350 pounds. A typical 2,000-square-foot Homestead roof can produce 3 to 4 tons of debris, so we match roofers with the right container and weight allowance. Tile and concrete roofs, common in South Florida, are heavier still and priced by the ton.</p>"
  "<h2>What You Can and Cannot Put in the Dumpster</h2>"
  "<p>Household junk, furniture, drywall, lumber, flooring, cabinets, shingles and yard waste are all fine. Not allowed: paint, oil, chemicals, batteries, tires, propane tanks, asbestos and hazardous waste. Appliances with refrigerant should be booked separately through our appliance removal service.</p>"
  "<h2>Dumpster vs Full-Service Junk Removal</h2>"
  "<p>If you have a few days and people to help load, a dumpster usually wins on cost. If you would rather not lift anything, or the job takes a single afternoon, full-service junk removal is often cheaper. Labor is included, and nothing sits in your driveway.</p>",
 steps_h2="How Dumpster Rental Works in Homestead",
 steps_p="Simple scheduling from delivery to pickup.",
 steps=[("Choose a Size", "Tell us about your project, and we will recommend a 10-, 15- or 20-yard dumpster.", "list"),
        ("We Deliver", "We set it on boards in your driveway or job site, usually the next day.", "truck"),
        ("You Fill It", "Load at your pace for up to 7 days. Keep debris level with the top.", "calendar"),
        ("We Haul It Away", "Call for pickup, and we haul it away and dispose of the debris responsibly.", "recycle")],
 price_h2="Dumpster Rental Prices in Homestead, FL",
 price_intro="Flat-rate pricing includes delivery, pickup, 7 days and the listed weight allowance.",
 headers=["Dumpster Size", "Weight Allowance", "Typical Price"],
 rows=[["10 yard", "1 ton included", "$295 to $375"], ["15 yard", "2 tons included", "$365 to $450"],
       ["20 yard", "3 tons included", "$425 to $525"], ["Extra days", "Per day after 7", "$15 to $25"], ["Extra weight", "Per ton over allowance", "$65 to $85"]],
 note="Concrete, dirt and clean fill require special dumpsters and are priced separately. Permits may be required for street placement in the City of Homestead.",
 local_h2="Driveway-Friendly Dumpsters for South Dade Homes",
 local_html="<p>Many Homestead homes have paver driveways and tight HOA rules. We lay protective boards under every container and place it exactly where you choose. Because our units are trailer-mounted, we can reach backyards and side yards that large roll-off trucks cannot.</p>"
  "<p>For placement on a public street or swale, check with the City of Homestead or Miami-Dade County. A right-of-way permit may be required. Most customers avoid this by placing the dumpster in the driveway, which needs no permit.</p>",
 local_img="construction-dumpster-homestead-fl", local_alt="Dumpster placed at a construction site in Homestead",
 related_h2="Other Debris Solutions",
 related_p="Not sure a dumpster is right? These services may fit your project better.",
 related=[("construction-debris-removal", "We load and haul renovation debris for you, no container needed."),
          ("hurricane-debris-removal", "Fast storm cleanup with crews and dumpsters after hurricanes."),
          ("estate-cleanout", "Full home cleanouts with labor included for families and executors.")],
 areas_h2="Dumpster Delivery Areas",
 areas_p="We deliver roll-off dumpsters to all of these Homestead-area communities.",
 faq_h2="Dumpster Rental FAQs",
 faq_p="Common questions about renting a dumpster in Homestead, FL.",
 faqs=[
  ("How much does it cost to rent a dumpster in Homestead?", "A 10-yard dumpster typically costs $295 to $375, a 15-yard dumpster costs $365 to $450, and a 20-yard dumpster costs $425 to $525. Prices include delivery, pickup, 7 days and a set weight allowance."),
  ("Do I need a permit for a dumpster in Homestead?", "No permit is needed when the dumpster sits on your private driveway. Placement on a public street, sidewalk or swale may require a right-of-way permit from the City of Homestead or Miami-Dade County."),
  ("How long can I keep the dumpster?", "Standard rentals include 7 days. Extra days usually cost $15 to $25 each, and you can call for early pickup any time the dumpster is full."),
  ("Will the dumpster damage my driveway?", "We place boards under every dumpster to spread the weight and protect concrete and pavers. Our trailer-mounted units are also lighter than traditional roll-off trucks."),
  ("What size dumpster do I need for a roof?", "Most asphalt shingle roofs on Homestead homes need a 15- or 20-yard dumpster. A 2,000-square-foot roof can produce 3 to 4 tons of debris, so weight matters more than volume."),
  ("How fast can you deliver a dumpster?", "Next-day delivery is standard in Homestead, and same-day delivery is often possible when you call before 10 AM."),
  ("What is not allowed in a dumpster?", "Paint, oil, chemicals, tires, batteries, propane tanks, asbestos and other hazardous waste are not allowed. Refrigerant appliances need separate handling."),
  ("What happens if I go over the weight limit?", "Overweight tonnage is billed at the landfill rate, typically $65 to $85 per ton. We help you estimate weight before delivery to avoid surprises."),
  ("Can I put yard waste in the dumpster?", "Yes. Branches, palm fronds and brush are allowed. For large yard jobs, a dedicated yard waste load can be cheaper because clean vegetation often costs less to dispose of."),
  ("Do you rent dumpsters to contractors?", "Yes. Contractors in Homestead and Florida City use our dumpsters for remodels, new construction cleanups and roofing projects, with swap-outs available on busy sites."),
 ],
 cta_h2="Reserve Your Homestead Dumpster",
 cta_p="Next-day delivery, flat-rate pricing and driveway-safe placement. Call to book your size.",
)

PAGES = [FURN, APPL, DUMP]
