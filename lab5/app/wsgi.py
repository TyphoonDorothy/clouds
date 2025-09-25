from my_project import create_app
from flask import Flask, request, Response
from functools import wraps
import os

app = create_app()

# Debug: Print to console what we're getting
username_app = os.getenv('USER')
password_app = os.getenv('PASSWORD')

print(f"DEBUG - USER env var: {username_app}")
print(f"DEBUG - PASSWORD env var: {password_app}")


# Add a debug endpoint
@app.route("/debug-auth")
def debug_auth():
    return {
        "USER_env": username_app,
        "PASSWORD_set": password_app is not None,
        "all_env_vars": dict(os.environ)
    }


def authenticate():
    return Response(
        'Authentication required', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        print(f"DEBUG - Auth object: {auth}")
        if auth:
            print(f"DEBUG - Username provided: {auth.username}")
            print(f"DEBUG - Expected username: {username_app}")

        if not auth or auth.username != username_app or auth.password != password_app:
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route("/")
@requires_auth
def index():
    return "Hello, you are authenticated!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)