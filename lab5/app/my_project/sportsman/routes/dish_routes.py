from flask import Blueprint
from ..controller.orders.dish_controller import DishController

dish_bp = Blueprint("dishes", __name__)
dish_controller = DishController()

@dish_bp.route("/dish", methods=['GET'])
def get_dish():
    return dish_controller.get_all()

@dish_bp.route("/dish/<int:dish_id>", methods=['GET'])
def get_dish_by_id(dish_id):
    return dish_controller.get_by_id(dish_id)

@dish_bp.route("/dish", methods=['POST'])
def add_dish():
    return dish_controller.create()

# @dish_bp.route("/dish/<int:dish_id>", methods=['PATCH'])
# def update_dish(dish_id):
#     return dish_controller.update(dish_id)

@dish_bp.route("/dish/<int:dish_id>", methods=['DELETE'])
def delete_dish(dish_id):
    return dish_controller.delete(dish_id)

# @dish_bp.route('/dish/insert', methods=['POST'])
# def insert_terminal():
#     return dish_controller.insert_dish()

@dish_bp.route("/dish/aggregate", methods=["GET"])
def get_dish_aggregate():
    return dish_controller.get_dish_aggregate()