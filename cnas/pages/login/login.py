from pages.page import page
from pages.system.pyscript import pyscript

from components.elements.html import html
from components.elements.body import body
from components.elements.para import para
from components.elements.div import div

from components.elements.button import button

from components.widgets.head_widget import head_widget

class login(page):
    def __init__(self, filename="login/htmls/login.html"):
        super().__init__(filename)

    @pyscript("login_pyscript.py")
    def __str__(self):
        return ""
