"""
language_extractor.py

Extracts spoken/programming languages if available.
"""


def extract_candidate_languages(candidate):

    languages = []

    for lang in candidate.get("languages", []):

        if isinstance(lang, dict):

            languages.append({
                "language": lang.get("language"),
                "proficiency": lang.get("proficiency")
            })

        else:
            languages.append({
                "language": lang,
                "proficiency": None
            })

    return languages