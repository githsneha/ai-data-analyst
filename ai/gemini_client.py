# ai/gemini_client.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt):

    try:
        response = model.generate_content(prompt)

        if not response or not hasattr(response, "text"):
            raise ValueError("Empty response from Gemini")

        return response.text.strip()

    except Exception as e:
        # IMPORTANT: do NOT return fake SQL/text
        raise RuntimeError(f"Gemini API failed: {str(e)}")