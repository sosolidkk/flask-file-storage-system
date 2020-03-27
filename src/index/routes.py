from os import mkdir, walk
from os.path import exists, isfile, isdir
from secrets import token_urlsafe
from . import index_blueprint
from .forms import UploadForm
from flask import (
    render_template,
    flash,
    url_for,
    redirect,
    jsonify,
    send_from_directory,
    send_file,
)
from werkzeug.utils import secure_filename


@index_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        data = form.file.data
        filename = secure_filename(data.filename)
        key = token_urlsafe(16)

        file_size = len(data.read())
        data.seek(0)

        if file_size > 2 * 1024 * 1024:
            flash(f"File size too big", "danger")
            return redirect(url_for("index"))

        if not exists(key):
            mkdir(f"files/{key}")
            data.save(f"files/{key}/{filename}")

        flash(
            f"File access key: {key}", "success",
        )
        return redirect(url_for("index.index"))
    return render_template(
        "index.html", title="Index page", brand="OneTimeUploads", form=form
    )


@index_blueprint.route("/<string:id>", methods=["GET"])
def download_file(id):
    filename = ""
    path = index_blueprint.config["UPLOAD_FOLDER"] + id + "/"

    if exists(path):
        for (_, _, files) in walk(path):
            filename = files[0]
        return send_file(path + filename, as_attachment=True)
    flash(f"KeyError, file not found!", "danger")
    return redirect(url_for("index.index"))
