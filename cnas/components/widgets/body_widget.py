from components.elements.tag import tag

class body_widget(tag):
    def __init__(self, *args, show_loading: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.append("<button id='call_python'></button>")
        self.append("<dialog id='loading'>")
        self.append("    <div class='loading-dialog-panel'>")
        self.append("        <p class='loading-dialog-text'>Loading...</p>")
        self.append("    </div>")
        self.append("</dialog>")
        if show_loading:
            self.append("<script>showLoading();</script>")
