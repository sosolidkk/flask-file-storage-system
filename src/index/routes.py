from . import index_blueprint
from .forms import SignInForm
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

        flash("Error! Incorrect login credentials", "danger")
    return render_template("index.html", form=form)
