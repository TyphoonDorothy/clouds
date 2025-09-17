from flask import Blueprint
from ..controller.orders.supplement_controller import SupplementController

supplement_bp = Blueprint("supplement", __name__)
supplement_controller = SupplementController()

@supplement_bp.route("/supplement", methods=['GET'])
def get_supplement():
    return supplement_controller.get_all()

@supplement_bp.route("/supplement/<int:supplement_id>", methods=['GET'])
def get_supplement_by_id(supplement_id):
    return supplement_controller.get_by_id(supplement_id)

@supplement_bp.route("/supplement", methods=['POST'])
def add_supplement():
    return supplement_controller.create()

@supplement_bp.route("/supplement/<int:supplement_id>", methods=['PATCH'])
def update_supplement(supplement_id):
    return supplement_controller.update(supplement_id)

@supplement_bp.route("/supplement/<int:supplementh_id>", methods=['DELETE'])
def delete_supplement(supplement_id):
    return supplement_controller.delete(supplement_id)