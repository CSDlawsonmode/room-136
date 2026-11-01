import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, FancyBboxPatch, FancyArrowPatch, Polygon
from figs import room, setup, dim, OUT, INK, MUTE, ACC, BLE, WALL

PANEL = "#f2c230"; PANEL_E = "#8a6a00"; ACCENT = "#c2189a"
ZONES = [("A  Screen zone", 0, 110, "#2f7fa6"), ("B  Desk zone", 110, 270, "#6a8f3a"), ("C  Rear / seating zone", 270, 376, "#a05a9a")]

def title(ax, t, sub):
    ax.text(-94, -50, t, fontsize=9, weight="bold", color=INK, va="center")
    ax.text(-94, -38, sub, fontsize=6.3, color=MUTE, va="center")

def fig_lighting():
    fig, ax = plt.subplots(figsize=(7.6, 6.6)); setup(ax, (-96, 428), (418, -58))
    room(ax, fb=False, cabs=True, demo=False)
    for name, z0, z1, c in ZONES:
        ax.add_patch(Rectangle((0, z0), 400, z1 - z0, fc=c, ec="none", alpha=.07, zorder=2))
        ax.text(396, z0 + 9, name, ha="right", va="center", fontsize=5.8, color=c, weight="bold", zorder=3)
    ax.add_patch(Rectangle((-76, 130), 76, 194, fc="#6a8f3a", ec="none", alpha=.07, zorder=2))
    ax.text(-38, 140, "D  Alcove", ha="center", va="center", fontsize=5.8, color="#6a8f3a", weight="bold", zorder=3)
    # TV gradient strips: glow on the wall behind each TV
    for i, c in enumerate(["#16a9c9", "#7b4bd1", "#e0457b"]):
        cx = 200 + (i - 1) * 86.1
        ax.add_patch(Rectangle((cx - 40, -9), 80.1, 9, fc=c, ec="none", alpha=.55, zorder=7))
    ax.text(200, -14, "3 x Hue Play gradient strip, 85\" size, behind the TVs", ha="center", va="bottom", fontsize=5.6, color=INK)
    # general lighting panels, indicative 4 x 4 grid plus 2 in the alcove
    for x in (50, 150, 250, 350):
        for z in (45, 135, 225, 315):
            ax.add_patch(Rectangle((x - 24, z - 6), 48, 12, fc=PANEL, ec=PANEL_E, lw=.7, zorder=8))
    for z in (190, 270):
        ax.add_patch(Rectangle((-44, z - 24), 12, 48, fc=PANEL, ec=PANEL_E, lw=.7, zorder=8))
    # reactive accent lights (synced with the center screen)
    acc = [(35, 9), (335, 9), (-70, 230), (393, 150), (393, 250), (200, 369)]
    for i, (x, z) in enumerate(acc):
        ax.add_patch(Circle((x, z), 6, fc=ACCENT, ec="white", lw=.8, zorder=10))
        ax.text(x, z, str(i + 1), ha="center", va="center", fontsize=5, color="white", weight="bold", zorder=11)
    ax.add_patch(Rectangle((176, 24), 48, 10, fc="#2b3640", ec="none", zorder=9))
    ax.text(200, 29, "sync box", ha="center", va="center", fontsize=4.8, color="white", zorder=10)
    # legend
    lx, lz = -86, 395
    ax.add_patch(Rectangle((lx, lz - 5), 24, 10, fc=PANEL, ec=PANEL_E, lw=.7)); ax.text(lx + 30, lz, "Hue-ready ceiling panel, 48 x 12\" (18 shown)", fontsize=5.8, va="center")
    ax.add_patch(Circle((lx + 214, lz), 6, fc=ACCENT, ec="white")); ax.text(lx + 224, lz, "reactive accent light, 1 to 6 (synced)", fontsize=5.8, va="center")
    ax.text(lx, lz + 14, "Panel count and positions are design intent only; the bidder's photometric layout governs. Accent positions assume wall-mounted color bars or strips.", fontsize=5.2, color=MUTE, va="center")
    title(ax, "Phase 2: Lighting concept", "Zones are separately dimmable. Room 136, plan view, inches. Accent lights and strips share one Hue entertainment area (10-light limit).")
    fig.savefig(OUT + "bid_lighting.png", dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig_audio():
    fig, ax = plt.subplots(figsize=(7.6, 6.6)); setup(ax, (-96, 428), (418, -58))
    room(ax, fb=False, cabs=True, demo=False)
    ax.add_patch(Ellipse((200, 150), 330, 170, fc="#6a8f3a", ec="#6a8f3a", alpha=.09, ls=(0, (5, 3)), zorder=2))
    ax.text(200, 152, "primary listening area (desk zone)", ha="center", va="center", fontsize=6.2, color="#46702a", zorder=3)
    ax.add_patch(Rectangle((92, 256), 216, 120, fc=BLE, ec=BLE, lw=.8, ls=(0, (5, 3)), alpha=.08, zorder=2))
    ax.text(200, 360, "bleacher zone (Phase 4)", ha="center", va="center", fontsize=5.8, color=BLE, zorder=3)
    def sp(x, z, mk, c, lab, dx=0, dz=0, ha="center", s=70, fc=None):
        ax.scatter([x], [z], marker=mk, s=s, c=fc or c, edgecolors=c, linewidths=1, zorder=10)
        ax.text(x + dx, z + dz, lab, ha=ha, va="center", fontsize=5.6, color=INK, zorder=11, bbox=dict(fc="white", ec="none", pad=.8, alpha=.85))
    sp(58, 8, "s", BLE, "L", 0, 17); sp(342, 8, "s", BLE, "R", 0, 17)
    ax.add_patch(Rectangle((178, 3), 44, 9, fc=BLE, ec="none", zorder=10)); ax.text(200, 30, "C (under center TV)", ha="center", va="center", fontsize=5.6, color=INK, zorder=11, bbox=dict(fc="white", ec="none", pad=.8, alpha=.85))
    sp(22, 22, "s", "#111", "SUB", 14, 11, ha="left", s=110, fc="#111")
    sp(386, 100, "s", "#111", "SUB 2 (alt)", -9, 0, ha="right", s=90, fc="white")
    sp(-70, 195, "^", "#b3541e", "SL (alcove wall)", 8, 0, ha="left"); sp(392, 195, "^", "#b3541e", "SR", -15, 0)
    sp(62, 369, "^", "#b3541e", "RL", 0, -14); sp(338, 369, "^", "#b3541e", "RR", 0, -14)
    for x, z, lab in [(100, 110, "TFL"), (300, 110, "TFR"), (100, 260, "TRL"), (300, 260, "TRR")]:
        sp(x, z, "o", "#c0392b", lab, 0, 14, fc="white")
    for x in (100, 300):
        ax.scatter([x], [185], marker="o", s=55, c="white", edgecolors="#c0392b", linewidths=.9, linestyle="dashed", zorder=10)
    ax.text(200, 214, "dashed pair: optional middle overheads (7.1.6)", ha="center", va="center", fontsize=5.2, color="#c0392b", zorder=11)
    dim(ax, (100, 110), (100, 260), 30, "150\"", fs=5.4)
    dim(ax, (100, 110), (300, 110), -26, "200\"", fs=5.4)
    lx, lz = -86, 395
    ax.scatter([lx + 6], [lz], marker="s", s=60, c=BLE); ax.text(lx + 16, lz, "front / center", fontsize=5.8, va="center")
    ax.scatter([lx + 80], [lz], marker="s", s=70, c="#111"); ax.text(lx + 90, lz, "subwoofer", fontsize=5.8, va="center")
    ax.scatter([lx + 140], [lz], marker="^", s=60, c="#b3541e"); ax.text(lx + 150, lz, "side / rear surround (wall)", fontsize=5.8, va="center")
    ax.scatter([lx + 262], [lz], marker="o", s=60, c="white", edgecolors="#c0392b", linewidths=1); ax.text(lx + 272, lz, "overhead (ceiling)", fontsize=5.8, va="center")
    ax.text(lx, lz + 18, "Indicative 7.1.4 layout. The west side has no wall beside the desk zone (open alcove), so SL is shown on the alcove wall;\nbidder to propose a balanced solution. Verify against wall and ceiling construction, the cabinets and the Phase 4 bleachers; heights shown at 45 degrees from the middle of the desk zone.", fontsize=5.2, color=MUTE, va="center")
    title(ax, "Phase 3: Dolby Atmos 7.1.4 concept", "Room 136, plan view, inches. L/C/R on the north wall with the three 85 in. TVs; overheads in the 10 ft ceiling.")
    fig.savefig(OUT + "bid_audio.png", dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

def box(ax, x, y, w, h, t, fc="#eef2f5", ec=INK, fs=6.3, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2", fc=fc, ec=ec, lw=.9, zorder=3))
    ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=fs, color=INK, zorder=4, weight="bold" if bold else "normal", linespacing=1.35)

def arrow(ax, p, q, c=INK, ls="-", label=None, lp=(0, 0), fs=5.3):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=7, lw=.9, color=c, ls=ls, zorder=2))
    if label:
        ax.text((p[0] + q[0]) / 2 + lp[0], (p[1] + q[1]) / 2 + lp[1], label, ha="center", va="center", fontsize=fs, color=c, zorder=5, bbox=dict(fc="white", ec="none", pad=.6))

def fig_flow():
    fig, ax = plt.subplots(figsize=(7.6, 4.0)); ax.set_xlim(0, 100); ax.set_ylim(0, 52); ax.axis("off")
    box(ax, 1, 36, 17, 13, "Sources\nteacher PC, game\nconsole, streamer", fc="#f6efe3")
    box(ax, 26, 36, 19, 13, "AV receiver /\nprocessor\nDolby Atmos, 11+ ch", fc="#e4eef7", bold=True)
    box(ax, 54, 36, 18, 13, "Hue Play HDMI\nsync box 8K", fc="#f7e4f0", bold=True)
    box(ax, 80, 36, 19, 13, "Center 85\" TV\n(main screen)", fc="#eef2f5")
    arrow(ax, (18.8, 42.5), (25.2, 42.5), label="HDMI", lp=(0, 3))
    arrow(ax, (45.8, 42.5), (53.2, 42.5), label="HDMI", lp=(0, 3))
    arrow(ax, (72.8, 42.5), (79.2, 42.5), label="HDMI", lp=(0, 3))
    box(ax, 21, 16, 28, 11, "11+ speakers: L C R, 2 side, 2 rear,\n4 overhead, subwoofer(s)", fc="#e8efe0")
    arrow(ax, (35.5, 35.2), (35.5, 27.8), c="#46702a", label="speaker wire", lp=(10, 0))
    box(ax, 54, 16, 18, 11, "Hue Bridge Pro\n(Zigbee hub)", fc="#f7e4f0", bold=True)
    arrow(ax, (63, 35.2), (63, 27.8), c=ACCENT, ls=(0, (3, 2)), label="LAN", lp=(5.5, 0))
    box(ax, 78, 12, 21, 19, "Hue lights\n3 gradient strips\n6 accent lights\nceiling panels (zones)", fc="#fbf3d4")
    arrow(ax, (72.8, 21.5), (77.2, 21.5), c=ACCENT, ls=(0, (3, 2)), label="Zigbee", lp=(0, 3.4))
    box(ax, 1, 1, 98, 6.5, "District network (Ethernet): bridge, sync box and AV receiver each need a wired port; district IT provides ports, VLAN and DHCP", fc="#f1f3f4", ec=MUTE, fs=5.8)
    ax.text(1, 12, "Left and right 85\" TVs take their\nown HDMI feeds (not shown). Their\nbacklights follow the center screen.", fontsize=5.5, color=MUTE, va="center")
    fig.savefig(OUT + "bid_flow.png", dpi=240, bbox_inches="tight", facecolor="white"); plt.close(fig)

if __name__ == "__main__":
    fig_lighting(); fig_audio(); fig_flow()
    print("bid figs ok")
