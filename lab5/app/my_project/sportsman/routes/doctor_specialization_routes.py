from flask import Blueprint, jsonify, request
from flasgger import swag_from
from my_project.sportsman.controller.orders.doctor_specialization_controller import DoctorSpecializationController

doctor_specialization_bp = Blueprint("doctor_specialization", __name__)
doctor_specialization_controller = DoctorSpecializationController()


@doctor_specialization_bp.route("/doctor_specialization", methods=['GET'])
@swag_from({
    'tags': ['DoctorSpecialization'],
    'responses': {
        200: {
            'description': 'List of all doctor specializations',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "Cardiology"}
                ]
            }
        }
    }
})
def get_doctor_specialization():
    return doctor_specialization_controller.get_all()


@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['GET'])
@swag_from({
    'tags': ['DoctorSpecialization'],
    'parameters': [
        {'name': 'doctor_specialization_id', 'in': 'path', 'type': 'integer', 'required': True,
         'description': 'ID of the doctor specialization'}
    ],
    'responses': {
        200: {
            'description': 'Doctor specialization details',
            'examples': {
                'application/json': {"id": 1, "name": "Cardiology"}
            }
        },
        404: {'description': 'Specialization not found'}
    }
})
def get_doctor_specialization_by_id(doctor_specialization_id):
    return doctor_specialization_controller.get_by_id(doctor_specialization_id)


# @doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>/doctors", methods=['GET'])
# @swag_from({
#     'tags': ['DoctorSpecialization'],
#     'parameters': [
#         {'name': 'doctor_specialization_id', 'in': 'path', 'type': 'integer', 'required': True,
#          'description': 'ID of the doctor specialization'}
#     ],
#     'responses': {
#         200: {
#             'description': 'List of doctors with this specialization',
#             'examples': {
#                 'application/json': [
#                     {"id": 1, "name": "John", "surname": "Doe", "doctor_specialization_id": 1, "doctor_contact_id": 1}
#                 ]
#             }
#         }
#     }
# })
# def get_doctors_by_specialization(doctor_specialization_id):
#     return jsonify(doctor_specialization_controller.service.get_doctors_by_specialization(doctor_specialization_id))


@doctor_specialization_bp.route("/doctor_specialization", methods=['POST'])
@swag_from({
    'tags': ['DoctorSpecialization'],
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
        201: {'description': 'Doctor specialization created successfully'}
    }
})
def add_doctor_specialization():
    return doctor_specialization_controller.create()


@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['PATCH'])
@swag_from({
    'tags': ['DoctorSpecialization'],
    'parameters': [
        {'name': 'doctor_specialization_id', 'in': 'path', 'type': 'integer', 'required': True},
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
        200: {'description': 'Doctor specialization updated successfully'},
        404: {'description': 'Specialization not found'}
    }
})
def update_doctor_specialization(doctor_specialization_id):
    return doctor_specialization_controller.update(doctor_specialization_id)


@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['DELETE'])
@swag_from({
    'tags': ['DoctorSpecialization'],
    'parameters': [
        {'name': 'doctor_specialization_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Doctor specialization deleted successfully'},
        404: {'description': 'Specialization not found'}
    }
})
def delete_doctor_specialization(doctor_specialization_id):
    return doctor_specialization_controller.delete(doctor_specialization_id)
