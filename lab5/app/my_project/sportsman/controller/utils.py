from flask import jsonify

def handle_response(data, status_code=200):
    return jsonify(data), status_code

def handle_error(message, status_code=400):
    return jsonify({"error": message}), status_code