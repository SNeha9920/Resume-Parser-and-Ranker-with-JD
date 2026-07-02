NEGATIVE_KEYWORDS = [

    "consulting",

    "research",

    "computer vision",

    "speech",

    "robotics",

    "framework enthusiast"
]


def extract_negative_signals(text):

    found = []

    lower = text.lower()

    for item in NEGATIVE_KEYWORDS:

        if item in lower:

            found.append(item)

    return found