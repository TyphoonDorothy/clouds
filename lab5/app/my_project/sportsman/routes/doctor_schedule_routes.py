from flask import Blueprint
from ..controller.orders.doctor_schedule_controller import DoctorScheduleController

doctor_schedule_bp = Blueprint("doctor_schedule", __name__)
doctor_schedule_controller = DoctorScheduleController()

@doctor_schedule_bp.route("/doctor_schedule", methods=['GET'])
def get_all_schedules():
    return doctor_schedule_controller.get_all()

@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['GET'])
def get_schedule_by_id(schedule_id):
    return doctor_schedule_controller.get_by_id(schedule_id)

@doctor_schedule_bp.route("/doctor_schedule", methods=['POST'])
def add_schedule():
    return doctor_schedule_controller.create()

@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['PATCH'])
def update_schedule(schedule_id):
    return doctor_schedule_controller.update(schedule_id)

@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['DELETE'])
def delete_schedule(schedule_id):
    return doctor_schedule_controller.delete(schedule_id)
