# search — Python search service

Indexes the course PDFs and ranks courses for a query (TF-IDF + semantic search).
Only the NestJS API calls this service. The URLs it must offer are in [../docs/api-contract.md](../docs/api-contract.md).

## Folders

| Path                 | What                                                                    |
|----------------------|-------------------------------------------------------------------------|
| `main.py`            | The FastAPI app. Add the `/index` and `/search` routes here.            |
| `indexing/loader.py` | Reads PDFs with pypdf                                                   |
| `indexing/preprocessing.py` | lowercase, accents/ligatures (NFKD), tokens, stopwords, Porter   |
| `indexing/indexer.py`| tf, df, idf = log10(N/df), TF-IDF, inverted file                        |
| `build_index.py`     | Old phase-1 script: builds `index.json` from the PDFs in `../pdfs`      |
| `tests/`             | pytest tests                                                            |

Still to add: database access with psycopg (`DATABASE_URL`), per-page chunks, and embeddings with
`sentence-transformers` (model `all-MiniLM-L6-v2`, 384 dimensions).
Never change the tables from Python: the schema belongs to Prisma (`api/prisma/schema.prisma`).

Code style: plain `for` loops and `if` statements, no list/dict comprehensions, a docstring on every function.

## Run with Docker (normal way)

From the repo root: `docker compose up --build`. Python files reload automatically.

```bash
docker compose exec search pytest
```

## Run without Docker

From the `search/` folder:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
```bash
python -c "import nltk; nltk.download('stopwords')"
```
```bash
uvicorn main:app --reload --port 8000
```
```bash
pytest
```
