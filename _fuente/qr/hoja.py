"""Printable letter-size sheet of the QR in several sizes, with crop marks.

Sizes are the cut square, quiet zone included. Vector output.
Run: python hoja.py  (needs segno + reportlab)
"""
from pathlib import Path
import segno
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
URL = "https://paola.iatelier.org"
qr = segno.make(URL, error="h")
matrix = [list(row) for row in qr.matrix]
n = len(matrix)
BORDER = 4  # quiet zone in modules

TINTA, PAPEL = HexColor("#3a2f28"), HexColor("#f4ecdd")
NEGRO, BLANCO = HexColor("#000000"), HexColor("#ffffff")
MARCA = HexColor("#999999")

def draw_qr(c, x, y, size, dark, light):
    total = n + 2 * BORDER
    m = size / total
    c.setFillColor(light)
    c.rect(x, y, size, size, stroke=0, fill=1)
    # one filled path for all modules, so viewers don't show seams between squares
    c.setFillColor(dark)
    path = c.beginPath()
    for r, row in enumerate(matrix):
        for col, v in enumerate(row):
            if v:
                path.rect(x + (col + BORDER) * m, y + size - (r + BORDER + 1) * m, m, m)
    c.drawPath(path, stroke=0, fill=1, fillMode=1)
    # crop marks just outside each corner
    c.setStrokeColor(MARCA)
    c.setLineWidth(0.3)
    g, L = 0.12 * cm, 0.45 * cm
    for cx, sx in ((x, -1), (x + size, 1)):
        for cy, sy in ((y, -1), (y + size, 1)):
            c.line(cx + sx * g, cy, cx + sx * (g + L), cy)
            c.line(cx, cy + sy * g, cx, cy + sy * (g + L))

W, H = letter
out = HERE / "paola-qr-imprimir.pdf"
c = canvas.Canvas(str(out), pagesize=letter)
c.setTitle("QR · paola.iatelier.org")

margin = 2 * cm
yy = H - margin
c.setFillColor(TINTA)
c.setFont("Helvetica", 9)
c.drawString(margin, yy, "QR para la postal  ·  " + URL + "  ·  imprimir al 100% (sin ajustar a página) y cortar por las marcas")
yy -= 1.2 * cm

rows = [  # (size cm, copies, dark, light, label)
    (2.5, 4, TINTA, PAPEL, "2.5 cm · tinta sobre papel"),
    (3.0, 4, TINTA, PAPEL, "3 cm · tinta sobre papel"),
    (4.0, 3, TINTA, PAPEL, "4 cm · tinta sobre papel"),
    (3.0, 4, NEGRO, BLANCO, "3 cm · blanco y negro"),
]
gap = 1.4 * cm
for size_cm, copies, dark, light, label in rows:
    s = size_cm * cm
    c.setFillColor(HexColor("#666666"))
    c.setFont("Helvetica", 7.5)
    c.drawString(margin, yy, label)
    yy -= 0.95 * cm + s
    x = margin
    for _ in range(copies):
        draw_qr(c, x, yy, s, dark, light)
        x += s + gap
    yy -= 1.05 * cm

# 1 cm reference to check print scale
margin = 1.4 * cm
c.setStrokeColor(TINTA); c.setLineWidth(0.6)
c.line(margin, margin, margin + cm, margin)
c.line(margin, margin - 0.1 * cm, margin, margin + 0.1 * cm)
c.line(margin + cm, margin - 0.1 * cm, margin + cm, margin + 0.1 * cm)
c.setFont("Helvetica", 7); c.setFillColor(HexColor("#666666"))
c.drawString(margin + 1.3 * cm, margin - 0.08 * cm, "1 cm (mídelo para confirmar que imprimió a escala)")
c.save()
print(out, round(yy / cm, 1), "cm left at bottom")
