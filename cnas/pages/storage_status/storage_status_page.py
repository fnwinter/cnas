from flask import jsonify
from jinja2 import Template

from pages.base.page import page
from pages.base.system.cmd_message_queue import CmdMessageQueue
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call


class storage_status_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("Storage status")

    @html_file("htmls/storage_status.html")
    @pyscript("storage_status_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("storage_status/api_df_h")
    def rest_api_df_h(self):
        try:
            event = {"event": "df_h_command", "source": "storage_status check status button"}
            result = CmdMessageQueue.send_message(event)
            if result is None:
                return jsonify({"status": "timeout", "message": "no response from service"}), 504
            return jsonify({"status": "ok", "message": "df -h", "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    def body_content(self):
        self.html = Template(self.html).render(
            title="Storage status",
            content="Check disk usage with df -h on the NAS host.",
        )
        return self
