from my_project import create_app
from flask import Flask, request, Response, make_response
from functools import wraps
import os

app = create_app()

username_app = os.getenv('USER', 'admin')
password_app = os.getenv('PASSWORD', 'password')


def authenticate():
    response = make_response('You need to login with proper credentials', 401)
    response.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    response.headers['Content-Type'] = 'text/plain'
    return response


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        print(f"Auth received: {auth}")
        if auth:
            print(f"Username: {auth.username}, Password provided: {'Yes' if auth.password else 'No'}")

        if not auth or auth.username != username_app or auth.password != password_app:
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route("/test")
def test():
    return "This works without auth"


@app.route("/")
@requires_auth
def index():
    return "Hello, you are authenticated!"


@app.route("/debug")
def debug():
    return {
        "expected_user": username_app,
        "password_set": bool(password_app),
        "env_user": os.getenv('APP_USER'),
        "env_pass_set": bool(os.getenv('APP_PASSWORD'))
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)