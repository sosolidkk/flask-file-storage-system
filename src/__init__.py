"""__init__.py src/
"""

from flask import Flask
from config import Config


def create_app(config_class=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from src.index import index_blueprint

    app.register_blueprint(index_blueprint)
