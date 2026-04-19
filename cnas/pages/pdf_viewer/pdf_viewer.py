from pages.base.page import page
from pages.base.system.html import html_file


class pdf_viewer_page(page):
    def __init__(self):
        super().__init__()
        super().set_title("PDF viewer")

    @html_file("htmls/pdf_viewer.html")
    def load_scripts(self):
        return self

    def body_content(self):
        return self
