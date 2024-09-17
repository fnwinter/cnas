class tag:
    def __init__(self, *args, **kwargs):
        """
        base object for all tags

        >>> from genhtml.w3c.tag import tag
        >>> t = tag(src = "http://cnas.com")
        >>> str(t.set_tag("test").make_element())
        '<test src=http://cnas.com></test>'
        >>> t = tag().set_content("hello world")
        >>> t = t.set_tag("tag").make_element()
        >>> str(t)
        '<tag>hello world</tag>'
        >>> t = tag().set_tag("tag", True).make_element()
        >>> str(t)
        '<tag/>'

        """
        self._open_tag = ""
        self._close_tag = ""
        self._content = ""
        self._tag = ""
        self._is_void_element = False
        self._children = []
        self._attributes = {}
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
        ...     .set_tag("test").make_element()
        >>> str(t)
        '<test>Hello World!</test>'

        """
        self._content = content
        return self

    def set_tag(self, tag_, is_void_element = False):
        self._tag = tag_
        self._is_void_element = is_void_element
        return self

    def make_element(self):
        if self._tag == "":
            return self

        _attr = ""
        for _key, _value in self._attributes.items():
            # class is python keyword
            _key = "class" if "class_" == _key else _key
            _attr += f" {_key}={_value}"

        if self._is_void_element:
            self._open_tag = f"<{self._tag}{_attr}/>"
        else:
            self._open_tag = f"<{self._tag}{_attr}>"
            self._close_tag = f"</{self._tag}>"
        return self

    def append(self, new_element):
        self._children.append(str(new_element))
        return self

    def get_attributes(self, key):
        return self._attributes.get(key)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __str__(self):
        return self._open_tag + self._content + \
            "".join(self._children) + self._close_tag
