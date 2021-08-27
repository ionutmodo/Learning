import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Used as a cryptographic key to generate signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database location
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(basedir, "application.db")}'

    # Send a signal to the application every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
