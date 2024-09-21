from genhtml.w3c.tag import tag

class photo_builder(tag):
    div_id = 0

    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})

        image_file = kwargs.get("src")
        file_path = kwargs.get("path")
        file_style = kwargs.get("style")

        photo_builder.div_id += 1

        init_display = "display:visible;"\
            if file_style == "folder" else "display:none;"

        div_id = f"photo{photo_builder.div_id}"\
            if file_style != "folder" else ""

        self.set_content(
f"""
<div data-target="{div_id}" data-path="{file_path}" class="column is-one-quarter picture hoverArea">
  <figure class="image is-square" style="align-items:flex-end; display:flex;">
    <img src="{image_file}" class="rounded" style="z-index:-1;">
    <div
      id="{div_id}"
      class="box is-align-content-center file_name"
      style="{init_display} width:100%; overflow:hidden; text-overflow:ellipsis; white-space:wrap; background-color:rgba(0, 0, 0, 0.6);">
      {file_path}
    </div>
  </figure>
</div>
"""
        ).make_element()
