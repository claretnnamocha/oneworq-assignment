from functools import wraps

from src.helpers import response


def controller(f):
    @wraps(f)
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        code = 200 if "status" in result and result["status"] else 400
        return response(data=result, code=code)

    return inner
