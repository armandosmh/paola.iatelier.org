"""Map for the guide: watercolor raster base + SVG overlay.

Geometry for the river, rail lines and Kyu-Yamate-dori comes from OpenStreetMap
(osm.json, cached Overpass result; see fetch query below). Station and T-Site
points come from Nominatim. The suggested river walk is hand-drawn on top.

Output (next to this script):
  mapa-base.png  watercolor washes (river, trees, T-Site glow)
  mapa.svg       crisp lines, stations, labels, red-thread walking route

Refresh osm.json (only if needed) with this Overpass query:
  [out:json];(way["waterway"="river"]["name"="目黒川"](BBOX);
   way["highway"]["name"="旧山手通り"](BBOX);way["railway"~"rail|subway"](BBOX););out tags geom;
"""
from pathlib import Path
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
W, H = 1420, 1060
LON0, LON1 = 139.6800, 139.7160
LAT0, LAT1 = 35.6375, 35.6600


def xy(lat, lon):
    x = (lon - LON0) / (LON1 - LON0) * W
    y = (LAT1 - lat) / (LAT1 - LAT0) * H
    return round(x, 1), round(y, 1)


P = {
    "shibuya": xy(35.6580, 139.7016),
    "ebisu": xy(35.6467, 139.7100),
    "daikanyama": xy(35.64812, 139.70322),
    "tsite": xy(35.64926, 139.69983),
    "nakameguro": xy(35.64434, 139.69905),
}

ways = json.loads((HERE / "osm.json").read_text(encoding="utf-8"))["elements"]


def lines(pred):
    return [[xy(g["lat"], g["lon"]) for g in w["geometry"]] for w in ways if pred(w["tags"])]


RIVER = lines(lambda t: t.get("name") == "目黒川" and t.get("tunnel") != "culvert")
YAMANOTE = lines(lambda t: t.get("name") == "山手線")
TOYOKO = lines(lambda t: t.get("name") == "東急東横線")
HIBIYA_UP = lines(lambda t: t.get("name") == "東京メトロ日比谷線" and t.get("tunnel") != "yes")
HIBIYA_TUN = lines(lambda t: t.get("name") == "東京メトロ日比谷線" and t.get("tunnel") == "yes")
YAMATE_DORI = lines(lambda t: t.get("name") == "旧山手通り")

# The river comes as one long way; keep its points in order.
river_pts = max(RIVER, key=len)

# Suggested walk: Naka-meguro station → river → upstream → up the hill to
# T-Site. The climb is a suggestion, not a specific street.
def nearest(seq, p):
    return min(range(len(seq)), key=lambda i: (seq[i][0] - p[0]) ** 2 + (seq[i][1] - p[1]) ** 2)

i_start = nearest(river_pts, P["nakameguro"])
i_turn = nearest(river_pts, xy(35.6482, 139.6905))
lo, hi = sorted((i_start, i_turn))
upstream = river_pts[lo:hi + 1]
if nearest(upstream, P["nakameguro"]) != 0:
    upstream = upstream[::-1]
PASEO = [P["nakameguro"]] + upstream + [xy(35.6490, 139.6935), xy(35.6494, 139.6965), P["tsite"]]
DIRECTO = [P["daikanyama"], xy(35.64755, 139.70175), xy(35.6488, 139.6999), P["tsite"]]


# ---------- watercolor raster ----------
rng = np.random.default_rng(7)


def noise(scale, seed):
    r = np.random.default_rng(seed)
    small = Image.fromarray((r.random((H // scale + 2, W // scale + 2)) * 255).astype("uint8"))
    return np.asarray(small.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(scale / 3)),
                      dtype=float) / 255


def shape(draw_fn, blur=3):
    im = Image.new("L", (W, H), 0)
    draw_fn(ImageDraw.Draw(im))
    return np.asarray(im.filter(ImageFilter.GaussianBlur(blur)), dtype=float) / 255


def wash(base, m, color, strength, seed):
    n = 0.55 + 0.45 * noise(60, seed) * (0.7 + 0.3 * noise(12, seed + 1))
    soft = np.asarray(Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(7)),
                      dtype=float) / 255
    edge = np.clip(m - soft, 0, 1)
    a = np.clip(m * n * strength + edge * 0.9 * strength, 0, 1)[..., None]
    c = np.array(color, dtype=float)
    return base * (1 - a) + base * (c / 255) * a  # multiply, like pigment on paper


img = np.ones((H, W, 3)) * np.array([244, 236, 221], dtype=float)
img *= (0.97 + 0.03 * noise(4, 1))[..., None]  # paper tooth

# Daikanyama sits on a ridge above the river
tx, ty = P["tsite"]
hill = shape(lambda d: d.ellipse([tx - 260, ty - 330, tx + 330, ty + 160], fill=255), 60)
img = wash(img, hill, (226, 196, 150), 0.35, 3)

river = shape(lambda d: [d.line(s, fill=255, width=24, joint="curve") for s in RIVER], 4)
img = wash(img, river, (120, 150, 165), 0.85, 5)


def trees(d):
    for (x0, y0), (x1, y1) in zip(river_pts, river_pts[1:]):
        seg = np.hypot(x1 - x0, y1 - y0)
        nx, ny = -(y1 - y0) / (seg or 1), (x1 - x0) / (seg or 1)
        for t in np.linspace(0, 1, max(1, int(seg // 44))):
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            for side in (-1, 1):
                r = rng.uniform(7, 12)
                off = side * rng.uniform(20, 28)
                cx, cy = x + nx * off, y + ny * off
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)



glow = shape(lambda d: d.ellipse([tx - 70, ty - 55, tx + 70, ty + 55], fill=255), 14)
img = wash(img, glow, (212, 137, 58), 0.9, 11)

Image.fromarray(np.clip(img, 0, 255).astype("uint8")).save(HERE / "mapa-base.png")


# ---------- SVG overlay ----------
FONT = 'font-family="Shippori Mincho"'


def pts(seq):
    return " ".join(f"{x},{y}" for x, y in seq)


def polys(seqs, attrs):
    return "\n".join(f'<polyline points="{pts(s)}" fill="none" {attrs}/>' for s in seqs)


def label(x, y, text, size, fill="#7a6a5c", anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" {FONT} font-size="{size}" fill="{fill}" {extra}>{text}</text>'


def station(key, ja, es, dx, dy, anchor="start"):
    x, y = P[key]
    return (f'<circle cx="{x}" cy="{y}" r="12" fill="#f4ecdd" stroke="#3a2f28" stroke-width="3"/>'
            + label(x + dx, y + dy, es, 40, "#3a2f28", anchor, 'font-weight="600"')
            + label(x + dx, y + dy + 36, ja, 31, "#7a6a5c", anchor))


rx, ry = river_pts[nearest(river_pts, xy(35.6470, 139.6925))]
scale_px = round(500 / ((LON1 - LON0) * 111320 * np.cos(np.radians(35.65))) * W)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
{polys(YAMATE_DORI, 'stroke="#b9a68e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"')}
{polys(YAMANOTE, 'stroke="#7fae4e" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"')}
{polys(HIBIYA_TUN, 'stroke="#9a9a92" stroke-width="5" stroke-dasharray="10 9"')}
{polys(HIBIYA_UP, 'stroke="#9a9a92" stroke-width="5"')}
{polys(TOYOKO, 'stroke="#c23b4a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"')}
{label(rx - 250, ry + 70, "目黒川 · río Meguro", 34, "#5f7f8c", "start", f'font-style="italic" letter-spacing="3" transform="rotate(32 {rx} {ry})"')}
{label(xy(35.6545, 139.6929)[0] + 18, xy(35.6545, 139.6929)[1], "旧山手通り", 29)}
{label(xy(35.6530, 139.7085)[0] + 14, xy(35.6530, 139.7085)[1], "JR Yamanote", 29, "#6d9440")}
{label(xy(35.6530, 139.7044)[0] - 14, xy(35.6530, 139.7044)[1], "Tōkyū Tōyoko", 29, "#a8323f", "end")}
{label(xy(35.6418, 139.7080)[0], xy(35.6418, 139.7080)[1], "Metro Hibiya (bajo tierra)", 29, "#7d7d76", "middle")}
{station("shibuya", "渋谷", "Shibuya", 22, -4)}
{station("ebisu", "恵比寿", "Ebisu", 22, 12)}
{station("daikanyama", "代官山", "Daikanyama", 24, 42)}
{station("nakameguro", "中目黒", "Naka-meguro", -24, 50, "end")}
<g transform="translate({tx},{ty})">
  <path d="M0 -40 C 16 -40 26 -27 26 -14 C 26 7 0 26 0 26 C 0 26 -26 7 -26 -14 C -26 -27 -16 -40 0 -40 Z" fill="#c0392b"/>
  {label(0, -6, "T", 26, "#f4ecdd", "middle", 'font-weight="600"')}
</g>
{label(tx - 40, ty - 92, "T-Site", 50, "#3a2f28", "end", 'font-weight="600"')}
{label(tx - 40, ty - 54, "代官山 蔦屋書店", 31, "#7a6a5c", "end")}
<g transform="translate({W - 90},{90})">
  <path d="M0 -42 L14 0 L0 -9 L-14 0 Z" fill="#3a2f28"/>{label(0, 36, "N", 34, "#3a2f28", "middle", 'font-weight="600"')}
</g>
<g transform="translate(60,{H - 60})">
  <line x1="0" y1="0" x2="{scale_px}" y2="0" stroke="#3a2f28" stroke-width="3"/>
  {label(0, -14, "500 m · unos 6 min a pie", 29)}
</g>
{label(W - 24, H - 22, "© OpenStreetMap", 22, "#9a8a7a", "end")}
</svg>'''
(HERE / "mapa.svg").write_text(svg, encoding="utf-8")
print("map ok")
