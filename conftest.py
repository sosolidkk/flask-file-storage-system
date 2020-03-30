import pytest
from src import create_app, db
from src.models import User
from config import TestingConfig


@pytest.fixture(scope="module")
def test_client():
    app = create_app(config_class=TestingConfig)
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope="module")
def init_db():
    db.create_all()

    user = User(username="test", email="test@gmail.com", password="test")
    user2 = User(username="john", email="john@gmail.com", password="john")

    db.session.add_all([user, user2])
    db.session.commit()

    yield db

    db.drop_all()
