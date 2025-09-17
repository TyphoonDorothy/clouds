from flask import Blueprint
from my_project.sportsman.controller.orders.sportsman_has_supplement_controller import SportsmanHasSupplementController


sportsman_has_supplement_bp = Blueprint("sportsman_has_supplement", __name__)
sportsman_has_supplement_controller = SportsmanHasSupplementController()

@sportsman_has_supplement_bp.route("/sportsman_has_supplement", methods=['GET'])
def get_sportsmen_has_supplement():
    return sportsman_has_supplement_controller.get_all()

@sportsman_has_supplement_bp.route("/sportsman_has_supplement/<int:sportsman_has_supplement_id>", methods=['GET'])
def get_sportsman_has_supplement_by_id(sportsman_has_supplement_id):
    return sportsman_has_supplement_controller.get_by_id(sportsman_has_supplement_id)

@sportsman_has_supplement_bp.route("/sportsman_has_supplement", methods=['POST'])
def add_sportsman_has_supplement():
    return sportsman_has_supplement_controller.create()

@sportsman_has_supplement_bp.route("/sportsman_has_supplement/<int:sportsman_has_supplement_id>", methods=['PATCH'])
def update_sportsman_has_supplement(sportsman_id):
    return sportsman_has_supplement_controller.update(sportsman_has_supplement_id)

@sportsman_has_supplement_bp.route("/sportsman_has_supplement/<int:sportsman_has_supplement_id>", methods=['DELETE'])
def delete_sportsman_has_supplement(sportsman_has_supplement_id):
    return sportsman_has_supplement_controller.delete(sportsman_has_supplement_id)