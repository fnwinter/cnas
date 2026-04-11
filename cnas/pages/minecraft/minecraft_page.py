from flask import jsonify
from jinja2 import Template

from pages.base.page import page
from pages.base.system.cmd_message_queue import CmdMessageQueue
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call

_ACTION_SCRIPTS: dict[str, str] = {
    "install_java": "java/install_minecraft_server.sh",
    "start_java": "java/start_minecraft_server.sh",
    "stop_java": "java/stop_minecraft_server.sh",
    "install_bedrock": "bedrock/install_bedrock_server.sh",
    "start_bedrock": "bedrock/start_bedrock_server.sh",
    "stop_bedrock": "bedrock/stop_bedrock_server.sh",
}


class minecraft_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("Minecraft")

    @html_file("htmls/minecraft.html")
    @pyscript("minecraft_pyscript.py")
    def load_scripts(self):
        return self

    @staticmethod
    def _queue_timeout_for_action(action: str) -> float:
        if action in ("install_java", "install_bedrock"):
            return 620.0
        return 90.0

    @rest_call("minecraft/api_run")
    def rest_minecraft_run(self):
        try:
            payload = self.json_data if isinstance(self.json_data, dict) else {}
            action = payload.get("action")
            script_key = _ACTION_SCRIPTS.get(action)
            if script_key is None:
                return jsonify({"status": "error", "message": "unknown action"}), 400
            event = {
                "event": "minecraft_script",
                "script_key": script_key,
                "source": f"minecraft page: {action}",
            }
            timeout = self._queue_timeout_for_action(action)
            result = CmdMessageQueue.send_message(event, timeout=timeout)
            if result is None:
                return jsonify({"status": "timeout", "message": "no response from service"}), 504
            return jsonify({"status": "ok", "message": action, "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    def body_content(self):
        self.html = Template(self.html).render(
            title="Minecraft servers",
            content="Run install / start / stop scripts under services/minecraft_server (Java and Bedrock).",
        )
        return self
