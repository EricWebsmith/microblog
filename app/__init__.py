from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

myapp = Flask(__name__)
# SECRET_KEY = os.urandom(32)
# myapp.config['SECRET_KEY'] = SECRET_KEY
myapp.config.from_object(Config)

db = SQLAlchemy(myapp)
migrate = Migrate(myapp, db)
from app import routes, models