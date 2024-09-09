from genhtml.w3c.tag import tag

class navibar_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _drop_down_menu =\
"""
            <a class="navbar-item">
             %s 
            </a>
"""
        test = ["test","test2","test3"]
        self.t = ""
        for t in test:
            self.t += _drop_down_menu % t


    def set_menu(self, menu):
        self.set_content(
f"""
  <!--start navibar-->
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <image style="float:left; padding: 8px 8px 8px 8px;"  src="static/images/cherry.png" width="50" height="50"/>

    <div id="navbar-menu" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href='/'>
          Home
        </a>
"""
"""
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More
          </a>
          <div class="navbar-dropdown">
"""
+ self.t +
"""
          </div>
        </div>
"""
"""
        <a class="navbar-item" href='/'>
          Help
        </a>

      </div>
    </div>
  </nav>
  <!--end navibar-->
"""

        ).make_element()
        return self
