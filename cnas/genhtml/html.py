from genhtml.tag import tag


class html(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = ["<html>", "</html>"]
        self.make_tag()
