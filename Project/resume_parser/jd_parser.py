"""
jd_parser.py

Converts a raw Job Description into a structured JSON.

Pipeline

Raw JD
    ↓
Cleaning
    ↓
Extract Title
Extract Experience
Extract Skills
Extract Responsibilities
Extract Location
Extract Preferences
Extract Negative Signals
Extract Behaviour Signals
    ↓
Normalize
    ↓
Structured JD JSON
"""
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from extractors.title_extractor import extract_title
from extractors.experience_extractor import extract_experience
from extractors.skill_extractor import extract_skills
from extractors.location_extractor import extract_locations
from extractors.company_extractor import extract_company_preferences
from extractors.responsibility_extractor import extract_responsibilities
from extractors.behaviour_extractor import extract_behaviour_preferences
from extractors.negative_extractor import extract_negative_signals
from extractors.embedding_extractor import generate_embedding

from preprocess import clean_text


class JDParser:

    def __init__(self):
        pass

    def parse(self, jd_text: str):

        text = clean_text(jd_text)

        jd = {

            "title": extract_title(text),

            "experience": extract_experience(text),

            "skills": extract_skills(text),

            "locations": extract_locations(text),

            "company_preferences":
                extract_company_preferences(text),

            "responsibilities":
                extract_responsibilities(text),

            "behaviour":
                extract_behaviour_preferences(text),

            "negative_signals":
                extract_negative_signals(text)
        }

        embedding_text = " ".join(
            jd["skills"]["mandatory"] +
            jd["skills"]["preferred"] +
            jd["responsibilities"]
        )

        jd["embedding"] = generate_embedding(embedding_text)


        return jd