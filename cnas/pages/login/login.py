from pages.page import page

from components.web.html import html
from components.web.body import body
from components.web.para import para
from components.web.div import div

from components.web.button import button

from components.builder.head_builder import head_builder

class login(page):
    def __init__(self, filename="login.html"):
        super().__init__(filename)

    def __str__(self):
        return self.html
