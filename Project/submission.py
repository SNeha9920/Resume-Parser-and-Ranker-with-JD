import csv

from reasoning_generator import generate_reasoning


def save_submission(jd, ranked_candidates, filename):

    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ])

        for candidate in ranked_candidates[:100]:

            writer.writerow([
                candidate["candidate_id"],
                candidate["rank"],
                round(candidate["score"], 3),
                generate_reasoning(jd, candidate)
            ])