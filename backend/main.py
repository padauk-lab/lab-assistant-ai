"""Backend API. Every other part of the system talks to the database through this."""

from fastapi import FastAPI

app = FastAPI(title="Lab Assistant API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Used by Docker and CI to check the API is alive."""
    return {"status": "ok"}
