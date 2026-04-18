from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file


class lost_pwd(page):
    def __init__(self):
        super().__init__()
        super().set_title("Lost Password")

    @html_file("htmls/lost_pwd.html")
    def load_scripts(self):
        return self

    def body_content(self):
        self.html = Template(self.html).render()
        return self
