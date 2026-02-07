"""
Configuration file for Smart Resume Analyzer
"""
import os

# Flask Configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
UPLOAD_FOLDER = 'uploads/resumes'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'pdf'}

# NLP Configuration
SPACY_MODEL = 'en_core_web_sm'

# Matching Configuration
MIN_SIMILARITY_THRESHOLD = 0.0  # Minimum similarity score to consider

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

