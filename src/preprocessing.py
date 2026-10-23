"""Steps 2–4 — Lexical analysis, stopword removal, normalization.
Owner: Member B
"""
import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

LANG_NAMES = {"fr": "french", "en": "english"}


def lowercase(text: str) -> str:
    # TODO (B)
    raise NotImplementedError


def remove_accents(text: str) -> str:
    """"école" → "ecole".
    Hint: unicodedata.normalize("NFD", text), then drop characters whose
    unicodedata.category(c) == "Mn" (the accent marks).
    """
    # TODO (B)
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    """Split on anything that is not a letter.
    "l'e-mail de m. dupont" → ["l", "e", "mail", "de", "m", "dupont"]
    Hint: re.findall(r"[a-z]+", text) works once accents are removed.
    Decide as a team whether to keep numbers.
    """
    # TODO (B)
    raise NotImplementedError


def remove_stopwords(tokens: list[str], lang: str) -> list[str]:
    """Remove stopwords using NLTK's list for `lang`.
    Careful: NLTK's French list has accents ("été", "à") — run
    remove_accents() on the list too, or "ete" won't be removed.
    Also drop 1-letter tokens ("l", "d", "m").
    """
    # TODO (B)
    raise NotImplementedError


def stem(tokens: list[str], lang: str) -> list[str]:
    """Snowball stemming: "economistes" → "econom" (French)."""
    # TODO (B): SnowballStemmer(LANG_NAMES[lang])
    raise NotImplementedError


def process(text: str, lang: str) -> list[str]:
    """Full pipeline for one document (or a query)."""
    text = remove_accents(lowercase(text))
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens, lang)
    return stem(tokens, lang)
