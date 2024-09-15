# modules/doc_utils.py

import docx
from PyPDF2 import PdfReader

def extract_text_from_document(uploaded_file):
    text = ""
    
    if uploaded_file.name.endswith('.pdf'):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()

    elif uploaded_file.name.endswith('.docx'):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text

    elif uploaded_file.name.endswith('.md'):
        text = uploaded_file.read().decode('utf-8')

    return text
