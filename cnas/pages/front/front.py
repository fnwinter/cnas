from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file


class front(page):
    def __init__(self):
        super().__init__()
        super().set_title("Front")
        super().need_login(True)

    @html_file("htmls/front.html")
    def load_scripts(self):
        return self

    def body_content(self):
        self.html = Template(self.html).render(
            title="Welcome",
            content="This is the front page. You can access Gallery, Music, or Test.",
        )
        return self
