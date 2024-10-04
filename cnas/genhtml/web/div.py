from genhtml.web.tag import tag


class div(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("div").make_element()
