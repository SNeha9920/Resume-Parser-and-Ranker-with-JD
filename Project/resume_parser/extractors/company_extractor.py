def extract_company_preferences(text):

    lower = text.lower()

    preference = {

        "preferred": [],

        "avoid": []
    }

    if "product company" in lower:

        preference["preferred"].append("Product")

    if "consulting" in lower:

        preference["avoid"].append("Consulting")

    if "research" in lower:

        preference["avoid"].append("Research")

    return preference




def extract_candidate_companies(candidate):

    companies = []

    for exp in candidate.get("career_history", []):

        companies.append({

            "company":

                exp.get("company"),

            "designation":

                exp.get("title"),

            "duration":

                exp.get("duration_months")
        })

    return companies