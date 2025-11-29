 # CI/CD + Semantic Release — FastAPI CRUD App
 ![GitHub Actions](https://img.shields.io/github/actions/workflow/status/MichAdebayo/CI-CD-semantic-release/ci.yml?branch=main)
 ![Semantic Release](https://img.shields.io/badge/release-python--semantic--release-orange?logo=semantic-release)
 ![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python)
 ![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-009688?logo=fastapi)
 ![Docker](https://img.shields.io/badge/docker-enabled-blue?logo=docker)
 ![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

<img align="center" width="900" height="700" alt="Image" src="https://github.com/user-attachments/assets/563061c5-9421-4f9c-97eb-1fe1d591d905" />

A small FastAPI-based CRUD application and a hands-on CI/CD reference using semantic-release, GitHub Actions, Docker, and best-practice tooling.

 ---

 ## Table of Contents
 - Overview
 - Key Features
 - Project Structure
 - Tech Stack
 - Installation
 - Configuration / Environment
 - Running the App
 - API Usage (Examples)
 - Tests
 - CI / Release / Deployment
 - Roadmap
 - Contributing
 - License
 - Acknowledgements

 ---

 ## Overview
 This repository is a minimal, production-like FastAPI application (Items CRUD) intended as a reference for implementing robust CI/CD pipelines with semantic-release and GitHub Actions. The project includes:

 - A FastAPI service with SQLModel models and PostgreSQL configuration
 - Business logic in a separate service layer
 - An automated release configuration using python-semantic-release
 - CI checks: linting (ruff), testing (pytest), type checking (mypy) and docs deployment via MkDocs
 - Helper scripts for local release and Docker image builds

 This repository is helpful if you want to learn how to integrate semantic-release into a Python project and build reliable CI/CD pipelines that automate versioning, changelogs, and publishing.

 ---

 ## Key Features
 - Small, well-separated FastAPI app with SQLModel + SQLAlchemy
 - Clear test coverage via pytest (unit and integration tests)
 - Semantic-release setup for automated versioning and changelog generation
 - GitHub Actions pipeline for linting, tests, and documentation deployment
 - Docker support for containerized builds
 - `scripts/release.sh` for local testing of the release flow
 - Multi-workflow CI/CD (CI, Release, CD) with GitHub App-based release auth
 - Container image build & push to GHCR with Trivy scanning and automated Render deploy

 ---

 ## Project Structure
 ```
 .
 ├── .github/                   # GitHub workflows
 │   └── workflows/
 │       ├── ci.yml            # CI checks — lint, tests, docs, triggers release workflow
 │       ├── release.yml       # Release workflow — uses GitHub App + semantic-release
 │       └── cd.yml            # CD workflow — build & push Docker images, scan, deploy to Render
 ├── app/                       # Application package
 │   ├── main.py                # FastAPI app, routes and lifespan
 │   ├── database.py            # SQLModel engine and db session generator
 │   ├── logging_config.py      # centralized logging configuration
 │   ├── models/                # SQLModel models (Item)
 │   ├── routes/                # Routers (items router)
 │   ├── schemas/               # DTOs / Pydantic / SQLModel schemas
 │   └── services/              # Business logic for CRUD operations
 ├── docs/                      # MkDocs content for documentation and workshop notes
 ├── tests/                     # Unit & Integration tests (pytest)
 ├── scripts/                   # Useful helper scripts (release, docker-build)
 ├── Dockerfile                 # Container image build file
 ├── CHANGELOG.md               # Managed by semantic-release
 ├── pyproject.toml             # Project metadata and tooling configuration
 └── README.md
 ```

 ---

 ## Tech Stack ✨
 - Python 3.13
 - FastAPI (HTTP API)
 - SQLModel (models + SQLAlchemy under the hood)
 - PostgreSQL (runtime DB) — SQLite is used for tests
 - python-semantic-release (automated versioning & changelog)
 - GitHub Actions (CI) — `ci.yml` example present
 - Docker (for containerization)
 - MkDocs (docs site)
 - uv (Astral) as a lightweight orchestration wrapper for Python commands

 ---

 ## Installation (Local Development)
 These steps assume macOS/Linux zsh. The project uses `uv` (Astral) for fast, ephemeral environments by default; if you use pip, venv or poetry, adapt accordingly.

 1. Clone the repository
 ```bash
 git clone https://github.com/MichAdebayo/CI-CD-semantic-release.git
 cd CI-CD-semantic-release
 ```

 2. Install `uv` (Astral) if you want to follow repo commands exactly
 ```bash
 curl -LsSf https://astral.sh/uv/install.sh | sh
 ```

 3. Install dependencies
 ```bash
 # Install app & dev dependencies using uv
 uv sync --dev  # syncs install using uv to the virtual environment
 ```

 4. Optional: Create local `.env` to override environment variables for development
 ```bash
 # Example .env.example file
 DATABASE_URL="ENTER YOUR DATABASE_URL"
 DEBUG_MODE="CHOOSE A DEBUG_MODE"
 ```

 ---

 ## Configuration / Environment Variables
 This app reads a few environment variables. Set them (e.g., in `.env`) or in the CI as repository secrets:

 - `DATABASE_URL` — Full DB connection string
 - `DEBUG_MODE` — Enable debug behavior in fastapi (optional)
 - `GITHUB_TOKEN` — Required for `semantic-release` to create tags & GitHub releases
 - CI secrets used in GitHub Actions include repository-level secrets shown in `ci.yml`
 - `APP_ID`, `APP_PRIVATE_KEY_B64` — Configure a GitHub App for `release.yml` to create short-lived tokens with least privilege
 - `DEPLOY_URL` — Render webhook to trigger deployment from `cd.yml` (used on `main` releases)
 - `GHCR_PAT` / `GHCR_USER` — Optional: local credentials used by `scripts/docker-build.sh` for manual GHCR login

Setting up GitHub App (quick steps):

1. Go to GitHub → Settings → Developer settings → GitHub Apps → New GitHub App.
2. Configure the app with repository-level permissions: select minimal write access to `contents`, `packages`, and `actions` as needed.
3. Generate a private key for the app and copy the Base64-encoded version into the repository secret `APP_PRIVATE_KEY_B64`.
4. Copy the `APP_ID` value into the repository secret `APP_ID`.
5. Add `DEPLOY_URL` as a secret (Render webhook URL) — used by the CD workflow to trigger a deploy on successful `main` release.

Note: Use GitHub repository secrets for these values. Do not check private keys or tokens into the repository.

Never commit secrets into the repo. Use GitHub repository secrets for CI workflows.

Environment file template
-------------------------
This repository provides a `.env.example` file with placeholder values for local development. The file contains `# pragma: allowlist secret` comments on sensitive placeholders so that security hooks (e.g., detect-secrets) accept the template as safe.

Best practice:
- Keep `.env.example` with placeholders only — **do not** add real secrets here.
- Add the real values to repository secrets for CI or to a local `.env` for development.

 ---

 ## Running the App
 Run the dev server with hot reload (recommended during development):
 ```bash
 uv run fastapi dev app/main.py
 ```

 Or run with uvicorn directly:
 ```bash
 uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
 ```

 In production (containerized):
 1. Build image with script
 ```bash
 ./scripts/docker-build.sh myorg/items:latest
 ```
 2. Run container
 ```bash
 docker run -p 8000:8000 --env DATABASE_URL="postgresql://..." myorg/items:latest
 ```

 ---

 ## API Usage Examples
 The app exposes a simple items CRUD at `/items` — path prefix is `/items`.

 Health & root endpoints:
 ```bash
 curl http://127.0.0.1:8000/
 curl http://127.0.0.1:8000/health
 ```

 Create item
 ```bash
 curl -X POST http://127.0.0.1:8000/items \
	 -H "Content-Type: application/json" \
	 -d '{"nom":"Keyboard","prix":49.99}'
 ```

 Get items
 ```bash
 curl http://127.0.0.1:8000/items
 ```

 Get single item
 ```bash
 curl http://127.0.0.1:8000/items/1
 ```

 Update item
 ```bash
 curl -X PUT http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d '{"prix":59.99}'
 ```

 Delete item
 ```bash
 curl -X DELETE http://127.0.0.1:8000/items/1
 ```

 Swagger UI (interactive): http://127.0.0.1:8000/docs
 ReDoc: http://127.0.0.1:8000/redoc

 ---

 ## Tests
 Run the full test suite locally (unit + integration) using `uv` for the environment management used by the repo:
 ```bash
 uv run pytest -q
 ```

 What the test suite covers:
 - Unit tests for the `Item` model and service layer (CRUD + edge cases)
 - Integration tests exercising FastAPI endpoints/handlers using `TestClient` with an in-memory SQLite test engine
 - Optional: coverage and linting is configured in CI

 ---

 ## CI / Release / Deployment
 This repository uses a multi-workflow GitHub Actions setup to separate responsibilities and secure the release flow. The three main workflows are:

 - `.github/workflows/ci.yml` — CI: installs dependencies, runs linting, tests, and docs deploy. It also triggers the release workflow via `workflow_call` if criteria are met.
 - `.github/workflows/release.yml` — Release: authenticates using a GitHub App token (created from `APP_ID` and `APP_PRIVATE_KEY_B64`), runs `python-semantic-release`, and publishes a GitHub Release (or runs a dry-run for PR validation). When a release is published, it invokes the CD workflow.
 - `.github/workflows/cd.yml` — CD: prepares Docker tags, builds & pushes Docker images to `ghcr.io/<repo>`, runs a Trivy image scan, and triggers a Render webhook for `main` stable releases.

Key CI & Release details (read the workflows for full logic):

 - CI runs on `develop` and `main` for pushes and PRs. It runs checks and triggers the `release.yml` workflow which either does a dry-run (for PRs) or publishes a release (for main/develop).
 - `release.yml` creates a short-lived GitHub App token (using `APP_ID` + `APP_PRIVATE_KEY_B64`) and runs `uv run semantic-release` to compute the next version and publish. For PRs it runs a safe dry-run; for `main` and `develop` it may publish depending on branch rules defined in `pyproject.toml`.
 - `cd.yml` (CD workflow) prepares the Docker tags (e.g., `ghcr.io/<repo>:latest`, `ghcr.io/<repo>:vX.Y.Z`), performs a BuildKit build and push using `GITHUB_TOKEN` (with `packages: write` permission), runs a Trivy vulnerability scan, and if publishing on `main` it triggers a Render webhook (`DEPLOY_URL`) to start a deploy.

Branching and version behaviour:

 - `main` — Stable releases and production deploys. Releases created on `main` run CD and trigger the Render webhook.
 - `develop` — Development releases and prereleases. Release flow may publish prereleases depending on configuration.
 - `deploy/ci_cd` — Optional branch for CI/CD testing and prerelease token `ci_cd` (as configured in `pyproject.toml`).

Required repository secrets and auth for CI/CD:

 - `APP_ID` — GitHub App ID used by `release.yml` to create a scoped token.
 - `APP_PRIVATE_KEY_B64` — Base64-encoded private key for the GitHub App.
 - `DEPLOY_URL` — Render webhook URL used by `cd.yml` to trigger application deployment (only for `main`).
 - `GITHUB_TOKEN` — Workflow token used to push to GHCR and perform repo actions (CI must have `permissions.packages: write` for `GITHUB_TOKEN` to push images).
 - (Optional) `GHCR_PAT` / `GHCR_USER` — Local Docker push credentials used by `scripts/docker-build.sh` used for manual builds.

Local release helper:
```bash
# Dry-run (prints next tag/version)
./scripts/release.sh

# Publish (requires GITHUB_TOKEN)
GITHUB_TOKEN=ghp_... ./scripts/release.sh --publish --yes
```

Notes:
 - `pyproject.toml` contains the `[tool.semantic_release]` configuration which controls the release behaviour (versioning, tags, changelog, branch rules).
 - Use the `APP_ID` + `APP_PRIVATE_KEY_B64` GitHub App workflow to keep production tokens limited in scope and short-lived. The release workflow creates an app token with the required permissions dynamically.

 ---

 ## Roadmap
 - Improve code coverage and add contract tests for endpoints
 - Expand docs and add hands-on guided notebooks
 - Add CI notifications (Slack/MS Teams) on release

 ---

 ## Contributing
I welcome contributions — here are a few ground rules to make the project pleasant to maintain:

 1. Fork the repository and open a PR with clear description and tests
 2. Use conventional commits to ensure semantic-release correctly updates versions
 3. Add tests for any substantial change
 4. Run formatting and linting before opening a PR (see `ci.yml` steps)

 Suggested commands for local dev:
 ```bash
 uv run ruff check app tests
 uv run pytest -q
 ```

 ---

 ## License
 This repository is distributed under the MIT License. See the `LICENSE` file for details.

 ---

 ## Acknowledgements
 - Built for learning and demonstrating CI/CD patterns around semantic-release with Python and FastAPI

## Author
- [Michael Adebayo](https://github.com/MichAdebayo)
