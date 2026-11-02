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
E.append(P("Caldwell High School is converting Room 136 (called Room 413 in some earlier drawings) into a media tech and esports classroom that also works as a small competition arena. The room's power, network, desks and computers are already in place. We are asking for firm pricing on six phases that can be awarded together or one at a time: three 85 in. displays, a Philips Hue lighting system with screen sync, retractable seating, a Dolby Atmos sound system, broadcast cameras, and wall graphics and finishes. Please price each phase and each alternate separately, and tell us what you would save by doing phases together."))
E.append(P("What the district already has", H2))
E.append(table([
    ["Item", "Status", "Approx. value"],
    ["<b>Power and network</b>", "Electrical and network infrastructure for the room is in place. Not part of this bid. Where a phase needs an outlet or a network port at a specific spot, check it on your site visit and price any missing piece as its own line, as noted under each phase.", "Not provided"],
    ["<b>Floor power and network</b>", "A desk power and network layout three drops across and two deep, matching the existing floor boxes. The district is checking whether to shift the drops 12 in. west; not decided. Treat positions as approximate, confirm them on your site visit, and do not locate anything that depends on them until the district confirms.", "Not provided"],
    ["<b>Video cabling</b>", "Two HDMI 2.1 fiber-optic cables already run through the ceiling from the north wall to the south wall. Not part of this bid. The district will mark both ends. Use them where they help, and tell us the length, connector type and 4K 120 Hz rating you assume before you price.", "Not provided"],
    ["<b>Desks and chairs</b>", "13 desks and 28 chairs.", "Not provided"],
    ["<b>Computers</b>", "24 student PCs, plus one or two teacher PCs: one for classroom use and one for esports streaming.", "12 PCs at about $2,700 each, about $32,400 (district figure). Other PCs: not provided."],
], [PW * .17, PW * .57, PW * .26]))
E.append(P("Values are the district's own figures, shown so bidders can see the investment already in the room. Only the PC figure has been entered so far; the others will be completed before release or left out.", S))
E.append(P("The six phases", H2))
E.append(table([
    ["Phase", "What it covers", "Why this order", "Depends on"],
    ["<b>1. Displays</b>", "Three 85 in. 4K 120 Hz displays on the north wall, mounts, HDMI 2.1 connections, setup and testing.", "The screens are the heart of the room, and the lighting needs them mounted first.", "None."],
    ["<b>2. Lighting and screen sync</b>", "Three Hue gradient strips behind the displays, a Hue Play HDMI Sync Box on the main screen, six reactive accent lights, Hue-controlled ceiling lighting in four dimmable zones, a Hue Bridge Pro, wall controls, programming.", "The most visible change for students. Needs the displays mounted and the existing power and network.", "Phase 1 mounts and clearances."],
    ["<b>3. Seating</b>", "Retractable bleacher seating on the south wall, plus removing two wall cabinets (Attachment A).", "Longest lead time. Settles what is on the south wall before sound and cameras are placed.", "None. Coordinate with Phases 4 and 5."],
    ["<b>4. Dolby Atmos audio</b>", "7.1.4 speaker system (11 speakers plus subwoofer), receiver or processor, amplification, rough-in, calibration, training.", "Rear speakers and overheads sit around the bleachers; the receiver joins the chain from Phase 2.", "Phases 1 to 3."],
    ["<b>5. Cameras and broadcast</b>", "Five 4K cameras (three on the north wall, two on the south wall), network and power for them, control, capture and switching for the esports streaming PC.", "Needs seating and lighting settled so the cameras see the room as it will really look.", "Phases 2 and 3."],
    ["<b>6. Wall graphics and finishes</b>", "Printed wall graphics and branding, and the remaining finish items that make it look like an arena. Scope still being set; unit prices requested.", "Last, so nothing is covered by or fights with the earlier work.", "Phases 1 to 5."],
], [PW * .17, PW * .41, PW * .26, PW * .16]))
E.append(P("The order is our proposal. Phases 1 and 2 should go first and in that order; phases 3 to 6 can be swapped, except that Phase 4 should not come before the seating decision. Tell us if a different sequence is cheaper or lower-risk.", S))
E.append(P("Room facts", H2))
E.append(table([
    ["Item", "Dimension or condition"],
    ["Main room", "400 in. x 376 in. (33 ft 4 in. x 31 ft 4 in.), about 1,044 sq ft; 10 ft ceiling; level floor with existing floor power and network boxes (see above). Ceiling type, slab and what is above the ceiling are to be confirmed on site."],
    ["Southwest alcove", "76 in. x 194 in., open to the room (no wall between the alcove and the desk area on the west side)."],
    ["Server room", "76 in. x 130 in., adjoining the northwest corner. Not part of the room; available for equipment if you recommend it."],
    ["Displays", "Three 85 in. TVs on the north wall, centers 86 in. apart, centered on the room. The center TV is the main screen."],
    ["Doors and window", "Three 36 in. doors (north wall near the east corner, east wall near the south corner, southwest entry). Window on the west side of the north end."],
    ["South wall", "Wall cabinets 46 / 36 / 36 in. wide, 13 in. deep, 58 to 85 in. above the floor; one 36 x 30 in. tall cabinet; countertop 145 in. long."],
], [PW * .20, PW * .80]))
E.append(Spacer(1, 6))

# ------------------------------------------------ integration
E.append(P("How the pieces connect", H1))
E.append(KeepTogether([img("bid_flow.png", PW * .78), P("Figure 1. Proposed signal flow. Phases 1 to 3: sources go to the sync box, and the sync box goes to the center TV. Phase 4 adds the receiver, which sits between the sources and the sync box, so sound stays decoded by the receiver and the lights follow the picture. Bidders may propose a different order, such as taking sound from the TV over eARC, and must say how Atmos, 4K 120 Hz and device switching behave. Some user reviews of the sync box report input-switching problems when an AV receiver is in the chain, so we want you to test the chain before handover and list the settings you used.", S)]))
E.append(P("The sync box only reads HDMI sources, so the picture it syncs to has to come through it. Philips lists the 8K sync box as supporting 4K at 120 Hz and HDMI 2.1; we did not find an official statement on variable refresh rate, so every bidder must confirm 4K 120 Hz, variable refresh rate and low-latency game mode against the esports PC before pricing. The two existing fiber cables must pass the same signal.", B))

# ------------------------------------------------ phase 1
E.append(P("Phase 1: Displays", H1))
E.append(P("All work by appropriately licensed contractors, permitted and inspected as the jurisdiction requires. Coordinate with the district electrician and facilities before any penetration.", S))
E.append(table([
    ["Item", "Requirement"],
    ["<b>Displays</b>", "Three matching 85 in. 4K (3840 x 2160) displays. Each must accept 4K at 120 Hz over HDMI 2.1 on at least two inputs, with variable refresh rate and auto low-latency mode, and eARC on one input. Say the model, panel type, and brightness and glare performance in a room with a 10 ft ceiling and light-colored walls. Warranty must cover daily use in a school; say if a commercial or pro-display model is needed to get that."],
    ["<b>Mounts</b>", "Three wall mounts rated for the display weight, centers 86 in. apart and centered on the room, aligned level with the same bottom height. The back of each display needs enough clearance for a Hue gradient strip (Phase 2), so tell us the standoff depth you will use. Wall backing behind the north wall has not been verified; confirm it and price any reinforcement. Include anti-theft hardware and concealed cable management."],
    ["<b>HDMI 2.1</b>", "Terminate and test the two existing ceiling fiber cables at the north wall and connect the center display. Report any cable that does not carry 4K 120 Hz. Left and right TV video feeds are Alternate 1E, below."],
    ["<b>Power and network</b>", "The district reports power and network are in place. Verify a duplex outlet behind each display and one network port near the north wall center. Price any correction as line 1D."],
    ["<b>Setup</b>", "Update firmware, set game mode and local dimming, turn off motion smoothing and unneeded smart features and advertising, and lock settings so a student cannot change them from the remote. Accounts belong to the district."],
    ["<b>Testing</b>", "Show 4K at 120 Hz on each display from the esports PC through every cable in the chain, and give us a short report."],
], [PW * .18, PW * .82]))
E.append(P("Alternates to price", H2))
E.extend(bl([
    "<b>1E.</b> HDMI 2.1 video to the left and right displays: show how you would feed them either a mirror of the center screen or their own source, and price each. Today the district only plans for their backlights to follow the center screen.",
    "<b>1F.</b> Commercial or pro-display models, if the base bid is a consumer model.",
]))

# ------------------------------------------------ phase 2
E.append(KeepTogether([P("Phase 2: Philips Hue lighting and screen sync", H1), P("The goal is a classroom with enough even light for daily teaching, a dimmed media mode that does not wash out the screens, and color that reacts to what is on the main screen.", B), img("bid_lighting.png", PW * .68), P("Figure 2. Lighting concept. Strips glow on the wall behind the three TVs; six accent lights and the strips form one sync group; four zones (A to D) dim separately.", S)]))
E.append(P("Base bid", H2))
E.append(table([
    ["Item", "Requirement"],
    ["<b>TV backlights</b>", "Three Hue Play gradient strips, 85 in. size, one on the back of each TV. Confirm fit with the Phase 1 mounts and standoff depth. Philips' listing says the strip can be cut to size, but some press coverage says it cannot; confirm with the manufacturer before you price."],
    ["<b>Sync box</b>", "One Hue Play HDMI Sync Box 8K on the center (main) screen, with all four inputs available. It syncs only HDMI sources, not the TV's own apps. It must pass 4K at 120 Hz from the esports PC."],
    ["<b>Reactive accent lights</b>", "Six color-capable Hue lights (light bars or strips) at the positions in Figure 2 or better ones you propose. A gradient strip counts as one light toward the sync box's 10-light limit, so three strips and six accent lights is 9 of 10; confirm the limit applies to the current firmware."],
    ["<b>Left and right TVs</b>", "Their strips should follow the center screen's sync. If a single sync box cannot do that, price the second and third box as Alternate 2E and say what each TV would need."],
    ["<b>Bridge</b>", "One Hue Bridge Pro on Ethernet (Philips lists 150+ lights and 50+ accessories). Place it where Zigbee reaches every fixture; say where."],
    ["<b>General lighting</b>", "Hue-controllable, dimmable ceiling fixtures in zones A to D. Design targets: 30 to 50 footcandles at desk height in the Class scene (the range commonly cited for classrooms; your lighting designer should confirm), color rendering of 80 or better, no direct glare on the TVs or student monitors. Our rough lumen check is about 16 panels at roughly 4,000 lumens each in the main room, plus two in the alcove. Your photometric layout governs."],
    ["<b>Power</b>", "Smart fixtures must never lose power at a wall switch. Remove or lock out the existing wall switches for the lights being replaced, say how, and include any change to the lighting circuits. Add outlets behind the displays only if Phase 1 found them missing. Existing network is used; check that a wired port reaches the bridge and sync box."],
    ["<b>Scenes</b>", "At least: Class (full light), Media (zone A dark, desk zone dimmed for screens), Esports (low light with color, accent lights live), Broadcast (steady, even light for the cameras, no color changes) and Full on / cleaning. One tap on a wall controller for each."],
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
E.append(P("Phase 3: Retractable seating", H1))
E.append(P("Pricing for the south-wall bleachers, based on our earlier inquiry (Attachment A, which still calls the room 413).", B))
E.extend(bl([
    "<b>Option 3A:</b> three 72 in. bays, three rows at 30 in. spacing (about 90 in. deep).",
    "<b>Option 3B:</b> the same bays, four rows (about 120 in. deep).",
    "<b>Cabinet work, 3C:</b> remove the two 36 in. wall cabinets at x = 78 to 150 in. and the countertop section from x = 92 in., and patch the wall. The 46 in. cabinet and the tall cabinet stay.",
    "Tell us stowed depth, wall backing needed, guardrail and access requirements and the standard you meet, and operating effort.",
    "Coordinate with Phases 4 and 5: rear speaker and overhead positions, and the two south-wall cameras, sit above or near the seating zone.",
]))

# ------------------------------------------------ phase 4
E.append(Spacer(1, 12))
E.append(KeepTogether([P("Phase 4: Dolby Atmos sound system", H1), P("The goal is clear, even sound for a room used for class instruction, media editing and esports watch parties, with true overhead channels and a main screen that stays in sync with the lights. This phase includes its own rough-in: speaker wire pathways, ceiling backing at the overhead positions, and the equipment's power and network connections, with any missing pieces priced in line 4A.", B), img("bid_audio.png", PW * .68), P("Figure 3. Atmos 7.1.4 concept. L, C and R sit with the TV wall; two side and two rear surrounds; four overheads placed about 45 degrees up from the middle of the desk zone (roughly 6 ft in front of and behind it, from the rule of thumb in Dolby's setup guidance).", S)]))
E.append(P("Base bid", H2))
E.append(table([
    ["Item", "Requirement"],
    ["<b>Layout</b>", "7.1.4: left, center, right, two side surrounds, two rear surrounds, four overhead speakers and at least one subwoofer. Positions in Figure 3 are indicative."],
    ["<b>Electronics</b>", "Receiver or processor with at least 11 amplified channels (or a processor plus amplification), Dolby Atmos decoding, HDMI 2.1 with 4K 120 Hz pass-through and eARC, automatic room correction, and a network port. Say what it does with the sync box in the chain (Figure 1)."],
    ["<b>Speakers</b>", "Overheads in-ceiling. Front and surround speakers on-wall or in-wall depending on wall construction. Center speaker under the center TV. The center has to work with three large TVs, so tell us how you aim and place it."],
    ["<b>Level and safety</b>", "A maximum volume the district can set and lock. Wall or remote volume control."],
    ["<b>Calibration</b>", "Measured room correction with all channels, a written result, and a saved configuration."],
    ["<b>Training and documents</b>", "Two hours of staff training and a one-page operating guide kept in the room."],
], [PW * .18, PW * .82]))
E.append(P("Alternates to price", H2))
E.extend(bl([
    "<b>4D.</b> 7.1.6: add two middle overhead speakers (dashed in Figure 3).",
    "<b>4E.</b> A second subwoofer on the east wall.",
    "<b>4F.</b> Acoustic treatment, if you think the room needs it, with your reasoning. Coordinate with Phase 6 wall finishes.",
]))
E.append(P("Design questions for your response", H2))
E.extend(bl([
    "The room holds more listeners than a home theater sweet spot, with several desk layouts. What do you change from a standard 7.1.4 to cover everyone (speaker choice, more overheads, delay and level)?",
    "The west side next to the desk zone is an open alcove, so there is no wall for the left side surround. Figure 3 shows it on the alcove wall, which is farther away than the right side. Propose a balanced solution.",
    "The rear surrounds sit over the south-wall cabinets and the bleachers (Phase 3). Confirm mounting height and clearance above the top row.",
    "Where do you recommend the electronics (the server room, the tall cabinet, or where the existing fiber cables end), and what HDMI cable type and length does that need?",
]))

# ------------------------------------------------ phase 5
E.append(Spacer(1, 12))
E.append(KeepTogether([P("Phase 5: Cameras and broadcast", H1), P("The goal is to broadcast events and show competitors and audience, on the room's screens and to a stream. Five 4K cameras: three on the north wall facing the room and two on the south wall facing the screens. Camera feeds go to the esports streaming PC.", B), img("bid_cameras.png", PW * .68), P("Figure 4. Camera concept. N1 to N3 sit on the north wall above or beside the displays and see competitors' faces and the audience; S1 and S2 sit high on the south wall and see the screens and competitors from behind. Positions and aim are for you to refine after a site visit.", S)]))
E.append(P("Base bid", H2))
E.append(table([
    ["Item", "Requirement"],
    ["<b>Cameras</b>", "Five 4K cameras, matching if possible, good in low light because Phase 2 dims the room. Base bid is remote pan-tilt-zoom cameras; price fixed cameras as Alternate 5E. Tell us frame rate, lens field of view, and sensor and low-light performance for your model."],
    ["<b>Video path</b>", "Your choice of network video (such as NDI, SRT or RTSP over PoE) or direct video cable to a switcher. State the bandwidth each camera needs. Camera traffic must not burden the district network: district IT will give a dedicated VLAN, and a dedicated PoE switch is part of your price. Network and power drops for the cameras are priced in line 5A."],
    ["<b>Control and mixing</b>", "A way for one operator to switch between cameras, recall camera positions and send a mix to the stream and to any TV. Software on the esports streaming PC, a hardware switcher, or both; recommend and price it. State the minimum specification the streaming PC needs, so the district can check it."],
    ["<b>Show on the screens</b>", "Any camera, or the program mix, can be put on the main screen as an HDMI source, at the same quality as other sources."],
    ["<b>Mounting</b>", "Rigid, level mounts that keep the lens clear of the TVs, accent lights, ceiling fixtures and the bleachers. Concealed cable. Confirm wall and ceiling backing at every camera."],
    ["<b>Lighting coordination</b>", "Color-changing accent lights make a camera's white balance drift. Say how you handle it with the Phase 2 Broadcast scene, and how you fix it when the lights are in Esports mode."],
    ["<b>Student privacy</b>", "These cameras record students. Staff must be able to power the cameras off from the room, there must be a visible indicator when a camera is live or streaming, and recorded video must be stored only where the district chooses. Media release and use of recordings follow district policy."],
    ["<b>Testing and training</b>", "Test all five feeds for at least 30 minutes with the streaming PC, a typical event layout and the lights in each scene. Two hours of staff training and a one-page operating guide."],
], [PW * .18, PW * .82]))
E.append(P("Alternates to price", H2))
E.extend(bl([
    "<b>5E.</b> Fixed cameras in place of pan-tilt-zoom cameras, for any position where you recommend it.",
    "<b>5F.</b> Hardware video switcher or capture device, if your base bid uses software only.",
]))

# ------------------------------------------------ phase 6
E.append(Spacer(1, 12))
E.append(P("Phase 6: Wall graphics and finishes", H1))
E.append(P("The district is still setting the scope for the finishes that make the room look like an arena. Until it does, we ask for unit prices so the work can be priced when the design is chosen.", B))
E.extend(bl([
    "<b>6A. Printed wall graphics.</b> Price per square foot, installed, for vinyl or printed fabric panels on the east, west and south walls (not the display wall), including a design allowance, proofs and removal. The district will supply logos and artwork.",
    "<b>6B. Signage.</b> Price for a room sign and one illuminated wall sign, supplied with the district's text or logo.",
    "<b>6C. Other finishes.</b> The district may add items such as paint, acoustic wall panels, trophy or display shelving, or a stage rail. List anything you would recommend and price it as a separate line.",
    "Every material must be rated for classroom use and meet the fire-code flame-spread requirements the jurisdiction applies. Give us the rating for each material, and its cleaning instructions.",
]))

# ------------------------------------------------ all phases
E.append(P("Requirements for every phase", H2))
E.extend(bl([
    "Prices are firm for 90 days. The district is expected to be tax-exempt; purchasing will confirm.",
    "Each phase is priced so it can be awarded alone. Show any discount for combining phases.",
    "Work happens outside class hours or during breaks. Give your proposed schedule and the days the room is out of use. Contractor staff must meet district requirements for badging and background checks; district purchasing will supply them.",
    "Product substitutions are welcome when they meet or beat the requirements. List the model numbers you propose and why.",
    "Submit with your bid: product data sheets, one marked-up plan per phase, manufacturer and labor warranty terms, lead times, and three references from school or public projects.",
    "At handover: as-built drawings, exported device configuration (receiver, bridge, sync box, cameras), district-owned account access, the operating guide, and staff training.",
]))
E.append(P("Questions about this bid", H2))
E.append(P("Send written questions to Chad Lawson (contact at the top). Answers will go to every bidder. Site visits are by appointment; we recommend one before you price, to confirm the ceiling, the north wall, the south wall and the west alcove."))
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
sec("PHASE 1: DISPLAYS")
line("1A", "Three 85 in. 4K 120 Hz displays")
line("1B", "Mounts, installation, wall reinforcement if needed")
line("1C", "HDMI 2.1 termination and testing, setup, configuration")
line("1D", "Correction of missing outlets or network ports (describe)")
line("1E (alt)", "HDMI 2.1 video to left and right displays (mirror price; independent-source price)")
line("1F (alt)", "Commercial or pro-display models")
line("", "<b>Phase 1 total (1A to 1D)</b>")
sec("PHASE 2: LIGHTING AND SCREEN SYNC")
line("2A", "Screen sync package: 3 gradient strips, sync box, Hue Bridge Pro")
line("2B", "Six reactive accent lights")
line("2C", "General lighting: fixtures, install, wall controls, removal of old fixtures, circuit changes")
line("2D", "Programming, scenes, testing, training")
line("2E (alt)", "Second and third sync box, if needed for left and right TVs")
line("", "<b>Phase 2 total (2A to 2D)</b>")
sec("PHASE 3: SEATING")
line("3A", "Three rows, three 72 in. bays")
line("3B (alt)", "Four rows, three 72 in. bays")
line("3C", "Remove two wall cabinets and countertop section, patch wall")
line("", "<b>Phase 3 total (3A + 3C)</b>")
sec("PHASE 4: DOLBY ATMOS AUDIO")
line("4A", "Rough-in: speaker pathways and wire, ceiling backing, power and network connections")
line("4B", "Receiver or processor, amplification, rack or cabinet")
line("4C", "Speakers (7.1.4) and subwoofer, installation, calibration, documentation, training")
line("4D (alt)", "Add two middle overheads (7.1.6)")
line("4E (alt)", "Second subwoofer")
line("4F (alt)", "Acoustic treatment (describe)")
line("", "<b>Phase 4 total (4A to 4C)</b>")
sec("PHASE 5: CAMERAS AND BROADCAST")
line("5A", "Network and power for five cameras, dedicated PoE switch")
line("5B", "Five 4K pan-tilt-zoom cameras, mounts and installation")
line("5C", "Control, capture and switching; configuration; testing; training")
line("5E (alt)", "Fixed cameras in place of pan-tilt-zoom (per camera)")
line("5F (alt)", "Hardware video switcher or capture device")
line("", "<b>Phase 5 total (5A to 5C)</b>")
sec("PHASE 6: WALL GRAPHICS AND FINISHES (unit prices)")
line("6A", "Printed wall graphics, installed (price per sq ft); design allowance")
line("6B", "Room sign and one illuminated wall sign")
line("6C", "Other finishes recommended (describe each line)")
sec("COMBINED")
line("", "Discount if Phases 1 and 2 are awarded together (amount or %)")
line("", "Discount if all of Phases 1 to 5 are awarded together (amount or %)")
t = table(rows, [PW * .11, PW * .56, PW * .19, PW * .14])
from reportlab.platypus import TableStyle
t.setStyle(TableStyle([("TOPPADDING", (0, 1), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 1), (-1, -1), 3.2), ("BOX", (2, 1), (3, -1), .4, LINE), ("INNERGRID", (2, 1), (3, -1), .4, LINE)]
                  + [c for i in secs for c in (("SPAN", (0, i), (-1, i)), ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#e6ebef")))]))
E.append(t)
E.append(Spacer(1, 8))
E.append(P("Authorized signature: ______________________________ &nbsp;&nbsp; Printed name and title: ______________________________", B))

# ------------------------------------------------ attachments and sources
E.append(P("Attachments and sources", H2))
E.append(P("<b>Attachment A:</b> Room413_Bleacher_Inquiry.pdf (uses the old room number). Dimensions are the district's own and are accurate to about an inch. The floor raceway concept in the same project folder is not part of this bid.", S))
E.append(P("Product facts are from the manufacturers' public pages and reviews, and should be checked against current data sheets: "
           + link("https://www.philips-hue.com/en-us/p/hue-philips-hue-play-hdmi-sync-box-8k/046677579753", "Hue Play HDMI Sync Box 8K") + ", "
           + link("https://www.philips-hue.com/en-us/p/hue-bridge-pro/046677582111", "Hue Bridge Pro") + ", "
           + link("https://www.philips-hue.com/en-us/p/lightstrips-philips-hue-play-gradient-strip-light-85/046677611767", "Hue Play gradient strip 85 in.") + ", "
           + link("https://www.dolby.com/about/support/guide/dolby-atmos-speaker-setup/", "Dolby Atmos speaker setup") + " and the "
           + link("https://www.dolby.com/siteassets/technologies/dolby-atmos/atmos-installation-guidelines-121318_r3.1.pdf", "Dolby Atmos home installation guidelines (2018)") + ".", S))

doc.build(E, onFirstPage=footer(TITLE), onLaterPages=footer(TITLE))
print("built bid")
