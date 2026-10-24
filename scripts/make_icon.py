"""Render images/icon.png: a cocoa mug with syntax-colored steam on espresso.

Pure stdlib. Each shape is a signed distance field; coverage = clamp(0.5 - d)
gives one-pixel anti-aliasing without supersampling.

    python3 scripts/make_icon.py
"""
import math
import struct
import zlib
from pathlib import Path

SIZE = 256
OUT = Path(__file__).resolve().parent.parent / "images" / "icon.png"


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


BG_TOP, BG_BOTTOM = hexrgb("#241a17"), hexrgb("#140e0c")
SAND, SAND_SHADE, RIM = hexrgb("#d4b99a"), hexrgb("#c4a684"), hexrgb("#e3cdb0")
WALNUT = hexrgb("#5c4033")
STEAM = [("#c4978c", 89, 0.0), ("#a3b08a", 113, 0.7), ("#8aaec2", 137, 1.4)]  # rose, sage, blue


def clamp(v):
    return 0.0 if v < 0 else 1.0 if v > 1 else v


def cov(d):
    return clamp(0.5 - d)


def sd_round_rect(x, y, x0, y0, x1, y1, r):
    cx, cy, hw, hh = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 - r, (y1 - y0) / 2 - r
    qx, qy = abs(x - cx) - hw, abs(y - cy) - hh
    return math.hypot(max(qx, 0), max(qy, 0)) + min(max(qx, qy), 0) - r


def sd_ellipse(x, y, cx, cy, rx, ry):
    return (math.hypot((x - cx) / rx, (y - cy) / ry) - 1) * min(rx, ry)


def sd_segment(x, y, ax, ay, bx, by):
    px, py, dx, dy = x - ax, y - ay, bx - ax, by - ay
    t = clamp((px * dx + py * dy) / (dx * dx + dy * dy))
    return math.hypot(px - dx * t, py - dy * t)


def polyline_dist(x, y, pts):
    return min(sd_segment(x, y, *pts[i], *pts[i + 1]) for i in range(len(pts) - 1))


# Steam: gentle sine wisps rising from the cocoa, each carrying its own t for the fade.
wisps = []
for color, x0, phase in STEAM:
    pts = []
    for i in range(25):
        t = i / 24
        pts.append((x0 + 7 * math.sin(t * 2 * math.pi + phase), 98 - 60 * t, t))
    wisps.append((hexrgb(color), pts))

# Snowflake on the mug: three crossing arms with a small V near each tip.
SNOW_C, ARM = (113, 160), 19
snow = []
for k in range(6):
    a = k * math.pi / 3
    ux, uy = math.cos(a), math.sin(a)
    tip = (SNOW_C[0] + ux * ARM, SNOW_C[1] + uy * ARM)
    snow.append((SNOW_C, tip))
    bx, by = SNOW_C[0] + ux * ARM * 0.6, SNOW_C[1] + uy * ARM * 0.6
    for s in (-1, 1):
        b = a + s * math.pi / 4
        snow.append(((bx, by), (bx + math.cos(b) * 7, by + math.sin(b) * 7)))


def over(dst, color, a):
    return tuple(d * (1 - a) + c * a for d, c in zip(dst, color))


def pixel(x, y):
    tile = cov(sd_round_rect(x, y, 0, 0, SIZE, SIZE, 56))
    if tile == 0:
        return (0, 0, 0, 0)
    c = over(BG_TOP, BG_BOTTOM, y / SIZE)

    # Soft shadow under the mug
    c = over(c, (0, 0, 0), 0.35 * clamp(-sd_ellipse(x, y, 118, 206, 66, 9) / 6))

    # Handle: right half of a ring, drawn first so the body overlaps the joint
    ring = max(abs(math.hypot(x - 165, y - 154) - 21) - 7, 165 - x)
    c = over(c, SAND_SHADE, cov(ring))

    # Body: flat-topped, rounded at the bottom, with a shaded right side
    body = max(sd_round_rect(x, y, 59, 90, 167, 202, 26), 116 - y)
    b = cov(body)
    c = over(c, SAND, b)
    c = over(c, SAND_SHADE, b * clamp(x - 140 + 0.5))

    # Rim and cocoa surface
    c = over(c, RIM, cov(sd_ellipse(x, y, 113, 116, 54, 13)))
    c = over(c, WALNUT, cov(sd_ellipse(x, y, 113, 117, 46, 9)))

    # Snowflake
    if abs(x - SNOW_C[0]) < 30 and abs(y - SNOW_C[1]) < 30:
        d = min(sd_segment(x, y, *a, *b) for a, b in snow) - 2.6
        c = over(c, WALNUT, cov(d))

    # Steam, fading toward the top
    if 30 < y < 106 and 70 < x < 156:
        for color, pts in wisps:
            best, bt = 1e9, 0
            for i in range(len(pts) - 1):
                d = sd_segment(x, y, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])
                if d < best:
                    best, bt = d, pts[i][2]
            a = cov(best - 4.5) * (1 - 0.75 * bt * bt)
            c = over(c, color, a)

    return (*c, tile)


def write_png(path, rows):
    raw = b"".join(b"\x00" + bytes(round(v * 255) for px in row for v in px) for row in rows)

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"\x89PNG\r\n\x1a\n"
                     + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 6, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(raw, 9))
                     + chunk(b"IEND", b""))


if __name__ == "__main__":
    write_png(OUT, [[pixel(x + 0.5, y + 0.5) for x in range(SIZE)] for y in range(SIZE)])
    print(OUT)
