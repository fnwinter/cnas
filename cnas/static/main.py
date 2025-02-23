import pyjokes
from pyweb import pydom

def get_joke():
    pydom["div#jokes"].html = f"{pyjokes.get_joke()} 🥁"
