from flask import Blueprint, jsonify, request
from flasgger import swag_from
from my_project.sportsman.controller.orders.program_controller import ProgramController

program_bp = Blueprint("programs", __name__)
program_controller = ProgramController()

@program_bp.route("/programs", methods=['GET'])
@swag_from({
    'tags': ['Program'],
    'responses': {
        200: {
            'description': 'List of all programs',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "Weight Loss"}
                ]
            }
        }
    }
})
def get_programs():
    return program_controller.get_all()

@program_bp.route("/programs/<int:program_id>", methods=['GET'])
@swag_from({
    'tags': ['Program'],
    'parameters': [
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the program'}
    ],
    'responses': {
        200: {'description': 'Program details', 'examples': {'application/json': {"id": 1, "name": "Weight Loss"}}},
        404: {'description': 'Program not found'}
    }
})
def get_program_by_id(program_id):
    return program_controller.get_by_id(program_id)

@program_bp.route("/programs", methods=['POST'])
@swag_from({
    'tags': ['Program'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {'description': 'Program created successfully'}
    }
})
def add_program():
    return program_controller.create()

@program_bp.route("/programs/<int:program_id>", methods=['PATCH'])
@swag_from({
    'tags': ['Program'],
    'parameters': [
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Program updated successfully'},
        404: {'description': 'Program not found'}
    }
})
def update_program(program_id):
    return program_controller.update(program_id)

@program_bp.route("/programs/<int:program_id>", methods=['DELETE'])
@swag_from({
    'tags': ['Program'],
    'parameters': [
        {'name': 'program_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Program deleted successfully'},
        404: {'description': 'Program not found'}
    }
})
def delete_program(program_id):
    return program_controller.delete(program_id)
