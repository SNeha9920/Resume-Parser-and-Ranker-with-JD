from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingMatcher:

    def match(self, jd, candidate):

        score = cosine_similarity(

            [jd["embedding"]],

            [candidate["embedding"]]

        )[0][0]

        return float(score)