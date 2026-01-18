import streamlit as st
import os
import PyPDF2 as pdf

from dotenv import load_dotenv
from groq import Groq

# 1. Configuration
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_groq_response(resume_text, job_description):

    prompt = f"""
Act as an expert HR Manager with 20 years of experience.
Analyze the following Resume against the Job Description.

Resume Text: {resume_text}
Job Description: {job_description}

Provide the output in the EXACT format:
-Match Percentage: (e.g., 85%)
-Missing Keywords: (List specific technical/soft skills missing)
-Profile Improvement: (Specific advice to close the gap)
"""
    
    completion = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [{"role": "user", "content": prompt}],
        temperature= 0.5,
    )
    return completion.choices[0].message.content

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

# 2. Streamlit UI
st.set_page_config(page_title="AI Resume Intelligence", page_icon=":robot:")
st.header("Smart Resume Analyzer (Powered by Groq)")

jd = st.text_area("Paste the Job Description (JD):")
uploaded_file = st.file_uploader("Upload your Resume (PDF):", type ="pdf")

if st.button("Analyze Match"):
    if uploaded_file and jd:
        with st.spinner("AI is analyzing your Profile..."):
            resume_text = input_pdf_text(uploaded_file)
            analysis = get_groq_response(resume_text, jd)
            st.subheader("Analysis Results:")
            st.write(analysis)
    else:
        st.error("Please upload a Resume and paste a Job first.")
