class Ranker:

    def rank(self, scored_candidates):

        ranked = sorted(
            scored_candidates,
            key=lambda x: x["score"],
            reverse=True
        )

        # Assign ranks
        for rank, candidate in enumerate(ranked, start=1):
            candidate["rank"] = rank

        return ranked