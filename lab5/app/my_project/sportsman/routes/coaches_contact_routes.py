from flask import Blueprint
from my_project.sportsman.controller.orders.coaches_contact_controller import CoachesContactController
from flask_jwt_extended import jwt_required, get_jwt_identity

coaches_contact_bp = Blueprint("coaches_contact", __name__)
coaches_contact_controller = CoachesContactController()


@coaches_contact_bp.route("/coaches_contact", methods=['GET'])
@jwt_required()
def get_coaches_contact():
    """
    Get all coaches contacts
    ---
    tags:
      - CoachesContact
    security:
      - BearerAuth: []
    responses:
      200:
        description: A list of coaches contacts
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
    return coaches_contact_controller.get_all()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['GET'])
@jwt_required()
def get_coaches_contact_by_id(coaches_contact_id):
    """
    Get a coaches contact by ID
    ---
    tags:
      - CoachesContact
    security:
      - BearerAuth: []
    parameters:
      - name: coaches_contact_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coaches contact found
      401:
        description: Missing or invalid token
      404:
        description: Coaches contact not found
    """
    user_id = get_jwt_identity()
    return coaches_contact_controller.get_by_id(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact", methods=['POST'])
@jwt_required()
def add_coaches_contact():
    """
    Create a new coaches contact
    ---
    tags:
      - CoachesContact
    security:
      - BearerAuth: []
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - phone
            - email
          properties:
            phone:
              type: string
              example: "+123456789"
            email:
              type: string
              example: "coach@email.com"
    responses:
      201:
        description: Coaches contact created
      401:
        description: Missing or invalid token
    """
    user_id = get_jwt_identity()
    return coaches_contact_controller.create()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['PATCH'])
@jwt_required()
def update_coaches_contact(coaches_contact_id):
    """
    Update a coaches contact
    ---
    tags:
      - CoachesContact
    security:
      - BearerAuth: []
    parameters:
      - name: coaches_contact_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            phone:
              type: string
              example: "+987654321"
            email:
              type: string
              example: "newcoach@email.com"
    responses:
      200:
        description: Coaches contact updated
      401:
        description: Missing or invalid token
      404:
        description: Coaches contact not found
    """
    user_id = get_jwt_identity()
    return coaches_contact_controller.update(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['DELETE'])
@jwt_required()
def delete_coaches_contact(coaches_contact_id):
    """
    Delete a coaches contact
    ---
    tags:
      - CoachesContact
    security:
      - BearerAuth: []
    parameters:
      - name: coaches_contact_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coaches contact deleted
      401:
        description: Missing or invalid token
      404:
        description: Coaches contact not found
    """
    user_id = get_jwt_identity()
    return coaches_contact_controller.delete(coaches_contact_id)