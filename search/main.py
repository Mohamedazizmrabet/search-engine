"""Search service (FastAPI).

Run locally:  uvicorn main:app --reload --port 8000
Only the NestJS API calls this service; the browser never does.
"""
from fastapi import FastAPI

app = FastAPI(title="Search service")


@app.get("/")
def hello():
    """Say hello, so the NestJS API can check that this service is running."""
    return {"message": "Hello from the search service"}
