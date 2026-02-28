from pages.page import page
from pages.system.pyscript import pyscript

from components.elements.html import html
from components.widgets.head_widget import head_widget
from components.widgets.body_widget import body_widget

class test_page(page):
    def __init__(self):
        pass

    @pyscript("test_pyscript.py")
    def __str__(self):
        return str(html(
            head_widget(title="test page"),
            body_widget(
            ).set_content(
"""<button id='call_python' ></button>
<button id="test" onclick='test_button()'>test</button>
<script>
    function __callPython(function_name, param1, param2, param3) {
        console.log("test_button __callPython before");
        const callPython_id = document.getElementById('call_python');
        callPython_id.setAttribute('data-value',
            JSON.stringify([function_name, param1, param2, param3]));
        callPython_id.click();
        console.log("test_button __callPython after");
    }
    function test_button() {
        console.log("test_button javascript");
        __callPython("test_button", "param1", "param2", "param3");
    }
</script>
""" + self.pyscript)
        ))
