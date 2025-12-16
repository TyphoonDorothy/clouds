from flask import Blueprint
from flasgger.utils import swag_from
from my_project.sportsman.controller.orders.dish_has_ingredient_controller import DishHasIngredientController
from flask_jwt_extended import jwt_required, get_jwt_identity

dish_has_ingredient_bp = Blueprint("dish_has_ingredient", __name__)
dish_has_ingredient_controller = DishHasIngredientController()

@dish_has_ingredient_bp.route("/dish_has_ingredient", methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['DishHasIngredient'],
    'security': [{'BearerAuth': []}],
    'responses': {
        200: {
            'description': 'List all dish-ingredient associations',
            'examples': {
                'application/json': [
                    {"dish_id": 1, "ingredient_id": 2},
                    {"dish_id": 1, "ingredient_id": 3}
                ]
            }
        },
        401: {'description': 'Missing or invalid token'}
    }
})
def get_dishes_has_ingredient():
    user_id = get_jwt_identity()
    return dish_has_ingredient_controller.get_all()


@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_id>/<int:ingredient_id>", methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['DishHasIngredient'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'dish_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'ingredient_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Return specific dish-ingredient link',
            'examples': {
                'application/json': {"dish_id": 1, "ingredient_id": 2}
            }
        },
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Association not found'}
    }
})
def get_dish_has_ingredient_by_id(dish_id, ingredient_id):
    user_id = get_jwt_identity()
    return dish_has_ingredient_controller.get_by_id(dish_id, ingredient_id)


@dish_has_ingredient_bp.route("/dish_has_ingredient", methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['DishHasIngredient'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'dish_id': {'type': 'integer'},
                    'ingredient_id': {'type': 'integer'}
                },
                'required': ['dish_id', 'ingredient_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Created new dish-ingredient link',
            'examples': {
                'application/json': {"dish_id": 1, "ingredient_id": 2}
            }
        },
        401: {'description': 'Missing or invalid token'}
    }
})
def add_dish_has_ingredient():
    user_id = get_jwt_identity()
    return dish_has_ingredient_controller.create()


@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_id>/<int:ingredient_id>", methods=['PATCH'])
@jwt_required()
@swag_from({
    'tags': ['DishHasIngredient'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {'name': 'dish_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'ingredient_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'dish_id': {'type': 'integer'},
                    'ingredient_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Updated association',
            'examples': {
                'application/json': {"dish_id": 1, "ingredient_id": 3}
            }
        },
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Association not found'}
    }
})
def update_dish_has_ingredient(dish_id, ingredient_id):
    user_id = get_jwt_identity()
    return dish_has_ingredient_controller.update(dish_id, ingredient_id)


@dish_has_ingredient_bp.route("/dish_has_ingredient/<int:dish_id>/<int:ingredient_id>", methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['DishHasIngredient'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {'name': 'dish_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'ingredient_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        204: {'description': 'Association deleted'},
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Association not found'}
    }
})
def delete_dish_has_ingredient(dish_id, ingredient_id):
    user_id = get_jwt_identity()
    return dish_has_ingredient_controller.delete(dish_id, ingredient_id)