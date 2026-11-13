# AGENTS.md

Instructions for AI coding tools (and humans) working in this repo.

## Start here

1. Read `docs/PROJECT_BRIEF.md` for what the system is, who owns what and the rules.
2. Read the newest file in `reports/` (files are named `YYYY-MM-DD-title.md`) for the latest progress.
3. Read the `README.md` inside the folder you are about to change.

## Rules

- Stay inside your folder. Only `backend/` (and `rag/` for its own vector tables) talks to the database. Everything else calls the API.
- `docs/api.md` is the contract between the AI group and the Data group. Do not change an endpoint without the project manager agreeing.
- Never commit secrets. Read them from environment variables loaded from `.env`, and add any new variable name (no value) to `.env.example`.
- Never commit real student data, not even in tests. Use fake data from `db/seed/`.
- Never send student data to a cloud LLM API. Use the local Ollama model, or pseudonymize first (S01, S02 and so on).
- Do not name a Python package after a standard library module (that is why the email job lives in `digest/`, not `email/`).
- Keep pull requests small and focused. Moving files goes in its own pull request with no code changes.
- After finishing a big piece of work, add a progress report to `reports/` using `reports/TEMPLATE.md`.

## Stack

Python, Neon Postgres + pgvector, Ollama (local LLM), Gmail API or SMTP, Google Drive, Streamlit. Free tools only.
