from genhtml.w3c.head import head
from genhtml.w3c.tag import tag

class photo_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__([], {})
        image_file = kwargs.get("src")
        self.set_content(
f"""
      <div class="column is-one-quarter">
        <figure class="image is-square">
            <img src="{image_file}" alt="Placeholder image">
        </figure>
      </div>
"""
        ).make_element()
