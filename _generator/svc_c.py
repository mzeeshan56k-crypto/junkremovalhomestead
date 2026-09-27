from lib import *

EST = dict(
 slug="estate-cleanout", name="Estate Cleanout", schema_name="Estate Cleanout in Homestead, FL", min=300,
 title="Estate Cleanout in Homestead, FL | Whole-House Cleanouts",
 desc="Estate cleanouts in Homestead, FL. Respectful whole-house cleanouts for families, executors and realtors, with sorting and donation. Call 877-745-9845.",
 h1="<em>Estate Cleanout</em> Services in Homestead, FL",
 lead="Clearing a loved one's home is hard enough. Our crew handles the sorting, lifting, donating and hauling with care so families, executors and realtors can move forward on their timeline.",
 points=["Respectful, patient crews", "Sorting and donation included", "Realtor- and probate-ready", "Whole house in 1 to 2 days"],
 hero_img="estate-cleanout-home-homestead", hero_alt="Estate cleanout truck at a Homestead home",
 intro_h2="Compassionate Estate Cleanouts That Homestead Families Trust",
 intro_html="<p>An estate cleanout is more than junk removal. There are photos, papers and keepsakes mixed with decades of everyday belongings, and decisions need to be made carefully. Our team slows down where it matters, sets aside personal documents and valuables we find, and follows your instructions on what to keep, donate or discard.</p>"
  "<p>We work with adult children, executors, probate attorneys and real estate agents across Homestead, Florida City, the Redland and Cutler Bay. A typical three-bedroom home produces 25 to 40 cubic yards of contents, which usually means two to three truckloads over one or two days.</p>",
 intro_img="junk-removal-truck-homestead-fl", intro_alt="Estate cleanout crew truck at a Homestead home",
 badge="<b>1 to 2 days</b>to clear most three-bedroom homes",
 body_html="<h2>What Our Estate Cleanout Service Includes</h2>"
  + checks(["Room-by-room sorting", "Setting aside papers and photos", "Furniture and appliance removal", "Clothing and household donation",
            "Garage, shed and yard cleanup", "Electronics recycling", "Coordination with estate sale companies", "Broom-clean handoff for realtors"])
  + "<h2>Whole-House Cleanouts for Sales and Probate</h2>"
  "<p>When a home is headed to market, time matters. Empty homes photograph better, show better and let inspectors see walls and floors clearly. We coordinate with realtors to meet listing dates. Executors can also get photos and itemized receipts to document the process for probate.</p>"
  "<p>If an estate sale company is handling valuables first, we come in afterward to clear everything that did not sell. That combination often recovers the most value for the estate.</p>"
  "<h2>Hoarding and Heavy Clutter Cleanouts</h2>"
  "<p>Some homes need more than a standard cleanout. We handle hoarding situations with discretion, working at a pace that respects the homeowner or family. Unmarked vehicles can be arranged on request, and our crews treat every home with patience. For single rooms or smaller projects, our standard junk removal service may be all you need.</p>"
  "<h2>A Donation-First Approach</h2>"
  "<p>Furniture, kitchenware, linens and clothing in good condition go to charities and resale partners in South Miami-Dade. Many families find comfort knowing a parent's belongings will help others locally. Metal and electronics are recycled, and only what is left goes to disposal.</p>",
 steps_h2="How an Estate Cleanout Works",
 steps_p="A clear plan from first call to empty house.",
 steps=[("Free Walk-through", "We visit or review photos and give a written estimate.", "home"),
        ("Plan the Sort", "You mark the items to keep. We set aside papers and valuables found.", "list"),
        ("Clear and Donate", "Crews remove contents room by room, donating first.", "truck"),
        ("Broom-Clean Handoff", "The home is swept and ready for cleaners, realtors or buyers.", "broom")],
 price_h2="Estate Cleanout Cost in Homestead",
 price_intro="Estate cleanouts are priced by total volume. Typical Homestead ranges are below.",
 headers=["Home Size", "Typical Volume", "Typical Price"],
 rows=[["Apartment or condo", "10 to 15 cubic yards", "$450 to $650"], ["Two-bedroom home", "15 to 25 cubic yards", "$650 to $1,100"],
       ["Three-bedroom home", "25 to 40 cubic yards", "$1,100 to $1,750"], ["Four-bedroom plus garage", "40 to 60 cubic yards", "$1,750 to $2,600"],
       ["Hoarding cleanouts", "Varies widely", "Quoted after walk-through"]],
 note="Estimates include labor, sorting, donation delivery, hauling and disposal. Final price confirmed after a walk-through or detailed photos.",
 local_h2="Serving Homestead Families and Out-of-Town Heirs",
 local_html="<p>Homestead has a large community of longtime residents. Many have lived in the same home since rebuilding after Hurricane Andrew in 1992. When those homes change hands, heirs often live out of state. We make remote cleanouts easy with lockbox access, video walk-throughs, photo updates and card payment by phone.</p>"
  "<p>We also know the local realtors, estate sale companies and donation centers, which keeps each project moving smoothly.</p>",
 local_img="junk-hauling-truck-homestead", local_alt="Hauling truck at a Homestead estate cleanout",
 related_h2="Services Often Paired With Estate Cleanouts",
 related_p="Helpful services when clearing a whole property in Homestead.",
 related=[("furniture-removal", "Remove large furniture pieces that did not sell at the estate sale."),
          ("garage-cleanout", "Clear the garage, sheds and workshop along with the house."),
          ("dumpster-rental", "Keep a dumpster on site for family members sorting over several days.")],
 areas_h2="Estate Cleanout Service Areas",
 areas_p="Whole house and estate cleanouts across these South Dade communities.",
 faq_h2="Estate Cleanout FAQs",
 faq_p="Answers for families, executors and realtors in Homestead.",
 faqs=[
  ("How much does an estate cleanout cost in Homestead?", "Most estate cleanouts in Homestead cost $650 to $2,600, depending on home size. A typical three-bedroom home with 25 to 40 cubic yards of contents runs about $1,100 to $1,750."),
  ("How long does an estate cleanout take?", "Most three-bedroom homes are cleared in one to two days. Larger homes, hoarding situations or homes with sheds and outbuildings may take longer."),
  ("What happens to valuables or documents you find?", "Any cash, jewelry, photos, documents or items that look personal are set aside for the family. We never discard papers without your approval."),
  ("Do I need to be present for the cleanout?", "No. Many heirs live out of state. We can work from lockbox access and provide video walk-throughs, photo updates and payment by phone."),
  ("Do you work with estate sale companies?", "Yes. We often clear homes after an estate sale, removing everything that did not sell so the house is ready to list."),
  ("Will you donate my parent's belongings?", "Yes. Usable furniture, clothing and household goods go to charities and resale partners in South Miami-Dade. We can provide donation receipts when available."),
  ("Can you provide receipts for probate?", "Yes. We provide itemized invoices and before-and-after photos, which executors often need to document estate expenses."),
  ("Do you handle hoarding cleanouts?", "Yes. We handle hoarding cleanouts with discretion and patience. These are quoted after a walk-through because volume and conditions vary widely."),
  ("Can you clean out a mobile home?", "Yes. We clear mobile and manufactured homes in parks around Homestead and Florida City, and we can quote the removal of attached decks and sheds."),
  ("Do you clean the house after it is emptied?", "We leave the home broom-clean. For deep cleaning, carpet cleaning or repairs, we can recommend trusted local providers."),
 ],
 cta_h2="Let Us Handle the Heavy Lifting",
 cta_p="Respectful, organized estate cleanouts across Homestead. Call for a free walk-through.",
)

COM = dict(
 slug="commercial-junk-removal", name="Commercial Junk Removal", schema_name="Commercial Junk Removal in Homestead, FL", min=150,
 title="Commercial Junk Removal in Homestead, FL | Office Cleanouts",
 desc="Commercial junk removal in Homestead, FL. Office furniture, retail fixtures and property turnovers with after-hours service. Call 877-745-9845.",
 h1="Commercial <em>Junk Removal</em> in Homestead, FL",
 lead="Offices, retail stores, restaurants, warehouses and rental properties across Homestead count on us to clear junk fast, on their schedule, without disrupting business.",
 points=["After-hours and weekend service", "Office and retail cleanouts", "Property manager turnovers", "Invoicing and COI available"],
 hero_img="construction-dumpster-homestead-fl", hero_alt="Commercial debris removal at a Homestead property",
 intro_h2="Business Junk Removal Built Around Your Hours",
 intro_html="<p>Downtime costs money. Our commercial crews work early mornings, evenings and weekends so stores stay open and offices stay productive. From a single conference table to an entire floor of cubicles, we remove it, haul it and leave the space clean.</p>"
  "<p>We serve businesses along Krome Avenue, US 1, Campbell Drive and the commercial corridors near Homestead-Miami Speedway. We also work with property managers who oversee apartment communities in Homestead and Florida City. Recurring service agreements are available for businesses that generate regular bulky waste.</p>",
 intro_img="roll-off-dumpster-rental-homestead", intro_alt="Commercial dumpsters and debris in Homestead, FL",
 badge="<b>7 days</b>a week, including early and late hours",
 body_html="<h2>Commercial Junk Removal Services We Offer</h2>"
  + checks(["Office furniture and cubicles", "Retail fixtures and shelving", "Restaurant equipment", "Warehouse pallets and racking",
            "Apartment turnovers and evictions", "Foreclosure and bank-owned cleanouts", "Electronic waste and IT equipment", "Construction and tenant buildout debris"])
  + "<h2>Office Cleanouts and Furniture Liquidation</h2>"
  "<p>Moving, downsizing or remodeling? We remove desks, chairs, filing cabinets, cubicle systems and break room appliances. Usable office furniture is donated or resold where possible, and electronics go to certified recyclers. See our furniture removal service for smaller office jobs.</p>"
  "<h2>Property Management and Apartment Turnovers</h2>"
  "<p>With a large rental market driven by Homestead Air Reserve Base families, agricultural workers and seasonal residents, property managers face frequent turnovers. We clear tenant leftovers, eviction contents and common-area junk quickly so units can be cleaned and relisted. Many managers keep us on call for recurring pickups across multiple properties.</p>"
  "<h2>Retail, Restaurant and Warehouse Cleanouts</h2>"
  "<p>Store resets, restaurant remodels and warehouse reorganizations create piles of fixtures, pallets and equipment. We haul it all, including commercial refrigerators through our appliance removal service. For buildouts with heavy debris, our construction debris removal crews can work alongside your contractor.</p>",
 steps_h2="How Commercial Junk Removal Works",
 steps_p="Professional, documented service from quote to cleanup.",
 steps=[("Site Review", "Share photos or schedule a walk-through for a written quote.", "list"),
        ("Schedule Around You", "Early, late or weekend time slots to avoid disruption.", "calendar"),
        ("Remove and Haul", "Crews clear items efficiently and protect your space.", "truck"),
        ("Invoice and Report", "Clear invoicing with donation and recycling details.", "shield")],
 price_h2="Commercial Junk Removal Pricing",
 price_intro="Commercial jobs are priced by volume and access. Typical Homestead ranges are below.",
 headers=["Job Type", "Typical Volume", "Typical Price"],
 rows=[["Small office cleanout", "4 to 8 cubic yards", "$250 to $450"], ["Apartment turnover", "5 to 12 cubic yards", "$300 to $560"],
       ["Retail fixture removal", "8 to 15 cubic yards", "$400 to $650"], ["Warehouse or multi-truck job", "Over 15 cubic yards", "Quoted per job"],
       ["Recurring service", "Weekly or monthly", "Custom contract pricing"]],
 note="After-hours service, elevator buildings and heavy equipment may affect pricing. Certificates of insurance can be provided on request.",
 local_h2="A Local Partner for Homestead Businesses",
 local_html="<p>National junk franchises often dispatch from Miami or beyond, adding travel time and cost. Our Homestead focus means faster response times and pricing that reflects local disposal costs. We know the loading docks, the business parks and the traffic patterns on US 1 and Krome Avenue, so jobs start on time.</p>"
  "<p>We also help businesses prepare for hurricane season by clearing loose outdoor items and debris that could become hazards in high winds.</p>",
 local_img="dumpster-delivery-driveway-homestead", local_alt="Dumpster service at a Homestead commercial property",
 related_h2="Related Business Services",
 related_p="Other services Homestead businesses rely on.",
 related=[("dumpster-rental", "Keep a dumpster on site for ongoing projects and resets."),
          ("construction-debris-removal", "Tenant improvement and remodel debris hauled fast."),
          ("hurricane-debris-removal", "Post-storm cleanup for commercial properties and lots.")],
 areas_h2="Commercial Service Areas",
 areas_p="Commercial junk removal across Homestead, Florida City and South Miami-Dade.",
 faq_h2="Commercial Junk Removal FAQs",
 faq_p="Common questions from Homestead business owners and property managers.",
 faqs=[
  ("How much does commercial junk removal cost in Homestead?", "Small office cleanouts typically cost $250 to $450, apartment turnovers $300 to $560, and retail fixture removals $400 to $650. Larger or recurring jobs are quoted individually."),
  ("Do you offer after-hours service?", "Yes. We work early mornings, evenings and weekends so your business can stay open. After-hours scheduling is available 7 days a week."),
  ("Can you provide a certificate of insurance?", "Yes. Certificates of insurance can be provided on request for property managers, landlords and commercial buildings that require them before work begins."),
  ("Do you handle eviction cleanouts?", "Yes. We clear eviction contents for landlords and property managers in Homestead once the legal process is complete and the property is released to the owner."),
  ("Do you recycle office electronics?", "Yes. Computers, monitors, printers and IT equipment go to certified electronics recyclers. We can document drop-offs for your records."),
  ("Can you set up recurring pickups?", "Yes. Businesses and property managers can schedule weekly, biweekly or monthly pickups with contract pricing and simple monthly invoicing."),
  ("How quickly can you respond to a commercial job?", "Most commercial jobs in Homestead can be scheduled within 24 to 48 hours, and urgent same-day service is often available."),
  ("Do you remove restaurant equipment?", "Yes. We remove commercial refrigerators, ovens, fryers, prep tables and shelving. Gas and hardwired equipment must be disconnected by a licensed professional first."),
  ("Do you work in multistory buildings?", "Yes. We work in elevator and walk-up buildings and coordinate with building management for loading dock and elevator reservations."),
  ("Do you serve foreclosures and bank-owned homes?", "Yes. We clear foreclosures and REO properties for banks, investors and asset managers, with photo documentation before and after the cleanout."),
 ],
 cta_h2="Keep Your Business Moving",
 cta_p="Fast, professional commercial junk removal in Homestead. Call for a quote today.",
)

HURR = dict(
 slug="hurricane-debris-removal", name="Hurricane Debris Removal", schema_name="Hurricane and Storm Debris Removal in Homestead, FL", min=150,
 title="Hurricane Debris Removal in Homestead, FL | Storm Cleanup",
 desc="Hurricane and storm debris removal in Homestead, FL. Downed limbs, fencing, wet drywall and ruined contents hauled fast. Call 877-745-9845.",
 h1="<em>Hurricane Debris Removal</em> and Storm Cleanup in Homestead, FL",
 lead="After a hurricane or tropical storm, fast cleanup protects your home and family. We haul downed limbs, broken fencing, water-damaged drywall, flooring and ruined contents across Homestead and South Dade.",
 points=["Rapid post-storm response", "Trees, fencing and roofing", "Flood-damaged contents", "Photos for insurance claims"],
 hero_img="storm-debris-lumber-pile-homestead", hero_alt="Storm debris and lumber pile beside a dumpster in Homestead",
 eyebrow="Homestead, FL Storm Cleanup",
 intro_h2="Storm Cleanup for a City That Knows Hurricanes",
 intro_html="<p>Homestead knows hurricanes better than almost anywhere in the United States. On August 24, 1992, Category 5 Hurricane Andrew made landfall just north of the city. It destroyed or damaged tens of thousands of homes and devastated Homestead Air Force Base. More recent storms like Irma in 2017 left fallen trees and damaged roofs across South Dade.</p>"
  "<p>After a storm, waiting weeks for county debris collection can leave wet materials sitting in your yard, drawing mold, mosquitoes and pests. Our <strong>storm debris removal service</strong> clears it quickly so repairs can start and your property is safe again.</p>",
 intro_img="yard-waste-removal-before-after-homestead", intro_alt="Storm debris cleared from a Homestead yard",
 badge="<b>June 1 to Nov 30</b>Atlantic hurricane season",
 body_html="<h2>Storm Debris We Remove</h2>"
  + checks(["Downed trees and limbs", "Broken fencing and screens", "Damaged roofing and shingles", "Water-damaged drywall and insulation",
            "Soaked carpet and flooring", "Ruined furniture and mattresses", "Spoiled refrigerators", "Damaged sheds and carports",
            "Pool cage and screen enclosure debris", "Outdoor furniture and grills"])
  + "<h2>Flood and Water Damage Cleanouts</h2>"
  "<p>When water gets inside, speed matters. The EPA advises that water-damaged materials be dried or removed within 24 to 48 hours to limit mold growth. We remove wet carpet, padding, drywall, cabinets and furniture so restoration contractors can start drying the structure. Refrigerators with spoiled food are sealed and hauled through our appliance removal service.</p>"
  "<h2>Tree and Yard Storm Cleanup</h2>"
  "<p>Fallen limbs, snapped palms and uprooted trees are the most common storm debris in Homestead. We cut up fallen limbs, load them and haul them away. For trees still standing or leaning on structures, call a licensed tree service first, then we handle the hauling. Routine yard piles are covered by our yard waste removal page.</p>"
  "<h2>Documentation for Insurance Claims</h2>"
  "<p>Insurance adjusters need proof. We take before-and-after photos of the debris we remove and provide detailed invoices that list the materials hauled. Many Homestead homeowners submit these with their claims. We recommend taking your own photos and videos before any cleanup begins.</p>"
  "<h2>Pre-Storm Cleanup</h2>"
  "<p>Loose items become projectiles in hurricane-force winds. Before a forecast storm, we remove old furniture, construction debris and yard piles that could damage your home or a neighbor's. Contractors often book us to clear job sites when a storm enters the forecast cone.</p>",
 steps_h2="How Storm Debris Removal Works",
 steps_p="Fast response focused on safety and documentation.",
 steps=[("Call After the Storm", "Once it is safe, call and send photos of the damage.", "phone"),
        ("Priority Scheduling", "We schedule the fastest available crew for your area.", "calendar"),
        ("Remove and Document", "Debris is hauled with photos taken for your records.", "shield"),
        ("Clean and Ready", "Your property is cleared so repairs and restoration can begin.", "broom")],
 price_h2="Storm Debris Removal Cost in Homestead",
 price_intro="Typical storm cleanup pricing by volume. Demand after major storms can affect scheduling.",
 headers=["Cleanup Type", "Typical Volume", "Typical Price"],
 rows=[["Small limb and debris pile", "2 to 4 cubic yards", "$150 to $280"], ["Fence and yard cleanup", "5 to 8 cubic yards", "$300 to $450"],
       ["Water-damaged room contents", "6 to 10 cubic yards", "$350 to $520"], ["Full truck of mixed storm debris", "15 cubic yards", "$560 to $700"],
       ["Whole home flood cleanout", "Multiple loads", "Quoted per job"]],
 note="Wet materials are heavier than dry debris, so storm loads often price toward the upper range. We never price gouge after storms. Prices confirmed on site.",
 local_h2="Know the County Storm Debris Rules",
 local_html="<p>After declared disasters, Miami-Dade County and the City of Homestead may run special storm debris collection. These programs usually require vegetative debris to be kept separate from construction debris at the curb. Collection can take weeks to reach every street after a major storm.</p>"
  "<p>We work alongside those programs. Many homeowners use us for debris the county will not take, for items inside the home, or simply to get the property cleared faster so repairs can start.</p>",
 local_img="dumpster-delivery-driveway-homestead", local_alt="Debris dumpster in a Homestead driveway after a storm",
 related_h2="Related Storm Cleanup Services",
 related_p="Services Homestead homeowners use during storm recovery.",
 related=[("yard-waste-removal", "Branches, palm fronds and brush cleared after storms."),
          ("construction-debris-removal", "Damaged drywall, roofing and building materials hauled."),
          ("dumpster-rental", "Keep a dumpster on site during longer storm repairs.")],
 areas_h2="Storm Cleanup Service Areas",
 areas_p="Hurricane and storm debris removal across Homestead and South Miami-Dade.",
 faq_h2="Hurricane Debris Removal FAQs",
 faq_p="What Homestead homeowners ask about storm debris cleanup.",
 faqs=[
  ("How much does storm debris removal cost in Homestead?", "Small limb and debris piles typically cost $150 to $280. A full 15-cubic-yard truck of mixed storm debris usually costs $560 to $700. Wet materials weigh more and may price higher."),
  ("How soon after a hurricane can you come?", "We begin scheduling as soon as roads are safe and open. Response times depend on storm severity, but calling early secures a spot on our schedule."),
  ("Should I wait for county storm debris pickup?", "County collection is free but can take weeks after major storms and has strict separation rules. Many homeowners hire us for faster removal or for items the county will not take."),
  ("Do you remove water-damaged drywall and carpet?", "Yes. The EPA recommends removing or drying wet materials within 24 to 48 hours to limit mold. We remove wet drywall, carpet, padding and cabinets quickly."),
  ("Can you help with my insurance claim?", "We provide before-and-after photos and itemized invoices listing debris removed. These records help support insurance claims for debris removal costs."),
  ("Do you cut down damaged trees?", "We cut and haul fallen limbs and trees already on the ground. Standing or leaning trees near structures should be handled by a licensed tree service first."),
  ("Do you remove damaged fencing and screen enclosures?", "Yes. We dismantle and haul damaged wood, vinyl and chain-link fencing, as well as pool cage and screen enclosure debris."),
  ("Do you raise prices after hurricanes?", "No. Our standard volume pricing stays in place after storms. Florida law prohibits price gouging during declared states of emergency."),
  ("Can you clear debris before a storm arrives?", "Yes. Pre-storm pickups remove loose junk, yard piles and construction materials that could become dangerous in high winds."),
  ("When is hurricane season in Homestead?", "Atlantic hurricane season runs from June 1 through November 30, with peak activity from mid-August through early October."),
 ],
 cta_h2="Get Storm Debris Cleared Fast",
 cta_p="Rapid, documented storm cleanup across Homestead. Call as soon as it is safe.",
)

PAGES = [EST, COM, HURR]
