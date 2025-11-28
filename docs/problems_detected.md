---
title: Problems Detected — Quality Audit
---

# 🛠️ Problems Detected — Summary & Fix Plan

> **Quick summary:** This page lists quality issues found during a quick review (formatting, security, imports, typing, documentation and dead code). It includes prioritization and concrete remediation steps.

## 📊 Snapshot

- High priority (3): secrets in code, DEBUG enabled, typing errors causing runtime failures
- Medium priority (6): unused imports, incorrect use of Pydantic/SQLModel types
- Low priority (4): formatting, overly long variable names, dead code

---

## ⚠️ Immediate actions (high severity)

!!! danger "Secrets & configuration"
    - `DEBUG` is enabled in `app/main.py` — disable in production and control via environment variables.
    - `secret` and `API_KEY` are set in code — move to `.env` or secret store and read via environment variables or `pydantic.BaseSettings`.

!!! danger "Database"
    - Postgres URL and roles appear misconfigured; verify `DATABASE_URL` in `.env.example` and make sure CI/production point to the correct host.

---

## 🔎 Prioritized issues table

| Issue | File / Location | Severity | Suggested fix |
|---|---|---:|---|
| Incorrect POST endpoint (`/items` vs `/items/`) | `app/routes/items.py` | 🔴 High | Fix route definitions and tests; choose a consistent trailing-slash policy for endpoints. |
| Secrets / API_KEY in code | `app/main.py` | 🔴 High | Move secrets to `.env`, update `.env.example`, use `pydantic.BaseSettings` or `python-dotenv`. |
| DEBUG_MODE enabled | `app/main.py` | 🔴 High | Read from environment and default to False in production. |
| AttributeError: 'str' object has no attribute 'model_dump' | `app/services/item_service.py` | 🔴 High | Ensure endpoint handlers receive typed models (e.g. `item_data: ItemCreate`) and that model instances are used before calling `model_dump`. Add unit tests. |
| Unused imports | `app/database.py`, `app/main.py`, `app/routes/items.py` | 🟠 Medium | Run `ruff --select F401` and remove unused imports; run `isort` to keep imports organized. |
| Typing issues in routes/models | `app/models/item.py`, `app/schemas/item.py` | 🟠 Medium | Add explicit annotations (e.g. `__tablename__: str = "items"`), use consistent type hints and run `mypy`. |
| Missing docstrings | `app/routes/*` | 🟢 Low | Add docstrings for endpoints (description, parameters, responses). |
| Dead code (`_old_helper_function`, `_legacy_method`) | `app/routes/items.py`, `app/models/items.py` | 🟢 Low | Remove unused/legacy functions or clearly mark them and add tests if they must remain. |

---

## ✅ Suggested remediation plan (iterative)

1. Remove secrets from source code and secure configuration in CI.
2. Fix runtime errors (e.g. `model_dump`) by adding types and targeted unit tests.
3. Run `ruff --fix` and `isort`, then validate types with `mypy`.
4. Remove dead code and add missing docstrings.
5. Add `pre-commit` hooks (`ruff`, `isort`, `black`) and CI jobs for linting, typing and tests.

---

## 🗂️ Quick checklist (tick as you go)

- [ ] Secrets removed from source
- [ ] `.env.example` updated with placeholders
- [ ] `DEBUG` controlled via environment
- [ ] Runtime type issues (e.g. `model_dump`) fixed and covered by tests
- [ ] Imports cleaned (`ruff --fix`, `isort`)
- [ ] Docstrings added
- [ ] Dead code removed
