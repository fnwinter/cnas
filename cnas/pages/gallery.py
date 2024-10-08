import os

from pages.page import page
from pages.error import error

from util.file_util import is_image_file
from util.config_path import get_gallery_path
from util.system_path import get_gallery_thumbnail_path
from util.path_util import rel_path

from genhtml.web.html import html
from genhtml.web.section import section
from genhtml.web.div import div
from genhtml.web.para import para
from genhtml.web.br import br

from genhtml.builder.head_builder import head_builder
from genhtml.builder.body_builder import body_builder
from genhtml.builder.navibar_builder import navibar_builder
from genhtml.builder.photo_builder import photo_builder
from genhtml.builder.footer_builder import footer_builder

from genhtml.bulma.image_modal import image_modal

class gallery(page):
    def __init__(self):
        super().__init__()
        self.files = []

        self.gallery_path = get_gallery_path()
        self.thumbnail_path = get_gallery_thumbnail_path()
        self.current_path = self.get_session("current_path")
        self.r_path = "."

        self.set_current_path()
        self.get_files()

    def set_current_path(self):
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
        _full = os.path.abspath(os.path.join(self.current_path, _path))

        if os.path.isdir(_full):
            self.current_path = _full
            self.set_session("current_path", _full)

    def get_files(self):
        self.r_path = rel_path(self.current_path, self.gallery_path)

        if self.current_path != self.gallery_path:
            self.files.append(
                photo_builder(
                    src="static/images/up.png",
                    path="..", type_="folder"))

        # folder
        for _folder in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _folder)
            if os.path.isdir(_path):
                self.files.append(
                    photo_builder(
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
                    photo_builder(
                        src="gallery_thumbnail/" + _rel_file,
                        path=_file,
                        type_="picture"))
            else:
                self.files.append(
                    photo_builder(src="static/images/no_cache.png"))
 

    def __str__(self):
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

        _modal = image_modal()

        return str(
            html(
                head_builder(title="Gallery"),
                body_builder(
                    navibar_builder().set_menu({
                        "Create Folder":"",
                        "-":"divider",
                        "Select":"/",
                        "Deselect":"",
                        "Delete":"",
                        "--":"divider",
                        "Download":"",
                        "Upload":"",
                      }),
                    _section,
                    _modal,
                    footer_builder()
                )
            )
        )
