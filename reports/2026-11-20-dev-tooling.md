# Progress report: Dev tooling and team setup

- **Date:** 2026-11-20
- **Written by:** Htet Pai
- **Area:** whole project
- **Phase:** 1

## What got done

- Renamed the teams to Agent Engineering and Infrastructure & System Engineering, moved KZN to Infrastructure & System Engineering
- Made all tools "starting choices" that the team can swap for better free options
- Added an industry-style dev setup: Python 3.12 with uv, ruff, pytest, pre-commit with gitleaks, Docker Compose (backend, frontend, Postgres + pgvector) and GitHub Actions CI
- Added a minimal FastAPI backend (`/health`) and Streamlit frontend so the Docker setup and CI have something real to run
- Added `docs/SETUP.md` (onboarding) and `CONTRIBUTING.md` (team rules)

## What changed from the plan (and why)

- Docker from day one instead of later: the project is meant to give everyone real industry experience
- Ollama stays outside Docker so it can use the GPU

## Problems or blockers

- None

## Next steps

- Make the CI checks required in branch protection
- Design `docs/tables.md` and `docs/api.md`
- Give out the first tasks to both teams
