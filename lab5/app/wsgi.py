from my_project import create_app
from flask import Flask, request, Response, make_response
from functools import wraps
import os

app = create_app()

username_app = os.getenv('USER')
password_app = os.getenv('PASSWORD')


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

@app.before_request
def require_authentication():
    if request.endpoint and request.endpoint.startswith('static'):
        return
    auth = request.authorization
    print(f"Before request - Auth received: {auth}")
    if not auth or auth.username != username_app or auth.password != password_app:
        return authenticate()


@app.route("/")
@requires_auth
def index():
    return "Hello, you are authenticated!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)