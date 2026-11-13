# Lab Assistant AI

An AI lab assistant for our IoMT lab at iU (11 students and 1 professor). Built by beginners, with free tools only, under [Padauk Lab](https://github.com/padauk-lab).

> Status: Week 1 (design and setup). Screenshots and a demo will be added here once the system is running.

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

## Tech stack (all free)

- Database: Neon Postgres with pgvector (for RAG)
- LLM: Ollama, an open model running locally (used for anything with student data)
- Email: Gmail API or SMTP
- Scheduler: cron on an always-on PC or a GitHub Actions schedule
- Files: Google Drive
- Frontend: Streamlit or a simple web app

## Architecture

The project has two groups that connect only through a shared API list.

- AI group: RAG, LLM chat box, Monday email, ebook library, Q&A board
- Data group: student database, equipment database, backend, frontend

Example endpoints: `GET /students/{id}`, `POST /progress`, `GET /equipment?name=`, `POST /questions`, `POST /chat`. Any change to the API list goes through the project manager.

<!-- Architecture diagram goes here later: ![Architecture](docs/images/architecture.png) -->

## Privacy

- Students join only by opt-in consent, and the consent message says what is stored and that a weekly digest goes to the professor
- Students see only their own data, the professor sees all
- Student data never goes to a free cloud LLM API. It runs on a local model, or it is pseudonymized (S01, S02 and so on) first
- Secrets (passwords, API keys) are never committed. They live in `.env`, which is in `.gitignore`
- The ebook library only stores files for open-access papers, our own documents and free books. Paywalled items are saved as links only

## Roadmap

- [ ] Week 1: agree on tables and the API list, repo setup, start data collection and consent
- [ ] Week 2: each part works alone with fake data
- [ ] Week 3: connect the parts (chat uses the real API and RAG, frontend uses the real API)
- [ ] Week 4: real data in, 20 to 30 test questions, test Monday email
- [ ] Week 5: launch in the lab, first real Monday email, collect feedback

## How we work

- Every change goes through a pull request into `main`, no direct pushes
- At least one approval is needed to merge, and pushing new commits after approval resets the approval
- Small pull requests, reviews within 1 to 2 days
- 30-minute weekly meeting with demos, and a weekly progress report in this repo

## Team

| Role | Members |
|------|---------|
| Project manager | Htet Pai |
| AI group | LMHP, SWYG, KZN |
| Data group | ANK, TDS |
