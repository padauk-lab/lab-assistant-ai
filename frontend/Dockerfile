FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /usr/local/bin/uv

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PROJECT_ENVIRONMENT=/opt/venv

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-default-groups --group frontend

COPY frontend ./frontend

RUN useradd --create-home appuser
USER appuser

EXPOSE 8501
CMD ["/opt/venv/bin/streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
