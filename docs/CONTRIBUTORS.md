# Guide du contributeur interne

Ce fichier est destiné à un unique contributeur interne pour configurer son environnement local et respecter les règles de qualité du dépôt.

---

## Prérequis

- Python 3.13 ou supérieur
- uv (outil de gestion de dépendances du projet) — installer si nécessaire :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- (optionnel) Docker pour tests Postgres si vous voulez une intégration plus réaliste

---

## Installer les dépendances (initial)

1. Synchronisez les dépendances du projet dans l'environnement uv :

```bash
uv sync
```

2. (Optionnel) Si vous utilisez un environnement virtualenv local, activez-le :

```bash
source .venv/bin/activate
```

---

## Pré-commit

Le projet utilise `pre-commit` pour garantir que les étapes qualité suivantes passent avant chaque commit :

- Ruff (lint & format)
- Mypy (vérification de types)
- Bandit (analyse de sécurité)
- Detect Secrets (recherche de secrets)
- pytest (tests unitaires & d'intégration)

### Installation et activation

```bash
# Installer pre-commit si vous ne l'avez pas
uv run pip install pre-commit

# Installer les hooks localement
pre-commit install
```

### Exécuter les hooks manuellement

```bash
# Exécuter tous les hooks sur tous les fichiers (pratique pour validation globale)
pre-commit run --all-files

# Exécuter un hook précis, par ex. ruff (hook fourni par pre-commit)
pre-commit run ruff --all-files
```

> Remarque : le hook `pytest` est configuré pour utiliser `uv run pytest -q`, ce qui garantit qu'il s'exécute dans l'environnement `uv` et trouve `sqlmodel`, `fastapi`, et autres dépendances dev.

### Si un hook modifie des fichiers

Si `pre-commit` auto-corrige des fichiers (ruff-format, trailing whitespace, etc.), refaites `git add` puis `git commit`.

---

## Lancer les vérifications manuellement (commandes utiles)

```bash
# Linter (Ruff)
uv run ruff check app tests

# Format check
uv run ruff format --check app tests

# Type checking
uv run mypy app

# Security scan
uv run bandit -r app/

# Tests unitaires & intégration
uv run pytest -q

# Detect secrets baseline (générer la baseline une fois)
uv run detect-secrets scan > .secrets.baseline
```

---

## Gestion du fichier de baseline `detect-secrets`

- Nous avons une baseline `.secrets.baseline` dans la racine du repo pour éviter de bloquer les détecteurs sur des faux positifs historiques.
- Si vous ajoutez une vraie clef, detect-secrets la listera pour correction. Pour ajouter un faux positif à la baseline, utilisez `detect-secrets` pour gérer la baseline (mais soyez prudent).

---

## Erreurs fréquentes et dépannages

- `ModuleNotFoundError` pour `sqlmodel` ou autres dépendances dans pre-commit: assurez-vous d'avoir exécuté `uv sync` et que `uv` est installé. Nous appelons `uv run pytest -q` dans le hook afin d'éviter ce souci.

- `mypy` signale `import-not-found` : Si cela arrive dans pre-commit, assurez-vous que mypy a `additional_dependencies` (déjà configuré pour le hook); sinon synchronisez `uv`.

- Ruff/Wrong formatting: exécutez `uv run ruff check --fix .` puis re-commit.

---

## Mise à jour de versions de hooks (mise à jour volontaire seulement)

Nous bloquons (pin) les versions des hooks et des outils pour assurer la stabilité. Si vous devez mettre à jour des hooks (ex : `mypy`, `ruff`), suivez ce workflow :

1. Créez une branche `chore/update-tools`.
2. Mettez à jour la version du hook dans `.pre-commit-config.yaml` (ou le `rev`).
3. Exécutez localement :

```bash
pre-commit autoupdate --repo <url-du-repo>  # facultatif
pre-commit clean
pre-commit run --all-files
uv run pytest -q
```

4. Si tout passe localement (pré-commit et tests), ouvrez une PR.
5. Laissez la CI exécuter les mêmes checks avant de merger sur `develop`.

**Important** : Ne faites pas d'autoupdate sans exécuter toutes les vérifications locales et la CI, car une mise à jour de hook peut introduire des exigences de dépendances non compatibles avec les versions de notre projet.

---

## CI & Protection de branche

- Le workflow CI s'exécute automatiquement sur :
  - `push` vers `develop` et `main`.
  - `pull_request` vers `develop`.

- La CI effectue : linting (ruff), vérification de formatage, type-check (mypy), sécurité (bandit), `detect-secrets`, `pytest`.

- Les PRs vers `develop` doivent satisfaire toutes ces étapes pour être fusionnées. Une règle de protection est en place (ou peut être mise en place) pour réclamer que la CI passe avant la fusion.

---

## Conduite pour les commits (workflow simplifié)

1. Exécutez rapidement les tests et le lint avant de commencer :

```bash
uv run ruff check app tests
uv run mypy app
uv run pytest -q
```

2. Une fois le travail terminé :

```bash
git add .
pre-commit run --files <changed files> || pre-commit run --all-files
git commit -m "feat: mon changement"
```

3. Push et ouvrir une PR vers `develop` : la CI exécutera ensuite toutes les vérifications.

---

## Notes supplémentaires et contact interne

- Ce document est interne et destiné à une seule personne (vous); adaptez les versions des outils en coordination si vous mettez à jour.
- Si vous avez besoin d'aide sur l'intégration du pipeline CI ou la gestion des versions d'outils, me notifier en ouvrant une PR et en ajoutant un commentaire sur les changements envisagés.

---

Merci — suivez ce guide pour garder la qualité et la sécurité du repo intactes.
