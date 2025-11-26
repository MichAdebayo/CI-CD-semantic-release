# Veille CI/CD

> Ci‑dessous, une synthèse de veille sur l'approche CI/CD.

---

## Table des matières
- 1) Qu'est-ce que la CI (Continuous Integration) ?
	- 1.1 Quels problèmes résout-elle ?
	- 1.2 Quels sont les principes clés ?
	- 1.3 Donnez 3 exemples d'outils de CI
- 2) Qu'est-ce que le CD (Continuous Deployment/Delivery) ?
	- 2.1 Différence entre Continuous Delivery et Continuous Deployment ?
	- 2.2 Quels sont les risques et bénéfices ?
- 3) Pourquoi CI/CD est important ?
 	- 3.1 Impact sur la qualité du code
 	- 3.2 Impact sur la vitesse de développement
 	- 3.3 Impact sur la collaboration en équipe
- 4) Qu'est-ce que uv ?
  	- 4.1 Qu'est-ce que uv ?
  	- 4.2 Comment uv fonctionne avec pyproject.toml ?
  	- 4.3 Comment utiliser uv dans GitHub Actions ?

---

## 1) Qu'est-ce que la CI (Continuous Integration) ? 🔁
La CI, ou intégration continue, est un processus d'automatisation permettant d'intégrer fréquemment les modifications de code dans un référentiel partagé (tronc commun). À chaque intégration, des étapes automatiques comme la compilation et l'exécution de tests (unitaires, d'intégration, etc.) sont lancées afin de garantir que les nouvelles modifications n'endommagent pas l'application. L'objectif est d'éviter les situations de « merge day » difficiles à gérer et de détecter tôt les conflits et régressions.


### 1.1) Quels problèmes résout-elle ?

- Réduction des conflits lors de la fusion de nombreuses branches (évite le « merge day").
- Diminution du temps et de l'effort nécessaires pour intégrer des modifications (moins de procédures manuelles).
- Détection précoce des bogues et régressions grâce à l'exécution automatique de tests.
- Atténuation des problèmes liés aux environnements de développement qui diffèrent d'un développeur à l'autre.


### 1.2) Quels sont les principes clés ?

- Intégrations fréquentes dans un référentiel partagé (tronc commun).
- Automatisation des compilations et des différentes couches de tests (unitaires, d'intégration, etc.).
- Vérifications automatiques à chaque étape pour s'assurer que l'application reste fonctionnelle.
- Retour rapide aux développeurs pour corriger rapidement les conflits ou régressions.


### 1.3) Donnez 3 exemples d'outils de CI

- **Jenkins** — outil de gestion populaire pouvant servir aussi bien de serveur CI que de hub CD complet.
- **Tekton / OpenShift Pipelines** — framework CI/CD cloud-native pour plateformes Kubernetes (notamment Red Hat OpenShift).
- **GoCD** — serveur CI/CD axé sur la modélisation et la visualisation des pipelines.


---

## 2) Qu'est-ce que le CD (Continuous Deployment/Delivery) ? 📦

CD regroupe la distribution continue et le déploiement continu :

- La **distribution continue** (Continuous Delivery) automatise la publication du code validé (après CI et tests) dans un référentiel ou un artefact prêt pour la production, rendant le code « deployable » à tout moment. L'étape de mise en production peut rester manuelle et confiée aux équipes d'exploitation.
- Le **déploiement continu** (Continuous Deployment) pousse plus loin l'automatisation : les modifications qui réussissent tous les tests sont automatiquement publiées en production, sans intervention manuelle.


### 2.1) Différence entre Continuous Delivery et Continuous Deployment ?

- **Continuous Delivery (distribution continue)** : Le code validé est automatiquement préparé et publié dans des artefacts ou référentiels prêts pour la production, mais le déploiement en production peut rester sous contrôle manuel (opérations).
- **Continuous Deployment (déploiement continu)** : La mise à jour est automatiquement déployée en production dès qu'elle a réussi les tests et les validations automatisées, sans étape manuelle.


### 2.2) Quels sont les risques et bénéfices ?

**Bénéfices :**

- Réduction des bogues et des défaillances de code.
- Réduction des temps d'arrêt et accélération des publications.
- Intégration plus rapide des retours utilisateurs et meilleure satisfaction.
- Réduction de la complexité et amélioration de l'efficacité des workflows.

**Risques :**

- Automatisation mal conçue peut entraîner des déploiements de code incorrect ou vulnérable si les tests sont insuffisants.
- Exposition possible de données sensibles si les pipelines ne sont pas sécurisés.
- Utilisation de composants tiers non sécurisés (vulnérabilités) si la vérification n'est pas rigoureuse.
- Accès non autorisé aux référentiels de code ou aux outils de développement si les contrôles de sécurité sont faibles.
- Le déploiement continu nécessite un investissement initial important pour définir et automatiser des tests fiables et des contrôles (shift-left / shift-right).


---

## 3) Pourquoi CI/CD est important ? 💡

### 3.1 Impact sur la qualité du code

- Les tests automatisés et les vérifications fréquentes permettent de détecter rapidement les erreurs et d'assurer que chaque modification répond aux critères de qualité, réduisant ainsi les régressions et améliorant la fiabilité du code.

### 3.2 Impact sur la vitesse de développement

- L'automatisation des étapes de build, test et publication réduit considérablement le délai entre l'écriture du code et sa mise à disposition, accélérant le cycle de sortie des fonctionnalités et l'intégration des retours utilisateurs.

### 3.3 Impact sur la collaboration en équipe

 - CI/CD favorise une culture DevOps et une meilleure collaboration entre les équipes de développement et d'exploitation, en réduisant la friction liée aux opérations manuelles et en encourageant une responsabilité partagée (incluant la sécurité, DevSecOps). Il facilite également la standardisation des environnements et la reproductibilité des déploiements.

---

## 4) Qu'est-ce que uv ? 🧰

uv est un gestionnaire de projets et de dépendances Python moderne, écrit en Rust. Il vise à remplacer plusieurs outils classiques (`pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, ...), en offrant une interface cohérente pour la gestion des environnements, des versions de Python, des outils et des dépendances. uv fournit également une interface `uv pip` compatible avec `pip` pour des gains de performance immédiats.

En bref, uv :
- Installe et gère des versions de Python (commande `uv python install`).
- Gère des environnements de projet (en créant `.venv` et en utilisant `uv sync`/`uv run`).
- Gère les dépendances et le lockfile (`uv.lock`) avec résolution multiplateforme.
- Fournit des fonctionnalités pour scripts, outils et workspaces (similaire à Cargo).

### 4.1) En quoi est-ce différent de `pip`/`poetry`/`pipenv` ?

- Remplace plusieurs outils par une seule interface : uv combine la gestion des dépendances, des environnements, des versions Python et des outils (pip/pipx/pyenv/poetry).
- Performances : uv est conçu pour être beaucoup plus rapide que `pip` (benchmarks cités sur la documentation), grâce à un cache efficace et des résolutions optimisées.
- Gestion centralisée du projet : uv utilise un `uv.lock` universel et fournit des mécanismes comme `dependency-groups`, `tool.uv.sources` et `workspaces` pour gérer les dépendances multi-plateformes et multi-projets.
- Compatibilité : uv propose une interface compatible `pip` (`uv pip`), facilitant la migration sans changer les flux de travail existants.

### 4.2) Quels sont les avantages ?

- **Vitesse** : 10–100x plus rapide que `pip` dans certains scénarios (selon la doc).
- **Unification d'outils** : rassembler plusieurs responsabilités (environnements, outils, installations de Python) au sein d'un seul outil réduit la complexité.
- **Reproductibilité** : `uv.lock` assure des installations cohérentes sur toutes les plateformes.
- **Cache global** : réduction de l'espace disque et des téléchargements grâce au cache partagé et au prunning (`uv cache prune --ci`).
- **Workspaces & scripts** : bon support pour monorepos et scripts avec metadata inline.
- **Interopérabilité** : type `uv pip` et export vers `pylock.toml` pour compatibilité avec d'autres outils.

---

## 5) Comment uv fonctionne avec `pyproject.toml` ? 🔧

### 5.1) Structure du fichier

uv s'appuie sur le `pyproject.toml` pour identifier la racine de projet et stocker la configuration. Les champs utilisés fréquemment :
- `[project]` : nom, version, `requires-python`, `dependencies` (PEP 621) et `optional-dependencies`.
- `[build-system]` : `requires` et `build-backend` (pour utiliser `uv_build`).
- `[tool.uv]` : configuration spécifique uv (par ex. `default-groups`, `dev-dependencies` legacy, `workspace` settings).
- `uv.lock` : lockfile créé automatiquement à côté de `pyproject.toml` (doit être versionné).

### 5.2) Gestion des dépendances (séparées par sections)

- `project.dependencies` : dépendances publiées pour la distribution (utilisé pour le packaging/PyPI).
- `project.optional-dependencies` : extras (par ex. `plot`, `excel`).
- `[dependency-groups]` : groupes locaux de dépendances pour le développement (`dev`, `lint`, `test`), normalisés par PEP 735.
- `[tool.uv.sources]` : sources alternatives (index, git, path, url, workspace) pour le développement et la résolution locale.
- `tool.uv.dev-dependencies` (legacy) : ancien emplacement pour les dépendances de développement, combiné avec `dev` group.

Ces champs permettent d'indiquer des dépendances par plateforme (via les markers PEP 508), des sources alternatives (Git, URL, index personnalisé), et des dépendances accessibles uniquement en dev via `dependency-groups`.

### 5.3) Build backend

Pour utiliser `uv` comme build backend, déclarez `uv_build` dans la section `[build-system]` du `pyproject.toml` :

```toml
[build-system]
requires = ["uv_build>=0.9.11,<0.10.0"]
build-backend = "uv_build"
```

Le backend `uv_build` a des choix par défaut (ex: `src/` pour modules) mais est configurable via `tool.uv.build-backend` (module-name, module-root, inclusion/exclusion de fichiers, `data` directories). Les fichiers inclus et exclus pour la source/wheel sont gérés via les options `source-include`, `source-exclude`, `wheel-exclude`, et suivent une syntaxe glob réduite (PEP 639).

---

## 6) Comment utiliser uv dans GitHub Actions ? ⚙️

### 6.1) Installation

La méthode recommandée est d'utiliser l'action officielle `astral-sh/setup-uv` :

```yaml
- uses: astral-sh/setup-uv@v6
	with:
		version: "0.9.11" # valeur exemplaire, pinner est recommandé
		enable-cache: true  # optional
```

On peut aussi installer et gérer la version de Python via `uv python install` ou utiliser `actions/setup-python` en parallèle.

### 6.2) Cache des dépendances

Deux approches :
- Configurer `enable-cache: true` dans `setup-uv`, qui gère le cache automatiquement.
- Gérer manuellement le cache avec `actions/cache`, en définissant `UV_CACHE_DIR` et un `key` basé sur `uv.lock` :

```yaml
env:
	UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv

- name: Restore uv cache
	uses: actions/cache@v4
	with:
		path: ${{ env.UV_CACHE_DIR }}
		key: uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
```

N'oubliez pas d'optimiser la taille du cache : `uv cache prune --ci`.

### 6.3) Exécution de commandes

Exemples de pipeline typiques :

- Installer uv et Python
```yaml
- uses: astral-sh/setup-uv@v6
- run: uv python install 3.13
```

- Installer le projet et les dépendances (dev inclus) :
```yaml
- run: uv sync --locked --all-extras --dev
```

- Lancer les tests :
```yaml
- run: uv run pytest tests
```

### 6.4) Points additionnels
- Pour `uv pip` (interface `pip`), si vous préférez installer dans l'environnement système, utilisez `UV_SYSTEM_PYTHON=1` ou `--system` flag.
- Pour les dépôts privés, configurez un PAT et authentifiez avec `gh auth login` et `gh auth setup-git` afin que `uv add` ou `uv sync` puisse récupérer des sources privées.
- Pour publier sur PyPI, on peut utiliser `uv build` puis `uv publish` dans une action GitHub après un tag `v*`.

---

## 7) Qu'est-ce que le versionnage sémantique (SemVer) ? 🔢

SemVer est une convention permettant de donner un sens clair aux numéros de version, permettant aux utilisateurs et outils de comprendre l'impact d'une release.

### Format
- SemVer suit la forme MAJOR.MINOR.PATCH (ex. `1.2.3`).
- On peut ajouter des pré-versions (ex. `1.2.3-alpha.1`) et des métadonnées de build (ex. `1.2.3+build.1`).

### Quand incrémenter chaque niveau ?
- MAJOR : modifications incompatibles — rupture de l'API/contrat avec les utilisateurs (ex. `1.0.0` → `2.0.0`).
- MINOR : ajout de nouvelles fonctionnalités compatibles rétro-activement (ex. `1.2.3` → `1.3.0`).
- PATCH : corrections de bugs compatibles rétro-activement (ex. `1.2.3` → `1.2.4`).

### Exemples & remarques
- Si un commit introduit un changement casse-tête API (BREAKING), bump MAJOR.
- Les versions pré-release aident à tester avant la publication stable.
- Garder `project.version` à jour (ou utilisez un outil qui l'update automatiquement comme PSR).

---

## 8) Qu'est-ce que Conventional Commits ? ✍️

Conventional Commits est une spécification qui standardise le format des messages de commit afin de rendre l'historique lisible et exploitable par des outils (génération automatique de changelog, détermination de bump SemVer...).

### Format des messages

```
<type>(<scope optionnel>)?: <description>

[corps optionnel]

[pied optionnel]
```

Les éléments principaux : `type` (ex. `feat`, `fix`), `scope` (quel composant affecté), `description`, `body` (motivation/détails), `footer` (références, `BREAKING CHANGE`).

### Types courants
- `feat` : nouvelle fonctionnalité (impacterait un bump MINOR).
- `fix` : correction de bogue (PATCH).
- `docs`, `style`, `chore`, `ci`, `test`, `refactor`, `perf`, `build` : métadonnées / organisation / qualité.

### Indiquer une rupture de compatibilité
- Utilisez `BREAKING CHANGE: <description>` dans le pied du commit, OU ajoutez `!` juste avant le `:` dans le titre du commit (ex. `feat(api)!: ...`). Cela déclenche un bump MAJOR.

### Impact sur le versionnage
- Les outils (ex. python-semantic-release) traduisent automatiquement les `types` en types de bump SemVer :
	- `fix` → PATCH
	- `feat` → MINOR
	- `BREAKING CHANGE` / `!` → MAJOR
- Les autres types n'affectent pas la version par défaut sauf s'ils contiennent un `BREAKING CHANGE`.

### Exemples
```text
feat(api): add filters to product listing

fix(auth): correct token handling on refresh

perf(db): reduce query time for aggregate requests

feat!: change auth token format

BREAKING CHANGE: token structure changed from `x.y` to `a.b.c`.
```

---

## 9) Comment python-semantic-release fonctionne ? 🐍🔧

Python Semantic Release (PSR) automatise la détermination de la prochaine version à partir des messages de commit (SemVer + Conventional Commits), puis met à jour le `version` du projet, génère ou met à jour un `CHANGELOG`, tagge le dépôt, et peut publier des artefacts et créer une Release sur la plateforme VCS (ex : GitHub).

### Configuration dans `pyproject.toml`
- La configuration se place dans la table `[tool.semantic_release]` :

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
commit_parser = "conventional"
vcs_release = true
[tool.semantic_release.commit_parser_options]
minor_tags = ["feat"]
patch_tags = ["fix","perf"]
parse_squash_commits = true
ignore_merge_commits = true
build_command = "python -m build --sdist --wheel ."
```

- `version_toml` : emplacement à mettre à jour lors d'un bump (ex. `pyproject.toml:project.version`).
- `commit_parser` : parser de messages (`conventional` par défaut pour Conventional Commits).
- `commit_parser_options` : permet d'ajuster les tags considérés pour `minor`/`patch` et gérer `squash`/`merge`.
- `build_command` : commande pour construire les artefacts avant publication.

### Génération du CHANGELOG
- PSR lit les messages et génère des notes de version (CHANGELOG) via des templates configurables.
- On peut définir `changelog_file`, `output_format` (`md`/`rst`) et `exclude_commit_patterns` pour filtrer les commits à ignorer (ex: `chore`, `ci`, `test`).

Example :
```toml
[tool.semantic_release.changelog]
changelog_file = "CHANGELOG.md"
output_format = "md"
exclude_commit_patterns = [
	"^chore(?:\\([^)]*?\\))?: .+",
	"^ci(?:\\([^)]*?\\))?: .+",
]
```

### Création des releases GitHub (ou autre VCS)
- PSR peut créer des tags et des releases sur la plateforme de VCS en utilisant un token stocké en variable d'environnement (ex. `GH_TOKEN` pour GitHub, `GITLAB_TOKEN` pour GitLab).
- Exemple : définissez `remote.token = "GH_TOKEN"` (dans les variables d'environnement CI) pour permettre à PSR de push les tags et créer des Releases.

### Workflow & commandes utiles
- Générer la configuration par défaut : `semantic-release generate-config --pyproject >> pyproject.toml`.
- Tester la config en simulation (no-op / dry run) :
	- `semantic-release -v --noop version` → voir ce qui se passerait sans tag/commit.
	- `semantic-release -vv version --no-commit --no-tag` → évaluer localement sans modification.
- Exécution finale en CI : `semantic-release version --push --vcs-release` (exige token et autorisations CI).

### Bonnes pratiques
- Forcer les Conventional Commits sur les branches via des hooks (commit-msg) et/ou un CI linter (ex. `commitlint`) pour garantir des messages parseables.
- Tester en local et en CI en mode `--noop` pour éviter des releases indésirables.
- Protéger les branches de release et utiliser des tokens limités (scopes minimaux) pour automatiser la publication.
- Vérifier `parse_squash_commits` si vous utilisez les merges par squash.

---

## 10) Annexes : MkDocs, déploiement GitHub Pages et mkdocstrings

### Comment MkDocs génère de la documentation ?

MkDocs prend des fichiers Markdown (par défaut dans le dossier `docs/`) et un fichier de configuration `mkdocs.yml`. La génération se fait principalement en deux étapes :

- En local / développement : `mkdocs serve` lance un serveur qui construit le site et fournit un rechargement automatique à chaque sauvegarde (dev-server).
- En production / build : `mkdocs build` lit les fichiers Markdown et la configuration (`mkdocs.yml`), convertit chaque page en HTML statique, applique le thème (par ex. `material`), copie les ressources (CSS/JS/images) et écrit la sortie dans le répertoire `site/`. MkDocs génère aussi des fichiers annexes utiles (par ex. `search_index.json`, `sitemap.xml`).

La navigation et l'ordre des pages sont définis via la clé `nav` dans `mkdocs.yml`. Des extensions Markdown et des plugins (ex. pour la recherche, l'autodoc, l'optimisation) peuvent être activés depuis la configuration pour enrichir le rendu.

### Comment déployer sur GitHub Pages ?

Plusieurs méthodes sont utilisées couramment :

- Méthode rapide (commande intégrée) : utiliser `mkdocs gh-deploy`. Cette commande construit le site puis publie automatiquement les fichiers générés dans une branche (généralement `gh-pages`) et pousse les modifications vers le dépôt distant.

	Exemple :
	```bash
	mkdocs gh-deploy
	```

- Méthode manuelle : construire puis pousser le contenu du dossier `site/` sur la branche choisie pour GitHub Pages (par ex. `gh-pages` ou `main`/`docs`). Exemple basique :
	```bash
	mkdocs build
	# puis copier/committer les fichiers de site/ dans la branche configurée pour Pages
	```

- Utiliser GitHub Pages (paramètres) : via `Settings → Pages → Build and deployment` vous pouvez choisir la source de publication (branche `gh-pages`, ou `main`/`docs`). Pour un site utilisateur, créez un dépôt nommé `username.github.io` et poussez la source.

- Déploiement CI/CD : automatiser la construction et le déploiement avec une action GitHub Actions (par exemple `peaceiris/actions-gh-pages` ou un job qui exécute `mkdocs build` puis déploie). Cette méthode est recommandée pour inclure tests/contrôles avant publication.

Note : quand vous utilisez des thèmes/plugins (ex. Material for MkDocs), pensez à définir `site_url` dans `mkdocs.yml` car certains plugins et le thème s'appuient sur cette URL pour générer des liens corrects (important pour GitHub Pages si le site n'est pas à la racine d'un domaine personnalisé).

### Qu'est-ce que mkdocstrings ?

`mkdocstrings` est un plugin MkDocs qui génère automatiquement la documentation API à partir des docstrings du code source. Plutôt que d'écrire manuellement toutes les pages d'API, vous insérez des directives dans vos fichiers Markdown (par exemple `::: package.module.Class`) et `mkdocstrings` extrait les signatures, les docstrings et les membres pour produire une documentation structurée et navigable.

Principaux points :
- Support multi-langage via des handlers (Python, JavaScript, etc.).
- Intégration naturelle avec les thèmes comme Material for MkDocs pour obtenir une présentation claire des API.
- Usage courant (exemple) :
	```markdown
	## API

	::: mypackage.module.MyClass
	```

mkdocstrings facilite la maintenance de la doc API (elle suit le code) et s'intègre dans le flux MkDocs (build, serve, plugins), ce qui permet d'avoir une documentation utilisateur + API cohérente et générée automatiquement.


## 7) Qu'est-ce que le versionnage sémantique (SemVer) ? 🔢

SemVer est une convention permettant de donner un sens clair aux numéros de version, permettant aux utilisateurs et outils de comprendre l'impact d'une release.

### Format
- SemVer suit la forme MAJOR.MINOR.PATCH (ex. `1.2.3`).
- On peut ajouter des pré-versions (ex. `1.2.3-alpha.1`) et des métadonnées de build (ex. `1.2.3+build.1`).

### Quand incrémenter chaque niveau ?
- MAJOR : modifications incompatibles — rupture de l'API/contrat avec les utilisateurs (ex. `1.0.0` → `2.0.0`).
- MINOR : ajout de nouvelles fonctionnalités compatibles rétro-activement (ex. `1.2.3` → `1.3.0`).
- PATCH : corrections de bugs compatibles rétro-activement (ex. `1.2.3` → `1.2.4`).

### Exemples & remarques
- Si un commit introduit un changement casse-tête API (BREAKING), bump MAJOR.
- Les versions pré-release aident à tester avant la publication stable.
- Garder `project.version` à jour (ou utilisez un outil qui l'update automatiquement comme PSR).

---

## 8) Qu'est-ce que Conventional Commits ? ✍️

Conventional Commits est une spécification qui standardise le format des messages de commit afin de rendre l'historique lisible et exploitable par des outils (génération automatique de changelog, détermination de bump SemVer...).

### Format des messages

```
<type>(<scope optionnel>)?: <description>

[corps optionnel]

[pied optionnel]
```

Les éléments principaux : `type` (ex. `feat`, `fix`), `scope` (quel composant affecté), `description`, `body` (motivation/détails), `footer` (références, `BREAKING CHANGE`).

### Types courants
- `feat` : nouvelle fonctionnalité (impacterait un bump MINOR).
- `fix` : correction de bogue (PATCH).
- `docs`, `style`, `chore`, `ci`, `test`, `refactor`, `perf`, `build` : métadonnées / organisation / qualité.

### Indiquer une rupture de compatibilité
- Utilisez `BREAKING CHANGE: <description>` dans le pied du commit, OU ajoutez `!` juste avant le `:` dans le titre du commit (ex. `feat(api)!: ...`). Cela déclenche un bump MAJOR.

### Impact sur le versionnage
- Les outils (ex. python-semantic-release) traduisent automatiquement les `types` en types de bump SemVer :
	- `fix` → PATCH
	- `feat` → MINOR
	- `BREAKING CHANGE` / `!` → MAJOR
- Les autres types n'affectent pas la version par défaut sauf s'ils contiennent un `BREAKING CHANGE`.

### Exemples
```text
feat(api): add filters to product listing

fix(auth): correct token handling on refresh

perf(db): reduce query time for aggregate requests

feat!: change auth token format

BREAKING CHANGE: token structure changed from `x.y` to `a.b.c`.
```

---

## 9) Comment python-semantic-release fonctionne ? 🐍🔧

Python Semantic Release (PSR) automatise la détermination de la prochaine version à partir des messages de commit (SemVer + Conventional Commits), puis met à jour le `version` du projet, génère ou met à jour un `CHANGELOG`, tagge le dépôt, et peut publier des artefacts et créer une Release sur la plateforme VCS (ex : GitHub).

### Configuration dans `pyproject.toml`
- La configuration se place dans la table `[tool.semantic_release]` :

```toml
[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
commit_parser = "conventional"
vcs_release = true
[tool.semantic_release.commit_parser_options]
minor_tags = ["feat"]
patch_tags = ["fix","perf"]
parse_squash_commits = true
ignore_merge_commits = true
build_command = "python -m build --sdist --wheel ."
```

- `version_toml` : emplacement à mettre à jour lors d'un bump (ex. `pyproject.toml:project.version`).
- `commit_parser` : parser de messages (`conventional` par défaut pour Conventional Commits).
- `commit_parser_options` : permet d'ajuster les tags considérés pour `minor`/`patch` et gérer `squash`/`merge`.
- `build_command` : commande pour construire les artefacts avant publication.

### Génération du CHANGELOG
- PSR lit les messages et génère des notes de version (CHANGELOG) via des templates configurables.
- On peut définir `changelog_file`, `output_format` (`md`/`rst`) et `exclude_commit_patterns` pour filtrer les commits à ignorer (ex: `chore`, `ci`, `test`).

Example :
```toml
[tool.semantic_release.changelog]
changelog_file = "CHANGELOG.md"
output_format = "md"
exclude_commit_patterns = [
	"^chore(?:\([^)]*?\))?: .+",
	"^ci(?:\([^)]*?\))?: .+",
]
```

### Création des releases GitHub (ou autre VCS)
- PSR peut créer des tags et des releases sur la plateforme de VCS en utilisant un token stocké en variable d'environnement (ex. `GH_TOKEN` pour GitHub, `GITLAB_TOKEN` pour GitLab).
- Exemple : définissez `remote.token = "GH_TOKEN"` (dans les variables d'environnement CI) pour permettre à PSR de push les tags et créer des Releases.

### Workflow & commandes utiles
- Générer la configuration par défaut : `semantic-release generate-config --pyproject >> pyproject.toml`.
- Tester la config en simulation (no-op / dry run) :
	- `semantic-release -v --noop version` → voir ce qui se passerait sans tag/commit.
	- `semantic-release -vv version --no-commit --no-tag` → évaluer localement sans modification.
- Exécution finale en CI : `semantic-release version --push --vcs-release` (exige token et autorisations CI).

### Bonnes pratiques
- Forcer les Conventional Commits sur les branches via des hooks (commit-msg) et/ou un CI linter (ex. `commitlint`) pour garantir des messages parseables.
- Tester en local et en CI en mode `--noop` pour éviter des releases indésirables.
- Protéger les branches de release et utiliser des tokens limités (scopes minimaux) pour automatiser la publication.
- Vérifier `parse_squash_commits` si vous utilisez les merges par squash.

---
