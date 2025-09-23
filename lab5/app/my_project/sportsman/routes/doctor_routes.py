from flask import Blueprint
from flasgger import swag_from
from ..controller.orders.doctor_controller import DoctorController

doctor_bp = Blueprint("doctor", __name__)
doctor_controller = DoctorController()


@doctor_bp.route("/doctor", methods=['GET'])
@swag_from({
    'tags': ['Doctor'],
    'responses': {
        200: {
            'description': 'List of all doctors',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "John", "surname": "Doe", "doctor_specialization_id": 2, "doctor_contact_id": 1}
                ]
            }
        }
    }
})
def get_doctor():
    return doctor_controller.get_all()


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['GET'])
@swag_from({
    'tags': ['Doctor'],
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
        404: {'description': 'Doctor not found'}
    }
})
def get_doctor_by_id(doctor_id):
    return doctor_controller.get_by_id(doctor_id)


@doctor_bp.route("/doctor", methods=['POST'])
@swag_from({
    'tags': ['Doctor'],
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
                    'doctor_contact_id': {'type': 'integer'}   # singular here
                },
                'required': ['name', 'surname', 'doctor_specialization_id', 'doctor_contact_id']
            }
        }
    ],
    'responses': {
        201: {'description': 'Doctor created successfully'}
    }
})
def add_doctor():
    return doctor_controller.create()


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['PATCH'])
@swag_from({
    'tags': ['Doctor'],
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
        404: {'description': 'Doctor not found'}
    }
})
def update_doctor(doctor_id):
    return doctor_controller.update(doctor_id)


@doctor_bp.route("/doctor/<int:doctor_id>", methods=['DELETE'])
@swag_from({
    'tags': ['Doctor'],
    'parameters': [
        {'name': 'doctor_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Doctor deleted successfully'},
        404: {'description': 'Doctor not found'}
    }
})
def delete_doctor(doctor_id):
    return doctor_controller.delete(doctor_id)
