"""
candidate_parser.py

Converts a raw candidate record into a structured profile
that can be consumed by the Matching Engine.
"""

from preprocess import clean_text

from extractors.skill_extractor import extract_candidate_skills
from extractors.experience_extractor import extract_candidate_experience
from extractors.education_extractor import extract_candidate_education
from extractors.company_extractor import extract_candidate_companies
from extractors.project_extractor import extract_candidate_projects
from extractors.location_extractor import extract_candidate_location
from extractors.behaviour_extractor import extract_candidate_behaviour
from extractors.certification_extractor import extract_candidate_certifications
from extractors.language_extractor import extract_candidate_languages
from extractors.embedding_extractor import generate_candidate_embedding
from extractors.embedding_extractor import generate_embedding


class CandidateParser:

    def __init__(self):
        pass

    def parse(self, candidate: dict):

        profile = {}

        ###################################################
        # Basic Information
        ###################################################

        profile["candidate_id"] = candidate.get("candidate_id")

        profile["name"] = candidate['profile'].get("anonymized_name")

        ###################################################
        # Experience
        ###################################################

        profile["experience"] = extract_candidate_experience(candidate)

        ###################################################
        # Skills
        ###################################################

        profile["skills"] = extract_candidate_skills(candidate)

        ###################################################
        # Education
        ###################################################

        profile["education"] = extract_candidate_education(candidate)

        ###################################################
        # Companies
        ###################################################

        profile["companies"] = extract_candidate_companies(candidate)

        ###################################################
        # Projects
        ###################################################

        profile["projects"] = extract_candidate_projects(candidate)

        ###################################################
        # Certifications
        ###################################################

        profile["certifications"] = extract_candidate_certifications(candidate)

        ###################################################
        # Languages
        ###################################################

        profile["languages"] = extract_candidate_languages(candidate)

        ###################################################
        # Location
        ###################################################

        profile["location"] = extract_candidate_location(candidate)

        ###################################################
        # Behaviour
        ###################################################

        profile["behaviour"] = extract_candidate_behaviour(candidate)

        ###################################################
        # Embedding
        ###################################################

        embedding_text = " ".join(profile["skills"]+profile["projects"])

        profile["embedding"] = generate_embedding(embedding_text)

        return profile