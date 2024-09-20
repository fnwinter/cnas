from flask import request, session

class page:
    def __init__(self):
        self.json_data = {}
        if request.is_json:
            self.json_data = request.get_json()

    def set_session(self, key, value):
        session[key] = value

    def get_session(self, key):
        return session.get(key)

    def clear_session(self, key):
        session.pop(key, None)
