import re


def clean_text(text):

    text = text.replace("\t", " ")

    text = re.sub(r"\n+", "\n", text)

    text = re.sub(r" +", " ", text)

    return text.strip()