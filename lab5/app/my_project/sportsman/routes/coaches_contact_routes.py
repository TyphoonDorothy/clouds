from flask import Blueprint
from my_project.sportsman.controller.orders.coaches_contact_controller import CoachesContactController


coaches_contact_bp = Blueprint("coaches_contact", __name__)
coaches_contact_controller = CoachesContactController()

@coaches_contact_bp.route("/coaches_contact", methods=['GET'])
def get_coaches_contact():
    return coaches_contact_controller.get_all()

@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['GET'])
def get_coaches_contact_by_id(coaches_contact_id):
    return coaches_contact_controller.get_by_id(coaches_contact_id)

@coaches_contact_bp.route("/coaches_contact", methods=['POST'])
def add_coaches_contact():
    return coaches_contact_controller.create()

@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['PATCH'])
def update_coaches_contact(coaches_contact_id):
    return coaches_contact_controller.update(coaches_contact_id)

@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['DELETE'])
def delete_coaches_contact(coaches_contact_id):
    return coaches_contact_controller.delete(coaches_contact_id)