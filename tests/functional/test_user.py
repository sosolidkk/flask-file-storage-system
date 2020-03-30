"""
This file (test_users.py) contains the functional tests for the index blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the users blueprint.
"""


def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check if the response is valid
    """
    response = test_client.get("/")

    assert response.status_code == 200
    assert b"What is" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Remember me" in response.data
    assert b"Sign in" in response.data
    assert b"Create an account" in response.data
    assert b"Forgot your password?" in response.data
    assert b"sosolidkk" in response.data


def test_post_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (POST)
    THEN check if the fields are required
    """
    response = test_client.post("/")

    assert response.status_code == 200
    assert b"Required field" in response.data


def test_valid_login_logout(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (POST)
    THEN check if the login is valid
    """

    user = {"username": "test", "password": "test"}
    response = test_client.post("/", data=user, follow_redirects=True)

    assert response.status_code == 200
    assert b"Sign in in successful on test." in response.data
    assert b"Logout" in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check if the logout is valid
    """

    response = test_client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Logout successful." in response.data


def test_invalid_login(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (POST)
    THEN check if the login is invalid
    """

    user = {"username": "test", "password": "teste"}
    response = test_client.post("/", data=user, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid user credentials." in response.data


def test_valid_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if the registration is valid
    """

    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "admin",
        "password_confirmation": "admin",
    }
    response = test_client.post("/sign_up", data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b"admin user created successful." in response.data
    assert b"What is" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Remember me" in response.data
    assert b"Sign in" in response.data
    assert b"Create an account" in response.data
    assert b"Forgot your password?" in response.data
    assert b"sosolidkk" in response.data


def test_invalid_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if the registration is not valid
    """

    response = test_client.post("/sign_up", data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Required field" in response.data


def test_same_username_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if the username is used
    """

    user = {
        "username": "test",
        "email": "test@gmail.com",
        "password": "test",
        "password_confirmation": "test",
    }
    response = test_client.post("/sign_up", data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b"Username already exists" in response.data


def test_same_email_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if the email is used
    """

    user = {
        "username": "admin",
        "email": "test@gmail.com",
        "password": "test",
        "password_confirmation": "test",
    }
    response = test_client.post("/sign_up", data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b"Please use a different email" in response.data


def test_invalid_email_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if the email is not valid
    """

    user = {
        "username": "admin",
        "email": "test",
        "password": "test",
        "password_confirmation": "test",
    }
    response = test_client.post("/sign_up", data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b"Insert a valid email" in response.data


def test_different_password_registration(test_client, init_db):
    """
    GIVEN a Flask application
    WHEN the '/sign_up' page is posted to (POST)
    THEN check if password are equal
    """

    user = {
        "username": "admin",
        "email": "test@gmail.com",
        "password": "test",
        "password_confirmation": "_test_",
    }
    response = test_client.post("/sign_up", data=user, follow_redirects=True)
    assert response.status_code == 200
    assert b"Password must be equal" in response.data
