from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file
from pages.base.system.pyscript import pyscript


class file_manager_page(page):
    """
    File manager page for browsing files and performing
    copy / move / rename / delete operations on the NAS storage.
    """
    def __init__(self):
        super().__init__()
        super().set_title("File manager")

    @html_file("htmls/file_manager.html")
    @pyscript("file_manager_pyscript.py")
    def load_scripts(self):
        return self

    def body_content(self):
        self.html = Template(self.html).render(
            title="File manager",
            content="Browse and manage files on the NAS storage.",
        )
        return self
