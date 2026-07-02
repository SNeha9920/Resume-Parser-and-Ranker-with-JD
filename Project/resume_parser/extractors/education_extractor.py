"""
education_extractor.py

Extracts education details from candidate profile.
"""


def extract_candidate_education(candidate):

    education = []

    for edu in candidate.get("education", []):

        education.append({
            "degree": edu.get("degree"),
            "specialization": edu.get("field_of_study"),
            "institution": edu.get("institution"),
            "year": edu.get("end_year"),
            "cgpa": edu.get("grade").split(' ')[0]
        })

    return education