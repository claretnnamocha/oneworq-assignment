from cmath import log
from functools import wraps
import os

import jwt
from flask import request
from src.helpers import response
from src.models import User


def authenticate(f):
    @wraps(f)
    def inner(*args, **kwargs):
        try:
            if (
                "authorization" not in request.headers
                or not request.headers["authorization"]
            ):
                return response(
                    data={"status": False, "message": "Unauthorized"}, code=401
                )

            decoded = jwt.decode(
                request.headers["authorization"],
                os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS"),
                algorithms=["HS256"],
            )

            payload = decoded["payload"]
            user = User.query.filter_by(id=payload).first()
 
            if not user:
                return response(
                    data={"status": False, "message": "Unauthorized"}, code=401
                )

            request.form = {**request.form, "userId": payload}

        except Exception:
            return response(data={"status": False, "message": "Unauthorized"}, code=401)

        result = f(*args, **kwargs)
        return result

    return inner
