from genhtml.web.tag import tag


class anchor(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("a").make_element()
