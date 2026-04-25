#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd "$SCRIPT_DIR"

DO_UPDATE=false
DO_INSTALL=false
DO_KILL=false
DO_BACKGROUND=false

for arg in "$@"; do
  case "$arg" in
    --update)
      DO_UPDATE=true
      ;;
    --install)
      DO_INSTALL=true
      ;;
    --kill)
      DO_KILL=true
      ;;
    --background)
      DO_BACKGROUND=true
      ;;
  esac
done

if [ "$DO_KILL" = true ]; then
  echo "# kill running cnas (flask --app cnas run)"
  if pkill -f "flask --app cnas run" 2>/dev/null; then
    echo "sent SIGTERM to matching process(es)"
  else
    echo "no matching flask cnas process found (or pkill unavailable)"
  fi
  exit 0
fi

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
if [ "$DO_BACKGROUND" = true ]; then
  flask --app cnas run --host=0.0.0.0 --port=8090 &
else
  flask --app cnas run --host=0.0.0.0 --port=8090
fi
popd

popd
