from flask import Blueprint, jsonify
from my_project.sportsman.controller.orders.coach_specialization_controller import CoachSpecializationController

coach_specialization_bp = Blueprint("coach_specialization", __name__)
coach_specialization_controller = CoachSpecializationController()


@coach_specialization_bp.route("/coach_specialization", methods=['GET'])
def get_coach_specialization():
    """
    Get all coach specializations
    ---
    tags:
      - Coach Specialization
    responses:
      200:
        description: List of coach specializations
    """
    return coach_specialization_controller.get_all()


@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['GET'])
def get_coach_specialization_by_id(coach_specialization_id):
    """
    Get a coach specialization by ID
    ---
    tags:
      - Coach Specialization
    parameters:
      - name: coach_specialization_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Coach specialization details
      404:
        description: Specialization not found
    """
    return coach_specialization_controller.get_by_id(coach_specialization_id)


# @coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>/coaches", methods=['GET'])
# def get_coaches_by_specialization(coach_specialization_id):
#     """
#     Get all coaches for a given specialization
#     ---
#     tags:
#       - Coach Specialization
#     parameters:
#       - name: coach_specialization_id
#         in: path
#         required: true
#         type: integer
#     responses:
#       200:
#         description: List of coaches with this specialization
#     """
#     coaches = coach_specialization_controller.service.get_coaches_by_specialization(coach_specialization_id)
#     return jsonify([c.to_dict() for c in coaches])


@coach_specialization_bp.route("/coach_specialization", methods=['POST'])
def add_coach_specialization():
    """
    Create a new coach specialization
    ---
    tags:
      - Coach Specialization
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
          required:
            - name
    responses:
      201:
        description: Specialization created successfully
      400:
        description: Invalid input
    """
    return coach_specialization_controller.create()


@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['PATCH'])
def update_coach_specialization(coach_specialization_id):
    """
    Update an existing coach specialization
    ---
    tags:
      - Coach Specialization
    parameters:
      - name: coach_specialization_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Specialization updated
      404:
        description: Specialization not found
    """
    return coach_specialization_controller.update(coach_specialization_id)


@coach_specialization_bp.route("/coach_specialization/<int:coach_specialization_id>", methods=['DELETE'])
def delete_coach_specialization(coach_specialization_id):
    """
    Delete a coach specialization
    ---
    tags:
      - Coach Specialization
    parameters:
      - name: coach_specialization_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Specialization deleted
      404:
        description: Specialization not found
    """
    return coach_specialization_controller.delete(coach_specialization_id)
