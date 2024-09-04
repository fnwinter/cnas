from genhtml.w3c.tag import tag


class head(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_tags(["<head>", "</head>"])
        self.make_element()
