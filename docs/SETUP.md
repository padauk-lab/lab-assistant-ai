# Setup guide

From zero to the whole system running on your laptop. Takes about 30 to 60 minutes the first time.

## 1. Install the tools (once per laptop)

| Tool | What it is for | Install |
|------|----------------|---------|
| WSL 2 + Ubuntu (Windows only) | A Linux environment on Windows. Run every command below inside Ubuntu | `wsl --install` in PowerShell as admin, then restart |
| Git | Version control | `sudo apt install git` |
| Docker Desktop | Runs the backend, frontend and database in containers | [docker.com](https://www.docker.com/products/docker-desktop/). On Windows, turn on Settings, Resources, WSL integration, Ubuntu |
| uv | Installs Python 3.12 and all libraries, exactly the same versions for everyone | `curl -LsSf https://astral.sh/uv/install.sh \| sh` then reopen the terminal |
| Ollama | Runs the LLM on your own machine (needed by Agent Engineering) | [ollama.com](https://ollama.com/download) |

Check everything works:

```bash
git --version
docker --version
uv --version
```

## 2. Git identity (once per laptop)

The repo is public, so use your GitHub no-reply email, not your personal one.
GitHub, Settings, Emails, then copy the address that ends in `@users.noreply.github.com`.

```bash
git config --global user.name "Your Name"
git config --global user.email "ID+username@users.noreply.github.com"
```

## 3. Get the project

Keep the project inside Ubuntu (for example `~/lab-assistant-ai`), not on the Windows Desktop. It is much faster.

```bash
cd ~
git clone https://github.com/padauk-lab/lab-assistant-ai.git
cd lab-assistant-ai
cp .env.example .env          # then open .env and fill in your values
uv sync                       # installs Python 3.12 + all libraries into .venv
uv run pre-commit install     # turns on the checks that run on every commit
```

## 4. Run it

```bash
docker compose up --build
```

- Backend API docs: http://localhost:8000/docs
- Frontend: http://localhost:8501
- Stop: `Ctrl+C`, then `docker compose down`
- Stop and delete the local database: `docker compose down --volumes`

## 5. Check your setup

```bash
uv run pytest                        # tests pass
uv run pre-commit run --all-files    # the same checks CI runs
```

If both pass, you are ready. Read [`CONTRIBUTING.md`](../CONTRIBUTING.md) before your first pull request.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `docker: command not found` in Ubuntu | Docker Desktop, Settings, Resources, WSL integration, turn on Ubuntu, then restart the terminal |
| `port is already allocated` | Something else uses port 5432, 8000 or 8501. Stop it, or run `docker compose down` first |
| `uv: command not found` | Close and reopen the terminal after installing uv |
| Containers cannot reach Ollama | Make sure Ollama is running. If it still fails, set the environment variable `OLLAMA_HOST=0.0.0.0` for Ollama and restart it |
| First `pre-commit` run is slow | Normal. It downloads the check tools once, then it is fast |
| Commit blocked by `gitleaks` | You tried to commit a secret. Move it to `.env` and use an environment variable instead |
