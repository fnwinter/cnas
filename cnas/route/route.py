from flask import send_from_directory

from pages.system.index import index
from pages.system.error import error

from pages.gallaery.gallery import gallery
from pages.music.music import music
from pages.login.login import login
from pages.login.login_api import login_api
from pages.test.test_page import test_page

from util.config import CONFIG
from util.system_path import get_gallery_thumbnail_path

def route(app):
    """
    System pages
    Index / Error / Unknown request page

    """
    @app.route("/")
    def index_page() -> str:
        return str(index())

    @app.route("/error")
    def error_page() -> str:
        return str(error("error page"))

    @app.route("/login")
    @app.route("/login/api", methods=['POST'])
    def login_page() -> str:
        return str(login())

    @app.route("/login_api", methods=['POST'])
    def login_api_page():
        return login_api().check_login()

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

    @app.route("/test")
    @app.route("/test/api", methods=['POST'])
    def test() -> str:
        return str(test_page())
