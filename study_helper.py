import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
def get_key():
    key=os.getenv("GEMINI_API_KEY")
    if key:
        return key
    return st.secrets["GEMINI_API_KEY"]
client=genai.Client(api_key=get_key())
st.title("AI study helper")
st.write("paste your notes and get a summary plus a quiz.")
text=st.text_area("paste your study notes here",height=200)
if st.button("generate"):
    if not text.strip():
        st.warning("Please enter some text to generate a summary and quiz.")
    else:
        with st.spinner("thinking..."):
            prompt=(
                "Summarize the following notes in 4 short bullet points:"
                "then write 5 quiz questions with answers.\n\n"+ text
            )
            response=client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
            )
        st.markdown(response.text)