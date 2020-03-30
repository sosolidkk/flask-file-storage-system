"""
forms.py index/
"""

from src.models import User
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    SelectField,
    SubmitField,
    StringField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    ValidationError,
)
from flask_wtf.file import FileField, FileRequired, FileAllowed


class SignInForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(message="Required field")]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Required field")]
    )
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign in")


class SignUpForm(FlaskForm):
    username = StringField("User", validators=[DataRequired(message="Required field")])
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Required field"),
            Email(message="Insert a valid email"),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(message="Required field")]
    )
    password_confirmation = PasswordField(
        "Password confirmation",
        validators=[
            DataRequired(message="Required field"),
            EqualTo("password", message="Password must be equal"),
        ],
    )
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email")


class UploadForm(FlaskForm):
    file = FileField("Select a file", validators=[FileRequired()])
