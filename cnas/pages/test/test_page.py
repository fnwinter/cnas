from flask import jsonify
from flask import request

from pages.page import page
from pages.system.pyscript import pyscript
from pages.system.rest_call import rest_call

from components.elements.html import html
from components.widgets.head_widget import head_widget
from components.widgets.body_widget import body_widget

class test_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("test page")

    @html("test.html")
    @pyscript("test_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("test/api1")
    def rest_test_api1(self):
        return jsonify({"status": "ok"}), 200

    @rest_call("test/api2")
    def post_api_call2(self):
        return jsonify({"status": "ok2"}), 200

    def body_content(self):
        return self.template.render(title=self.title, content=self.content)
