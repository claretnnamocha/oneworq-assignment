from flasgger import swag_from
from flask import Blueprint, request
from src.middlewares import controller, validate
from src.modules.auth import service, validators

routes = Blueprint("auth", __name__, url_prefix="/auth")


@routes.post("/sign-in")
@validate(validators.signIn)
@controller
def signIn():
    return service.signIn(request.form)


@routes.post("/sign-up")
@validate(validators.signUp)
def signUp():
    return service.signUp(request.form)
