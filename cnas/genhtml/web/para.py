from genhtml.web.tag import tag


class para(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("p").make_element()
