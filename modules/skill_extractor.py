"""
Skill Extractor Module
Uses spaCy NLP to extract skills from resume text
"""

import spacy
import re
from typing import List, Set
from modules.skill_db import SKILLS_DATABASE


# Load spaCy model (will be loaded on first use)
_nlp_model = None


def load_spacy_model():
    """
    Loads the spaCy English model
    Uses lazy loading to avoid loading on import
    """
    global _nlp_model
    if _nlp_model is None:
        try:
            _nlp_model = spacy.load("en_core_web_sm")
        except OSError:
            raise Exception(
                "spaCy model 'en_core_web_sm' not found. "
                "Please install it using: python -m spacy download en_core_web_sm"
            )
    return _nlp_model


def extract_skills(resume_text: str) -> List[str]:
    """
    Extracts skills from resume text by matching against skills database
    
    Args:
        resume_text: Cleaned resume text (lowercase)
        
    Returns:
        List of extracted skills (unique, sorted)
    """
    if not resume_text:
        return []
    
    # Load spaCy model
    nlp = load_spacy_model()
    
    # Process text with spaCy
    doc = nlp(resume_text.lower())
    
    # Extract tokens and phrases
    tokens = [token.text.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    
    # Extract noun phrases (often contain skill names)
    noun_phrases = [chunk.text.lower().strip() for chunk in doc.noun_chunks]
    
    # Combine tokens and phrases
    all_text_units = tokens + noun_phrases
    
    # Also check for multi-word skills by looking at the original text
    text_lower = resume_text.lower()
    
    # Find matching skills
    matched_skills = set()
    
    # Sort skills by length (longest first) to match multi-word skills first
    sorted_skills = sorted(SKILLS_DATABASE, key=len, reverse=True)
    
    for skill in sorted_skills:
        # Check if skill appears in text
        # Use word boundaries for single words, flexible matching for phrases
        if len(skill.split()) == 1:
            # Single word: use word boundary
            pattern = r'\b' + re.escape(skill) + r'\b'
        else:
            # Multi-word: flexible matching
            pattern = re.escape(skill)
        
        if re.search(pattern, text_lower, re.IGNORECASE):
            matched_skills.add(skill)
    
    # Also check tokens directly
    for token in tokens:
        if token in SKILLS_DATABASE:
            matched_skills.add(token)
    
    # Check noun phrases
    for phrase in noun_phrases:
        # Check if phrase contains a skill
        for skill in sorted_skills:
            if skill in phrase or phrase in skill:
                matched_skills.add(skill)
    
    # Remove duplicates and return sorted list
    return sorted(list(matched_skills))


def normalize_skill_name(skill: str) -> str:
    """
    Normalizes skill names for consistent matching
    
    Args:
        skill: Raw skill name
        
    Returns:
        Normalized skill name
    """
    # Convert to lowercase and strip whitespace
    normalized = skill.lower().strip()
    
    # Remove special characters but keep hyphens and dots
    normalized = re.sub(r'[^\w\s\.\-]', '', normalized)
    
    # Normalize whitespace
    normalized = re.sub(r'\s+', ' ', normalized)
    
    return normalized.strip()

