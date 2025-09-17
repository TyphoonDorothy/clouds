from flask import Blueprint
from ..controller.orders.doctor_controller import DoctorController

doctor_bp = Blueprint("doctor", __name__)
doctor_controller = DoctorController()

@doctor_bp.route("/doctor", methods=['GET'])
def get_doctor():
    return doctor_controller.get_all()

@doctor_bp.route("/doctor/<int:doctor_id>", methods=['GET'])
def get_doctor_by_id(doctor_id):
    return doctor_controller.get_by_id(doctor_id)

@doctor_bp.route("/doctor", methods=['POST'])
def add_doctor():
    return doctor_controller.create()

@doctor_bp.route("/doctor/<int:doctor_id>", methods=['PATCH'])
def update_doctor(doctor_id):
    return doctor_controller.update(doctor_id)

@doctor_bp.route("/doctor/<int:doctor_id>", methods=['DELETE'])
def delete_doctor(doctor_id):
    return doctor_controller.delete(doctor_id)

@doctor_bp.route('/doctor/generate', methods=['POST'])
def generate_databases_and_tables():
    return doctor_controller.generate_databases_and_tables()