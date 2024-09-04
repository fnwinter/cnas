from genhtml.tag import tag


class head(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        title = self.get_attributes('cnas_title')
        self.set_tags(["<head>", "</head>"])
        self._content = \
            f"""
<meta charset=\"UTF-8\">
<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
<link rel=\"stylesheet\" href=\"static/bulma/css/bulma.min.css\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>{title}</title>
"""
        self.make_element()
