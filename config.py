import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'actual_secret_key'
    # sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Email sending
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['flaskprojectinbox@gmail.com']
    # pagination
    POSTS_PER_PAGE = 10
    # translations
    LANGUAGES = ['en', 'es']
    # Azure translator service
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # elasticsearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
