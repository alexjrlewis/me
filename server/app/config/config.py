"""Module containing the Config class."""

import secrets

from dotenv import dotenv_values

config = dotenv_values(".env")


class Config:
    """Class to configure the application."""

    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False  # do not alphabetically sort in jsonfiy method.
    MAIL_SERVER = config["MAIL_SERVER"]
    MAIL_PORT = config["MAIL_PORT"]
    MAIL_USERNAME = config["MAIL_USERNAME"]
    MAIL_PASSWORD = config["MAIL_PASSWORD"]
    MAIL_USE_TLS = config["MAIL_USE_TLS"]
    MAIL_USE_SSL = config["MAIL_USE_SSL"]
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = config["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = config["RECAPTCHA_PRIVATE_KEY"]
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_TEST_URI')
    SECRET_KEY = secrets.token_urlsafe(32)
    TEMPLATES_AUTO_RELOAD = True
    # WTF_CSRF_METHODS = [] # https://stackoverflow.com/questions/38624060/flask-disable-csrf-in-unittest
