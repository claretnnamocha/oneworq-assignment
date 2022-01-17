from functools import wraps
from urllib.parse import parse_qsl

from cerberus import Validator
from flask import request
from src.helpers import response


def validate(schema):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            v = Validator(schema)

            params = (
                convert(dict(parse_qsl(request.query_string)))
                if request.method == "GET"
                else request.json or {}
            )

            if not v.validate(params):
                data = {
                    "status": False,
                    "message": "Validation Error",
                    "data": v.errors,
                }
                return response(data=data, code=400)
            request.form = {**request.form, **v.document}
            result = f(*args, **kwargs)
            return result

        return inner

    return outer


def convert(data):
    if isinstance(data, bytes):
        return data.decode("ascii")
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)
    return data
