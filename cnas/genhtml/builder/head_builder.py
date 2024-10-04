from genhtml.web.head import head
from genhtml.web.tag import tag

__HEAD__=\
"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%s</title>
    <link rel="stylesheet" href="static/bulma/css/bulma.min.css">
    <link rel="stylesheet" href="static/css/cnas.css">
    <script type="text/javascript" src="static/jquery/jquery-3.7.1.min.js"></script>
    <script type="text/javascript" src="static/javascripts/cnas.js"></script>
    <script type="text/javascript" src="static/javascripts/cnas_gallery.js"></script>
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
"""

class head_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__([], {})
        self.title = kwargs.get("title")

    def __str__(self):
        return str(head().set_content(
            __HEAD__ % self.title
        ))
