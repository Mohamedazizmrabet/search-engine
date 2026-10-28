"""Steps 2–4 — Lexical analysis, stopword removal, normalization (English).
Owner: Member B
"""
import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def lowercase(text: str) -> str:
    """"Base Militaire" → "base militaire"  (slide 20)."""
    return text.lower()


def remove_accents(text: str) -> str:
    """"café" → "cafe", and PDF ligatures "ﬁ" → "fi"  (slide 20)."""
    decomposed = unicodedata.normalize("NFKD", text)
    result = ""
    for c in decomposed:
        if unicodedata.category(c) != "Mn":
            result = result + c
    return result


def tokenize(text: str) -> list[str]:
    """Split on anything that is not a letter.
    "it's an e-mail." → ["it", "s", "an", "e", "mail"]
    """
    tokens = re.findall(r"[a-z]+", text)
    return tokens


def remove_stopwords(tokens: list[str]) -> list[str]:
    """Drop English stopwords and 1-letter tokens ("s", "t")."""
    stop = stopwords.words("english")
    kept = []
    for t in tokens:
        if len(t) > 1 and t not in stop:
            kept.append(t)
    return kept


def stem(tokens: list[str]) -> list[str]:
    """Porter stemming (slide 31): "retrieving" → "retriev"."""
    stemmer = PorterStemmer()
    stems = []
    for t in tokens:
        stems.append(stemmer.stem(t))
    return stems


def process(text: str) -> list[str]:
    """Full pipeline for one document (or a query)."""
    text = lowercase(text)
    text = remove_accents(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stem(tokens)
    return tokens


if __name__ == "__main__":
    sample = "The retrieval system is retrieving the ﬁles it retrieved."
    print(process(sample))