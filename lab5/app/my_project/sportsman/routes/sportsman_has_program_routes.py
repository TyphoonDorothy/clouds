from flask import Blueprint
from my_project.sportsman.controller.orders.sportsman_has_program_controller import SportsmanHasProgramController


sportsman_has_program_bp = Blueprint("sportsman_has_program", __name__)
sportsman_has_program_controller = SportsmanHasProgramController()

@sportsman_has_program_bp.route("/sportsman_has_program", methods=['GET'])
def get_sportsmen_has_program():
    return sportsman_has_program_controller.get_all()

@sportsman_has_program_bp.route("/sportsman_has_program/<int:sportsman_has_program_id>", methods=['GET'])
def get_sportsman_has_program_by_id(sportsman_has_program_id):
    return sportsman_has_programt_controller.get_by_id(sportsman_has_program_id)

@sportsman_has_program_bp.route("/sportsman_has_program", methods=['POST'])
def add_sportsman_has_program():
    return sportsman_has_program_controller.create()

@sportsman_has_program_bp.route("/sportsman_has_program/<int:sportsman_has_program_id>", methods=['PATCH'])
def update_sportsman_has_program(sportsman_id):
    return sportsman_has_program_controller.update(sportsman_has_program_id)

@sportsman_has_program_bp.route("/sportsman_has_program/<int:sportsman_has_program_id>", methods=['DELETE'])
def delete_sportsman_has_program(sportsman_has_program_id):
    return sportsman_has_program_controller.delete(sportsman_has_program_id)

@sportsman_has_program_bp.route("/sportsman_has_program/insert", methods=['POST'])
def insert_sportsman_program(sportsman_has_program_id):
    return sportsman_has_program_controller.insert_junction_entry()