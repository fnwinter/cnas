from genhtml.w3c.head import head
from genhtml.w3c.tag import tag

class photo_builder(tag):
    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})
        image_file = kwargs.get("src")
        file_path = kwargs.get("path")
        self.set_content(
f"""
      <div data-path="{file_path}" class="column is-one-quarter picture">
        <figure class="image is-square">
            <img src="{image_file}" class="rounded" alt="Placeholder image" style="z-index:-1;">
        <div style="overflow: hidden;text-overflow: ellipsis;white-space: wrap;">{file_path}</div>
        </figure>
      </div>
"""
        ).make_element()
