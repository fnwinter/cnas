from pages.page import page

from components.elements.html import html
from components.elements.div import div

from components.widgets.head_widget import head_widget
from components.widgets.body_widget import body_widget
from components.widgets.navibar_widget import navibar_widget
from components.widgets.footer_widget import footer_widget

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
                head_widget(title="Error"),
                body_widget(
                    navibar_widget(),
                    div(
                        div()
                            .set_content(msg),
                    style=__CONTENT_STYLE__),
                    footer_widget()
                )
            )
        )
