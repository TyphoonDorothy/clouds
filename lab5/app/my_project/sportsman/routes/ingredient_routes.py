from flask import Blueprint
from my_project.sportsman.controller.orders.ingredient_controller import IngredientController


ingredient_bp = Blueprint("ingredients", __name__)
ingredient_controller = IngredientController()

@ingredient_bp.route("/ingredients", methods=['GET'])
def get_ingredients():
    return ingredient_controller.get_all()

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['GET'])
def get_ingredient_by_id(ingredient_id):
    return ingredient_controller.get_by_id(ingredient_id)

@ingredient_bp.route("/ingredients", methods=['POST'])
def add_ingredient():
    return ingredient_controller.create()

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['PATCH'])
def update_ingridient(ingredient_id):
    return ingredient_controller.update(ingredient_id)

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['DELETE'])
def delete_ingredient(ingredient_id):
    return ingredient_controller.delete(ingredient_id)