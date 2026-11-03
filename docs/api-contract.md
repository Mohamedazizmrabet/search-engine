# API contract

The list of every URL between the three parts, so each person can work on their part in parallel.
If you need to change something here, tell the other two first.

```
React (web)  ──HTTP/JSON──▶  NestJS (api)  ──HTTP/JSON──▶  Python (search)
```

- The browser **only** calls the NestJS API (`http://localhost:3000`).
- Only the NestJS API calls the Python service (`http://search:8000`, inside Docker).
- Admin URLs (marked 🔒) need the header `Authorization: Bearer <accessToken>`.
  Without a valid token the API answers `401 Unauthorized`.
- Errors use the NestJS default shape: `{ "statusCode": 404, "message": "Course not found", "error": "Not Found" }`.

---

## Part 1 — web → api (NestJS)

### POST /auth/login
Log in an admin (FR7).

Request:
```json
{ "email": "admin@sesame.tn", "password": "secret123" }
```
Response `200`:
```json
{ "accessToken": "eyJhbGciOiJIUzI1NiIs..." }
```
Wrong email or password → `401`.

### GET /subjects
List all subjects (for the filter and the course grid).

Response `200`:
```json
[
  { "id": 1, "name": "SOA and indexing" },
  { "id": 2, "name": "Cloud & Big Data" }
]
```

### POST /subjects 🔒
Add a subject (FR10). Request: `{ "name": "Cloud & Big Data" }` → Response `201`: `{ "id": 2, "name": "Cloud & Big Data" }`.
Name already used → `409`.

### PATCH /subjects/:id 🔒
Rename a subject (FR10). Request: `{ "name": "Cloud and Big Data" }` → Response `200`: `{ "id": 2, "name": "Cloud and Big Data" }`.

### DELETE /subjects/:id 🔒
Delete a subject (FR10). Response `204` (no body).
The subject still has courses → `409` (delete its courses first).

### GET /courses?subjectId=2
List courses for the home page grid (FR3). `subjectId` is optional.

Response `200`:
```json
[
  {
    "id": 7,
    "title": "Chapter 3 - Docker",
    "subject": { "id": 2, "name": "Cloud & Big Data" },
    "pageCount": 42,
    "createdAt": "2026-11-03T10:15:00.000Z",
    "pdfUrl": "/courses/7/pdf"
  }
]
```

### GET /courses/:id/pdf
Returns the PDF file itself (`Content-Type: application/pdf`) (FR5).
To open it at a page, the front-end adds `#page=N` to the URL: `http://localhost:3000/courses/7/pdf#page=12`.

### POST /courses 🔒
Add a course (FR8). Request is `multipart/form-data` (not JSON):

| field       | type   | example               |
|-------------|--------|-----------------------|
| `file`      | PDF    | `docker.pdf`          |
| `title`     | text   | `Chapter 3 - Docker`  |
| `subjectId` | number | `2`                   |

What the API does: save the PDF in `/pdfs` → create the course row → call `POST /index` on the search service.

Response `201`: the course, same shape as one item of `GET /courses`.
The search service could not read the PDF (scanned PDF) → the API deletes the course and the file, then answers `422`:
```json
{ "statusCode": 422, "message": "PDF cannot be processed", "error": "Unprocessable Entity" }
```

### DELETE /courses/:id 🔒
Delete a course (FR9). Response `204`.
What the API does: call `DELETE /index/:courseId` on the search service → delete the course row → delete the PDF file.

### GET /search?q=docker&subjectId=2
Search courses (FR1, FR2, FR4). `subjectId` is optional.

Response `200` (sorted by `score`, highest first):
```json
{
  "query": "docker",
  "results": [
    {
      "course": {
        "id": 7,
        "title": "Chapter 3 - Docker",
        "subject": { "id": 2, "name": "Cloud & Big Data" },
        "pdfUrl": "/courses/7/pdf"
      },
      "page": 12,
      "score": 0.87,
      "tfidfScore": 0.91,
      "semanticScore": 0.83
    }
  ]
}
```
No result → `"results": []` and the front-end shows "No course found" (FR6).

---

## Part 2 — api → search (Python FastAPI)

The NestJS API adds the subject names and titles; the Python service only returns ids and scores.

### GET /
Hello / check that the service runs. Response `200`: `{ "message": "Hello from the search service" }`.

### POST /index
Index one course (FR11–FR16). The course row already exists (created by NestJS).

Request:
```json
{ "courseId": 7, "pdfPath": "/pdfs/7-docker.pdf" }
```
What the service does: read the PDF page by page → preprocessing → update `terms` (df, total_frequency) and `postings` (tf) → one row in `chunks` per page with its embedding → update `page_count` and `term_count` in `courses`.

Response `200`:
```json
{ "courseId": 7, "pageCount": 42, "termCount": 1830 }
```
No text in the PDF → `422`: `{ "detail": "PDF has no text" }`. Nothing is written in that case.

### DELETE /index/{courseId}
Remove a course from the index (FR9). Decreases `df` / `total_frequency` of its terms (and deletes terms that reach df = 0), deletes its postings and chunks.

Response `200`: `{ "courseId": 7, "deleted": true }`.

### POST /search
Rank the courses for a query (FR17).

Request:
```json
{ "query": "docker", "subjectId": 2, "limit": 20 }
```
`subjectId` can be `null` (all subjects).

Response `200`:
```json
{
  "results": [
    { "courseId": 7, "page": 12, "score": 0.87, "tfidfScore": 0.91, "semanticScore": 0.83 }
  ]
}
```
- `tfidfScore` = Σ tf(t, d) × log10(N / df(t)), then divided by the best score of this query → between 0 and 1.
- `semanticScore` = cosine similarity of the closest chunk of the course (pgvector), between 0 and 1.
- `score` = α × tfidfScore + (1 − α) × semanticScore, with α = 0.5.
- `page` = page of the closest chunk.
