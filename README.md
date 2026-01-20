# 🤖 Smart Resume Analyzer (Powered by Groq)

An intelligent resume analysis tool that uses AI to match your resume against job descriptions and provides actionable insights for improvement.

## ✨ Features

- 📄 **Multi-Format Resume Upload** - Upload resumes in PDF, DOCX, or TXT format
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
- **Document Processing**: python-docx (for DOCX files)
- **Environment**: Python 3.8+

## 📋 Requirements

- Python 3.8+
- All dependencies listed in `requirements.txt`:
  - groq
  - python-dotenv
  - stream
  - python-docxlit
  - PyPDF2

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Resume_Analyzer_Groq
   ```
:
   ```bash
   python -m venv resume_venve and activate a virtual environment** (already set up):
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
Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open in browser**:
   - The app will automatically open at `http://localhost:8501`

4. **Use the analyzer**:
   - Paste the job description in the text area
   - Upload your resume (PDF, DOCX, or TXTon in the text area
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
│   app.py                    # Main Streamlit application
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
├── .env.example              # Environment variables template
├── .env                      # Environment variables (local, not tracked)
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── resume_venv/              # Virtual environment (not committed)
    ├── Scripts/              # Activation scripts
    └── Lib/                  # Python packagesconfigured in `app.py` (in production, use environment variables).
securely stored in `.env` file (never commit this file).

### Setup API Key
1. Get your Groq API key from [https://console.groq.com/keys](https://console.groq.com/keys)
2. Create a `.env` file in the project root (copy from `.env.example`):
   ```bash
   GROQ_API_KEY=your_api_key_here
   ```
3. Never commit `.env` - it's excluded by `.gitignore`
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

- UsFile Upload Issues
- **PDF**: Ensure the file is readable and not corrupted
- **DOCX**: Verify it's a valid Microsoft Word document
- **TXT**: Make sure it's encoded in UTF-8
- Try with a smaller file first if upload failsevant projects and experience
- Use the feedback to iteratively improve your resume

## 🐛 Troubleshooting

### API Issues
- Vx] Support for multiple file formats (DOCX, TXT) ✅ Completed!
- [ ] Resume template suggestions
- [ ] Skill gap analysis with learning resources
- [ ] Batch processing multiple resumes
- [ ] Integration with RAG (Retrieval-Augmented Generation) for accurate skill extraction
- [ ] Export analysis reports as PDF
- [ ] Resume scoring history and comparison
- Ensure the PDF is readable and not corrupted
- Try with a smaller PDF file first

## 📝 Future Enhancements

- [ ] Support for multiple file formats (DOCX, TXT)
- [ ] Resume template suggestions
- [ ] Skill gap analysis with learning resources
- [ ] Integration with RAG (Retrieval-Augmented Generation) for more        accurate skill extraction.
- [ ] Export analysis reports as PDF

---

# Resume Analyzer Groq - .gitignore

# Python
*.py[cod]
__pycache__/
*.so
*.egg
*.egg-info/
dist/
build/

# Virtual Environment
venv/
ENV/
env/
.env

# IDEs and Editors
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# macOS
.DS_Store

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/

# Groq specific
groq_api_key
groq_model
