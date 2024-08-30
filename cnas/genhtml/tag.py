class tag(object):
  def __init__(self):
    self.text = ""
    self.tags = []
    self.children = []

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def add(self, tag):
    self.children.append(tag.output())

  def output(self):
    return self.tags[0] + self.text + "".join(self.children) + self.tags[1]
