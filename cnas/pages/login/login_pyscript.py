import json

from pyscript import when
from pyscript import document
from pyscript import window

try:
    import pyodide_js
    pyodide_js.loadPackage('cryptography')

    @when("click", "#call_python")
    def dispatch_event(event):
        __call_python = document.querySelector("#call_python")
        __value = json.loads(event.target.getAttribute("data-value"))
        
        __function_name = __value[0]
        __param1 = __value[1]
        __param2 = __value[2]
        __param3 = __value[3]
        if __function_name == "generateUrl":
            generateUrl(__param1, __param2)
        elif __function_name == "decryptUrlData":
            decryptUrlData(__param1, __param2)

except Exception as e:
    print(f"Error loading pyodide_js, pyscript package: {str(e)}")

def test():
    print("test")