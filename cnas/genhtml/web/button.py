from genhtml.web.tag import tag


class button(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("button").make_element()
