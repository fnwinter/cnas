from genhtml.w3c.tag import tag


class body(tag):
    def __init__(self, *args, **kwargs):
        """
        create body tag

        >>> from genhtml.w3c.body import body
        >>> _body = body()
        >>> str(_body)
        '<body></body>'

        """

        super().__init__(*args, **kwargs)
        self.set_tags(["<body>", "</body>"])\
            .make_element()
