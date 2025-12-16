from flask import Blueprint
from flasgger import swag_from
from ..controller.orders.doctor_controller import DoctorController
from flask_jwt_extended import jwt_required, get_jwt_identity

doctor_bp = Blueprint("doctor", __name__)
doctor_controller = DoctorController()


@doctor_bp.route("/doctor", methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Doctor'],
    'security': [{'BearerAuth': []}],
    'responses': {
        200: {
            'description': 'List of all doctors',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "John", "surname": "Doe", "doctor_specialization_id": 2, "doctor_contact_id": 1}
                ]
            }
        },
        401: {'description': 'Missing or invalid token'}
    }
})
def get_doctor():
    user_id = get_jwt_identity()
    return doctor_controller.get_all()


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Doctor'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {'name': 'doctor_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Doctor details',
            'examples': {
                'application/json': {"id": 1, "name": "John", "surname": "Doe", "doctor_specialization_id": 2, "doctor_contact_id": 1}
            }
        },
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Doctor not found'}
    }
})
def get_doctor_by_id(doctor_id):
    user_id = get_jwt_identity()
    return doctor_controller.get_by_id(doctor_id)


@doctor_bp.route("/doctor", methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Doctor'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'doctor_specialization_id': {'type': 'integer'},
                    'doctor_contact_id': {'type': 'integer'}
                },
                'required': ['name', 'surname', 'doctor_specialization_id', 'doctor_contact_id']
            }
        }
    ],
    'responses': {
        201: {'description': 'Doctor created successfully'},
        401: {'description': 'Missing or invalid token'}
    }
})
def add_doctor():
    user_id = get_jwt_identity()
    return doctor_controller.create()


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['PATCH'])
@jwt_required()
@swag_from({
    'tags': ['Doctor'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {'name': 'doctor_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'doctor_specialization_id': {'type': 'integer'},
                    'doctor_contact_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Doctor updated successfully'},
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Doctor not found'}
    }
})
def update_doctor(doctor_id):
    user_id = get_jwt_identity()
    return doctor_controller.update(doctor_id)


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['DELETE'])
@jwt_required()
@swag_from({
    'tags': ['Doctor'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {'name': 'doctor_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Doctor deleted successfully'},
        401: {'description': 'Missing or invalid token'},
        404: {'description': 'Doctor not found'}
    }
})
def delete_doctor(doctor_id):
    user_id = get_jwt_identity()
    return doctor_controller.delete(doctor_id)