import sys

from flask import Flask

from route.route import route
from services.service import service_process
from util.config import CONFIG
from util.setup import setup

if not setup():
    print("setup failed")
    sys.exit(1)

app = Flask(__name__)

# please set this value in config(~/.cnas/config.json)
_secret_key = CONFIG.get("secret_key")
app.secret_key = 'your_secret_key'\
    if _secret_key is None else _secret_key

service_process()
route(app)
