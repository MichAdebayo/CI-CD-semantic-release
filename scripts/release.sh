#!/usr/bin/env bash
set -euo pipefail

# Release helper script for local publishing using python-semantic-release (via uv)
#
# Default behavior (no args): dry-run that prints the release tag (safe)
# Usage:
#   ./scripts/release.sh            # Default: prints the next tag (dry-run)
#   ./scripts/release.sh --help     # Show usage
#   ./scripts/release.sh --publish  # Perform an actual publish (requires GITHUB_TOKEN)
#   ./scripts/release.sh --publish --yes # Non-interactive publish
#

show_help() {
  cat <<EOF
Usage: $0 [options]

Options:
  --help            Show this help message and exit
  --dry-run         Print the next release tag/version and exit (default)
  --publish         Run semantic-release publish (requires GITHUB_TOKEN)
  --yes             Non-interactive: don't ask for confirmation when using --publish
  --as-prerelease    Force-as-prerelease
  --prerelease-token TOKEN  Specify a prerelease token (e.g., ci_cd)

Examples:
  # Dry-run (print tag)
  ./scripts/release.sh

  # Preview prerelease tag
  ./scripts/release.sh --dry-run --as-prerelease --prerelease-token ci_cd

  # Publish (interactive confirm)
  GITHUB_TOKEN=ghp_... ./scripts/release.sh --publish

  # Publish non-interactive
  GITHUB_TOKEN=ghp_... ./scripts/release.sh --publish --yes
EOF
}

DRY_RUN=true
PUBLISH=false
NON_INTERACTIVE=false
AS_PRERELEASE=false
PRERELEASE_TOKEN=""

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --help)
      show_help
      exit 0
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --publish)
      DRY_RUN=false
      PUBLISH=true
      shift
      ;;
    --yes)
      NON_INTERACTIVE=true
      shift
      ;;
    --as-prerelease)
      AS_PRERELEASE=true
      shift
      ;;
    --prerelease-token)
      PRERELEASE_TOKEN="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      show_help
      exit 2
      ;;
  esac
done

echo "[release.sh] Starting release script (DRY_RUN=${DRY_RUN}, PUBLISH=${PUBLISH}, PRERELEASE_TOKEN=${PRERELEASE_TOKEN})"

# 1) Refresh dependencies
echo "[release.sh] Syncing dependencies (including dev)"
uv sync --dev

# 2) If publishing and GHCR_PAT present, log in to ghcr.io (for docker publishing). Only login when publishing to avoid leaking creds accidentally.
if $PUBLISH && [ -n "${GHCR_PAT:-}" ]; then
  echo "[release.sh] GHCR_PAT detected -- logging in to ghcr.io"
  GHCR_USER=${GHCR_USER:-"${GITHUB_ACTOR:-$(git config user.name || echo 'local')}"}
  echo "$GHCR_PAT" | docker login ghcr.io -u "$GHCR_USER" --password-stdin
elif [ -n "${GHCR_PAT:-}" ]; then
  echo "[release.sh] GHCR_PAT available, but not publishing: skipping ghcr login"
fi

# 3) Dry-run: print tag/version and exit
if $DRY_RUN; then
  echo "[release.sh] Dry-run — printing next version tag"
  CMD=(uv run semantic-release version --no-commit --no-tag --no-changelog --no-push --no-vcs-release --skip-build --print-tag)
  if $AS_PRERELEASE; then
    CMD+=(--as-prerelease)
  fi
  if [ -n "${PRERELEASE_TOKEN}" ]; then
    CMD+=(--prerelease-token "${PRERELEASE_TOKEN}")
  fi
  echo "[release.sh] Running: ${CMD[*]}"
  "${CMD[@]}"
  echo "[release.sh] Dry-run complete."
  exit 0
fi

# 4) Publishing path — require GITHUB_TOKEN
if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "[release.sh] ERROR: GITHUB_TOKEN is not set. GITHUB_TOKEN is required to publish releases."
  echo "[release.sh] In CI (GitHub Actions) this is available by default as the repository token."
  echo "[release.sh] For local runs, export a personal token with the necessary scopes (repo, packages) as GITHUB_TOKEN."
  exit 1
fi

# 5) Confirm user intent unless --yes provided
if ! $NON_INTERACTIVE; then
  echo "[release.sh] You are about to publish - this will create tags and GitHub releases."
  read -p "Proceed with publish? (y/N): " yn
  case "$yn" in
    [Yy]*) ;;
    *) echo "Cancelled by user"; exit 0; ;;
  esac
fi

# 6) Configure git to allow commits/tags if running locally
git config user.name "release-bot" || true
git config user.email "release-bot@example.com" || true

echo "[release.sh] Running python-semantic-release publish..."
CMD=(uv run semantic-release publish)
if $AS_PRERELEASE; then
  CMD+=(--prerelease)
fi
if [ -n "${PRERELEASE_TOKEN}" ]; then
  CMD+=(--prerelease-token "${PRERELEASE_TOKEN}")
fi
echo "[release.sh] Running: ${CMD[*]}"
"${CMD[@]}"

echo "[release.sh] Done"
