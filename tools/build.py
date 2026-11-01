import os
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(HERE, "build"))
DOCS = os.path.join(HERE, "..", "docs")
from pdfcommon import *
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak, KeepTogether

# ------------------------------------------------ bleacher package
doc = SimpleDocTemplate(os.path.join(DOCS, "Room413_Bleacher_Inquiry.pdf"), pagesize=letter,
                        leftMargin=.7 * inch, rightMargin=.7 * inch, topMargin=.6 * inch, bottomMargin=.7 * inch,
                        title="Room 413 Retractable Seating Inquiry", author="Chad Lawson")
E = []
E.append(P("Retractable Bleacher Seating: Room 413 Project Information", H1))
E.append(P("Caldwell High School, 3401 S Indiana Avenue, Caldwell, ID 83605 &nbsp;|&nbsp; Prepared October 29, 2026", S))
E.append(P("Contact: Chad Lawson, Media Technologies and District Esports Coordinator &nbsp;|&nbsp; clawson@caldwellschools.org &nbsp;|&nbsp; 208-455-3304 ext. 2136", S))
E.append(Spacer(1, 4))
E.append(P("We are looking at a retractable seating system for a media and esports classroom. The room is 400 in. by 376 in. with a 10 ft ceiling, and the seating would face three wall-mounted displays on the north wall. The same room is used as a regular class, so the seating has to fold back and clear the floor. Please review the drawing and notes below and send specifications and budgetary pricing for the options that fit. Items marked as assumptions are open and we welcome your recommendation."))
E.append(img("plan_dim.png", PW))
E.append(P("Figure 1. Plan view, inches unless noted. North is up. The dashed outline shows the largest seating footprint under consideration; the shaded area shows the 3-row option.", S))
E.append(PageBreak())

E.append(P("Key dimensions", H2))
E.append(table([
    ["Item", "Dimension"],
    ["Room, side wall to side wall", "400 in. (33 ft 4 in.)"],
    ["Room, north wall to south wall", "376 in. (31 ft 4 in.)"],
    ["Ceiling height", "120 in. (10 ft)"],
    ["Seating wall (south)", "Full 400 in. width; wall cabinets and one tall cabinet along the west portion (see below)"],
    ["Displays", "Three 85 in. TVs on the north wall, centers 86 in. apart, centered on the room"],
    ["Doors", "North wall (near east corner), east wall (near south corner) and a southwest entry; all 36 in. openings"],
    ["Alcove at southwest", "76 in. wide, 194 in. long, open to the room"],
    ["Floor", "Level; floor type and slab details to be confirmed on site"],
], [PW * .33, PW * .67]))
E.append(P("South wall conditions", H2))
E.extend(bl([
    "<b>Wall cabinets:</b> three, 46, 36 and 36 in. wide, running west to east. All are 13 in. deep, 27 in. tall, mounted with the bottom 58 in. and the top 85 in. above the floor.",
    "<b>Tall cabinet:</b> 36 in. wide, 30 in. deep, 85 in. high, at the west end against the entry pier.",
    "<b>Likely changes:</b> the two 36 in. wall cabinets would be removed if the seating is centered on the displays. The 46 in. cabinet and the tall cabinet would stay.",
    "<b>Wall construction and backing:</b> not yet verified. We will confirm what is behind the cabinets before any wall attachment.",
]))
E.append(P("Seating the room is meant to hold", H2))
E.append(P("These are working assumptions, not requirements:"))
E.extend(bl([
    "<b>Capacity:</b> about 24 to 36 spectator seats. The drawing assumes three 72 in. bays with three seats each (216 in. total width).",
    "<b>Option A, 3 rows:</b> about 90 in. deep at 30 in. row spacing.",
    "<b>Option B, 4 rows:</b> about 120 in. deep at 30 in. row spacing. Chair-back systems list row spacing of 28 to 33 in., so four rows run deeper than the 24 in. rows shown in our early layouts.",
    "<b>Chairs:</b> chair-back or platform seating preferred over plain benches; folding or fold-down seats that stow with the platform.",
    "<b>Operation:</b> manual or power-assist, whichever suits a small room. Class use is daily, so it needs to be quick and safe for staff to operate.",
    "<b>Retracted depth:</b> we need to know how far the stowed system sticks out from the south wall, since the floor in front is classroom space.",
]))
E.append(KeepTogether([img("section.png", PW * .6), P("Figure 2. Illustrative section at x = 120 in., 4 rows at 30 in. spacing and 10.25 in. rise. Seat and body heights are assumptions. The top row sits in the same space as the 58 to 85 in. wall cabinet, which is why the cabinets are the first thing to resolve.", S)]))

E.append(P("Examples of retractable systems we are considering", H2))
E.append(P("Published manufacturer information only. Please correct anything that does not apply to your configuration.", S))
E.append(table([
    ["System", "What it is", "Published specs"],
    ["<b>Interkal VISION</b> on the Wide Deck Premier platform", "Telescopic platform with fold-down chair-back seating, blow-molded plastic with cast aluminum brackets.",
     "Row spacing 30, 32 or 33 in. Minimum rise 10.25 in. Seat widths 19 to 24 in., plus an 18 in. armless option. Manual, semi-manual or semi-automatic (gas strut) fold-down. Optional tablet arms, cup holders and row/seat numbers. 15 standard colors."],
    ["<b>Interkal POLARIS</b> multi-purpose seat", "Bench-and-chair seat for telescopic systems and stadium seating, with optional backrest and armrests.",
     "Row spacing 26 in. (bench only), 28 in. (with backrest or backrest and armrests), 30 in. (with backrest and cup-holder armrests). Seat widths 18 to 23 in. Seat depth 13.5 in. Rise and retracted depth not stated."],
    ["<b>Hussey Seatway TP</b> telescopic platform", "Retractable platform available wall-attached, recessed into a wall pocket, or portable on locking floor pintels.",
     "Seat options include Gallery 3, Club Bench, Metro, Premia and the Quattro Collection. Manual or power-assisted. The Club Bench needs a minimum rise just under 10.5 in. Row depth and retracted depth are not published."],
], [PW * .22, PW * .27, PW * .51]))
E.append(P("Questions for your team", H2))
E.extend(bl([
    "What is the stowed depth from the wall for 3 and for 4 rows, with chairs folded?",
    "Which configurations fit a 400 in. wide, 376 in. deep room with a 120 in. ceiling and 36 in. doors, and what row spacing and rise do you recommend?",
    "Wall-attached, recessed or portable? What are the wall backing and floor requirements for each?",
    "What are the guardrail, handrail and access requirements at the top row, and which standard does the system meet (for example ICC 300)?",
    "Manual versus power-assist: operating effort, power requirement and typical service interval.",
    "Per-seat and per-bay budgetary pricing for both options, plus delivery, installation and lead time.",
    "Do you offer a site visit or a field check of the south wall before final design?",
]))
E.append(P("Assumptions and sources", H2))
E.append(P("Dimensions come from our own floor plan and field measurements and are accurate to about an inch. The server-room walls are not part of this inquiry. Bleacher footprints in Figure 1 are our working assumptions. Product details are from the manufacturers' public pages: "
           "<link href='https://www.interkal.com/Vision-Platform-Chair-Seating' color='#0b6e99'>Interkal VISION</link>, "
           "<link href='https://www.interkal.com/polaris-multi-purpose-seating' color='#0b6e99'>Interkal POLARIS</link> and "
           "<link href='https://www.husseyseating.com/products/seatway-tp/' color='#0b6e99'>Hussey Seatway TP</link>.", S))
doc.build(E, onFirstPage=footer("Room 413 retractable seating inquiry | Caldwell High School"), onLaterPages=footer("Room 413 retractable seating inquiry | Caldwell High School"))

# ------------------------------------------------ raceway plans
doc = SimpleDocTemplate(os.path.join(DOCS, "Room413_Raceway_Plans.pdf"), pagesize=letter,
                        leftMargin=.7 * inch, rightMargin=.7 * inch, topMargin=.6 * inch, bottomMargin=.7 * inch,
                        title="Room 413 Floor Raceway Plans", author="Chad Lawson")
E = []
E.append(P("Room 413: FSR Smart-Way Floor Raceway Concept", H1))
E.append(P("One set of runs that serves all three layouts. Concept for discussion with the district electrician and facilities, not an engineered drawing.", S))
E.append(img("race_class.png", PW))
E.append(P("<b>The idea.</b> A single 280 in. cross-run along z = 141 in. passes through the middle desk of each group in the class layout (west column, center stack, east column) and through the middle desk of each team row in the competition layout, which happen to land at the same height in the room. A 99 in. spur runs south from the center of the cross-run to the south end of the stack and picks up the existing floor boxes as the feed. That puts a device box within one desk-length (70 in.) of every seat in every layout.", B))
E.append(PageBreak())
E.append(img("race_bleach.png", PW))
E.append(P("The student layout is the same as Layout 1, so the same boxes stay live. The teacher desk moves to the alcove, and the bleacher footprint (shown as modeled, 4 rows at 24 in.) stays clear of the raceway, which ends at z = 240 in.", B))
E.append(PageBreak())
E.append(img("race_comp.png", PW * .86))
E.append(P("Only the two boxes under the middle desk of each team row are live. The other positions are blanked, and the spur sits in the center of the 46 in. aisle, where it is walked on but not rolled across by desks.", B))
E.append(P("Rough quantities and open items", H2))
E.append(table([
    ["Item", "Estimate"],
    ["Raceway, cross-run + spur", "about 380 in. (31.6 ft), roughly six 6 ft sections cut to length"],
    ["Fittings", "1 tee (at the center of the cross-run), end caps, feeder tie-in at the existing floor box (186, 240)"],
    ["Device boxes", "6 positions: 4 live in the class layouts, 2 live in competition; the rest blanked"],
    ["Open: height and width", "FSR's page does not list the raceway cross-section. The 8 in. width drawn here is the figure we recalled for the product; confirm before final layout."],
    ["Open: rolling loads", "Straight sections are rated 8,000 lb per tire; the tee is rated 1,500 lb and corners 2,500 lb. Keep caster traffic off fittings where possible."],
    ["Open: electrical", "Circuit count, breaker capacity and code review for esports PCs on the run. UL listing was not stated on the product page."],
    ["Open: feed and network", "The feed point is assumed to be the existing floor box. Network can share the low-voltage compartment but needs a patch path from the server room."],
], [PW * .26, PW * .74]))
E.append(P("Source: <link href='https://fsrinc.com/fsr-products/product/4029-smartway-floor-raceway/category_pathway-176' color='#0b6e99'>FSR Smart-Way Floor Raceway</link>. Positions are in inches from the northwest corner of the main room (x east, z south).", S))
doc.build(E, onFirstPage=footer("Room 413 raceway concept | Caldwell High School"), onLaterPages=footer("Room 413 raceway concept | Caldwell High School"))
print("built")
