import os
from pathlib import Path
import PyPDF2
from docx import Document

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = []
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text.append(f"\n--- Page {page_num + 1} ---\n")
                    text.append(page_text)
    except Exception as e:
        text.append(f"\n[Error reading {pdf_path}: {str(e)}]\n")
    return ''.join(text)

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    text = []
    try:
        doc = Document(docx_path)
        for para in doc.paragraphs:
            if para.text.strip():
                text.append(para.text)
    except Exception as e:
        text.append(f"\n[Error reading {docx_path}: {str(e)}]\n")
    return '\n'.join(text)

def concat_all_documents(folder_path=None, output_file='concatenated_output.txt'):
    """
    Concatenate all PDF and DOCX files in the specified folder.
    
    Args:
        folder_path: Path to the folder containing documents. If None, uses current directory.
        output_file: Name of the output text file.
    """
    if folder_path is None:
        folder_path = Path(__file__).parent
    else:
        folder_path = Path(folder_path)
    
    # Get all PDF and DOCX files
    pdf_files = sorted(folder_path.glob('*.pdf'))
    docx_files = sorted(folder_path.glob('*.docx'))
    
    all_files = list(pdf_files) + list(docx_files)
    
    if not all_files:
        print("No PDF or DOCX files found in the folder.")
        return
    
    print(f"Found {len(pdf_files)} PDF files and {len(docx_files)} DOCX files")
    
    # Concatenate all text
    concatenated_text = []
    
    for file_path in all_files:
        print(f"Processing: {file_path.name}")
        concatenated_text.append(f"\n{'='*80}\n")
        concatenated_text.append(f"FILE: {file_path.name}\n")
        concatenated_text.append(f"{'='*80}\n\n")
        
        if file_path.suffix.lower() == '.pdf':
            text = extract_text_from_pdf(file_path)
        elif file_path.suffix.lower() == '.docx':
            text = extract_text_from_docx(file_path)
        else:
            continue
        
        concatenated_text.append(text)
        concatenated_text.append('\n\n')
    
    # Write to output file
    output_path = folder_path / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(concatenated_text))
    
    print(f"\nSuccessfully concatenated {len(all_files)} files into: {output_path}")
    print(f"Total output size: {len(''.join(concatenated_text))} characters")

if __name__ == '__main__':
    concat_all_documents()
