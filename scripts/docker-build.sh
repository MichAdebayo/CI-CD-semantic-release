#!/usr/bin/env bash
set -euo pipefail

# Load .env if present
if [ -f .env ]; then
  # shellcheck disable=SC1091
  set -a
  . .env
  set +a
fi

TAG=${1:-local-ci-cd-semantic-release:test}

if [ -n "${GHCR_USER:-}" ] && [ -n "${GHCR_PAT:-}" ]; then
  echo "Logging into ghcr.io as ${GHCR_USER}"
  echo "${GHCR_PAT}" | docker login ghcr.io -u "${GHCR_USER}" --password-stdin
else
  echo "GHCR_USER or GHCR_PAT not set. Skipping ghcr login."
fi

echo "Building image ${TAG}..."
docker build -t "${TAG}" .

echo "Build finished: ${TAG}"
