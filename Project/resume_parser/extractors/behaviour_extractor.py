def extract_behaviour_preferences(text):

    behaviour = {}

    lower = text.lower()

    if "notice period" in lower:

        behaviour["notice_period"] = True

    if "active" in lower:

        behaviour["recent_activity"] = True

    if "response rate" in lower:

        behaviour["response_rate"] = True

    return behaviour


def extract_candidate_behaviour(candidate):

    return {

        "last_active":

            candidate['redrob_signals'].get("last_active_date"),

        "notice_period":

            candidate['redrob_signals'].get("notice_period_days"),

        "response_rate":

            candidate['redrob_signals'].get("recruiter_response_rate"),

        "profile_completion":

            candidate['redrob_signals'].get("profile_completeness_score"),

        "open_to_work":

            candidate['redrob_signals'].get("open_to_work_flag"),

        "verified":

            candidate['redrob_signals'].get("verified_phone")
    }