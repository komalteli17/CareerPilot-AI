import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

client = OpenAI(api_key=api_key)


def ask_ai(prompt):

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text