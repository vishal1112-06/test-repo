# AI Study Helper

Paste your study notes and get a short summary plus a 5-question quiz, powered by Google Gemini.

**Live app:** https://vishal-study-buddy.streamlit.app

## Features
- Summarizes notes into 4 bullet points
- Generates 5 quiz questions with answers

## Tech stack
- Python
- Streamlit
- Google Gemini API (google-genai)

## Run locally
1. `pip install -r requirements.txt`
2. Create a `.env` file with `GEMINI_API_KEY=your_key`
3. `python -m streamlit run study_helper.py`

Built by Vishal