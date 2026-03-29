"""Dispatch command messages from the service process."""

from __future__ import annotations

import subprocess
from typing import Any


class CmdHandler:
    """Handles structured command events from CmdMessageQueue."""

    EVENT_TEST_COMMAND = "test_command"
    EVENT_MDSTAT_COMMAND = "mdstat_command"

    @classmethod
    def handle(cls, message: Any) -> dict[str, Any]:
        if isinstance(message, dict) and message.get("event") == cls.EVENT_TEST_COMMAND:
            return cls._handle_test_command(message)
        if isinstance(message, dict) and message.get("event") == cls.EVENT_MDSTAT_COMMAND:
            return cls._handle_mdstat_command(message)
        return {"status": "ok", "event": message, "received": True}

    @classmethod
    def _handle_test_command(cls, message: dict[str, Any]) -> dict[str, Any]:
        proc = subprocess.run(
            "ls",
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
        output = (proc.stdout or "") + (proc.stderr or "")
        return {
            "status": "ok" if proc.returncode == 0 else "error",
            "event": cls.EVENT_TEST_COMMAND,
            "received": True,
            "result": output,
            "returncode": proc.returncode,
            "source": message.get("source"),
        }

    @classmethod
    def _handle_mdstat_command(cls, message: dict[str, Any]) -> dict[str, Any]:
        proc = subprocess.run(
            "cat /proc/mdstat",
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        output = (proc.stdout or "") + (proc.stderr or "")
        return {
            "status": "ok" if proc.returncode == 0 else "error",
            "event": cls.EVENT_MDSTAT_COMMAND,
            "received": True,
            "result": output,
            "returncode": proc.returncode,
            "source": message.get("source"),
        }
