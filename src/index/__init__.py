"""__init__.py index/
"""

from flask import Blueprint

index_blueprint = Blueprint(
    "index",
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)
index_blueprint.config = {}


@index_blueprint.record
def record_params(setup_state):
    app = setup_state.app
    index_blueprint.config = dict([(key, value) for key, value in app.config.items()])


from . import routes
