# CHANGELOG

<!-- version list -->

## v0.2.1 (2025-11-28)

### Bug Fixes

- **cd**: Regenerate hook url for render
  ([`2402277`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/2402277dc30163082a10cbda40f73f5628ef4962))

### Refactoring

- **workflows**: Update deployment conditions for Render and CI workflows
  ([`8f78363`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/8f783635bb1243d0c8e99ff77ddb0b6e0660b33e))


## v0.2.0 (2025-11-28)


## v0.2.0-dev.8 (2025-11-28)

### Bug Fixes

- **.gitignore**: Add ci.yml and cs.pem files to ignore list
  ([`3b1a7c8`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/3b1a7c82839f378d88cbec07e7fb6ec0b1716a71))

### Refactoring

- **ci**: Update secrets in workflows to include RENDER_DEPLOY_HOOK_URL
  ([`0d31acf`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/0d31acfff66eff1aaf5acb57191c5ca376d180a3))

- **docs**: Simplify theme configuration in MkDocs
  ([`3a561cf`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/3a561cfbe2e1acb4ca5617a10013f78f769a9551))

- **docs**: Update contributors documentation link in mkdocs.yml
  ([`302c3ae`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/302c3aeb75e33cf772a9ed8cfe21556eb966c08a))

- **docs**: Update navigation in mkdocs.yml
  ([`26f9da9`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/26f9da911f87e2ee9506f96147e3c91ca256eaf2))

- **docs**: Update navigation links in MkDocs configuration
  ([`9c08786`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/9c087861c0135cecfd6593cd80c1889935d2e814))

- **docs**: Update theme configuration in MkDocs
  ([`f96ca91`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/f96ca91a964f5d4d3a964d1cffdceebc906e589b))

- **env**: Update .env.example and pre-commit configuration for secret management
  ([`7f2e4e2`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7f2e4e2ce68084b56db1253c4705666e4dd8581c))


## v0.2.0-dev.7 (2025-11-28)

### Features

- **docs**: Add initial documentation structure and content.
  ([`1dff052`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/1dff052459c5f47d188fe6ea5e65cf9c745d7b5f))

### Refactoring

- **ci**: Uncomment Mypy, Bandit, Detect Secrets, and testing steps in CI workflow
  ([`7d175e9`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7d175e91be50445cb1079eb54c30d44a97ca51a3))


## v0.2.0-dev.6 (2025-11-27)

### Features

- **ci**: Add Trivy image scanning step and include image metadata labels
  ([`82cd64e`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/82cd64e0600ea1c30fc9487a294612c6ee766369))

### Refactoring

- **ci**: Simplify authentication method by using GITHUB_TOKEN for GHCR
  ([`7d438bf`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7d438bf9e890bf9c766a3c73f08a43993216c5e3))


## v0.2.0-dev.5 (2025-11-27)

### Features

- **ci**: Comment out unused checks and scans in CI workflow
  ([`c3382ef`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/c3382ef1afb09a4416a3610587a5b93f7347b845))


## v0.2.0-dev.4 (2025-11-27)

### Features

- **release**: Enhance GitHub App token handling and streamline authentication process in workflows
  ([`89d57a3`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/89d57a3f64c9eda9b12d9f86b5fb7e37b66bb29f))


## v0.2.0-dev.3 (2025-11-27)

### Features

- **release**: Refactor GitHub App token handling and streamline private key decoding
  ([`f0d324b`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/f0d324b6fd4249b859901b543ba1b9215411ab62))


## v0.2.0-dev.2 (2025-11-27)

### Features

- **release**: Add GitHub App token handling and permissions checks in workflows
  ([`15de9bb`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/15de9bbb03c0bf59bd38e9743ce89e732fa5564a))

- **release**: Refine token source handling and diagnostics in workflows
  ([`0b8b5d3`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/0b8b5d3481af25df74ff846bd995889c61e63d6d))

- **release**: Update GitHub App token handling and streamline workflow inputs
  ([`aaea965`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/aaea965ed4fa450ce723ae9abc1e8f0131cc71b1))


## v0.2.0-dev.1 (2025-11-27)

### Bug Fixes

- **app**: Add test comment to trigger semantic release
  ([`cd34263`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/cd342638c465814c6d75c6cac83fc7793c125aef))

- **cd**: Allow CD workflow to skip unsupported branches without failing
  ([`8979a1b`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/8979a1bf664c1e5442ca81c5a528ca1e24ae1f73))

- **cd**: Ensure empty tags output is written for unsupported branches to prevent failures
  ([`7d5b00d`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7d5b00d51cef0a56dc42f62e17f3824f94474faf))

- **ci**: Correct syntax for setting APP_PRIVATE_KEY in environment variables
  ([`9257594`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/9257594510e5b990200e75665fa9161d4873b012))

- **ci**: Update permissions to allow write access for contents in CI workflow
  ([`fd84d6d`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/fd84d6db2c023d0ab2d09b85fe15ec5aee87fee6))

- **release**: Conditionally compute release version only when base_ref is empty
  ([`f727f35`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/f727f355700b55276ceffc40629a0b6d1387c772))

- **release**: Ensure allow_zero_version is set to true in semantic release configuration
  ([`b787527`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/b7875277fe62d6539765fc285df8c40d1ca7bc1f))

- **release**: Improve token handling and ensure correct branch checkout in release workflow
  ([`c0fc827`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/c0fc827037b20c6d5c8b77442944c00884e93561))

- **release**: Set prerelease to false for main branch in semantic release configuration
  ([`5c9162a`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/5c9162a6215698544a5accc06a0acbff59e6c0ca))

- **release**: Update token handling to fallback on github.token if RELEASE_GITHUB_TOKEN is empty;
  add debug step for verifying local and remote tags
  ([`5c9162a`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/5c9162a6215698544a5accc06a0acbff59e6c0ca))

### Features

- **cd**: Restructure CD workflow to prepare tags and build Docker images conditionally
  ([`e7801d4`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/e7801d4b337ae0e37a3a367dc4da0d1d54033ad5))

- **release**: Add fallback for GitHub App installation token creation and improve token handling
  ([`7ec7ba9`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7ec7ba9e4c5e2b58e8b1fbe35d4339682e62195f))

- **release**: Add PR context handling and improve branch resolution in release workflow
  ([`2254b16`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/2254b16735c878d0eacce8c94370be56d541b3e6))

- **release**: Add token validation for publish runs and enforce token forwarding
  ([`7b85dfc`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7b85dfc87c70092f8c614bae04e0eded8f8e1aea))

- **release**: Add version computation step and pass version to CD workflow
  ([`fbcf820`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/fbcf8206becbd93fbd121abce56a0ee2ee075238))

- **release**: Enhance GitHub App token handling and add verification steps for GHCR login
  ([`c61b52d`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/c61b52deaca4a2970586bec601f8f8df86434859))

- **release**: Enhance logging for semantic-release publish and display token presence
  ([`7dd090e`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/7dd090eba74c5d893652fc1595a883d0175bd25a))

- **release**: Enhance private key handling by adding support for base64 encoded keys and improving
  validation logic
  ([`2979837`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/29798377c525160f00af361ebed6db1bfb06f97e))

- **release**: Enhance private key handling by supporting both PEM and base64 formats
  ([`78f1e49`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/78f1e4925963cca7d185b1a14bf133dee42d73e4))

- **release**: Enhance release workflow by improving environment variable handling and output
  settings
  ([`fb36ddd`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/fb36ddd6177e80759ca3e01e8564bbd86eb9091b))

- **release**: Enhance semantic version handling and improve CD workflow for PRs
  ([`5e6ff39`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/5e6ff39614a49a01e15393e4b3a2a5bb02896929))

- **release**: Enhance semantic-release logging and debugging for push behavior
  ([`dddef97`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/dddef97360fd313cdf0e8d4c087fff52ef1485e1))

- **release**: Enhance tag preparation logic for Docker image based on branch and version input
  ([`350b61c`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/350b61c599c1b94c7b1397ae5667bf5320972460))

- **release**: Enhance token handling and Git configuration for release workflow
  ([`270eb28`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/270eb28e73b05dfeab6e8e204024541322abb8da))

- **release**: Enhance token management and add token source verification; update commit message
  format in pyproject.toml
  ([`720c63d`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/720c63df61e103bab0ac1de25a9972f10fa7e5ff))

- **release**: Forward APP secrets to release workflow for token creation
  ([`de08abe`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/de08abeddd37d450f6ba3ec1e6b50a88caaf9ad6))

- **release**: Refine tag preparation logic for main and develop branches, add support for
  deploy/ci_cd branch
  ([`a2a8d65`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/a2a8d65adba44bd1df6c8ba825595c76e627fc8b))

- **release**: Update GitHub App token creation process and enhance private key handling
  ([`4b7ddcf`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/4b7ddcf20b8b0b13b2918bb5cefb07780e2eb858))

- **release**: Update semantic-release commands for version bump and changelog generation
  ([`8530712`](https://github.com/MichAdebayo/CI-CD-semantic-release/commit/8530712e55e0805aabbe0e92784c8543a4cc4ee5))


## v0.1.0 (2025-11-26)

- Initial Release
