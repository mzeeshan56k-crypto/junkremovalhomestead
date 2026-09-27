from lib import *

# Standard volume pricing shared by the homepage, hubs and location pages
PRICE_HEADERS = ["Load Size", "What It Usually Holds", "Typical Price Range"]
PRICE_ROWS = [["Single item", "One couch, mattress or appliance", "$95 to $150"],
              ["1/4 truck (about 4 yards)", "Bedroom set or small garage corner", "$180 to $280"],
              ["1/2 truck (about 7.5 yards)", "One car garage or small apartment", "$300 to $425"],
              ["3/4 truck (about 11 yards)", "Two bedroom home cleanout", "$440 to $560"],
              ["Full truck (about 15 yards)", "Whole house or large estate", "$560 to $650"]]

FC = dict(
 slug="florida-city", name="Florida City", zips="33034", map_q="Florida+City,+FL+33034",
 title="Junk Removal Florida City FL | Same Day Junk Pickup",
 desc="Junk removal in Florida City, FL 33034. Same day junk pickup, furniture and appliance hauling, cleanouts and dumpsters. Upfront prices. Call 877-745-9845.",
 h1="Junk Removal in <em>Florida City, FL</em>",
 lead="From motel turnovers on US 1 to backyard cleanups west of Krome Avenue, our crew picks up, loads and hauls junk across Florida City, usually the same day you call. You get an upfront price before we lift a thing.",
 points=["Same day pickup in 33034", "Upfront, volume based pricing", "Homes, rentals and businesses", "Donation and recycling first"],
 hero_img="junk-hauling-truck-homestead", hero_alt="Junk hauling truck on a job in Florida City, FL",
 intro_h2="Local Junk Hauling for Florida City Homes and Businesses",
 intro_html="<p>Florida City is the last stop on US 1 before the 18 Mile Stretch to Key Largo, and the Florida's Turnpike ends right here. That makes it a busy little city of about 13,000 residents, with single family homes, apartment complexes, farm properties and a long row of hotels, restaurants and shops that serve travelers heading to the Keys and Everglades National Park.</p>"
  "<p>All of that turnover creates junk. Tenants move out and leave furniture behind, hotels replace mattresses and TVs, and growers west of town clear out old equipment and shade house frames. Our crews are based just up the road in Homestead, so Florida City is part of our core service area with no extra travel fee.</p>"
  "<p>Whether you need one old recliner gone or a full <strong>junk removal in Florida City</strong> for a rental that needs to be listed this week, two uniformed movers do all the lifting, loading and sweeping.</p>",
 intro_img="commercial-debris-dumpster-homestead", intro_alt="Commercial junk and debris loaded for removal in Florida City",
 badge="<b>0 travel fee</b>anywhere in Florida City",
 body_html="<h2>What We Haul Away in Florida City</h2>"
  "<p>If two people can safely carry it, we can usually take it. Popular Florida City pickups include:</p>"
  + checks(["Couches, beds and dressers", "Mattresses and box springs", "Refrigerators and washers", "TVs and electronics",
            "Motel and rental furniture", "Office and retail fixtures", "Old sheds and playsets", "Palm fronds and yard waste"])
  + "<p>For single bulky pieces, see our <a href=\"/service/furniture-removal\">furniture removal</a> and <a href=\"/service/appliance-removal\">appliance removal</a> services. We cannot haul paint, fuel, pool chemicals, propane tanks, asbestos or medical waste.</p>"
  "<h2>Why Florida City Residents Call a Junk Removal Company</h2>"
  "<p>Florida City is its own municipality, so its trash and bulk pickup schedule is not the same as the City of Homestead or unincorporated Miami-Dade. Bulk collection also has limits on what goes to the curb and how much. Construction debris, tires, concrete and large piles often do not qualify, and you still have to drag everything to the street yourself in the South Florida heat.</p>"
  "<p>A private <strong>junk pickup service in Florida City</strong> skips the waiting and the heavy lifting. We carry items from inside the home, garage or unit, haul them away the same day and pay the disposal fees. Landlords and property managers use us between tenants so units can be cleaned, painted and rented without a pile of old furniture sitting in the parking lot.</p>"
  "<h2>Commercial Junk Removal Along US 1 and Palm Drive</h2>"
  "<p>Hotels, restaurants, shops and offices along US 1 and Palm Drive rely on us for <a href=\"/service/commercial-junk-removal\">commercial junk removal</a>: mattress and case goods swaps, kitchen equipment, display fixtures, pallets and cardboard. We schedule early mornings or after closing so guests and customers never see the work, and we can return on a recurring schedule for businesses that generate junk every month.</p>",
 price_h2="Junk Removal Cost in Florida City, FL",
 price_intro="Florida City pricing is the same as Homestead. You pay for the space your items take up in our 15 cubic yard truck, with labor, travel and disposal included.",
 local_h2="Farm, Grove and Storm Cleanup West of Florida City",
 local_html="<p>West of Krome Avenue, Florida City blends into working farmland, nurseries and packing houses. We clear out broken irrigation parts, old shade cloth and frames, worn out farm furniture, tires and the odd abandoned trailer, and we bring a second truck when a property needs a big one day cleanup.</p>"
  "<p>Florida City took the full force of Hurricane Andrew in 1992, and every hurricane season since has been a reminder to stay ready. When a storm passes, we add crews for <a href=\"/service/hurricane-debris-removal\">hurricane debris removal</a> and <a href=\"/service/yard-waste-removal\">yard waste removal</a>, hauling downed limbs, fencing and water damaged contents so you are not waiting weeks for county collection.</p>",
 local_img="furniture-junk-pickup-homestead", local_alt="Old furniture picked up from a home in Florida City, FL",
 nearby=["Homestead", "Leisure City", "Redland", "Princeton"],
 faq_h2="Florida City Junk Removal FAQs",
 faq_p="Answers to the questions Florida City customers ask most before booking.",
 faqs=[
  ("How much does junk removal cost in Florida City?", "Most Florida City jobs cost between $95 for a single item and about $650 for a full 15 cubic yard truckload. A quarter truck, which fits a bedroom set or a small garage corner, usually runs $180 to $280. We confirm the exact price on site before we start."),
  ("Do you offer same day junk pickup in Florida City, FL 33034?", "Yes. Calls before noon usually get same day service in Florida City, and afternoon calls are normally handled the next morning. You get a two hour arrival window and a call about 30 minutes before the crew arrives."),
  ("Do you charge a travel fee to Florida City?", "No. Florida City sits inside our core service area just south of Homestead, so travel is included in the price you are quoted."),
  ("Can you clear out a motel room or rental unit?", "Yes. We remove mattresses, beds, dressers, TVs and anything else left behind, from one room or an entire property. Hotels and landlords can book early morning or recurring pickups."),
  ("Will you pick up from farm or nursery properties?", "Yes. We haul old equipment parts, shade house frames, irrigation pipe, tires, pallets and farm debris from properties west of Krome Avenue. Hazardous chemicals and fuel are the exceptions."),
  ("Do you donate items from Florida City pickups?", "Yes. Usable furniture and household goods go to local donation partners in South Miami-Dade, metal goes to scrap recyclers, and cardboard is recycled. Only what is left goes to a licensed disposal facility."),
 ],
 cta_h2="Need Junk Gone in Florida City Today?",
 cta_p="Call for a free, no obligation price. Same day junk removal is available across Florida City and the rest of South Dade.",
)

CB = dict(
 slug="cutler-bay", name="Cutler Bay", zips="33157, 33189, 33190", map_q="Cutler+Bay,+FL",
 title="Junk Removal Cutler Bay FL | Furniture and Junk Pickup",
 desc="Junk removal in Cutler Bay, FL. Same day furniture, appliance and junk pickup, garage and estate cleanouts with upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in <em>Cutler Bay, FL</em>",
 lead="Remodeling in Saga Bay, cleaning out a parent's home in Lakes by the Bay or just done with the clutter? Our crew lifts, loads and hauls it away across Cutler Bay with an upfront price and a clean sweep at the end.",
 points=["Same day and next day pickup", "Priced by truck volume", "We carry from any room", "Donate and recycle first"],
 hero_img="estate-cleanout-home-homestead", hero_alt="Home ready for a junk removal cleanout in Cutler Bay, FL",
 intro_h2="Full Service Junk Removal for Cutler Bay Homeowners",
 intro_html="<p>Cutler Bay became a town in 2005 and today is home to about 45,000 people between US 1 and Biscayne Bay. Much of it was built from the 1960s through the 1980s, and many of those homes are now being remodeled, downsized or passed to the next generation. That means kitchens coming out, garages full of decades of storage and whole houses that need to be emptied before a sale.</p>"
  "<p>Our trucks come up from Homestead every day, so <strong>junk removal in Cutler Bay</strong> is routine for us. Each truck holds about 15 cubic yards, roughly six pickup beds, and most household jobs are finished in one trip. Two movers handle everything from the back bedroom to the backyard shed, and you never have to haul a sofa to the swale.</p>"
  "<p>We work in Saga Bay, Lakes by the Bay, Cutler Ridge, Bel Aire and the neighborhoods off Old Cutler Road, Caribbean Boulevard and SW 216th Street.</p>",
 intro_img="garage-junk-pickup-carport-homestead", intro_alt="Garage junk pickup from a carport in Cutler Bay",
 badge="<b>15 yd</b>trucks clear most homes in one trip",
 body_html="<h2>Junk We Remove Across Cutler Bay</h2>"
  "<p>We take almost everything that is not hazardous, including:</p>"
  + checks(["Sofas, sectionals and recliners", "Mattresses and bed frames", "Old kitchen cabinets and counters", "Refrigerators, washers and dryers",
            "Garage and attic clutter", "Patio sets and grills", "Exercise equipment", "Hot tubs and playsets"])
  + "<p>Bigger projects often combine services: a <a href=\"/service/garage-cleanout\">garage cleanout</a> with <a href=\"/service/appliance-removal\">appliance removal</a>, or a remodel that needs <a href=\"/service/construction-debris-removal\">construction debris removal</a> once the demo crew is done.</p>"
  "<h2>Why Hire Junk Haulers Instead of Waiting for Bulky Pickup</h2>"
  "<p>Most Cutler Bay homes are covered by Miami-Dade County waste collection, which includes two bulky waste pickups per year of up to 25 cubic yards each. The county will not take single items over 150 pounds, construction debris, tires or anything left in the swale more than 3 days before your appointment, and you still have to carry it all out yourself.</p>"
  "<p>With a private <strong>junk pickup service in Cutler Bay</strong>, the crew removes items from inside the house, loads the truck on the spot and leaves nothing on the lawn for neighbors or code enforcement to notice. For families on a closing date or landlords between tenants, same day removal is often worth far more than waiting weeks for a free slot.</p>"
  "<h2>Estate Cleanouts and Downsizing in Cutler Bay</h2>"
  "<p>Many Cutler Bay homes have been in the same family for decades. When it is time to sell, our <a href=\"/service/estate-cleanout\">estate cleanout</a> team works room by room, sets aside keepsakes and paperwork for you, donates what is usable and hauls the rest. Realtors and executors can hand us a key and get photos when the home is empty and swept.</p>",
 price_h2="Junk Removal Prices in Cutler Bay, FL",
 price_intro="You pay only for the space your items fill in the truck. Labor, loading, travel to Cutler Bay and disposal fees are included in every price.",
 local_h2="Storm Ready Junk Removal Near Biscayne Bay",
 local_html="<p>Cutler Bay sits right on Biscayne Bay, and Hurricane Andrew brought one of the worst storm surges in the area's history in 1992. Low lying streets near the bay still see flooding in heavy summer storms. When water gets in, soaked carpet, drywall and furniture need to come out fast before mold sets in, and our crews prioritize those calls.</p>"
  "<p>After storms we also run <a href=\"/service/hurricane-debris-removal\">hurricane debris removal</a> for fallen limbs, broken fencing and damaged sheds, and <a href=\"/service/yard-waste-removal\">yard waste removal</a> for the palm fronds and branches that pile up every season.</p>",
 local_img="storm-debris-lumber-pile-homestead", local_alt="Storm debris and lumber pile removed in Cutler Bay",
 nearby=["Princeton", "Homestead", "Leisure City", "Florida City"],
 faq_h2="Cutler Bay Junk Removal FAQs",
 faq_p="What Cutler Bay homeowners ask most about junk pickup, pricing and timing.",
 faqs=[
  ("How much does junk removal cost in Cutler Bay?", "Most Cutler Bay jobs cost between $95 for one bulky item and about $650 for a full 15 cubic yard truck. A half truck, which usually covers a one car garage, runs $300 to $425. The final price is confirmed on site before any work starts."),
  ("Do you serve all of Cutler Bay?", "Yes. We cover ZIP codes 33157, 33189 and 33190, including Saga Bay, Lakes by the Bay, Cutler Ridge and the neighborhoods along Old Cutler Road and Caribbean Boulevard."),
  ("Can I get same day junk removal in Cutler Bay?", "Usually, yes. Call before noon and we can often arrive the same day. Otherwise we schedule a two hour window the next day and call about 30 minutes before the crew arrives."),
  ("Do you remove water damaged carpet and drywall after flooding?", "Yes. We remove soaked carpet, padding, drywall, cabinets and furniture after floods and storms, and we can move quickly so drying and repairs can start."),
  ("Why not just use the county bulky waste pickup?", "County bulky pickup is limited to two appointments per year, refuses single items over 150 pounds and construction debris, and requires you to move everything to the swale. We carry items from inside and haul them the same day."),
  ("Do you handle estate cleanouts for realtors and executors?", "Yes. We empty whole homes, set aside documents and keepsakes, donate usable items and leave the home broom clean. You do not need to be on site if a realtor or property manager provides access."),
 ],
 cta_h2="Ready for Junk Removal in Cutler Bay?",
 cta_p="Call now for a free, upfront quote. Same day junk pickup is available across Cutler Bay and South Miami-Dade.",
)

LC = dict(
 slug="leisure-city", name="Leisure City", zips="33033", map_q="Leisure+City,+FL+33033",
 title="Junk Removal Leisure City FL | Same Day Hauling",
 desc="Junk removal in Leisure City, FL 33033. Same day junk hauling for furniture, appliances, yard waste and cleanouts. Upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in <em>Leisure City, FL</em>",
 lead="Old furniture in the carport, a broken fridge on the patio or a rental that needs clearing? Our crew handles junk hauling across Leisure City, often the same day, and you get a firm price before we start.",
 points=["Same day pickup in 33033", "No need to drag junk to the curb", "Upfront volume pricing", "Homes, rentals and yards"],
 hero_img="dumpster-delivery-driveway-homestead", hero_alt="Junk removal and dumpster delivery on a Leisure City driveway",
 intro_h2="Your Neighborhood Junk Removal Crew in Leisure City",
 intro_html="<p>Leisure City sits just north of Homestead, and our trucks pass through it on almost every run. It is an unincorporated community of more than 22,000 people, with many block homes that date back to the 1950s through the 1970s alongside newer infill houses, duplexes and apartment complexes.</p>"
  "<p>Older homes and busy households mean full carports, crowded sheds and backyards that collect broken furniture and appliances. Our <strong>junk removal service in Leisure City</strong> clears all of it. Two movers carry everything out, load a 15 cubic yard truck and sweep up, so the only thing you do is point.</p>"
  "<p>Because we are only minutes away, Leisure City customers get the same fast scheduling and pricing as Homestead, with no travel charge.</p>",
 intro_img="junk-removal-truck-homestead-fl", intro_alt="Junk removal truck parked at a Leisure City home",
 badge="<b>Minutes away</b>from every Leisure City street",
 body_html="<h2>What We Pick Up in Leisure City</h2>"
  "<p>Common Leisure City junk removal jobs include:</p>"
  + checks(["Carport and patio clutter", "Couches, mattresses and beds", "Old refrigerators and freezers", "Washers, dryers and water heaters",
            "Broken sheds and fencing", "Tires and car parts", "Yard waste and tree limbs", "Move out and tenant leftovers"])
  + "<p>Need more room to work? Pair a pickup with a <a href=\"/service/garage-cleanout\">garage cleanout</a>, or rent a <a href=\"/service/dumpster-rental\">dumpster</a> for a remodel that will take a few weeks.</p>"
  "<h2>County Bulky Pickup Rules in Leisure City</h2>"
  "<p>Leisure City is unincorporated, so trash service comes from Miami-Dade County rather than the City of Homestead. The county allows two bulky waste pickups per year, up to 25 cubic yards each, and will not collect single items over 150 pounds, construction debris or tires. Piles can only go out 3 days before the appointment, and anything placed early can bring a code citation.</p>"
  "<p>When your two pickups are used up, when you have heavy items like a fridge or a hot tub, or when you simply cannot wait weeks, a <strong>junk pickup service in Leisure City</strong> is the easy fix. We take items straight from wherever they sit and handle disposal and recycling for you.</p>"
  "<h2>Rental Turnovers and Move Outs</h2>"
  "<p>Leisure City has a lot of rental homes and duplexes, and with families moving in and out near Homestead Air Reserve Base, tenant turnovers happen year round. Landlords and property managers call us to remove everything left behind in one visit so the unit can be cleaned and rented the same week. We can work from photos and a lockbox code, then send pictures when the job is done.</p>",
 price_h2="Junk Removal Cost in Leisure City, FL",
 price_intro="Leisure City prices match our Homestead rates. You pay for the truck space your items use, with labor, travel and disposal included.",
 local_h2="Backyard and Yard Waste Cleanup in Leisure City",
 local_html="<p>Leisure City lots often have mature mango, avocado and palm trees, and they drop a steady stream of fronds, branches and fruit. After a trim, or after a summer storm, we bag and haul the whole pile through our <a href=\"/service/yard-waste-removal\">yard waste removal</a> service so it is not sitting on the swale for weeks.</p>"
  "<p>We also tear down and remove rotted wood sheds, old chain link, playsets and above ground pools, and we can handle <a href=\"/service/hurricane-debris-removal\">hurricane debris removal</a> when a storm brings down limbs and fencing across the neighborhood.</p>",
 local_img="garage-cleanout-before-after-homestead", local_alt="Garage cleanout before and after in Leisure City, FL",
 nearby=["Homestead", "Princeton", "Florida City", "Redland"],
 faq_h2="Leisure City Junk Removal FAQs",
 faq_p="Quick answers for Leisure City homeowners, renters and landlords.",
 faqs=[
  ("How much does junk removal cost in Leisure City?", "Most Leisure City jobs cost between $95 for a single item and about $650 for a full 15 cubic yard truck. A quarter truck, about a bedroom set, runs $180 to $280. We confirm the exact price on site before loading."),
  ("Can you pick up junk the same day in Leisure City, FL 33033?", "Yes. Leisure City is minutes from our Homestead base, so calls before noon usually get same day pickup. Later calls are normally scheduled for the next morning."),
  ("I already used my two county bulky pickups. Can you help?", "Yes. We are not limited by the county schedule. We haul any amount, including items over 150 pounds, construction debris and tires that county bulky pickup refuses."),
  ("Do I have to bring the junk to the curb?", "No. We pick up from carports, backyards, sheds and inside the home. Keeping items off the swale also avoids county rules about placing piles more than 3 days before a pickup."),
  ("Do you tear down old sheds?", "Yes. We take apart and remove wood and metal sheds, playsets, fencing and above ground pools, then haul all of the debris away."),
  ("Do you work with landlords and property managers?", "Yes. We handle tenant move outs and evictions with photo updates, lockbox access and invoices for your records, so you do not need to meet us on site."),
 ],
 cta_h2="Clear Out Your Leisure City Home Today",
 cta_p="Call for a free, upfront price. Same day junk removal is available across Leisure City and all of South Dade.",
)

PR = dict(
 slug="princeton", name="Princeton", zips="33032", map_q="Princeton,+FL+33032",
 title="Junk Removal Princeton FL | Junk Pickup and Cleanouts",
 desc="Junk removal in Princeton, FL 33032. Same day junk pickup, move in and move out cleanouts, construction debris and garage cleanouts. Call 877-745-9845.",
 h1="Junk Removal in <em>Princeton, FL</em>",
 lead="New home boxes, builder leftovers or a garage that filled up faster than expected? Our crew clears it out across Princeton with same day service and an upfront price before we lift anything.",
 points=["Same day pickup in 33032", "HOA friendly, nothing left out", "Upfront volume pricing", "Move in and move out help"],
 hero_img="construction-dumpster-homestead-fl", hero_alt="Construction debris ready for removal at a new home in Princeton, FL",
 intro_h2="Junk Removal for One of South Dade's Fastest Growing Communities",
 intro_html="<p>Princeton has been one of the fastest growing communities in South Miami-Dade over the past decade. Farmland between US 1 and Krome Avenue has turned into new subdivisions, townhomes and apartments, especially along SW 248th Street (Coconut Palm Drive) and the streets around it.</p>"
  "<p>Growth means a steady stream of junk: moving boxes and packing foam, furniture that did not fit the new floor plan, builder leftovers from upgrades, and older homes nearby being remodeled. Our <strong>junk removal service in Princeton</strong> handles all of it. Two movers lift and load, and a 15 cubic yard truck clears most jobs in one trip.</p>"
  "<p>Princeton is a short drive from our Homestead base, so same day scheduling and our standard pricing apply with no travel fee.</p>",
 intro_img="roll-off-dumpster-rental-homestead", intro_alt="Roll off dumpster for a remodel project in Princeton, FL",
 badge="<b>1 trip</b>clears most move in messes",
 body_html="<h2>What We Haul Away in Princeton</h2>"
  "<p>Some of the most common Princeton pickups:</p>"
  + checks(["Moving boxes and packing material", "Old furniture and mattresses", "Appliances replaced in upgrades", "Builder scraps and trim",
            "Garage and closet clutter", "Patio furniture and grills", "Exercise equipment", "Kids' playsets and trampolines"])
  + "<p>Doing upgrades after closing? Our <a href=\"/service/construction-debris-removal\">construction debris removal</a> clears drywall, tile, flooring and cabinets. For longer projects, a <a href=\"/service/dumpster-rental\">driveway dumpster</a> lets you load at your own pace.</p>"
  "<h2>HOA Friendly Junk Pickup</h2>"
  "<p>Many Princeton subdivisions have homeowners associations with rules about piles, trailers and bulk items sitting out front. Princeton is also unincorporated, so county bulky collection applies: two pickups per year, nothing over 150 pounds and nothing placed out more than 3 days early. That leaves a lot of junk with nowhere to go.</p>"
  "<p>We avoid the problem entirely. Our crew picks up straight from the garage, patio or inside the home, loads the truck on the spot and leaves nothing on the curb for the HOA to flag. If you need a pickup on a specific day for an inspection or walk through, we will schedule around it.</p>"
  "<h2>Move In and Move Out Cleanouts</h2>"
  "<p>New homeowners call us after the movers leave to clear boxes and the furniture that did not make the cut. Sellers and renters call us before they leave to empty garages, sheds and closets. Either way, one visit takes care of it, and usable items go to local donation partners instead of the landfill.</p>",
 price_h2="Junk Removal Prices in Princeton, FL",
 price_intro="Prices are based on truck volume, with labor, loading, travel and disposal included. The final price is always confirmed on site before we start.",
 local_h2="Garage and Remodel Cleanups Across Princeton",
 local_html="<p>Newer Princeton homes often have compact garages that fill quickly with overflow furniture, tools and boxes. Our <a href=\"/service/garage-cleanout\">garage cleanout</a> service sorts what you keep, hauls the rest and sweeps the floor so you can park inside again, which matters in South Florida summers.</p>"
  "<p>For contractors and homeowners doing larger remodels, we remove tear out debris between phases so the site stays clean for inspections, and we can come back on a schedule as the project moves forward.</p>",
 local_img="dumpster-trailer-loaded-homestead", local_alt="Loaded junk trailer after a cleanout in Princeton, FL",
 nearby=["Leisure City", "Homestead", "Cutler Bay", "Redland"],
 faq_h2="Princeton Junk Removal FAQs",
 faq_p="Common questions from Princeton homeowners, renters and builders.",
 faqs=[
  ("How much does junk removal cost in Princeton, FL?", "Most Princeton jobs cost $95 for a single item up to about $650 for a full 15 cubic yard truckload. Moving box and packing pickups often fit in a quarter truck for $180 to $280."),
  ("Do you pick up moving boxes and packing material?", "Yes. We haul flattened or loose boxes, foam, plastic wrap and packing paper, and cardboard is recycled whenever possible."),
  ("Will my HOA have a problem with the pickup?", "No. We load directly from the garage, patio or inside the home, so nothing sits on the curb or lawn. The crew is usually in and out in under an hour for typical jobs."),
  ("Can you remove builder leftovers and remodel debris?", "Yes. We remove drywall, tile, flooring, trim, cabinets and packaging from upgrades and remodels. Very heavy materials such as concrete or tile in bulk may be priced by weight."),
  ("Is same day junk removal available in Princeton?", "Yes. Call before noon for the best chance of same day service. You will get a two hour arrival window and a call about 30 minutes before we arrive."),
  ("What ZIP codes do you cover around Princeton?", "We cover 33032 and the surrounding areas, including Naranja, Modello, Leisure City and Goulds, all with no added travel fee."),
 ],
 cta_h2="Get Your Princeton Junk Hauled Today",
 cta_p="Call now for a free, upfront quote. Same day junk pickup is available across Princeton and South Miami-Dade.",
)

RL = dict(
 slug="redland", name="Redland", zips="33031, 33170, 33187", map_q="Redland,+FL",
 title="Junk Removal Redland FL | Farm, Yard and Home Cleanouts",
 desc="Junk removal in the Redland, FL. Farm and grove cleanups, yard waste, sheds, appliances and property cleanouts with upfront pricing. Call 877-745-9845.",
 h1="Junk Removal in the <em>Redland, FL</em>",
 lead="Big lots, long driveways and years of stored equipment? Our crew clears homes, barns, groves and nurseries across the Redland with upfront pricing and trucks that handle rural properties with ease.",
 points=["Acreage and farm cleanouts", "Sheds, trailers and equipment", "Yard waste and storm debris", "Upfront volume pricing"],
 hero_img="yard-waste-removal-before-after-homestead", hero_alt="Yard waste and brush removed from a Redland property",
 intro_h2="Rural Junk Removal Built for Redland Properties",
 intro_html="<p>The Redland is the agricultural heart of South Miami-Dade, stretching west and north of Homestead with tropical fruit groves, plant nurseries, horse properties and homes on large lots along Krome Avenue and the roads around it. Properties here collect a different kind of junk than a city lot: old farm equipment, rusted sheds, shade house frames, irrigation pipe, tires and decades of stored belongings.</p>"
  "<p>Our <strong>junk removal service in the Redland</strong> is set up for that. We bring two strong movers, a 15 cubic yard truck and the tools to take apart sheds and structures, and we are comfortable on gravel drives and grass lanes. If the job needs more than one load, we plan multiple trips or a second truck so the work finishes in one day.</p>",
 intro_img="storm-debris-lumber-pile-homestead", intro_alt="Lumber and debris pile cleared from a Redland farm",
 badge="<b>Big lots</b>and big cleanouts welcome",
 body_html="<h2>What We Remove From Redland Homes and Farms</h2>"
  "<p>Typical Redland pickups include:</p>"
  + checks(["Old sheds and barn contents", "Shade house frames and cloth", "Irrigation pipe and fittings", "Tires and equipment parts",
            "Old trailers and camper junk", "Fencing and gates", "Tree limbs and brush piles", "Household furniture and appliances"])
  + "<p>For big brush piles, see our <a href=\"/service/yard-waste-removal\">yard waste removal</a> service. For a remodel or an extended cleanup, a <a href=\"/service/dumpster-rental\">roll off dumpster</a> can sit on site while you work.</p>"
  "<h2>Why Redland Owners Hire a Junk Hauling Company</h2>"
  "<p>The Redland is unincorporated, so county bulky collection applies: two pickups per year of up to 25 cubic yards, no single item over 150 pounds and no construction debris or tires. On a large property that barely scratches the surface, and loading a borrowed trailer for trips to the Moody Drive center means many hot hours of work.</p>"
  "<p>We handle the lifting, loading and disposal, and we sort metal for scrap, usable items for donation and green waste for mulch where possible. You get one price upfront and one visit that clears the whole list.</p>"
  "<h2>Estate and Property Cleanouts on Acreage</h2>"
  "<p>When a Redland property is sold or passed down, there is often a house, a barn and several outbuildings to empty. Our <a href=\"/service/estate-cleanout\">estate cleanout</a> team works through each building, sets aside anything the family wants to keep and leaves every structure clean for buyers, surveyors and appraisers.</p>",
 price_h2="Junk Removal Cost in the Redland",
 price_intro="Redland prices use the same volume rates as Homestead. Very heavy materials such as concrete, rock or scrap metal in bulk may be priced by weight.",
 local_h2="Storm and Grove Cleanup in the Redland",
 local_html="<p>Open groves and tall trees take a beating in tropical storms and hurricanes, and the Redland saw heavy damage from Andrew in 1992 and again from Irma in 2017. After a storm we run <a href=\"/service/hurricane-debris-removal\">hurricane debris removal</a> for downed limbs, twisted shade structures, broken fencing and damaged sheds.</p>"
  "<p>We also help growers and nurseries clear out dead trees after a freeze or a disease outbreak, old pots and trays, and worn out equipment, working around your harvest and shipping schedule.</p>",
 local_img="dumpster-trailer-loaded-homestead", local_alt="Trailer loaded with junk from a Redland property cleanout",
 nearby=["Homestead", "Florida City", "Princeton", "Leisure City"],
 faq_h2="Redland Junk Removal FAQs",
 faq_p="What Redland homeowners, growers and nurseries ask most.",
 faqs=[
  ("How much does junk removal cost in the Redland?", "Most Redland jobs cost between $95 for one item and about $650 per full 15 cubic yard truckload. Large farm cleanouts often need multiple loads, and we quote the full job upfront."),
  ("Do you remove old sheds, trailers and farm equipment?", "Yes. We take apart and remove sheds, shade structures, fencing and junk trailers, and we haul equipment parts, tires and irrigation pipe. Fuel, oil and chemicals must be drained or removed first."),
  ("Can your truck get down long or gravel driveways?", "Yes. Our trucks regularly work on rural Redland properties with gravel drives and grass lanes. Let us know about low branches or soft ground when you call and we will plan for it."),
  ("Do you recycle metal and green waste?", "Yes. Scrap metal goes to recyclers, usable items go to donation partners and clean yard waste is taken for mulching where possible, so less goes to the landfill."),
  ("What areas of the Redland do you cover?", "We cover the Redland in ZIP codes 33031, 33170 and 33187, plus nearby Homestead, Florida City, Princeton and Goulds, with no added travel fee inside our service area."),
  ("Can you handle a whole property cleanout in one day?", "Most can be done in a day. For very large properties we send a second truck or plan back to back loads so the house, barn and outbuildings are cleared together."),
 ],
 cta_h2="Clear Your Redland Property Today",
 cta_p="Call for a free, upfront quote on your home, grove or nursery cleanout.",
)

PAGES = [FC, CB, LC, PR, RL]
LOC = {l["name"]: l for l in PAGES}

STEPS = lambda city: [
    ("Call for a Price", f"Call {PHONE} and tell us what needs to go in {city}.", "phone"),
    ("Pick a Time", "Choose same day or a scheduled two hour arrival window.", "calendar"),
    ("We Lift and Load", "The crew confirms the price, then removes everything.", "truck"),
    ("Sweep and Sort", "We sweep up, then donate, recycle and dispose responsibly.", "recycle")]

def nearby(l):
    arts = []
    for n in l["nearby"]:
        if n == "Homestead":
            arts.append('<article><h3><a href="/">Junk Removal Homestead</a></h3><p>Our home base, with same day pickup across ZIP codes 33030, 33033 and 33035.</p></article>')
        else:
            o = LOC[n]
            arts.append(f'<article><h3><a href="{loc_url(n)}">Junk Removal {n}</a></h3><p>Same day junk pickup and cleanouts in {n}, FL {o["zips"]}.</p></article>')
    return (f'<section class="section alt"><div class="wrap">{sec_head("Junk Removal Near " + l["name"], "We also serve these nearby South Dade communities with the same crews and pricing.", "Nearby Areas")}'
            f'<div class="related stagger">{"".join(arts)}</div></div></section>')

def build_location(l):
    path = loc_url(l["name"])
    n = l["name"]
    crumbs = [("Home", "/"), ("Service Areas", "/service-areas"), (n, None)]
    b = [
        hero(l["h1"], l["lead"], l["points"], l["hero_img"], l["hero_alt"], crumbs=crumbs, eyebrow=f"{n}, FL {l['zips']}"),
        trust(),
        split(l["intro_h2"], l["intro_html"], l["intro_img"], l["intro_alt"], badge=l["badge"], eyebrow=f"Serving {n}"),
        service_cards(f"Junk Removal Services in {n}", f"Every service we offer in Homestead is available in {n}, for homes, rentals and businesses.", alt_bg=True, include_home=True),
        prose(l["body_html"]),
        steps(f"How Junk Pickup Works in {n}", "Booking takes about two minutes. Here is what to expect from first call to clean floor.", STEPS(n), alt_bg=True),
        pricing(l["price_h2"], l["price_intro"], PRICE_HEADERS, PRICE_ROWS,
                "Typical price ranges. Very heavy loads such as concrete, dirt or roofing may be priced by weight. Your final price is confirmed on site before work begins."),
        split(l["local_h2"], l["local_html"], l["local_img"], l["local_alt"], rev=True, alt_bg=True, eyebrow="Local Know How"),
        nearby(l),
        areas(f"Areas We Serve Around {n}", f"{n} is part of our core South Miami-Dade service area. Here are the communities and ZIP codes we cover.",
              map_q=l["map_q"], map_title=f"{n}, Florida"),
        faq(l["faq_h2"], l["faq_p"], l["faqs"]),
        cta(l["cta_h2"], l["cta_p"]),
    ]
    svc = {"name": f"Junk Removal in {n}, FL", "type": "Junk Removal", "min": 95, "area": [{"@type": "City", "name": f"{n}, FL"}]}
    return path, page(path, l["title"], l["desc"], "\n".join(b), l["faqs"], crumbs, service=svc)
