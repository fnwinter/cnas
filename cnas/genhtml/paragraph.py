from genhtml.tag import tag


class p(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = ["<p>", "</p>"]
        self.text = self.attributes.get('cnas_text')
        self.make_tag()
