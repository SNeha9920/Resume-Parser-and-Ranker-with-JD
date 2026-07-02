def extract_responsibilities(text):

    keywords = [

        "ranking",

        "retrieval",

        "search",

        "evaluation",

        "mentoring",

        "deployment",

        "experimentation"
    ]

    found = []

    lower = text.lower()

    for word in keywords:

        if word in lower:

            found.append(word)

    return found