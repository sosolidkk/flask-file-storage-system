from src import db, login
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        username
        email address
        password (hashed using wekzeug.security)
        description of user (filled later on the dashboard)
        date that the user registered on
        last time user logged in
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(256))
    registered_on = db.Column(db.DateTime, nullable=True)
    last_seen = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = self.set_password(password)
        self.about_me = ""
        self.registered_on = datetime.now()
        self.last_seen = datetime.now()

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        return generate_password_hash(password, salt_length=8)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"
