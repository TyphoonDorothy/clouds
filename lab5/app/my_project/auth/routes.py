# my_project/auth/routes.py
from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import check_password_hash
from .model import User
from my_project.database import db
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint("auth", __name__)

def create_user_in_db(username: str, password: str):
    """
    Helper: creates a user row and commits. Raises ValueError on validation error.
    Returns the created User instance.
    """
    username = (username or "").strip()
    if not username:
        raise ValueError("username required")
    if not password:
        raise ValueError("password required")

    # check existence
    existing = db.session.query(User).filter_by(username=username).first()
    if existing:
        raise ValueError("username_exists")

    pw_hash = generate_password_hash(password)
    user = User(username=username, password_hash=pw_hash)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        raise ValueError("username_exists") from e

    current_app.logger.info("[AUTH] Created user id=%s username=%s", user.id, user.username)
    print(f"[AUTH] created user id={user.id} username={user.username}", flush=True)

    return user


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    try:
        user = create_user_in_db(username=username, password=password)
    except ValueError as e:
        msg = str(e)
        if msg == "username_exists":
            current_app.logger.info("[AUTH] Register attempt failed - username exists: %s", username)
            return jsonify({"msg": "username already exists"}), 400
        else:
            current_app.logger.info("[AUTH] Register attempt failed - %s", msg)
            return jsonify({"msg": msg}), 400
    except Exception as e:
        current_app.logger.exception("[AUTH] Unexpected error creating user")
        return jsonify({"msg": "internal error"}), 500

    # Generate JWT tokens immediately
    access = create_access_token(identity=user.id)
    refresh = create_refresh_token(identity=user.id)

    print(f"[JWT] Created access token for new user id={user.id} username={user.username}", flush=True)
    print(f"[JWT] Created refresh token for new user id={user.id} username={user.username}", flush=True)

    return jsonify({
        "id": user.id,
        "username": user.username,
        "access_token": access,
        "refresh_token": refresh
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User login - returns access and refresh tokens
    ---
    tags:
      - auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
          required:
            - username
            - password
    responses:
      200:
        description: tokens
        schema:
          type: object
          properties:
            access_token:
              type: string
            refresh_token:
              type: string
      400:
        description: missing fields
      401:
        description: invalid credentials
    """
    data = request.json or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        current_app.logger.info("[JWT] Login attempt missing username/password")
        return jsonify({"msg": "username and password required"}), 400

    user = db.session.query(User).filter_by(username=username).first()
    if not user:
        current_app.logger.info(f"[JWT] Login failed: user not found: {username}")
        return jsonify({"msg": "Invalid credentials"}), 401

    if not check_password_hash(user.password_hash, password):
        current_app.logger.info(f"[JWT] Login failed: bad password for user: {username} (id={user.id})")
        return jsonify({"msg": "Invalid credentials"}), 401

    access = create_access_token(identity=user.id)
    refresh = create_refresh_token(identity=user.id)

    # log (use debug for token string) and forced prints for immediate visibility
    current_app.logger.info(f"[JWT] Created tokens for user id={user.id} username={user.username}")
    current_app.logger.debug(f"[JWT] access={access}")
    print(f"[JWT] access={access}", flush=True)
    print(f"[JWT] refresh={refresh}", flush=True)

    return jsonify(access_token=access, refresh_token=refresh), 200


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """
    Refresh access token using a refresh JWT
    ---
    tags:
      - auth
    security:
      - BearerAuth: []
    responses:
      200:
        description: new access token
        schema:
          type: object
          properties:
            access_token:
              type: string
      401:
        description: invalid or expired refresh token
    """
    current_user = get_jwt_identity()
    new_access = create_access_token(identity=current_user)
    current_app.logger.info(f"[JWT] Refresh used by user id={current_user}")
    print(f"[JWT] new_access={new_access}", flush=True)
    return jsonify(access_token=new_access), 200


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    Logout (example) — demonstrates blacklisting hook point
    ---
    tags:
      - auth
    security:
      - BearerAuth: []
    responses:
      200:
        description: logged out
    """
    user_id = get_jwt_identity()
    jwt_data = get_jwt()
    jti = jwt_data.get("jti")
    # Here you would add jti to your revocation store (redis) if using immediate revocation.
    current_app.logger.info(f"[JWT] Logout requested by user id={user_id}, jti={jti}")
    print(f"[JWT] logout_jti={jti}", flush=True)
    return jsonify({"msg": "logged out"}), 200


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """
    Protected endpoint example
    ---
    tags:
      - auth
    security:
      - BearerAuth: []
    responses:
      200:
        description: OK
        schema:
          type: object
          properties:
            hello:
              type: string
            username:
              type: string
      401:
        description: missing token
    """
    user_id = get_jwt_identity()
    current_app.logger.info(f"[JWT] Protected route accessed by user id={user_id}")
    user = db.session.get(User, user_id)
    username = user.username if user else None
    return jsonify({"hello": f"user {user_id}", "username": username}), 200
