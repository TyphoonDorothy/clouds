from flask import Flask
import yaml
import os
from my_project.database import db
from my_project.sportsman.routes.__init__ import register_routes
from flasgger import Swagger
from my_project.auth.routes import bp as auth_bp
from flask import url_for

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
    # IMPORTANT: pass requestInterceptor as a string that will be evaluated in the browser
    "swagger_ui_parameters": {
        # the global requestInterceptor function name we defined in swagger_auth.js
        # swagger-ui expects an actual function; Flasgger will place the string as-is in JS config
        "requestInterceptor": "window.swaggerRequestInterceptor"
    },
    # add the custom JS file so it runs inside Swagger UI
    "swagger_ui_js": [
        "/static/swagger_auth.js"   # Flask serves static files from my_project/static by default
    ],
}

def create_app():
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_routes(app)

    Swagger(app, template=SWAGGER_TEMPLATE)

    return app
