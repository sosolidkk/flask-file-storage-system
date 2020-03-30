"""
routes.py dashboard/
"""

from . import dashboard_blueprint
from src import db
from datetime import datetime
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user


@dashboard_blueprint.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@dashboard_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout successful.", "success")
    return redirect(url_for("index.index"))


@dashboard_blueprint.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()
