from flask import Flask, render_template, request
import os

from services.resume_parser import extract_text_from_pdf
from services.ai_analyzer import analyze_resume


app = Flask(__name__)


# ==========================================
# Upload folder
# ==========================================

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================
# Home
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Upload Resume
# ==========================================

@app.route("/upload", methods=["POST"])
def upload_resume():

    resume = request.files.get("resume")


    # Check file
    if resume is None:

        return """
        <h2>❌ No resume selected.</h2>
        <a href="/">← Go Back</a>
        """


    if resume.filename == "":

        return """
        <h2>❌ Please select a resume.</h2>
        <a href="/">← Go Back</a>
        """


    # ==========================================
    # Allowed extensions
    # ==========================================

    allowed_extensions = [".pdf", ".docx"]

    file_extension = os.path.splitext(
        resume.filename
    )[1].lower()


    if file_extension not in allowed_extensions:

        return """
        <h2>❌ Only PDF and DOCX files are allowed.</h2>
        <a href="/">← Go Back</a>
        """


    # ==========================================
    # Save resume
    # ==========================================

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(file_path)


    print()
    print("================================")
    print("📄 RESUME UPLOADED")
    print("File:", resume.filename)
    print("================================")


    # ==========================================
    # PDF
    # ==========================================

    if file_extension == ".pdf":

        try:

            print("📖 Extracting PDF text...")

            resume_text = extract_text_from_pdf(
                file_path
            )

            print("✅ PDF text extracted")


        except Exception as e:

            print("❌ PDF ERROR:", e)

            return f"""
            <h2>❌ PDF Reading Error</h2>

            <p>{str(e)}</p>

            <a href="/">
                ← Upload another resume
            </a>
            """


        # ==========================================
        # Check text
        # ==========================================

        if not resume_text.strip():

            return """
            <h2>⚠️ No readable text found.</h2>

            <p>
            Please upload a PDF containing selectable text.
            </p>

            <a href="/">
                ← Upload another resume
            </a>
            """


        # ==========================================
        # AI Analysis
        # ==========================================

        ai_analysis = analyze_resume(
            resume_text
        )


        # ==========================================
        # AI Error
        # ==========================================

        if "error" in ai_analysis:

            return f"""
            <h2>❌ AI Analysis Error</h2>

            <p>{ai_analysis["error"]}</p>

            <a href="/">
                ← Try Again
            </a>
            """


        # ==========================================
        # Get values
        # ==========================================

        name = ai_analysis.get(
            "name",
            "Not mentioned"
        )


        education = ai_analysis.get(
            "education",
            []
        )


        skills = ai_analysis.get(
            "skills",
            []
        )


        experience = ai_analysis.get(
            "experience",
            []
        )


        job_roles = ai_analysis.get(
            "job_roles",
            []
        )


        score = ai_analysis.get(
            "score",
            0
        )


        suggestions = ai_analysis.get(
            "suggestions",
            []
        )


        # ==========================================
        # Convert lists to HTML
        # ==========================================

        education_html = "".join(

            f"<li>{item}</li>"

            for item in education

        )


        skills_html = "".join(

            f"<span>{item}</span>"

            for item in skills

        )


        experience_html = "".join(

            f"<li>{item}</li>"

            for item in experience

        )


        jobs_html = "".join(

            f"<li>{item}</li>"

            for item in job_roles

        )


        suggestions_html = "".join(

            f"<li>{item}</li>"

            for item in suggestions

        )


        # ==========================================
        # Dashboard
        # ==========================================

        return f"""

        <!DOCTYPE html>

        <html>

        <head>

            <meta charset="UTF-8">

            <meta name="viewport"
                  content="width=device-width, initial-scale=1.0">

            <title>
                CareerPilot AI
            </title>


            <style>

                * {{
                    box-sizing: border-box;
                }}


                body {{

                    margin: 0;

                    padding: 30px;

                    font-family: Arial, sans-serif;

                    background: #f5f7fb;

                }}


                .container {{

                    max-width: 1000px;

                    margin: auto;

                }}


                header {{

                    text-align: center;

                    margin-bottom: 30px;

                }}


                header h1 {{

                    color: #4f46e5;

                    font-size: 36px;

                }}


                header p {{

                    color: #666;

                }}


                .card {{

                    background: white;

                    padding: 25px;

                    margin-bottom: 20px;

                    border-radius: 15px;

                    box-shadow:
                        0 5px 20px
                        rgba(0,0,0,0.08);

                }}


                .score-card {{

                    text-align: center;

                }}


                .score {{

                    font-size: 60px;

                    font-weight: bold;

                    color: #4f46e5;

                }}


                .score-label {{

                    color: #666;

                    font-size: 18px;

                }}


                .grid {{

                    display: grid;

                    grid-template-columns:
                        repeat(
                            auto-fit,
                            minmax(300px, 1fr)
                        );

                    gap: 20px;

                }}


                h2 {{

                    color: #333;

                    margin-top: 0;

                }}


                li {{

                    margin-bottom: 10px;

                    line-height: 1.5;

                }}


                .skills span {{

                    display: inline-block;

                    background: #eef2ff;

                    color: #3730a3;

                    padding: 8px 12px;

                    margin: 5px;

                    border-radius: 20px;

                }}


                .button {{

                    display: inline-block;

                    background: #4f46e5;

                    color: white;

                    padding: 13px 22px;

                    border-radius: 8px;

                    text-decoration: none;

                }}

            </style>

        </head>


        <body>


        <div class="container">


            <header>

                <h1>
                    🚀 CareerPilot AI
                </h1>

                <p>
                    AI-Powered Resume Analyzer
                </p>

            </header>


            <!-- Score -->

            <div class="card score-card">

                <div class="score">
                    {score}/100
                </div>

                <div class="score-label">
                    📊 Resume Score
                </div>

            </div>


            <!-- Name -->

            <div class="card">

                <h2>
                    👤 Candidate
                </h2>

                <p>
                    <strong>Name:</strong>
                    {name}
                </p>

            </div>


            <!-- Grid -->

            <div class="grid">


                <!-- Education -->

                <div class="card">

                    <h2>
                        🎓 Education
                    </h2>

                    <ul>

                        {education_html}

                    </ul>

                </div>


                <!-- Skills -->

                <div class="card">

                    <h2>
                        💻 Skills
                    </h2>

                    <div class="skills">

                        {skills_html}

                    </div>

                </div>


                <!-- Experience -->

                <div class="card">

                    <h2>
                        💼 Experience
                    </h2>

                    <ul>

                        {experience_html}

                    </ul>

                </div>


                <!-- Job Roles -->

                <div class="card">

                    <h2>
                        🎯 Suitable Job Roles
                    </h2>

                    <ul>

                        {jobs_html}

                    </ul>

                </div>


                <!-- Suggestions -->

                <div class="card">

                    <h2>
                        💡 Suggestions
                    </h2>

                    <ul>

                        {suggestions_html}

                    </ul>

                </div>


            </div>


            <!-- Resume text -->

            <div class="card">

                <h2>
                    📄 Extracted Resume Text
                </h2>

                <pre style="
                    white-space: pre-wrap;
                    line-height: 1.6;
                ">{resume_text}</pre>

            </div>


            <a
                href="/"
                class="button"
            >
                ← Upload Another Resume
            </a>


        </div>


        </body>

        </html>

        """


    # ==========================================
    # DOCX
    # ==========================================

    return f"""

    <h1>✅ Resume Uploaded Successfully</h1>

    <p>
        File: {resume.filename}
    </p>

    <p>
        DOCX analysis will be added next.
    </p>

    <a href="/">
        ← Upload another resume
    </a>

    """


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )