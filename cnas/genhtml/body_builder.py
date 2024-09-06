from genhtml.w3c.head import head
from genhtml.w3c.tag import tag

class body_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(args, {})

    def __str__(self):
        return str()
