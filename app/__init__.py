import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, request
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.errors import bp as errors_bp


myapp = Flask(__name__)
SECRET_KEY = os.urandom(32)
myapp.config['SECRET_KEY'] = SECRET_KEY
myapp.config.from_object(Config)

db = SQLAlchemy(myapp)
migrate = Migrate(myapp, db)

login = LoginManager(myapp)
login.login_view = 'login'
mail = Mail(myapp)
bootstrap = Bootstrap(myapp)
moment = Moment(myapp)
babel = Babel(myapp)
myapp.register_blueprint(errors_bp)
from app import models, routes

if not myapp.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    myapp.logger.addHandler(file_handler)

    myapp.logger.setLevel(logging.INFO)
    myapp.logger.info('Microblog startup')

@babel.localeselector
def get_locale():
    print(request.accept_languages.best_match(myapp.config['LANGUAGES']))
    return 'zh'
    # return request.accept_languages.best_match(myapp.config['LANGUAGES'])