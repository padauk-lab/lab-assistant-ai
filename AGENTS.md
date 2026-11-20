# AGENTS.md

Instructions for AI coding tools (and humans) working in this repo.

## Start here

1. Read `docs/PROJECT_BRIEF.md` for what the system is, who owns what and the rules.
2. Read the newest file in `reports/` (files are named `YYYY-MM-DD-title.md`) for the latest progress.
3. Read the `README.md` inside the folder you are about to change.

## Commands

```bash
uv sync                              # install dependencies
uv run pre-commit install            # enable commit checks (once per clone)
docker compose up --build            # run the whole system
uv run pytest                        # tests
uv run ruff check . && uv run ruff format .   # lint and format
uv run pre-commit run --all-files    # everything CI checks
uv add --group <area> <package>      # add a dependency (area: backend, frontend, ...)
```

## Rules

- CI must be green before merging. Run `uv run pre-commit run --all-files` and `uv run pytest` before pushing.
- Every new feature comes with tests in a `tests/` folder next to the code.
- Add dependencies with `uv add`, never `pip install`, and commit the updated `uv.lock`.
- Stay inside your folder. Only `backend/` (and `rag/` for its own vector tables) talks to the database. Everything else calls the API.
- `docs/api.md` is the contract between the Agent Engineering and Infrastructure & System Engineering teams. Do not change an endpoint without the project manager agreeing.
- Never commit secrets. Read them from environment variables loaded from `.env`, and add any new variable name (no value) to `.env.example`.
- Real student data lives only in the live database, never in this repo. The repo is public, so code, tests and examples use fake data from `db/seed/`.
- Never send student data to a cloud LLM API. Use a local model (currently Ollama), or pseudonymize first (S01, S02 and so on).
- Do not name a Python package after a standard library module (that is why the email job lives in `digest/`, not `email/`).
- Keep pull requests small and focused. Moving files goes in its own pull request with no code changes.
- After finishing a big piece of work, add a progress report to `reports/` using `reports/TEMPLATE.md`.

## Stack (starting choices, not fixed)

Python 3.12 with uv, FastAPI, Streamlit, Postgres + pgvector (local Docker for dev, Neon for hosting), Ollama on the host (local LLM), Gmail API or SMTP, Google Drive, Docker Compose, GitHub Actions.

Better tool? Propose it. Any tool can be swapped if it is free, keeps student data private, and does not break the API contract. Write a short note in your PR on why, and agree with the project manager if it affects the other team.
