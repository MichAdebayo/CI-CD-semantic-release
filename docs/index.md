---
title: CI/CD + Semantic Release — Workshop & Reference
---

# 🚀 CI/CD + Semantic Release — Workshop & Reference

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Workflows-2088FF?style=flat-square&logo=github-actions)](https://github.com/features/actions)
[![MkDocs](https://img.shields.io/badge/MkDocs-Material-7B61FF?style=flat-square&logo=mkdocs)](https://squidfunk.github.io/mkdocs-material/)

> This repository is an interactive workshop and reference for building a professional CI/CD pipeline around a FastAPI application. It covers semantic release, code quality (linters/formatters/type checking), security scans and automated release practices.

---

## Quick start

Run these commands from the repository root (zsh). Examples use `uv` (Astral); adapt to your environment if you prefer `pip`/`venv`/`poetry`.

```bash
# install / sync dependencies
uv sync

# run the app in development (auto-reload)
uv run fastapi dev app/main.py

# run tests
uv run pytest

# quick lint check
uv run ruff check .
```

---

## What you'll find in this documentation

- 🎯 **Workshop brief** — `docs/brief.md` — workshop plan, phases and learning objectives
- 🔎 **Tool survey** — `docs/tool_survey.md` — CI/CD concepts, `uv`, and semantic-release overview
- 🧰 **Tool comparison** — `docs/tool_comparison.md` — recommended tools and setup guidance
- 🛠️ **Problems detected** — `docs/problems_detected.md` — audit results and prioritized fixes

---

## Project overview (structure)

Top-level layout:

```
app/
	├─ main.py            # FastAPI application entry
	├─ database.py        # DB engine and session helpers
	├─ logging_config.py  # logging setup
	├─ models/            # SQLModel models
	├─ routes/            # API routers (items)
	├─ schemas/           # Pydantic/SQLModel schemas
	└─ services/          # business logic

docs/                   # MkDocs content (this site)
tests/                  # unit & integration tests (pytest)
mkdocs.yml              # docs configuration
pyproject.toml          # project metadata and tool config
```

## Development notes

- The app is a small CRUD API (Items) backed by PostgreSQL (SQLModel + SQLAlchemy).
- Use environment variables and a `.env` file for secrets and configuration; do not commit sensitive values.
- Semantic release is configured in `pyproject.toml` (see `[tool.semantic_release]`). The project uses Conventional Commits to generate changelogs and releases.

## Useful commands

```bash
# development server
uv run fastapi dev app/main.py

# run tests
uv run pytest

# lint (ruff)
uv run ruff check .

# format (optional)
uv run ruff format .

# build docs locally
uv run mkdocs build
uv run mkdocs serve
```

## CI / Release

- Recommended CI flow: lint → type-check → tests → security scans → semantic release.
- Semantic release settings are present in `pyproject.toml` (`[tool.semantic_release]`). CI must provide a token (e.g. `GH_TOKEN`) to publish releases.
