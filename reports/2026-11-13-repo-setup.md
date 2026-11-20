# Progress report: Repo setup

- **Date:** 2026-11-13
- **Written by:** Htet Pai
- **Area:** whole project
- **Phase:** 1

## What got done

- Created the public repo `padauk-lab/lab-assistant-ai` with a README and a Python `.gitignore`
- Protected `main`: pull request required, 1 approval needed, new commits after approval reset the approval, no bypassing (admins included)
- Set up the folder structure with a README per folder
- Added the project brief (`docs/PROJECT_BRIEF.md`), `AGENTS.md` and `CLAUDE.md` so coding tools pick up the project context automatically
- Added templates for progress reports and pull requests, plus `.env.example`

## What changed from the plan (and why)

- The README roadmap uses phases instead of week numbers, so it stays true even if the schedule slips. Real dates go in these reports
- The Monday email folder is called `digest/`, not `email/`, to avoid clashing with Python's built-in `email` module

## Problems or blockers

- None yet. The folder structure is a draft to confirm at the first weekly meeting

## Next steps

- Agree on table definitions (`docs/tables.md`) and the API list (`docs/api.md`)
- Start data collection and the consent process with the professor
- Add teammates' GitHub usernames so a CODEOWNERS file can auto-request the right reviewers
