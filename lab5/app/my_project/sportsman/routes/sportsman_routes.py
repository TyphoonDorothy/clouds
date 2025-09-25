from flask import Blueprint
from flasgger import swag_from
from my_project.sportsman.controller.orders.sportsman_controller import SportsmanController

sportsman_bp = Blueprint("sportsman", __name__)
sportsman_controller = SportsmanController()

@sportsman_bp.route("/sportsman", methods=['GET'])
@swag_from({
    'tags': ['Sportsman'],
    'responses': {
        200: {
            'description': 'List of all sportsmen',
            'examples': {
                'application/json': [
                    {
                        "id": 1,
                        "name": "John",
                        "surname": "Doe",
                        "age": 25,
                        "height": 180,
                        "weight": 75
                    }
                ]
            }
        }
    }
})
def get_sportsmen():
    return sportsman_controller.get_all()


@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['GET'])
@swag_from({
    'tags': ['Sportsman'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the sportsman'}
    ],
    'responses': {
        200: {'description': 'Sportsman details',
              'examples': {'application/json': {
                  "id": 1,
                  "name": "John",
                  "surname": "Doe",
                  "age": 25,
                  "height": 180,
                  "weight": 75
              }}},
        404: {'description': 'Sportsman not found'}
    }
})
def get_sportsman_by_id(sportsman_id):
    return sportsman_controller.get_by_id(sportsman_id)


@sportsman_bp.route("/sportsman", methods=['POST'])
@swag_from({
    'tags': ['Sportsman'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'age': {'type': 'integer'},
                    'height': {'type': 'number'},
                    'weight': {'type': 'number'}
                },
                'required': ['name', 'surname', 'age', 'height', 'weight']
            }
        }
    ],
    'responses': {
        201: {'description': 'Sportsman created successfully'}
    }
})
def add_sportsman():
    return sportsman_controller.create()


@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['PATCH'])
@swag_from({
    'tags': ['Sportsman'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'age': {'type': 'integer'},
                    'height': {'type': 'number'},
                    'weight': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Sportsman updated successfully'},
        404: {'description': 'Sportsman not found'}
    }
})
def update_sportsmen(sportsman_id):
    return sportsman_controller.update(sportsman_id)


@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['DELETE'])
@swag_from({
    'tags': ['Sportsman'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Sportsman deleted successfully'},
        404: {'description': 'Sportsman not found'}
    }
})
def delete_sportsman(sportsman_id):
    return sportsman_controller.delete(sportsman_id)


# @sportsman_bp.route("/sportsman/noname", methods=['POST'])
# @swag_from({
#     'tags': ['Sportsman'],
#     'responses': {
#         201: {'description': 'Inserted noname rows successfully'}
#     }
# })
# def insert_nonames():
#     return sportsman_controller.insert_noname_rows()
