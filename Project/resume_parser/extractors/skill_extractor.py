import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config.skills import SKILLS


def extract_skills(text):

    mandatory = []

    preferred = []

    lower = text.lower()

    for skill in SKILLS:

        if skill in lower:

            if "must" in lower:

                mandatory.append(skill)

            else:

                preferred.append(skill)

    return {

        "mandatory": sorted(set(mandatory)),

        "preferred": sorted(set(preferred))
    }



from config.skills import SKILLS


def extract_candidate_skills(candidate):

    raw_skills = candidate.get("skills", [])

    normalized = []

    for skill in raw_skills:

        skill = skill.get("name") if isinstance(skill, dict) else skill

        if skill:
            skill = skill.lower()  # Now it's safely a string!
        else:
            continue

        for canonical, aliases in SKILLS.items():

            if skill in aliases:

                normalized.append(canonical)

                break

    return sorted(set(normalized))