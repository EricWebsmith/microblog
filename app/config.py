import os


class Config:
    SECRET = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
