import os
from flask import   request, session

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class page:
    def __init__(self, filename = None):
        self.filename = os.path.join(SCRIPT_DIR, filename) if filename is not None else None
        self.pyscript = ""
        self.api_result = None
        self.json_data = {}
        if request.is_json:
            self.json_data = request.get_json()
        if self.filename is not None:
            with open(self.filename, "r") as f:
                self.html = "".join(f.readlines())
        else:
            self.html = ""

    def set_session(self, key, value):
        session[key] = value

    def get_session(self, key):
        return session.get(key)

    def clear_session(self, key):
        session.pop(key, None)

    def get_result(self):
        if self.api_result is not None:
            return self.api_result
        return self.html