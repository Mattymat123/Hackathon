import os
import subprocess
from datetime import datetime

def export_to_pdf(content: str, filename: str = None) -> str:
    """
    Export markdown content to PDF using markdown-pdf.
    
    Args:
        content: The markdown content to convert to PDF
        filename: Optional custom filename (without extension)
    
    Returns:
        Path to the generated PDF file
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aktstykke_{timestamp}"
    
    # Create temporary markdown file
    md_path = os.path.join(output_dir, f"{filename}.md")
    pdf_path = os.path.join(output_dir, f"{filename}.pdf")
    
    # Write content to markdown file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    try:
        # Convert markdown to PDF using markdown-pdf
        result = subprocess.run(
            ['markdown-pdf', md_path, '-o', pdf_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Clean up temporary markdown file
        os.remove(md_path)
        
        return pdf_path
    except subprocess.CalledProcessError as e:
        # If markdown-pdf fails, provide helpful error message
        error_msg = f"Error converting to PDF: {e.stderr}"
        raise Exception(error_msg)
    except FileNotFoundError:
        raise Exception("markdown-pdf is not installed. Please install it with: npm install -g markdown-pdf")
