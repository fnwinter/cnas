import json

from pyscript import when
from pyscript import document

@when("click", "#call_python")
def dispatch_event(event):
    __call_python = document.querySelector("#call_python")
    __value = json.loads(event.target.getAttribute("data-value"))
    
    __function_name = __value[0]
    __param1 = __value[1]
    __param2 = __value[2]
    __param3 = __value[3]
    print(event.detail)
    print(event.type)
    print(__function_name, __param1, __param2, __param3)
