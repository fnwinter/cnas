from flask import jsonify, request, session, redirect

from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call

from util.config import CONFIG
from util.hash_string import verify_string


class login(page):
    def __init__(self):
        super().__init__()
        super().set_title("Login")

    @html_file("htmls/login.html")
    @pyscript("login_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("login/login")
    def post_login(self):
        """Accept id/password, verify against config admin_id/admin_password (hash_string), set session on success."""
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "No request data."}), 200

        id_val = (data.get("id") or "").strip()
        password_val = data.get("password") or ""

        if not id_val or not password_val:
            return jsonify({"success": False, "message": "Please enter both ID and password."}), 200

        if not self._verify_admin(id_val, password_val):
            return jsonify({"success": False, "message": "Invalid ID or password."}), 200

        self.set_session("user_email", id_val)
        return jsonify({"success": True, "message": "Login successful."}), 200

    @rest_call("login/logout")
    def post_logout(self):
        """Clear session and redirect to login page."""
        session.clear()
        return redirect("/login")

    def _verify_admin(self, id_val: str, password_val: str) -> bool:
        """Compare id/password with config admin_id/admin_password using hash_string (verify_string)."""
        stored_id_hash = CONFIG.get("admin_id")
        stored_password_hash = CONFIG.get("admin_password")
        if not stored_id_hash or not stored_password_hash:
            return False
        return verify_string(id_val, stored_id_hash) and verify_string(password_val, stored_password_hash)

    def body_content(self):
        self.html = Template(self.html).render()
        return self
