from flask import Blueprint, jsonify, request
from sqlalchemy import text
from ..controller.orders.coach_controller import CoachController
from my_project.database import db
from flasgger import swag_from

coach_bp = Blueprint("coach", __name__)
coach_controller = CoachController()

@coach_bp.route("/coach", methods=['GET'])
def get_coach():
    return coach_controller.get_all()

@coach_bp.route("/coach/<int:coach_id>", methods=['GET'])
def get_coach_by_id(coach_id):
    return coach_controller.get_by_id(coach_id)

@coach_bp.route("/coach", methods=['POST'])
@swag_from({
    'tags': ['Add coach'],
    'parameters': [
        {'name': 'id',
         'in': 'path',
         'type': 'integer',
         'required': True,
         'description': 'ID'},
        {'name': 'name',
         'in': 'path',
         'type': 'string',
         'required': True,
         'description': 'First Name'},
        {'name': 'Surname',
         'in': 'path',
         'type': 'string',
         'required': True,
         'description': 'Last Name'},
        {'name': 'specialization_id',
         'in': 'path',
         'type': 'integer',
         'required': True,
         'description': 'specialization_id'},
        {'name': 'contact_id',
         'in': 'path',
         'type': 'integer',
         'required': True,
         'description': 'contact_id'}
    ],
    'responses': {
        200: {
            'description': 'Added a coach'
        }
    }
})
def add_coach():
    return coach_controller.create()

@coach_bp.route("/coach/<int:coach_id>", methods=['PATCH'])
def update_coach(coach_id):
    return coach_controller.update(coach_id)

@coach_bp.route("/coach/<int:coach_id>", methods=['DELETE'])
def delete_coach(coach_id):
    return coach_controller.delete(coach_id)

@coach_bp.route("/coach/insert", methods=['POST'])
def insert_coach():
    try:
        data = request.get_json()
        name = data.get('name')
        surname = data.get('surname')
        specialization_id = data.get('specialization_id')
        contact_id = data.get('contact_id')

        if not name or not surname or not specialization_id or not contact_id:
            return jsonify({"error": "All fields are required."}), 400

        db.session.execute(
            text("""
                CALL insert_into_coach(:name, :surname, :specialization_id, :contact_id)
            """),
            {
                "name": name,
                "surname": surname,
                "specialization_id": specialization_id,
                "contact_id": contact_id,
            }
        )
        db.session.commit()

        return jsonify({"message": "Coach added successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400