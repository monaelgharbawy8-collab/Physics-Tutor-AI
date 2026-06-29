import streamlit as st
import google.generativeai as genai
# ---------------------------
# Gemini API Configuration
# ---------------------------
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------------
# Streamlit Page Settings
# ---------------------------
st.set_page_config(
    page_title="Physics Tutor AI",
    page_icon="⚛️",
    layout="wide"
)

st.title("⚛️ Physics Tutor AI")
st.write("Ask any Physics question and get explanations, formulas, examples, and quizzes.")

# ---------------------------
# Session State
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# User Input
# ---------------------------
question = st.text_input(
    "Ask a Physics Question:",
    placeholder="Example: Explain Newton's Second Law"
)

# ---------------------------
# Generate Response
# ---------------------------
if st.button("Ask AI") and question:

    prompt = f"""
    You are an expert Physics Tutor.

    Answer the following question:

    {question}

    Structure your response as:

    1. Definition
    2. Formula (if applicable)
    3. Explanation
    4. Real-life Example
    5. Practice Question
    """

    response = model.generate_content(prompt)

    answer = response.text

    st.session_state.messages.append(
        {"question": question, "answer": answer}
    )

# ---------------------------
# Chat History
# ---------------------------
for item in reversed(st.session_state.messages):

    st.markdown("---")

    st.markdown(
        f"### 🧑 Student\n{item['question']}"
    )

    st.markdown(
        f"### 🤖 Physics Tutor\n{item['answer']}"
    )

# ---------------------------
# Clear History Button
# ---------------------------
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()