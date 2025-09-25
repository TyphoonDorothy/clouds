from flask import Blueprint
from ..controller.orders.dish_controller import DishController

dish_bp = Blueprint("dishes", __name__)
dish_controller = DishController()


@dish_bp.route("/dish", methods=['GET'])
def get_dishes():
    """
    Get all dishes
    ---
    tags:
      - Dish
    responses:
      200:
        description: List of all dishes
    """
    return dish_controller.get_all()


@dish_bp.route("/dish/<int:dish_id>", methods=['GET'])
def get_dish_by_id(dish_id):
    """
    Get dish by ID
    ---
    tags:
      - Dish
    parameters:
      - name: dish_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Dish retrieved
    """
    return dish_controller.get_by_id(dish_id)


@dish_bp.route("/dish", methods=['POST'])
def add_dish():
    """
    Add new dish
    ---
    tags:
      - Dish
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
    """
    return dish_controller.create()


@dish_bp.route("/dish/<int:dish_id>", methods=['PATCH'])
def update_dish(dish_id):
    """
    Update an existing dish
    ---
    tags:
      - Dish
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
    """
    return dish_controller.update(dish_id)


@dish_bp.route("/dish/<int:dish_id>", methods=['DELETE'])
def delete_dish(dish_id):
    """
    Delete a dish
    ---
    tags:
      - Dish
    parameters:
      - name: dish_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Dish deleted
    """
    return dish_controller.delete(dish_id)


# @dish_bp.route("/dish/aggregate", methods=["GET"])
# def get_dish_aggregate():
#     """
#     Get dish aggregate stats (example: total calories, avg calories, etc.)
#     ---
#     tags:
#       - Dish
#     responses:
#       200:
#         description: Aggregate data for dishes
#     """
#     return dish_controller.get_dish_aggregate()
