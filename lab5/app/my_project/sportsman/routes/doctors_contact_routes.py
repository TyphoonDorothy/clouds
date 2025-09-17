from flask import Blueprint
from my_project.sportsman.controller.orders.doctors_contact_controller import DoctorsContactController


doctors_contact_bp = Blueprint("doctors_contact", __name__)
doctors_contact_controller = DoctorsContactController()

@doctors_contact_bp.route("/doctors_contact", methods=['GET'])
def get_doctors_contact():
    return doctors_contact_controller.get_all()

@doctors_contact_bp.route("/doctors_contact/<int:doctors_contact_id>", methods=['GET'])
def get_doctors_contact_by_id(doctors_contact_id):
    return doctors_contact_controller.get_by_id(doctors_contact_id)

@doctors_contact_bp.route("/doctors_contact", methods=['POST'])
def add_doctors_contact():
    return doctors_contact_controller.create()

@doctors_contact_bp.route("/doctors_contact/<int:doctors_contact_id>", methods=['PATCH'])
def update_doctors_contact(doctors_contact_id):
    return doctors_contact_controller.update(doctors_contact_id)

@doctors_contact_bp.route("/doctors_contact/<int:doctors_contact_id>", methods=['DELETE'])
def delete_doctors_contact(doctors_contact_id):
    return doctors_contact_controller.delete(doctors_contact_id)