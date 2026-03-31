from flask import jsonify
from jinja2 import Template

from pages.base.page import page
from pages.base.system.cmd_message_queue import CmdMessageQueue
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call


class system_status_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("System status")

    @html_file("htmls/system_status.html")
    @pyscript("system_status_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("system_status/api_mdstat")
    def rest_api_mdstat(self):
        try:
            event = {"event": "mdstat_command", "source": "system_status mdstat button"}
            result = CmdMessageQueue.send_message(event)
            if result is None:
                return jsonify({"status": "timeout", "message": "no response from service"}), 504
            return jsonify({"status": "ok", "message": "mdstat", "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @rest_call("system_status/api_ps_aux")
    def rest_api_ps_aux(self):
        try:
            event = {"event": "ps_aux_command", "source": "system_status ps aux button"}
            result = CmdMessageQueue.send_message(event, timeout=120.0)
            if result is None:
                return jsonify({"status": "timeout", "message": "no response from service"}), 504
            return jsonify({"status": "ok", "message": "ps aux", "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    def body_content(self):
        self.html = Template(self.html).render(
            title="System status",
            content="View service and process status here. (Extend with APIs or widgets as needed.)",
        )
        return self
