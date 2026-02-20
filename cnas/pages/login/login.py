from pages.page import page

from components.elements.html import html
from components.elements.body import body
from components.elements.para import para
from components.elements.div import div

from components.elements.button import button

from components.widgets.head_builder import head_builder

class login(page):
    def __init__(self, filename="login.html"):
        super().__init__(filename)

    def __str__(self):
        return self.html
