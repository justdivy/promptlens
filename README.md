# 🔍 PromptLens — Prompt Engineering Analyzer

A Python + Flask web app that analyzes, scores, and optimizes AI prompts using the Claude API.

## 📁 Project Structure

```
promptlens/
├── app.py              ← Flask backend (Python)
├── requirements.txt    ← Dependencies
├── README.md
└── templates/
    └── index.html      ← Frontend UI
```

## ⚙️ Setup & Run

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Set your Anthropic API Key
**Windows (CMD):**
```cmd
set ANTHROPIC_API_KEY=your_api_key_here
```
**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
```
http://localhost:5000
```

## 🎯 Features

- **Overall Score (0–100)** with grade: Excellent / Good / Average / Weak
- **4 Dimension Scores** — Clarity, Specificity, Task Alignment, Context Richness
- **Technique Detection** — Zero-shot, Few-shot, Chain-of-thought, Role-based, etc.
- **Issues & Strengths** list
- **Before/After Comparison** — Original vs AI-optimized prompt

## 📚 Syllabus Coverage

| Feature | Topic |
|---|---|
| Prompt scoring & optimization | Unit-II: Prompt Engineering Basics |
| Zero-shot / Few-shot detection | Unit-II: Advanced Techniques |
| Chain-of-thought identification | Unit-II: Advanced Techniques |
| NLG for optimized prompt | Unit-I: NLG & NLU |
| Metrics for quality/relevance | Unit-II: Metrics to assess LLM responses |

## 🔑 Get API Key
1. Go to https://console.anthropic.com
2. Sign up / Log in
3. Create an API key
4. Use it in Step 2 above
