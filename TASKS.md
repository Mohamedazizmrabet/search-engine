# Task split — demo on Tuesday

## Shared contract (agree on this first!)

Data passed between modules:

| From → To | Shape |
|---|---|
| `loader` → `main` | `{"D1": {"path": "data/x.txt", "lang": "fr", "text": "..."}, ...}` |
| `preprocessing.process(text, lang)` | returns `["econom", "index", ...]` |
| `main` → `indexer` | `{"D1": ["econom", "index", ...], "D2": [...]}` |

## Member A — Lead: loading + integration (steps 1 & glue)
- [ ] Create the GitHub repo, push this skeleton, add teammates as collaborators
- [ ] `src/loader.py`: read every `.txt` in `data/` (UTF-8), assign IDs D1, D2…
- [ ] Language detection with `langdetect` (seed = 0, fallback to "en")
- [ ] Add 5–10 real test files to `data/` (course chapters as text, FR + EN)
- [ ] `main.py`: connect all modules once B and C merge
- [ ] Prepare the Tuesday demo (see below)

## Member B — Preprocessing (steps 2, 3, 4)
- [ ] `lowercase()` and `remove_accents()`
- [ ] `tokenize()`: split on spaces, punctuation, apostrophes (`l'ensemble` → `l`, `ensemble`)
- [ ] `remove_stopwords()` with NLTK French/English lists
- [ ] `stem()` with NLTK Snowball (french / english)
- [ ] `process()` chaining everything
- [ ] Make `tests/test_preprocessing.py` pass

## Member C — Weighting + inverted file (steps 5, 6)
- [ ] `compute_tf()`, `compute_df()`, `compute_idf()` (log10), `compute_tfidf()`
- [ ] `build_inverted_file()`: dictionary (df, collection freq) + postings (doc, tf, tfidf)
- [ ] `save_index()` / `load_index()` to/from JSON
- [ ] Make `tests/test_indexer.py` pass (checks against slides 51–53 and 56–59)

## Timeline

| Day | Goal |
|---|---|
| Fri | Repo created, everyone cloned, contract agreed |
| Sat–Sun | Each member codes their module on their branch, tests passing |
| Mon | Merge everything, run `main.py` end to end, fix bugs |
| Tue | Demo |

## Tuesday demo checklist
- [ ] `python main.py` runs on real files and produces `index.json`
- [ ] Show one document going through every step (print before/after)
- [ ] Show TF-IDF results matching the slide exercise
- [ ] Show the GitHub commit history (proof everyone contributed)
