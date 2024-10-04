from genhtml.web.tag import tag
from genhtml.web.anchor import anchor
from genhtml.web.hr import hr

__NAVIBAR_HEAD__ =\
"""
  <!--start navibar-->
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <image style="float:left; padding: 8px 8px 8px 8px;"
            src="static/images/cherry.png" width="50" height="50"/>

    <div id="navbar-menu" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href='/'>
          Home
        </a>
"""
__NAVIBAR_MORE__ =\
"""
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More
          </a>
          <div class="navbar-dropdown">
            %s
          </div>
        </div>
"""
__NAVIBAR_TAIL__ =\
"""
        <a class="navbar-item" href='/'>
          Help
        </a>
      </div>
    </div>
  </nav>
  <!--end navibar-->
"""


class navibar_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drop_list = []
        self.set_content(
            __NAVIBAR_HEAD__
            + __NAVIBAR_TAIL__
        ).make_element()

    def set_menu(self, drop_menu):
        assert drop_menu, "No drop down menu"
        assert isinstance(drop_menu, dict), "Drop down menu should be dict type"

        self.drop_list = []
        for _title, _url in drop_menu.items():
            if _url == "divider":
                self.drop_list.append(hr(class_="navbar-divider"))
            else:
                _anchor = anchor(class_="navbar-item", href=f"{_url}")
                _anchor.set_content(_title)
                self.drop_list.append(_anchor)

        _drop_str = ""
        for d in self.drop_list:
            _drop_str += str(d)

        self.set_content(
            __NAVIBAR_HEAD__
            + __NAVIBAR_MORE__ % _drop_str
            + __NAVIBAR_TAIL__
        ).make_element()
        return self
