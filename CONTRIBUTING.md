# Contributing

How we work. Same rules for everyone, including the project manager.

## The flow for every task

```bash
git checkout main && git pull                 # start from the latest main
git checkout -b <area>/<short-description>    # e.g. rag/pdf-chunking
# ... write code and tests ...
uv run pre-commit run --all-files             # lint, format, secret scan
uv run pytest                                 # tests
git add -A && git commit -m "Add PDF chunking for RAG ingest"
git push -u origin <area>/<short-description>
```

Then open a pull request on GitHub and fill in the template.

## Branch names

`<area>/<short-description>`, lowercase with hyphens.
Areas: `rag`, `llm`, `digest`, `qa`, `library`, `db`, `backend`, `frontend`, `docs`, `chore` (tooling and config).

## Commit messages

Start with a verb, say what the commit does: `Add /students endpoint`, `Fix date filter in digest`.
Not: `update`, `fix`, `asdf`.

## Pull requests

- One task per pull request. Small is better: under about 300 changed lines is easy to review
- CI must be green and 1 reviewer must approve before merging. New commits reset the approval
- You cannot approve your own pull request
- Reviewers respond within 1 to 2 days. Use **Request changes** with a clear "change X to Y", not vague comments
- Changing `docs/api.md` needs the project manager's agreement

## Code rules

- Stay inside your area's folder
- Every feature comes with tests in a `tests/` folder next to the code
- Add libraries with `uv add --group <area> <package>`, never `pip install`. Commit the updated `uv.lock`
- Secrets only in `.env`, read with environment variables. New variable names go in `.env.example`
- No real student data in the repo, ever. Use fake data from `db/seed/`
- Student data never goes to a cloud LLM API. Use the local model or pseudonymize first

## Review checklist (for reviewers)

1. Does it do what the task asked?
2. Is it inside the author's own folder?
3. No secrets, no real student data?
4. Are there tests, and do they test something meaningful?
5. Is the code readable without the author explaining it?

## Stuck?

Ask in the team chat after 30 minutes of being stuck. Do not stay silent for a day.
