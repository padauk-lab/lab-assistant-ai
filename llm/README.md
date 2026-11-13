# llm/

The chat brain. Runs an open model locally with Ollama and answers using tools.

**Owner:** AI group (LMHP, SWYG, KZN)

## What goes here

- `tools/` wraps the backend API and RAG search so the model can call them
- `prompts/` holds system prompts
- A pseudonymize step (S01, S02 and so on) before any text with student data goes to a free cloud API
