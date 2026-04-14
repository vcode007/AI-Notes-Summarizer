from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors
import os
import time
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

INPUT_DIR = Path("input_files")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)  # create outputs folder if missing


def summarize_text(raw_text: str) -> dict:
    prompt = f"""
Return the summary as a JSON object with three keys: 'title', 'key_points' (a list), and 'sentiment' (a single word).

Notes:
{raw_text}
"""

    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={"response_mime_type": "application/json"},
            )
            return json.loads(response.text)

        except errors.ServerError as e:
            if "503" in str(e) and attempt < max_attempts:
                print(f"Attempt {attempt} failed with 503. Retrying in 5 seconds...")
                time.sleep(5)
                attempt += 1
            else:
                raise


# Loop through every .txt file in input_files
for txt_path in INPUT_DIR.glob("*.txt"):
    raw_text = txt_path.read_text(encoding="utf-8").strip()
    if not raw_text:
        print(f"Skipping empty file: {txt_path.name}")
        continue

    summary_data = summarize_text(raw_text)

    # Output file name: file1.txt -> file1_summary.json
    out_path = OUTPUT_DIR / f"{txt_path.stem}_summary.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    print(f"Saved: {out_path}")