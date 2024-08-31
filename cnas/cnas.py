from flask import Flask

from route.route import route

app = Flask(__name__)

route(app)
