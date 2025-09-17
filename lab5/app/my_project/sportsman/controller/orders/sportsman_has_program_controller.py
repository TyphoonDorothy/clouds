from flask import request, jsonify
from my_project.sportsman.controller.general_controller import GeneralController
from my_project.sportsman.controller.__init__ import SportsmanHasProgramService
from my_project.sportsman.controller.utils import handle_error, handle_response


class SportsmanHasProgramController(GeneralController):
    def __init__(self):
        super().__init__(SportsmanHasProgramService())

    def insert_junction_entry(self):
        try:
            data = request.json
            sportsman_id = data.get("sportsman_id")
            program_id = data.get("program_id")

            # Validate input
            if not sportsman_id or not program_id:
                return handle_error("Missing required fields: sportsman_id, program_id.", 400)

            # Call the service
            self.service.insert_sportsman_program(sportsman_id, program_id)

            return handle_response({"message": "Junction entry created successfully."}, 201)
        except ValueError as ve:
            return handle_error(str(ve), 409)  # Business logic errors
        except Exception as e:
            return handle_error(f"Unexpected error: {str(e)}", 500)
