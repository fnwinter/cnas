import os

from jinja2 import Template

from pages.base.page import page

from util.file_util import is_image_file
from util.config_path import get_gallery_path
from util.system_path import get_gallery_thumbnail_path
from util.path_util import rel_path

from components.elements.section import section
from components.elements.div import div
from components.elements.para import para
from components.elements.br import br

from components.widgets.photo_widget import photo_widget

from components.widgets.image_widget import image_widget

__GALLERY_TEMPLATE__ = """
{{ content }}
{{ modal }}
"""


class gallery(page):
    """
    Gallery page for browsing images from the configured gallery path.
    """
    def __init__(self):
        super().__init__()
        super().set_title("Gallery")
        self.files = []

        gallery_path = get_gallery_path()
        self.gallery_path = os.path.abspath(gallery_path) if gallery_path else ""
        self.thumbnail_path = get_gallery_thumbnail_path()
        session_path = self.get_session("current_path")
        self.current_path = session_path if isinstance(session_path, str) else self.gallery_path
        self.r_path = "."

        self.set_current_path()
        self.get_files()

    def set_current_path(self):
        if not self.gallery_path or not os.path.isdir(self.gallery_path):
            self.current_path = ""
            return
        if not self.current_path:
            self.current_path = self.gallery_path
        if not rel_path(self.current_path, self.gallery_path):
            self.current_path = self.gallery_path
        if not os.path.exists(self.current_path):
            self.current_path = self.gallery_path
        if not os.path.isdir(self.current_path):
            self.current_path = self.gallery_path
        if not self.json_data.get("path"):
            return

        _path = self.json_data.get("path")
        if not isinstance(_path, str):
            return
        _full = os.path.abspath(os.path.join(self.current_path, _path))

        if os.path.isdir(_full):
            self.current_path = _full
            self.set_session("current_path", _full)

    def get_files(self):
        if not self.current_path or not os.path.isdir(self.current_path):
            return
        self.r_path = rel_path(self.current_path, self.gallery_path)
        if not self.r_path:
            self.r_path = "."

        if self.current_path != self.gallery_path:
            self.files.append(
                photo_widget(
                    src="static/images/up.png",
                    path="..", type_="folder"))

        # folder
        for _folder in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _folder)
            if os.path.isdir(_path):
                self.files.append(
                    photo_widget(
                        src="static/images/folder.png",
                        path=_folder,
                        type_="folder"))

        # images
        for _file in os.listdir(self.current_path):
            if not is_image_file(_file):
                continue
            _rel_file = os.path.join(self.r_path, _file)
            _thumb_nail_path = os.path.join(self.thumbnail_path, _rel_file)

            if os.path.exists(_thumb_nail_path):
                self.files.append(
                    photo_widget(
                        src="gallery_thumbnail/" + _rel_file,
                        path=_file,
                        type_="picture"))
            else:
                self.files.append(
                    photo_widget(src="static/images/no_cache.png"))

    def load_scripts(self):
        return self

    def body_content(self):
        _title_div = div(
            para(class_="title is-1 is-spaced").set_content("Gallery"),
            para(class_="subtitle is-3").set_content(f"/gallery/{self.r_path}"),
            br()
        )

        _div = div(class_="columns is-multiline")
        _div.append(
            div(id="rel_path", data_path=f"{self.r_path}"))

        for _file in self.files:
            _div.append(_file)

        _section = section(
            div(_title_div, class_="container").append(_div),
            class_="section")

        _modal = image_widget()

        self.html = Template(__GALLERY_TEMPLATE__).render(
            content=str(_section),
            modal=str(_modal),
        )
        return self

    def __str__(self):
        return self.load_scripts().body_content().get_content()
