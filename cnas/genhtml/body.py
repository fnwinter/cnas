from genhtml.tag import tag

class body(tag):
  def __init__(self):
    """
    create body tag

    >>> from genhtml.body import body
    >>> _body = body()
    >>> _body.output()
    '<body></body>'

    """

    super().__init__()
    self.tags = ["<body>", "</body>"]

