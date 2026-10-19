
# AI Resume Analyzer

## Project Overview

AI Resume Analyzer is a web application designed to analyze resumes and extract important information from uploaded documents. It helps users review resume details and view a resume score based on the application's scoring logic.

## Features

- Upload resumes in PDF and DOCX formats.
- Extract resume text.
- Identify details such as name, email, phone number, education, skills, and projects.
- Display a resume score based on the configured scoring logic.
- Simple and responsive user interface.
- Dark theme design.

## Technologies Used

- Python
- Flask
- PyMuPDF
- python-docx
- HTML
- CSS
- JavaScript

## Project Structure

```text
AI_Resume_Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── style.css
│   └── script.js
└── uploads/
```

## Installation

### 1. Install Python

Install Python and make sure it is available on your system.

### 2. Open the project folder

Open the AI Resume Analyzer folder in Visual Studio Code.

### 3. Install dependencies

Open the VS Code terminal and run:

```bash
py -m pip install -r requirements.txt
```

### 4. Run the application

Run the following command:

```bash
py app.py
```

### 5. Open the website

Open this address in your browser:

http://127.0.0.1:5000

## How to Use

1. Open the AI Resume Analyzer website.
2. Select a PDF or DOCX resume.
3. Click the Analyze Resume button.
4. Review the extracted resume details and score.

## Important Notes

- Keep the terminal running while using the local website.
- The supported file formats depend on the implementation in `app.py`.
- The resume score depends on the scoring rules configured in the application.
- Do not upload confidential resumes to an untrusted deployment.

## Author

AI Resume Analyzer Project
