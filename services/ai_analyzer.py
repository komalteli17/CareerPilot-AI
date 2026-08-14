import ollama
import json
import re


def analyze_resume(resume_text):

    # Resume text limit
    resume_text = resume_text[:5000]

    prompt = f"""
You are an AI Resume Analyzer.

Analyze the resume carefully.

IMPORTANT RULES:
1. Use ONLY information present in the resume.
2. Do NOT invent skills, experience, education, companies, or projects.
3. If a field is not available, use an empty array [].
4. Calculate a realistic resume score from 0 to 100.
5. Return ONLY valid JSON.
6. Do NOT use markdown.
7. Do NOT use ```json.
8. Keep all values simple strings, numbers, or arrays.
9. Education must contain objects with:
   type, school, percentage, year
10. Experience must contain objects with:
   title, company, duration
11. job_roles must contain suitable roles based ONLY on the candidate's education, experience and explicitly mentioned skills.
12. suggestions must contain practical improvements based on missing resume sections.

Return EXACTLY this JSON structure:

{{
    "name": "",
    "education": [],
    "skills": [],
    "experience": [],
    "job_roles": [],
    "score": 0,
    "suggestions": []
}}

Resume:

{resume_text}
"""

    try:

        print("🤖 Sending resume to Ollama...")

        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        content = response["message"]["content"].strip()

        print("✅ Ollama response received")
        print("RAW AI RESPONSE:")
        print(content)

        # -----------------------------------------
        # Remove markdown code fences
        # -----------------------------------------

        content = re.sub(r"^```json\s*", "", content)
        content = re.sub(r"^```\s*", "", content)
        content = re.sub(r"\s*```$", "", content)

        content = content.strip()

        # -----------------------------------------
        # Extract JSON if model adds extra text
        # -----------------------------------------

        start = content.find("{")
        end = content.rfind("}")

        if start != -1 and end != -1:
            content = content[start:end + 1]

        # -----------------------------------------
        # Parse JSON
        # -----------------------------------------

        analysis = json.loads(content)

        # -----------------------------------------
        # Make sure all required fields exist
        # -----------------------------------------

        result = {
            "name": analysis.get("name", "Not mentioned"),
            "education": analysis.get("education", []),
            "skills": analysis.get("skills", []),
            "experience": analysis.get("experience", []),
            "job_roles": analysis.get("job_roles", []),
            "score": analysis.get("score", 0),
            "suggestions": analysis.get("suggestions", [])
        }

        # -----------------------------------------
        # Validate score
        # -----------------------------------------

        try:
            result["score"] = int(result["score"])
        except:
            result["score"] = 0

        if result["score"] < 0:
            result["score"] = 0

        if result["score"] > 100:
            result["score"] = 100

        # -----------------------------------------
        # Ensure arrays
        # -----------------------------------------

        for field in [
            "education",
            "skills",
            "experience",
            "job_roles",
            "suggestions"
        ]:
            if not isinstance(result[field], list):
                result[field] = []

        print("✅ Resume analysis completed")

        return result

    except json.JSONDecodeError as e:

        print("❌ JSON ERROR:", e)
        print("AI CONTENT:", content)

        return {
            "name": "Not mentioned",
            "education": [],
            "skills": [],
            "experience": [],
            "job_roles": [],
            "score": 0,
            "suggestions": [
                "AI returned an invalid response. Please try uploading the resume again."
            ]
        }

    except Exception as e:

        print("❌ AI ERROR:", e)

        return {
            "name": "Not mentioned",
            "education": [],
            "skills": [],
            "experience": [],
            "job_roles": [],
            "score": 0,
            "suggestions": [
                "Unable to analyze the resume.",
                str(e)
            ]
        }