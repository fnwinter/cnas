from pages.page import page
from util.config import CONFIG

from genhtml.w3c.html import html
from genhtml.head_builder import head_builder
from genhtml.body_builder import body_builder

class gallery(page):
    def __init__(self):
        pass

    def __str__(self):
        return str(\
            html(\
                head_builder("Gallery"),
                body_builder(\
                )\
                )\
            )
