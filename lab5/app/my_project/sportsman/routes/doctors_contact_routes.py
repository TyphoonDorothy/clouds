from flask import Blueprint, jsonify, request
from flasgger import swag_from
from my_project.sportsman.controller.orders.doctors_contact_controller import DoctorsContactController

doctors_contact_bp = Blueprint("doctors_contact", __name__)
doctors_contact_controller = DoctorsContactController()


@doctors_contact_bp.route("/doctors_contact", methods=['GET'])
@swag_from({
    'tags': ['DoctorsContact'],
    'responses': {
        200: {
            'description': 'List of all doctors contacts',
            'examples': {
                'application/json': [
                    {"id": 1, "phone": "+123456789", "email": "doc@example.com"}
                ]
            }
        }
    }
})
def get_doctors_contact():
    return doctors_contact_controller.get_all()


@doctors_contact_bp.route("/doctors_contact", methods=['POST'])
@swag_from({
    'tags': ['DoctorsContact'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'phone': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['phone', 'email']
            }
        }
    ],
    'responses': {
        201: {'description': 'Doctors contact created successfully'}
    }
})
def add_doctors_contact():
    return doctors_contact_controller.create()


@doctors_contact_bp.route("/doctors_contact/<int:doctors_contact_id>", methods=['PATCH'])
@swag_from({
    'tags': ['DoctorsContact'],
    'parameters': [
        {'name': 'doctors_contact_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'phone': {'type': 'string'},
                    'email': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Doctors contact updated successfully'},
        404: {'description': 'Doctors contact not found'}
    }
})
def update_doctors_contact(doctors_contact_id):
    return doctors_contact_controller.update(doctors_contact_id)


@doctors_contact_bp.route("/doctors_contact/<int:doctors_contact_id>", methods=['DELETE'])
@swag_from({
    'tags': ['DoctorsContact'],
    'parameters': [
        {'name': 'doctors_contact_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Doctors contact deleted successfully'},
        404: {'description': 'Doctors contact not found'}
    }
})
def delete_doctors_contact(doctors_contact_id):
    return doctors_contact_controller.delete(doctors_contact_id)
