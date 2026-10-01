from lib import *
import zips, seo

# Standard volume pricing shared by the homepage, hubs and location pages
PRICE_HEADERS = ["Load Size", "What It Usually Holds", "Typical Price Range"]
PRICE_ROWS = [["Single item", "One couch, mattress or appliance", "$95 to $150"],
              ["1/8 truck (about 2 yards)", "Loveseat plus a few boxes", "$130 to $175"],
              ["1/4 truck (about 4 yards)", "Bedroom set or small garage corner", "$180 to $280"],
              ["1/2 truck (about 7.5 yards)", "One-car garage or small apartment", "$300 to $425"],
              ["3/4 truck (about 11 yards)", "Packed one-car garage or several rooms", "$440 to $560"],
              ["Full truck (about 15 yards)", "Two-car garage or a small home's contents", "$560 to $650"]]

FC = dict(
 slug="florida-city", name="Florida City", zips="33034", map_q="Florida+City,+FL+33034",
 title="Junk Removal in Florida City, FL 33034 | Same-Day Pickup",
 desc="Junk removal in Florida City, FL 33034. Same-day junk pickup, furniture and appliance hauling, cleanouts and dumpsters. Upfront prices. Call 877-745-9845.",
 h1="Junk Removal in <em>Florida City, FL 33034</em>",
 lead="From motel turnovers on US 1 to backyard cleanups west of Krome Avenue, we haul junk across Florida City. Call before noon, and we can usually come the same day. You get an upfront price before we lift a thing.",
 points=["Same-day pickup in 33034", "Upfront, volume-based pricing", "Homes, rentals and businesses", "Donation and recycling first"],
 hero_img="junk-hauling-truck-homestead", hero_alt="Junk hauling truck on a job in Florida City, FL",
 intro_h2="Local Junk Hauling for Florida City Homes and Businesses",
 intro_html="<p>Florida City is the last stop on US 1 before the 18-Mile Stretch to Key Largo, and the Florida's Turnpike ends right here. That makes it a busy city of about 13,000 residents. It has single-family homes, apartment complexes and farm properties. It also has a long row of hotels, restaurants and shops that serve travelers heading to the Keys and Everglades National Park.</p>"
  "<p>All of that turnover creates junk. Tenants move out and leave furniture behind. Hotels replace mattresses and TVs. Growers west of town clear out old equipment and shade-house frames. Florida City is part of our core service area, so there is never a travel fee.</p>"
  "<p>Whether it is one old recliner or a whole rental that needs to be emptied before it is listed, our two-person crew does the lifting, loading and sweeping.</p>",
 intro_img="commercial-debris-dumpster-homestead", intro_alt="Commercial junk and debris loaded for removal in Florida City",
 badge="<b>No travel fee</b>anywhere in Florida City",
 body_html="<h2>What We Haul Away in Florida City</h2>"
  "<p>If two people can safely carry it, we can usually take it. Popular Florida City pickups include:</p>"
  + checks(["Couches, beds and dressers", "Mattresses and box springs", "Refrigerators and washers", "TVs and electronics",
            "Motel and rental furniture", "Office and retail fixtures", "Old sheds and playsets", "Palm fronds and yard waste"])
  + "<p>For single bulky pieces, see our furniture removal and appliance removal services. We cannot haul paint, fuel, pool chemicals, propane tanks, asbestos or medical waste.</p>"
  "<h2>Why Florida City Residents Call a Junk Removal Company</h2>"
  "<p>Florida City is its own municipality, so it sets its own trash and bulk pickup schedule. Bulk collection also has limits on what goes to the curb and how much. Construction debris, tires, concrete and large piles often do not qualify. You also have to drag everything to the street yourself in the South Florida heat.</p>"
  "<p>A private pickup skips the waiting and the heavy lifting. We carry items from inside the home, garage or unit, haul them away the same day and pay the disposal fees. Landlords and property managers use us between tenants so units can be cleaned, painted and rented without a pile of old furniture sitting in the parking lot.</p>"
  "<h2>Business Cleanouts Along US 1 and Palm Drive</h2>"
  "<p>Hotels, restaurants, shops and offices along US 1 and Palm Drive rely on us for commercial junk removal. Typical jobs include mattress and furniture swaps, kitchen equipment, display fixtures, pallets and cardboard. We schedule early mornings or after closing, so guests and customers never see the work. For businesses that generate junk every month, we can return on a recurring schedule.</p>",
 price_h2="Junk Removal Cost in Florida City, FL",
 price_intro="Florida City pricing is simple. You pay for the space your items take up in our 15-cubic-yard truck, with labor, travel and disposal included.",
 local_h2="Farm, Grove and Storm Cleanup West of Florida City",
 local_html="<p>West of Krome Avenue, Florida City blends into working farmland, nurseries and packing houses. We clear out broken irrigation parts, old shade cloth and frames, worn-out farm furniture, tires and the occasional abandoned trailer. When a property needs a big one-day cleanup, we bring a second truck.</p>"
  "<p>Florida City took the full force of Hurricane Andrew in 1992, and every hurricane season since has been a reminder to stay ready. When a storm passes, we add crews for hurricane debris and yard waste removal. We haul downed limbs, fencing and water-damaged contents, so you are not waiting weeks for public storm debris collection.</p>",
 local_img="furniture-junk-pickup-homestead", local_alt="Old furniture picked up from a home in Florida City, FL",
 faq_h2="Florida City Junk Removal FAQs",
 faq_p="Answers to the questions Florida City customers ask most before booking.",
 faqs=[
  ("How much does junk removal cost in Florida City?", "Most Florida City jobs cost between $95 for a single item and about $650 for a full 15-cubic-yard truckload. A quarter truck, which fits a bedroom set or a small garage corner, usually runs $180 to $280. We confirm the exact price on site before we start."),
  ("Do you offer same-day junk pickup in Florida City, FL 33034?", "Yes. Calls before noon usually get same-day service in Florida City, and afternoon calls are normally handled the next morning. You get a two-hour arrival window and a call about 30 minutes before the crew arrives."),
  ("Do you charge a travel fee to Florida City?", "No. Florida City sits inside our core service area, so travel is included in the price you are quoted."),
  ("Can you clear out a motel room or rental unit?", "Yes. We remove mattresses, beds, dressers, TVs and anything else left behind, from one room or an entire property. Hotels and landlords can book early-morning or recurring pickups."),
  ("Will you pick up from farm or nursery properties?", "Yes. We haul old equipment parts, shade-house frames, irrigation pipe, tires, pallets and farm debris from properties west of Krome Avenue. Hazardous chemicals and fuel are the exceptions."),
  ("Do you donate items from Florida City pickups?", "Yes. Usable furniture and household goods go to local donation partners in South Miami-Dade, metal goes to scrap recyclers, and cardboard is recycled. Only what is left goes to a licensed disposal facility."),
 ],
 cta_h2="Need Junk Gone in Florida City Today?",
 cta_p="Call for a free, no-obligation price. Same-day junk removal is available across Florida City and the rest of South Dade.",
)

CB = dict(
 slug="cutler-bay", name="Cutler Bay", zips="33157, 33189, 33190", map_q="Cutler+Bay,+FL",
 title="Junk Removal in Cutler Bay, FL 33157, 33189 and 33190",
 desc="Junk removal in Cutler Bay, FL 33189. Same-day furniture, appliance and junk pickup, garage and estate cleanouts with upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in <em>Cutler Bay, FL</em>",
 lead="Remodeling in Saga Bay, cleaning out a parent's home in Lakes by the Bay or just done with the clutter? Our crew lifts, loads and hauls it away across Cutler Bay with an upfront price and a clean sweep at the end.",
 points=["Same-day and next-day pickup", "Priced by truck volume", "We carry from any room", "Donate and recycle first"],
 hero_img="estate-cleanout-home-homestead", hero_alt="Home ready for a junk removal cleanout in Cutler Bay, FL",
 intro_h2="Full-Service Junk Removal for Cutler Bay Homeowners",
 intro_html="<p>Cutler Bay became a town in 2005 and today is home to about 45,000 people between US 1 and Biscayne Bay. Much of it was built from the 1960s through the 1980s, and many of those homes are now being remodeled, downsized or passed to the next generation. That means kitchens coming out, garages full of decades of storage and whole houses that need to be emptied before a sale.</p>"
  "<p>Cutler Bay homes are a regular part of our schedule. Each truck holds about 15 cubic yards, roughly six pickup beds, and most household jobs are finished in one trip. Two movers handle everything from the back bedroom to the backyard shed, and you never have to haul a sofa to the swale.</p>"
  "<p>We work in Saga Bay, Lakes by the Bay, Cutler Ridge and the neighborhoods off Old Cutler Road, Caribbean Boulevard and SW 216th Street.</p>",
 intro_img="garage-junk-pickup-carport-homestead", intro_alt="Garage junk pickup from a carport in Cutler Bay",
 badge="<b>15 yards</b>of space in every truck",
 body_html="<h2>Junk We Remove Across Cutler Bay</h2>"
  "<p>We take almost everything that is not hazardous, including:</p>"
  + checks(["Sofas, sectionals and recliners", "Mattresses and bed frames", "Old kitchen cabinets and counters", "Refrigerators, washers and dryers",
            "Garage and attic clutter", "Patio sets and grills", "Exercise equipment", "Hot tubs and playsets"])
  + "<p>Bigger projects often combine services: a garage cleanout with appliance removal, or a remodel that needs construction debris removal once the demo crew is done.</p>"
  "<h2>Why Hire Junk Haulers Instead of Waiting for Bulky Pickup</h2>"
  "<p>Most Cutler Bay homes are covered by Miami-Dade County waste collection, which includes two bulky waste pickups per year of up to 25 cubic yards each. The county will not take single items over 150 pounds, construction debris or tires. It also rejects anything left in the swale more than 3 days before your appointment. And you still have to carry it all out yourself.</p>"
  "<p>With a private pickup, the crew removes items from inside the house and loads the truck on the spot. Nothing is left on the lawn for neighbors or code enforcement to notice. For families on a closing date or landlords between tenants, same-day removal is often worth far more than waiting weeks for a free slot.</p>"
  "<h3>Read More: <a href=\"/blog/homestead-bulk-trash-pickup-rules\">Bulk Trash Pickup Rules Explained</a></h3>"
  "<h2>Estate Cleanouts and Downsizing in Cutler Bay</h2>"
  "<p>Many Cutler Bay homes have been in the same family for decades. When it is time to sell, our estate cleanout team works room by room, sets aside keepsakes and paperwork for you, donates what is usable and hauls the rest. Realtors and executors can hand us a key, and we will call when the home is empty and swept.</p>",
 price_h2="Junk Removal Prices in Cutler Bay, FL",
 price_intro="You pay only for the space your items fill in the truck. Labor, loading, travel to Cutler Bay and disposal fees are included in every price.",
 local_h2="Storm-Ready Junk Removal Near Biscayne Bay",
 local_html="<p>Cutler Bay sits right on Biscayne Bay. In 1992, Hurricane Andrew brought one of the worst storm surges in the area's history. Low-lying streets near the bay still see flooding in heavy summer storms. When water gets in, soaked carpet, drywall and furniture need to come out fast before mold sets in, and our crews prioritize those calls.</p>"
  "<p>After storms, our hurricane debris crews remove fallen limbs, broken fencing and damaged sheds. Our yard waste service clears the palm fronds and branches that pile up every season.</p>",
 local_img="storm-debris-lumber-pile-homestead", local_alt="Storm debris and lumber pile removed in Cutler Bay",
 faq_h2="Cutler Bay Junk Removal FAQs",
 faq_p="What Cutler Bay homeowners ask most about junk pickup, pricing and timing.",
 faqs=[
  ("How much does junk removal cost in Cutler Bay?", "Most Cutler Bay jobs cost between $95 for one bulky item and about $650 for a full 15-cubic-yard truck. A half truck, which usually covers a one-car garage, runs $300 to $425. The final price is confirmed on site before any work starts."),
  ("Do you serve all of Cutler Bay?", "Yes. We cover ZIP codes 33157, 33189 and 33190. That includes Saga Bay, Lakes by the Bay, Cutler Ridge and the neighborhoods along Old Cutler Road and Caribbean Boulevard."),
  ("Can I get same-day junk removal in Cutler Bay?", "Usually, yes. Call before noon, and we can often arrive the same day. Otherwise, we schedule a two-hour window the next day and call about 30 minutes before the crew arrives."),
  ("Do you remove water-damaged carpet and drywall after flooding?", "Yes. We remove soaked carpet, padding, drywall, cabinets and furniture after floods and storms, and we can move quickly so drying and repairs can start."),
  ("Why not just use the county bulky waste pickup?", "County bulky pickup is limited to two appointments per year. It refuses single items over 150 pounds and construction debris, and you must move everything to the swale yourself. We carry items from inside and haul them the same day."),
  ("Do you handle estate cleanouts for realtors and executors?", "Yes. We empty whole homes, set aside documents and keepsakes, donate usable items and leave the home broom-clean. You do not need to be on site if a realtor or property manager provides access."),
 ],
 cta_h2="Ready for Junk Removal in Cutler Bay?",
 cta_p="Call now for a free, upfront quote. Same-day junk pickup is available across Cutler Bay and South Miami-Dade.",
)

LC = dict(
 slug="leisure-city", name="Leisure City", zips="33033", map_q="Leisure+City,+FL+33033",
 title="Junk Removal in Leisure City, FL 33033 | Same-Day Hauling",
 desc="Junk removal in Leisure City, FL 33033. Same-day junk hauling for furniture, appliances, yard waste and cleanouts. Upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in <em>Leisure City, FL 33033</em>",
 lead="Old furniture in the carport, a broken fridge on the patio or a rental that needs clearing? Our crew handles junk hauling across Leisure City, often the same day, and you get a firm price before we start.",
 points=["Same-day pickup in 33033", "No need to drag junk to the curb", "Upfront volume pricing", "Homes, rentals and yards"],
 hero_img="dumpster-delivery-driveway-homestead", hero_alt="Junk removal and dumpster delivery on a Leisure City driveway",
 intro_h2="Your Neighborhood Junk Removal Crew in Leisure City",
 intro_html="<p>Leisure City sits close to our base. It is an unincorporated community of more than 22,000 people. Many of its block homes date from the 1950s to the 1970s, and they sit alongside newer houses, duplexes and apartment complexes.</p>"
  "<p>Older homes and busy households mean full carports, crowded sheds and backyards that collect broken furniture and appliances. We clear all of it in one visit. Two movers carry everything out, load a 15-cubic-yard truck and sweep up, so the only thing you do is point.</p>"
  "<p>Leisure City is close to our base, so scheduling is quick, and there is no travel fee.</p>",
 intro_img="junk-removal-truck-homestead-fl", intro_alt="Junk removal truck parked at a Leisure City home",
 badge="<b>Close by</b>for quick Leisure City pickups",
 body_html="<h2>What We Pick Up in Leisure City</h2>"
  "<p>Common Leisure City junk removal jobs include:</p>"
  + checks(["Carport and patio clutter", "Couches, mattresses and beds", "Old refrigerators and freezers", "Washers, dryers and water heaters",
            "Broken sheds and fencing", "Tires and car parts", "Yard waste and tree limbs", "Move-out and tenant leftovers"])
  + "<p>Need more room to work? Pair a pickup with a garage cleanout, or rent a dumpster for a remodel that will take a few weeks.</p>"
  "<h2>County Bulky Pickup Rules in Leisure City</h2>"
  "<p>Leisure City is unincorporated, so trash service comes from Miami-Dade County rather than a city government. The county allows two bulky waste pickups per year, up to 25 cubic yards each. It will not collect single items over 150 pounds, construction debris or tires. Piles can go out no more than 3 days before the appointment, and anything placed early can bring a code citation.</p>"
  "<p>A private pickup is the easy fix when your two county pickups are used up. It also helps with heavy items like a fridge or hot tub, or when you cannot wait weeks. We take items straight from wherever they sit and handle disposal and recycling for you.</p>"
  "<h3>Read More: <a href=\"/blog/homestead-bulk-trash-pickup-rules\">Bulk Trash Pickup Rules Explained</a></h3>"
  "<h2>Rental Turnovers and Move-Outs</h2>"
  "<p>Leisure City has many rental homes and duplexes. With military families moving in and out near Homestead Air Reserve Base, tenant turnovers happen year-round. Landlords and property managers call us to remove everything left behind in one visit so the unit can be cleaned and rented the same week. We can work from a lockbox code and call you when the job is done.</p>",
 price_h2="Junk Removal Cost in Leisure City, FL",
 price_intro="Leisure City pricing is simple. You pay for the truck space your items use, with labor, travel and disposal included.",
 local_h2="Backyard and Yard Waste Cleanup in Leisure City",
 local_html="<p>Leisure City lots often have mature mango, avocado and palm trees, and they drop a steady stream of fronds, branches and fruit. After a trim, or after a summer storm, we bag and haul the whole pile through our yard waste removal service so it is not sitting on the swale for weeks.</p>"
  "<p>We also tear down and remove rotted wood sheds, old chain-link fencing, playsets and above-ground pools. When a storm brings down limbs and fences across the neighborhood, we handle hurricane debris removal too.</p>",
 local_img="garage-cleanout-before-after-homestead", local_alt="Garage cleanout before and after in Leisure City, FL",
 faq_h2="Leisure City Junk Removal FAQs",
 faq_p="Quick answers for Leisure City homeowners, renters and landlords.",
 faqs=[
  ("How much does junk removal cost in Leisure City?", "Most Leisure City jobs cost between $95 for a single item and about $650 for a full 15-cubic-yard truck. A quarter truck, about a bedroom set, runs $180 to $280. We confirm the exact price on site before loading."),
  ("Can you pick up junk the same day in Leisure City, FL 33033?", "Yes. Our crews are minutes away, so calls before noon usually get same-day pickup. Later calls are normally scheduled for the next morning."),
  ("I already used my two county bulky pickups. Can you help?", "Yes. We are not limited by the county schedule. We take loads larger than the county limit, including items over 150 pounds, construction debris and tires that county bulky pickup refuses."),
  ("Do I have to bring the junk to the curb?", "No. We pick up from carports, backyards, sheds and inside the home. Keeping items off the swale also avoids county rules about placing piles more than 3 days before a pickup."),
  ("Do you tear down old sheds?", "Yes. We take apart and remove wood and metal sheds, playsets, fencing and above-ground pools, then haul all the debris away."),
  ("Do you work with landlords and property managers?", "Yes. We handle tenant move-outs and evictions with lockbox access and itemized invoices for your records, so you do not need to meet us on site."),
 ],
 cta_h2="Clear Out Your Leisure City Home Today",
 cta_p="Call for a free, upfront price. Same-day junk removal is available across Leisure City and all of South Dade.",
)

PR = dict(
 slug="princeton", name="Princeton", zips="33032", map_q="Princeton,+FL+33032",
 title="Junk Removal in Princeton, FL 33032 | Pickup and Cleanouts",
 desc="Junk removal in Princeton, FL 33032. Same-day junk pickup, move-in and move-out cleanouts, construction debris and garage cleanouts. Call 877-745-9845.",
 h1="Junk Removal in <em>Princeton, FL 33032</em>",
 lead="New home boxes, builder leftovers or a garage that filled up faster than expected? Our crew clears it out across Princeton with same-day service and an upfront price before we lift anything.",
 points=["Same-day pickup in 33032", "HOA-friendly, nothing left out", "Upfront volume pricing", "Move-in and move-out help"],
 hero_img="construction-dumpster-homestead-fl", hero_alt="Construction debris ready for removal at a new home in Princeton, FL",
 intro_h2="Junk Removal for One of South Dade's Fastest-Growing Communities",
 intro_html="<p>Princeton has been one of the fastest-growing communities in South Miami-Dade over the past decade. Farmland between US 1 and Krome Avenue has become new subdivisions, townhomes and apartments. Much of that growth is along SW 248th Street, also known as Coconut Palm Drive.</p>"
  "<p>Growth brings a steady stream of junk. Think moving boxes, packing foam and furniture that did not fit the new floor plan. Add builder leftovers from upgrades and older nearby homes being remodeled. We handle all of it. Two movers lift and load, and a 15-cubic-yard truck clears most jobs in one trip.</p>"
  "<p>Princeton is inside our core service area, so same-day pickup is often available and there is no travel fee.</p>",
 intro_img="roll-off-dumpster-rental-homestead", intro_alt="Roll-off dumpster for a remodel project in Princeton, FL",
 badge="<b>1 trip</b>clears most move-in messes",
 body_html="<h2>What We Haul Away in Princeton</h2>"
  "<p>Some of the most common Princeton pickups include:</p>"
  + checks(["Moving boxes and packing material", "Old furniture and mattresses", "Appliances replaced in upgrades", "Builder scraps and trim",
            "Garage and closet clutter", "Patio furniture and grills", "Exercise equipment", "Kids' playsets and trampolines"])
  + "<p>Doing upgrades after closing? Our construction debris removal clears drywall, tile, flooring and cabinets. For longer projects, a driveway dumpster lets you load at your own pace.</p>"
  "<h2>HOA-Friendly Junk Pickup</h2>"
  "<p>Many Princeton subdivisions have homeowners associations with rules about piles, trailers and bulk items sitting out front. Princeton is also unincorporated, so county bulky collection rules apply. You get two pickups per year, nothing over 150 pounds and nothing placed out more than 3 days early. That leaves a lot of junk with nowhere to go.</p>"
  "<p>We avoid the problem entirely. Our crew picks up straight from the garage, patio or inside the home, loads the truck on the spot and leaves nothing on the curb for the HOA to flag. If you need a pickup on a specific day for an inspection or walk-through, we will schedule around it.</p>"
  "<h2>Move-In and Move-Out Cleanouts</h2>"
  "<p>New homeowners call us after the movers leave to clear boxes and the furniture that did not make the cut. Sellers and renters call us before they leave to empty garages, sheds and closets. Either way, one visit takes care of it, and usable items go to local donation partners instead of the landfill.</p>",
 price_h2="Junk Removal Prices in Princeton, FL",
 price_intro="Prices are based on truck volume, with labor, loading, travel and disposal included. The final price is always confirmed on site before we start.",
 local_h2="Garage and Remodel Cleanups Across Princeton",
 local_html="<p>Newer Princeton homes often have compact garages that fill quickly with overflow furniture, tools and boxes. Our garage cleanout service sorts what you keep, hauls the rest and sweeps the floor so you can park inside again, which matters in South Florida summers.</p>"
  "<p>For contractors and homeowners doing larger remodels, we remove tear-out debris between phases so the site stays clean for inspections. We can also return on a set schedule as the project moves forward.</p>",
 local_img="dumpster-trailer-loaded-homestead", local_alt="Loaded junk trailer after a cleanout in Princeton, FL",
 faq_h2="Princeton Junk Removal FAQs",
 faq_p="Common questions from Princeton homeowners, renters and builders.",
 faqs=[
  ("How much does junk removal cost in Princeton, FL?", "Most Princeton jobs range from $95 for a single item to about $650 for a full 15-cubic-yard truckload. Pickups of moving boxes and packing material often fit in a quarter truck for $180 to $280."),
  ("Do you pick up moving boxes and packing material?", "Yes. We haul flattened or loose boxes, foam, plastic wrap and packing paper, and cardboard is recycled whenever possible."),
  ("Will my HOA have a problem with the pickup?", "No. We load directly from the garage, patio or inside the home, so nothing sits on the curb or lawn. The crew is usually in and out in under an hour for typical jobs."),
  ("Can you remove builder leftovers and remodel debris?", "Yes. We remove drywall, tile, flooring, trim, cabinets and packaging from upgrades and remodels. Very heavy materials such as concrete or tile in bulk may be priced by weight."),
  ("Is same-day junk removal available in Princeton?", "Yes. Call before noon for the best chance of same-day service. You will get a two-hour arrival window and a call about 30 minutes before we arrive."),
  ("What ZIP code do you cover in Princeton?", "We cover every street in Princeton's ZIP code, 33032, with no travel fee. That includes the newer subdivisions along SW 248th Street and the older homes near US 1."),
 ],
 cta_h2="Get Your Princeton Junk Hauled Today",
 cta_p="Call now for a free, upfront quote. Same-day junk pickup is available across Princeton and South Miami-Dade.",
)

RL = dict(
 slug="redland", name="Redland", zips="33031, 33170, 33187", map_q="Redland,+FL",
 title="Junk Removal in the Redland, FL 33031 | Farm Cleanouts",
 desc="Junk removal in the Redland, FL 33031. Farm and grove cleanups, yard waste, sheds, appliances and property cleanouts with upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in the <em>Redland, FL</em>",
 lead="Big lots, long driveways and years of stored equipment? Our crew clears homes, barns, groves and nurseries across the Redland with upfront pricing and trucks that handle rural properties with ease.",
 points=["Acreage and farm cleanouts", "Sheds, trailers and equipment", "Yard waste and storm debris", "Upfront volume pricing"],
 hero_img="yard-waste-removal-before-after-homestead", hero_alt="Yard waste and brush removed from a Redland property",
 intro_h2="Rural Junk Removal Built for Redland Properties",
 intro_html="<p>The Redland is the agricultural heart of South Miami-Dade. It stretches across the western edge of the county, with tropical fruit groves, plant nurseries, horse properties and homes on large lots along Krome Avenue. Properties here collect a different kind of junk than a city lot. Common finds include old farm equipment, rusted sheds, shade-house frames, irrigation pipe, tires and decades of stored belongings.</p>"
  "<p>Our crews are set up for that. We bring a two-person crew, a 15-cubic-yard truck and the tools to take apart sheds and structures, and we are comfortable on gravel drives and grass lanes. If the job needs more than one load, we plan multiple trips or send a second truck so the work finishes in one day.</p>",
 intro_img="storm-debris-lumber-pile-homestead", intro_alt="Lumber and debris pile cleared from a Redland farm",
 badge="<b>Big lots</b>and big cleanouts welcome",
 body_html="<h2>What We Remove From Redland Homes and Farms</h2>"
  "<p>Typical Redland pickups include:</p>"
  + checks(["Old sheds and barn contents", "Shade-house frames and cloth", "Irrigation pipe and fittings", "Tires and equipment parts",
            "Old trailers and camper junk", "Fencing and gates", "Tree limbs and brush piles", "Household furniture and appliances"])
  + "<p>For big brush piles, see our yard waste removal service. For a remodel or an extended cleanup, a roll-off dumpster can sit on site while you work.</p>"
  "<h2>Why Redland Owners Hire a Junk Hauling Company</h2>"
  "<p>The Redland is unincorporated, so county bulky collection rules apply. You get two pickups per year of up to 25 cubic yards each. No single item can exceed 150 pounds, and construction debris and tires are not accepted. On a large property, that barely scratches the surface. Loading a borrowed trailer for trips to the Moody Drive center also means many hot hours of work.</p>"
  "<p>We handle the lifting, loading and disposal, and we sort metal for scrap, usable items for donation and green waste for mulch where possible. You get one price upfront and one visit that clears the whole list.</p>"
  "<h3>Read More: <a href=\"/blog/homestead-bulk-trash-pickup-rules\">Bulk Trash Pickup Rules Explained</a></h3>"
  "<h2>Estate and Property Cleanouts on Acreage</h2>"
  "<p>When a Redland property is sold or passed down, there is often a house, a barn and several outbuildings to empty. Our estate cleanout team works through each building and sets aside anything the family wants to keep. Every structure is left clean for buyers, surveyors and appraisers.</p>",
 price_h2="Junk Removal Cost in the Redland",
 price_intro="Redland pricing uses simple volume rates. Very heavy materials such as concrete, rock or scrap metal in bulk may be priced by weight.",
 local_h2="Storm and Grove Cleanup in the Redland",
 local_html="<p>Open groves and tall trees take a beating in tropical storms. The Redland saw heavy damage from Hurricane Andrew in 1992 and again from Hurricane Irma in 2017. After a storm, we run hurricane debris removal for downed limbs, twisted shade structures, broken fencing and damaged sheds.</p>"
  "<p>We also help growers and nurseries clear out dead trees after a freeze or disease outbreak. We remove old pots, trays and worn-out equipment too, and we work around your harvest and shipping schedule.</p>",
 local_img="dumpster-trailer-loaded-homestead", local_alt="Trailer loaded with junk from a Redland property cleanout",
 faq_h2="Redland Junk Removal FAQs",
 faq_p="What Redland homeowners, growers and nurseries ask most.",
 faqs=[
  ("How much does junk removal cost in the Redland?", "Most Redland jobs cost between $95 for one item and about $650 per full 15-cubic-yard truckload. Large farm cleanouts often need multiple loads, and we quote the full job upfront."),
  ("Do you remove old sheds, trailers and farm equipment?", "Yes. We take apart and remove sheds, shade structures, fencing and junk trailers, and we haul equipment parts, tires and irrigation pipe. Fuel, oil and chemicals must be drained or removed first."),
  ("Can your truck get down long or gravel driveways?", "Yes. Our trucks regularly work on rural Redland properties with gravel drives and grass lanes. Let us know about low branches or soft ground when you call, and we will plan for it."),
  ("Do you recycle metal and green waste?", "Yes. Scrap metal goes to recyclers, and usable items go to donation partners. Clean yard waste is mulched where possible, which keeps more out of the landfill."),
  ("What areas of the Redland do you cover?", "We cover the Redland in ZIP codes 33031, 33170 and 33187, with no travel fee anywhere in the Redland."),
  ("Can you handle a whole property cleanout in one day?", "Most can be done in a day. For very large properties, we send a second truck or plan back-to-back loads so the house, barn and outbuildings are cleared together."),
 ],
 cta_h2="Clear Your Redland Property Today",
 cta_p="Call for a free, upfront quote on your home, grove or nursery cleanout.",
)

PAGES = [FC, CB, LC, PR, RL]
LOC = {l["name"]: l for l in PAGES}

def place(n):
    return "the Redland" if n == "Redland" else n


def build_location(l):
    path = loc_url(l["name"])
    n = l["name"]
    p = place(n)
    zs = [z.strip() for z in l["zips"].split(",")]
    crumbs = [("Home", "/"), ("Service Areas", "/service-areas"), (n, None)]
    b = [
        hero(l["h1"], l["lead"], l["points"], l["hero_img"], l["hero_alt"], crumbs=crumbs, eyebrow=f"{n}, FL {l['zips']}", area=p),
        trust(),
        seo.location_qa(p, ("ZIP code " if len(zs) == 1 else "ZIP codes ") + zips.zip_list(zs)),
        split(l["intro_h2"], l["intro_html"], l["intro_img"], l["intro_alt"], badge=l["badge"], eyebrow=f"Serving {p[0].upper() + p[1:]}"),
        service_cards(f"Junk Removal Services in {p}", f"Every service below is available in {p} for homes, rentals and businesses.", alt_bg=True,
                      place=p, zip_text=("ZIP code " if len(zs) == 1 else "ZIP codes ") + zips.zip_list(zs)),
        prose(l["body_html"]),
        pricing(l["price_h2"], l["price_intro"], PRICE_HEADERS, PRICE_ROWS,
                "Typical price ranges. Very heavy loads such as concrete, dirt or roofing may be priced by weight. "
                f"Your final price is confirmed on site before work begins. Prices updated {seo.UPDATED}."),
        split(l["local_h2"], l["local_html"], l["local_img"], l["local_alt"], rev=True, alt_bg=True, eyebrow="Local Know How"),
        zips.location_section(l, p),
        faq(l["faq_h2"], l["faq_p"], l["faqs"]),
        cta(l["cta_h2"], l["cta_p"]),
    ]
    svc = {"name": f"Junk Removal in {n}, FL", "type": "Junk Removal", "min": 95, "max": 650, "catalog": seo.offer_catalog(f"Junk Removal in {p}", SITE + path, PRICE_ROWS),
           "area": [seo.entity(n)] + zips.zip_schema(zs)}
    return path, page(path, l["title"], l["desc"], "\n".join(b), l["faqs"], crumbs, service=svc)
