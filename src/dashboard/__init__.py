"""
__init__.py dashboard/
"""

from flask import Blueprint

dashboard_blueprint = Blueprint(
    "dashboard",
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)
dashboard_blueprint.config = {}


@dashboard_blueprint.record
def record_params(setup_state):
    app = setup_state.app
    dashboard_blueprint.config = dict(
        [(key, value) for key, value in app.config.items()]
    )


from . import routes
