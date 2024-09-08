import os

from pages.page import page
from util.config import CONFIG

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
        pass

    def __str__(self):
        _path_div = div(
            para(class_="'title is-1 is-spaced'").set_content("Gallery"),
            para(class_="'subtitle is-3'").set_content("/root"),
            br()
        )
 
        _div = div(
            class_="'columns is-multiline'"
        )
 
        _div.append(
            photo_builder(src="static/images/up.png")
        )

        _gallery_path = CONFIG.get("gallery_path")
        for root,dirs,files in os.walk(_gallery_path):
            for f in files:
              if "jpg" == f[-3:]:
                      _div.append(
                          photo_builder(src="gallery_file/" + f)
                          )

        _section = section(
            div(_path_div, class_="container").append(_div),
            class_="section")

        return str(
            html(
                head_builder(title="Gallery"),
                body_builder(
                    navibar_builder(),
                    _section,
                    footer_builder()
                )
            )
        )
