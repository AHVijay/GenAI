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
  - streamlit
  - PyPDF2
  - python-docx

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Resume_Analyzer_Groq
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv resume_venv
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

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open in browser**:
   - The app will automatically open at `http://localhost:8501`

4. **Use the analyzer**:
   - Paste the job description in the text area
   - Upload your resume (PDF, DOCX, or TXT format)
   - Click "Analyze Match" to get your analysis report

## 📁 Project Structure

```
Resume_Analyzer_Groq/
├── app.py                    # Main Streamlit application
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
├── .env.example              # Environment variables template
├── .env                      # Environment variables (local, not tracked)
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── resume_venv/              # Virtual environment (not committed)
    ├── Scripts/              # Activation scripts
    └── Lib/                  # Python packages
```

## 🔑 Configuration

The application uses the Groq API for AI analysis. The API key is securely stored in `.env` file (never commit this file).

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

- Use a well-formatted, detailed resume
- Include specific keywords from the job description
- Ensure your resume highlights relevant projects and experience
- Use the feedback to iteratively improve your resume

## 🐛 Troubleshooting

### API Issues
- Verify your Groq API key is valid
- Check internet connection
- Ensure API rate limits haven't been exceeded

### File Upload Issues
- **PDF**: Ensure the file is readable and not corrupted
- **DOCX**: Verify it's a valid Microsoft Word document
- **TXT**: Make sure it's encoded in UTF-8
- Try with a smaller file first if upload fails

## 📝 Future Enhancements

- [x] Support for multiple file formats (DOCX, TXT) ✅ Completed!
- [ ] Resume template suggestions
- [ ] Skill gap analysis with learning resources
- [ ] Batch processing multiple resumes
- [ ] Integration with RAG (Retrieval-Augmented Generation) for accurate skill extraction
- [ ] Export analysis reports as PDF
- [ ] Resume scoring history and comparison

<<<<<<< HEAD
## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/GenAI.git
cd GenAI

# Set up environment
python -m venv resume_venv
.\resume_venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set up API key
echo GROQ_API_KEY=your_key_here > .env

# Run the app
streamlit run app.py
```

=======
## 📝 Future Enhancements
- [ ] Resume template suggestions
- [ ] Skill gap analysis with learning resources
- [ ] Integration with RAG (Retrieval-Augmented Generation) for more        accurate skill extraction.
- [ ] Export analysis reports as PDF

Thank You
>>>>>>> a85fca13b891bd8be7bc2d712d78d38f793c7023
