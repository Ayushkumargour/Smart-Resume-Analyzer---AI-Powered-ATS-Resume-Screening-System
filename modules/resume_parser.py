"""
Resume Parser Module
Extracts text from PDF resumes using PyPDF2
"""

import PyPDF2
import re
from typing import Optional


def extract_text_from_pdf(pdf_path: str) -> Optional[str]:
    """
    Extracts text from a PDF file
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text as a string, or None if extraction fails
    """
    try:
        text = ""
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from all pages
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text += page_text + "\n"
        
        # Clean the text
        cleaned_text = clean_text(text)
        
        return cleaned_text if cleaned_text.strip() else None
        
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return None


def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
    - Removing excessive whitespace
    - Converting to lowercase
    - Removing special characters (keeping alphanumeric and basic punctuation)
    
    Args:
        text: Raw extracted text
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Replace multiple whitespace characters with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove excessive newlines
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters but keep alphanumeric, spaces, and basic punctuation
    # This helps preserve skill names and technical terms
    text = re.sub(r'[^\w\s\.\-\+\#]', ' ', text)
    
    # Final whitespace cleanup
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def get_resume_text(pdf_path: str) -> Optional[str]:
    """
    Main function to extract and clean resume text
    
    Args:
        pdf_path: Path to the PDF resume
        
    Returns:
        Cleaned resume text or None if extraction fails
    """
    return extract_text_from_pdf(pdf_path)

