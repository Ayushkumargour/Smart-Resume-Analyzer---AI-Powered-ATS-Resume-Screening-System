# 🔍 Smart Resume Analyzer

A production-ready, AI-powered web application that analyzes resumes against job descriptions using Natural Language Processing (NLP) and machine learning techniques. This project simulates an Applicant Tracking System (ATS) to help job seekers understand how well their resume matches a job description.

## ✨ Features

- **PDF Resume Parsing**: Extracts text from multi-page PDF resumes using PyPDF2
- **NLP-Based Skill Extraction**: Uses spaCy to identify technical skills from resume text
- **Intelligent Matching**: Employs TF-IDF vectorization and cosine similarity to calculate match scores
- **Comprehensive Skill Database**: Includes 200+ technical skills across programming languages, frameworks, databases, cloud platforms, and more
- **Modern Web UI**: Clean, responsive interface with real-time analysis results
- **Detailed Analysis**: Shows matched skills, missing skills, and overall compatibility percentage

## 🛠️ Tech Stack

- **Python 3.12**: Core programming language
- **Flask**: Web framework for the backend
- **spaCy**: Natural Language Processing for skill extraction
- **PyPDF2**: PDF text extraction
- **NLTK**: Text preprocessing utilities
- **scikit-learn**: TF-IDF vectorization and cosine similarity calculations
- **HTML/CSS**: Frontend interface

## 📁 Project Structure

```
Smart-Resume-Analyzer/
│
├── app.py                 # Flask application with routes
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
│
├── modules/
│   ├── resume_parser.py   # PDF text extraction
│   ├── skill_extractor.py # NLP-based skill extraction
│   ├── matcher.py         # TF-IDF and similarity matching
│   └── skill_db.py        # Skills database
│
├── templates/
│   └── index.html         # Frontend HTML
│
├── static/
│   └── style.css          # CSS styling
│
├── uploads/
│   └── resumes/           # Temporary storage for uploaded PDFs
│
└── README.md              # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd Smart-Resume-Analyzer
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download spaCy English Model

```bash
python -m spacy download en_core_web_sm
```

This is **required** for the NLP functionality to work.

## 🎯 How to Run

1. **Activate your virtual environment** (if using one)

2. **Start the Flask application**:

```bash
python app.py
```

3. **Open your browser** and navigate to:

```
http://localhost:5000
```

4. **Upload a resume PDF** and **paste a job description**, then click "Analyze Resume"

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main-interface.png)

### Analysis Results
![Results](screenshots/results.png)

*Note: Add your own screenshots after running the application*

## 🔧 How It Works

1. **Resume Upload**: User uploads a PDF resume file
2. **Text Extraction**: PyPDF2 extracts all text from the PDF
3. **Skill Extraction**: spaCy NLP model identifies technical skills from the resume text by matching against a comprehensive skills database
4. **Job Description Analysis**: The same skill extraction process is applied to the job description
5. **Matching Algorithm**: 
   - TF-IDF vectorization converts both texts into numerical vectors
   - Cosine similarity calculates the match percentage
   - Skills are compared to identify matches and gaps
6. **Results Display**: The web interface shows match percentage, matched skills, missing skills, and all extracted skills

## 📊 Example Output

- **Match Percentage**: 75.5%
- **Matched Skills**: Python, Flask, PostgreSQL, Docker, AWS
- **Missing Skills**: Kubernetes, React, GraphQL
- **Resume Skills**: [All skills found in resume]
- **JD Skills**: [All skills found in job description]

## 🎨 Features in Detail

### Skill Database
The `skill_db.py` module contains a comprehensive database of technical skills including:
- Programming languages (Python, Java, JavaScript, etc.)
- Web frameworks (Flask, Django, React, Angular, etc.)
- Databases (PostgreSQL, MongoDB, Redis, etc.)
- Cloud platforms (AWS, Azure, GCP, etc.)
- DevOps tools (Docker, Kubernetes, Jenkins, etc.)
- Data Science & ML tools (TensorFlow, PyTorch, scikit-learn, etc.)

### NLP Processing
- Uses spaCy's English model for tokenization and text processing
- Matches skills using pattern recognition and database lookup
- Handles multi-word skills and variations

### Matching Algorithm
- TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- Cosine similarity for semantic matching
- N-gram analysis (unigrams, bigrams, trigrams) for better accuracy

## 🐛 Troubleshooting

### Issue: spaCy model not found
**Solution**: Run `python -m spacy download en_core_web_sm`

### Issue: PDF text extraction fails
**Solution**: Ensure the PDF contains selectable text (not scanned images). Use OCR for scanned PDFs.

### Issue: Port 5000 already in use
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: Import errors
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 🔒 Security Notes

- Change the `SECRET_KEY` in `config.py` for production use
- Implement file size limits (currently 16MB)
- Add authentication for production deployment
- Validate and sanitize all user inputs
- Consider using environment variables for sensitive configuration

## 🚀 Future Enhancements

- [ ] Support for DOCX and TXT file formats
- [ ] OCR integration for scanned PDFs
- [ ] Resume improvement suggestions
- [ ] Export analysis results as PDF
- [ ] User authentication and resume history
- [ ] Advanced NLP models (BERT, GPT-based)
- [ ] Industry-specific skill databases
- [ ] Resume scoring breakdown by category
- [ ] Integration with job boards APIs
- [ ] Multi-language support

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Built with ❤️ using Python, Flask, and AI/ML technologies.

## 🙏 Acknowledgments

- spaCy team for excellent NLP library
- scikit-learn for machine learning utilities
- Flask community for the web framework
- All open-source contributors

---

**Note**: This project is designed for educational and portfolio purposes. For production use, consider additional security measures, error handling, and scalability improvements.

## 📧 Contact

For questions or contributions, please open an issue on GitHub.

---

⭐ **Star this repo if you find it helpful!** ⭐

