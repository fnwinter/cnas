import asyncio
import json

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
    __params = __value[1:]

    handler = BUTTON_HANDLERS.get(__function_name)
    if handler is not None:
        result = handler(*__params)
        if asyncio.iscoroutine(result):
            asyncio.ensure_future(result)
    else:
        print(f"No handler registered for: {__function_name}")
