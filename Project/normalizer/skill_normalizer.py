from config.skills import SKILLS


class SkillNormalizer:

    def __init__(self):
        self.lookup = {}

        for canonical, aliases in SKILLS.items():

            for alias in aliases:

                self.lookup[alias.lower()] = canonical

    def normalize(self, skills):

        normalized = set()

        for skill in skills:

            key = skill.lower().strip()

            if key in self.lookup:

                normalized.add(self.lookup[key])

            else:

                normalized.add(key)

        return list(normalized)