import os
from flask import request, session, jsonify

from components.elements.html import html
from components.widgets.head_widget import head_widget
from components.widgets.navibar_widget import navibar_widget
from components.widgets.body_widget import body_widget

from util.config import CONFIG
from util.hash_string import verify_string

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _collect_rest_api_mapping(cls) -> dict:
    """Collect methods decorated with @rest_call from this class and bases; return {api_path: method_name} dict."""
    mapping = {}
    for c in reversed(cls.__mro__):
        for name, attr in getattr(c, "__dict__", {}).items():
            api_path = getattr(attr, "_rest_api_path", None)
            if callable(attr) and api_path is not None:
                mapping[api_path] = name
    return mapping


class page:
    def __init__(self, filename=None):
        self.rest_api_mapping = _collect_rest_api_mapping(self.__class__)
        self.filename = os.path.join(SCRIPT_DIR, filename) if filename is not None else None
        self.pyscript = ""
        self.api_result = None
        self.json_data = {}
        self._need_login = False
        self._need_admin = False
        if request.is_json:
            self.json_data = request.get_json()
        if self.filename is not None:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.html = "".join(f.readlines())
        else:
            self.html = ""

    def set_title(self, title):
        self.title = title
        return self

    def need_login(self, value: bool):
        """When True, get_content() redirects to /login if user is not logged in."""
        self._need_login = value
        return self

    def need_admin(self, value: bool):
        """When True, get_content() requires the session user to match the admin account.
        Non-admin REST API calls return 403 JSON; page navigation redirects to /login.
        """
        self._need_admin = value
        if value:
            self._need_login = True
        return self

    def _is_admin(self) -> bool:
        """Return True when the logged-in user's email matches the configured admin_id hash."""
        user_email = self.get_session("user_email")
        if not user_email:
            return False
        stored_id_hash = CONFIG.get("admin_id")
        if not stored_id_hash:
            return False
        return verify_string(user_email, stored_id_hash)

    def set_pyscript(self, pyscript):
        self.pyscript = pyscript
        return self

    def set_session(self, key, value):
        session[key] = value

    def get_session(self, key):
        return session.get(key)

    def clear_session(self, key):
        session.pop(key, None)

    def _redirect_to_login(self):
        """Return HTML that redirects to the login page (read from htmls/redirect.html)."""
        redirect_path = os.path.join(SCRIPT_DIR, "htmls", "redirect.html")
        with open(redirect_path, "r", encoding="utf-8") as f:
            return f.read()

    def get_content(self, navibar=True):
        path_key = request.path.lstrip("/")
        is_api = path_key in self.rest_api_mapping

        if getattr(self, "_need_admin", False) and not self._is_admin():
            if is_api:
                return jsonify({"status": "error", "message": "Admin only."}), 403
            return self._redirect_to_login()

        if is_api:
            method_name = self.rest_api_mapping[path_key]
            return getattr(self, method_name)()

        if getattr(self, "_need_login", False) and not self.get_session("user_email"):
            return self._redirect_to_login()

        need_loading = self.pyscript != "" and self.pyscript is not None

        __html = html(
            head_widget(title=self.title),
            navibar_widget().set_auth(self.get_session("user_email") or "") if navibar else None,
            body_widget(need_loading).set_content(
                self.html + self.pyscript))
        return str(__html)
