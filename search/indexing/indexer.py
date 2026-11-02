"""Steps 5–6 — Weighting (TF, IDF, TF-IDF) and the inverted file.
Owner: Member C

Input everywhere: docs = {"D1": ["term", "term", ...], "D2": [...]}
"""
import json
import math


def compute_tf(docs: dict) -> dict:
    """{"D1": {"caesar": 1, ...}, ...} — occurrences of each term per doc."""
    tf = {}
    for doc_id in docs:
        counts = {}
        for term in docs[doc_id]:
            if term in counts:
                counts[term] = counts[term] + 1
            else:
                counts[term] = 1
        tf[doc_id] = counts
    return tf


def compute_df(tf: dict) -> dict:
    """{"caesar": 2, ...} — number of documents containing each term."""
    df = {}
    for doc_id in tf:
        for term in tf[doc_id]:
            if term in df:
                df[term] = df[term] + 1
            else:
                df[term] = 1
    return df


def compute_idf(df: dict, n_docs: int) -> dict:
    """idf(t) = log10(N / df(t))  (slide 45)."""
    idf = {}
    for term in df:
        idf[term] = math.log10(n_docs / df[term])
    return idf


def compute_tfidf(tf: dict, idf: dict) -> dict:
    """{"D1": {"caesar": 0.0, ...}, ...} — tf * idf  (slide 48)."""
    tfidf = {}
    for doc_id in tf:
        weights = {}
        for term in tf[doc_id]:
            weights[term] = tf[doc_id][term] * idf[term]
        tfidf[doc_id] = weights
    return tfidf


def build_inverted_file(docs: dict) -> dict:
    """Return the inverted file (slide 59):

    {
      "n_docs": 2,
      "dictionary": {"caesar": {"df": 2, "coll_freq": 3}, ...},
      "postings":   {"caesar": [{"doc": "D1", "tf": 1, "tfidf": 0.0}, ...], ...}
    }
    Terms sorted alphabetically.
    """
    n_docs = len(docs)
    tf = compute_tf(docs)
    df = compute_df(tf)
    idf = compute_idf(df, n_docs)
    tfidf = compute_tfidf(tf, idf)

    dictionary = {}
    postings = {}

    for term in sorted(df):
        coll_freq = 0
        term_postings = []
        for doc_id in tf:
            if term in tf[doc_id]:
                coll_freq = coll_freq + tf[doc_id][term]
                entry = {
                    "doc": doc_id,
                    "tf": tf[doc_id][term],
                    "tfidf": round(tfidf[doc_id][term], 3),
                }
                term_postings.append(entry)
        dictionary[term] = {"df": df[term], "coll_freq": coll_freq}
        postings[term] = term_postings

    index = {
        "n_docs": n_docs,
        "dictionary": dictionary,
        "postings": postings,
    }
    return index


def save_index(index: dict, path: str = "index.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


def load_index(path: str = "index.json") -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)