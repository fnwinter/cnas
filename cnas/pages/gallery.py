import os

from pages.page import page
from pages.error import error

from util.file_util import is_image_file
from util.config_path import get_gallery_path
from util.system_path import get_gallery_thumbnail_path

from genhtml.w3c.html import html
from genhtml.w3c.section import section
from genhtml.w3c.div import div
from genhtml.w3c.para import para
from genhtml.w3c.br import br

from genhtml.head_builder import head_builder
from genhtml.body_builder import body_builder
from genhtml.navibar_builder import navibar_builder
from genhtml.photo_builder import photo_builder
from genhtml.footer_builder import footer_builder

class gallery(page):
    def __init__(self):
        super().__init__()
        self.pictures = []

        self.gallery_path = get_gallery_path()
        self.thumbnail_path = get_gallery_thumbnail_path()
        self.current_path = self.get_session("current_path")
        if not self.current_path:
            self.current_path = self.gallery_path
        if not os.path.abspath(self.gallery_path) in\
            os.path.abspath(self.current_path):
            self.current_path = self.gallery_path

        self.get_path()
        self.get_list()

    def get_path(self):
        if self.json_data and self.json_data.get("path"):
            _rel_path = self.json_data.get("path")
            _full = os.path.join(self.current_path, _rel_path)
            self.set_session("current_path", os.path.abspath(_full))
            print(_full)
            print(_rel_path)

    def get_list(self):
        # folder
        for _folder in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _folder)
            if os.path.isdir(_path):
                self.pictures.append(
                    photo_builder(
                        src="static/images/folder.png",
                        path=_folder))

        # images
        for _file in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _file)
            if not is_image_file(_file):
                continue

            _rel_path = os.path.relpath(self.current_path, self.gallery_path)
            _rel_full = os.path.join(_rel_path, _file)
            _thumb_nail_path = os.path.join(self.thumbnail_path, _rel_path)

            if os.path.exists(_thumb_nail_path):
                self.pictures.append(
                    photo_builder(
                        src="gallery_thumbnail/" + _rel_full,
                        path=_file))
            else:
                self.pictures.append(
                    photo_builder(src="static/images/no_cache.png"))
 

    def __str__(self):
        _title_div = div(
            para(class_="'title is-1 is-spaced'").set_content("Gallery"),
            para(class_="'subtitle is-3'").set_content("/root"),
            br()
        )

        _div = div(
            photo_builder(src="static/images/up.png", path=".."),
            class_="'columns is-multiline'"
        )

        for pic in self.pictures:
            _div.append(pic)

        _section = section(
            div(_title_div, class_="container").append(_div),
            class_="section")

        return str(
            html(
                head_builder(title="Gallery"),
                body_builder(
                    navibar_builder().set_menu({
                        "Create Folder":"",
                        "Select":"/",
                        "Deselect":"",
                        "Delete":"",
                        "Download":"",
                        "Upload":"",
                      }),
                    _section,
                    footer_builder()
                )
            )
        )
