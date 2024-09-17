from genhtml.w3c.tag import tag

class br(tag):
    def __init__(self, *args, **kwargs):
        super().__init__([], {})
        self.set_tag("br", True).make_element()
