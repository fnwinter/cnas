from genhtml.web.tag import tag


class body(tag):
    def __init__(self, *args, **kwargs):
        """
        create body tag

        >>> from genhtml.web.body import body
        >>> _body = body()
        >>> str(_body)
        '<body></body>'

        """

        super().__init__(*args, **kwargs)
        self.set_tag("body").make_element()
