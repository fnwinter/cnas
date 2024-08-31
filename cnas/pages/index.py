from pages.page import page

from genhtml.html import html
from genhtml.head import head
from genhtml.body import body
from genhtml.paragraph import p


class index(page):
    def __init__(self):
        pass

    def __str__(self):
        with html(head(cnas_title="cnas")) as _html:
            with body() as _body:
                _body.append(p(cnas_text="index"))
            _html.append(_body)
            return str(_html)
