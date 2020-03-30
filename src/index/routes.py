"""
routes.py index/
"""

from . import index_blueprint
from .forms import SignInForm, SignUpForm
from src import db
from src.models import User
from flask import (
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required, login_user

BRAND = "FastUploads"


@index_blueprint.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        flash("Redirecting to user dashboard...")
        return redirect(url_for("dashboard.dashboard"))

    form = SignInForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user is None or not user.check_password(form.password.data):
                flash("Invalid user credentials.", "danger")
                return redirect(url_for("index.index"))

            login_user(user, remember=form.remember_me.data)
            flash(f"Sign in in successful on {user.username}.", "success")
            return redirect(url_for("dashboard.dashboard"))

        flash("Error on sign in", "danger")
    return render_template("index.html", title="Index", brand=BRAND, form=form)


@index_blueprint.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
            )

            db.session.add(user)
            db.session.commit()

            flash(f"{user.username} User was created successful!", "success")
            return redirect(url_for("index.index"))
    return render_template("sign_up.html", title="Sign up", brand=BRAND, form=form)
