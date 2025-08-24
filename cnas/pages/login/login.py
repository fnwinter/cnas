from pages.page import page

from genhtml.web.html import html
from genhtml.web.body import body
from genhtml.web.para import para
from genhtml.web.div import div

from genhtml.web.button import button

from genhtml.builder.head_builder import head_builder

class login(page):
    def __init__(self):
        pass

    def __str__(self):
        with html(head_builder()) as _html:
            with body() as _body:
                _body.append(para("Login"))
                with div() as _div:
                    _div.append(para("Email"))
                    _div.append(para("Password"))
                    _div.append(button("Login"))
                _body.append(_div)

            _html.append(_body)
            return str(_html)
