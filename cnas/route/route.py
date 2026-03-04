from flask import send_from_directory

from pages.base.error import error
from pages.front.front import front

from pages.gallaery.gallery import gallery
from pages.music.music import music
from pages.login.login import login
from pages.test.test_page import test_page

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
    @app.route("/login/api", methods=["POST"])
    def login_page():
        return login().load_scripts().body_content().get_content()

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

    @app.route("/test/api1", methods=['GET', 'POST'])
    @app.route("/test/api2", methods=['GET', 'POST'])
    @app.route("/test")
    def test():
        return test_page().load_scripts().body_content().get_content()
