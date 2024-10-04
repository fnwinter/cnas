from genhtml.web.tag import tag
from genhtml.web.figure import figure
from genhtml.web.div import div
from genhtml.web.image import image

__MUSIC_CARD__ =\
"""
<div class="card" style="width:256px;margin:5px;">
  <div class="card-image">
    <figure class="imagei is-4by3">
      <img
        src="https://bulma.io/assets/images/placeholders/256x256.png"
        alt="Placeholder image"
      />
    </figure>
  </div>
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img
            src="https://bulma.io/assets/images/placeholders/96x96.png"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">John Smith</p>
        <p class="subtitle is-6">@johnsmith</p>
      </div>
    </div>

    <div class="content">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
      iaculis mauris. <a>@bulmaio</a>. <a href="#">#css</a>
      <a href="#">#responsive</a>
      <br />
      <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
    </div>
  </div>
</div>
"""

class music_builder(tag):
    auto_index = 0

    def __init__(self, *args, **kwargs):
        # no inheritance
        super().__init__([], {})
        self.set_content(__MUSIC_CARD__)

    def __str__(self):
          return super().__str__() + "\n"
