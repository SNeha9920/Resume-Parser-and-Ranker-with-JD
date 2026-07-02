import re


def extract_experience(text):

    result = {

        "minimum": None,

        "maximum": None,

        "flexible": False
    }

    match = re.search(
        r"(\d+)\s*[-–]\s*(\d+)\s*years",
        text,
        flags=re.IGNORECASE
    )

    if match:

        result["minimum"] = int(match.group(1))

        result["maximum"] = int(match.group(2))

        result["flexible"] = True

        return result

    match = re.search(
        r"(\d+)\+?\s*years",
        text,
        flags=re.IGNORECASE
    )

    if match:

        result["minimum"] = int(match.group(1))

    return result




def extract_candidate_experience(candidate):

    return {

        "years": candidate['profile'].get("years_of_experience", 0),

        "current_company":

            candidate['profile'].get("current_company"),

        "designation":

            candidate['profile'].get("current_title")
    }