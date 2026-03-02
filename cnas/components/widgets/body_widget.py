from components.elements.tag import tag

class body_widget(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.append("<button id='call_python'></button>")
        self.append("<dialog id='loading'>")
        self.append("    <p>Loading...</p>")
        self.append("</dialog>")
        self.append("<script>showLoading();</script>")