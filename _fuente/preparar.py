"""Build web assets from the source painting: scene image (webp + jpg) and wind mask.

The wind mask is grayscale: white = moves with the wind, black = still.
Run: python3 _fuente/preparar.py  (from the project root)
"""
from pathlib import Path
import colorsys
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
src = Image.open(ROOT / "_fuente/escena-original.jpg").convert("RGB")
out = ROOT / "img"
out.mkdir(exist_ok=True)

# Scene for the shader and for link previews
src.save(out / "escena.webp", quality=86, method=6)
src.resize((1200, round(1200 * src.height / src.width)), Image.LANCZOS).save(out / "og.jpg", quality=84)

# Wind mask at half resolution
W, H = src.width // 2, src.height // 2
small = src.resize((W, H), Image.LANCZOS)
px = small.load()
mask = Image.new("L", (W, H))
mp = mask.load()

def smooth(a, b, x):
    t = min(max((x - a) / (b - a), 0.0), 1.0)
    return t * t * (3 - 2 * t)

for y in range(H):
    fy = y / H
    for x in range(W):
        fx = x / W
        r, g, b = (c / 255 for c in px[x, y])
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        hd = h * 360
        m = 0.0
        if s > 0.22 and 15 <= hd <= 60 and v > 0.45 and fy < 0.6:  # autumn leaves (lit windows sit lower)
            m = smooth(0.22, 0.45, s)
        elif s > 0.18 and 60 < hd <= 150 and v > 0.25:    # green trees and bushes
            m = 0.7 * smooth(0.18, 0.4, s)
        # thin dark branches inside the big tree crown
        if fx < 0.48 and fy < 0.55 and v < 0.5 and s < 0.6:
            m = max(m, 0.6)
        # anchor: crowns sway, trunks and ground barely move
        if fx < 0.48:
            m *= 1.0 - 0.85 * smooth(0.30, 0.72, fy)
        else:
            m *= 1.0 - 0.6 * smooth(0.55, 0.95, fy)
        mp[x, y] = int(255 * min(m, 1.0))

mask = mask.filter(ImageFilter.GaussianBlur(6))
mask.save(out / "viento.png", optimize=True)
print("ok", (out / "escena.webp").stat().st_size // 1024, "KB scene,",
      (out / "viento.png").stat().st_size // 1024, "KB mask")
