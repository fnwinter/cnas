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
from genhtml.music_builder import music_builder

from genhtml.footer_builder import footer_builder

from genhtml.bulma.image_modal import image_modal


class music(page):
    def __init__(self):
        pass

    def __str__(self):
        _title_div = div(
            para(class_="title is-1 is-spaced").set_content("Music"),
            para(class_="subtitle is-3").set_content(f"/music/path"),
            br()
        )

        _div = div(class_="columns is-multiline")
        _div.append(music_builder())
        _div.append(music_builder())
        _div.append(music_builder())
        _div.append(music_builder())
        _div.append(music_builder())
        _div.append(music_builder())
        _div.append(music_builder())

        _section = section(
            div(_title_div, class_="container").append(_div),
            class_="section")

        _modal = image_modal()

        return str(
            html(
                head_builder(title="Music"),
                body_builder(
                    navibar_builder().set_menu({
                        "Playlist":"",
                        "":"",
                        "Create folder":"",
                        "Upload files":"",
                        "Delete":""
                      }),
                    _section,
                    _modal,
                    footer_builder()
                )
            )
        )
