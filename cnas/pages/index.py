from pages.page import page

from genhtml.web.html import html
from genhtml.web.body import body
from genhtml.web.para import para
from genhtml.web.div import div

from genhtml.web.script import script
from genhtml.web.button import button

from genhtml.head_builder import head_builder

class index(page):
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
