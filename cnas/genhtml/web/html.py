from genhtml.web.tag import tag


class html(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("html").make_element()
