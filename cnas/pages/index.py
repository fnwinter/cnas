from pages.page import page

from genhtml.w3c.html import html
from genhtml.w3c.head import head
from genhtml.w3c.body import body
from genhtml.w3c.para import para


class index(page):
    def __init__(self):
        pass

    def __str__(self):
        with html(head()) as _html:
            with body() as _body:
                _body.append(para(content="index"))
            _html.append(_body)
            return str(_html)
