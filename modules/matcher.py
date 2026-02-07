"""
Matcher Module
Uses TF-IDF and cosine similarity to match resume against job description
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
from modules.skill_extractor import extract_skills


def calculate_match_score(resume_text: str, job_description: str) -> Dict:
    """
    Calculates match score between resume and job description
    
    Args:
        resume_text: Extracted resume text
        job_description: Job description text
        
    Returns:
        Dictionary containing:
        - match_percentage: Similarity score (0-100)
        - matched_skills: Skills found in both resume and JD
        - missing_skills: Skills in JD but not in resume
        - resume_skills: All skills found in resume
        - jd_skills: All skills found in job description
    """
    if not resume_text or not job_description:
        return {
            'match_percentage': 0.0,
            'matched_skills': [],
            'missing_skills': [],
            'resume_skills': [],
            'jd_skills': []
        }
    
    # Extract skills from both documents
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description.lower())
    
    # Calculate TF-IDF similarity
    documents = [resume_text, job_description]
    
    # Create TF-IDF vectorizer
    # Use ngram_range to capture phrases and technical terms
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 3),  # Unigrams, bigrams, and trigrams
        max_features=5000,
        stop_words='english',
        lowercase=True,
        strip_accents='unicode'
    )
    
    try:
        # Fit and transform documents
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        similarity_score = similarity_matrix[0][0]
        
        # Convert to percentage (0-100)
        match_percentage = round(similarity_score * 100, 2)
        
    except Exception as e:
        print(f"Error calculating similarity: {str(e)}")
        match_percentage = 0.0
    
    # Find matched and missing skills
    resume_skills_set = set(resume_skills)
    jd_skills_set = set(jd_skills)
    
    matched_skills = sorted(list(resume_skills_set.intersection(jd_skills_set)))
    missing_skills = sorted(list(jd_skills_set - resume_skills_set))
    
    return {
        'match_percentage': match_percentage,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'resume_skills': sorted(resume_skills),
        'jd_skills': sorted(jd_skills)
    }


def get_match_analysis(resume_text: str, job_description: str) -> Dict:
    """
    Comprehensive match analysis between resume and job description
    
    Args:
        resume_text: Extracted resume text
        job_description: Job description text
        
    Returns:
        Complete analysis dictionary
    """
    return calculate_match_score(resume_text, job_description)

