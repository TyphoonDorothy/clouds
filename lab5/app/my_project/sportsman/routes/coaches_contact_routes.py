from flask import Blueprint
from my_project.sportsman.controller.orders.coaches_contact_controller import CoachesContactController

coaches_contact_bp = Blueprint("coaches_contact", __name__)
coaches_contact_controller = CoachesContactController()


@coaches_contact_bp.route("/coaches_contact", methods=['GET'])
def get_coaches_contact():
    """
    Get all coaches contacts
    ---
    tags:
      - CoachesContact
    responses:
      200:
        description: A list of coaches contacts
    """
    return coaches_contact_controller.get_all()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['GET'])
def get_coaches_contact_by_id(coaches_contact_id):
    """
    Get a coaches contact by ID
    ---
    tags:
      - CoachesContact
    parameters:
      - name: coaches_contact_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coaches contact found
      404:
        description: Coaches contact not found
    """
    return coaches_contact_controller.get_by_id(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact", methods=['POST'])
def add_coaches_contact():
    """
    Create a new coaches contact
    ---
    tags:
      - CoachesContact
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
    """
    return coaches_contact_controller.create()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['PATCH'])
def update_coaches_contact(coaches_contact_id):
    """
    Update a coaches contact
    ---
    tags:
      - CoachesContact
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
      404:
        description: Coaches contact not found
    """
    return coaches_contact_controller.update(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['DELETE'])
def delete_coaches_contact(coaches_contact_id):
    """
    Delete a coaches contact
    ---
    tags:
      - CoachesContact
    parameters:
      - name: coaches_contact_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Coaches contact deleted
      404:
        description: Coaches contact not found
    """
    return coaches_contact_controller.delete(coaches_contact_id)
