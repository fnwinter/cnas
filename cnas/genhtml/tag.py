class tag:
    def __init__(self, *args, **kwargs):
        self.open_tag = ""
        self.close_tag = ""
        self.text = ""
        self.tags = []
        self.children = []
        self.attributes = {}
        for _t in args:
            if isinstance(_t, tag):
                self.children.append(str(_t))
        for key, value in kwargs.items():
            self.attributes[key] = value

    def make_tag(self):
        self.open_tag = self.tags[0][0:-1]
        for _key, _value in self.attributes.items():
            if "cnas_" not in _key:
                self.open_tag += f" {_key} = {_value} "
        self.open_tag += ">"
        self.close_tag = self.tags[1] if len(self.tags) == 2 else ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def append(self, new_tag):
        self.children.append(str(new_tag))

    def __str__(self):
        return self.open_tag + self.text + \
            "".join(self.children) + self.close_tag
