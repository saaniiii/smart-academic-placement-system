import pdfplumber

SKILLS_DB = [
    "python","java","c","c++","sql",
    "machine learning","data analysis",
    "data engineering","pandas","numpy",
    "tensorflow","django","flask",
    "power bi","tableau","excel",
    "communication","problem solving",
    "aws","cloud","spark"
]

def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text.lower()

    return text


def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def analyze_resume(file):

    text = extract_text_from_pdf(file)

    skills = extract_skills(text)

    return skills