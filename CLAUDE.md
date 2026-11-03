# Room 136 Media Tech / Esports

Owner: Chad Lawson, Media Technologies teacher and District Esports Coordinator, Caldwell High School. Interactive 3D lab layout (three.js) plus vendor/bid PDFs built from the same geometry. See README.md for the file map.

## Working style
- Chad thinks globally and wants help with details. Be concise, lead with the big picture, push back on weak plans. Dry tone in chat; no sarcasm in formal documents (bids, vendor inquiries, admin or parent communications).
- Prefer existing solutions over building from scratch.
- No student data belongs in this project. If any appears, keep it out of anything shared outside caldwellschools.org.

## Model (index.html)
Single self-contained page. three.js r128 and OrbitControls from jsDelivr, so it needs internet. Edit in place; there is no build step. Serve with `python -m http.server` to view.

Coordinates are inches: x east, z south, y up. North is -z.
- Main room x 0-400, z 0-376. SW alcove x -76..0, z 130..324. Server room x -76..0, z 0..130.
- Entry door x -61..-25 at z=324. Server-room door x -68..-32 at z=130; it swings into the classroom and rests against the west wall.
- Desks are 70x30 with two seats; gaming PC tower under each. 12 student desks plus the teacher desk.
- Chairs and figures are separate scene-level seat units (`ALLSEATS`) so they can move independently of desks.
- Layouts are `MODES` (class, bleach, comp, comp3, comp3v, pres, presb). Build phases are set with `setPhase(n)`, which rebuilds the phase-dependent poses (`compPoses`, `comp3Poses`, `presPoses`). `setMode(name, instant)` drives the animations.
- Phase 1: 24 gaming PCs, one 75 in. portable floor-stand TV at the center of the north wall, streaming station in the server room. Full build: three 85 in. TVs on the north wall, premium center, lower-grade sides.
- Competition: home game = 3 desks in a row; visitors = 6 desks, each team one in front and two behind, facing south.

## Unverified assumptions (confirm with Chad before relying on them)
Countertop depth 24 in.; tall cabinet height 85 in.; bleachers 3 bays x 72 in.; server room 76 x 130 in.; chair-back bleacher row spacing 30-33 in.

## Known gaps
- The model has been checked only with a stubbed three.js and numeric position tests, never visually. Open it in a real browser and look at every mode and phase first.
- The bleacher and raceway PDFs still say Room 413 and predate the comp3, comp3v and Phase 1 layouts.
- Not yet modeled: PTZ camera positions and cable runs (3 PTZ at the front, 2 more at the back later), NDI routing to the side TVs.

## PDFs
Regenerate with the commands in README.md (`pip install -r tools/requirements.txt`). Scripts in `tools/` draw the figures into `tools/build/`, then assemble the PDFs into `docs/`.

## AV plan notes (for context)
- Remote OBS: OBS WebSocket on port 4455 on the hub PC; the classroom PC or laptop connects over the LAN.
- Cameras: IP PTZ over PoE, NDI/NDI|HX or ONVIF/VISCA control; not SDI by default.
- Side TVs: 6 NDI player feeds into capture/receiver PC in the server room, three HDMI outputs to the TVs.
- Teacher PC casting: NDI Screen Capture HD. Casting classroom screens raises FERPA concerns; get IT/VLAN approval.

## Git
Do not push without Chad's say-so. Check `git status` and `git log` before editing, since other sessions have committed here.
