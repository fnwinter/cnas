from flask import jsonify
from flask import request

from pages.page import page
from pages.system.pyscript import pyscript
from pages.system.api_call import api_call

from components.elements.html import html
from components.widgets.head_widget import head_widget
from components.widgets.body_widget import body_widget

class test_page(page):
    @pyscript("test_pyscript.py")
    def __init__(self):
        pass

    def post_api_call(self):
        print("request.method:", request.method)
        print("request.url:", request.url)
        print("request.headers:", dict(request.headers))
        print("request.get_data(as_text=True):", request.get_data(as_text=True))
        if request.is_json:
            print("request.get_json():", request.get_json())
        return jsonify({"status": "ok"})

    @api_call
    def __str__(self):
        print("__str__ is called")
        if self.api_result is not None:
            print("api_result:", self.api_result)
            return self.api_result
        print("result is None")
        return str(html(
            head_widget(title="test page"),
            body_widget(
            ).set_content(
"""<button id='call_python'></button>
<button id="test" onclick='test_button()'>test</button>
<script>
    function test_button() {
        callPython("test_button", "param1", "param2", "param3");
    }
</script>
""" + self.pyscript)
        ))
