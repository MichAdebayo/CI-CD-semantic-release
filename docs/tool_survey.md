# CI/CD Technical Watch 🚀

!!! info "Document Overview"
    This document provides a comprehensive overview of CI/CD practices, tools, and modern Python development workflows.

---

## 📑 Table of Contents

- [Continuous Integration (CI)](#continuous-integration-ci)
- [Continuous Deployment/Delivery (CD)](#continuous-deploymentdelivery-cd)
- [Why CI/CD Matters](#why-cicd-matters)
- [UV: Modern Python Package Manager](#uv-modern-python-package-manager)
- [Working with pyproject.toml](#working-with-pyprojecttoml)
- [CI/CD with GitHub Actions](#cicd-with-github-actions)
- [Semantic Versioning (SemVer)](#semantic-versioning-semver)
- [Conventional Commits](#conventional-commits)
- [Python Semantic Release](#python-semantic-release)
- [Documentation with MkDocs](#documentation-with-mkdocs)

---

## 🔁 Continuous Integration (CI)

**Continuous Integration (CI)** is an automated process that enables frequent integration of code changes into a shared repository (main branch). With each integration, automated steps such as building and running tests (unit, integration, etc.) are triggered to ensure new changes don't break the application.

!!! success "Main Goal"
    Avoid difficult-to-manage "merge day" situations and detect conflicts and regressions early.

### 🎯 Problems CI Solves

CI addresses several critical development challenges:

- ✅ **Reduces merge conflicts** when integrating multiple branches (eliminates "merge day")
- ⏱️ **Decreases time and effort** required to integrate changes (fewer manual procedures)
- 🐛 **Early bug detection** through automatic test execution
- 🖥️ **Mitigates environment inconsistencies** between different developer setups

### 🔑 Key Principles

!!! tip "Core CI Principles"
    1. **Frequent integrations** into a shared repository (trunk-based development)
    2. **Build automation** and multi-layer testing (unit, integration, etc.)
    3. **Automatic verification** at each step to ensure application functionality
    4. **Fast feedback** to developers for quick conflict/regression fixes

### 🛠️ Popular CI Tools

| Tool | Description |
|------|-------------|
| **Jenkins** | Popular management tool serving as both CI server and complete CD hub |
| **Tekton / OpenShift Pipelines** | Cloud-native CI/CD framework for Kubernetes platforms (especially Red Hat OpenShift) |
| **GoCD** | CI/CD server focused on pipeline modeling and visualization |

---

## 📦 Continuous Deployment/Delivery (CD)

CD encompasses two related but distinct practices:

### 🔄 Continuous Delivery vs Continuous Deployment

!!! info "Two Flavors of CD"

    **Continuous Delivery** 🎯

    - Automates the release of validated code (after CI and tests) to a repository or artifact ready for production
    - Makes code "deployable" at any time
    - Production deployment remains manual, managed by operations teams

    **Continuous Deployment** 🚀

    - Takes automation further: changes that pass all tests are automatically released to production
    - No manual intervention required

### ⚖️ Benefits and Risks

=== "Benefits ✅"

    - 🐛 Reduced bugs and code failures
    - ⚡ Reduced downtime and faster releases
    - 👥 Faster user feedback integration and better satisfaction
    - 🔧 Reduced complexity and improved workflow efficiency

=== "Risks ⚠️"

    - 🚨 Poorly designed automation can deploy incorrect or vulnerable code if testing is insufficient
    - 🔓 Possible exposure of sensitive data if pipelines aren't secured
    - 🔒 Use of unsecured third-party components (vulnerabilities) without rigorous verification
    - 👤 Unauthorized access to code repositories or development tools with weak security controls
    - 💰 Continuous deployment requires significant upfront investment to define and automate reliable tests and controls (shift-left / shift-right)

---

## 💡 Why CI/CD Matters

### 🎨 Impact on Code Quality

!!! success "Quality Improvements"
    Automated tests and frequent checks enable rapid error detection and ensure each change meets quality criteria, reducing regressions and improving code reliability.

### ⚡ Impact on Development Speed

!!! tip "Accelerated Delivery"
    Automation of build, test, and release steps significantly reduces the time between writing code and making it available, accelerating the feature release cycle and user feedback integration.

### 🤝 Impact on Team Collaboration

!!! info "Enhanced Teamwork"
    CI/CD fosters a DevOps culture and better collaboration between development and operations teams by:

    - Reducing friction from manual operations
    - Encouraging shared responsibility (including security - DevSecOps)
    - Facilitating environment standardization
    - Ensuring deployment reproducibility

---

## 🧰 UV: Modern Python Package Manager

**UV** is a modern Python project and dependency manager written in Rust. It aims to replace multiple traditional tools (`pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, etc.) by offering a consistent interface for managing environments, Python versions, tools, and dependencies.

!!! tip "Key Features"
    - 🐍 Installs and manages Python versions (`uv python install`)
    - 📁 Manages project environments (creates `.venv` and uses `uv sync`/`uv run`)
    - 📦 Handles dependencies and lockfile (`uv.lock`) with multi-platform resolution
    - 🔧 Provides features for scripts, tools, and workspaces (similar to Cargo)

### 🆚 Differences from pip/poetry/pipenv

| Aspect | UV Advantage |
|--------|--------------|
| **Unification** | Replaces multiple tools with a single interface |
| **Performance** | 10-100x faster than pip in many scenarios ⚡ |
| **Project Management** | Centralized with universal `uv.lock` and features like `dependency-groups` |
| **Compatibility** | Provides pip-compatible interface (`uv pip`) for easy migration |

### ✨ Key Advantages

!!! success "Why Choose UV?"
    - ⚡ **Speed**: 10-100x faster than `pip` in certain scenarios
    - 🎯 **Tool Unification**: Combines multiple responsibilities (environments, tools, Python installations) in one tool
    - 🔒 **Reproducibility**: `uv.lock` ensures consistent installations across all platforms
    - 💾 **Global Cache**: Reduces disk space and downloads with shared cache and pruning (`uv cache prune --ci`)
    - 📚 **Workspaces & Scripts**: Strong support for monorepos and scripts with inline metadata
    - 🔄 **Interoperability**: `uv pip` interface and export to `pylock.toml` for compatibility

---

## 🔧 Working with pyproject.toml

### 📋 File Structure

UV relies on `pyproject.toml` to identify the project root and store configuration.

!!! info "Key Sections"

    **`[project]`** - Basic metadata

    - `name`, `version`, `requires-python`
    - `dependencies` (PEP 621)
    - `optional-dependencies`

    **`[build-system]`** - Build configuration

    - `requires` and `build-backend` (to use `uv_build`)

    **`[tool.uv]`** - UV-specific settings

    - `default-groups`, `dev-dependencies` (legacy)
    - `workspace` settings

    **`uv.lock`** - Lockfile (automatically created, should be version controlled)

### 📦 Dependency Management

Dependencies are organized by purpose:

=== "Production"
    ```toml
    [project]
    dependencies = [
        "requests>=2.28.0",
        "pydantic>=2.0.0",
    ]
    ```

=== "Optional Features"
    ```toml
    [project.optional-dependencies]
    plot = ["matplotlib>=3.5.0"]
    excel = ["openpyxl>=3.0.0"]
    ```

=== "Development"
    ```toml
    [dependency-groups]
    dev = ["pytest>=7.0.0", "black>=23.0.0"]
    lint = ["ruff>=0.1.0", "mypy>=1.0.0"]
    test = ["pytest-cov>=4.0.0"]
    ```

=== "Alternative Sources"
    ```toml
    [tool.uv.sources]
    my-package = { git = "https://github.com/user/repo.git" }
    local-package = { path = "../local-pkg" }
    ```

### 🏗️ Build Backend

To use UV as a build backend:

```toml
[build-system]
requires = ["uv_build>=0.9.11,<0.10.0"]
build-backend = "uv_build"
```

!!! tip "Build Backend Configuration"
    The `uv_build` backend has sensible defaults (e.g., `src/` for modules) but is configurable via `tool.uv.build-backend` for module naming, root paths, file inclusion/exclusion, and data directories.

---

## ⚙️ CI/CD with GitHub Actions

### 🔌 Installation

The recommended method is using the official `astral-sh/setup-uv` action:

```yaml
- uses: astral-sh/setup-uv@v6
  with:
    version: "0.9.11"  # Pin version recommended
    enable-cache: true  # Optional
```

### 💾 Dependency Caching

Two approaches for caching:

=== "Automatic (Recommended)"
    ```yaml
    - uses: astral-sh/setup-uv@v6
      with:
        enable-cache: true
    ```

=== "Manual"
    ```yaml
    env:
      UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv

    - name: Restore uv cache
      uses: actions/cache@v4
      with:
        path: ${{ env.UV_CACHE_DIR }}
        key: uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}

    - name: Minimize cache
      run: uv cache prune --ci
    ```

### 🚀 Command Execution

Typical pipeline workflow:

```yaml
# Install UV and Python
- uses: astral-sh/setup-uv@v6
- run: uv python install 3.13

# Install project and dependencies (including dev)
- run: uv sync --locked --all-extras --dev

# Run tests
- run: uv run pytest tests

# Build package
- run: uv build

# Publish to PyPI (on tag)
- run: uv publish
```

!!! warning "Additional Considerations"
    - For `uv pip` (pip interface), use `UV_SYSTEM_PYTHON=1` or `--system` flag for system environment installation
    - For private repositories, configure a PAT and authenticate with `gh auth login` and `gh auth setup-git`
    - For PyPI publishing, use `uv build` then `uv publish` in a GitHub Action after a `v*` tag

---

## 🔢 Semantic Versioning (SemVer)

**SemVer** is a convention that gives clear meaning to version numbers, allowing users and tools to understand the impact of a release.

### 📐 Format

```
MAJOR.MINOR.PATCH[-prerelease][+build]
```

**Example**: `1.2.3-alpha.1+build.123`

### 📈 When to Increment

| Level | When to Increment | Example |
|-------|-------------------|---------|
| 🔴 **MAJOR** | Breaking changes - API/contract incompatibility | `1.0.0` → `2.0.0` |
| 🟡 **MINOR** | New features (backward compatible) | `1.2.3` → `1.3.0` |
| 🟢 **PATCH** | Bug fixes (backward compatible) | `1.2.3` → `1.2.4` |

!!! example "Examples"
    - API-breaking commit → bump **MAJOR**
    - Pre-release versions help testing before stable release
    - Keep `project.version` updated (or use automatic tools like PSR)

---

## ✍️ Conventional Commits

**Conventional Commits** is a specification that standardizes commit message format to make history readable and exploitable by tools (automatic changelog generation, SemVer bump determination, etc.).

### 📝 Message Format

```
<type>(<optional scope>): <description>

[optional body]

[optional footer]
```

### 🏷️ Common Types

| Type | Purpose | Version Impact |
|------|---------|----------------|
| `feat` | New feature | MINOR ⬆️ |
| `fix` | Bug fix | PATCH ⬆️ |
| `docs` | Documentation only | None |
| `style` | Code style/formatting | None |
| `refactor` | Code refactoring | None |
| `perf` | Performance improvement | None |
| `test` | Adding tests | None |
| `chore` | Maintenance tasks | None |
| `ci` | CI configuration | None |
| `build` | Build system changes | None |

### 💥 Breaking Changes

To indicate breaking changes:

=== "Footer Method"
    ```
    feat(api): add new authentication method

    BREAKING CHANGE: Previous auth tokens are no longer valid.
    Users must regenerate their tokens.
    ```

=== "Exclamation Mark"
    ```
    feat(api)!: change authentication format

    Token structure changed from x.y to a.b.c format.
    ```

### 📊 Impact on Versioning

!!! info "Automatic Version Bumps"
    Tools like `python-semantic-release` automatically translate commit types:

    - `fix` → **PATCH** bump
    - `feat` → **MINOR** bump
    - `BREAKING CHANGE` or `!` → **MAJOR** bump

### 💡 Examples

```text
feat(api): add filters to product listing

fix(auth): correct token handling on refresh

perf(db): reduce query time for aggregate requests

feat!: change auth token format

BREAKING CHANGE: token structure changed from `x.y` to `a.b.c`.
```

---

## 🐍 Python Semantic Release

**Python Semantic Release (PSR)** automates version determination from commit messages (SemVer + Conventional Commits), updates project version, generates/updates CHANGELOG, tags the repository, and can publish artifacts and create VCS releases.

### ⚙️ Configuration in pyproject.toml

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
commit_parser = "conventional"
vcs_release = true

[tool.semantic_release.commit_parser_options]
minor_tags = ["feat"]
patch_tags = ["fix", "perf"]
parse_squash_commits = true
ignore_merge_commits = true

build_command = "python -m build --sdist --wheel ."
```

!!! info "Key Configuration Options"
    - **`version_toml`**: Location to update during version bump
    - **`commit_parser`**: Message parser (`conventional` by default)
    - **`commit_parser_options`**: Adjust tags for `minor`/`patch` and handle squash/merge
    - **`build_command`**: Command to build artifacts before publishing

### 📄 CHANGELOG Generation

```toml
[tool.semantic_release.changelog]
changelog_file = "CHANGELOG.md"
output_format = "md"
exclude_commit_patterns = [
    "^chore(?:\\([^)]*?\\))?: .+",
    "^ci(?:\\([^)]*?\\))?: .+",
]
```

### 🏷️ GitHub Releases

PSR can create tags and releases on VCS platforms using an environment token:

```bash
# Set in GitHub Actions
GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 🔧 Useful Commands

=== "Generate Config"
    ```bash
    semantic-release generate-config --pyproject >> pyproject.toml
    ```

=== "Dry Run"
    ```bash
    # See what would happen without changes
    semantic-release -v --noop version

    # Local evaluation without commit/tag
    semantic-release -vv version --no-commit --no-tag
    ```

=== "CI Execution"
    ```bash
    semantic-release version --push --vcs-release
    ```

### ✅ Best Practices

!!! tip "Recommended Practices"
    - ✅ Enforce Conventional Commits via hooks (`commit-msg`) and/or CI linter (`commitlint`)
    - ✅ Test locally and in CI with `--noop` mode to avoid unwanted releases
    - ✅ Protect release branches and use limited-scope tokens for automation
    - ✅ Verify `parse_squash_commits` if using squash merges

---

## 📚 Documentation with MkDocs

### 🏗️ How MkDocs Generates Documentation

MkDocs takes Markdown files (default in `docs/` folder) and a `mkdocs.yml` configuration file to generate static HTML documentation.

=== "Development"
    ```bash
    mkdocs serve
    ```
    Launches a dev server with auto-reload on file changes

=== "Production"
    ```bash
    mkdocs build
    ```
    Generates static HTML in `site/` directory

!!! info "Generation Process"
    1. Reads Markdown files and `mkdocs.yml` configuration
    2. Converts each page to static HTML
    3. Applies theme (e.g., Material)
    4. Copies resources (CSS/JS/images)
    5. Generates search index and sitemap

### 🚀 Deploying to GitHub Pages

=== "Quick Method"
    ```bash
    mkdocs gh-deploy
    ```
    Builds and publishes automatically to `gh-pages` branch

=== "Manual Method"
    ```bash
    mkdocs build
    # Copy site/ contents to gh-pages branch
    ```

=== "GitHub Actions (Recommended)"
    ```yaml
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./site
    ```

!!! warning "Important Configuration"
    Set `site_url` in `mkdocs.yml` for correct link generation, especially when using themes/plugins like Material for MkDocs.

### 🔌 mkdocstrings Plugin

**mkdocstrings** automatically generates API documentation from code docstrings.

!!! success "Key Features"
    - 📝 Auto-generates API docs from docstrings
    - 🌐 Multi-language support via handlers (Python, JavaScript, etc.)
    - 🎨 Natural integration with Material theme
    - 🔄 Documentation stays in sync with code

**Usage Example:**

```markdown
## API Reference

::: mypackage.module.MyClass
    options:
      show_source: true
      members_order: source
```

This extracts signatures, docstrings, and members to produce structured, navigable documentation automatically.

---

!!! success "Summary"
    This guide covers modern CI/CD practices, from continuous integration fundamentals to automated documentation deployment. By combining tools like UV, GitHub Actions, Semantic Release, and MkDocs, you can create a robust, automated development pipeline that improves code quality, accelerates delivery, and enhances team collaboration.
