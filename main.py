from pyexpat.errors import messages
import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
print(f"key ", os.getenv("GOOGLE_API_KEY"))
print("Attempting to initialize model...")
model = genai.GenerativeModel('gemini-2.0-flash')
print("Model initialized.")

st.set_page_config(page_title="Gemini Q&A", layout="centered")
st.title("💬 Ask Me Anything (Gemini AI)")

user_input = st.text_area("Enter your question:")

if st.button("Get Answer") and user_input.strip() != "":
    with st.spinner("Thinking..."):
        print("Sending request to Gemini API...")
        response = model.generate_content(user_input)
        st.write("### Answer:")
        st.write(response.text)