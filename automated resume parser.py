import fitz  # PyMuPDF
import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF resume"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def extract_info(text):
    """Extract key details like name, email, phone number, and skills"""
    doc = nlp(text)
    
    # Extract name (assuming first entity is a person's name)
    name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), "Unknown")

    # Extract email
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = email_match.group(0) if email_match else "Not found"

    # Extract phone number
    phone_match = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    phone = phone_match.group(0) if phone_match else "Not found"

    # Extract skills based on predefined keywords
    skills_keywords = ["Python", "JavaScript", "React", "SQL", "Machine Learning", "AI", "Django", "Flask"]
    skills = [word for word in text.split() if word in skills_keywords]

    return {"Name": name, "Email": email, "Phone": phone, "Skills": skills}

# Example Usage
resume_path = "example_resume.pdf"  # Replace with the path to your resume
resume_text = extract_text_from_pdf(resume_path)
parsed_data = extract_info(resume_text)

print(parsed_data)