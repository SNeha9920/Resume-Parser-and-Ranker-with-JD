"""
certification_extractor.py

Extracts certifications from candidate profile.
"""


def extract_candidate_certifications(candidate):

    certifications = []

    for cert in candidate.get("certifications", []):

        certifications.append({
            "name": cert.get("name"),
            "issuer": cert.get("issuer"),
            "year": cert.get("year")
        })

    return certifications