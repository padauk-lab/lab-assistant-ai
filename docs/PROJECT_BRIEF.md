# Project Brief: Lab Assistant AI

Read this first if you are new to the project (human or coding tool). For the latest progress, read the newest file in `reports/`.

## 1. What we are building

An AI lab assistant for our IoMT lab at iU (11 students and 1 professor, mostly international students busy with school and work). The goal is a small system that actually works, built by beginners, with zero budget and free tools only.

## 2. The 7 functions

| # | Function | Summary |
|---|----------|---------|
| 1 | RAG | Answers from school guidelines, policies, timetables per year level, plus library PDFs |
| 2 | Student progress database | Per student: id, name, student number, year, project topic, current stage, progress note, struggle (optional, written by the student), last update, opted_in. No code files stored |
| 3 | Monday email | Weekly progress digest sent ONLY to the professor: each student's stage, latest update, last-updated date, who may need help, upcoming deadlines. Students get no emails |
| 4 | Equipment database | Tables `equipment` (id, name, category, quantity, location, status, notes) and `loans` (id, equipment_id, student_id, borrowed_at, returned_at). First step: inventory the lab in a spreadsheet and import it |
| 5 | LLM chat box | Explains projects and answers questions, using the other functions as tools |
| 6 | Q&A box | Students post questions with visibility `professor_only` or `everyone`, classmates answer, the AI can suggest answers from RAG. Tables `questions`, `answers` |
| 7 | Ebook library | PDFs in a shared Google Drive folder. The database stores only info: title, author, type, tags, Drive file_id, file_link, uploaded_by |

How progress gets in: students update any time through the chat or a page, and the lab assistant can enter notes from lab meetings. No weekly nagging of students.

Dropped for now (do not re-add): paper finder, senior handover and future-student features, emails to students, the "each person builds their own DL model" rule.

## 3. System structure

```
                 +------------------+
  students  ---> |    frontend/     |  (Streamlit pages + chat box)
  professor      +--------+---------+
                          |  HTTP calls only
                          v
                 +------------------+        +------------------+
                 |    backend/      | <----- |  llm/  (Ollama)  |  chat calls the API + RAG as tools
                 |  (the API)       | <----- |  digest/         |  Monday job reads progress via the API
                 +--------+---------+        |  qa/             |  suggests answers via RAG
                          |                  +--------+---------+
                          v                           |
                 +------------------+                 |
                 |  Neon Postgres   | <---------------+  rag/ stores and searches chunks (pgvector)
                 |  + pgvector      |
                 +------------------+
  Google Drive: library PDF files (database keeps only info and links)
  Gmail: sends the Monday digest to the professor
```

Rule: nothing except `backend/` (and `rag/` for its own vector tables) talks to the database directly. Everyone else goes through the API in `docs/api.md`.

## 4. Repo structure

| Folder | What | Owner |
|--------|------|-------|
| `docs/` | Table definitions, API list, consent message, images | Htet Pai |
| `db/` | Schema, migrations, fake seed data, backups | Data group |
| `backend/` | The API server | Data group |
| `frontend/` | Pages and chat box UI | Data group, Htet Pai helps |
| `rag/` | Ingest, embed, search | AI group |
| `llm/` | Chat agent, tools, prompts, pseudonymize | AI group |
| `digest/` | Monday email job | AI group |
| `qa/` | AI answer suggestions for the Q&A board | AI group |
| `library/` | Google Drive helpers for the ebook library | AI group |
| `scripts/` | One-off jobs (equipment spreadsheet import) | Whoever writes it |
| `reports/` | Progress reports after each big piece of work | Everyone |

Each folder has its own README saying what goes there.

## 5. Team and work allocation

- **AI group (LMHP, SWYG, KZN):** RAG, LLM chat box, Monday email, ebook library, Q&A box
- **Data group (ANK, TDS):** student DB, equipment DB, backend, frontend
- **Htet Pai (project manager):** manages both groups, helps with frontend and backend side pieces (not the critical path), reviews both groups, owns the API list, handles professor communication and consent

The two groups connect only through the API list (for example `GET /students/{id}`, `POST /progress`, `GET /equipment?name=`, `POST /questions`, `POST /chat`). Any change to it goes through Htet Pai.

## 6. Privacy rules (non-negotiable)

- Opt-in only. The professor asks for consent, and the consent message states what is stored and that a Monday digest goes to the professor
- Students see only their own data, the professor sees all
- Free LLM API tiers may use our data, so anything with student data runs on the local model (Ollama), or is pseudonymized (S01, S02 and so on) before calling a free API. Guideline and timetable text is fine to send
- Secrets (email password, keys) never go in GitHub. Use `.env` (already in `.gitignore`) and list variable names in `.env.example`
- Regular database backups
- Never commit real student data, not even in tests. Use fake data in `db/seed/`

## 7. Free stack

Neon Postgres (with pgvector), Gmail API or SMTP, cron on an always-on PC or a GitHub Actions schedule, Ollama, Google Drive, Streamlit or a simple web app. Nothing paid, no Terraform.

## 8. Way of working

- Every change goes through a pull request into `main`. At least 1 approval is needed, and pushing new commits after approval resets the approval
- Small pull requests, reviews within 1 to 2 days, cross-group code review weekly
- Fixed owners per task plus weekly goals, 30-minute weekly meeting with demos
- After each big piece of work, add a progress report to `reports/`

## 9. Plan (phases)

1. Agree on tables and the API list, repo setup, start data collection and consent
2. Each part works alone with fake data
3. Connect the parts (chat uses the real API and RAG, frontend uses the real API)
4. Real data in, 20 to 30 test questions, test Monday email sent to ourselves
5. Launch in the lab, first real Monday email to the professor, collect feedback
