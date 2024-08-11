from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)

    # Pasamos la configuracion a Flask desde el archivo de configuracion "Config.py"
    app.config.from_object(config[config_name])

    with app.app_context():
        from . import routes

    return app
