from flask import jsonify
from jinja2 import Template

from pages.base.page import page
from pages.base.system.cmd_message_queue import CmdMessageQueue
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call

class test_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("test page")

    @html_file("htmls/test.html")
    @pyscript("test_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("test/api1")
    def rest_test_api1(self):
        return jsonify({"status": "ok"}), 200

    @rest_call("test/api2")
    def post_api_call2(self):
        return jsonify({"status": "ok2"}), 200

    @rest_call("test/api_command")
    def rest_api_command(self):
        try:
            event = {"event": "test_command", "source": "ls command button"}
            result = CmdMessageQueue.send_message(event)
            if result is None:
                return jsonify({"status": "timeout", "message": "no response from service"}), 504
            print("test/api_command response:", result)
            return jsonify({"status": "ok", "message": "command sent", "result": result}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    def body_content(self):
        self.html = Template(self.html).render(title="button call test", content="This page is for testing the button call functionality.")
        return self
