# Text Search Engine — Indexing Phase

Group project for the *Techniques d'indexation et de référencement* course (SESAME).
A search engine over plain `.txt` files (French and English). **Phase 1: indexing.**

## Pipeline

```
data/*.txt
  → (1) load + detect language      src/loader.py
  → (2) lexical analysis            src/preprocessing.py
  → (3) stopword removal            src/preprocessing.py
  → (4) normalization (stemming)    src/preprocessing.py
  → (5) weighting (TF, IDF, TF-IDF) src/indexer.py
  → (6) inverted file → index.json  src/indexer.py
```

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

## Run

```bash
python main.py          # builds index.json from data/
pytest                  # runs the tests
```

## Team workflow

- Never push directly to `main`. Each person works on their own branch.
- Open a Pull Request when a task is done; one teammate reviews it before merging.
- See `TASKS.md` for who does what.
