import os

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://username:password@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
