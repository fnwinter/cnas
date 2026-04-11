#!/bin/sh
cd "$(dirname "$0")" || exit 1

chmod +x bedrock_server
exec ./bedrock_server
