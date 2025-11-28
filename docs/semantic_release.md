---
title: Semantic Release
---

# 🚀 Semantic Release — Automated Versioning & Publishing

This page explains how **semantic release** works in general and how it's specifically configured and applied in this project. Semantic release automates versioning, changelog generation, and publishing based on conventional commit messages.

---

## Contents

- [What is Semantic Release?](#what-is-semantic-release-)
- [How It Works](#how-it-works-)
- [Configuration in This Project](#configuration-in-this-project-)
- [Branching Strategy & Versioning](#branching-strategy--versioning-)
- [GitHub Actions Workflow](#github-actions-workflow-)
- [Conventional Commits](#conventional-commits-)
- [Examples](#examples-)
- [Troubleshooting](#troubleshooting-)

---

## What is Semantic Release? 🤖

**Semantic Release** is a tool that automates the release process for software projects. It analyzes commit messages to determine the next version number, generates changelogs, creates Git tags, and can publish to package registries or VCS releases.

### Key Benefits

- **Automated Versioning**: No more manual version bumps — versions are calculated from commit history
- **Consistent Releases**: Enforces semantic versioning (SemVer) and conventional commits
- **Changelog Generation**: Automatically creates detailed changelogs from commit messages
- **CI/CD Integration**: Works seamlessly with GitHub Actions, GitLab CI, etc.

### Core Concepts

- **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH` (e.g., `1.2.3`)
- **Conventional Commits**: Standardized commit message format for automation
- **Release Channels**: Different branches can produce different types of releases

---

## How It Works 🔄

1. **Analyze Commits**: Scans commit messages since the last release
2. **Determine Version Bump**:
   - `fix:` commits → PATCH bump (e.g., `1.0.0` → `1.0.1`)
   - `feat:` commits → MINOR bump (e.g., `1.0.0` → `1.1.0`)
   - Breaking changes → MAJOR bump (e.g., `1.0.0` → `2.0.0`)
3. **Update Version**: Modifies `pyproject.toml` (or other files)
4. **Generate Changelog**: Creates/updates `CHANGELOG.md`
5. **Create Git Tag**: Tags the commit with the new version
6. **Publish**: Uploads to PyPI, creates GitHub release, etc.

!!! note "Dry-Run Mode"
    You can test semantic release locally with `--print` or `--no-commit` flags to see what would happen without making changes.

---

## Configuration in This Project ⚙️

This project uses **`python-semantic-release`** (PSR) with configuration in `pyproject.toml`.

### Key Settings

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]  # Where to update version
tag_format = "v{version}"                         # Git tag format (e.g., v1.2.3)
upload_to_pypi = false                            # Don't publish to PyPI
upload_to_vcs_release = true                      # Create GitHub releases
build_command = ""                                # No build step needed
commit_message = "chore(release): bump version to {version}"
starting_version = "0.1.0"
allow_zero_version = true
```

### Changelog Configuration

```toml
[tool.semantic_release.changelog]
filename = "CHANGELOG.md"  # Output file for changelog
```

### Branch-Specific Rules

```toml
[tool.semantic_release.branches.main]
match = "main"
prerelease = false  # Produces stable releases (e.g., 1.2.3)

[tool.semantic_release.branches.develop]
match = "develop"
prerelease = true
prerelease_token = "dev"  # Produces dev prereleases (e.g., 1.2.3-dev.1)

[tool.semantic_release.branches."deploy/ci_cd"]
match = "deploy/ci_cd"
prerelease = true
prerelease_token = "ci_cd"  # Produces ci_cd prereleases (e.g., 1.2.3-ci_cd.1)
```

---

## Branching Strategy & Versioning 🌿

### Release Branches

- **`main`**: Production releases (stable versions like `1.2.3`)
- **`develop`**: Development releases (prereleases like `1.2.3-dev.1`)
- **`deploy/ci_cd`**: CI/CD testing releases (prereleases like `1.2.3-ci_cd.1`)

### Version Calculation

- **Stable Releases** (main): Based on conventional commits since last stable tag
- **Prereleases** (develop/deploy/ci_cd): Increment prerelease counter on every qualifying commit

!!! tip "Prerelease Tokens"
    Prerelease versions include a token (e.g., `-dev.1`, `-ci_cd.1`) to distinguish them from stable releases.

---

## GitHub Actions Workflow 🔧

The release process is automated via `.github/workflows/release.yml`.

### Trigger Conditions

- Runs on pushes to `main`, `develop`, or `deploy/ci_cd` branches
- Uses GitHub App authentication for secure token management
- Called via `workflow_call` from other workflows

### Workflow Steps

1. **Authentication**: Creates GitHub App token
2. **Checkout**: Fetches full git history and tags
3. **Setup**: Installs uv and dependencies
4. **Dry-run** (PRs): Simulates release for pull requests
5. **Release** (main/develop): Runs `semantic-release version --changelog` and `semantic-release publish`
6. **CD Trigger**: Calls deployment workflow if a new version was created

### Key Commands

```bash
# Version bump and changelog
uv run semantic-release version --changelog

# Publish (create GitHub release)
uv run semantic-release publish
```

!!! warning "Git Configuration"
    The workflow configures git with a bot user to avoid commit attribution issues.

---

## Conventional Commits 📝

All commits must follow the **Conventional Commits** format for semantic release to work:

```
type(scope): description

[body]

[footer]
```

### Commit Types

- `feat:` → MINOR version bump
- `fix:` → PATCH version bump
- `docs:`, `style:`, `refactor:`, `perf:`, `test:`, `chore:` → No version bump (unless breaking)
- `BREAKING CHANGE:` → MAJOR version bump

### Breaking Changes

- Add `!` after type: `feat(api)!: remove deprecated endpoint`
- Or use footer: `BREAKING CHANGE: description`

### Examples

```bash
git commit -m "feat: add user authentication endpoint"
git commit -m "fix: resolve database connection timeout"
git commit -m "feat!: redesign API with breaking changes"
```

---

## Examples 📋

### Stable Release (main branch)

**Commits since v1.1.0:**
- `feat: add export functionality`
- `fix: correct typo in error message`

**Result:** Version `1.2.0`, tag `v1.2.0`, GitHub release created

### Prerelease (develop branch)

**Commits since v1.2.0-dev.2:**
- `feat: implement new dashboard`

**Result:** Version `1.2.0-dev.3`, tag `v1.2.0-dev.3`

### Local Testing

```bash
# Dry-run to see next version
uv run semantic-release version --print

# Full simulation (no changes)
uv run semantic-release version --no-commit --no-tag --no-push
```

---

## Troubleshooting 🔍

### Common Issues

!!! question "No version bump occurred"
    **Cause:** No conventional commits since last release
    **Fix:** Ensure commits use proper format (`feat:`, `fix:`, etc.)

!!! question "Authentication failed"
    **Cause:** GitHub token issues
    **Fix:** Check GitHub App configuration and secrets

!!! question "Version file not updated"
    **Cause:** Incorrect `version_toml` path
    **Fix:** Verify `pyproject.toml:project.version` exists

### Useful Commands

```bash
# Check current version
uv run semantic-release version --print

# View changelog without committing
uv run semantic-release version --changelog --no-commit

# Debug commit parsing
uv run semantic-release version --verbosity DEBUG
```

### Local Release Script

Use `scripts/release.sh` for local testing:

```bash
# Dry-run
./scripts/release.sh

# Publish (requires GITHUB_TOKEN)
GITHUB_TOKEN=ghp_... ./scripts/release.sh --publish
```

---

For more details, see the [Python Semantic Release documentation](https://python-semantic-release.readthedocs.io/) or check the project's `pyproject.toml` configuration.
