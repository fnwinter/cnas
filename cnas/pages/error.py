from pages.page import page

from genhtml.web.html import html
from genhtml.web.div import div

from genhtml.builder.head_builder import head_builder
from genhtml.builder.body_builder import body_builder
from genhtml.builder.navibar_builder import navibar_builder
from genhtml.builder.footer_builder import footer_builder

__ERROR_MSG__ =\
"""
<article class="message is-danger">
  <div class="message-header">
    <p>Danger</p>
    <button class="delete" aria-label="delete"></button>
  </div>
  <div class="message-body">
  %s
  </div>
</article>
"""

__CONTENT_STYLE__ = "display: flex;justify-content: center;"\
"align-items: center;text-align: center;height: 78vh;"

class error(page):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        msg = __ERROR_MSG__ % self.error_message

        return str(
            html(
                head_builder(title="Error"),
                body_builder(
                    navibar_builder(),
                    div(
                        div()
                            .set_content(msg),
                    style=__CONTENT_STYLE__),
                    footer_builder()
                )
            )
        )
