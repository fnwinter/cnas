from genhtml.web.tag import tag


class image(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("image", True).make_element()
