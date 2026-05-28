#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd "$SCRIPT_DIR"

DO_UPDATE=false
DO_INSTALL=false
DO_KILL=false
DO_BACKGROUND=false
DO_HTTPS=false
DOMAIN=""

while [ $# -gt 0 ]; do
  case "$1" in
    --update)
      DO_UPDATE=true
      shift
      ;;
    --install)
      DO_INSTALL=true
      shift
      ;;
    --kill)
      DO_KILL=true
      shift
      ;;
    --background)
      DO_BACKGROUND=true
      shift
      ;;
    --https)
      DO_HTTPS=true
      shift
      ;;
    --domain)
      if [ -z "${2:-}" ]; then
        echo "error: --domain requires a value"
        exit 1
      fi
      DOMAIN="$2"
      shift 2
      ;;
    --domain=*)
      DOMAIN="${1#*=}"
      if [ -z "$DOMAIN" ]; then
        echo "error: --domain requires a value"
        exit 1
      fi
      shift
      ;;
    --*)
      echo "error: unknown option: $1"
      exit 1
      ;;
    *)
      if [ -n "$DOMAIN" ]; then
        echo "error: unexpected argument: $1"
        exit 1
      fi
      DOMAIN="$1"
      shift
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

FLASK_ARGS=(--host=0.0.0.0 --port=8090)

if [ "$DO_HTTPS" = true ]; then
  if [ -z "$DOMAIN" ]; then
    echo "error: --https requires a domain (e.g. ./run.sh example.com --https)"
    exit 1
  fi

  SSL_KEY="/etc/letsencrypt/live/${DOMAIN}/privkey.pem"
  SSL_CERT="/etc/letsencrypt/live/${DOMAIN}/fullchain.pem"

  if [ ! -f "$SSL_KEY" ]; then
    echo "error: SSL key not found: $SSL_KEY"
    exit 1
  fi
  if [ ! -f "$SSL_CERT" ]; then
    echo "error: SSL cert not found: $SSL_CERT"
    exit 1
  fi

  FLASK_ARGS+=(--key="$SSL_KEY" --cert="$SSL_CERT")
  echo "HTTPS enabled for domain: $DOMAIN"
fi

if [ "$DO_BACKGROUND" = true ]; then
  flask --app cnas run "${FLASK_ARGS[@]}" &
else
  flask --app cnas run "${FLASK_ARGS[@]}"
fi
popd

popd
