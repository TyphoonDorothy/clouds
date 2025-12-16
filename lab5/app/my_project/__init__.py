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

def create_app():
    app = Flask(__name__)
    jwt = JWTManager()
    
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = config.get('jwt_secret_key', 'nklnknl')
    
    # ===== CRITICAL: ALL CSRF SETTINGS =====
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['JWT_CSRF_CHECK_FORM'] = False
    app.config['JWT_CSRF_IN_COOKIES'] = False
    # =======================================
    
    db.init_app(app)
    jwt.init_app(app)  # JWTManager MUST be initialized AFTER config is set
    register_routes(app)
    
    # Initialize Swagger with template
    swagger = Swagger(app, template=SWAGGER_TEMPLATE)
    
    # Debug: Print config to verify
    print("=" * 50)
    print("JWT CSRF Settings:")
    print(f"JWT_COOKIE_CSRF_PROTECT: {app.config.get('JWT_COOKIE_CSRF_PROTECT')}")
    print(f"WTF_CSRF_ENABLED: {app.config.get('WTF_CSRF_ENABLED')}")
    print(f"JWT_CSRF_CHECK_FORM: {app.config.get('JWT_CSRF_CHECK_FORM')}")
    print(f"JWT_CSRF_IN_COOKIES: {app.config.get('JWT_CSRF_IN_COOKIES')}")
    print("=" * 50)
    
    return app