from flask import Blueprint, jsonify, request
from sqlalchemy import text
from ..controller.orders.coach_controller import CoachController
from my_project.database import db
from flasgger import swag_from
from ..domain.coach import Coach
from flask_jwt_extended import jwt_required, get_jwt_identity

coach_bp = Blueprint("coach", __name__)
coach_controller = CoachController()


@coach_bp.route("/coach", methods=['GET'])
@jwt_required()
def get_coach():
    """
    Get all coaches
    ---
    tags:
      - Coach
    security:
      - BearerAuth: []
    responses:
      200:
        description: List of coaches
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
    return coach_controller.get_all()


@coach_bp.route("/coach/<int:coach_id>", methods=['GET'])
@jwt_required()
def get_coach_by_id(coach_id):
    """
    Get coach by ID
    ---
    tags:
      - Coach
    security:
      - BearerAuth: []
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coach details
      401:
        description: Missing or invalid token
      404:
        description: Coach not found
    """
    user_id = get_jwt_identity()
    return coach_controller.get_by_id(coach_id)


@coach_bp.route("/coach", methods=['POST'])
@jwt_required()
def add_coach():
    """
    Add a new coach
    ---
    tags:
      - Coach
    security:
      - BearerAuth: []
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
      201:
        description: Coach added
      400:
        description: Invalid input
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
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
@jwt_required()
def update_coach(coach_id):
    """
    Update a coach
    ---
    tags:
      - Coach
    security:
      - BearerAuth: []
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            surname:
              type: string
            coach_specialization_id:
              type: integer
            contact_id:
              type: integer
    responses:
      200:
        description: Coach updated
      400:
        description: Invalid input
      401:
        description: Missing or invalid token
      404:
        description: Coach not found
    """
    user_id = get_jwt_identity()
    coach = Coach.query.get(coach_id)
    if not coach:
        return jsonify({"error": "Coach not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update only provided fields (PATCH = partial update)
    if "name" in data:
        coach.name = data["name"]
    if "surname" in data:
        coach.surname = data["surname"]
    if "coach_specialization_id" in data:
        coach.coach_specialization_id = data["coach_specialization_id"]
    if "contact_id" in data:
        coach.contact_id = data["contact_id"]

    db.session.commit()

    return jsonify({"message": "Coach updated", "coach": {
        "id": coach.id,
        "name": coach.name,
        "surname": coach.surname,
        "coach_specialization_id": coach.coach_specialization_id,
        "contact_id": coach.contact_id
    }})


@coach_bp.route("/coach/<int:coach_id>", methods=['DELETE'])
@jwt_required()
def delete_coach(coach_id):
    """
    Delete a coach
    ---
    tags:
      - Coach
    security:
      - BearerAuth: []
    parameters:
      - name: coach_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coach deleted
      401:
        description: Missing or invalid token
      404:
        description: Coach not found
    """
    user_id = get_jwt_identity()
    return coach_controller.delete(coach_id)

