from genhtml.w3c.tag import tag

class script(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tag("script").make_element()
