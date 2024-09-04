from pages.page import page
from util.config import CONFIG


class gallery(page):
    def __init__(self):
        pass

    def __str__(self):
        return f"image {CONFIG.get('gallery_path')}"
