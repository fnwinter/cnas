from pages.base.page import page
from pages.base.system.html import html_file


class trac_page(page):
    """
    Trac page for embedding the self-hosted Trac project management tool.
    Renders an iframe that points to the reverse-proxied Trac endpoint
    (see /trac_proxy/* routes in route.py), so that requests arriving on
    the CNAS HTTP port are transparently forwarded to the Trac server.
    """
    def __init__(self):
        super().__init__()
        super().set_title("Trac")
        super().need_login(True)

    @html_file("htmls/trac.html")
    def load_scripts(self):
        return self

    def body_content(self):
        return self
