import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

if not GEMINI_MODEL:
    raise ValueError("GEMINI_MODEL not found")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str):

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text