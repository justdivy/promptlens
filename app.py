import os
import json
import time
from groq import Groq
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load .env
load_dotenv()

app = Flask(__name__)

# API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(" GROQ_API_KEY not found")

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """You are PromptLens, an expert prompt engineering analyzer.

Analyze the user's prompt and return ONLY a valid JSON object.

Return EXACTLY this structure:
{
  "overallScore": 0,
  "detectedTechnique": "",
  "dimensions": [
    {"name": "Clarity", "score": 0, "note": ""},
    {"name": "Specificity", "score": 0, "note": ""},
    {"name": "Task Alignment", "score": 0, "note": ""},
    {"name": "Context Richness", "score": 0, "note": ""}
  ],
  "techniquesDetected": [],
  "techniquesMissing": [],
  "techniqueExplanation": "",
  "issues": [
    {"type": "bad", "title": "", "desc": ""},
    {"type": "warn", "title": "", "desc": ""},
    {"type": "good", "title": "", "desc": ""}
  ],
  "optimizedPrompt": ""
}

Rules:
- Return ONLY JSON
- No explanation
- No markdown
- Fill all fields properly
- Score must be between 0–100
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    prompt_text = data.get("prompt", "").strip()

    if not prompt_text:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        for i in range(3):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",   # ✅ FINAL MODEL
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt_text}
                    ]
                )
                break
            except Exception as e:
                if i == 2:
                    raise e
                time.sleep(2)

        raw = response.choices[0].message.content.strip()

        raw = raw.replace("```json", "").replace("```", "").strip()

        result = json.loads(raw)

        return jsonify(result)

    except Exception as e:  
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)