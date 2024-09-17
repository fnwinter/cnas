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

    def __str__(self):
        if self.json_data:
            print(self.json_data.get("path"))

        _gallery_path = get_gallery_path()
        if _gallery_path is None or not os.path.exists(_gallery_path):
            return str(error("No gallery path"))

        _title_div = div(
            para(class_="'title is-1 is-spaced'").set_content("Gallery"),
            para(class_="'subtitle is-3'").set_content("/root"),
            br()
        )

        _div = div(
            photo_builder(src="static/images/up.png", path=".."),
            class_="'columns is-multiline'"
        )

        for _f in os.listdir(_gallery_path):
            _path = os.path.join(_gallery_path, _f)
            if not os.path.isdir(_path):
                continue
            _div.append(
                photo_builder(
                    src="static/images/folder.png",
                    path=_path))

        for _f in os.listdir(_gallery_path):
            _path = os.path.join(_gallery_path, _f)
            if not os.path.isfile(_path) and is_image_file(_f):
                _div.append(
                    photo_builder(src="static/images/no_cache.png"))
                continue
            if is_image_file(_f):
                _div.append(
                    photo_builder(
                        src="gallery_file/" + _f,
                        path=_path))

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
