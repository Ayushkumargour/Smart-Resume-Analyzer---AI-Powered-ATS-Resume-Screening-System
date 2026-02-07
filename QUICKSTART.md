# Quick Start Guide

## 🚀 Fast Setup (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download spaCy Model (REQUIRED)
```bash
python -m spacy download en_core_web_sm
```

### 3. Run the Application
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

## ✅ That's it!

The application is now running and ready to analyze resumes.

## 📝 Testing

1. Upload a PDF resume (make sure it has selectable text, not scanned)
2. Paste a job description
3. Click "Analyze Resume"
4. View your match score and skills analysis

## 🐛 Common Issues

**Issue**: `spacy.errors.OSError: Can't find model 'en_core_web_sm'`
**Fix**: Run `python -m spacy download en_core_web_sm`

**Issue**: Port 5000 already in use
**Fix**: Change port in `app.py` line 185: `app.run(debug=True, host='0.0.0.0', port=5001)`

**Issue**: PDF extraction fails
**Fix**: Ensure PDF has selectable text (not an image scan). Use a text-based PDF.

## 📦 Project Structure

```
Smart-Resume-Analyzer/
├── app.py              # Main Flask application
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── modules/            # Core modules
├── templates/          # HTML templates
├── static/             # CSS files
└── uploads/            # Upload directory
```

## 🎯 Next Steps

- Add your own resume PDFs for testing
- Customize skills in `modules/skill_db.py`
- Deploy to production (Heroku, AWS, etc.)
- Add screenshots to README.md

---

**Happy Analyzing! 🎉**

