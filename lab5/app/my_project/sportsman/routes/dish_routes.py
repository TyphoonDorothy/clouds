from flask import Blueprint
from ..controller.orders.dish_controller import DishController
from flask_jwt_extended import jwt_required, get_jwt_identity

dish_bp = Blueprint("dishes", __name__)
dish_controller = DishController()


@dish_bp.route("/dish", methods=['GET'])
@jwt_required()
def get_dishes():
    """
    Get all dishes
    ---
    tags:
      - Dish
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of all dishes
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
    return dish_controller.get_all()


@dish_bp.route("/dish/<int:dish_id>", methods=['GET'])
@jwt_required()
def get_dish_by_id(dish_id):
    """
    Get dish by ID
    ---
    tags:
      - Dish
    security:
      - BearerAuth: []
    parameters:
      - name: dish_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Dish retrieved
      401:
        description: Missing or invalid token
      404:
        description: Dish not found
    """
    user_id = get_jwt_identity()
    return dish_controller.get_by_id(dish_id)


@dish_bp.route("/dish", methods=['POST'])
@jwt_required()
def add_dish():
    """
    Add new dish
    ---
    tags:
      - Dish
    security:
      - BearerAuth: []
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            calories:
              type: number
    responses:
      201:
        description: Dish created
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
    return dish_controller.create()


@dish_bp.route("/dish/<int:dish_id>", methods=['PATCH'])
@jwt_required()
def update_dish(dish_id):
    """
    Update an existing dish
    ---
    tags:
      - Dish
    security:
      - BearerAuth: []
    parameters:
      - name: dish_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            calories:
              type: number
    responses:
      200:
        description: Dish updated
      401:
        description: Missing or invalid token
      404:
        description: Dish not found
    """
    user_id = get_jwt_identity()
    return dish_controller.update(dish_id)


@dish_bp.route("/dish/<int:dish_id>", methods=['DELETE'])
@jwt_required()
def delete_dish(dish_id):
    """
    Delete a dish
    ---
    tags:
      - Dish
    security:
      - BearerAuth: []
    parameters:
      - name: dish_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Dish deleted
      401:
        description: Missing or invalid token
      404:
        description: Dish not found
    """
    user_id = get_jwt_identity()
    return dish_controller.delete(dish_id)


# @dish_bp.route("/dish/aggregate", methods=["GET"])
# @jwt_required()
# def get_dish_aggregate():
#     """
#     Get dish aggregate stats (example: total calories, avg calories, etc.)
#     ---
#     tags:
#       - Dish
#     security:
#       - BearerAuth: []
#     responses:
#       200:
#         description: Aggregate data for dishes
#       401:
#         description: Missing or invalid token
#     """
#     user_id = get_jwt_identity()
#     return dish_controller.get_dish_aggregate()