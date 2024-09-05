from flask import Flask

from route.route import route
from service.background import background

app = Flask(__name__)

background()
route(app)
