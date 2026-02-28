#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd "$SCRIPT_DIR"

DO_UPDATE=false
DO_INSTALL=false

for arg in "$@"; do
  case "$arg" in
    --update)
      DO_UPDATE=true
      ;;
    --install)
      DO_INSTALL=true
      ;;
  esac
done

echo "# update code"
if [ "$DO_UPDATE" = true ]; then
  git pull origin main
else
  echo "skip git pull (no --update)"
fi

echo "# set venv"
if [ "$DO_INSTALL" = true ]; then
  if [[ "$(uname)" == "Darwin" ]]; then
    pipx install virtualenv
  else
    python3 -m pip install virtualenv
  fi
fi

if [ ! -d venv ]; then
  if command -v virtualenv >/dev/null 2>&1; then
    virtualenv venv
  else
    python3 -m virtualenv venv
  fi
fi
source ./venv/bin/activate

echo "# install dependencies"
if [ "$DO_INSTALL" = true ]; then
  python3 -m pip install --upgrade pip
  python3 -m pip install -r cnas/requirements.txt
else
  echo "skip pip install (no --install)"
fi

echo "# run cherrynas"
pushd cnas
flask --app cnas run --host=0.0.0.0 --port=8090
popd

popd
