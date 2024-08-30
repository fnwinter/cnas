from genhtml.tag import tag

class head(tag):
  def __init__(self, title):
    super().__init__()
    self.tags = ["<head>", "</head>"]
    self.text = \
f"""
<meta charset=\"UTF-8\">
<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
<link rel=\"stylesheet\" href=\"static/bulma/css/bulma.min.css\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>{title}</title>
"""
