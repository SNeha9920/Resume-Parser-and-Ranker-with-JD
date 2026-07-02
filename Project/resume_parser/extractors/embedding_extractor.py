from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_candidate_embedding(profile):

    text = " ".join(

        profile["skills"]

        +

        profile["career_history"]

        +

        profile["certifications"]

        +

        profile["redrob_signals"]

    )

    return model.encode(text)


def generate_embedding(text):
    return model.encode(text)