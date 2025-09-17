from flask import Flask
import yaml
import os
from my_project.database import db
from my_project.sportsman.routes.__init__ import register_routes

def create_app():
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yml")
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_routes(app)

    return app