# Lab Assistant AI

[![CI](https://github.com/padauk-lab/lab-assistant-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/padauk-lab/lab-assistant-ai/actions/workflows/ci.yml)

An AI lab assistant for our IoMT lab at iU (11 students and 1 professor). Built by a student team with free tools and an industry-style workflow, under [Padauk Lab](https://github.com/padauk-lab).

> Status: Phase 1 (design and setup). Screenshots and a demo will be added here once the system is running.

<!-- Screenshots go here later, for example: ![Chat box](docs/images/chat.png) -->

## What it does

| # | Feature | What it is |
|---|---------|-----------|
| 1 | RAG search | Answers questions from school guidelines, policies, timetables per year level and library PDFs |
| 2 | Student progress database | Each student's project topic, current stage, progress note and last update (opt-in only) |
| 3 | Monday email | A weekly progress digest sent only to the professor |
| 4 | Equipment database | Lab inventory plus who borrowed what and when |
| 5 | LLM chat box | Explains projects and answers questions, using the other features as tools |
| 6 | Q&A board | Students post questions (professor only or everyone), classmates answer, the AI can suggest answers |
| 7 | Ebook library | Book and paper info in the database, files in a shared Google Drive folder |

## Tech stack (starting choices, all free)

These are where we start, not fixed rules. If someone finds a better free option, propose it in a PR.

- Language: Python 3.12, dependencies managed with [uv](https://docs.astral.sh/uv/)
- Backend: FastAPI
- Database: Postgres with pgvector (for RAG). Local Postgres in Docker for development, Neon for the hosted database
- LLM: Ollama, an open model running locally (used for anything with student data)
- Email: Gmail API or SMTP
- Scheduler: cron on an always-on PC or a GitHub Actions schedule
- Files: Google Drive
- Frontend: Streamlit
- Dev environment: Docker Compose (Ollama runs on the host so it can use the GPU)
- Quality: ruff (lint and format), pytest, pre-commit hooks, gitleaks (secret scanning)
- CI: GitHub Actions runs lint, tests and a Docker build on every pull request

## Quick start

```bash
git clone https://github.com/padauk-lab/lab-assistant-ai.git
cd lab-assistant-ai
cp .env.example .env            # fill in your own values
uv sync                         # install Python dependencies
uv run pre-commit install       # turn on the commit checks
docker compose up --build       # start the whole system
```

- Backend API docs: http://localhost:8000/docs
- Frontend: http://localhost:8501

First time? Follow [`docs/SETUP.md`](docs/SETUP.md) for installing Docker, uv and Ollama.

## Architecture

The project has two teams that connect only through a shared API list.

- Agent Engineering: RAG, LLM chat box, Monday email, ebook library, Q&A board
- Infrastructure & System Engineering: student database, equipment database, backend, frontend

Example endpoints: `GET /students/{id}`, `POST /progress`, `GET /equipment?name=`, `POST /questions`, `POST /chat`. Any change to the API list goes through the project manager.

<!-- Architecture diagram goes here later: ![Architecture](docs/images/architecture.png) -->

## Privacy

- Students join only by opt-in consent, and the consent message says what is stored and that a weekly digest goes to the professor
- Students see only their own data, the professor sees all
- Student data never goes to a free cloud LLM API. It runs on a local model, or it is pseudonymized (S01, S02 and so on) first
- Secrets (passwords, API keys) are never committed. They live in `.env`, which is in `.gitignore`
- The ebook library only stores files for open-access papers, our own documents and free books. Paywalled items are saved as links only

## Repo structure

| Folder | What | Owner |
|--------|------|-------|
| `docs/` | Project brief, table definitions, API list, images | Project manager |
| `db/` | Schema, migrations, fake seed data | Infrastructure & System Engineering |
| `backend/` | The API server | Infrastructure & System Engineering |
| `frontend/` | Pages and chat box UI | Infrastructure & System Engineering |
| `rag/` | Ingest, embed, search | Agent Engineering |
| `llm/` | Chat agent, tools, prompts | Agent Engineering |
| `digest/` | Monday email job | Agent Engineering |
| `qa/` | AI answer suggestions for the Q&A board | Agent Engineering |
| `library/` | Google Drive helpers for the ebook library | Agent Engineering |
| `scripts/` | One-off jobs | Script author |
| `reports/` | Progress reports | Everyone |

New here? Read [`docs/PROJECT_BRIEF.md`](docs/PROJECT_BRIEF.md), then the newest file in [`reports/`](reports/). Coding tools pick up the same context automatically from `AGENTS.md` and `CLAUDE.md`.

## Roadmap

- [ ] Phase 1: agree on tables and the API list, repo setup, start data collection and consent
- [ ] Phase 2: each part works alone with fake data
- [ ] Phase 3: connect the parts (chat uses the real API and RAG, frontend uses the real API)
- [ ] Phase 4: real data in, 20 to 30 test questions, test Monday email
- [ ] Phase 5: launch in the lab, first real Monday email, collect feedback

Dated progress lives in [`reports/`](reports/).

## How we work

- Every change goes through a pull request into `main`, no direct pushes
- A pull request merges only when CI is green and at least one reviewer approves. New commits after approval reset the approval
- Every feature comes with tests
- Full rules: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Small pull requests, reviews within 1 to 2 days
- 30-minute weekly meeting with demos, and a progress report in `reports/` after each big piece of work

## Team

| Role | Members |
|------|---------|
| Project manager | Htet Pai |
| Agent Engineering | LMHP, SWYH |
| Infrastructure & System Engineering | ANK, TDS, KZN |
