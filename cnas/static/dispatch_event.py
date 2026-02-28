import json
import types

from pyscript import when
from pyscript import document

# 함수 이름 → 콜백 등록 (순환 import 방지)
BUTTON_HANDLERS = {}

def register_handler(name, callback):
    BUTTON_HANDLERS[name] = callback

@when("click", "#call_python")
def dispatch_event(event):
    __call_python = document.querySelector("#call_python")
    __value = json.loads(event.target.getAttribute("data-value"))

    __function_name = __value[0]
    __param1 = __value[1]
    __param2 = __value[2]
    __param3 = __value[3]

    handler = BUTTON_HANDLERS.get(__function_name)
    if handler is not None:
        handler(__param1, __param2, __param3)
    else:
        print(f"No handler registered for: {__function_name}")
