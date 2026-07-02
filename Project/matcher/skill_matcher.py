class SkillMatcher:

    def match(self, jd, candidate):

        jd_skills = set(jd["skills"]["mandatory"])

        candidate_skills = set(candidate["skills"])

        matched = jd_skills & candidate_skills

        if len(jd_skills) == 0:
            return 0

        return len(matched) / len(jd_skills)