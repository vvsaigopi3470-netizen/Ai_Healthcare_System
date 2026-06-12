from reportlab.platypus import \
SimpleDocTemplate

from reportlab.platypus import \
Paragraph

from reportlab.lib.styles \
import getSampleStyleSheet

def export_pdf(
title,
content,
filename
):

    filepath = f"""
    generated_reports/
    {filename}.pdf
    """

    doc = SimpleDocTemplate(
    filepath
    )

    styles = getSampleStyleSheet()

    elements = [

    Paragraph(
    title,
    styles['Title']
    ),

    Paragraph(
    content,
    styles['BodyText']
    )

    ]

    doc.build(elements)

    return filepath