from genhtml.w3c.tag import tag

class photo_builder(tag):
    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})

        image_file = kwargs.get("src")
        file_path = kwargs.get("path")
        file_type = kwargs.get("type")

        self.set_content(
f"""
<div data-path="{file_path}" class="column is-one-quarter picture">
  <figure class="image is-square" style="align-items:flex-end; display:flex;">
    <img src="{image_file}" class="rounded" style="z-index:-1;">
    <div
      class="box is-align-content-center"
      style="width:100%; overflow:hidden; text-overflow:ellipsis; white-space:wrap; background-color:rgba(0, 0, 0, 0.6);">
      {file_path}
    </div>
  </figure>
</div>
"""
        ).make_element()
