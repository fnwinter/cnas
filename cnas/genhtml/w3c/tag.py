class tag:
    def __init__(self, *args, **kwargs):
        """
        base object for all tags

        >>> from genhtml.w3c.tag import tag
        >>> t = tag(src = "http://cnas.com")
        >>> t._tags = ["<test>","</test>"]
        >>> t = t.make_element()
        >>> str(t)
        '<test src=http://cnas.com></test>'
        >>> t = tag().set_content("hello world")
        >>> t = t.set_tags(["<tag>","</tag>"]).make_element()
        >>> str(t)
        '<tag>hello world</tag>'
        >>> t = tag().set_tags(["<tag/>"]).make_element()
        >>> str(t)
        '<tag/>'

        """
        self._open_tag = ""
        self._close_tag = ""
        self._content = ""
        self._tags = []
        self._children = []
        self._attributes = {}
        self._is_void_element = False
        for _t in args:
            if isinstance(_t, tag):
                self._children.append(str(_t))
        for key, value in kwargs.items():
            if key == "content":
                self._content = value
            else:
                self._attributes[key] = value

    def set_content(self, content):
        """
        set content in the element

        >>> from genhtml.w3c.tag import tag
        >>> t = tag(content = "test")
        >>> str(t)
        'test'
        >>> t = tag().set_content("Hello World!") \
        ...     .set_tags(["<test>","</test>"]).make_element()
        >>> str(t)
        '<test>Hello World!</test>'

        """
        self._content = content
        return self

    def set_tags(self, tags):
        self._tags = tags
        self._is_void_element = len(self._tags) == 1
        return self

    def make_element(self):
        if self._is_void_element:
            self._open_tag = self._tags[0][0:-2]
            for _key, _value in self._attributes.items():
                if "cnas_" not in _key:
                    self._open_tag += f" {_key}={_value}"
            self._open_tag += "/>"
        else:
            self._open_tag = self._tags[0][0:-1]
            for _key, _value in self._attributes.items():
                if "cnas_" not in _key:
                    self._open_tag += f" {_key}={_value}"
            self._open_tag += ">"
            self._close_tag = self._tags[1]
        return self

    def append(self, new_element):
        self._children.append(str(new_element))

    def get_attributes(self, key):
        return self._attributes.get(key)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __str__(self):
        return self._open_tag + self._content + \
            "".join(self._children) + self._close_tag
