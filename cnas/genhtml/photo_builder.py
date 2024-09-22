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

        display = "display:visible;"\
            if file_style == "folder" else "display:none;"

        div_id = f"photo{photo_builder.div_id}"\
            if file_style != "folder" else ""

        class_type = "folder" if file_style == "folder" else "picture"

        self.set_content(
f"""
<div data-target="{div_id}" data-path="{file_path}" class="column is-one-quarter {class_type} hoverArea modal-button js-modal-trigger">
  <figure class="image is-square div-bottom">
    <img src="{image_file}" class="rounded" style="z-index:-1;">
    <div id="{div_id}" class="box is-align-content-center"
      style="{display} width:100%; background-color:rgba(0,0,0,0.6);">
      <div class="center-text">{file_path}</div>
    </div>
  </figure>
</div>
"""
        ).make_element()
