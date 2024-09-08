from genhtml.w3c.tag import tag

class footer_builder(tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_content(
f"""
<footer class="footer">
  <div class="content has-text-centered">
    <p>
      <strong>CherryNAS</strong> by <a href="https://fnwinter.github.io">JungJik Lee</a>.
      The source code is licensed
      <a href="https://opensource.org/license/mit">MIT</a>. The
      website content is licensed
    </p>
    <p>
      <button class="button is-dark">Go to up</button>
    </p>
  </div>
</footer>
"""
      ).make_element()
