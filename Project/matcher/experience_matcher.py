class ExperienceMatcher:

    def match(self, jd, candidate):

        required = jd["experience"]["minimum"]

        actual = candidate["experience"]["years"]

        if actual >= required:
            return 1

        return actual / required