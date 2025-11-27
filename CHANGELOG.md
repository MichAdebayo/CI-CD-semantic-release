# CHANGELOG

<!-- version list -->

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
