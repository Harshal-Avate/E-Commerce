"""
E-Commerce Project Report — Markdown to PDF Converter
Uses ReportLab (pure Python, no system dependencies).
"""
import re
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, Preformatted, KeepTogether
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ─────── Paths ───────
MD_PATH  = r"C:\Users\dell\.gemini\antigravity\brain\211de26d-8c3f-4c82-a7c9-cdf58476e74c\E-Commerce_Project_Report.md"
PDF_PATH = r"C:\Users\dell\.gemini\antigravity\brain\211de26d-8c3f-4c82-a7c9-cdf58476e74c\E-Commerce_Project_Report.pdf"

# ─────── Colors ───────
NAVY    = colors.HexColor("#003366")
BLUE2   = colors.HexColor("#1a5276")
LBLUE   = colors.HexColor("#aac4e0")
TBLUE   = colors.HexColor("#f0f5fa")
CODEBG  = colors.HexColor("#f4f6f8")
CODEBRD = colors.HexColor("#003366")
WHITE   = colors.white
DARK    = colors.HexColor("#1a1a1a")
GRAY    = colors.HexColor("#666666")

# ─────── Styles ───────
styles = getSampleStyleSheet()

def S(name, **kw):
    """Create a ParagraphStyle."""
    return ParagraphStyle(name, **kw)

sTitle = S("sTitle",
    fontName="Helvetica-Bold", fontSize=24, leading=30,
    textColor=NAVY, alignment=TA_CENTER, spaceAfter=6)

sSubtitle = S("sSubtitle",
    fontName="Helvetica", fontSize=13, leading=18,
    textColor=BLUE2, alignment=TA_CENTER, spaceAfter=4)

sMeta = S("sMeta",
    fontName="Helvetica", fontSize=10, leading=14,
    textColor=DARK, alignment=TA_CENTER, spaceAfter=2)

sH1 = S("sH1",
    fontName="Helvetica-Bold", fontSize=16, leading=22,
    textColor=NAVY, spaceBefore=20, spaceAfter=8,
    borderPad=4)

sH2 = S("sH2",
    fontName="Helvetica-Bold", fontSize=13, leading=18,
    textColor=NAVY, spaceBefore=14, spaceAfter=6)

sH3 = S("sH3",
    fontName="Helvetica-Bold", fontSize=11, leading=16,
    textColor=BLUE2, spaceBefore=10, spaceAfter=4)

sH4 = S("sH4",
    fontName="Helvetica-BoldOblique", fontSize=10.5, leading=14,
    textColor=BLUE2, spaceBefore=8, spaceAfter=3)

sBody = S("sBody",
    fontName="Helvetica", fontSize=10.5, leading=16,
    textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=6)

sBold = S("sBold",
    fontName="Helvetica-Bold", fontSize=10.5, leading=16,
    textColor=DARK, spaceAfter=6)

sCode = S("sCode",
    fontName="Courier", fontSize=8.5, leading=13,
    textColor=DARK, backColor=CODEBG, spaceAfter=6,
    leftIndent=10, rightIndent=10, spaceBefore=4,
    borderColor=CODEBRD, borderWidth=0.5, borderPad=6)

sBullet = S("sBullet",
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=DARK, leftIndent=18, bulletIndent=6,
    spaceAfter=3)

sNumBullet = S("sNumBullet",
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=DARK, leftIndent=22, bulletIndent=6,
    spaceAfter=3)

sCenter = S("sCenter",
    fontName="Helvetica", fontSize=10.5, leading=15,
    textColor=DARK, alignment=TA_CENTER, spaceAfter=4)

sCellH = S("sCellH",
    fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=WHITE)

sCellB = S("sCellB",
    fontName="Helvetica", fontSize=9, leading=12,
    textColor=DARK)

sHr = S("sHr", spaceAfter=0, spaceBefore=0)

# ─────── Header / Footer ───────
def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 18*mm, w, 18*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(WHITE)
    canvas.drawString(30*mm, h - 12*mm, "E-Commerce Web Application — Project Report")
    canvas.drawRightString(w - 20*mm, h - 12*mm, "2025–2026")

    # Footer
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 12*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(30*mm, 4*mm, "Confidential — For Academic Use Only")
    canvas.drawRightString(w - 20*mm, 4*mm, f"Page {doc.page}")
    canvas.restoreState()

def on_first_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Gradient-like top banner for cover
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 60*mm, w, 60*mm, fill=1, stroke=0)
    canvas.setFillColor(LBLUE)
    canvas.rect(0, h - 62*mm, w, 2*mm, fill=1, stroke=0)
    # Bottom bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 25*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(WHITE)
    canvas.drawString(30*mm, 10*mm, "Django · Python · SQLite · HTML · CSS · JavaScript")
    canvas.drawRightString(w - 20*mm, 10*mm, "2025–2026")
    canvas.restoreState()

# ─────── Escape HTML chars ───────
def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline_fmt(text):
    """Handle bold/italic/code inline formatting."""
    text = esc(text)
    # Bold+italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`(.*?)`', r'<font name="Courier" size="9">\1</font>', text)
    # Markdown link [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return text

# ─────── Table parser ───────
def parse_md_table(lines):
    rows = []
    for line in lines:
        line = line.strip().strip("|")
        if re.match(r'^[-:\s|]+$', line):
            continue
        cells = [c.strip() for c in line.split("|")]
        rows.append(cells)
    if not rows:
        return None

    col_n = max(len(r) for r in rows)
    for r in rows:
        while len(r) < col_n:
            r.append("")

    # Build reportlab table data
    data = []
    for i, row in enumerate(rows):
        if i == 0:
            data.append([Paragraph(inline_fmt(c), sCellH) for c in row])
        else:
            data.append([Paragraph(inline_fmt(c), sCellB) for c in row])

    col_w = (A4[0] - 50*mm) / col_n
    tbl = Table(data, colWidths=[col_w] * col_n, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0),  NAVY),
        ("TEXTCOLOR",   (0,0), (-1,0),  WHITE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, TBLUE]),
        ("GRID",        (0,0), (-1,-1), 0.5, LBLUE),
        ("FONTNAME",    (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0,0), (-1,-1), 9),
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",  (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING",(0,0), (-1,-1), 6),
    ]))
    return tbl

# ─────── Main parser ───────
def md_to_flowables(md_text):
    story = []
    lines = md_text.split("\n")
    i = 0
    in_code = False
    code_buf = []
    table_buf = []
    in_table = False
    first_h1 = True

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()

        # ── Fenced code block
        if stripped.startswith("```"):
            if not in_code:
                in_code = True
                code_buf = []
                i += 1
                continue
            else:
                in_code = False
                code_text = "\n".join(code_buf)
                story.append(Preformatted(code_text, sCode))
                story.append(Spacer(1, 4))
                code_buf = []
                i += 1
                continue

        if in_code:
            code_buf.append(raw)
            i += 1
            continue

        # ── Markdown table
        if stripped.startswith("|"):
            table_buf.append(stripped)
            i += 1
            continue
        else:
            if table_buf:
                tbl = parse_md_table(table_buf)
                if tbl:
                    story.append(tbl)
                    story.append(Spacer(1, 8))
                table_buf = []

        # ── HR
        if re.match(r'^[-]{3,}$', stripped) or re.match(r'^[*]{3,}$', stripped):
            story.append(HRFlowable(width="100%", thickness=1.2, color=LBLUE))
            story.append(Spacer(1, 4))
            i += 1
            continue

        # ── Headings
        m = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if m:
            level = len(m.group(1))
            text = inline_fmt(m.group(2))
            if level == 1:
                if not first_h1:
                    story.append(PageBreak())
                first_h1 = False
                story.append(Paragraph(text, sH1))
                story.append(HRFlowable(width="100%", thickness=2, color=NAVY))
                story.append(Spacer(1, 6))
            elif level == 2:
                story.append(Spacer(1, 6))
                story.append(Paragraph(text, sH2))
                story.append(HRFlowable(width="100%", thickness=0.8, color=LBLUE))
                story.append(Spacer(1, 4))
            elif level == 3:
                story.append(Paragraph(text, sH3))
            elif level >= 4:
                story.append(Paragraph(text, sH4))
            i += 1
            continue

        # ── Unordered list
        m = re.match(r'^[-*+]\s+(.*)', stripped)
        if m:
            story.append(Paragraph(f"• {inline_fmt(m.group(1))}", sBullet))
            i += 1
            continue

        # ── Ordered list
        m = re.match(r'^\d+\.\s+(.*)', stripped)
        if m:
            story.append(Paragraph(f"{inline_fmt(m.group(0))}", sNumBullet))
            i += 1
            continue

        # ── Blockquote
        if stripped.startswith(">"):
            text = stripped.lstrip("> ").strip()
            story.append(Paragraph(f"<i>{inline_fmt(text)}</i>", S("BQ",
                fontName="Helvetica-Oblique", fontSize=10, leading=15,
                textColor=BLUE2, leftIndent=20, borderColor=NAVY,
                borderWidth=2, borderPad=8, spaceBefore=4, spaceAfter=4)))
            i += 1
            continue

        # ── Empty line
        if not stripped:
            story.append(Spacer(1, 4))
            i += 1
            continue

        # ── Bold-only standalone line (e.g., **Title:**)
        if re.match(r'^\*\*.*\*\*$', stripped):
            story.append(Paragraph(inline_fmt(stripped), sBold))
            i += 1
            continue

        # ── Normal paragraph
        story.append(Paragraph(inline_fmt(stripped), sBody))
        i += 1

    # flush any remaining table
    if table_buf:
        tbl = parse_md_table(table_buf)
        if tbl:
            story.append(tbl)

    return story

# ─────── Build PDF ───────
def build_pdf():
    print("Reading markdown...")
    with open(MD_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Split off the cover (first 5 lines with title and meta)
    lines = md_text.strip().split("\n")
    # Remove H1 title from top (we'll make a custom cover page)
    title_line = lines[0] if lines[0].startswith("# ") else "# E-Commerce Web Application"
    title_text = title_line.lstrip("# ").strip()

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=30*mm, rightMargin=20*mm,
        topMargin=25*mm, bottomMargin=20*mm,
        title="E-Commerce Web Application — Project Report",
        author="Student",
        subject="Academic Project Report",
    )

    story = []

    # ── Cover Page ──
    story.append(Spacer(1, 50*mm))
    story.append(Paragraph("E-Commerce Web Application", sTitle))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Project Report", sSubtitle))
    story.append(Spacer(1, 10*mm))
    story.append(HRFlowable(width="60%", thickness=2, color=LBLUE, hAlign="CENTER"))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("Technology Stack: Python · Django · SQLite · HTML · CSS · JavaScript", sMeta))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Academic Year: 2025–2026", sMeta))
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph("Submitted By: [Your Name]", sMeta))
    story.append(Paragraph("Roll No.: [Your Roll No.]", sMeta))
    story.append(Paragraph("Department: [Your Department]", sMeta))
    story.append(Paragraph("Institution: [Your Institution]", sMeta))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Guide: [Guide Name] | Date: March 20, 2026", sMeta))
    story.append(PageBreak())

    # ── Parse rest of markdown ──
    print("Parsing markdown...")
    # Skip the first H1 line since we have custom cover
    body_md = "\n".join(lines[1:])
    story += md_to_flowables(body_md)

    # ── Build ──
    print("Building PDF...")
    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_page)

    size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"\n✅ PDF created successfully!")
    print(f"📄 Location: {PDF_PATH}")
    print(f"📦 File size: {size_kb:.1f} KB")

if __name__ == "__main__":
    build_pdf()
