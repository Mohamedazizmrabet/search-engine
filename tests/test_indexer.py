import math
from src.indexer import compute_tf, compute_df, compute_idf, compute_tfidf, build_inverted_file


def test_idf_slide_47():
    # D1 = {crayon, rouge, maison}, D2 = {policier, velo, rouge}
    docs = {"D1": ["crayon", "rouge", "maison", "rouge"],
            "D2": ["policier", "velo", "rouge"]}
    idf = compute_idf(compute_df(compute_tf(docs)), 2)
    assert idf["rouge"] == 0
    assert math.isclose(idf["crayon"], 0.301, abs_tol=0.001)


def test_tfidf_slide_53():
    # Rebuild the frequency matrix of slide 51 as fake documents
    matrix = {
        "D1": {"t1": 157, "t2": 4, "t3": 232, "t5": 57, "t6": 2, "t7": 2},
        "D2": {"t1": 73, "t2": 157, "t3": 223, "t4": 10},
        "D3": {"t6": 3, "t7": 1},
        "D4": {"t2": 1, "t3": 2, "t6": 5, "t7": 1},
        "D5": {"t2": 1, "t3": 1, "t6": 5, "t7": 1},
        "D6": {"t3": 1, "t6": 1},
    }
    docs = {d: [t for t, n in terms.items() for _ in range(n)] for d, terms in matrix.items()}
    tf = compute_tf(docs)
    tfidf = compute_tfidf(tf, compute_idf(compute_df(tf), 6))
    assert math.isclose(tfidf["D1"]["t1"], 74.908, abs_tol=0.01)
    assert math.isclose(tfidf["D2"]["t4"], 7.782, abs_tol=0.01)
    assert math.isclose(tfidf["D6"]["t3"], 0.079, abs_tol=0.001)


def test_inverted_file_structure():
    docs = {"D1": ["caesar", "brutus"], "D2": ["caesar", "caesar"]}
    index = build_inverted_file(docs)
    assert index["dictionary"]["caesar"] == {"df": 2, "coll_freq": 3}
    postings = {p["doc"]: p["tf"] for p in index["postings"]["caesar"]}
    assert postings == {"D1": 1, "D2": 2}
