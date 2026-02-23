import os

from pages.page import page

from util.config_path import get_music_path

from components.elements.html import html
from components.elements.section import section
from components.elements.div import div
from components.elements.para import para
from components.elements.br import br

from components.widgets.head_builder import head_builder
from components.widgets.body_builder import body_builder
from components.widgets.navibar_builder import navibar_builder
from components.widgets.music_builder import music_builder
from components.widgets.footer_builder import footer_builder

from components.widgets.image_modal import image_modal

__MUSIC_TEST__ =\
"""
    <audio id='music_player'>
        <source src="/music_file/Daft Punk_Contact.MP3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
"""

class music(page):
    def __init__(self):
        self.music_path = get_music_path()

    def __str__(self):
        _title_div = div(
            para(class_="title is-1 is-spaced").set_content("Music"),
            para(class_="subtitle is-3").set_content("/music/path"),
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

        for __file in os.listdir(self.music_path):
            __path = os.path.join(self.music_path, __file)
            print(f"{__file}")
            if os.path.isdir(__path):
                print("album")
            else:
                print("file")

        _section = section(
            div(_title_div, class_="container").append(_div),
            class_="section")

        _modal = image_modal()
        __music = div()
        __music.set_content(__MUSIC_TEST__)

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
                    __music,
                    footer_builder()
                )
            )
        )
