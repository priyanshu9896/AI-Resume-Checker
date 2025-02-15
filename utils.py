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

def suggest_resume_improvements(text):
    """Suggests possible improvements in the resume text."""
    suggestions = []
    if len(text.split()) < 150:
        suggestions.append("Consider adding more content to your resume to provide sufficient details about your experience.")
    if "teamwork" not in text and "collaboration" not in text:
        suggestions.append("Mentioning teamwork or collaboration can make your resume more appealing to employers.")
    if "leadership" not in text:
        suggestions.append("Adding leadership experience or skills can strengthen your resume.")
    return suggestions
