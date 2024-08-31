from genhtml.tag import tag


class image(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = ["<image>"]
        self.make_tag()
