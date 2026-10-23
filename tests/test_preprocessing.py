from src.preprocessing import lowercase, remove_accents, tokenize, process


def test_lowercase():
    assert lowercase("Base Militaire") == "base militaire"   # slide 20


def test_remove_accents():
    assert remove_accents("école") == "ecole"                 # slide 20


def test_tokenize_apostrophes():
    assert tokenize("l'ensemble aujourd'hui") == ["l", "ensemble", "aujourd", "hui"]


def test_french_stemming_groups_variants():
    # économie / économistes / économiques should share one stem (slide 27)
    terms = process("économie économistes économiques", "fr")
    assert len(set(terms)) == 1


def test_stopwords_removed():
    terms = process("Le crayon rouge est dans la maison rouge.", "fr")
    assert "le" not in terms and "la" not in terms and "dans" not in terms
