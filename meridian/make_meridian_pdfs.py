"""Meridian Intelligence PDF helpers.

Rebuilt into the repository on 31 August 2026 after the original copy was lost
with an ephemeral scratchpad. Keep this file in the repo: every Meridian PDF
generator imports from it.

Usage:
    from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether,
)

TEAL = HexColor('#0F7B7B')
BLUE = HexColor('#1F5FA8')
NAVY = HexColor('#12263F')
RED = HexColor('#B23A31')
GREY = HexColor('#5A6672')
LINE = HexColor('#D6DCE2')

BODY = 'Helvetica'
BOLD = 'Helvetica-Bold'

S = {
    'L': ParagraphStyle('L', fontName=BOLD, fontSize=15, leading=18,
                        textColor=NAVY, spaceBefore=2, spaceAfter=3),
    'H': ParagraphStyle('H', fontName=BOLD, fontSize=11.5, leading=14,
                        textColor=TEAL, spaceBefore=9, spaceAfter=3),
    'SUB': ParagraphStyle('SUB', fontName=BOLD, fontSize=9.8, leading=12,
                          textColor=NAVY, spaceBefore=7, spaceAfter=2),
    'P': ParagraphStyle('P', fontName=BODY, fontSize=9.2, leading=12.6,
                        textColor=HexColor('#1B2733'), spaceAfter=4,
                        alignment=TA_LEFT),
    'B': ParagraphStyle('B', fontName=BODY, fontSize=9.2, leading=12.6,
                        textColor=HexColor('#1B2733'), spaceAfter=2.5,
                        leftIndent=9, bulletIndent=1),
    'N': ParagraphStyle('N', fontName=BODY, fontSize=7.6, leading=10,
                        textColor=GREY, spaceBefore=3, spaceAfter=3),
    'TH': ParagraphStyle('TH', fontName=BOLD, fontSize=8.2, leading=10.2,
                         textColor=white),
    'TD': ParagraphStyle('TD', fontName=BODY, fontSize=8.2, leading=10.4,
                         textColor=HexColor('#1B2733')),
    'CO': ParagraphStyle('CO', fontName=BODY, fontSize=9.2, leading=12.6,
                         textColor=HexColor('#12263F')),
}


def L(t):
    return Paragraph(t, S['L'])


def H(t):
    return Paragraph(t, S['H'])


def SUB(t):
    return Paragraph(t, S['SUB'])


def P(t):
    return Paragraph(t, S['P'])


def B(t):
    return Paragraph(t, S['B'], bulletText='•')


def N(t):
    return Paragraph(t, S['N'])


def rule(colour=TEAL, width=1.1):
    return HRFlowable(width='100%', thickness=width, color=colour,
                      spaceBefore=1, spaceAfter=6)


def callout(text, bar=TEAL, bg=HexColor('#EAF5F4')):
    """A tinted box with a coloured left bar."""
    t = Table([[Paragraph(text, S['CO'])]], colWidths=[168 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 2.6, bar),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 5)])


def simple_table(header, rows, widths, header_bg=NAVY):
    data = [[Paragraph(h, S['TH']) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), S['TD']) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ('BACKGROUND', (0, 0), (-1, 0), header_bg),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.5, LINE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(('BACKGROUND', (0, i), (-1, i), HexColor('#F5F8FA')))
    t.setStyle(TableStyle(style))
    return KeepTogether([Spacer(1, 2), t, Spacer(1, 6)])


def build(path, flowables, title='Meridian Intelligence',
          footer='Meridian Intelligence  ·  Private and confidential'):
    """Render flowables to an A4 PDF with the Meridian header band and footer."""

    def page(canv, doc):
        canv.saveState()
        # header band
        canv.setFillColor(NAVY)
        canv.rect(0, A4[1] - 16 * mm, A4[0], 16 * mm, stroke=0, fill=1)
        canv.setFillColor(white)
        canv.setFont(BOLD, 10.5)
        canv.drawString(21 * mm, A4[1] - 10.6 * mm, 'MERIDIAN INTELLIGENCE')
        canv.setFillColor(HexColor('#7FD4D0'))
        canv.setFont(BODY, 8)
        canv.drawRightString(A4[0] - 21 * mm, A4[1] - 10.4 * mm, title)
        # footer
        canv.setFillColor(GREY)
        canv.setFont(BODY, 7.2)
        canv.drawString(21 * mm, 11 * mm, footer)
        canv.drawRightString(A4[0] - 21 * mm, 11 * mm, str(canv.getPageNumber()))
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.4)
        canv.line(21 * mm, 14.5 * mm, A4[0] - 21 * mm, 14.5 * mm)
        canv.restoreState()

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=21 * mm, rightMargin=21 * mm,
                          topMargin=22 * mm, bottomMargin=18 * mm,
                          title=title, author='Meridian Intelligence')
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=page)])
    doc.build(flowables)
    return path
