#!/bin/sh

if command -v pkill >/dev/null 2>&1; then
  if pkill -x bedrock_server 2>/dev/null; then
    exit 0
  fi
  echo "no bedrock_server process found" >&2
  exit 1
fi

if command -v killall >/dev/null 2>&1; then
  if killall -q bedrock_server 2>/dev/null; then
    exit 0
  fi
  echo "no bedrock_server process found" >&2
  exit 1
fi

echo "pkill or killall is required but not installed." >&2
exit 1