def generate_reasoning(jd, candidate):

    reasons = []

    # ---------- Skills ----------
    jd_skills = (
        jd.get("skills", {}).get("mandatory", [])
        + jd.get("skills", {}).get("preferred", [])
    )

    jd_skills = set(s.lower() for s in jd_skills)
    candidate_skills = set(s.lower() for s in candidate.get("skills", []))

    matched = jd_skills.intersection(candidate_skills)

    if matched:
        reasons.append(
            f"Matched {len(matched)} key skills ({', '.join(sorted(matched))})"
        )

    # ---------- Semantic Match ----------
    embedding_score = candidate.get("features", {}).get("embedding", 0)

    if embedding_score > 0.8:
        reasons.append("Excellent semantic match with the job description")
    elif embedding_score > 0.6:
        reasons.append("Good semantic match with the job description")
    elif embedding_score > 0.4:
        reasons.append("Moderate semantic relevance")

    # ---------- Experience ----------
    years = candidate.get("experience", {}).get("years", 0)

    if years > 0:
        reasons.append(f"{years} years of experience")

    # ---------- Company ----------
    companies = candidate.get("companies", [])

    if companies:
        reasons.append(
            f"Worked at {companies[0].get('company')}"
        )

    if not reasons:
        reasons.append(
            "Relevant technical profile with partial alignment to the job description."
        )

    reasons = ", ".join(reasons)
    print(reasons)
    return reasons