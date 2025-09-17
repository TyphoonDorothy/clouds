from flask import Blueprint, jsonify, request
from my_project.sportsman.controller.orders.doctor_specialization_controller import DoctorSpecializationController

doctor_specialization_bp = Blueprint("doctor_specialization", __name__)
doctor_specialization_controller = DoctorSpecializationController()

@doctor_specialization_bp.route("/doctor_specialization", methods=['GET'])
def get_doctor_specialization():
    return doctor_specialization_controller.get_all()

@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['GET'])
def get_doctor_specialization_by_id(doctor_specialization_id):
    return doctor_specialization_controller.get_by_id(doctor_specialization_id)

# Виправлено: параметр і маршрут тепер узгоджені
@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>/doctors", methods=['GET'])
def get_doctors_by_specialization(doctor_specialization_id):
    return jsonify(doctor_specialization_controller.service.get_doctors_by_specialization(doctor_specialization_id))

@doctor_specialization_bp.route("/doctor_specialization", methods=['POST'])
def add_doctor_specialization():
    return doctor_specialization_controller.create()

@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['PATCH'])
def update_doctor_specialization(doctor_specialization_id):
    return doctor_specialization_controller.update(doctor_specialization_id)

@doctor_specialization_bp.route("/doctor_specialization/<int:doctor_specialization_id>", methods=['DELETE'])
def delete_doctor_specialization(doctor_specialization_id):
    return doctor_specialization_controller.delete(doctor_specialization_id)
