"""Build the guide PDF: map → inline SVG into guia.html → pdf/como-llegar.pdf.

Run from anywhere: python3 _fuente/pdf/build.py
Needs: weasyprint, pillow, numpy. Fonts load from Google Fonts (needs network).
"""
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image
from weasyprint import HTML

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "pdf" / "como-llegar.pdf"

# Cover: a lighter JPEG of the landing painting, so the PDF stays small for phones.
cover = Image.open(HERE.parent.parent / "img" / "escena.webp").convert("RGB")
cover.thumbnail((1400, 1400))
cover.save(HERE / "_portada.jpg", quality=82)

subprocess.run([sys.executable, str(HERE / "mapa.py")], check=True)
svg = (HERE / "mapa.svg").read_text(encoding="utf-8")
html = (HERE / "guia.html").read_text(encoding="utf-8")


def inline(m):
    # WeasyPrint can't use web fonts inside an <img> SVG, so the map goes inline.
    return re.sub(r'width="\d+" height="\d+"', f'style="{m.group(1) or ""}"', svg, count=1)


html = re.sub(r'<img src="mapa.svg" alt=""(?: style="([^"]*)")?>', inline, html)
render = HERE / "_render.html"
render.write_text(html, encoding="utf-8")
OUT.parent.mkdir(exist_ok=True)
HTML(render).write_pdf(OUT)
print(OUT.relative_to(HERE.parent.parent))
