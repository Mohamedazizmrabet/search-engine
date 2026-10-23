"""Steps 5–6 — Weighting (TF, IDF, TF-IDF) and the inverted file.
Owner: Member C

Input everywhere: docs = {"D1": ["term", "term", ...], "D2": [...]}
"""
import json
import math
from collections import Counter


def compute_tf(docs: dict) -> dict:
    """{"D1": {"caesar": 1, ...}, ...} — occurrences of each term per doc."""
    # TODO (C): Counter() is your friend
    raise NotImplementedError


def compute_df(tf: dict) -> dict:
    """{"caesar": 2, ...} — number of documents containing each term."""
    # TODO (C)
    raise NotImplementedError


def compute_idf(df: dict, n_docs: int) -> dict:
    """idf(t) = log10(N / df(t))  (slide 45)."""
    # TODO (C)
    raise NotImplementedError


def compute_tfidf(tf: dict, idf: dict) -> dict:
    """{"D1": {"caesar": 0.0, ...}, ...} — tf * idf  (slide 48)."""
    # TODO (C)
    raise NotImplementedError


def build_inverted_file(docs: dict) -> dict:
    """Return the inverted file (slide 59):

    {
      "n_docs": 2,
      "dictionary": {"caesar": {"df": 2, "coll_freq": 3}, ...},
      "postings":   {"caesar": [{"doc": "D1", "tf": 1, "tfidf": 0.0}, ...], ...}
    }
    Terms sorted alphabetically.
    """
    # TODO (C): use the four functions above
    raise NotImplementedError


def save_index(index: dict, path: str = "index.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


def load_index(path: str = "index.json") -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)
