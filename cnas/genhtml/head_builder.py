from genhtml.w3c.head import head
from genhtml.w3c.tag import tag

class head_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__([], {})
        self.title = kwargs.get("title")

    def __str__(self):
        return str(head().set_content(
f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <link rel="stylesheet" href="static/bulma/css/bulma.min.css">
"""
        ))
