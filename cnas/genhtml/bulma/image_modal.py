from genhtml.web.tag import tag
from genhtml.web.div import div

__IMAGE_MODAL__=\
"""
<div class="modal-background"></div>
<div class="modal-content">
  <p class="image is-4by3">
    <img id="full_image" src="%s" alt="">
  </p>
</div>
<button class="modal-close is-large" aria-label="close"></button>
"""

class image_modal(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = ""

    def __str__(self):
        return str(div(class_="modal").set_content(
            __IMAGE_MODAL__ % self.url
        ))
