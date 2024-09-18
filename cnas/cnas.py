from flask import Flask

from route.route import route
from service.background import background
from util.config import CONFIG

app = Flask(__name__)

# please set this value in config(~/.cnas/config.json)
_secret_key = CONFIG.get("secret_key")
app.secret_key = 'your_secret_key'\
    if _secret_key is None else _secret_key

background()
route(app)
