from flask import send_from_directory
from flask import request, Response

from pages.base.error import error
from pages.front.front import front

from pages.gallaery.gallery import gallery
from pages.music.music import music
from pages.login.login import login
from pages.login.lost_pwd import lost_pwd
from pages.storage_status.storage_status_page import storage_status_page
from pages.system_status.system_status_page import system_status_page
from pages.minecraft.minecraft_page import minecraft_page
from pages.test.test_page import test_page
from pages.pdf_viewer.pdf_viewer import pdf_viewer_page

from util.config import CONFIG
from util.system_path import get_gallery_thumbnail_path

def route(app):
    """
    System pages
    Index / Error / Unknown request page

    """
    @app.route("/")
    def index_page():
        return front().load_scripts().body_content().get_content()

    @app.route("/error")
    def error_page() -> str:
        return str(error("error page"))

    @app.route("/login")
    @app.route("/login/login", methods=["POST"])
    @app.route("/login/logout", methods=["POST"])
    def login_page():
        return login().load_scripts().body_content().get_content(navibar=False)

    @app.route("/lost_pwd")
    def lost_pwd_page():
        return lost_pwd().load_scripts().body_content().get_content(navibar=False)

    @app.route("/gallery", methods=['GET', 'POST'])
    def gallery_page() -> str:
        return str(gallery())

    @app.route('/gallery_file/<path:filename>')
    def gallery_file(filename):
        directory = CONFIG.get('gallery_path')
        return send_from_directory(directory, filename)

    @app.route('/gallery_thumbnail/<path:filename>')
    def gallery_thumbnail(filename):
        directory = get_gallery_thumbnail_path()
        return send_from_directory(directory, filename)

    @app.route("/music")
    def music_page() -> str:
        return str(music())

    @app.route('/music_file/<path:filename>')
    def music_file(filename):
        directory = CONFIG.get('music_path')
        return send_from_directory(directory, filename)

    @app.route("/system_status/api_mdstat", methods=["GET", "POST"])
    @app.route("/system_status/api_ps_aux", methods=["GET", "POST"])
    @app.route("/system_status")
    def system_status():
        return system_status_page().load_scripts().body_content().get_content()

    @app.route("/storage_status/api_df_h", methods=["GET", "POST"])
    @app.route("/storage_status")
    def storage_status():
        return storage_status_page().load_scripts().body_content().get_content()

    @app.route("/minecraft/api_run", methods=["GET", "POST"])
    @app.route("/minecraft")
    def minecraft():
        return minecraft_page().load_scripts().body_content().get_content()

    @app.route("/test/api1", methods=['GET', 'POST'])
    @app.route("/test/api2", methods=['GET', 'POST'])
    @app.route("/test/api_command", methods=['GET', 'POST'])
    @app.route("/test")
    def test():
        return test_page().load_scripts().body_content().get_content()

    @app.route("/pdf_viewer")
    def pdf_viewer():
        return pdf_viewer_page().load_scripts().body_content().get_content()

    @app.route("/trac")
    @app.route("/trac/<path:subpath>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
    def proxy(subpath = None):
        TARGET_HOST = "http://127.0.0.1:8080"
        target_url =  f"{TARGET_HOST}/{subpath}" if subpath else f"{TARGET_HOST}/"
        headers = {k: v for k, v in request.headers if k.lower() != "host"}
        import requests
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=request.args.to_dict(),
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            stream=True,
        )
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        response_headers = [
            (name, value) for name, value in resp.raw.headers.items()
            if name.lower() not in excluded_headers
        ]
        return Response(resp.content, resp.status_code, response_headers)