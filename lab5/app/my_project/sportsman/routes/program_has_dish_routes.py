from flask import Blueprint
from my_project.sportsman.controller.orders.program_has_dish_controller import ProgramHasDishController


program_has_dish_bp = Blueprint("program_has_dish", __name__)
program_has_dish_controller = ProgramHasDishController()

@program_has_dish_bp.route("/program_has_dish", methods=['GET'])
def get_sportsmen_has_program():
    return program_has_dish_controller.get_all()

@program_has_dish_bp.route("/program_has_dish/<int:program_has_dish_id>", methods=['GET'])
def get_program_has_dish_by_id(program_has_dish_id):
    return program_has_dish_controller.get_by_id(program_has_dish_id)

@program_has_dish_bp.route("/program_has_dish", methods=['POST'])
def add_program_has_dish():
    return program_has_dish_controller.create()

@program_has_dish_bp.route("/program_has_dish/<int:program_has_dish_id>", methods=['PATCH'])
def update_program_has_dish(sportsman_id):
    return program_has_dish_controller.update(program_has_dish_id)

@program_has_dish_bp.route("/program_has_dish/<int:program_has_dish_id>", methods=['DELETE'])
def delete_program_has_dish(program_has_dish_id):
    return program_has_dish_controller.delete(program_has_dish_id)