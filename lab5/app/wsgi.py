from my_project import create_app
from flask import Flask, request, Response, make_response
from functools import wraps
import os, sys
sys.path.append(os.path.dirname(__file__))

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)