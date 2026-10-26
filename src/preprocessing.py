"""Steps 2–4 — Lexical analysis, stopword removal, normalization.
Owner: Member B
"""
import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

LANG_NAMES = {"fr": "french", "en": "english"}


def lowercase(text: str) -> str:
    """"Base Militaire" → "base militaire"  (slide 20)."""
    return text.lower()


def remove_accents(text: str) -> str:
    """"école" → "ecole"  (slide 20)."""
    decomposed = unicodedata.normalize("NFD", text)
    result = ""
    for c in decomposed:
        if unicodedata.category(c) != "Mn":
            result = result + c
    return result


def tokenize(text: str) -> list[str]:
    """Split on anything that is not a letter.
    "l'e-mail de m. dupont" → ["l", "e", "mail", "de", "m", "dupont"]
    """
    tokens = re.findall(r"[a-z]+", text)
    return tokens


def get_stopwords(lang: str) -> list[str]:
    """NLTK's stopword list for `lang`, with accents removed."""
    words = stopwords.words(LANG_NAMES[lang])
    clean_words = []
    for w in words:
        clean_words.append(remove_accents(w))
    return clean_words


def remove_stopwords(tokens: list[str], lang: str) -> list[str]:
    """Drop stopwords and 1-letter tokens ("l", "d", "m")."""
    stop = get_stopwords(lang)
    kept = []
    for t in tokens:
        if len(t) > 1 and t not in stop:
            kept.append(t)
    return kept


def stem(tokens: list[str], lang: str) -> list[str]:
    """Snowball stemming: "economistes" → "econom" (French)."""
    stemmer = SnowballStemmer(LANG_NAMES[lang])
    stems = []
    for t in tokens:
        stems.append(stemmer.stem(t))
    return stems


def process(text: str, lang: str) -> list[str]:
    """Full pipeline for one document (or a query)."""
    text = lowercase(text)
    text = remove_accents(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens, lang)
    tokens = stem(tokens, lang)
    return tokens


if __name__ == "__main__":
    sample = "L'économie mondiale dépend des économistes."
    print(process(sample, "fr"))