from genhtml.w3c.tag import tag


class figure(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("figure").make_element()
