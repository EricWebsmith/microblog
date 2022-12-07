import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    ADMINS = ['your-email@example.com']
    MAIL_SERVER='localhost'
    MAIL_PORT=8025
    LANGUAGES = ['es', 'cn']