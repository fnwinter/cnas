class GenHTML(object):
  def __init__(self):
    self.html = ""
    pass

  def header(self):
    self.html = \
"""<head>
    <meta charset=\"UTF-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <link rel=\"stylesheet\" href=\"static/bulma/css/bulma.min.css\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Login</title>
</head>"""

  def body(self):
    self.html = self.html + "<body>"

  def output(self):
    return self.html
