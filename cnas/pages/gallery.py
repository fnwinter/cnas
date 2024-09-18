import os

from pages.page import page
from pages.error import error

from util.file_util import is_image_file
from util.config_path import get_gallery_path

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

    def get_path(self):
        _gallery_path = None
        if self.json_data and self.json_data.get("path"):
            _gallery_path = self.json_data.get("path")
        else:
          _gallery_path = get_gallery_path()
        print(_gallery_path)

        if _gallery_path is None or not os.path.exists(_gallery_path):
            return str(error("No gallery path"))

    def get_list(self):
        # folder
        for _folder in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _folder)
            if os.path.isdir(_path):
                _div.append(
                    photo_builder(
                        src="static/images/folder.png",
                        path=_folder))

        # images
        for _file in os.listdir(self.current_path):
            _path = os.path.join(self.current_path, _file)
            _rel_path = ""
            _thumb_nail_path = ""
            if not is_image_file(_file):
                continue
            if not os.path.exists(_path):
                continue
            if os.path.exist(_thumb_nail_path):
                _div.append(
                    photo_builder(
                        src="gallery_thumbnail/" + _rel_path,
                        path=_file))
            else:
                _div.append(
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
