"""
Smart Resume Analyzer - Flask Application
Main application file with routes and error handling
"""

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_CONTENT_LENGTH
from modules.resume_parser import get_resume_text
from modules.matcher import get_match_analysis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    """
    Check if file extension is allowed
    
    Args:
        filename: Name of the file
        
    Returns:
        True if allowed, False otherwise
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """
    Main page - displays upload form
    """
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze resume against job description
    
    Handles:
    - File upload validation
    - PDF text extraction
    - Skill matching
    - Error handling
    """
    try:
        # Check if resume file is present
        if 'resume' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No resume file uploaded'
            }), 400
        
        resume_file = request.files['resume']
        job_description = request.form.get('job_description', '').strip()
        
        # Validate inputs
        if resume_file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No file selected'
            }), 400
        
        if not job_description:
            return jsonify({
                'success': False,
                'error': 'Job description is required'
            }), 400
        
        # Validate file type
        if not allowed_file(resume_file.filename):
            return jsonify({
                'success': False,
                'error': 'Invalid file type. Only PDF files are allowed.'
            }), 400
        
        # Save uploaded file
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)
        
        try:
            # Extract text from PDF
            resume_text = get_resume_text(filepath)
            
            if not resume_text:
                return jsonify({
                    'success': False,
                    'error': 'Could not extract text from PDF. Please ensure the PDF contains readable text.'
                }), 400
            
            # Perform matching analysis
            analysis = get_match_analysis(resume_text, job_description)
            
            # Clean up uploaded file (optional - you may want to keep it)
            try:
                os.remove(filepath)
            except:
                pass  # Ignore cleanup errors
            
            # Return results
            return jsonify({
                'success': True,
                'results': {
                    'match_percentage': analysis['match_percentage'],
                    'matched_skills': analysis['matched_skills'],
                    'missing_skills': analysis['missing_skills'],
                    'resume_skills': analysis['resume_skills'],
                    'jd_skills': analysis['jd_skills']
                }
            })
            
        except Exception as e:
            # Clean up file on error
            try:
                os.remove(filepath)
            except:
                pass
            
            return jsonify({
                'success': False,
                'error': f'Error processing resume: {str(e)}'
            }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """
    Handle file size limit exceeded
    """
    return jsonify({
        'success': False,
        'error': 'File size exceeds maximum allowed size (16MB)'
    }), 413


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({
        'success': False,
        'error': 'Page not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("Smart Resume Analyzer - Starting Application")
    print("=" * 60)
    print("\nMake sure you have installed the spaCy model:")
    print("python -m spacy download en_core_web_sm")
    print("\nStarting Flask server...")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)


