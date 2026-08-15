from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

print("=" * 50)
print("Key Found :", key is not None)
print("Key Prefix:", key[:12] if key else "None")
print("Key Length:", len(key) if key else 0)
print("=" * 50)

client = OpenAI(api_key=key)

try:
    models = client.models.list()
    print("SUCCESS")
    for m in models.data[:10]:
        print(m.id)
except Exception as e:
    print(e)