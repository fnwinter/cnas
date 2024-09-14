from pages.page import page

from genhtml.w3c.html import html
from genhtml.w3c.head import head
from genhtml.w3c.body import body
from genhtml.w3c.para import para
from genhtml.w3c.div import div

from genhtml.head_builder import head_builder
from genhtml.body_builder import body_builder
from genhtml.navibar_builder import navibar_builder
from genhtml.footer_builder import footer_builder

class error(page):
    def __init__(self, error_message):
        self.error_message = error_message
        pass

    def __str__(self):
        content_style = "'display: flex;justify-content: center;"\
            "align-items: center;text-align: center;height: 75vh;'"
        return str(
            html(
                head_builder(title="Error"),
                body_builder(
                    navibar_builder(),
                    div(
                        div(class_="'notification is-danger'")\
                            .set_content(self.error_message),
                        style=content_style),
                    footer_builder()
                )
            )
        )
