import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Ensure UTF-8 console output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not found in .env file.")
    sys.exit(1)

client = Groq(api_key=api_key)

print("\n==========================================")
print("       AVAILABLE GROQ MODELS LIST         ")
print("==========================================")
try:
    models = client.models.list()
    for idx, model in enumerate(models.data, 1):
        owned_by = getattr(model, "owned_by", "groq")
        print(f" {idx:2d}. {model.id:<38} (owned by: {owned_by})")
    print("==========================================\n")
    print(f"Total available models: {len(models.data)}\n")
except Exception as e:
    print(f"Failed to fetch models: {e}")
