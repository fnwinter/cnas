from pages.page import page

from genhtml.w3c.html import html
from genhtml.w3c.body import body
from genhtml.w3c.para import para
from genhtml.w3c.div import div

from genhtml.w3c.script import script
from genhtml.w3c.button import button

from genhtml.head_builder import head_builder

class music(page):
    def __init__(self):
        pass

    def __str__(self):
        with html(head_builder()) as _html:
            with body() as _body:
                _body.append(para(content="index"))
                _body.append(
                    script(
                        type_="py",
                        src="static/main.py",
                        config="static/pyscript.toml"
                    )
                )
                _body.append(
                    button(
                        id_="get_joke",
                        py_click="get_joke"
                    ).set_content("button")
                )
                _body.append(
                    div(
                        id_="jokes"
                    )
                )

            _html.append(_body)
            return str(_html)
