import PyPDF2
import re

def extract_text_from_pdf(uploaded_file):
    """Extracts and cleans text from an uploaded PDF resume."""
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return preprocess_text(text.strip())

def preprocess_text(text):
    """Cleans and preprocesses text by removing special characters and extra spaces."""
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)  # Normalize spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text
