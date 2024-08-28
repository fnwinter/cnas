from flask import Flask

from genhtml.genhtml import GenHTML

app = Flask(__name__)

@app.route("/")
def index():
  gh = GenHTML()
  gh.header()
  return gh.output()

