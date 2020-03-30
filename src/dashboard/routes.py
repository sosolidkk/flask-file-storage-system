"""
routes.py dashboard/
"""

from . import dashboard_blueprint
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
