import os
import matplotlib
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# matplotlib ships DejaVu Sans, so the PDFs build the same on Windows, macOS and Linux
FONTS = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONTS, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVB", os.path.join(FONTS, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB")
INK = colors.HexColor("#1f2a33"); MUTE = colors.HexColor("#5b6670"); ACC = colors.HexColor("#0b6e99"); LINE = colors.HexColor("#cfd6dc")
H1 = ParagraphStyle("h1", fontName="DVB", fontSize=15, leading=19, textColor=INK, spaceAfter=3)
H2 = ParagraphStyle("h2", fontName="DVB", fontSize=10.5, leading=14, textColor=INK, spaceBefore=9, spaceAfter=3)
B = ParagraphStyle("b", fontName="DV", fontSize=8.6, leading=12.2, textColor=INK, spaceAfter=3)
S = ParagraphStyle("s", fontName="DV", fontSize=7.4, leading=10.2, textColor=MUTE, spaceAfter=2)
BL = ParagraphStyle("bl", parent=B, leftIndent=11, bulletIndent=1, spaceAfter=2)
TC = ParagraphStyle("tc", fontName="DV", fontSize=7.8, leading=10.6, textColor=INK)
TH = ParagraphStyle("th", fontName="DVB", fontSize=7.8, leading=10.6, textColor=colors.white)
PW = letter[0] - 1.4 * inch

def P(t, st=B): return Paragraph(t, st)
def bl(items): return [Paragraph(i, BL, bulletText="•") for i in items]
def img(path, w):
    from PIL import Image as PI
    iw, ih = PI.open(path).size
    return Image(path, width=w, height=w * ih / iw)
def table(rows, widths, head=True):
    data = [[Paragraph(c, TH if (head and r == 0) else TC) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .4, LINE),
          ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 4)]
    if head: st.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2b3640")))
    t.setStyle(TableStyle(st)); return t
def footer(title):
    def f(c, d):
        c.saveState(); c.setFont("DV", 7); c.setFillColor(MUTE)
        c.drawString(0.7 * inch, 0.45 * inch, title)
        c.drawRightString(letter[0] - 0.7 * inch, 0.45 * inch, "Page %d" % d.page); c.restoreState()
    return f
