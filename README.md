# 🤖 Smart Resume Analyzer (Powered by Groq)

An intelligent resume analysis tool that uses AI to match your resume against job descriptions and provides actionable insights for improvement.

## ✨ Features

- 📄 **PDF Resume Upload** - Easily upload your resume in PDF format
- 🔍 **Job Description Analysis** - Paste the job description you're targeting
- 🎯 **Smart Matching** - AI-powered analysis using Groq's Llama 3.3 70B model
- 📊 **Detailed Report** - Get insights including:
  - Match Percentage - How well your resume aligns with the job
  - Missing Keywords - Technical and soft skills you're lacking
  - Profile Improvement - Specific, actionable advice to improve your chances

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Modern Python web framework
- **LLM**: [Groq API](https://groq.com/) - Fast inference with Llama 3.3 70B
- **PDF Processing**: PyPDF2
- **Environment**: Python 3.x

## 📋 Requirements

- Python 3.8+
- All dependencies listed in `requirements.txt`:
  - groq
  - python-dotenv
  - streamlit
  - PyPDF2

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Resume_Analyzer_Groq
   ```

2. **Create and activate a virtual environment** (already set up):
   ```bash
   .\resume_venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Activate the virtual environment**:
   ```bash
   .\resume_venv\Scripts\Activate.ps1
   ```

2. **Navigate to the app directory**:
   ```bash
   cd resume_venv
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**:
   - The app will automatically open at `http://localhost:8501`

5. **Use the analyzer**:
   - Paste the job description in the text area
   - Upload your resume (PDF format)
   - Click "Analyze Match" to get your analysis report

## 📁 Project Structure

```
Resume_Analyzer_Groq/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── resume_venv/             # Virtual environment
│   ├── app.py               # Main Streamlit application
│   ├── Scripts/             # Activation scripts
│   └── Lib/                 # Python packages
└── .env                     # Environment variables (not tracked)
```

## 🔑 Configuration

The application uses the Groq API for AI analysis. The API key is configured in `app.py` (in production, use environment variables).

### Model Used
- **Model**: Llama 3.3 70B Versatile
- **Temperature**: 0.5 (balanced between creativity and consistency)

## 📊 Output Format

The analysis provides results in the following format:

```
-Match Percentage: 85%
-Missing Keywords: [List of missing skills]
-Profile Improvement: [Specific recommendations]
```

## 💡 Tips for Best Results

- Use a well-formatted, detailed resume
- Include specific keywords from the job description
- Ensure your resume highlights relevant projects and experience
- Use the feedback to iteratively improve your resume

## 🐛 Troubleshooting

### API Issues
- Verify your Groq API key is valid
- Check internet connection
- Ensure API rate limits haven't been exceeded

### PDF Upload Issues
- Ensure the PDF is readable and not corrupted
- Try with a smaller PDF file first

## 📝 Future Enhancements

- [ ] Support for multiple file formats (DOCX, TXT)
- [ ] Resume template suggestions
- [ ] Skill gap analysis with learning resources
- [ ] Integration with RAG (Retrieval-Augmented Generation) for more        accurate skill extraction.
- [ ] Export analysis reports as PDF

---
