#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Copy meridian engine files from repo to ~/meridian on every session start
cp -r "$CLAUDE_PROJECT_DIR/meridian" "$HOME/meridian"
