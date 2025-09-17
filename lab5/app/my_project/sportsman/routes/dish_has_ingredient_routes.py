from flask import Blueprint
from my_project.sportsman.controller.orders.dish_has_ingredient_controller import DishHasIngredientController


dish_has_ingredient_bp = Blueprint("dish_has_ingredient", __name__)
dish_has_ingredient_controller = DishHasIngredientController()

@dish_has_ingredient_bp.route("/dish_has_ingredient", methods=['GET'])
def get_dishes_has_ingredient():
    return dish_has_ingredient_controller.get_all()

@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_has_ingredient_id>", methods=['GET'])
def get_dish_has_ingredient_by_id(dish_has_ingredient_id):
    return dish_has_ingredient_controller.get_by_id(program_has_dish_id)

@dish_has_ingredient_bp.route("/dish_has_ingredient", methods=['POST'])
def add_dish_has_ingredient():
    return dish_has_ingredient_controller.create()

@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_has_ingredient_id>", methods=['PATCH'])
def update_dish_has_ingredient(sportsman_id):
    return dish_has_ingredient_controller.update(dish_has_ingredient_id)

@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_has_ingredient_id>", methods=['DELETE'])
def delete_dish_has_ingredient(dish_has_ingredient_id):
    return dish_has_ingredient_controller.delete(dish_has_ingredient_id)