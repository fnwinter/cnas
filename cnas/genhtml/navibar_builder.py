from genhtml.w3c.tag import tag

class navibar_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_content(
f"""
  <!--start navibar-->
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <image style="float:left; padding: 8px 8px 8px 8px;"  src="static/images/cherry.png" width="50" height="50"/>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item" href='/'>
          Home
        </a>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More
          </a>
          <div class="navbar-dropdown">
            <a class="navbar-item">
              Create folder
            </a>
            <a class="navbar-item">
              Select
            </a>
            <a class="navbar-item">
              Delete
            </a>
            <a class="navbar-item">
              Upload
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item">
              Smaller thumbnails
            </a>
            <a class="navbar-item">
              Bigger thumbnails
            </a>
            <a class="navbar-item">
              Update thumbnails
            </a>
          </div>
        </div>

      </div>
    </div>
  </nav>
  <!--end navibar-->
"""

        ).make_element()
