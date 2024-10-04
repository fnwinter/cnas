from genhtml.web.tag import tag


class head(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("head").make_element()
