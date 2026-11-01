# Room 136 Media Tech / Esports

Interactive 3D layout of the Caldwell High School media tech and esports computer lab, built from field measurements (inches; x east, z south, y up), plus the vendor and electrical planning documents made from the same geometry.

## Contents

| Path | What it is |
|---|---|
| `index.html` | The 3D model. Single self-contained page; three.js and fonts load from CDNs, so it needs internet. Open it in a browser, or serve the folder (`python -m http.server`). |
| `docs/Room413_Bleacher_Inquiry.pdf` | Dimensioned plan, south-wall cabinet details and questions for a bleacher vendor. |
| `docs/Room413_Raceway_Plans.pdf` | FSR Smart-Way floor raceway concept over three layouts. |
| `docs/Room136_Phased_Bid_Package.pdf` | Draft four-phase bid package: infrastructure, Philips Hue lighting with screen sync, Dolby Atmos audio, retractable seating. Includes plans, a signal-flow diagram and a fill-in price sheet. Draft for district purchasing review. |
| `tools/figs.py`, `tools/build.py` | Scripts that draw the plans and assemble the bleacher and raceway PDFs. |
| `tools/figs_bid.py`, `tools/build_bid.py` | Scripts that draw the lighting, audio and signal-flow figures and assemble the bid package. |
| `tools/pdfcommon.py` | Shared fonts and layout helpers for the PDF scripts. |

The PDFs were made when the room was still called 413; the model has been renamed.

## Model features

- Layouts: Class, Class + bleachers out, Competition, Presentation, Presentation + bleachers out. Desks and chairs animate between them, including desks rolling through the server room door.
- Toggles: bleachers installed / out, students, wall fade, floor boxes, south wall cabinets, door swing zones, and a demo mode that removes the two 36 in. wall cabinets and the countertop section from x = 92 in.
- Camera presets: corner, top down, side, from / facing the bleachers, teacher desk, student seat, server room.

## Room data

- Main room 400 x 376 in., 10 ft ceiling, three 85 in. TVs on the north wall.
- Southwest alcove 76 x 194 in.; server room wall 130 in.
- South wall: wall cabinets 46 / 36 / 36 in. wide, 13 in. deep, 58 to 85 in. above the floor; tall cabinet 36 x 30 in.; countertop 145 in. long, top at 24 in.
- Assumptions to confirm: countertop depth 24 in., bleachers 3 bays x 72 in., server room 76 x 130 in., chair-back bleachers need 30 to 33 in. row spacing.

## Rebuilding the PDFs

```
pip install -r tools/requirements.txt
python tools/figs.py     # draws the plan images into tools/build/
python tools/build.py    # writes the bleacher and raceway PDFs into docs/
python tools/figs_bid.py # draws the bid figures into tools/build/
python tools/build_bid.py  # writes the bid package into docs/
```

## Student data

None. This project contains room geometry and furniture only.
