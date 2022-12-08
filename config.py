import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    ADMINS = ['your-email@example.com']
    MAIL_SERVER='localhost'
    MAIL_PORT=8025
    LANGUAGES = ['zh', 'en']
    MS_TRANSLATOR_KEY='29e43fcb2d2844e389cac10c462ccb93'