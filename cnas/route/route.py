from flask import send_from_directory

from pages.index import index
from pages.error import error

from pages.gallery import gallery
from pages.music import music

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

    """
    Gallery page
    """
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

    """
    Music page
    """
    @app.route("/music")
    def music_page() -> str:
        return str(music())
