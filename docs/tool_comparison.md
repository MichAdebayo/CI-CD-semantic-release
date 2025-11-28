# 🧭 Tool Comparison — CI/CD Recommendations

!!! abstract "Document Purpose"
    This document summarizes recommended tooling for FastAPI projects using UV, covering linting, formatting, type checking, testing, and security scanning. The goal is a pragmatic stack that works well locally (fast hooks) and in CI (strict checks).

---

## ⚡ Quick Recommendations

!!! success "Recommended Stack at a Glance"

    | Category | Tool | Why? |
    |----------|------|------|
    | 🔍 **Linting** | Ruff + isort | Blazing fast, comprehensive rules |
    | 🎨 **Formatting** | Black or Ruff Format | Consistent, opinionated styling |
    | 🔎 **Type Checking** | Mypy (CI) + Pyright (IDE) | Best of both worlds |
    | 🧪 **Testing** | pytest + Hypothesis | Industry standard + property testing |
    | 🔐 **Security** | Bandit + Semgrep + Safety + Trivy | Multi-layered protection |

---

## 🔍 Linters — Speed, Rules & Ergonomics

Comparing tools for code quality and style enforcement.

| Tool | Category | Pros | Cons | Score | Status |
|------|----------|------|------|------:|--------|
| **Ruff** | Linter | ⚡ Very fast (Rust-based)<br/>📦 Combines linting, fixing & formatting<br/>⚙️ Supports `pyproject.toml` | ⚠️ Fewer deep analysis rules than Pylint for legacy code | 9/10 | ✅ **Recommended** |
| **Flake8** | Linter | 🔌 Mature ecosystem with many plugins<br/>📚 bugbear, docstrings, etc. | 🐌 Slower on large codebases<br/>🔌 Relies heavily on plugins | 7/10 | ⚠️ Specific contexts |
| **Pylint** | Linter | 🔬 Deep static analysis<br/>📊 Code smells & complexity metrics | 🗣️ Verbose and slow by default<br/>⚙️ Requires extensive tuning | 7/10 | ⚠️ Audits/legacy code |
| **Pyflakes** | Linter | ⚡ Fast execution<br/>🎯 Detects undefined names/unused vars | ❌ No stylistic checks (PEP8) | 6/10 | ⚠️ Component use only |
| **Semgrep** | SAST/Linter | ⚡ Fast rule-based checks<br/>🔐 Security policy enforcement | 🔒 More SAST-oriented<br/>⚠️ May overlap with other tools | 8/10 | ✅ Security policies |

### 💡 Why Choose Ruff?

!!! tip "Ruff: The Pragmatic Default"
    Ruff's speed and wide coverage make it ideal for:

    - ✅ Pre-commit hooks with instant feedback
    - ✅ Large codebases requiring fast linting
    - ✅ Teams wanting unified tooling

    **Use Pylint only when you need deep, opinionated code audits.**

---

## 🎨 Formatters — Speed, Configurability & Adoption

Ensuring consistent code style across your project.

| Tool | Category | Pros | Cons | Score | Status |
|------|----------|------|------|------:|--------|
| **Black** | Formatter | 🎯 Opinionated & stable<br/>🌍 Widely adopted<br/>📉 Small, consistent diffs | ⚙️ Limited customization | 9/10 | ✅ **Recommended** |
| **Ruff Format** | Formatter | ⚡ Very fast & lightweight<br/>🔗 Integrates with Ruff toolchain | 🚧 Still evolving feature set | 9/10 | ✅ Great alternative |
| **autopep8** | Formatter | 📏 PEP8-focused fixes<br/>⚙️ Configurable | 🤷 Less opinionated<br/>📈 Larger diffs | 6/10 | ⚠️ Legacy use |
| **YAPF** | Formatter | ⚙️ Highly configurable | 📉 Less adoption<br/>⚠️ Results vary across versions | 6/10 | ⚠️ Not recommended |
| **isort** | Import Sorter | 🏆 Industry standard<br/>🤝 Black-compatible | 📦 Imports only (not full formatter) | 8/10 | ✅ **Use alongside** |

### 🎯 Recommended Combination

!!! success "Winning Formula"
    **Black** (or **Ruff Format**) + **isort**

    - Black/Ruff Format provides stable, opinionated formatting
    - isort manages import organization
    - Ruff can consolidate both if you want a single fast binary

=== "Option A: Classic"
    ```yaml
    # .pre-commit-config.yaml
    - repo: https://github.com/psf/black
      hooks:
        - id: black
    - repo: https://github.com/pycqa/isort
      hooks:
        - id: isort
    ```

=== "Option B: Unified"
    ```yaml
    # .pre-commit-config.yaml
    - repo: https://github.com/astral-sh/ruff-pre-commit
      hooks:
        - id: ruff
        - id: ruff-format
    - repo: https://github.com/pycqa/isort
      hooks:
        - id: isort
    ```

---

## 🔎 Type Checkers — Precision, Speed & IDE Integration

Static type checking for Python codebases.

| Tool | Category | Pros | Cons | Score | Status |
|------|----------|------|------|------:|--------|
| **Mypy** | Static Type Checker | 📚 Reference implementation<br/>🔒 Strict checks available<br/>🔌 Plugin support (SQLModel, FastAPI) | 🐌 Can be slower<br/>📖 Configuration learning curve | 9/10 | ✅ **CI-focused** |
| **Pyright** | Static Type Checker | ⚡ Very fast<br/>💻 Excellent editor integration (Pylance)<br/>🎯 Great developer experience | ⚠️ Less strict by default vs Mypy | 8/10 | ✅ **IDE-focused** |
| **Pyre** | Static Type Checker | ⚡ Fast & scalable<br/>🔬 Advanced analysis (Pysa) | 🏢 Less common outside Meta<br/>⚙️ Heavier setup | 7/10 | ⚠️ Large codebases |
| **Pytype** | Static Type Checker | 🔄 Good inference for migrations | 📉 Less mainstream adoption | 7/10 | ⚠️ Alternative |
| **Typeguard** | Runtime Checker | 🧪 Runtime validation in tests | ⚠️ Runtime overhead<br/>❌ Not for production | 7/10 | ⚠️ Test-only |

### 🎯 Recommended Strategy

!!! tip "Best of Both Worlds"
    **Mypy in CI** (strict mode) + **Pyright for IDE** (developer feedback)

    This combination provides:

    - ✅ Strict enforcement in CI pipeline
    - ✅ Fast, real-time feedback during development
    - ✅ Best tooling integration for both contexts

**Configuration Example:**

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

---

## 🧪 Testing Frameworks — Ease of Use, Plugins & Assertions

Building robust test suites for your application.

| Tool | Category | Pros | Cons | Score | Status |
|------|----------|------|------|------:|--------|
| **pytest** | Framework | ✨ Simple syntax with assert introspection<br/>🔌 Modular fixtures<br/>🎯 Vast plugin ecosystem<br/>📊 Parametrized tests | 📚 Learning curve for advanced fixtures | 10/10 | ✅ **Recommended** |
| **unittest** | Framework (stdlib) | 📦 Built into Python<br/>🔒 Stable & mature<br/>🤝 `unittest.mock` integration | 📝 Verbose syntax (assertEqual, etc.)<br/>😕 Less ergonomic | 7/10 | ⚠️ Compatibility use |
| **nose2** | Framework | 🔌 Easy plugins<br/>🔍 Test discovery | 📉 Less active development<br/>👥 Smaller community | 6/10 | ⚠️ Not recommended |
| **Hypothesis** | Property Testing | 🎲 Generates random/priority tests<br/>🔍 Finds edge cases<br/>🧮 Great for algorithms | 🤔 Different testing approach<br/>📚 Requires different test design | 9/10 | ✅ **Complementary** |
| **Robot Framework** | Acceptance/RPA | 🤖 Robot syntax<br/>🌐 Multi-language support<br/>🎯 High-level tests & RPA | ⚠️ Overkill for simple API projects<br/>🎯 Acceptance test focus | 6/10 | ⚠️ Specific use case |

### 🎯 Recommended Testing Stack

!!! success "Winning Combination"
    **pytest** as the foundation + **Hypothesis** for property testing

    **Why pytest?**

    - ✅ Industry standard with massive adoption
    - ✅ Rich plugin ecosystem (coverage, markers, fixtures)
    - ✅ Excellent ergonomics and readability

    **When to add Hypothesis?**

    - ✅ Parsers and data transformation logic
    - ✅ Algorithm implementations
    - ✅ Complex business rules
    - ✅ Edge case discovery

**Example Usage:**

=== "pytest Basic"
    ```python
    # test_api.py
    def test_user_creation(client):
        response = client.post("/users", json={"name": "Alice"})
        assert response.status_code == 201
        assert response.json()["name"] == "Alice"
    ```

=== "pytest + Fixtures"
    ```python
    # conftest.py
    @pytest.fixture
    def client():
        return TestClient(app)

    # test_api.py
    def test_user_creation(client):
        response = client.post("/users", json={"name": "Alice"})
        assert response.status_code == 201
    ```

=== "pytest + Hypothesis"
    ```python
    from hypothesis import given
    from hypothesis import strategies as st

    @given(st.text(min_size=1, max_size=100))
    def test_username_validation(username):
        result = validate_username(username)
        assert isinstance(result, bool)
    ```

---

## 🔐 Security Scanners — Vulnerability Detection & False Positives

Multi-layered security scanning for applications and dependencies.

| Tool | Category | Pros | Cons | Score | Status |
|------|----------|------|------|------:|--------|
| **Bandit** | Static Code Security | 🔍 AST analysis<br/>⚠️ Detects vulnerable patterns<br/>🐍 Python-specific (shell injection, unsafe eval) | ⚠️ False positives possible<br/>⚙️ Rule tuning required | 8/10 | ✅ **Recommended** |
| **Safety** | SCA (Dependencies) | 🔍 Known vulnerability detection<br/>📊 Vulnerability database<br/>✨ Simple to use | 💰 Advanced features paid (PyUp)<br/>📦 Limited to dependencies | 8/10 | ✅ **Recommended** |
| **Trivy** | Container/Image | 🐳 Scans images & OS packages<br/>⚡ Fast & comprehensive<br/>🆓 Open source (Aqua) | 🏗️ Requires built image artifact | 9/10 | ✅ **Recommended** |
| **Semgrep** | SAST (Policy) | 🎯 Flexible rule engine<br/>📝 Code-like rules<br/>🔄 Reusable patterns<br/>📉 Low false positives | 💰 Advanced features paid (Pro)<br/>⚙️ Requires tuning | 8/10 | ✅ **Recommended** |
| **Snyk** | SCA + Platform | 📊 SCA, SAST, container, IaC<br/>🔧 Remediation guidance<br/>🔗 GitHub/GitLab integration<br/>📈 UI reporting | 💰 Paid (free tier limited)<br/>💼 Enterprise features costly | 9/10 | ✅ Enterprise/org |

### 🛡️ Defense in Depth Strategy

!!! warning "Security Requires Multiple Layers"
    No single tool catches everything. Build a comprehensive security strategy:

=== "Code Analysis"
    **Static Application Security Testing (SAST)**

    - ✅ **Bandit** - Python-specific security issues
    - ✅ **Semgrep** - Custom security policies

    ```yaml
    # .github/workflows/security.yml
    - name: Run Bandit
      run: bandit -r src/ -f json -o bandit-report.json

    - name: Run Semgrep
      run: semgrep --config auto src/
    ```

=== "Dependency Analysis"
    **Software Composition Analysis (SCA)**

    - ✅ **Safety** - Quick checks (open source)
    - ✅ **Snyk** - Enterprise reporting & remediation

    ```yaml
    - name: Check dependencies
      run: safety check --json

    - name: Snyk test
      run: snyk test --severity-threshold=high
    ```

=== "Container Security"
    **Image & Runtime Scanning**

    - ✅ **Trivy** - Container image vulnerabilities

    ```yaml
    - name: Build image
      run: docker build -t myapp:latest .

    - name: Scan with Trivy
      run: trivy image myapp:latest
    ```

### 🎯 Recommended Security Stack

!!! success "Comprehensive Coverage"
    **Bandit + Semgrep** (SAST) + **Safety/Snyk** (SCA) + **Trivy** (Containers)

    This combination covers:

    - 🔍 Static code vulnerabilities
    - 📦 Dependency vulnerabilities
    - 🐳 Container security
    - 🔐 Security policy enforcement

---

## ✅ Pragmatic Stack Recommendation

### 🏠 Local Development & Pre-commit

!!! tip "Fast Feedback Loop"
    Keep local hooks lightweight for developer productivity:

```yaml
# .pre-commit-config.yaml
repos:
  # Formatting & Linting
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  # Import sorting
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--atomic]

  # Type checking (optional - can be slow)
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]

  # Quick security checks
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
```

**Local Tools:**

- ⚡ Ruff (lint + format)
- 📦 isort (imports)
- 🔎 Mypy/Pyright (type checking)
- 🧪 pytest + Hypothesis (testing)
- 🔐 Bandit + Semgrep (quick security)
- 📊 Safety (dependency scan)

### ☁️ CI Pipeline Jobs

!!! info "Comprehensive CI Checks"
    Run parallel jobs for speed:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run isort --check-only .

  type-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync
      - run: uv run mypy src/

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync
      - run: uv run pytest --cov --cov-report=xml
      - uses: codecov/codecov-action@v3

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
      - run: uv sync
      - run: uv run bandit -r src/
      - run: uv run semgrep --config auto src/
      - run: uv run safety check

  security-image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t app:${{ github.sha }} .
      - name: Scan with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
```

**CI Jobs:**

1. 🔍 **Lint** - Ruff check + format check + isort check
2. 🔎 **Type Check** - Mypy (strict mode) or Pyright
3. 🧪 **Tests** - pytest with coverage
4. 🔐 **Security** - Bandit + Semgrep + Safety
5. 🐳 **Image Security** - Trivy scan on Docker images

### 🚀 CD/Release Pipeline

!!! success "Production-Ready Releases"
    Additional checks before deployment:

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  security-final:
    runs-on: ubuntu-latest
    steps:
      - name: Final Snyk scan
        run: snyk test --severity-threshold=critical

      - name: Final Trivy scan
        run: trivy image app:${{ github.ref_name }}

  publish:
    needs: security-final
    runs-on: ubuntu-latest
    steps:
      - run: uv build
      - run: uv publish
```

---

## 💡 Detailed Recommendations & Adoption Tips

### 🚀 Start Small & Iterate

!!! tip "Progressive Adoption Strategy"

    **Phase 1: Foundation (Week 1)**

    1. ✅ Set up Ruff + Black + isort in pre-commit → fast corrections
    2. ✅ Add basic pytest tests
    3. ✅ Configure pyproject.toml

    **Phase 2: Quality Gates (Week 2-3)**

    1. ✅ Add Mypy to CI with `--ignore-missing-imports`
    2. ✅ Gradually increase strictness
    3. ✅ Add coverage requirements

    **Phase 3: Security (Week 3-4)**

    1. ✅ Integrate Bandit + Safety
    2. ✅ Add Semgrep rules
    3. ✅ Set up Trivy for containers

### 🔧 Tool Complementarity

!!! success "Use Multiple Tools in Harmony"
    Each tool catches different issue classes:

    - 🔍 **Ruff** - Quick fixes & common issues
    - 🔎 **Mypy** - Type safety & contracts
    - 🔐 **Semgrep** - Security policies & patterns
    - 📦 **Safety** - Dependency vulnerabilities
    - 🐳 **Trivy** - Container security

    **Don't replace, complement!**

### ⚡ CI Performance Optimization

!!! tip "Speed Up Your Pipeline"

    **Caching Strategy:**

    ```yaml
    - uses: astral-sh/setup-uv@v6
      with:
        enable-cache: true

    - uses: actions/cache@v4
      with:
        path: |
          ~/.cache/pip
          ~/.cache/pre-commit
        key: ${{ runner.os }}-cache-${{ hashFiles('**/uv.lock') }}
    ```

    **Parallelization:**

    - ✅ Run lint, type-check, test, and security jobs in parallel
    - ✅ Use matrix strategies for multi-version testing
    - ✅ Cache UV dependencies and pre-commit environments

### 🔐 Security & False Positives

!!! warning "Managing Security Tool Noise"

    **Configuration Best Practices:**

    ```toml
    # pyproject.toml
    [tool.bandit]
    exclude_dirs = ["tests", "migrations"]
    skips = ["B101"]  # Skip assert warnings in tests

    [tool.semgrep]
    paths.exclude = [
        "tests/",
        "*/migrations/",
    ]
    ```

    **Progressive Refinement:**

    1. ✅ Start with default rules
    2. ✅ Create baseline of existing issues
    3. ✅ Add suppressions for false positives
    4. ✅ Document why suppressions exist
    5. ✅ Use Snyk/Safety Pro for prioritized remediation

### 👨‍💻 Developer Workflow Optimization

!!! tip "Balance Speed and Quality"

    **Local (Fast):**

    - ⚡ Ruff `--fix` (instant)
    - ⚡ isort `--atomic` (fast)
    - ⚡ Quick formatting checks

    **CI (Comprehensive):**

    - 🔍 Full Bandit scan
    - 🐳 Trivy image scan
    - 🔎 Mypy strict mode
    - 📊 Full test suite with coverage

---

## 🔗 Official Resources & Documentation

### 🔍 Linting & Formatting

- **Ruff**: [docs.astral.sh/ruff](https://docs.astral.sh/ruff/) | [GitHub](https://github.com/astral-sh/ruff)
- **Black**: [black.readthedocs.io](https://black.readthedocs.io/) | [GitHub](https://github.com/psf/black)
- **Flake8**: [flake8.pycqa.org](https://flake8.pycqa.org/)
- **Pylint**: [pylint.pycqa.org](https://pylint.pycqa.org/)
- **isort**: [pycqa.github.io/isort](https://pycqa.github.io/isort/)

### 🔎 Type Checking

- **Mypy**: [mypy-lang.org](https://mypy-lang.org/)
- **Pyright**: [GitHub](https://github.com/microsoft/pyright) | **Pylance**: VSCode extension
- **Pyre**: [pyre-check.org](https://pyre-check.org/)
- **Pytype**: [google.github.io/pytype](https://google.github.io/pytype/)

### 🧪 Testing

- **pytest**: [pytest.org](https://pytest.org/)
- **Hypothesis**: [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/)
- **unittest**: [Python docs](https://docs.python.org/3/library/unittest.html)

### 🔐 Security

- **Bandit**: [bandit.readthedocs.io](https://bandit.readthedocs.io/)
- **Safety**: [safetycli.com](https://safetycli.com/) (PyUp)
- **Snyk**: [snyk.io](https://snyk.io/)
- **Trivy**: [trivy.dev](https://trivy.dev/)
- **Semgrep**: [semgrep.dev](https://semgrep.dev/)

---

## 📝 Conclusion

!!! success "Modern CI/CD Pipeline for FastAPI + UV"

    **Recommended Stack:**

    === "Code Quality"
        - 🔍 **Ruff** (lint + format) or **Black**
        - 📦 **isort** (import sorting)
        - 🔎 **Mypy** (CI) + **Pyright** (IDE)

    === "Testing"
        - 🧪 **pytest** (foundation)
        - 🎲 **Hypothesis** (property testing)
        - 📊 Coverage reporting

    === "Security"
        - 🔐 **Bandit + Semgrep** (SAST)
        - 📦 **Safety/Snyk** (SCA)
        - 🐳 **Trivy** (containers)

    This combination provides:

    ✅ **Fast local development** with instant feedback
    ✅ **Comprehensive CI checks** catching issues early
    ✅ **Multi-layered security** protecting production
    ✅ **Developer-friendly** workflow with minimal friction

**Ready to implement?** Start with Phase 1 and iterate! 🚀
