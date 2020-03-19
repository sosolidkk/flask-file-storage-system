from flask import Flask
from config import Config, DevelopmentConfig

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)
app.config.from_object(DevelopmentConfig)

from app import routes
