from flask import Flask, render_template, request, redirect, url_for
import os
import re
import fitz

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Comprehensive Technical Skills Database
SKILLS_DATABASE = [
    "python", "java", "c", "c++", "html", "css", "javascript", "sql", 
    "mongodb", "flask", "django", "react", "node.js", "machine learning", 
    "artificial intelligence", "data science", "fastapi", "docker", "git",
    "aws", "angular", "bootstrap", "tailwind", "postgresql", "linux"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    # Check if a file is part of the request
    if "resume" not in request.files:
        return render_template("index.html", error="No file part in the request.")
    
    file = request.files["resume"]

    if file.filename == "":
        return render_template("index.html", error="No resume file selected.")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from PDF file using PyMuPDF (fitz)
    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        return render_template("index.html", error="Error occurred while parsing the PDF file.")

    resume_text_lower = text.lower()

    # Extract basic information
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    name = lines[0] if lines else "Candidate Name Not Found"

    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email = email_match.group() if email_match else "Not Provided"

    phone_match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)
    phone = phone_match.group() if phone_match else "Not Provided"

    # Identify found and missing skills
    found_skills = [skill for skill in SKILLS_DATABASE if skill in resume_text_lower]
    missing_skills = [skill for skill in SKILLS_DATABASE if skill not in resume_text_lower]

    # Calculate ATS Score dynamically
    if len(SKILLS_DATABASE) > 0:
        score = int((len(found_skills) / len(SKILLS_DATABASE)) * 100)
        score = min(score, 100)
    else:
        score = 0

    # Generate professional suggestions
    suggestions = []
    if len(found_skills) < 5:
        suggestions.append("Add more relevant technical skills to enhance your profile visibility.")
    if "project" not in resume_text_lower:
        suggestions.append("Include a dedicated 'Projects' section highlighting your practical work.")
    if "github" not in resume_text_lower:
        suggestions.append("Add your GitHub profile link to showcase your source code repositories.")
    if "linkedin" not in resume_text_lower:
        suggestions.append("Add your LinkedIn profile link for professional networking.")
    if "certification" not in resume_text_lower and "certificate" not in resume_text_lower:
        suggestions.append("Highlight any relevant certifications or professional courses completed.")

    # Generate professional summary feedback
    if score >= 75:
        summary = "Outstanding Resume! Your resume is highly ATS-friendly and contains essential industry-standard technical skills."
    elif score >= 50:
        summary = "Good Resume! Incorporate more project descriptions, certifications, and technical keywords to improve your score."
    else:
        summary = "Your resume requires significant improvement. Add core technical skills, detailed project records, and online profiles."

    return render_template(
        "result.html",
        score=score,
        found_skills=found_skills,
        missing_skills=missing_skills,
        suggestions=suggestions,
        name=name,
        email=email,
        phone=phone,
        summary=summary,
        skills=", ".join(found_skills)
    )

if __name__ == "__main__":
    app.run(debug=True)