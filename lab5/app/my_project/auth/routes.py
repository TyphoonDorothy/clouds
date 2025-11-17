from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import check_password_hash

# correct import for model in the same package
from .model import User
from my_project.database import db

auth_bp = Blueprint("auth", __name__)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        print("[JWT] Login attempt with missing username/password")
        return jsonify({"msg": "username and password required"}), 400

    user = db.session.query(User).filter_by(username=username).first()
    if not user:
        print(f"[JWT] Login failed: user not found: {username}")
        return jsonify({"msg": "Invalid credentials"}), 401

    if not check_password_hash(user.password_hash, password):
        print(f"[JWT] Login failed: bad password for user: {username} (id={user.id})")
        return jsonify({"msg": "Invalid credentials"}), 401

    access = create_access_token(identity=user.id)
    refresh = create_refresh_token(identity=user.id)

    print(f"[JWT] Created access token for user: id={user.id} username={user.username}")
    print(f"[JWT] Created refresh token for user: id={user.id} username={user.username}")

    return jsonify(access_token=access, refresh_token=refresh), 200


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access = create_access_token(identity=current_user)
    print(f"[JWT] Refresh used by user id={current_user} — new access token created")
    return jsonify(access_token=new_access), 200


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    user_id = get_jwt_identity()
    jwt_data = get_jwt()
    jti = jwt_data.get("jti")
    # Optional: add revocation to Redis here
    print(f"[JWT] Logout requested by user id={user_id}, jti={jti} (would add to blacklist if enabled)")
    return jsonify({"msg": "logged out"}), 200


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    print(f"[JWT] Protected route accessed by user id={user_id}")
    # Optionally fetch user info to return
    user = db.session.query(User).get(user_id)
    username = user.username if user else None
    return jsonify({"hello": f"user {user_id}", "username": username}), 200
