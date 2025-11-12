from markdown_pdf import MarkdownPdf, Section

def export_to_pdf(content: str, filename: str = None) -> str:
    """
    Export markdown content to PDF using markdown-pdf.
    
    Args:
        content: The markdown content to convert to PDF
        filename: filename (without extension)
    
    Returns:
        str: Status message
    """

    pdf_filename = f"{filename}.pdf"
    pdf = MarkdownPdf()
    pdf.add_section(Section(content, toc=False))
    pdf.save(pdf_filename)

    return f"PDF exported successfully as {pdf_filename}"