from components.elements.tag import tag

__ICON_CARD__ =\
"""
<button
  id="%(id)s"
  type="button"
  class="button icon-widget %(class_)s"
  onclick="%(onclick)s"
  style="display:flex;flex-direction:column;align-items:center;justify-content:center;
         width:128px;height:128px;margin:5px;padding:10px;
         background-color:#ffffff;border:1px solid #D2C4B4;border-radius:8px;
         cursor:pointer;%(style)s"
>
  <figure class="image is-64x64" style="margin:0 0 8px 0;padding:0;">
    <img src="%(src)s" alt="%(alt)s"
         style="width:100%%;height:100%%;object-fit:cover;
                border-radius:12px;display:block;margin:0;padding:0;"/>
  </figure>
  <span class="icon-widget-text" style="font-size:14px;color:#000000;">%(text)s</span>
</button>
"""

class icon_widget(tag):
    auto_index = 0

    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})
        icon_widget.auto_index += 1

        _id = kwargs.get("id_", f"icon_widget_{icon_widget.auto_index}")
        _src = kwargs.get("src", "")
        _text = kwargs.get("text", "")
        _alt = kwargs.get("alt", _text)
        _onclick = kwargs.get("onclick", "")
        _class = kwargs.get("class_", "")
        _style = kwargs.get("style", "")

        self.set_content(__ICON_CARD__ % {
            "id": _id,
            "src": _src,
            "alt": _alt,
            "text": _text,
            "onclick": _onclick,
            "class_": _class,
            "style": _style,
        })

    def __str__(self):
        return super().__str__() + "\n"
