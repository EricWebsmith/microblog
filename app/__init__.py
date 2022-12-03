import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

myapp = Flask(__name__)
SECRET_KEY = os.urandom(32)
myapp.config['SECRET_KEY'] = SECRET_KEY
myapp.config.from_object(Config)

db = SQLAlchemy(myapp)
migrate = Migrate(myapp, db)

login = LoginManager(myapp)
login.login_view = 'login'
from app import models, routes
