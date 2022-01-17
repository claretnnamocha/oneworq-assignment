import os

import jwt
from src.models import User, db
from src.helpers import pluck


def signIn(params):
    password, email = pluck(params, "password", "email")
    user = User.query.filter_by(email=email).first()

    print(user)

    if not user or not user.validatePassword(password):
        return {
            "status": False,
            "message": "Invalid credentials",
        }

    data = jwt.encode(
        {"payload": user.id}, os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    )

    return {
        "status": True,
        "message": "Login successful",
        "data": data,
    }


def signUp(params):
    password, email, firstname, lastname = pluck(
        params, "password", "email", "firstname", "lastname"
    )
    user = User.query.filter_by(email=email).first()
    if user:
        return {
            "status": False,
            "message": "This email has been used to create an account",
        }
    user = User(password=password, email=email, firstname=firstname, lastname=lastname)

    db.session.add(user)
    db.session.commit()

    return {
        "status": True,
        "message": "Registration successful",
    }
