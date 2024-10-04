from genhtml.w3c.tag import tag
from genhtml.w3c.figure import figure
from genhtml.w3c.div import div
from genhtml.w3c.image import image

class photo_builder(tag):
    auto_index = 0

    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})

        photo_builder.auto_index += 1

        image_file = kwargs.get("src")
        file_path = kwargs.get("path")
        file_type = kwargs.get("type_")

        div_id = ""
        if file_type == "folder":
            display_class = "display:visible;"
        else:
            div_id = f"photo_{photo_builder.auto_index}"
            display_class = "display:none;"

        _div = div(
            figure(
                image(
                    src=f"{image_file}",
                    style="z-index:-1;",
                    class_="rounded"
                ),
                div(
                    div(class_="center-text",
                        content=f"{file_path}"),
                    id_=f"{div_id}",
                    class_="box is-align-content-center",
                    style=f"{display_class} width:100%; "\
                          f"background-color:rgba(0,0,0,0.6);",

                    ),
                    class_="image is-square div-bottom",
                ),
                data_target=f"{div_id}",
                data_path=f"{file_path}",
                class_=f"column is-one-quarter modal-button "\
                      f"js-modal-trigger hoverArea {file_type}"
            )
 
        self.append(_div)

    def __str__(self):
          return super().__str__() + "\n"
