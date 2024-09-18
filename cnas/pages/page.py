from flask import request, session

class page:
    def __init__(self):
        self.json_data = None
        if request.is_json:
            self.json_data = request.get_json()

    def set_session(key, value):
        session[key] = value

    def get_session(key):
        return session.get(key)

    def clear_session(key):
        session.pop(key, None)
