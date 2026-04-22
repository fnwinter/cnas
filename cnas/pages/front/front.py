from jinja2 import Template

from pages.base.page import page
from pages.base.system.html import html_file

from components.widgets.icon_widget import icon_widget

# Destinations shown on the front page. Each entry: (label, href, icon_src)
# NOTE: only cherry.png exists today; replace icon paths when assets are added.
__FRONT_BUTTONS__ = [
    ("Gallery",        "/gallery",        "static/icons/gallery.png"),
    ("Music",          "/music",          "static/icons/music.png"),
    ("Test",           "/test",           "static/icons/test.png"),
    ("PDF viewer",     "/pdf_viewer",     "static/icons/pdf_viewer.png"),
    ("System status",  "/system_status",  "static/icons/system_status.png"),
    ("Storage status", "/storage_status", "static/icons/storage_status.png"),
    ("Minecraft",      "/minecraft",      "static/icons/minecraft_server.png"),
    ("Trac",           "/trac_proxy",     "static/icons/trac.png"),
]

class front(page):
    def __init__(self):
        super().__init__()
        super().set_title("Front")
        super().need_login(True)

    @html_file("htmls/front.html")
    def load_scripts(self):
        return self

    def body_content(self):
        buttons_html = "".join(
            str(icon_widget(
                id_=f"front_btn_{i}",
                src=_src,
                text=_label,
                alt=_label,
                onclick=f"location.href='{_href}'",
            ))
            for i, (_label, _href, _src) in enumerate(__FRONT_BUTTONS__)
        )

        self.html = Template(self.html).render(
            title="Welcome",
            content="Front page of the CNAS system.",
            buttons=buttons_html,
        )
        return self
