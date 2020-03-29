from . import index_blueprint
from .forms import SignInForm, SignUpForm
from flask import (
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    send_file,
    url_for,
)
from werkzeug.utils import secure_filename


@index_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = SignInForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            print(form.data)
            flash("Logged in successful", "success")
            return redirect(url_for("index.index"))

        flash("Error on sign in", "danger")
    return render_template("index.html", title="Index", brand="!", form=form)


@index_blueprint.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            flash("Sign up successful", "success")
            return redirect(url_for("index.index"))

        flash("Error on sign up", "danger")
    return render_template("sign_up.html", title="Sign up", brand="!", form=form)
