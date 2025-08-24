from pages.page import page

from genhtml.web.html import html
from genhtml.web.body import body
from genhtml.web.para import para
from genhtml.web.div import div

from genhtml.web.button import button

from genhtml.builder.head_builder import head_builder

class login(page):
    def __init__(self, filename="login.html"):
        super().__init__(filename)

    def __str__(self):
        return self.html
