#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

cd "$SCRIPT_DIR"

if [ ! -x "$SCRIPT_DIR/.venv/bin/jupyter" ]; then
  echo "Jupyter is not installed in $SCRIPT_DIR/.venv." >&2
  echo "Expected executable: $SCRIPT_DIR/.venv/bin/jupyter" >&2
  exit 1
fi

mkdir -p "$SCRIPT_DIR/.jupyter/data" \
  "$SCRIPT_DIR/.jupyter/config" \
  "$SCRIPT_DIR/.jupyter/runtime" \
  "$SCRIPT_DIR/.matplotlib" \
  "$SCRIPT_DIR/.cache"

export JUPYTER_DATA_DIR="$SCRIPT_DIR/.jupyter/data"
export JUPYTER_CONFIG_DIR="$SCRIPT_DIR/.jupyter/config"
export JUPYTER_RUNTIME_DIR="$SCRIPT_DIR/.jupyter/runtime"
export MPLCONFIGDIR="$SCRIPT_DIR/.matplotlib"
export XDG_CACHE_HOME="$SCRIPT_DIR/.cache"

exec "$SCRIPT_DIR/.venv/bin/jupyter" notebook "$@"
