#!/usr/bin/env python3
"""
Marketing Report PDF Generator — AI Marketing Claude Code Skills
Generates professional, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, Image)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# Color palette
COLORS = {
    "primary": HexColor("#1B2A4A"),
    "accent": HexColor("#2D5BFF"),
    "highlight": HexColor("#FF6B35"),
    "success": HexColor("#00C853"),
    "warning": HexColor("#FFB300"),
    "danger": HexColor("#FF1744"),
    "light_bg": HexColor("#F5F7FA"),
    "text": HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border": HexColor("#E0E6ED"),
    "white": white,
    "black": black,
}


def score_color(score):
    """Return color based on score value."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def draw_score_gauge(score, x, y, size=80):
    """Create a circular score gauge drawing."""
    d = Drawing(size + 20, size + 30)

    # Background circle
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Score arc (simplified as colored inner circle)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=color, strokeColor=None))

    # White center
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))

    # Score text
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))

    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Create a horizontal bar chart for category scores."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Category label
        d.add(String(label_x, y + 5, cat[:22],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))

        # Background bar
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))

        # Score bar
        bar_width = (score / 100) * max_bar_width
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None))

        # Score label
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))

    return d


def generate_report(data, output_path):
    """Generate a professional marketing PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=28,
        textColor=COLORS["primary"],
        spaceAfter=6,
        fontName="Helvetica-Bold"
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        textColor=COLORS["text_light"],
        spaceAfter=20,
        fontName="Helvetica"
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=COLORS["primary"],
        spaceBefore=20,
        spaceAfter=10,
        fontName="Helvetica-Bold"
    )

    subheading_style = ParagraphStyle(
        "CustomSubheading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=COLORS["accent"],
        spaceBefore=14,
        spaceAfter=8,
        fontName="Helvetica-Bold"
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        textColor=COLORS["text"],
        spaceAfter=6,
        fontName="Helvetica",
        leading=14
    )

    # Build document elements
    elements = []

    # === COVER PAGE ===
    elements.append(Spacer(1, 1.5 * inch))
    elements.append(Paragraph("Relatório de Auditoria de Marketing", title_style))

    url = data.get("url", "exemplo.com")
    date_str = data.get("date", datetime.now().strftime("%d de %B de %Y"))
    elements.append(Paragraph(f"{url}", subtitle_style))
    elements.append(Paragraph(f"Gerado em: {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    # Overall score gauge
    overall_score = data.get("overall_score", 0)
    gauge = draw_score_gauge(overall_score, 0, 0, size=100)
    elements.append(gauge)
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Pontuação Geral de Marketing: {int(overall_score)}/100 (Nota: {grade})", heading_style))

    exec_summary = data.get("executive_summary", "Este relatório fornece uma análise abrangente da eficácia de marketing do site em conteúdo, conversão, SEO, posicionamento competitivo, confiança da marca e estratégia de crescimento.")
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(PageBreak())

    # === SCORE BREAKDOWN ===
    elements.append(Paragraph("Detalhamento da Pontuação", heading_style))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Conteúdo e Mensagem", "Otimização de Conversão", "SEO e Descoberta",
        "Posicionamento Competitivo", "Marca e Confiança", "Estratégia de Crescimento"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    # Bar chart
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 0.3 * inch))

    # Score table
    score_data = [["Categoria", "Pontuação", "Peso", "Status"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Forte" if score >= 75 else "Precisa Melhorar" if score >= 50 else "Crítico"
        weight = weights[i] if i < len(weights) else "—"
        score_data.append([name, f"{int(score)}/100", weight, status])

    score_table = Table(score_data, colWidths=[180, 70, 60, 90])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)

    elements.append(PageBreak())

    # === KEY FINDINGS ===
    elements.append(Paragraph("Principais Constatações", heading_style))

    findings = data.get("findings", [])
    if not findings:
        findings = [
            {"severity": "Crítico", "finding": "A manchete da página inicial carece de clareza — os visitantes não conseguem entender a proposta de valor em menos de 5 segundos"},
            {"severity": "Alta", "finding": "Sem prova social na página inicial — faltando depoimentos, logotipos de clientes e selos de confiança"},
            {"severity": "Alta", "finding": "O CTA primário usa texto genérico ('Começar') em vez de uma copy focada em valor"},
            {"severity": "Média", "finding": "Faltam meta descrições em páginas de destino importantes"},
            {"severity": "Média", "finding": "Nenhum mecanismo de captura de e-mail ou isca digital visível"},
            {"severity": "Baixa", "finding": "O conteúdo do blog carece de links internos para as páginas de produtos"},
        ]

    findings_data = [["Severidade", "Constatação"]]
    for f in findings:
        severity = f.get("severity", "Média")
        finding = f.get("finding", "")
        findings_data.append([severity, Paragraph(finding, body_style)])

    findings_table = Table(findings_data, colWidths=[70, 400])
    severity_colors = {
        "Crítico": COLORS["danger"],
        "Alta": COLORS["highlight"],
        "Média": COLORS["warning"],
        "Baixa": COLORS["accent"]
    }
    table_style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        color = severity_colors.get(f.get("severity", "Média"), COLORS["warning"])
        table_style_cmds.append(("TEXTCOLOR", (0, i), (0, i), color))
        table_style_cmds.append(("FONTNAME", (0, i), (0, i), "Helvetica-Bold"))

    findings_table.setStyle(TableStyle(table_style_cmds))
    elements.append(findings_table)

    elements.append(PageBreak())

    # === ACTION PLAN ===
    elements.append(Paragraph("Plano de Ação Priorizado", heading_style))

    # Quick Wins
    elements.append(Paragraph("Ganhos Rápidos (Esta Semana)", subheading_style))
    quick_wins = data.get("quick_wins", [
        "Reescrever a manchete da página inicial para ser específica e focada em benefícios",
        "Adicionar 3-5 logotipos de clientes ou selos de confiança acima da dobra",
        "Alterar o CTA primário para um texto focado em valor (ex: 'Iniciar Teste Grátis — Sem Cartão de Crédito')",
        "Adicionar meta descrições às 5 principais págimas de destino",
    ])
    for i, win in enumerate(quick_wins, 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Medium-Term
    elements.append(Paragraph("Médio Prazo (1-3 Meses)", subheading_style))
    medium_term = data.get("medium_term", [
        "Construir funil de captura de e-mail com isca digital",
        "Criar páginas de comparação para os 3 principais concorrentes",
        "Desenvolver 3 estudos de caso com resultados mensuráveis",
        "Implementar estratégia de conteúdo de blog visando palavras-chave de alta intenção",
    ])
    for i, action in enumerate(medium_term, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Strategic
    elements.append(Paragraph("Estratégico (3-6 Meses)", subheading_style))
    strategic = data.get("strategic", [
        "Lançar programa de indicação com estrutura de incentivos",
        "Construir hub de autoridade de conteúdo com conteúdo pilar",
        "Implementar campanha de retargeting de funil completo",
        "Desenvolver otimização de preços baseada em métricas de valor",
    ])
    for i, action in enumerate(strategic, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === COMPETITOR SNAPSHOT ===
    if data.get("competitors"):
        elements.append(Paragraph("Cenário Competitivo", heading_style))

        comp_data = [["", data.get("brand_name", "Alvo")] + [c.get("name", f"Concorrente {i+1}") for i, c in enumerate(data["competitors"][:3])]]
        comp_rows = [["Posicionamento", "positioning"], ["Preço", "pricing"], ["Prova Social", "social_proof"], ["Conteúdo", "content"]]

        for label, key in comp_rows:
            row = [label, data.get("brand_name", "Alvo")]
            for comp in data["competitors"][:3]:
                row.append(comp.get(key, "—"))
            # Ensure consistent columns
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        col_width = 470 / col_count
        comp_table = Table(comp_data, colWidths=[col_width] * col_count)
        comp_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === METHODOLOGY ===
    elements.append(Paragraph("Metodologia", heading_style))
    elements.append(Paragraph(
        "Esta auditoria avalia seis dimensões principais da eficácia de marketing. "
        "Cada categoria é pontuada de 0 a 100 com base nas melhores práticas do setor e benchmarks competitivos.",
        body_style
    ))

    method_data = [
        ["Categoria", "Peso", "O que Medimos"],
        ["Conteúdo e Mensagem", "25%", "Qualidade da copy, clareza da proposta de valor, eficácia do CTA"],
        ["Otimização de Conversão", "20%", "Design do funil, formulários, prova social, redução de fricção"],
        ["SEO e Descoberta", "20%", "SEO on-page, SEO técnico, estrutura de conteúdo"],
        ["Posicionamento Competitivo", "15%", "Diferenciação de mercado, preços, estratégia de alternativas"],
        ["Marca e Confiança", "10%", "Qualidade do design, sinais de confiança, indicadores de autoridade"],
        ["Estratégia de Crescimento", "10%", "Estratégia de preços, canais de aquisição, retenção"],
    ]

    method_table = Table(method_data, colWidths=[140, 50, 280])
    method_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        "Gerado pela AI Marketing Suite para Claude Code",
        ParagraphStyle("Footer", parent=body_style, fontSize=8, textColor=COLORS["text_light"])
    ))

    # Build PDF
    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        # Demo mode — generate sample report
        sample_data = {
            "url": "https://example.com",
            "date": datetime.now().strftime("%B %d, %Y"),
            "overall_score": 62,
            "executive_summary": "This marketing audit reveals several high-impact opportunities to improve conversion rates and strengthen competitive positioning. The website has solid content foundations but is underperforming in conversion optimization and competitive awareness.",
            "categories": {
                "Content & Messaging": {"score": 68, "weight": "25%"},
                "Conversion Optimization": {"score": 52, "weight": "20%"},
                "SEO & Discoverability": {"score": 74, "weight": "20%"},
                "Competitive Positioning": {"score": 48, "weight": "15%"},
                "Brand & Trust": {"score": 70, "weight": "10%"},
                "Growth & Strategy": {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critical", "finding": "Homepage headline is generic — doesn't communicate specific value to target audience"},
                {"severity": "Critical", "finding": "No social proof visible above the fold on the homepage"},
                {"severity": "High", "finding": "Primary CTA button says 'Submit' — should use value-driven text"},
                {"severity": "High", "finding": "Pricing page lacks comparison features and doesn't address objections"},
                {"severity": "Medium", "finding": "Missing competitor comparison pages — losing high-intent search traffic"},
                {"severity": "Medium", "finding": "Blog posts have no internal links to product pages"},
                {"severity": "Low", "finding": "Social media links in footer but no social proof integration"},
            ],
            "quick_wins": [
                "Rewrite homepage headline: 'We help businesses grow' → 'Get 3x more qualified leads in 30 days — without cold calling'",
                "Add 5 client logos above the fold with 'Trusted by 500+ companies' text",
                "Change form button from 'Submit' to 'Get My Free Marketing Audit'",
                "Add testimonial section with name, photo, company, and specific results",
            ],
            "medium_term": [
                "Build '[Competitor] Alternative' landing pages for top 3 competitors",
                "Create 3 video case studies showing measurable client results",
                "Implement exit-intent popup with lead magnet offer",
                "Launch email nurture sequence for leads who don't convert immediately",
            ],
            "strategic": [
                "Develop content authority hub with 10 pillar pages targeting high-volume keywords",
                "Build referral program with double-sided incentives",
                "Launch retargeting campaigns across Meta and Google with funnel-based messaging",
                "Create free tool or assessment to capture leads at top of funnel",
            ],
            "competitors": [
                {"name": "Comp A", "positioning": "All-in-one platform", "pricing": "$49-199/mo", "social_proof": "10K+ users", "content": "Active blog"},
                {"name": "Comp B", "positioning": "Enterprise focus", "pricing": "Custom", "social_proof": "Fortune 500 logos", "content": "Whitepapers"},
                {"name": "Comp C", "positioning": "Budget-friendly", "pricing": "Free-$29/mo", "social_proof": "4.8★ G2", "content": "YouTube channel"},
            ],
            "brand_name": "Example Co"
        }

        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    # JSON input mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
