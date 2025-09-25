from my_project import create_app
from flask import Flask, request, Response
import os

app = create_app()

username_app = os.getenv('USER')
password_app = os.getenv('PASSWORD')

def authenticate():
    return Response(
        "Authentication required", 401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != username_app or auth.password != password_app:
            return authenticate()
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__  # Needed for Flask routing
    return decorated

@app.route("/")
@requires_auth
def index():
    return "Hello, you are authenticated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
