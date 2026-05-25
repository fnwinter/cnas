import requests
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
from pages.file_manager.file_manager_page import file_manager_page
from pages.setting.setting_page import setting_page
from pages.trac.trac_page import trac_page

from util.config import CONFIG
from util.system_path import get_gallery_thumbnail_path

TRAC_TARGET_HOST = "http://192.168.29.205:8080/"
TRAC_PROXY_TIMEOUT = 30


def _trac_proxy_response(subpath: str):
    # Reverse proxy to the local Trac server. Requests hitting /trac/*
    # on the CNAS port are forwarded to TARGET_HOST and the response is
    # streamed back to the original client.
    target_url = f"{TRAC_TARGET_HOST}/trac/{subpath}" if subpath else f"{TRAC_TARGET_HOST}/trac"
    headers = {k: v for k, v in request.headers if k.lower() != "host"}
    resp = requests.request(
        method=request.method,
        url=target_url,
        headers=headers,
        params=request.args.to_dict(),
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=True,
        timeout=TRAC_PROXY_TIMEOUT,
    )
    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    response_headers = [
        (name, value) for name, value in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]
    return Response(resp.content, resp.status_code, response_headers)


def _register_system_routes(app):
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


def _register_media_routes(app):
    @app.route("/gallery", methods=['GET', 'POST'])
    def gallery_page() -> str:
        return gallery().load_scripts().body_content().get_content()

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


def _register_status_routes(app):
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


def _register_feature_routes(app):
    @app.route("/test/api1", methods=['GET', 'POST'])
    @app.route("/test/api2", methods=['GET', 'POST'])
    @app.route("/test/api_command", methods=['GET', 'POST'])
    @app.route("/test")
    def test():
        return test_page().load_scripts().body_content().get_content()

    @app.route("/pdf_viewer")
    def pdf_viewer():
        return pdf_viewer_page().load_scripts().body_content().get_content()

    @app.route("/file_manager")
    def file_manager():
        return file_manager_page().load_scripts().body_content().get_content()

    @app.route("/setting/api_save_folders", methods=["POST"])
    @app.route("/setting")
    def setting():
        return setting_page().load_scripts().body_content().get_content()

    @app.route("/trac_proxy")
    def trac():
        return trac_page().load_scripts().body_content().get_content()

    @app.route("/trac", defaults={"subpath": ""})
    @app.route("/trac/<path:subpath>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
    def trac_proxy(subpath: str):
        return _trac_proxy_response(subpath)


def route(app):
    """
    System pages
    Index / Error / Unknown request page

    """
    _register_system_routes(app)
    _register_media_routes(app)
    _register_status_routes(app)
    _register_feature_routes(app)
