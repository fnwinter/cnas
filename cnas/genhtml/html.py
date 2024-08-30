from genhtml.tag import tag

class html(tag):
  def __init__(self):
    super().__init__()
    self.tags = ["<html>", "</html>"]

