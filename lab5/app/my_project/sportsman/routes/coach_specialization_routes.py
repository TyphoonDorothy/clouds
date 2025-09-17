from flask import Blueprint, jsonify
from my_project.sportsman.controller.orders.coach_specialization_controller import CoachSpecializationController


coach_specialization_bp = Blueprint("coach_specialization", __name__)
coach_specialization_controller = CoachSpecializationController()

@coach_specialization_bp.route("/coach_specialization", methods=['GET'])
def get_coach_specialization():
    return coach_specialization_controller.get_all()

@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['GET'])
def get_coach_specialization_by_id(coach_specialization_id):
    return coach_specialization_controller.get_by_id(coach_specialization_id)

@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>/coaches", methods=['GET'])
def get_coaches_by_specialization(specialization_id):
    return jsonify(coach_specialization_controller.service.get_coaches_by_specialization(specialization_id))

@coach_specialization_bp.route("/coach_specialization", methods=['POST'])
def add_coach_specialization():
    return coach_specialization_controller.create()

@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['PATCH'])
def update_coach_specialization(coach_specialization_id):
    return coach_specialization_controller.update(coach_specialization_id)

@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['DELETE'])
def delete_coach_specialization(coachr_specialization_id):
    return coach_specialization_controller.delete(coach_specialization_id)