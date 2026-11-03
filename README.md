# Course search engine — SESAME

Search engine for students' PDF course materials, for the *Indexing and Referencing Techniques* module.
Team: Safi Hanafi, Makrem Riahi, Mohamed Aziz Mrabet.

- Full specification: [docs/specification.md](docs/specification.md)
- URLs between the parts: [docs/api-contract.md](docs/api-contract.md)

## The 3 parts

| Folder              | What                                        | Tech                        | URL                     |
|---------------------|---------------------------------------------|-----------------------------|-------------------------|
| [web/](web/)        | The website (search bar, course grid, admin)| React + Vite + Tailwind     | http://localhost:5173   |
| [api/](api/)        | Main API: login, courses, subjects, PDFs    | NestJS + Prisma             | http://localhost:3000   |
| [search/](search/)  | Indexing + search (TF-IDF + semantic)       | Python + FastAPI            | internal only           |
| `db` (Docker)       | Database                                    | PostgreSQL + pgvector       | localhost:5432          |
| [pdfs/](pdfs/)      | Uploaded PDF files (not pushed to GitHub)   | shared folder               |                         |

```
React (web)  →  NestJS (api)  →  Python (search)
                     ↓                  ↓
                 PostgreSQL  ←──────────┘
```

## Start everything

You need [Docker Desktop](https://www.docker.com/products/docker-desktop/) running.

1. Create your `.env` files from the examples (only the first time):
   ```bash
   cp api/.env.example api/.env
   ```
   ```bash
   cp search/.env.example search/.env
   ```
   ```bash
   cp web/.env.example web/.env
   ```
2. Start:
   ```bash
   docker compose up --build
   ```
3. Open http://localhost:5173. The "Connection check" box should show the API, the database and the search service.

Stop with `Ctrl+C`, or `docker compose down`. To also erase the database: `docker compose down -v`.

## Tests

```bash
docker compose exec search pytest
```
```bash
docker compose exec api npm test
```

## Team workflow

- Never push directly to `main`. Each person works on their own branch.
- Open a Pull Request when a task is done; one teammate reviews it before merging.
- Never commit `.env` files (they are in `.gitignore`).
- Only Prisma changes the database tables (`api/prisma/schema.prisma`). The Python service only reads and writes rows.
