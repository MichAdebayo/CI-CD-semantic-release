---
title: Contributor Guide
---

# 🤝 Contributor Guide (Internal)

This guide explains how to set up a local environment, run checks, and follow the repository quality rules. It's written for contributors working directly on this repo.

---

## Prerequisites

- Python 3.13 or newer
- `uv` (project dependency manager). Install with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- (Optional) Docker — useful when running PostgreSQL for integration tests.

---

## Initial setup — install dependencies

1. Sync project dependencies into `uv`:

```bash
uv sync
```

2. (Optional) If you use a local virtualenv, activate it:

```bash
source .venv/bin/activate
```

---

## Pre-commit hooks

We use `pre-commit` to enforce quality checks before commits. Current hooks include:

- `ruff` (lint & format)
- `mypy` (type checking)
- `bandit` (security checks)
- `detect-secrets` (secrets scanning)
- `pytest` (tests)

### Install and enable

```bash
# Install pre-commit (via uv to use the project runtime)
uv run pip install pre-commit

# Install hooks into your local Git config
pre-commit install
```

### Run hooks manually

```bash
# Run all hooks against all files
pre-commit run --all-files

# Run a single hook (example: ruff)
pre-commit run ruff --all-files
```

Note: The `pytest` hook is configured to run `uv run pytest -q` so it executes within the `uv` environment and resolves project dependencies such as `sqlmodel` and `fastapi`.

If a hook auto-fixes files (for example `ruff --fix`), re-add the changed files and commit again:

```bash
git add <files>
git commit -m "chore: apply auto-formatting"
```

---

## Useful verification commands

Run these locally to validate code before pushing:

```bash
# Lint (ruff)
uv run ruff check app tests

# Format check
uv run ruff format --check app tests

# Type checking
uv run mypy app

# Security scan
uv run bandit -r app/

# Unit & integration tests
uv run pytest -q

# Generate detect-secrets baseline (once)
uv run detect-secrets scan > .secrets.baseline
```

---

## `detect-secrets` baseline

- We keep a `.secrets.baseline` file at the repo root to avoid failing on historical false positives.
- If you add a real secret, `detect-secrets` will surface it. To add a false positive to the baseline, use the `detect-secrets` tooling—but be cautious and review with the team.

::: warning
Do not commit real secrets. If you encounter a secret, rotate it immediately and follow the project's secret management policy.
:::

---

## Common issues & troubleshooting

- ModuleNotFoundError for `sqlmodel` or other deps in pre-commit: ensure `uv` is installed and you've run `uv sync` so hooks run with the right environment.
- `mypy` reports `import-not-found`: ensure the hook has the additional dependencies configured, or run `uv sync` locally.
- Formatting fixes not applied: run `uv run ruff check --fix .` then re-commit the changes.

If a local fix doesn't resolve the CI failure, run the same commands locally and open a PR documenting steps taken.

---

## Updating pinned hook/tool versions (manual process)

We pin hook and tool versions for stability. If you must update a tool (e.g. `mypy`, `ruff`) follow this workflow:

1. Create a branch: `chore/update-tools`
2. Update the `rev` or version in `.pre-commit-config.yaml`.
3. Run locally:

```bash
pre-commit clean
pre-commit run --all-files
uv run pytest -q
```

4. If checks pass, open a PR and let CI run the same checks before merging into `develop`.

::: tip
Avoid running `pre-commit autoupdate` blindly. Always run the full local checks and tests after any change to hook versions.
:::

---

## CI & branch protection

- CI runs on pushes to `develop` and `main`, and on pull requests targeting `develop`.
- CI jobs include: linting (`ruff`), format checks, type checking (`mypy`), security scans (`bandit`, `detect-secrets`), and tests (`pytest`).
- PRs must pass all checks before merging. Branch protection can enforce this.

---

## Commit & PR workflow (simple)

1. Run quick checks before you start working:

```bash
uv run ruff check app tests
uv run mypy app
uv run pytest -q
```

2. When ready to commit:

```bash
git add .
pre-commit run --files <changed files> || pre-commit run --all-files
git commit -m "feat: short description"
git push origin <branch>
```

3. Open a PR against `develop`. CI will run the full pipeline.

---

## Notes & contact

- This document is internal and targeted to contributors working on this repository. Coordinate tool-version updates with the team.
- If you need help with CI pipeline changes or tool upgrades, open a PR and add a comment describing the change and why it's needed.

---

Thank you — follow this guide to keep the repository healthy, secure, and consistent.
