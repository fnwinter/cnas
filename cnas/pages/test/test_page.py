from flask import jsonify

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

    def api_call(self):
        return "result from api_call"

    @api_call
    def __str__(self):
        print("__str__ is called")
        if self.api_result is not None:
            return str(self.api_result)
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
