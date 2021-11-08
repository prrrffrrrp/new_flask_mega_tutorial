import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'actual_secret_key'
