from my_project import create_app
from flask import Flask, request, Response
from functools import wraps  # Import this
import os

app = create_app()

username_app = os.getenv('USER')
password_app = os.getenv('PASSWORD')

def authenticate():
    """Send a 401 response that enables basic auth"""
    return Response(
        'Authentication required\n'
        'Please provide valid credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    @wraps(f)  # Use this instead of manual __name__ assignment
    def decorated(*args, **kwargs):
        auth = request.authorization
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