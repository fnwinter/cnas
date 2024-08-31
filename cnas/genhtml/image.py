from genhtml.tag import tag

class image(tag):
  def __init__(self):
    super().__init__()
    self.tags = ["<html>", "</html>"]

