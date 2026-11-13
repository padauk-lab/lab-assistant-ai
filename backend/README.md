# backend/

The API server. Every other part (frontend, chat, Monday email) talks to the database only through this API.

**Owner:** Data group (ANK, TDS)

## What goes here

- One route file per resource: students, progress, equipment, loans, questions, answers, library
- Endpoints must match `docs/api.md` exactly
- Access rules live here: students see only their own data, the professor sees all
