from flask import Blueprint
from ..controller.orders.user_controller import UserController
from flask_jwt_extended import JWTManager, create_access_token, jwt_required


user_bp = Blueprint("user", __name__)
user_controller = UserController()


@user_bp.route("/login", methods=['POST'])
def user_dish():
    """
    Create a new user
    ---
    tags:
      - User
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
              password: string
    responses:
      201:
        description: user created
    """
    return user_controller.create()



@user_bp.route("/login/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User deleted
    """
    return user_controller.delete(user_id)
