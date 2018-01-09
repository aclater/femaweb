from flask import Flask
from config import Config

application = Flask(__name__)
application.config.from_object(Config)

from application import routes