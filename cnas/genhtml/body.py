from genhtml.tag import tag


class body(tag):
    def __init__(self, *args, **kwargs):
        """
        create body tag

        >>> from genhtml.body import body
        >>> _body = body()
        >>> str(_body)
        '<body></body>'

        """

        super().__init__(*args, **kwargs)
        self.tags = ["<body>", "</body>"]
        self.make_tag()
