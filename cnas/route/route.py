from pages.index import index
from pages.gallery import gallery

def route(app):
  @app.route("/")
  def index_page() -> str:
    return str(index())

  @app.route("/gallery")
  def gallery_page() -> str:
    return str(gallery())
