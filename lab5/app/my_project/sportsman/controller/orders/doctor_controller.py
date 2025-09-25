from flask import jsonify
from my_project.sportsman.controller.general_controller import GeneralController
from my_project.sportsman.controller.utils import handle_response
from my_project.sportsman.controller.__init__ import DoctorService

class DoctorController(GeneralController):
    def __init__(self):
        super().__init__(DoctorService())

    def generate_databases_and_tables(self):
        result = self.service.generate_databases_and_tables()
        if "error" in result:
            return jsonify(result), 500
        return jsonify(result), 200
