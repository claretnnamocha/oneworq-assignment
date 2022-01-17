import os

from flasgger import Swagger, swag_from
from flask import Blueprint, Flask, json
from werkzeug.exceptions import HTTPException

from src.configs.swagger import swagger_config, swagger_template
from src.helpers import handle_exception
from src.models import db
from src.modules import auth, shop

app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS"),
    SWAGGER={"title": "Ecommerce API", "uiversion": 2},
)
app.register_error_handler(HTTPException, handle_exception)

Swagger(
    app,
    config=swagger_config,
    template=swagger_template,
    # template_file="docs/*.yml",
)

db.app = app
db.init_app(app)


api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(auth)
api.register_blueprint(shop)


app.register_blueprint(api)
