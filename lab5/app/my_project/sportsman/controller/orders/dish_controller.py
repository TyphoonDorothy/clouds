from ..__init__ import DishService
from ..general_controller import GeneralController
from flask import jsonify, request
from my_project.sportsman.controller.utils import handle_error, handle_response

class DishController(GeneralController):
    def __init__(self):
        super().__init__(DishService())

    def insert_dish(self):
        try:
            data = request.json
            required_fields = ['name', 'calories']

            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400

            self.service.insert_dish(
                name=data['name'],
                calories=data['calories']
            )

            return jsonify({"message": "Dish inserted successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_dish_aggregate(self):
        try:
            operation = request.args.get("operation", "").upper()
            if not operation:
                return handle_error("Operation parameter is required.", 400)

            result = self.service.get_dish_aggregate(operation)
            return handle_response({"operation": operation, "result": result}, 200)

        except ValueError as e:
            return handle_error(str(e), 400)
        except Exception as e:
            return handle_error(f"Unexpected error: {str(e)}", 500)
