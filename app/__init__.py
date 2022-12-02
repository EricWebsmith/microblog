from flask import Flask
from app.config import Config
import os
myapp = Flask(__name__)
SECRET_KEY = os.urandom(32)
myapp.config['SECRET_KEY'] = SECRET_KEY
# myapp.config.from_object(Config)
from app import routes