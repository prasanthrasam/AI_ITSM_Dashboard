from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file.")

print(f"✅ API Key Loaded: {api_key[:12]}...")

# Create OpenAI client
client = OpenAI(api_key=api_key)


def generate_ai_summary(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced IT Service Management consultant. "
                        "Analyze incident data and provide concise executive insights "
                        "and recommendations."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.3,
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ OpenAI Error: {str(e)}"