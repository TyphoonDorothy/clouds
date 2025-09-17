from flask import Blueprint
from my_project.sportsman.controller.orders.program_controller import ProgramController


program_bp = Blueprint("programs", __name__)
program_controller = ProgramController()

@program_bp.route("/programs", methods=['GET'])
def get_programs():
    return program_controller.get_all()

@program_bp.route("/programs/<int:program_id>", methods=['GET'])
def get_program_by_id(program_id):
    return program_controller.get_by_id(programt_id)

@program_bp.route("/programs", methods=['POST'])
def add_program():
    return program_controller.create()

@program_bp.route("/programs/<int:program_id>", methods=['PATCH'])
def update_program(program_id):
    return program_controller.update(program_id)

@program_bp.route("/programs/<int:program_id>", methods=['DELETE'])
def delete_program(program_id):
    return program_controller.delete(program_id)