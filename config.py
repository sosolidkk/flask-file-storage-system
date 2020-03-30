"""config.py
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(16)
    WTF_CSRF_SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(16)
    UPLOAD_FOLDER = basedir + "/files/"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or f"sqlite:///{os.path.join(basedir, 'temp/toy_db.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or f"sqlite:///{os.path.join(basedir, 'temp/test_db.db')}"
    )
