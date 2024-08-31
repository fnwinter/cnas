from pages.page import page

from genhtml.html import html
from genhtml.head import head
from genhtml.body import body
from genhtml.image import image

class index(page):
  def __init__(self):
    super().__init__()

  def __str__(self):
    with html() as _html:
      _html.add(head("cnas"))
      with body() as _body:
        _body.add(image())
        _html.add(_body)
      return _html.output()

