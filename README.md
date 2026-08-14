# 🚀 CareerPilot AI

## AI-Powered Resume Analyzer

CareerPilot AI is an AI-powered resume analysis application that helps candidates understand their resume, identify skills and experience, calculate a resume score, and discover suitable job roles.

It uses **Python, Flask, Ollama, and PDF/DOCX text extraction** to automatically analyze uploaded resumes.

---

## ✨ Features

* 📄 Upload PDF and DOCX resumes
* 🔍 Automatic resume text extraction
* 🤖 AI-powered resume analysis using Ollama
* 📊 Resume score out of 100
* 👤 Candidate information extraction
* 🎓 Education detection
* 💻 Technical skills extraction
* 💼 Work experience analysis
* 🎯 Suitable job role recommendations
* 💡 Resume improvement suggestions
* 📱 Modern responsive UI
* ⚡ Local AI processing with Ollama

---

## 🖥️ Application Preview

### 🏠 Resume Upload

CareerPilot AI provides a modern dashboard for uploading resumes.

### 📊 Resume Analysis

The application analyzes the uploaded resume and displays:

* Resume Score
* Candidate Name
* Education
* Skills
* Experience
* Suitable Job Roles
* Suggestions

---

## 🛠️ Tech Stack

| Technology  | Purpose               |
| ----------- | --------------------- |
| Python      | Backend               |
| Flask       | Web Framework         |
| Ollama      | Local AI / LLM        |
| Llama 3.2   | Resume Analysis       |
| HTML        | Frontend              |
| CSS         | UI Design             |
| JavaScript  | Frontend Interactions |
| PDF Parser  | PDF Text Extraction   |
| DOCX Parser | DOCX Text Extraction  |

---

## 📂 Project Structure

```text
CareerPilot-AI/
│
├── app.py
├── analyzer.py
│
├── services/
│   └── resume_parser.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/komalteli17/CareerPilot-AI.git
```

### 2. Open the project

```bash
cd CareerPilot-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Ollama Setup

Install Ollama and download the required model:

```bash
ollama pull llama3.2
```

Verify the model:

```bash
ollama list
```

Make sure Ollama is running before starting CareerPilot AI.

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Upload a resume and let CareerPilot AI analyze it.

---

## 🔄 How It Works

```text
Resume Upload
      ↓
PDF/DOCX Text Extraction
      ↓
Resume Text
      ↓
Ollama / Llama 3.2
      ↓
AI Resume Analysis
      ↓
Structured JSON
      ↓
CareerPilot AI Dashboard
      ↓
Score + Skills + Experience
+ Job Roles + Suggestions
```

---

## 🎯 Use Cases

CareerPilot AI can help:

* Students
* Fresh graduates
* Job seekers
* Internship applicants
* Career switchers
* Candidates improving their resumes

---

## 🚀 Future Improvements

* 📈 Advanced resume scoring
* 🎯 Job description matching
* 🔎 Job recommendations
* 📑 ATS compatibility score
* 📥 Downloadable analysis report
* 👤 User authentication
* 🗃️ Resume history
* 📊 Career analytics dashboard
* 🌐 Cloud deployment

---

## 🔐 Privacy

CareerPilot AI uses Ollama for local AI processing.

Do not upload real resumes, passwords, API keys, or other sensitive information to the GitHub repository.

---

## 👩‍💻 Developer

**Komal Teli**

BCA Graduate | Python | AI/ML | Generative AI | Web Development | Prompt Engineering

---

## ⭐ Project Highlights

This project demonstrates practical experience with:

* Generative AI
* Local LLM integration
* Prompt Engineering
* Python
* Flask
* Resume parsing
* JSON-based AI responses
* Frontend development
* AI-powered career recommendations

---

## 📜 License

This project is created for educational and portfolio purposes.
