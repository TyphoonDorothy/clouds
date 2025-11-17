import os
from getpass import getpass
from werkzeug.security import generate_password_hash
from my_project import create_app
from my_project.database import db
from my_project.auth.model import User

app = create_app()
with app.app_context():
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if db.session.query(User).filter_by(username=username).first():
        print("User already exists:", username)
    else:
        user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print("Created user:", user)
