from genhtml.web.tag import tag


class hr(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("hr").make_element()
