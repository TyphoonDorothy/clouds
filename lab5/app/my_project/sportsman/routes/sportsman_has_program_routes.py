from flask import Blueprint
from flasgger import swag_from
from my_project.sportsman.controller.orders.sportsman_has_program_controller import SportsmanHasProgramController

sportsman_has_program_bp = Blueprint("sportsman_has_program", __name__)
controller = SportsmanHasProgramController()

@sportsman_has_program_bp.route("/sportsman_has_program", methods=['GET'])
@swag_from({
    'tags': ['SportsmanHasProgram'],
    'responses': {
        200: {
            'description': 'List of all Sportsman-Program relationships',
            'examples': {
                'application/json': [
                    {"sportsman_id": 1, "program_id": 2}
                ]
            }
        }
    }
})
def get_sportsmen_has_program():
    return controller.get_all()


@sportsman_has_program_bp.route("/sportsman_has_program/<int:sportsman_id>/<int:program_id>", methods=['GET'])
@swag_from({
    'tags': ['SportsmanHasProgram'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True},
    ],
    'responses': {
        200: {'description': 'Relationship details', 'examples': {'application/json': {"sportsman_id": 1, "program_id": 2}}},
        404: {'description': 'Relationship not found'}
    }
})
def get_sportsman_has_program_by_id(sportsman_id, program_id):
    return controller.get_by_id(sportsman_id, program_id)


@sportsman_has_program_bp.route("/sportsman_has_program", methods=['POST'])
@swag_from({
    'tags': ['SportsmanHasProgram'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'sportsman_id': {'type': 'integer'},
                    'program_id': {'type': 'integer'}
                },
                'required': ['sportsman_id', 'program_id']
            }
        }
    ],
    'responses': {201: {'description': 'Relationship created successfully'}}
})
def add_sportsman_has_program():
    return controller.create()

@sportsman_has_program_bp.route(
    "/sportsman_has_program/<int:sportsman_id>/<int:program_id>", methods=['PATCH']
)
@swag_from({
    'tags': ['SportsmanHasProgram'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'new_sportsman_id': {'type': 'integer'},
                    'new_program_id': {'type': 'integer'}
                },
                'required': ['new_sportsman_id', 'new_program_id']
            }
        }
    ],
    'responses': {
        200: {'description': 'Relationship updated successfully'},
        404: {'description': 'Original relationship not found'}
    }
})
def update_sportsman_has_program(sportsman_id, program_id):
    return controller.update(sportsman_id, program_id)


@sportsman_has_program_bp.route("/sportsman_has_program/<int:sportsman_id>/<int:program_id>", methods=['DELETE'])
@swag_from({
    'tags': ['SportsmanHasProgram'],
    'parameters': [
        {'name': 'sportsman_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True},
    ],
    'responses': {
        200: {'description': 'Relationship deleted successfully'},
        404: {'description': 'Relationship not found'}
    }
})
def delete_sportsman_has_program(sportsman_id, program_id):
    return controller.delete(sportsman_id, program_id)


# @sportsman_has_program_bp.route("/sportsman_has_program/insert", methods=['POST'])
# @swag_from({
#     'tags': ['SportsmanHasProgram'],
#     'responses': {201: {'description': 'Junction entry inserted'}}
# })
# def insert_sportsman_program():
#     return controller.insert_junction_entry()
