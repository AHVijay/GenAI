import streamlit as st
import os
import PyPDF2 as pdf
import docx

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

def extract_text_from_file(uploaded_file):
    """Extract text from PDF, DOCX, or TXT files"""
    filename = uploaded_file.name.lower()
    
    if filename.endswith('.pdf'):
        # PDF extraction
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text
        
    elif filename.endswith('.docx'):
        # DOCX extraction
        doc = docx.Document(uploaded_file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
        
    elif filename.endswith('.txt'):
        # TXT extraction
        return str(uploaded_file.read(), "utf-8")
    
    else:
        return None

# 2. Streamlit UI
st.set_page_config(page_title="AI Resume Intelligence", page_icon=":robot:")
st.header("Smart Resume Analyzer (Multi-Format Support)")

jd = st.text_area("Paste the Job Description (JD):")

# File uploader with accept parameter for better file type filtering
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF, DOCX, or TXT):", 
    type=None,  # Accept all files
    accept_multiple_files=False,
    help="Supported formats: PDF, DOCX (Word), TXT"
)

if st.button("Analyze Match"):
    if uploaded_file and jd:
        # Validate file type
        valid_extensions = ['.pdf', '.docx', '.txt']
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()
        
        if file_ext not in valid_extensions:
            st.error(f"❌ Unsupported file format: {file_ext}. Please upload PDF, DOCX, or TXT.")
        else:
            with st.spinner("AI is analyzing your Profile..."):
                resume_text = extract_text_from_file(uploaded_file)
                
                if resume_text:
                    analysis = get_groq_response(resume_text, jd)
                    st.subheader("Analysis Results:")
                    st.write(analysis)
                else:
                    st.error("❌ Could not extract text from file. Please check the file format.")
    else:
        st.error("Please upload a Resume and paste a Job Description first.")
