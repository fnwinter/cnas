from flask import jsonify
from jinja2 import Template

from pages.page import page
from pages.system.html import html_file
from pages.system.pyscript import pyscript
from pages.system.rest_call import rest_call

class test_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("test page")

    @html_file("htmls/test.html")
    @pyscript("test_pyscript.py")
    def load_scripts(self):
        self.template = Template(self.html)
        return self

    @rest_call("test/api1")
    def rest_test_api1(self):
        return jsonify({"status": "ok"}), 200

    @rest_call("test/api2")
    def post_api_call2(self):
        return jsonify({"status": "ok2"}), 200

    def body_content(self):
        self.html = self.template.render(title="button call test", content="This page is for testing the button call functionality.")
        return self
