#!/bin/sh
set -e
cd "$(dirname "$0")" || exit 1

ZIP_URL="https://www.minecraft.net/bedrockdedicatedserver/bin-linux/bedrock-server-1.26.14.1.zip"
ZIP_FILE="bedrock-server-1.26.14.1.zip"
SERVER_BIN="bedrock_server"

if ! command -v wget >/dev/null 2>&1; then
  echo "wget is required but not installed." >&2
  exit 1
fi
if ! command -v unzip >/dev/null 2>&1; then
  echo "unzip is required but not installed." >&2
  exit 1
fi

wget -O "$ZIP_FILE" "$ZIP_URL"
unzip -o "$ZIP_FILE"

if [ ! -f "$SERVER_BIN" ]; then
  echo "expected executable not found: $SERVER_BIN" >&2
  exit 1
fi

chmod +x "$SERVER_BIN"
