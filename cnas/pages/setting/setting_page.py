import os

from flask import jsonify, request
from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript
from pages.base.system.rest_call import rest_call

from util.config import CONFIG


class setting_page(page):
    """
    Admin-only setting page.
    Configure folder paths used across CNAS (gallery / music).
    """
    def __init__(self):
        super().__init__()
        super().set_title("Setting")
        super().need_admin(True)

    @html_file("htmls/setting.html")
    @pyscript("setting_pyscript.py")
    def load_scripts(self):
        return self

    @rest_call("setting/api_save_folders")
    def rest_save_folders(self):
        """Validate and persist gallery_path / music_path to CONFIG."""
        data = request.get_json(silent=True) or {}
        gallery_path = (data.get("gallery_path") or "").strip()
        music_path = (data.get("music_path") or "").strip()

        if gallery_path:
            gallery_path = os.path.abspath(os.path.expanduser(gallery_path))
            if not os.path.isdir(gallery_path):
                message = f"Gallery path is not a directory: {gallery_path}"
                return jsonify({"status": "error", "message": message}), 400
            CONFIG.set("gallery_path", gallery_path)

        if music_path:
            music_path = os.path.abspath(os.path.expanduser(music_path))
            if not os.path.isdir(music_path):
                message = f"Music path is not a directory: {music_path}"
                return jsonify({"status": "error", "message": message}), 400
            CONFIG.set("music_path", music_path)

        CONFIG.save()
        return jsonify({
            "status": "ok",
            "message": "Saved.",
            "gallery_path": CONFIG.get("gallery_path") or "",
            "music_path": CONFIG.get("music_path") or "",
        }), 200

    def body_content(self):
        return self.set_body_html(Template(self.html).render(
            title="Setting",
            content="Configure folder paths used by CNAS features.",
            gallery_path=CONFIG.get("gallery_path") or "",
            music_path=CONFIG.get("music_path") or "",
        ))
