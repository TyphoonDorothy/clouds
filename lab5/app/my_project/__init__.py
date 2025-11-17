from flask import Flask
import yaml
import os
from my_project.database import db
from my_project.sportsman.routes.__init__ import register_routes
from flasgger import Swagger
from flask_jwt_extended import JWTManager

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {"title": "My API", "version": "1.0"},
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: Bearer <JWT token>"
        }
    }
}

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "swagger_ui_parameters": {
        "requestInterceptor": "window.swaggerRequestInterceptor"
    },
    "swagger_ui_js": [
        "/static/swagger_auth.js"
    ],
}

jwt = JWTManager()  # create instance globally so other modules can import

def create_app():
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = config.get('jwt_secret_key', 'replace_with_secure_random')  # required

    db.init_app(app)
    jwt.init_app(app)  # initialize JWTManager
    register_routes(app)
    Swagger(app, template=SWAGGER_TEMPLATE)

    return app
