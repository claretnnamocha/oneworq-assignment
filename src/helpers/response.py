import json
from datetime import datetime

from flask import Response


def response(data, code):
    data["timestamp"] = datetime.utcnow().strftime("%a, %d %B %Y %H:%M:%S GMT")
    return Response(json.dumps(data), status=code, mimetype="application/json")


def handle_exception(e):
    data = {"message": e.name, "status": False}
    return response(data=data, code=e.code)
