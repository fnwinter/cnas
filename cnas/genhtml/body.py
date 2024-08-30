from genhtml.tag import tag

class body(tag):
  def __init__(self):
    super().__init__()
    self.tags = ["<body>", "</body>"]

