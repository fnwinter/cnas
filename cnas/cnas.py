from flask import Flask

from genhtml.html import html
from genhtml.head import head
from genhtml.body import body

app = Flask(__name__)

@app.route("/")
def index():
  with html() as _html:
    _html.add(head("cnas"))
    with body() as _body:
      _body.add(image())
      _html.add(_body)
    return _html.output()

