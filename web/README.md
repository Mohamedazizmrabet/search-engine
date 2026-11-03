# web — React front-end

The website: search bar at the top, course cards grouped by subject (like the LMS), results page, admin area.
It only talks to the NestJS API. The URLs are in [../docs/api-contract.md](../docs/api-contract.md).

## Folders

| Path                | What                                                         |
|---------------------|--------------------------------------------------------------|
| `src/App.tsx`       | Header + the routes (`/`, `/search`, `/admin`)               |
| `src/pages/`        | One file per page: `HomePage`, `SearchPage`, `AdminPage`     |
| `src/components/`   | Reusable pieces: `SearchBar`, `CourseCard`, ... (to create)  |
| `src/api/client.ts` | All calls to the NestJS API go through here                  |
| `src/index.css`     | Loads Tailwind CSS                                           |

Styling: Tailwind classes directly in `className` (e.g. `className="rounded-lg bg-white p-4 shadow"`).

## Run

With Docker (from the repo root): `docker compose up --build`, then open http://localhost:5173.

Without Docker (from `web/`):
```bash
npm install
```
```bash
npm run dev
```
```bash
npm run build
```
