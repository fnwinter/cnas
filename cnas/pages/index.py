from pages.page import page

from genhtml.html import html
from genhtml.head import head
from genhtml.body import body
from genhtml.image import image


class index(page):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        with html(head(cnas_title="cnas")) as _html:
            with body(image()) as _body:
                _body.append(image())
            _html.append(_body)
            return str(_html)
