# syntax=docker/dockerfile:1.6
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PYTHONPATH=/app

WORKDIR /app

# APT robusto (menos falhas intermitentes)
RUN set -eux; \
    printf 'Acquire::Retries "5";\nAcquire::http::Timeout "30";\nAcquire::https::Timeout "30";\n' \
    > /etc/apt/apt.conf.d/80-retries

# Dependências mínimas de build p/ libs C (bs4/lxml etc.)
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    ca-certificates curl git build-essential \
    libxml2-dev libxslt-dev \
    ; \
    rm -rf /var/lib/apt/lists/*

# Usuário não-root
RUN useradd -m appuser && mkdir -p /app && chown -R appuser:appuser /app
USER appuser

# Preferível: pegar uv do container oficial (sem curl|sh)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /home/appuser/.local/bin/uv
ENV PATH="/app/.venv/bin:/home/appuser/.local/bin:${PATH}"

# Maximiza cache: só manifests primeiro
COPY --chown=appuser:appuser pyproject.toml uv.lock README.md ./
RUN mkdir -p /app/.venv

# -------------------------
# DEV IMAGE (com extras)
# -------------------------
FROM base AS dev
ARG INSTALL_DEV=0
RUN if [ "$INSTALL_DEV" = "1" ]; then \
    uv sync --frozen --extra dev; \
    else \
    uv sync --frozen --no-dev; \
    fi
COPY --chown=appuser:appuser . .
CMD ["bash"]

# -------------------------
# RUNTIME IMAGE (lean)
# -------------------------
FROM base AS runtime
RUN set -eux; \
    uv sync --frozen --no-dev
COPY --chown=appuser:appuser . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
