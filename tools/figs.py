import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyArrowPatch, Arc
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build") + os.sep
os.makedirs(OUT, exist_ok=True)
plt.rcParams["font.family"] = "DejaVu Sans"
INK = "#1f2a33"; WALL = "#2b3640"; GRID = "#d9dee2"; DESK = "#c9d6e2"; DESKE = "#46627a"
WOOD = "#c39b66"; RACE = "#e8590c"; BLE = "#2c4c7c"; MUTE = "#6b7782"; ACC = "#0b6e99"
W, D = 400, 376

def setup(ax, xlim=(-100, 430), ylim=(400, -40)):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")

def room(ax, show_doors=True, fb=True, tvs=True, cabs=True, demo=True):
    # server room (outside the room)
    ax.add_patch(Rectangle((-76, 0), 76, 130, fc="#eef0f2", ec=MUTE, ls=(0, (4, 3)), lw=1, hatch="////", alpha=.55, zorder=0))
    ax.text(-38, 40, "SERVER ROOM\n(76 x 130, not\npart of the room)", ha="center", va="center", fontsize=5.6, color=MUTE)
    pts = [(0, 0), (W, 0), (W, D), (-5, D), (-5, 324), (-76, 324), (-76, 130), (0, 130), (0, 0)]
    ax.add_patch(Polygon(pts, closed=True, fc="#fbfaf7", ec="none", zorder=1))
    # grid every 12 in
    for gx in range(0, W + 1, 48):
        ax.plot([gx, gx], [0, D], color=GRID, lw=.4, zorder=1.1)
    for gz in range(0, D + 1, 48):
        ax.plot([0, W], [gz, gz], color=GRID, lw=.4, zorder=1.1)
    # walls (thick lines) with door gaps
    def wall(p, q, gaps=(), lw=3.2):
        (x1, z1), (x2, z2) = p, q
        L = math.hypot(x2 - x1, z2 - z1); ux, uz = (x2 - x1) / L, (z2 - z1) / L
        cur = 0
        for a, b in sorted(gaps) + [(L, L)]:
            if a > cur:
                ax.plot([x1 + ux * cur, x1 + ux * a], [z1 + uz * cur, z1 + uz * a], color=WALL, lw=lw, solid_capstyle="butt", zorder=5)
            cur = b
    wall((0, 0), (W, 0), [(360, 396)])
    wall((W, 0), (W, D), [(312, 348)])
    wall((W, D), (-5, D))
    wall((-5, D), (-5, 324))
    wall((-5, 324), (-76, 324), [(15 + 0, 51)] if False else [(-5 - (-25), -5 - (-61))])
    wall((-76, 324), (-76, 130))
    wall((-76, 130), (0, 130), [(8, 44)])
    wall((0, 130), (0, 0), [(12, 110)])
    # window glazing on x=0
    ax.plot([0, 0], [20, 118], color="#6fb2d6", lw=2.4, zorder=6)
    ax.text(5, 69, "window", rotation=90, fontsize=5.2, color="#2f7fa6", va="center", ha="left", zorder=6)
    # door labels
    ax.text(378, 12, "door\n36\"", ha="center", va="top", fontsize=5.2, color=ACC)
    ax.text(392, 330, "door\n36\"", ha="right", va="center", fontsize=5.2, color=ACC)
    ax.text(-43, 316, "entry door 36\"", ha="center", va="bottom", fontsize=5.2, color=ACC)
    ax.text(-50, 123, "door 36\"", ha="center", va="bottom", fontsize=5.2, color=ACC)
    if tvs:
        for i in range(3):
            cx = 200 + (i - 1) * 86.1
            ax.add_patch(Rectangle((cx - 37, 0), 74.1, 3.2, fc="#0c0e10", ec="none", zorder=7))
        ax.text(200, 11, "3 x 85\" TV, centers 86\" apart", ha="center", va="top", fontsize=5.4, color=INK)
    if cabs:
        for x0, x1, dem in [(32, 78, False), (78, 114, True), (114, 150, True)]:
            ax.add_patch(Rectangle((x0, 363), x1 - x0, 13, fc=WOOD, ec=INK, lw=.7, zorder=6, hatch="xx" if (dem and demo) else None, alpha=.95))
        ax.add_patch(Rectangle((-5, 346), 36, 30, fc="#a97f4c", ec=INK, lw=.7, zorder=6))
    if fb:
        for x in (114, 186, 258, 330):
            for z in (92, 240):
                ax.add_patch(Circle((x, z), 4.5, fc="#ff7a3d", ec="none", zorder=4))

def dim(ax, p, q, off, text, fs=6.2, side=1):
    (x1, z1), (x2, z2) = p, q
    L = math.hypot(x2 - x1, z2 - z1)
    nx, nz = -(z2 - z1) / L * off, (x2 - x1) / L * off
    a = (x1 + nx, z1 + nz); b = (x2 + nx, z2 + nz)
    ax.plot([x1, a[0]], [z1, a[1]], color=MUTE, lw=.4, zorder=8)
    ax.plot([x2, b[0]], [z2, b[1]], color=MUTE, lw=.4, zorder=8)
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="<|-|>", mutation_scale=5, lw=.6, color=INK, zorder=9))
    mx, mz = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    rot = 0 if abs(z2 - z1) < 1e-6 else 90
    ax.text(mx, mz, text, ha="center", va="center", rotation=rot, fontsize=fs, color=INK, zorder=10,
            bbox=dict(fc="white", ec="none", pad=1.1))

def fig_dimensioned():
    fig, ax = plt.subplots(figsize=(7.6, 6.7)); setup(ax, (-112, 452), (432, -52))
    room(ax)
    # bleacher envelopes
    ax.add_patch(Rectangle((92, 256), 216, 120, fc="none", ec=BLE, lw=1, ls=(0, (5, 3)), zorder=7))
    ax.add_patch(Rectangle((92, 286), 216, 90, fc=BLE, ec="none", alpha=.12, zorder=3))
    ax.text(200, 271, "4 rows at 30\" = 120\" deep (z 256 to 376)", ha="center", va="center", fontsize=5.8, color=BLE)
    ax.text(200, 331, "ASSUMED BLEACHER ZONE\n3 bays x 72\" = 216\" wide, centered on the TVs\n3 rows at 30\" = 90\" deep (shaded)", ha="center", va="center", fontsize=6.2, color=BLE, zorder=8)
    # dimension lines
    dim(ax, (0, 0), (W, 0), -26, "400\" (33'-4\") side wall to side wall")
    dim(ax, (W, 0), (W, D), 22, "376\" (31'-4\")  north wall to south wall")
    dim(ax, (-76, 324), (-76, 130), -16, "194\" alcove")
    dim(ax, (-76, 130), (-76, 0), -16, "130\" server wall")
    dim(ax, (-76, 324), (0, 324), 20, "76\"", side=1)
    dim(ax, (-5, 324), (-5, 376), -34, "52\"")
    # south wall cabinet run
    dim(ax, (-5, 376), (31, 376), 16, "36\"")
    dim(ax, (32, 376), (78, 376), 16, "46\"")
    dim(ax, (78, 376), (114, 376), 16, "36\"")
    dim(ax, (114, 376), (150, 376), 16, "36\"")
    dim(ax, (92, 376), (308, 376), 30, "216\" bleacher width")
    ax.text(15, 358, "tall\ncabinet\n36 x 30", ha="center", va="center", fontsize=5.0, color="white", zorder=9)
    ax.text(55, 369.5, "46", ha="center", va="center", fontsize=5, color=INK, zorder=9)
    ax.text(96, 369.5, "36", ha="center", va="center", fontsize=5, color=INK, zorder=9)
    ax.text(132, 369.5, "36", ha="center", va="center", fontsize=5, color=INK, zorder=9)
    ax.text(-100, 421, "Wall cabinets 13\" deep, 58\" to 85\" above floor (the two hatched 36\" units are the likely removals).\nTall cabinet 85\" high. Ceiling 120\" (10 ft).", fontsize=5.6, color=INK, ha="left", va="center")
    ax.text(300, 60, "orange dots = existing\nfloor boxes (8)", fontsize=5.6, color="#c2541d", ha="center")
    # north arrow
    ax.add_patch(FancyArrowPatch((428, 48), (428, 18), arrowstyle="-|>", mutation_scale=8, lw=1, color=INK))
    ax.text(428, 54, "N", ha="center", va="top", fontsize=7, color=INK, weight="bold")
    ax.text(-110, -44, "Room 413  |  plan view (inches unless noted)", fontsize=8, weight="bold", color=INK, va="center")
    fig.savefig(OUT + "plan_dim.png", dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig_section():
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    ax.set_xlim(236, 420); ax.set_ylim(-6, 128); ax.set_aspect("equal"); ax.axis("off")
    ax.plot([236, 376], [0, 0], color=INK, lw=2)           # floor
    ax.plot([376, 376], [0, 120], color=INK, lw=2.4)       # south wall
    ax.plot([236, 376], [120, 120], color=INK, lw=1.2, ls=(0, (6, 3)))
    ax.text(238, 123, "ceiling 120\"", fontsize=6.4, color=INK, va="bottom")
    ax.add_patch(Rectangle((363, 58), 13, 27, fc=WOOD, ec=INK, lw=.8))
    ax.text(398, 71.5, "wall cabinet\n58\" to 85\"\n(13\" deep)", fontsize=6, ha="center", va="center", color=INK)
    rise, sp = 10.25, 30
    for i in range(4):
        zf = 376 - sp * (4 - i); h = rise * (i + 1)
        ax.add_patch(Rectangle((zf, 0), sp, h, fc="#c3c9ce", ec=INK, lw=.6))
        sx = zf + sp - 9
        ax.add_patch(Rectangle((sx - 2, h + 17), 3, 17, fc=BLE, ec="none"))      # back
        ax.add_patch(Rectangle((sx - 14, h + 16), 16, 2.5, fc=BLE, ec="none"))   # seat
        # seated person
        ax.add_patch(Circle((sx - 7, h + 18 + 31), 5, fc="#e9b78f", ec="none", alpha=.9))
        ax.plot([sx - 7, sx - 7], [h + 18, h + 18 + 26], color="#e9b78f", lw=4, solid_capstyle="round", alpha=.9)
        ax.text(zf + sp / 2, 3, "row %d\n%s\"" % (i + 1, ("%.2f" % h).rstrip("0").rstrip(".")), fontsize=5.4, ha="center", va="bottom", color=INK)
    ax.plot([354, 376], [90, 90], color="#c0392b", lw=.8)
    ax.text(300, 100, "seated head, row 4: about 90\" up\n(illustrative)", fontsize=5.8, color="#c0392b", ha="center")
    ax.text(236 + 2, 30, "front of\nbleacher\nz = 256", fontsize=5.8, color=MUTE)
    fig.savefig(OUT + "section.png", dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ---------- raceway plans ----------
def rad(d): return d * math.pi / 180
def loc(p, lx, lz):
    return (p[0] + lx * math.cos(p[2]) + lz * math.sin(p[2]), p[1] - lx * math.sin(p[2]) + lz * math.cos(p[2]))
def desk(ax, p, fc=DESK, label=None):
    x, z, r = p
    pts = [loc(p, a, b) for a, b in [(-35, -15), (35, -15), (35, 15), (-35, 15)]]
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=DESKE, lw=.8, zorder=6, alpha=.92))
    # screen edge (monitor side = +z edge)
    a, b = loc(p, -30, 12), loc(p, 30, 12)
    ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=1.6, zorder=7, solid_capstyle="butt")
    cx, cz = loc(p, 0, -29)
    ax.add_patch(Circle((cx, cz), 8.5, fc="#fff", ec=DESKE, lw=.6, zorder=6.5))

TEACH_T = (200, 261, math.pi)
TEACH_A = (-12, 165, rad(90))
def class_poses(side=False):
    a = []; sx = [60, 185, 215, 340]; rot = [-90, 90, -90, 90]
    for s in range(4):
        for j in range(3):
            a.append((sx[s], 71 + 70 * j, rad(rot[s])))
    a.append(TEACH_A if side else TEACH_T)
    return a
def comp_poses():
    out = []
    rows = [-70, 0, 70]
    for cx, phi in [(106, rad(56)), (294, -rad(56))]:
        for r in rows:
            out.append((cx + r * math.cos(phi), 140 - r * math.sin(phi), phi))
    out.append(TEACH_A)
    return out

def race(ax, mode):
    # to scale: 8" wide
    def band(x0, z0, x1, z1):
        if z0 == z1:
            ax.add_patch(Rectangle((min(x0, x1), z0 - 4), abs(x1 - x0), 8, fc=RACE, ec="#a63d06", lw=.6, zorder=8))
        else:
            ax.add_patch(Rectangle((x0 - 4, min(z0, z1)), 8, abs(z1 - z0), fc=RACE, ec="#a63d06", lw=.6, zorder=8))
    band(60, 141, 340, 141)       # cross run
    band(200, 141, 200, 240)      # spine south
    # feeder from existing floor box
    ax.plot([186, 200], [240, 240], color=RACE, lw=1.1, ls=(0, (2, 1.6)), zorder=8)
    active = {"class": [(60, 141), (200, 141), (200, 211), (340, 141)],
              "bleach": [(60, 141), (200, 141), (200, 211), (340, 141)],
              "comp": [(106, 141), (294, 141)]}[mode]
    allb = [(60, 141), (200, 141), (200, 211), (340, 141), (106, 141), (294, 141)]
    for b in allb:
        on = b in active
        ax.add_patch(Rectangle((b[0] - 7, b[1] - 7), 14, 14, fc="#ffffff" if not on else "#7a2a00", ec="#7a2a00", lw=1.0, zorder=9))
        if on:
            ax.add_patch(Rectangle((b[0] - 3.2, b[1] - 3.2), 6.4, 6.4, fc="#ffd9c2", ec="none", zorder=10))
    ax.add_patch(Circle((200, 240), 6, fc="#7a2a00", ec="none", zorder=10))
    ax.text(228, 236, "feed from existing\nfloor box (186, 240)", fontsize=5.4, color="#7a2a00", va="center", zorder=11, bbox=dict(fc="white", ec="none", pad=1))

def fig_raceway(mode, title, sub, fname):
    fig, ax = plt.subplots(figsize=(7.6, 6.4)); setup(ax, (-96, 428), (408, -42))
    room(ax, cabs=True, demo=False)
    if mode == "class":
        ps = class_poses(False)
    elif mode == "bleach":
        ps = class_poses(True)
    else:
        ps = comp_poses()
    for i, p in enumerate(ps):
        desk(ax, p, fc="#f3dcc6" if i == len(ps) - 1 and mode != "comp" else DESK)
    if mode == "comp":
        desk(ax, TEACH_A, fc="#f3dcc6")
    if mode in ("bleach", "comp"):
        ax.add_patch(Rectangle((92, 280), 216, 96, fc=BLE, ec=BLE, lw=.9, ls=(0, (5, 3)), alpha=.14, zorder=3))
        ax.text(200, 328, "bleachers out (as modeled: 4 rows x 24\")", ha="center", va="center", fontsize=6.4, color=BLE, zorder=4)
    race(ax, mode)
    if mode == "comp":
        ax.text(200, 100, "aisle", ha="center", fontsize=6, color=MUTE, style="italic")
        ax.text(-38, 250, "6 extra desks\nroll to the\nserver room", ha="center", va="center", fontsize=5.8, color=MUTE, zorder=3)
    ax.text(-94, -34, title, fontsize=9, weight="bold", color=INK, va="center")
    ax.text(-94, -22, sub, fontsize=6.3, color=MUTE, va="center")
    # legend
    lx, lz = -70, 396
    ax.add_patch(Rectangle((lx, lz - 4 + 0), 26, 8, fc=RACE, ec="#a63d06", lw=.6, zorder=8)); ax.text(lx + 31, lz + 4, "raceway, 8\" wide, to scale", fontsize=5.8, va="center")
    ax.add_patch(Rectangle((lx + 138, lz - 3), 10, 10, fc="#7a2a00", ec="#7a2a00")); ax.text(lx + 152, lz + 3, "device box in use", fontsize=5.8, va="center")
    ax.add_patch(Rectangle((lx + 216, lz - 3), 10, 10, fc="#fff", ec="#7a2a00")); ax.text(lx + 230, lz + 3, "blanked this layout", fontsize=5.8, va="center")
    ax.plot([lx + 316, lx + 330], [lz + 2, lz + 2], color=INK, lw=1.6); ax.text(lx + 334, lz + 3, "screen side", fontsize=5.8, va="center")
    fig.savefig(OUT + fname, dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

if __name__ == "__main__":
    fig_dimensioned(); fig_section()
    fig_raceway("class", "Layout 1: Class", "Bleachers folded. Teacher desk T'd onto the south end of the center stack.", "race_class.png")
    fig_raceway("bleach", "Layout 2: Class + bleachers out", "Teacher desk moves to the alcove; the student layout is unchanged.", "race_bleach.png")
    fig_raceway("comp", "Layout 3: Competition", "Two 1x3 team rows at 56 degrees, 46\" aisle; extra desks leave the room.", "race_comp.png")
    print("ok")
