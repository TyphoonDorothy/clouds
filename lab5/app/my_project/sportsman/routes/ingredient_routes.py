from flask import Blueprint
from flasgger import swag_from
from my_project.sportsman.controller.orders.ingredient_controller import IngredientController

ingredient_bp = Blueprint("ingredients", __name__)
ingredient_controller = IngredientController()

@ingredient_bp.route("/ingredients", methods=['GET'])
@swag_from({
    'tags': ['Ingredient'],
    'responses': {
        200: {
            'description': 'List of all ingredients',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "Sugar", "calories": 387.0}
                ]
            }
        }
    }
})
def get_ingredients():
    return ingredient_controller.get_all()

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['GET'])
@swag_from({
    'tags': ['Ingredient'],
    'parameters': [
        {'name': 'ingredient_id', 'in': 'path', 'type': 'integer', 'required': True,
         'description': 'ID of the ingredient'}
    ],
    'responses': {
        200: {
            'description': 'Ingredient details',
            'examples': {
                'application/json': {"id": 1, "name": "Sugar", "calories": 387.0}
            }
        },
        404: {'description': 'Ingredient not found'}
    }
})
def get_ingredient_by_id(ingredient_id):
    return ingredient_controller.get_by_id(ingredient_id)

@ingredient_bp.route("/ingredients", methods=['POST'])
@swag_from({
    'tags': ['Ingredient'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'calories': {'type': 'number'}
                },
                'required': ['name', 'calories']
            }
        }
    ],
    'responses': {
        201: {'description': 'Ingredient created successfully'}
    }
})
def add_ingredient():
    return ingredient_controller.create()

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['PATCH'])
@swag_from({
    'tags': ['Ingredient'],
    'parameters': [
        {'name': 'ingredient_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'calories': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Ingredient updated successfully'},
        404: {'description': 'Ingredient not found'}
    }
})
def update_ingredient(ingredient_id): 
    return ingredient_controller.update(ingredient_id)

@ingredient_bp.route("/ingredients/<int:ingredient_id>", methods=['DELETE'])
@swag_from({
    'tags': ['Ingredient'],
    'parameters': [
        {'name': 'ingredient_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Ingredient deleted successfully'},
        404: {'description': 'Ingredient not found'}
    }
})
def delete_ingredient(ingredient_id):
    return ingredient_controller.delete(ingredient_id)
