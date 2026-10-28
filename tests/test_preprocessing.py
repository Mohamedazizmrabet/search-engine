from src.preprocessing import lowercase, remove_accents, tokenize, process


def test_lowercase():
    assert lowercase("Base Militaire") == "base militaire"   # slide 20


def test_remove_accents_and_ligatures():
    assert remove_accents("café") == "cafe"
    assert remove_accents("ﬁle") == "file"                    # PDF ligature


def test_tokenize_apostrophes():
    assert tokenize("it's an e-mail") == ["it", "s", "an", "e", "mail"]


def test_porter_groups_variants():
    # retrieve / retrieving / retrieved → one stem (slide 27)
    terms = process("retrieve retrieving retrieved")
    assert len(set(terms)) == 1


def test_stopwords_removed():
    terms = process("The red pencil is in the red house.")
    assert "the" not in terms and "is" not in terms and "in" not in terms