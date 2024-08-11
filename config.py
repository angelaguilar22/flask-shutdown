import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_ECHO = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
