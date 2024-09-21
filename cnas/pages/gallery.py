import os

from pages.page import page
from pages.error import error

from util.file_util import is_image_file
from util.config_path import get_gallery_path
from util.system_path import get_gallery_thumbnail_path
from util.path_util import rel_path

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
        self.files = []

        self.gallery_path = get_gallery_path()
        self.thumbnail_path = get_gallery_thumbnail_path()
        self.current_path = self.get_session("current_path")

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
        if self.current_path != self.gallery_path:
            self.files.append(
                photo_builder(
                    src="static/images/up.png",
                    path="..", style="folder"))

        # folder
        for _folder in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _folder)
            if os.path.isdir(_path):
                self.files.append(
                    photo_builder(
                        src="static/images/folder.png",
                        path=_folder,
                        style="folder"))

        # images
        for _file in os.listdir(self.current_path):
            if not is_image_file(_file):
                continue
            _rel_path = rel_path(self.current_path, self.gallery_path)
            _rel_file = os.path.join(_rel_path, _file)
            _thumb_nail_path = os.path.join(self.thumbnail_path, _rel_file)

            if os.path.exists(_thumb_nail_path):
                self.files.append(
                    photo_builder(
                        src="gallery_thumbnail/" + _rel_file,
                        path=_file))
            else:
                self.files.append(
                    photo_builder(src="static/images/no_cache.png"))
 

    def __str__(self):
        _rel_path = rel_path(self.current_path, self.gallery_path)

        _title_div = div(
            para(class_="'title is-1 is-spaced'").set_content("Gallery"),
            para(class_="'subtitle is-3'").set_content(f"/root/{_rel_path}"),
            br()
        )

        _div = div(class_="'columns is-multiline'")

        for _file in self.files:
            _div.append(_file)

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
