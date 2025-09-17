from flask import Blueprint
from my_project.sportsman.controller.orders.sportsman_controller import SportsmanController

sportsman_bp = Blueprint("sportsman", __name__)
sportsman_controller = SportsmanController()

@sportsman_bp.route("/sportsman", methods=['GET'])
def get_sportsmen():
    return sportsman_controller.get_all()

@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['GET'])
def get_sportsman_by_id(sportsman_id):
    return sportsman_controller.get_by_id(sportsman_id)

# Виправлено: маршрут для POST
@sportsman_bp.route("/sportsman", methods=['POST'])
def add_sportsman():
    return sportsman_controller.create()

@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['PATCH'])
def update_sportsmen(sportsman_id):
    return sportsman_controller.update(sportsman_id)

@sportsman_bp.route("/sportsman/<int:sportsman_id>", methods=['DELETE'])
def delete_sportsman(sportsman_id):
    return sportsman_controller.delete(sportsman_id)

@sportsman_bp.route("/sportsman/noname", methods=['POST'])
def insert_nonames():
    return sportsman_controller.insert_noname_rows()
