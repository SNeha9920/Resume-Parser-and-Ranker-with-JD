from normalizer.skill_normalizer import SkillNormalizer


class CandidateNormalizer:

    def __init__(self):

        self.skill_normalizer = SkillNormalizer()

    def normalize(self, candidate):

        candidate["skills"] = self.skill_normalizer.normalize(
            candidate["skills"]
        )

        return candidate