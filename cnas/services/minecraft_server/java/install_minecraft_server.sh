#!/bin/sh
set -e

JAVA_MAJOR=""

parse_java_major() {
  line=""
  if java --version >/tmp/jv_out.$$ 2>&1; then
    line=$(head -n 1 /tmp/jv_out.$$)
  else
    java -version >/tmp/jv_out.$$ 2>&1 || true
    line=$(head -n 1 /tmp/jv_out.$$)
  fi
  rm -f /tmp/jv_out.$$

  quoted=$(printf '%s\n' "$line" | sed -n 's/.*version "\([^"]*\)".*/\1/p')
  if [ -n "$quoted" ]; then
    major=$(printf '%s\n' "$quoted" | cut -d. -f1)
    minor=$(printf '%s\n' "$quoted" | cut -d. -f2)
    if [ "$major" = "1" ]; then
      JAVA_MAJOR=$minor
      return
    fi
    JAVA_MAJOR=$major
    return
  fi

  ver=$(printf '%s\n' "$line" | awk '{print $2}')
  JAVA_MAJOR=$(printf '%s\n' "$ver" | cut -d. -f1)
}

if ! command -v java >/dev/null 2>&1; then
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "apt-get not found; install openjdk-25-jre manually." >&2
    exit 1
  fi
  apt-get update
  apt-get install -y openjdk-25-jre
fi

parse_java_major

if ! printf '%s\n' "$JAVA_MAJOR" | grep -Eq '^[0-9]+$'; then
  echo "java version error" >&2
  exit 1
fi

if [ "$JAVA_MAJOR" -lt 25 ]; then
  echo "java version error" >&2
  exit 1
fi
