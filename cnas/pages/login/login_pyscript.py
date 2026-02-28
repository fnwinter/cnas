import json

from pyscript import when
from pyscript import document
from pyscript import window

try:
    import pyodide_js
    pyodide_js.loadPackage('cryptography')

except Exception as e:
    print(f"Error loading pyodide_js, pyscript package: {str(e)}")

def test():
    print("test")