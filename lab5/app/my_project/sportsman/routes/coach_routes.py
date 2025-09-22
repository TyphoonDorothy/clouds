from flask import Blueprint, jsonify, request
from sqlalchemy import text
from ..controller.orders.coach_controller import CoachController
from my_project.database import db
from flasgger import swag_from

coach_bp = Blueprint("coach", __name__)
coach_controller = CoachController()


@coach_bp.route("/coach", methods=['GET'])
def get_coach():
    """
    Get all coaches
    ---
    tags:
      - Coach
    responses:
      200:
        description: List of coaches
    """
    return coach_controller.get_all()


@coach_bp.route("/coach/<int:coach_id>", methods=['GET'])
def get_coach_by_id(coach_id):
    """
    Get coach by ID
    ---
    tags:
      - Coach
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coach details
    """
    return coach_controller.get_by_id(coach_id)


@coach_bp.route("/coach", methods=['POST'])
def add_coach():
    """
    Add a new coach
    ---
    tags:
      - Coach
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            surname:
              type: string
            coach_specialization_id:
              type: integer
            contact_id:
              type: integer
          required:
            - id
            - name
            - surname
    responses:
      200:
        description: Coach added
    """
    data = request.get_json()
    new_coach = Coach(
        id=data.get("id"),
        name=data.get("name"),
        surname=data.get("surname"),
        coach_specialization_id=data.get("coach_specialization_id"),
        contact_id=data.get("contact_id")
    )
    try:
        db.session.add(new_coach)
        db.session.commit()
        return jsonify({"message": "Coach added", "id": new_coach.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@coach_bp.route("/coach/<int:coach_id>", methods=['PATCH'])
def update_coach(coach_id):
    """
    Update a coach
    ---
    tags:
      - Coach
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coach updated
    """
    return coach_controller.update(coach_id)


@coach_bp.route("/coach/<int:coach_id>", methods=['DELETE'])
def delete_coach(coach_id):
    """
    Delete a coach
    ---
    tags:
      - Coach
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coach deleted
    """
    return coach_controller.delete(coach_id)


# @coach_bp.route("/coach/insert", methods=['POST'])
# def insert_coach():
#     """
#     Insert coach via stored procedure
#     ---
#     tags:
#       - Coach
#     parameters:
#       - in: body
#         name: body
#         required: true
#         schema:
#           type: object
#           properties:
#             name:
#               type: string
#             surname:
#               type: string
#             coach_specialization_id:
#               type: integer
#             contact_id:
#               type: integer
#           required:
#             - name
#             - surname
#             - specialization_id
#             - contact_id
#     responses:
#       201:
#         description: Coach added successfully
#       400:
#         description: Error
#     """
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         surname = data.get('surname')
#         specialization_id = data.get('specialization_id')
#         contact_id = data.get('contact_id')
#
#         if not name or not surname or not specialization_id or not contact_id:
#             return jsonify({"error": "All fields are required."}), 400
#
#         db.session.execute(
#             text("""CALL insert_into_coach(:name, :surname, :specialization_id, :contact_id)"""),
#             {"name": name, "surname": surname, "specialization_id": specialization_id, "contact_id": contact_id}
#         )
#         db.session.commit()
#
#         return jsonify({"message": "Coach added successfully."}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 400
