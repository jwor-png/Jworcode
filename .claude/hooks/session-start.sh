#!/bin/bash
# Cuan session-start: enable PDF reading tooling (idempotent, never blocks).
# The remote container is ephemeral, so re-enable each session.
set +e
# 1) Fix the Python PDF stack (cffi backend, used by pypdf/pdfminer/cryptography)
python3 -c "import _cffi_backend" 2>/dev/null || pip install --quiet --force-reinstall --no-cache-dir cffi >/dev/null 2>&1
# 2) Ensure poppler (pdftotext + pdftoppm) so the Read tool can render/read PDFs
command -v pdftotext >/dev/null 2>&1 || { apt-get update -qq >/dev/null 2>&1; apt-get install -y poppler-utils >/dev/null 2>&1; }
exit 0
