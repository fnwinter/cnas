import os

from pages.page import page
from util.config import CONFIG

from genhtml.w3c.html import html
from genhtml.w3c.section import section
from genhtml.w3c.div import div

from genhtml.head_builder import head_builder
from genhtml.body_builder import body_builder
from genhtml.navibar_builder import navibar_builder
from genhtml.photo_builder import photo_builder

class gallery(page):
    def __init__(self):
        pass

    def __str__(self):
        _d = div(_class="'columns is-multiline'")
        _d.append(
            photo_builder(src="static/images/up.png"))

        _gallery_path = CONFIG.get("gallery_path")
        for root,dirs,files in os.walk(_gallery_path):
            for f in files:
              if "jpg" == f[-3:]:
                      _d.append(
                          photo_builder(src="gallery_file/" + f)
                          )

        _s = section(
            div(class_="container").append(_d),
            class_="section")

        return str(
            html(
                head_builder(title="Gallery"),
                body_builder(
                    navibar_builder(),
                    _s
                )
            )
        )
