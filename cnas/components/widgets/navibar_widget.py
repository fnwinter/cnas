from components.elements.tag import tag
from components.elements.anchor import anchor
from components.elements.hr import hr

__NAVIBAR_HEAD__ =\
"""
  <!--start navibar-->
  <nav class="navbar cnas-navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img class="cnas-navbar-logo" src="static/images/cherry.png" alt="CNAS logo" width="40" height="40"/>
      </a>
    </div>

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
            __NAVIBAR_MORE_ITEMS__
          </div>
        </div>
"""
__NAVIBAR_TAIL__ =\
"""
        <a class="navbar-item" href='/'>
          Help
        </a>
      </div>
      <div class="navbar-end">
        __NAVIBAR_AUTH__
      </div>
    </div>
  </nav>
  <style>
    .cnas-navbar {
      background-color: #ffffff;
      border-bottom: 1px solid #D2C4B4;
    }
    .cnas-navbar .navbar-item,
    .cnas-navbar .navbar-link {
      color: #000000;
    }
    .cnas-navbar .navbar-item:hover,
    .cnas-navbar .navbar-link:hover {
      background-color: #F3E3D0;
      color: #000000;
    }
    .cnas-navbar .navbar-end .navbar-item {
      display: flex;
      align-items: center;
    }
    .cnas-navbar .navbar-end .navbar-item form {
      margin: 0;
      display: flex;
      align-items: center;
    }
    .cnas-navbar-logo {
      border-radius: 50%;
      object-fit: cover;
    }
  </style>
  <!--end navibar-->
"""


class navibar_widget(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drop_list = []
        self.auth_html = ""
        self.set_content(__NAVIBAR_HEAD__ + __NAVIBAR_TAIL__.replace("__NAVIBAR_AUTH__", self.auth_html)).make_element()

    def set_auth(self, user_email: str):
        if not user_email:
            self.auth_html = ""
            self._render_navbar()
            return self

        self.auth_html = f"""
        <div class='navbar-item'>
          Logged in as <strong style='margin-left:6px;'>{user_email}</strong>
        </div>
        <div class='navbar-item'>
          <form method='POST' action='/login/logout'>
            <button type='submit' class='button is-primary is-small'>Logout</button>
          </form>
        </div>
        """
        self._render_navbar()
        return self

    def _render_navbar(self):
        _drop_str = "".join(str(d) for d in self.drop_list)
        _more_str = __NAVIBAR_MORE__.replace("__NAVIBAR_MORE_ITEMS__", _drop_str) if _drop_str else ""
        _tail_str = __NAVIBAR_TAIL__.replace("__NAVIBAR_AUTH__", self.auth_html)
        self.set_content(__NAVIBAR_HEAD__ + _more_str + _tail_str).make_element()
        return self

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

        self._render_navbar()
        return self
