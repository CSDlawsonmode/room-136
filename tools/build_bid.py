import os
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(HERE, "build"))
DOCS = os.path.join(HERE, "..", "docs")
from pdfcommon import *
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak, KeepTogether

def link(url, text): return "<link href='%s' color='#0b6e99'>%s</link>" % (url, text)
BLANK = "&nbsp;"
TITLE = "Room 136 phased bid package | Caldwell High School"

doc = SimpleDocTemplate(os.path.join(DOCS, "Room136_Phased_Bid_Package.pdf"), pagesize=letter,
                        leftMargin=.7 * inch, rightMargin=.7 * inch, topMargin=.6 * inch, bottomMargin=.7 * inch,
                        title="Room 136 Phased Bid Package", author="Chad Lawson")
E = []

# ------------------------------------------------ page 1: overview
E.append(P("Room 136 Media Tech / Esports: Phased Bid Package", H1))
E.append(P("Caldwell High School, 3401 S Indiana Avenue, Caldwell, ID 83605 &nbsp;|&nbsp; Draft prepared November 1, 2026 &nbsp;|&nbsp; Bid no. and due date: to be assigned by district purchasing", S))
E.append(P("Contact: Chad Lawson, Media Technologies and District Esports Coordinator &nbsp;|&nbsp; clawson@caldwellschools.org &nbsp;|&nbsp; 208-455-3304 ext. 2136", S))
E.append(P("Draft for review by the district purchasing office before release. Bidding rules, insurance, bonding and award terms are the district's and will be attached by purchasing.", S))
E.append(Spacer(1, 4))
E.append(P("Purpose", H2))
E.append(P("Caldwell High School is converting Room 136 (called Room 413 in some earlier drawings) into a media tech and esports classroom. We are asking for firm pricing on four phases that can be awarded together or one at a time: building infrastructure, a Philips Hue lighting system with screen sync, a Dolby Atmos sound system, and retractable seating. Please price each phase and each alternate separately, and tell us what you would save by doing phases together."))
E.append(P("What the district already has", H2))
E.append(P("<b>Not part of this bid:</b> the student desks, the student and teacher PCs, and the district network (switches, cabling back to the server room, internet service). Your work connects to these. Network ports, VLAN and addressing are provided by district IT on request, as noted under each phase."))
E.append(P("The four phases", H2))
E.append(table([
    ["Phase", "What it covers", "Why this order", "Depends on"],
    ["<b>1. Infrastructure</b>", "Circuits and outlets, low-voltage pathways, speaker and HDMI wiring, ceiling backing, floor raceway for the desks (Attachment B).", "Opens the walls, ceiling and floor once, so later phases do not have to.", "None. Should go first."],
    ["<b>2. Lighting and screen sync</b>", "Three Hue gradient strips behind the 85 in. TVs, a Hue Play HDMI Sync Box on the main screen, six reactive accent lights, Hue-controlled ceiling lighting in four dimmable zones, a Hue Bridge Pro, wall controls, programming.", "The most visible change for students, and it needs only power and one network port.", "Phase 1 power and network drops."],
    ["<b>3. Dolby Atmos audio</b>", "7.1.4 speaker system (11 speakers plus subwoofer), receiver or processor, amplification, calibration, training.", "Needs the speaker wire and ceiling backing from Phase 1; ties into the sync box from Phase 2.", "Phase 1 pathways. Interlocks with Phase 2 sync box."],
    ["<b>4. Seating</b>", "Retractable bleacher seating on the south wall, plus removing two wall cabinets (Attachment A).", "Longest lead time, and the room works without it.", "Coordinate rear speakers (Phase 3) with the seating."],
], [PW * .17, PW * .40, PW * .26, PW * .17]))
E.append(P("The phase order is our proposal. Phase 1 should come first; phases 2, 3 and 4 can be swapped. Tell us if a different sequence is cheaper or lower-risk.", S))
E.append(P("Room facts", H2))
E.append(table([
    ["Item", "Dimension or condition"],
    ["Main room", "400 in. x 376 in. (33 ft 4 in. x 31 ft 4 in.), about 1,044 sq ft; 10 ft ceiling; level floor with eight existing floor boxes. Ceiling type, slab and what is above the ceiling are to be confirmed on site."],
    ["Southwest alcove", "76 in. x 194 in., open to the room (no wall between the alcove and the desk area on the west side)."],
    ["Server room", "76 in. x 130 in., adjoining the northwest corner. Not part of the room; available for equipment if you recommend it."],
    ["Displays", "Three 85 in. TVs on the north wall, centers 86 in. apart, centered on the room. The center TV is the main screen."],
    ["Doors and window", "Three 36 in. doors (north wall near the east corner, east wall near the south corner, southwest entry). Window on the west side of the north end."],
    ["South wall", "Wall cabinets 46 / 36 / 36 in. wide, 13 in. deep, 58 to 85 in. above the floor; one 36 x 30 in. tall cabinet; countertop 145 in. long."],
], [PW * .20, PW * .80]))
E.append(PageBreak())

# ------------------------------------------------ phase 1
E.append(P("Phase 1: Infrastructure and rough-in", H1))
E.append(P("All work by appropriately licensed contractors, permitted and inspected as the jurisdiction requires. Coordinate with the district electrician and facilities before any penetration.", S))
E.extend(bl([
    "<b>Lighting power.</b> Constant (unswitched) power to every Hue fixture. Smart fixtures must never lose power at a wall switch. Remove or lock out the existing wall switches for the lights being replaced, and say how you will do it.",
    "<b>Screen wall power.</b> A duplex outlet behind each of the three TVs for the gradient strips, and outlets at the north wall center for the sync box and receiver, all concealed.",
    "<b>AV equipment power.</b> Dedicated, surge-protected circuit for the receiver or processor and amplification, wherever you locate it. Tell us the load.",
    "<b>Network drops.</b> Three Ethernet ports near the north wall center: Hue Bridge Pro, Hue Play HDMI Sync Box and the AV receiver. District IT supplies the switch ports, VLAN and addresses. Tell us the traffic and discovery requirements early (the sync box and bridge have to reach each other on the same network).",
    "<b>Speaker and HDMI pathways.</b> Conduit or accessible pathway, with pull strings, from the equipment location to 11 speaker positions and the subwoofer(s) shown in Figure 3, and for HDMI between the receiver, sync box and center TV. Allow for the optional 7.1.6 and second subwoofer.",
    "<b>Ceiling backing.</b> Rigid backing or bridging at the four overhead speaker positions (six if Alternate 3D is taken) and anywhere ceiling lighting is replaced.",
    "<b>Floor raceway.</b> FSR Smart-Way floor raceway per Attachment B: one 280 in. cross-run, a 99 in. spur and six device boxes, fed from the existing floor box at (186, 240). Price this as its own line item.",
    "<b>Firestopping, patching, paint.</b> Every penetration firestopped and closed to the existing finish.",
]))
E.append(P("Phase 1 submittals", H2))
E.extend(bl([
    "Marked-up plan showing every circuit, outlet, drop and pathway, with conduit sizes.",
    "The load you assume for lighting and for AV, so the district electrician can check the panel.",
    "Written confirmation of ceiling construction and any change you recommend for the overhead speakers or fixtures.",
]))

# ------------------------------------------------ integration
E.append(P("How the pieces connect", H2))
E.append(KeepTogether([img("bid_flow.png", PW * .8), P("Figure 1. Proposed signal flow. Sources feed the receiver, the receiver feeds the sync box, and the sync box feeds the center TV, so sound stays decoded by the receiver and the lights follow the picture. Bidders may propose a different order, such as sync box before the receiver, and must say how Atmos and device switching behave. Some user reviews of the sync box report problems with input switching when an AV receiver is in the chain, so we want you to test this chain before handover and list the settings you used.", S)]))

E.append(PageBreak())

# ------------------------------------------------ phase 2
E.append(P("Phase 2: Philips Hue lighting and screen sync", H1))
E.append(P("The goal is a classroom with enough even light for daily teaching, a dimmed media mode that does not wash out the screens, and color that reacts to what is on the main screen.", B))
E.append(KeepTogether([img("bid_lighting.png", PW * .74), P("Figure 2. Lighting concept. Strips glow on the wall behind the three TVs; six accent lights and the strips form one sync group; four zones (A to D) dim separately.", S)]))
E.append(P("Base bid", H2))
E.append(table([
    ["Item", "Requirement"],
    ["<b>TV backlights</b>", "Three Hue Play gradient strips, 85 in. size, one on the back of each TV. Confirm fit with the current wall mounts and standoff depth. Philips' listing says the strip can be cut to size, but some press coverage says it cannot; confirm with the manufacturer before you price."],
    ["<b>Sync box</b>", "One Hue Play HDMI Sync Box 8K on the center (main) screen, with all four inputs available. It syncs only HDMI sources, not the TV's own apps."],
    ["<b>Reactive accent lights</b>", "Six color-capable Hue lights (light bars or strips) at the positions in Figure 2 or better ones you propose. A gradient strip counts as one light toward the sync box's 10-light limit, so three strips and six accent lights is 9 of 10; confirm the limit applies to the current firmware."],
    ["<b>Left and right TVs</b>", "Their strips should follow the center screen's sync. If a single sync box cannot do that, price the second and third box as Alternate 2E and say what each TV would need."],
    ["<b>Bridge</b>", "One Hue Bridge Pro on Ethernet (Philips lists 150+ lights and 50+ accessories). Place it where Zigbee reaches every fixture; say where."],
    ["<b>General lighting</b>", "Hue-controllable, dimmable ceiling fixtures in zones A to D. Design targets: 30 to 50 footcandles at desk height in the Class scene (the range commonly cited for classrooms; your lighting designer should confirm), color rendering of 80 or better, no direct glare on the TVs or student monitors. Our rough lumen check is about 16 panels at roughly 4,000 lumens each in the main room, plus two in the alcove. Your photometric layout governs."],
    ["<b>Scenes</b>", "At least: Class (full light), Media (zone A dark, desk zone dimmed for screens), Esports (low light with color, accent lights live), and Full on / cleaning. One tap on a wall controller for each."],
    ["<b>Wall controls</b>", "Hue wall dimmers or scene controllers at each door, and one at the teacher station. Count them against the bridge's accessory limit."],
    ["<b>Fail-safe</b>", "Say what happens to the lights if the bridge or the district network is down, and give a manual way to get full light in the room."],
    ["<b>Accounts</b>", "Hue accounts, bridge and app access must belong to the district, not to an individual."],
], [PW * .18, PW * .82]))
E.append(P("Safety and code", H2))
E.extend(bl([
    "Existing emergency and egress lighting must stay as it is, on its own circuits, and keep working in a power loss.",
    "Philips Hue is sold as a consumer product line, and we found no education or commercial program. State the warranty terms you can give for classroom use and the listing (UL or ETL) of every fixture.",
    "If you recommend a commercial smart-lighting platform for the general lighting and Hue only for the screen sync and accent lights, price that as an alternate. The sync box can only drive Hue lights.",
]))

# ------------------------------------------------ phase 3
E.append(Spacer(1, 12))
E.append(KeepTogether([P("Phase 3: Dolby Atmos sound system", H1), P("The goal is clear, even sound for a room used for class instruction, media editing and esports watch parties, with true overhead channels and a main screen that stays in sync with the lights.", B), img("bid_audio.png", PW * .74), P("Figure 3. Atmos 7.1.4 concept. L, C and R sit with the TV wall; two side and two rear surrounds; four overheads placed about 45 degrees up from the middle of the desk zone (roughly 6 ft in front of and behind it, from the rule of thumb in Dolby's setup guidance).", S)]))
E.append(P("Base bid", H2))
E.append(table([
    ["Item", "Requirement"],
    ["<b>Layout</b>", "7.1.4: left, center, right, two side surrounds, two rear surrounds, four overhead speakers and at least one subwoofer. Positions in Figure 3 are indicative."],
    ["<b>Electronics</b>", "Receiver or processor with at least 11 amplified channels (or a processor plus amplification), Dolby Atmos decoding, HDMI eARC, automatic room correction, and a network port. Say what it does with the sync box in the signal chain (Figure 1)."],
    ["<b>Speakers</b>", "Overheads in-ceiling. Front and surround speakers on-wall or in-wall depending on wall construction. Center speaker under the center TV. The center has to work with three large TVs, so tell us how you aim and place it."],
    ["<b>Level and safety</b>", "A maximum volume the district can set and lock. Wall or remote volume control."],
    ["<b>Calibration</b>", "Measured room correction with all channels, a written result, and a saved configuration."],
    ["<b>Training and documents</b>", "Two hours of staff training and a one-page operating guide kept in the room."],
], [PW * .18, PW * .82]))
E.append(P("Alternates to price", H2))
E.extend(bl([
    "<b>3D.</b> 7.1.6: add two middle overhead speakers (dashed in Figure 3).",
    "<b>3E.</b> A second subwoofer on the east wall.",
    "<b>3F.</b> Acoustic treatment, if you think the room needs it, with your reasoning.",
]))
E.append(P("Design questions for your response", H2))
E.extend(bl([
    "The room holds more listeners than a home theater sweet spot, with several desk layouts. What do you change from a standard 7.1.4 to cover everyone (speaker choice, more overheads, delay and level)?",
    "The west side next to the desk zone is an open alcove, so there is no wall for the left side surround. Figure 3 shows it on the alcove wall, which is farther away than the right side. Propose a balanced solution.",
    "The rear surrounds sit over the south-wall cabinets and the bleachers (Phase 4). Confirm mounting height and clearance above the top row.",
    "Where do you recommend the electronics (the server room, the tall cabinet, or elsewhere), and what HDMI cable type and length does that need?",
]))

# ------------------------------------------------ phase 4
E.append(Spacer(1, 12))
E.append(P("Phase 4: Retractable seating", H1))
E.append(P("Pricing for the south-wall bleachers, based on our earlier inquiry (Attachment A, which still calls the room 413).", B))
E.extend(bl([
    "<b>Option 4A:</b> three 72 in. bays, three rows at 30 in. spacing (about 90 in. deep).",
    "<b>Option 4B:</b> the same bays, four rows (about 120 in. deep).",
    "<b>Cabinet work, 4C:</b> remove the two 36 in. wall cabinets at x = 78 to 150 in. and the countertop section from x = 92 in., and patch the wall. The 46 in. cabinet and the tall cabinet stay.",
    "Tell us stowed depth, wall backing needed, guardrail and access requirements and the standard you meet, and operating effort.",
    "Coordinate with Phase 3: rear surround positions and overhead speaker TRL and TRR sit above the seating zone.",
]))

# ------------------------------------------------ all phases
E.append(P("Requirements for every phase", H2))
E.extend(bl([
    "Prices are firm for 90 days. The district is expected to be tax-exempt; purchasing will confirm.",
    "Each phase is priced so it can be awarded alone. Show any discount for combining phases.",
    "Work happens outside class hours or during breaks. Give your proposed schedule and the days the room is out of use. Contractor staff must meet district requirements for badging and background checks; district purchasing will supply them.",
    "Product substitutions are welcome when they meet or beat the requirements. List the model numbers you propose and why.",
    "Submit with your bid: product data sheets, one marked-up plan per phase, manufacturer and labor warranty terms, lead times, and three references from school or public projects.",
    "At handover: as-built drawings, exported device configuration (receiver, bridge, sync box), district-owned account access, the operating guide, and staff training.",
]))
E.append(P("Questions about this bid", H2))
E.append(P("Send written questions to Chad Lawson (contact at the top). Answers will go to every bidder. Site visits are by appointment; we recommend one before you price, to confirm the ceiling, the south wall and the west alcove."))
E.append(PageBreak())

# ------------------------------------------------ price sheet
E.append(P("Bid price sheet", H1))
E.append(P("Bidder: ______________________________ &nbsp;&nbsp; Idaho contractor license no.: ______________ &nbsp;&nbsp; Date: ____________", B))
E.append(P("Write a price for every line. Write \"NB\" for no bid. Include equipment, labor, permits and delivery.", S))
rows = [["Line", "Description", "Price ($)", "Lead time"]]
secs = []
def sec(t):
    secs.append(len(rows)); rows.append(["<b>%s</b>" % t, "", "", ""])
def line(a, b): rows.append([a, b, BLANK, BLANK])
sec("PHASE 1: INFRASTRUCTURE")
line("1A", "Circuits and outlets (lighting, screen wall, AV)")
line("1B", "Network drops, speaker and HDMI pathways and wiring")
line("1C", "Ceiling backing and firestopping, patch and paint")
line("1D", "Floor raceway per Attachment B")
line("", "<b>Phase 1 total</b>")
sec("PHASE 2: LIGHTING AND SCREEN SYNC")
line("2A", "Screen sync package: 3 gradient strips, sync box, Hue Bridge Pro")
line("2B", "Six reactive accent lights")
line("2C", "General lighting: fixtures, install, wall controls, removal of old fixtures")
line("2D", "Programming, scenes, testing, training")
line("2E (alt)", "Second and third sync box, if needed for left and right TVs")
line("", "<b>Phase 2 total (2A to 2D)</b>")
sec("PHASE 3: DOLBY ATMOS AUDIO")
line("3A", "Receiver or processor, amplification, rack or cabinet")
line("3B", "Speakers (7.1.4) and subwoofer, installation")
line("3C", "Calibration, documentation, training")
line("3D (alt)", "Add two middle overheads (7.1.6)")
line("3E (alt)", "Second subwoofer")
line("3F (alt)", "Acoustic treatment (describe)")
line("", "<b>Phase 3 total (3A to 3C)</b>")
sec("PHASE 4: SEATING")
line("4A", "Three rows, three 72 in. bays")
line("4B (alt)", "Four rows, three 72 in. bays")
line("4C", "Remove two wall cabinets and countertop section, patch wall")
line("", "<b>Phase 4 total (4A + 4C)</b>")
sec("COMBINED")
line("", "Discount if Phases 1 to 3 are awarded together (amount or %)")
line("", "Discount if all four phases are awarded together (amount or %)")
t = table(rows, [PW * .11, PW * .56, PW * .19, PW * .14])
from reportlab.platypus import TableStyle
t.setStyle(TableStyle([("TOPPADDING", (0, 1), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 1), (-1, -1), 3.5), ("BOX", (2, 1), (3, -1), .4, LINE), ("INNERGRID", (2, 1), (3, -1), .4, LINE)]
                  + [c for i in secs for c in (("SPAN", (0, i), (-1, i)), ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#e6ebef")))]))
E.append(t)
E.append(Spacer(1, 8))
E.append(P("Authorized signature: ______________________________ &nbsp;&nbsp; Printed name and title: ______________________________", B))

# ------------------------------------------------ attachments and sources
E.append(P("Attachments and sources", H2))
E.append(P("<b>Attachment A:</b> Room413_Bleacher_Inquiry.pdf. <b>Attachment B:</b> Room413_Raceway_Plans.pdf. Both are in the same project folder, and both use the old room number. Dimensions are the district's own and are accurate to about an inch.", S))
E.append(P("Product facts are from the manufacturers' public pages and reviews, and should be checked against current data sheets: "
           + link("https://www.philips-hue.com/en-us/p/hue-philips-hue-play-hdmi-sync-box-8k/046677579753", "Hue Play HDMI Sync Box 8K") + ", "
           + link("https://www.philips-hue.com/en-us/p/hue-bridge-pro/046677582111", "Hue Bridge Pro") + ", "
           + link("https://www.philips-hue.com/en-us/p/lightstrips-philips-hue-play-gradient-strip-light-85/046677611767", "Hue Play gradient strip 85 in.") + ", "
           + link("https://www.dolby.com/about/support/guide/dolby-atmos-speaker-setup/", "Dolby Atmos speaker setup") + " and the "
           + link("https://www.dolby.com/siteassets/technologies/dolby-atmos/atmos-installation-guidelines-121318_r3.1.pdf", "Dolby Atmos home installation guidelines (2018)") + ".", S))

doc.build(E, onFirstPage=footer(TITLE), onLaterPages=footer(TITLE))
print("built bid")
