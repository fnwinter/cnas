import os
from flask import   request, session

from components.elements.html import html
from components.widgets.head_widget import head_widget
from components.widgets.body_widget import body_widget

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _collect_rest_api_mapping(cls) -> dict:
    """Collect methods decorated with @rest_call from this class and bases; return {api_path: method_name} dict."""
    mapping = {}
    for c in reversed(cls.__mro__):
        for name, attr in getattr(c, "__dict__", {}).items():
            if callable(attr) and getattr(attr, "_rest_api_path", None) is not None:
                mapping[attr._rest_api_path] = name
    return mapping


class page:
    def __init__(self, filename = None):
        self.rest_api_mapping = _collect_rest_api_mapping(self.__class__)
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

    def set_title(self, title):
        self.title = title
        return self

    def set_pyscript(self, pyscript):
        self.pyscript = pyscript
        return self

    def set_session(self, key, value):
        session[key] = value

    def get_session(self, key):
        return session.get(key)

    def clear_session(self, key):
        session.pop(key, None)

    def get_content(self):
        path_key = request.path.lstrip("/")
        if path_key in self.rest_api_mapping:
            method_name = self.rest_api_mapping[path_key]
            return getattr(self, method_name)()

        __html = html(
            head_widget(title=self.title),
            body_widget(
            ).set_content(
                self.html +
                self.pyscript
            )
        )
        return str(__html)