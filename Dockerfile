FROM python:3.13-slim AS builder

WORKDIR /src

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv into builder so we can use uv sync/pip consistently
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_SYSTEM_PYTHON=1

# Copy dependency files first for caching
COPY pyproject.toml uv.lock ./

# Install build/runtime dependencies (uv will read pyproject/uv.lock)
RUN uv sync --dev || true

    # Install the package into the builder image
    COPY . .
    RUN uv pip install .

FROM python:3.13-slim

WORKDIR /app

# Create non-root user with a home directory
RUN groupadd --system app && useradd --system --gid app --home /home/app --create-home app

# Ensure home and cache dirs exist and are owned by the app user
RUN mkdir -p /home/app/.cache/uv && chown -R app:app /home/app
ENV HOME=/home/app

# Copy uv binary for runtime
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_SYSTEM_PYTHON=1

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /usr/lib /usr/lib

# Copy application code
COPY --from=builder /src /app

# Change ownership of /app to app user
RUN chown -R app:app /app

USER app

EXPOSE 8000

# Run using uvicorn ASGI server
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
