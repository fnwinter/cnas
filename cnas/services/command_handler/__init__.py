"""Dispatch command messages from the service process."""

from __future__ import annotations

import os
import subprocess
from typing import Any


class CmdHandler:
    """Handles structured command events from CmdMessageQueue."""

    EVENT_TEST_COMMAND = "test_command"
    EVENT_MDSTAT_COMMAND = "mdstat_command"
    EVENT_DF_H_COMMAND = "df_h_command"
    EVENT_PS_AUX_COMMAND = "ps_aux_command"
    EVENT_MINECRAFT_SCRIPT = "minecraft_script"

    _MINECRAFT_SCRIPTS: dict[str, dict[str, Any]] = {
        "java/install_minecraft_server.sh": {"background": False, "timeout": 600},
        "java/start_minecraft_server.sh": {"background": True},
        "java/stop_minecraft_server.sh": {"background": False, "timeout": 60},
        "bedrock/install_bedrock_server.sh": {"background": False, "timeout": 600},
        "bedrock/start_bedrock_server.sh": {"background": True},
        "bedrock/stop_bedrock_server.sh": {"background": False, "timeout": 60},
    }

    @classmethod
    def _minecraft_server_root(cls) -> str:
        here = os.path.dirname(os.path.abspath(__file__))
        cnas_pkg = os.path.dirname(os.path.dirname(here))
        return os.path.join(cnas_pkg, "services", "minecraft_server")

    @classmethod
    def handle(cls, message: Any) -> dict[str, Any]:
        if isinstance(message, dict) and message.get("event") == cls.EVENT_TEST_COMMAND:
            return cls._handle_test_command(message)
        if isinstance(message, dict) and message.get("event") == cls.EVENT_MDSTAT_COMMAND:
            return cls._handle_mdstat_command(message)
        if isinstance(message, dict) and message.get("event") == cls.EVENT_DF_H_COMMAND:
            return cls._handle_df_h_command(message)
        if isinstance(message, dict) and message.get("event") == cls.EVENT_PS_AUX_COMMAND:
            return cls._handle_ps_aux_command(message)
        if isinstance(message, dict) and message.get("event") == cls.EVENT_MINECRAFT_SCRIPT:
            return cls._handle_minecraft_script(message)
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

    @classmethod
    def _handle_df_h_command(cls, message: dict[str, Any]) -> dict[str, Any]:
        proc = subprocess.run(
            "df -h",
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
            "event": cls.EVENT_DF_H_COMMAND,
            "received": True,
            "result": output,
            "returncode": proc.returncode,
            "source": message.get("source"),
        }

    @classmethod
    def _handle_ps_aux_command(cls, message: dict[str, Any]) -> dict[str, Any]:
        proc = subprocess.run(
            "ps aux",
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=90,
        )
        output = (proc.stdout or "") + (proc.stderr or "")
        return {
            "status": "ok" if proc.returncode == 0 else "error",
            "event": cls.EVENT_PS_AUX_COMMAND,
            "received": True,
            "result": output,
            "returncode": proc.returncode,
            "source": message.get("source"),
        }

    @classmethod
    def _handle_minecraft_script(cls, message: dict[str, Any]) -> dict[str, Any]:  # pylint: disable=too-many-locals
        rel = message.get("script_key")
        if not isinstance(rel, str) or rel not in cls._MINECRAFT_SCRIPTS:
            return {
                "status": "error",
                "event": cls.EVENT_MINECRAFT_SCRIPT,
                "received": True,
                "result": f"invalid script_key: {rel!r}",
                "returncode": None,
                "source": message.get("source"),
            }

        root = os.path.normpath(cls._minecraft_server_root())
        script_path = os.path.normpath(os.path.join(root, *rel.split("/")))
        if script_path != root and not script_path.startswith(root + os.sep):
            return {
                "status": "error",
                "event": cls.EVENT_MINECRAFT_SCRIPT,
                "received": True,
                "result": "script path outside minecraft_server root",
                "returncode": None,
                "source": message.get("source"),
            }

        if not os.path.isfile(script_path):
            return {
                "status": "error",
                "event": cls.EVENT_MINECRAFT_SCRIPT,
                "received": True,
                "result": f"missing script: {script_path}",
                "returncode": None,
                "source": message.get("source"),
            }

        cfg = cls._MINECRAFT_SCRIPTS[rel]
        script_dir = os.path.dirname(script_path)

        if cfg.get("background"):
            proc = subprocess.Popen(  # pylint: disable=consider-using-with
                ["/bin/sh", script_path],
                cwd=script_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            return {
                "status": "ok",
                "event": cls.EVENT_MINECRAFT_SCRIPT,
                "received": True,
                "result": f"started in background (pid={proc.pid})",
                "returncode": None,
                "pid": proc.pid,
                "script_key": rel,
                "source": message.get("source"),
            }

        timeout = float(cfg.get("timeout", 120))
        try:
            proc = subprocess.run(
                ["/bin/sh", script_path],
                cwd=script_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as e:
            chunks: list[str] = []
            for stream in (e.stdout, e.stderr):
                if not stream:
                    continue
                if isinstance(stream, str):
                    decoded = stream
                else:
                    decoded = stream.decode("utf-8", errors="replace")
                chunks.append(decoded)
            out = "\n".join(chunks).strip()
            msg = f"script timed out after {timeout}s"
            if out:
                msg = f"{msg}\n{out}"
            return {
                "status": "error",
                "event": cls.EVENT_MINECRAFT_SCRIPT,
                "received": True,
                "result": msg,
                "returncode": None,
                "script_key": rel,
                "source": message.get("source"),
            }
        output = (proc.stdout or "") + (proc.stderr or "")
        return {
            "status": "ok" if proc.returncode == 0 else "error",
            "event": cls.EVENT_MINECRAFT_SCRIPT,
            "received": True,
            "result": output,
            "returncode": proc.returncode,
            "script_key": rel,
            "source": message.get("source"),
        }
