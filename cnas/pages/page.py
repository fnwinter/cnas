from flask import request

class page:
    def __init__(self):
        self.json_data = None
        if request.is_json:
            self.json_data = request.get_json()
